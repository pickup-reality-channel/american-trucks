"""Narration (Piper) -> Ken Burns scenes (ffmpeg) -> captions burned in LAST. Outputs video, .srt, credits."""
import json, sys, pathlib, subprocess, wave, re, os

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


def main(video):
    d = pathlib.Path("videos") / video
    out = d / "out"; out.mkdir(exist_ok=True)
    scenes = json.loads((d / "script.json").read_text())["scenes"]
    parts, srt, t0 = [], [], 0.0
    for i, s in enumerate(scenes):
        wav = out / f"{i}.wav"
        run("piper", "--model", MODEL, "--output_file", str(wav), input=s["text"].encode())
        dur = wav_len(wav) + 0.35
        frames = int(dur * FPS)
        zoom = f"zoompan=z='1+0.0006*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}"
        cap = s["caption"].replace("'", "").replace(":", " -")
        label = (f"drawtext=text='{cap}':fontcolor=white:fontsize=56:borderw=4:bordercolor=black:"
                 f"box=1:boxcolor=0xC8102E@0.9:boxborderw=18:x=60:y=60")
        seg = out / f"{i}.mp4"
        run("ffmpeg", "-y", "-loop", "1", "-i", str(d / "media" / f"{i}.jpg"), "-i", str(wav),
            "-vf", f"scale=3840:-1,{zoom},{label},format=yuv420p", "-t", f"{dur:.2f}",
            "-c:v", "libx264", "-r", str(FPS), "-c:a", "aac", "-shortest", str(seg))
        cs = chunks(s["text"]); step = (dur - 0.35) / len(cs)
        for j, c in enumerate(cs):
            srt.append(f"{len(srt)+1}\n{ts(t0 + j*step)} --> {ts(t0 + (j+1)*step)}\n{c}\n")
        t0 += dur; parts.append(seg)
    (out / "list.txt").write_text("".join(f"file '{p.name}'\n" for p in parts))
    (out / "captions.srt").write_text("\n".join(srt))
    nocap = out / "nocaps.mp4"
    run("ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(out / "list.txt"), "-c", "copy", str(nocap))
    style = "FontName=DejaVu Sans,Bold=1,FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Alignment=2,MarginV=40"
    run("ffmpeg", "-y", "-i", str(nocap), "-vf", f"subtitles={out/'captions.srt'}:force_style='{style}'",
        "-c:a", "copy", str(out / f"{video}.mp4"))
    print("done", out / f"{video}.mp4")


if __name__ == "__main__":
    main(sys.argv[1])
