"""Download one real photo per scene from Wikimedia Commons and record its license/credit."""
import json, sys, pathlib, requests

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "american-trucks-channel/1.0 (github.com/viniciushoscher-ctrl/american-trucks)"}


def pick(query, used):
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 25,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1920,
    }
    pages = requests.get(API, params=params, headers=HEADERS, timeout=60).json().get("query", {}).get("pages", {})
    for p in sorted(pages.values(), key=lambda x: x.get("index", 0)):
        info = (p.get("imageinfo") or [{}])[0]
        if info.get("mime") != "image/jpeg" or info.get("width", 0) < 2000:
            continue
        if info["width"] < info.get("height", 0) * 1.3 or p["title"] in used:
            continue
        meta = info.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if not lic.startswith(("CC", "Public domain", "PD")):
            continue
        artist = meta.get("Artist", {}).get("value", "unknown")
        return {"title": p["title"], "url": info["thumburl"], "page": info["descriptionurl"],
                "license": lic, "artist": artist}
    return None


def main(video):
    d = pathlib.Path("videos") / video
    script = json.loads((d / "script.json").read_text())
    (d / "media").mkdir(exist_ok=True)
    used, credits = set(), []
    for i, s in enumerate(script["scenes"]):
        m = pick(s["query"], used)
        if m is None:  # nothing new for this query: reuse the previous scene's photo
            m = dict(credits[-1]); print(i, "reuse", m["title"])
            (d / "media" / f"{i}.jpg").write_bytes((d / "media" / f"{i-1}.jpg").read_bytes())
        else:
            used.add(m["title"])
            (d / "media" / f"{i}.jpg").write_bytes(requests.get(m["url"], headers=HEADERS, timeout=120).content)
            print(i, m["title"], m["license"])
        credits.append({**m, "scene": i})
    (d / "credits.json").write_text(json.dumps(credits, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
