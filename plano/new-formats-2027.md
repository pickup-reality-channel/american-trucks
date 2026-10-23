# Pickup Reality — Phase 2: 4 daily angles on exotic cars (from Feb 2027)

Status: **DRAFT, waiting for Vinicius's approval.** Nothing will be rendered until it is approved.

## 1. Where we are

- 58 long videos are uploaded and scheduled through the API (`agendamento/youtube-state.json`). The last long goes out on **Thu 11/02/2027**. Videos 39 and 40 are still in production.
- Shorts are scheduled at 17:00 and 21:00 BRT every day until **11/03/2027** (`agendamento/shorts-schedule.csv`).
- Long-video mp4 copies in the project folder were cleared to free space (the GitHub Releases `videoNN` stay the source of truth). Shorts were kept.

## 2. The idea in one line

Every day has **one theme** (one exotic car, plus a rival). That theme is published as **4 separate videos**, each from a totally different angle, each with its own title formula and its own thumbnail layout. The viewer who liked one angle gets three more on the same car, and the end screen of each one links the other three.

## 3. The 4 angles

| | Angle | Title formula | Thumbnail layout | What the video covers |
|---|---|---|---|---|
| **A** | Hidden facts | `2 Things You Didn't Know About the [Model]` | Huge yellow **"2"** + the car, one detail circled in red | Two little-known, verifiable facts, each told as a mini-story with a twist. The rest of the video builds up to them. |
| **B** | Head to head | `[Model] vs [Rival]: The Difference Nobody Explains` | Split screen, both cars facing each other, red **VS** in the middle | Engineering, performance, price, who buys each one, and the one difference that actually matters. |
| **C** | Money | `What It Really Costs to Own a [Model]` | The car + a big red price tag / dollar stack | US MSRP, options, insurance, tires, service intervals, depreciation, resale. Only published, sourced numbers. |
| **D** | The story | `The Insane Story Behind the [Model]` | Old archive photo (sepia) next to the modern car | Who made it, why, what went wrong, what nearly killed the project, and where it is today. |

