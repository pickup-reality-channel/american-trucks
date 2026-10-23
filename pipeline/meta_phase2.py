"""Phase-2 metadata: python3 pipeline/meta_phase2.py 61 62 ...
Reads videos/videoNN/script.json + sources.md, pulls chapters/credits/shorts from the deliveries-videoNN branch,
and writes agendamento/meta/videoNN.json and agendamento/creditos/videoNN.md (same format as phase 1)."""
import html, json, pathlib, re, sys, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/viniciushoscher-ctrl/american-trucks/deliveries-video{n}/deliveries/video{n}/{f}"
EBOOK = "Get the 2027 Truck Buyer's Guide: [LINK HERE]"
CREDITS = "https://github.com/viniciushoscher-ctrl/american-trucks/blob/main/agendamento/creditos/video{n}.md"


def raw(n, f):
    return urllib.request.urlopen(RAW.format(n=n, f=f), timeout=60).read().decode()


def themes():
    # day table in the plan: | day | date | Theme (Rival) | A | B | C | D |
    out = {}
    for line in (ROOT / "plano/new-formats-2027.md").read_text().splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 7 and c[0].isdigit():
            m = re.match(r"(.+?)\s*\((.+)\)", c[2])
            out[int(c[0])] = (m.group(1), m.group(2)) if m else (c[2], "")
    return out



def build(n, th):
    vid = f"video{n}"
    d = ROOT / "videos" / vid
    sj = json.load(open(d / "script.json"))
    sources = (d / "sources.md").read_text().strip()
    chapters = raw(n, "chapters.txt").strip()
    credits = json.loads(raw(n, "credits.json"))
    shorts_md = raw(n, "shorts/shorts.md")
    model, rival = th[(n - 61) // 4 + 1]
    hook = " ".join(s["text"] for s in sj["scenes"][:2])
    desc = (f"{hook}\n\nEvery figure in this video comes from a published source, listed below.\n\n{EBOOK}\n\n"
            f"Chapters:\n{chapters}\n\nSources:\n{sources}\n\nFull sources and photo credits: {CREDITS.format(n=n)}")
    brand = model.split()[0]
    tags = [model, brand, "supercars", "exotic cars", "Pickup Reality"] + ([rival] if rival and sj["angle"] == "B" else [])
    # shorts.md blocks: "shortK.mp4 (..s)\nTitle: <chapter>: ...\nDescription: <caption>. ..."
    shorts = []
    for b in re.split(r"\n\s*\n", shorts_md.strip()):
        f = re.match(r"(short\d+\.mp4)", b)
        t = re.search(r"Title: (.+?): The Real Numbers", b)
        cap = re.search(r"Description: (.+?)\. Full video", b)
        if not f:
            continue
        chap = t.group(1) if t else ""
        if f.group(1) == "short1.mp4" or not chap or chap.lower() == "intro":
            title = f"{sj['title']} #Shorts"
        else:
            title = f"{model}: {chap} #Shorts"
        hint = cap.group(1).title() if cap else chap
        shorts.append({"file": f.group(1), "title": title,
                       "description": f"{model}, {hint.lower()}. Full video on the Pickup Reality channel. {EBOOK}"})
    meta = {"video": n, "title": sj["title"], "description": desc, "tags": tags, "shorts": shorts}
    (ROOT / "agendamento/meta" / f"{vid}.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n")
    seen, lines = set(), []
    for c in credits:
        t = c["title"].replace("File:", "")
        if t in seen:
            continue
        seen.add(t)
        a = html.unescape(re.sub("<[^>]+>", "", c.get("artist", "") or "")).strip()
        lines.append(f"- {t} by {a or 'unknown'}, {c.get('license', '')}")
    (ROOT / "agendamento/creditos" / f"{vid}.md").write_text(
        f"# Photo credits: {sj['title']}\n\n" + "\n".join(lines) + f"\n\n## Sources\n\n{sources}\n")
    print(vid, len(desc), "chars,", len(shorts), "shorts,", len(lines), "photos")
    if len(desc) > 5000:
        raise SystemExit(f"{vid}: description over YouTube's 5000-character limit")


if __name__ == "__main__":
    th = themes()
    for a in sys.argv[1:]:
        build(int(a), th)
