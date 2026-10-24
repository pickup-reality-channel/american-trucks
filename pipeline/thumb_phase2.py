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
PRICE = {63: "$3.17M", 67: "$665K", 71: "$529K", 75: "$120K", 79: "$450K", 83: "$20.5M", 87: "$2.3M", 91: "$2.19M", 95: "$294K", 99: "$277K", 103: "$2.7M", 107: "$890K", 111: "$1M+", 115: "$3.9M", 119: "$885K", 123: "$175K"}


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


def glow(im, xy, s, size, color=YEL, anchor="la", radius=18):
    # soft coloured halo under the text so it pops on busy photos
    f = ImageFont.truetype(FONT, size)
    layer = Image.new("RGB", im.size, BLK)
    ImageDraw.Draw(layer).text(xy, s, font=f, fill=color, anchor=anchor, stroke_width=14)
    layer = layer.filter(ImageFilter.GaussianBlur(radius))
    return Image.blend(im, Image.composite(layer, im, layer.convert("L").point(lambda v: min(255, v * 2))), 0.55)


def finish(im):
    # punchy grade: more colour and contrast, sharper, dark vignette, thin yellow frame
    im = ImageEnhance.Color(im).enhance(1.3)
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=3))
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse([-W * 0.25, -H * 0.35, W * 1.25, H * 1.35], fill=255)
    v = v.filter(ImageFilter.GaussianBlur(120))
    im = Image.composite(im, ImageEnhance.Brightness(im).enhance(0.45), v)
    ImageDraw.Draw(im).rectangle([0, 0, W - 1, H - 1], outline=YEL, width=8)
    return im


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
    g = Image.new("L", (W, H))
    gd = ImageDraw.Draw(g)
    for x in range(int(W * 0.62)):
        gd.line([(x, 0), (x, H)], fill=int(235 * (1 - x / (W * 0.62))))
    im.paste(Image.new("RGB", (W, H), BLK), (0, 0), g)
    im = glow(im, (30, 340), "2", 600, YEL, "lm", 28)
    d = ImageDraw.Draw(im)
    text(d, (30, 340), "2", 600, YEL, "lm", 14)
    text(d, (355, 200), "THINGS YOU", fit_size("THINGS YOU", 560, 130), WHT, "lm", 9)
    text(d, (355, 340), "DIDN'T KNOW", fit_size("DIDN'T KNOW", 620, 130), WHT, "lm", 9)
    # red plate with the model
    name = short(model)
    fs = fit_size(name, 640, 120)
    plate_w = int(ImageFont.truetype(FONT, fs).getlength(name)) + 90
    d.polygon([(W - plate_w - 40, H - 190), (W - 20, H - 210), (W - 20, H - 40), (W - plate_w - 60, H - 20)], fill=RED, outline=WHT)
    text(d, (W - 20 - plate_w // 2 - 10, H - 115), name, fs, WHT, "mm", 6)
    return im


def layout_b(n, sj, model, rival):
    left = fit(photo(n, scene_for(sj, [model])), W // 2 + 60, H)
    right = fit(photo(n, scene_for(sj, [rival.split()[-1], rival])), W // 2 + 60, H)
    im = Image.new("RGB", (W, H))
    im.paste(left, (0, 0))
    m = Image.new("L", (W // 2 + 60, H), 0)
    ImageDraw.Draw(m).polygon([(60, 0), (W // 2 + 60, 0), (W // 2 + 60, H), (0, H)], fill=255)
    im.paste(right, (W // 2 - 60, 0), m)
    d = ImageDraw.Draw(im)
    d.line([(W // 2 + 30, 0), (W // 2 - 30, H)], fill=WHT, width=14)
    d.rectangle([0, H - 150, W, H], fill=BLK)
    d.rectangle([0, H - 156, W, H - 150], fill=YEL)
    a, b = short(model), short(rival)
    text(d, (W // 4, H - 75), a, fit_size(a, 560, 115), YEL, "mm", 6)
    text(d, (3 * W // 4, H - 75), b, fit_size(b, 560, 115), YEL, "mm", 6)
    im = glow(im, (W // 2, 270), "VS", 190, RED, "mm", 22)
    d = ImageDraw.Draw(im)
    d.ellipse([W // 2 - 130, 150, W // 2 + 130, 390], fill=RED, outline=WHT, width=12)
    text(d, (W // 2, 272), "VS", 170, WHT, "mm", 8)
    return im


def layout_c(n, sj, model):
    im = fit(photo(n, 0), W, H)
    price = PRICE.get(n, "$$$")
    tag = Image.new("RGBA", (680, 330), (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.polygon([(100, 0), (680, 0), (680, 330), (100, 330), (0, 165)], fill=RED + (255,), outline=WHT)
    td.polygon([(110, 12), (668, 12), (668, 318), (110, 318), (18, 165)], outline=YEL, width=5)
    td.ellipse([45, 138, 95, 188], fill=WHT)
    f = ImageFont.truetype(FONT, fit_size(price, 520, 240))
    td.text((395, 165), price, font=f, fill=WHT, anchor="mm", stroke_width=7, stroke_fill=BLK)
    tag = tag.rotate(8, expand=True, resample=Image.BICUBIC)
    shadow = Image.new("RGBA", tag.size, (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", tag.size, (0, 0, 0, 170)), (0, 0), tag)
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    im.paste(shadow, (50, 58), shadow)
    im.paste(tag, (36, 36), tag)
    d = ImageDraw.Draw(im)
    d.rectangle([0, H - 170, W, H], fill=BLK)
    d.rectangle([0, H - 176, W, H - 170], fill=RED)
    line = f"REAL COST OF A {short(model)}"
    text(d, (W // 2, H - 85), line, fit_size(line, 1180, 125), YEL, "mm", 6)
    return im


def layout_d(n, sj, model):
    old = fit(photo(n, 0, 1), W // 2 + 40, H)
    old = ImageOps.colorize(ImageOps.grayscale(old), (40, 25, 10), (245, 225, 185))
    new = fit(photo(n, len(sj["scenes"]) - 1), W // 2 + 40, H)
    new = ImageEnhance.Color(new).enhance(1.35)
    im = Image.new("RGB", (W, H))
    im.paste(old, (0, 0))
    m = Image.new("L", (W // 2 + 40, H), 0)
    ImageDraw.Draw(m).polygon([(50, 0), (W // 2 + 40, 0), (W // 2 + 40, H), (0, H)], fill=255)
    im.paste(new, (W // 2 - 40, 0), m)
    d = ImageDraw.Draw(im)
    d.line([(W // 2 + 25, 0), (W // 2 - 25, H)], fill=YEL, width=16)
    d.rectangle([0, 0, W, 165], fill=RED)
    d.rectangle([0, 165, W, 173], fill=YEL)
    text(d, (W // 2, 84), "THE INSANE STORY", fit_size("THE INSANE STORY", 1150, 140), WHT, "mm", 8)
    name = short(model)
    d.rectangle([0, H - 150, W, H], fill=BLK)
    d.rectangle([0, H - 156, W, H - 150], fill=YEL)
    text(d, (W // 2, H - 75), name, fit_size(name, 1100, 120), YEL, "mm", 6)
    return im


def build(n, th):
    sj = json.load(open(ROOT / "videos" / f"video{n}" / "script.json"))
    model, rival = th[(n - 61) // 4 + 1]
    a = sj["angle"]
    im = {"A": lambda: layout_a(n, sj, model), "B": lambda: layout_b(n, sj, model, rival),
          "C": lambda: layout_c(n, sj, model), "D": lambda: layout_d(n, sj, model)}[a]()
    im = finish(im.convert("RGB"))
    out = ROOT / "agendamento/thumbs" / f"video{n}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(out, quality=90)
    print(out.name, a, model)


if __name__ == "__main__":
    th = themes()
    for x in sys.argv[1:]:
        build(int(x), th)
