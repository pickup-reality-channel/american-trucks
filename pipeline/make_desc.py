import json,re,sys,html
v=sys.argv[1]; d="/mnt/project-files/entregas/"+v
sj=json.load(open(f"/home/claude/american-trucks/videos/{v}/script.json"))
ch=open(d+"/chapters.txt").read().strip()
cr=json.load(open(d+"/credits.json"))
sents=re.split(r'(?<=[.?!])\s+',sj["scenes"][0]["text"])
intro=sj["scenes"][0]["text"]
import os
sf=f"/home/claude/american-trucks/videos/{v}/sources.txt"
src=open(sf).read().strip() if os.path.exists(sf) else next((s["text"] for s in sj["scenes"][:6] if re.search(r"\bsources?\b|We used|we used",s["text"])),"")
seen=set();lines=[]
for c in cr:
    t=c["title"].replace("File:","")
    if t in seen: continue
    seen.add(t)
    a=html.unescape(re.sub("<[^>]+>","",c.get("artist","") or "")).strip()
    lines.append(f"- {t} by {a or 'unknown'}, {c.get('license','')}")
out=f"""# {v}: delivery (Pickup Reality)

**Title:** {sj['title']}

## Description (paste on YouTube)
{intro}

Get the 2027 Truck Buyer's Guide: [LINK HERE]

Chapters:
{ch}

Sources:
{src}

Photos from Wikimedia Commons (credits):
"""+"\n".join(lines)+"\n"
open(d+"/titulo-e-descricao.md","w").write(out);print(sj['title'])
