"""Narration (Piper) -> Ken Burns scenes (ffmpeg) -> captions burned in LAST. Outputs video, .srt, credits."""
import json, sys, pathlib, subprocess, wave, re, os
from concurrent.futures import ThreadPoolExecutor

W, H, FPS = 1920, 1080, 30
MODEL = os.environ.get("PIPER_MODEL", "voices/en_US-ryan-high.onnx")


def run(*a, **k):
    subprocess.run(a, check=True, **k)


def wav_len(p):
    with wave.open(str(p)) as w:
        return w.getnframes() / w.getframerate()


def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int((s % 1) * 1000):03}"


def chunks(text, n=7):
    """Caption chunks that end at punctuation when possible, at most n words."""
    out, cur = [], []
    for w in text.split():
        cur.append(w)
        if len(cur) >= n or (w[-1] in ".,?!:" and len(cur) >= 3):
            out.append(" ".join(cur)); cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def tts(job):
    i, s, out = job
    wav = out / f"{i}.wav"
    run("piper", "--model", MODEL, "--output_file", str(wav), input=s["text"].encode())
    return wav_len(wav) + 0.35


def render_segment(job):
    i, s, d, out, dur = job
    frames = int(dur * FPS)
    zoom = f"zoompan=z='1+0.0006*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}"
    cap = s["caption"].replace("'", "").replace(":", " -")
    label = (f"drawtext=text='{cap}':fontcolor=white:fontsize=56:borderw=4:bordercolor=black:"
             f"box=1:boxcolor=0xC8102E@0.9:boxborderw=18:x=60:y=60")
    run("ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(d / "media" / f"{i}.jpg"), "-i", str(out / f"{i}.wav"),
        "-vf", f"scale=2880:-1,{zoom},{label},format=yuv420p", "-t", f"{dur:.2f}",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), "-c:a", "aac", "-shortest", str(out / f"{i}.mp4"))


def main(video):
    d = pathlib.Path("videos") / video
    out = d / "out"; out.mkdir(exist_ok=True)
    scenes = json.loads((d / "script.json").read_text())["scenes"]
    with ThreadPoolExecutor(4) as ex:
        durs = list(ex.map(tts, [(i, s, out) for i, s in enumerate(scenes)]))
    srt, t0, chapters = [], 0.0, []
    for s, dur in zip(scenes, durs):
        if s.get("chapter"):
            chapters.append(f"{int(t0//60)}:{int(t0%60):02d} {s['chapter']}")
        cs = chunks(s["text"]); step = (dur - 0.35) / len(cs)
        for j, c in enumerate(cs):
            srt.append(f"{len(srt)+1}\n{ts(t0 + j*step)} --> {ts(t0 + (j+1)*step)}\n{c}\n")
        t0 += dur
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(render_segment, [(i, s, d, out, dur) for i, (s, dur) in enumerate(zip(scenes, durs))]))
    (out / "list.txt").write_text("".join(f"file '{i}.mp4'\n" for i in range(len(scenes))))
    (out / "captions.srt").write_text("\n".join(srt))
    (out / "chapters.txt").write_text("\n".join(chapters) + "\n")
    nocap = out / "nocaps.mp4"
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / "list.txt"), "-c", "copy", str(nocap))
    style = "FontName=DejaVu Sans,Bold=1,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=40"
    final = out / f"{video}.mp4"
    # captions last; slideshow content compresses well, so crf 27 keeps a 23 min video near 150 MB
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(nocap), "-vf", f"subtitles={out/'captions.srt'}:force_style='{style}'",
        "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "27", "-c:a", "aac", "-b:a", "96k", str(final))
    # small preview + frames so the result can be reviewed without downloading the full file
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "scale=640:360", "-c:v", "libx264", "-preset", "veryfast",
        "-b:v", "250k", "-c:a", "aac", "-b:a", "48k", str(out / "preview.mp4"))
    total = sum(durs)
    for k, t in enumerate([20, total * 0.25, total * 0.5, total * 0.75, total - 20]):
        run("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.1f}", "-i", str(final), "-frames:v", "1", "-vf", "scale=960:-1", str(out / f"frame{k}.jpg"))
    print("done", final, f"{total/60:.1f} min")


if __name__ == "__main__":
    main(sys.argv[1])