Rotating title variants (so the channel doesn't look repetitive, same promise each time):
- A: `2 Secrets Hidden Inside the [Model]` · `The [Model] Has 2 Secrets Most Owners Never Notice`
- B: `[Model] or [Rival]? The Real Difference` · `Why the [Model] Beats the [Rival] (And Where It Loses)`
- C: `The Real Cost of a [Model] (Insurance, Tires, Service)` · `Can a Normal Person Afford a [Model]?`
- D: `Why the [Model] Almost Never Happened` · `The Man Who Built the [Model]`

Title rules (same as phase 1): curiosity first, 50–70 characters, the model name always in the title, **strictly factual** (if the claim in the title is not in the sources, the title changes, not the facts).

## 4. Length and slots

- Each of the 4 videos: **10–12 minutes** (above 8 min, so mid-roll ads work). Four 20+ minute videos per day on the same car would repeat itself and would take 4x the render time.
- Posting times (BRT): **A 10:00 · B 13:00 · C 16:00 · D 19:00**. Shorts stay at 17:00 and 21:00.
- Proposed start: **Fri 12/02/2027**, the day after the last long video, so the channel never has a day without long content. (Vinicius wrote "28 de 2027"; if he means 28/02/2027, the channel would have 16 days with only Shorts. See open questions.)
- First batch = 30 days × 4 = **120 videos**, from 12/02 to 13/03/2027.

## 5. First batch: 30 themes (120 titles)

| Day | Date | Theme (rival) | A — 2 things | B — vs | C — money | D — story |
|---|---|---|---|---|---|---|
| 1 | 12/02 | Bugatti Chiron (Koenigsegg Jesko) | 2 Things You Didn't Know About the Bugatti Chiron | Bugatti Chiron vs Koenigsegg Jesko: The Difference Nobody Explains | What It Really Costs to Own a Bugatti Chiron | The Insane Story Behind the Bugatti Chiron |
| 2 | 13/02 | Lamborghini Revuelto (Ferrari 12Cilindri) | 2 Secrets Hidden Inside the Lamborghini Revuelto | Lamborghini Revuelto or Ferrari 12Cilindri? The Real Difference | The Real Cost of a Lamborghini Revuelto (Insurance, Tires, Service) | Why Lamborghini Built the Revuelto the Way It Did |
| 3 | 14/02 | Ferrari SF90 Stradale (McLaren Artura) | 2 Things You Didn't Know About the Ferrari SF90 | Ferrari SF90 vs McLaren Artura: The Difference Nobody Explains | Can a Normal Person Afford a Ferrari SF90? | The Insane Story Behind Ferrari's First Plug-In Hybrid |
| 4 | 15/02 | Chevrolet Corvette Z06 (Porsche 911 GT3 RS) | 2 Things You Didn't Know About the Corvette Z06 | Why the Corvette Z06 Beats the 911 GT3 RS (And Where It Loses) | What It Really Costs to Own a Corvette Z06 | The Insane Story Behind the Mid-Engine Corvette |
| 5 | 16/02 | Ford GT (Ford GT40) | 2 Secrets Hidden Inside the Ford GT | Ford GT vs GT40: The Difference Nobody Explains | The Real Cost of a Ford GT (And Why Owners Had to Sign a Contract) | The Man Who Made Ford Beat Ferrari |
| 6 | 17/02 | McLaren F1 (McLaren W1) | 2 Things You Didn't Know About the McLaren F1 | McLaren F1 vs McLaren W1: The Real Difference | What It Really Costs to Own a McLaren F1 Today | The Insane Story Behind the McLaren F1 |
| 7 | 18/02 | Rimac Nevera (Bugatti Tourbillon) | 2 Things You Didn't Know About the Rimac Nevera | Rimac Nevera vs Bugatti Tourbillon: Electric vs V16 | The Real Cost of an Electric Hypercar | How a Kid From Croatia Ended Up Running Bugatti |
| 8 | 19/02 | Pagani Utopia (Pagani Zonda) | 2 Secrets Hidden Inside the Pagani Utopia | Pagani Zonda vs Utopia: The Difference Nobody Explains | What It Really Costs to Own a Pagani | The Insane Story Behind Horacio Pagani |
| 9 | 20/02 | Dodge Viper ACR (Corvette ZR1) | 2 Things You Didn't Know About the Dodge Viper | Dodge Viper ACR vs Corvette ZR1: The Real Difference | The Real Cost of Owning a Viper Today | Why the Dodge Viper Was Killed (Twice) |
| 10 | 21/02 | Lamborghini Urus (Ferrari Purosangue) | 2 Things You Didn't Know About the Lamborghini Urus | Lamborghini Urus vs Ferrari Purosangue: The Difference Nobody Explains | What It Really Costs to Own a Lamborghini Urus | Why Lamborghini Bet Everything on an SUV |
| 11 | 22/02 | Mercedes-AMG One (Aston Martin Valkyrie) | 2 Secrets Hidden Inside the Mercedes-AMG One | AMG One vs Aston Martin Valkyrie: The Real Difference | The Real Cost of a Formula 1 Car for the Road | Why the Mercedes-AMG One Took Years Longer Than Promised |
| 12 | 23/02 | Lexus LFA (Nissan GT-R) | 2 Things You Didn't Know About the Lexus LFA | Lexus LFA vs Nissan GT-R: The Difference Nobody Explains | Why the Lexus LFA Is Worth More Now Than New | The Insane Story Behind the Lexus LFA |
| 13 | 24/02 | Shelby Cobra 427 (AC Ace) | 2 Things You Didn't Know About the Shelby Cobra | Shelby Cobra vs AC Ace: The Real Difference | What a Real Shelby Cobra Costs Today | The Man Who Built the Shelby Cobra |
| 14 | 25/02 | Ferrari F40 (Porsche 959) | 2 Secrets Hidden Inside the Ferrari F40 | Ferrari F40 vs Porsche 959: The Difference Nobody Explains | What It Really Costs to Own a Ferrari F40 | The Insane Story Behind the Last Car Enzo Ferrari Approved |
| 15 | 26/02 | Lamborghini Countach (Lamborghini Miura) | 2 Things You Didn't Know About the Lamborghini Countach | Countach vs Miura: The Real Difference | The Real Cost of Owning a Classic Lamborghini | How a Tractor Maker Ended Up Building the Countach |
| 16 | 27/02 | Corvette ZR1 C8 (Ferrari 296 GTB) | 2 Things You Didn't Know About the New Corvette ZR1 | Corvette ZR1 vs Ferrari 296 GTB: The Difference Nobody Explains | Can a Normal Person Afford a Corvette ZR1? | The Insane Story Behind America's Fastest Corvette |
| 17 | 28/02 | Ford Mustang GTD (Porsche 911 GT3) | 2 Secrets Hidden Inside the Ford Mustang GTD | Mustang GTD vs Porsche 911 GT3: The Real Difference | What It Really Costs to Own a Mustang GTD | Why Ford Built a Mustang to Beat Porsche |
| 18 | 01/03 | Hennessey Venom F5 (SSC Tuatara) | 2 Things You Didn't Know About the Hennessey Venom F5 | Venom F5 vs SSC Tuatara: The Difference Nobody Explains | The Real Cost of an American Hypercar | The Insane Story Behind America's Speed-Record War |
| 19 | 02/03 | Bugatti Veyron (Bugatti Chiron) | 2 Things You Didn't Know About the Bugatti Veyron | Bugatti Veyron vs Chiron: The Real Difference | What It Really Costs to Own a Bugatti Veyron | Why the Bugatti Veyron Almost Never Happened |
| 20 | 03/03 | Porsche 918 Spyder (Ferrari LaFerrari) | 2 Secrets Hidden Inside the Porsche 918 Spyder | Porsche 918 vs LaFerrari: The Difference Nobody Explains | The Real Cost of Owning a Porsche 918 | The Insane Story Behind the Hypercar Holy Trinity |
| 21 | 04/03 | Ram 1500 TRX (Ford F-150 Raptor R) | 2 Things You Didn't Know About the Ram TRX | Ram TRX vs Raptor R: The Difference Nobody Explains | What It Really Costs to Own a Ram TRX | Why Ram Killed the TRX (And What Came Next) |
| 22 | 05/03 | Ferrari Purosangue (Rolls-Royce Cullinan) | 2 Things You Didn't Know About the Ferrari Purosangue | Ferrari Purosangue vs Rolls-Royce Cullinan: The Real Difference | Can a Normal Person Afford a Ferrari SUV? | Why Ferrari Swore It Would Never Build an SUV |
| 23 | 06/03 | Mercedes G63 AMG 6x6 (Hennessey VelociRaptor 6x6) | 2 Secrets Hidden Inside the Mercedes G63 6x6 | G63 6x6 vs VelociRaptor 6x6: The Difference Nobody Explains | The Real Cost of a Six-Wheel Truck | The Insane Story Behind the Mercedes 6x6 |
| 24 | 07/03 | DeLorean DMC-12 (Tesla Cybertruck) | 2 Things You Didn't Know About the DeLorean | DeLorean vs Cybertruck: Two Stainless Steel Bets | What It Really Costs to Own a DeLorean Today | The Insane Story Behind John DeLorean |
| 25 | 08/03 | Koenigsegg Gemera (Koenigsegg Regera) | 2 Things You Didn't Know About the Koenigsegg Gemera | Koenigsegg Gemera vs Regera: The Real Difference | What It Really Costs to Own a Koenigsegg | Why Koenigsegg Builds Hypercars in a Fighter-Jet Hangar |
| 26 | 09/03 | Aston Martin DB5 (Aston Martin DB12) | 2 Secrets Hidden Inside the Aston Martin DB5 | Aston Martin DB5 vs DB12: The Difference Nobody Explains | What a Real Aston Martin DB5 Costs Today | The Insane Story Behind James Bond's Aston Martin |
| 27 | 10/03 | Lamborghini Aventador SVJ (Huracán STO) | 2 Things You Didn't Know About the Aventador SVJ | Aventador SVJ vs Huracán STO: The Real Difference | The Real Cost of Owning a Lamborghini Aventador | Why the Aventador Was the Last of Its Kind |
| 28 | 11/03 | Toyota 2000GT (Datsun 240Z) | 2 Things You Didn't Know About the Toyota 2000GT | Toyota 2000GT vs Datsun 240Z: The Difference Nobody Explains | Why a Toyota 2000GT Costs More Than a New Ferrari | The Insane Story Behind Japan's First Supercar |
| 29 | 12/03 | Ferrari Enzo (Ferrari F50) | 2 Secrets Hidden Inside the Ferrari Enzo | Ferrari Enzo vs F50: The Real Difference | What It Really Costs to Own a Ferrari Enzo | The Insane Story Behind the Ferrari Enzo |
| 30 | 13/03 | Czinger 21C (McLaren Senna) | 2 Things You Didn't Know About the Czinger 21C | Czinger 21C vs McLaren Senna: The Difference Nobody Explains | The Real Cost of a 3D-Printed Hypercar | The Insane Story Behind the Czinger 21C |

Every title with a factual claim inside it (e.g. "Owners Had to Sign a Contract", "Killed Twice", "Costs More Than a New Ferrari") is kept **only if the research confirms it**; otherwise the line falls back to the base formula of that angle.

## 6. How it reuses the current pipeline

- **One research pass per day, four scripts.** The research for a theme produces one `sources.json`; the four scripts (A–D) are written from it, so facts are checked once and stay consistent across the four videos.
- `videos/dayNN-[a|b|c|d]/script.json` per video, same format as today, plus an `angle` field. `pipeline/build.py` renders them unchanged (Piper narration, Ken Burns scenes, captions burned **last**).
- `pipeline/fetch_media.py` + Actions fetch real photos (Wikimedia Commons has plenty of exotic cars and archive photos). No AI images. Credits go in `credits.json` as today.
- Thumbnails: **4 fixed Canva templates, one per angle** (section 3), so each day's four thumbnails look clearly different from each other but the channel stays recognisable. `thumbs.yml` exports them.
- Upload: `pipeline/yt_upload.py` / `youtube.yml`. Quota check: 4 long uploads + thumbnails (6,600 units) + the 2 daily Shorts (3,200) = 9,800 of the 10,000 daily units until 11/03/2027. It fits, but with no margin; I will ask Google for a quota increase together with the API audit.
- Releases keep the `videoNN` pattern (`dayNN-a` … `dayNN-d`) so nothing large goes to the project folder.

## 6b. Trend slot (from the viral-video research, 2026-10-23)

Source: `/mnt/project-files/pesquisa/viral-car-videos-2026-10-23.md` (YouTube API, last 10 days). What it shows:
- New-reveal exotics pull the biggest numbers: the Tesla Roadster reveal (15/10/2026) put several videos above 10M views in about a week; Porsche Mission S videos reached ~2.6M.
- "Banned + cheap" works for long videos (a banned-Chinese-car video hit 2.5M in under 3 days).
- Our own niche also moves: pickup-market and hidden-dealer-stock videos at 540k–670k in under a week.

How the plan uses it:
- The 30 themes above are evergreen and stay the base. **One day per week becomes a trend day**: the theme is swapped for whatever car is breaking news that week, with the same 4 angles (e.g. "2 Things Nobody Tells You About the Tesla Roadster", "Porsche Mission S vs Corvette ZR1").
- Before each batch is scripted, `trends.yml` (branch `claude/project-thread-p1ji6g`, about 2,000 quota units per run) re-pulls the data, because news from October 2026 will be stale by February 2027.
- Banned/cheap and truck themes (e.g. a Chinese pickup sold outside the US) are good bridge days back to the truck audience (open question 3).

## 7. Open questions for Vinicius

1. **Start date:** 12/02/2027 (no gap after the last long video, my recommendation) or 28/02/2027?
2. **Length:** 10–12 minutes per video (my recommendation), or keep >20 min for at least one angle (e.g. D, the story)?
3. **Same channel?** Exotic cars are a step away from "Pickup Reality" (trucks). Keeping it on the same channel is simpler; a second channel would keep the audiences clean. Day 21 (Ram TRX vs Raptor R) is a bridge back to trucks; we could add one truck theme per week to keep the old audience.
4. **E-book:** the "2027 Truck Buyer's Guide" fits the truck videos, not hypercars. Keep it in every description, or only on truck themes?
5. **Shorts for phase 2:** keep making 5 Shorts per day from these videos, or stop new Shorts until the current queue ends (11/03/2027)?
