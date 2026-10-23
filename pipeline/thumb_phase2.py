"""Phase-2 thumbnails, one fixed layout per angle (A 2 things / B vs / C money / D story):
python3 pipeline/thumb_phase2.py 61 62 ... -> agendamento/thumbs/videoNN.jpg (1280x720).
Photos are the video's own Wikimedia Commons media from the deliveries-videoNN branch."""
import io, json, pathlib, re, sys, urllib.request
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/viniciushoscher-ctrl/american-trucks/deliveries-video{n}/deliveries/video{n}/media/{f}"
FONT = str(ROOT / "pipeline/fonts/Anton-Regular.ttf")
W, H = 1280, 720
YEL, RED, BLK, WHT = (255, 221, 0), (220, 20, 30), (0, 0, 0), (255, 255, 255)
# money angle: the price on the tag (only figures quoted in that video's script)
PRICE = {63: "$3.17M", 67: "$665K", 71: "$529K", 75: "$120K", 79: "$450K"}


def themes():
    out = {}
    for line in (ROOT / "plano/new-formats-2027.md").read_text().splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) == 7 and c[0].isdigit():
            m = re.match(r"(.+?)\s*\((.+)\)", c[2])
            out[int(c[0])] = (m.group(1), m.group(2)) if m else (c[2], "")
    return out


def short(name):
    # "Bugatti Chiron" -> "CHIRON", "Ferrari SF90" -> "SF90", "Chevrolet Corvette Z06" -> "CORVETTE Z06"
    w = name.split()
    return " ".join(w[1:] if len(w) > 1 else w).upper()


def photo(n, scene, cut=0):
    data = urllib.request.urlopen(RAW.format(n=n, f=f"{scene}_{cut}.jpg"), timeout=60).read()
    return Image.open(io.BytesIO(data)).convert("RGB")


def fit(im, w, h):
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.55))


def text(d, xy, s, size, fill=YEL, anchor="la", stroke=8):
    f = ImageFont.truetype(FONT, size)
    d.text(xy, s, font=f, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=BLK)
    return f


def fit_size(s, max_w, size):
    while size > 30 and ImageFont.truetype(FONT, size).getlength(s) > max_w:
        size -= 4
    return size


def scene_for(sj, words):
    for i, s in enumerate(sj["scenes"]):
        if any(w.lower() in s["query"].lower() for w in words):
            return i
    return 0


def layout_a(n, sj, model):
    im = fit(photo(n, 0), W, H)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    d = ImageDraw.Draw(im)
    # dark left gradient so the "2" pops
    g = Image.new("L", (W, H))
    gd = ImageDraw.Draw(g)
    for x in range(W // 2):
        gd.line([(x, 0), (x, H)], fill=int(200 * (1 - x / (W / 2))))
    im.paste(Image.new("RGB", (W, H), BLK), (0, 0), g)
    d = ImageDraw.Draw(im)
    text(d, (40, 360), "2", 560, YEL, "lm", 12)
    text(d, (350, 230), "THINGS YOU", fit_size("THINGS YOU", 520, 120), WHT, "lm")
    text(d, (350, 360), "DIDN'T KNOW", fit_size("DIDN'T KNOW", 560, 120), WHT, "lm")
    name = short(model)
    text(d, (W - 40, H - 40), name, fit_size(name, 700, 130), YEL, "rd")
    return im


def layout_b(n, sj, model, rival):
    left = fit(photo(n, scene_for(sj, [model])), W // 2, H)
    right = fit(photo(n, scene_for(sj, [rival.split()[-1], rival])), W // 2, H)
    im = Image.new("RGB", (W, H))
    im.paste(left, (0, 0))
    im.paste(right, (W // 2, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([W // 2 - 6, 0, W // 2 + 6, H], fill=WHT)
    d.rectangle([0, H - 150, W, H], fill=BLK)
    a, b = short(model), short(rival)
    text(d, (W // 4, H - 75), a, fit_size(a, 560, 110), YEL, "mm", 6)
    text(d, (3 * W // 4, H - 75), b, fit_size(b, 560, 110), YEL, "mm", 6)
    d.ellipse([W // 2 - 120, 170, W // 2 + 120, 410], fill=RED, outline=WHT, width=10)
    text(d, (W // 2, 290), "VS", 150, WHT, "mm", 6)
    return im


def layout_c(n, sj, model):
    im = fit(photo(n, 0), W, H)
    im = ImageEnhance.Contrast(im).enhance(1.1)
    d = ImageDraw.Draw(im)
    price = PRICE.get(n, "$$$")
    # price tag: rotated red label with a hole
    tag = Image.new("RGBA", (620, 300), (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.polygon([(90, 0), (620, 0), (620, 300), (90, 300), (0, 150)], fill=RED + (255,), outline=WHT)
    td.ellipse([40, 125, 90, 175], fill=WHT)
    f = ImageFont.truetype(FONT, fit_size(price, 470, 210))
    td.text((360, 150), price, font=f, fill=WHT, anchor="mm", stroke_width=6, stroke_fill=BLK)
    tag = tag.rotate(8, expand=True, resample=Image.BICUBIC)
    im.paste(tag, (40, 40), tag)
    d = ImageDraw.Draw(im)
    d.rectangle([0, H - 170, W, H], fill=BLK)
    line = f"REAL COST OF A {short(model)}"
    text(d, (W // 2, H - 85), line, fit_size(line, 1180, 120), YEL, "mm", 6)
    return im


def layout_d(n, sj, model):
    old = fit(photo(n, 0, 1), W // 2, H)
    old = ImageOps.colorize(ImageOps.grayscale(old), (40, 25, 10), (240, 220, 180))
    old = old.filter(ImageFilter.GaussianBlur(0.6))
    new = fit(photo(n, len(sj["scenes"]) - 1), W // 2, H)
    new = ImageEnhance.Color(new).enhance(1.3)
    im = Image.new("RGB", (W, H))
    im.paste(old, (0, 0))
    im.paste(new, (W // 2, 0))
    d = ImageDraw.Draw(im)
    d.polygon([(W // 2 - 30, 0), (W // 2 + 30, 0), (W // 2 + 30, H), (W // 2 - 30, H)], fill=YEL)
    d.rectangle([0, 0, W, 160], fill=BLK)
    text(d, (W // 2, 80), "THE INSANE STORY", fit_size("THE INSANE STORY", 1150, 130), YEL, "mm", 6)
    name = short(model)
    text(d, (W // 2, H - 60), name, fit_size(name, 1000, 140), WHT, "mm", 10)
    return im


def build(n, th):
    sj = json.load(open(ROOT / "videos" / f"video{n}" / "script.json"))
    model, rival = th[(n - 61) // 4 + 1]
    a = sj["angle"]
    im = {"A": lambda: layout_a(n, sj, model), "B": lambda: layout_b(n, sj, model, rival),
          "C": lambda: layout_c(n, sj, model), "D": lambda: layout_d(n, sj, model)}[a]()
    out = ROOT / "agendamento/thumbs" / f"video{n}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out, quality=90)
    print(out.name, a, model)


if __name__ == "__main__":
    th = themes()
    for x in sys.argv[1:]:
        build(int(x), th)
