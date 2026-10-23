"""Find car/truck videos that blew up on YouTube in the US in the last N days (read-only research).
usage: yt_trends.py [days]
Secrets: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN. Cost: ~100 units per query + 1 per 50 stats.
Writes research/trends/latest.json and latest.md (sorted by views per day)."""
import datetime as dt, json, pathlib, sys, requests
from yt_upload import token

API = "https://www.googleapis.com/youtube/v3"
QUERIES = ["car", "truck", "pickup truck", "supercar", "cars", "ford", "tesla", "chevy", "toyota", "car crash"]
OUT = pathlib.Path("research/trends")


def get(path, h, **params):
    r = requests.get(f"{API}/{path}", headers=h, params=params, timeout=60)
    if not r.ok:
        print(f"{path} {params.get('q', '')}: {r.status_code} {r.text[:300]}")
        return {}
    return r.json()


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    h = {"Authorization": f"Bearer {token()}"}
    now = dt.datetime.now(dt.timezone.utc)
    after = (now - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    found = {}
    # Autos & Vehicles chart (US) plus keyword searches, long and Shorts
    d = get("videos", h, part="id", chart="mostPopular", regionCode="US", videoCategoryId="2", maxResults=50)
    for it in d.get("items", []): found.setdefault(it["id"], "chart:autos")
    for q in QUERIES:
        for cat in ["2", None]:
            p = dict(part="id", q=q, type="video", order="viewCount", publishedAfter=after, regionCode="US",
                     relevanceLanguage="en", maxResults=50)
            if cat: p["videoCategoryId"] = cat
            for it in get("search", h, **p).get("items", []):
                found.setdefault(it["id"]["videoId"], f"search:{q}{'/autos' if cat else ''}")
    ids, rows = list(found), []
    for i in range(0, len(ids), 50):
        d = get("videos", h, part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]))
        for v in d.get("items", []):
            s, st = v["snippet"], v.get("statistics", {})
            pub = dt.datetime.fromisoformat(s["publishedAt"].replace("Z", "+00:00"))
            age = max((now - pub).total_seconds() / 86400, 0.1)
            views = int(st.get("viewCount", 0))
            rows.append({"id": v["id"], "url": f"https://www.youtube.com/watch?v={v['id']}", "title": s["title"],
                         "channel": s["channelTitle"], "published": s["publishedAt"], "age_days": round(age, 1),
                         "views": views, "views_per_day": int(views / age), "likes": int(st.get("likeCount", 0)),
                         "comments": int(st.get("commentCount", 0)), "duration": v["contentDetails"]["duration"],
                         "category": s.get("categoryId"), "lang": s.get("defaultAudioLanguage") or s.get("defaultLanguage"),
                         "source": found[v["id"]]})
    rows = [r for r in rows if r["age_days"] <= days + 0.5]
    rows.sort(key=lambda r: -r["views"])
    OUT.mkdir(parents=True, exist_ok=True)
    meta = {"generated_utc": now.isoformat(timespec="seconds"), "window_days": days, "count": len(rows)}
    (OUT / "latest.json").write_text(json.dumps({"meta": meta, "videos": rows}, indent=1, ensure_ascii=False))
    md = [f"# YouTube car/truck videos, US, last {days} days (pulled {meta['generated_utc']})", "",
          "| views | age (d) | views/day | duration | channel | title | source |", "|---|---|---|---|---|---|---|"]
    for r in rows[:150]:
        md.append(f"| {r['views']:,} | {r['age_days']} | {r['views_per_day']:,} | {r['duration']} | {r['channel']} | "
                  f"[{r['title'].replace('|', '/')}]({r['url']}) | {r['source']} |")
    (OUT / "latest.md").write_text("\n".join(md) + "\n")
    print(f"{len(rows)} videos; top 10:")
    for r in rows[:10]: print(f"{r['views']:>12,} {r['age_days']:>5}d {r['channel']}: {r['title']}")


if __name__ == "__main__":
    main()
