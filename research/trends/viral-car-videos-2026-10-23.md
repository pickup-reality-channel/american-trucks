# Viral car videos on YouTube, last 10 days (pulled 2026-10-23 17:30 UTC)

**How this was measured.** Pulled straight from the YouTube Data API through the channel's own credentials (workflow `trends.yml`, script `pipeline/yt_trends.py`). It ran 20 searches with the US region filter (car, truck, pickup truck, supercar, ford, tesla, chevy, toyota and more), plus the US "Autos & Vehicles" chart. Only videos published on or after 2026-10-13 were kept, which gave 781 videos. Full raw list: `research/trends/latest.md` / `latest.json` on branch `claude/project-thread-p1ji6g`.

**Caveats.**
- View counts and ages below are exact API numbers at pull time, not estimates.
- "US" means the videos are available and relevant in the US region search. The API does not show where another channel's views come from, so the share of US viewers is unknown.
- Indian, Hindi, Arabic and kids' channels were left out of the picks.
- Web news sources could not be used to cross-check views, because YouTube and chart sites (Playboard and similar) are blocked for page fetching from here.

## The big story: Tesla's "flying" Roadster reveal (Oct 15)

Tesla's Roadster reveal took over the whole automotive category this week. Many of the top 100 videos are about it, long-form and Shorts alike.

Facts from [TechCrunch](https://techcrunch.com/2026/10/15/tesla-reveals-spacex-powered-roadster-that-flies-and-falls-with-style/) and [Electrek](https://electrek.co/2026/10/15/tesla-unveils-cyberfied-new-roadster-kickflip/), both dated 2026-10-15:
- **Trims:** Performance, Thrust and Rocket. The Rocket trim is invite-only and not approved for public roads.
- **"Flying":** cold-gas thrusters fed by about 600 L of compressed air in carbon-fiber pressure vessels (COPVs). In the staged demo the car went up an inverted ramp and hopped over a Cybertruck, a Semi and a Model Y.
- **Claimed performance:** 0-60 mph in under 1 second (Thrust trim), about 300 miles of range, over 230 mph.
- **Price:** none announced. Reservations take $50k for Performance and $250k for Thrust.
- **Production:** Musk said "2028".
- **What changed since the 2017 promise:** range went from 620 mi to about 300 mi, seating from 4 seats (2+2) to 2 at most, and production from 2020 to 2028.

## Long-form picks (4+ min, English)

| Views | Age | Length | Channel | Title | Why it works |
|---|---|---|---|---|---|
| 12,021,742 | 6.6 d | 22:45 | Marques Brownlee | [The NEW Tesla Roadster: My Honest Reaction](https://www.youtube.com/watch?v=scwlR0QHGOk) | Timing on the biggest event of the week, plus a promise of honesty in a hype cycle |
| 10,609,483 | 7.6 d | 6:43 | YOUCAR | [NEW TESLA ROADSTER - It Can Fly!!! (SpaceX Technology)](https://www.youtube.com/watch?v=Fdhwkap2DFU) | Leads with the impossible claim ("It Can Fly"); a faceless-style news recap |
| 10,564,209 | 5.0 d | 53:01 | Mat Armstrong | [BUGATTI REFUSED TO SELL US THE FINAL PART SO WE MADE IT](https://www.youtube.com/watch?v=81OEc1j1Hyc) | Villain (Bugatti refused), underdog, and a payoff |
| 9,980,524 | 7.6 d | 10:15 | CNET | [Tesla's Flying Roadster Revealed: Everything That Happened in 10 Minutes](https://www.youtube.com/watch?v=TWHXrLzUKJc) | Saves the viewer time: a 23-minute event in 10 |
| 9,289,259 | 6.9 d | 57:20 | The Civil Rights Lawyer | [Tesla Saves Owner From Prison](https://www.youtube.com/watch?v=A4Q8q0KQQ14) | The car as the hero of a legal story; curiosity gap |
| 5,472,794 | 6.2 d | 25:23 | WD Detailing | [Granddaughter Sees Deceased Grandfather's $1,000,000 Ferrari CLEANED...](https://www.youtube.com/watch?v=cXnXKZQveYA) | Emotion plus a price tag |
| 3,897,379 | 7.3 d | 27:04 | Hagerty | [The FLYING Tesla Roadster explained by the man who engineered it](https://www.youtube.com/watch?v=22rvpUecLts) | "Explained": the how behind the hype |
| 2,650,326 | 7.8 d | 8:03 | carwow | [Porsche just proved why it's the SUPERCAR KING! New Mission S](https://www.youtube.com/watch?v=qKcO0LbPPDE) | New exotic, plus a claim to the crown |
| 2,617,072 | 4.0 d | 14:30 | Top Gear | [Porsche Has Finally Built A Supercar!](https://www.youtube.com/watch?v=ECpoCJGxP-U) | "Finally" implies a long wait is over |
| 2,543,687 | 2.9 d | 58:12 | Rich Rebuilds | [I Bought a Banned Chinese Car From a Rental Company for $2,000](https://www.youtube.com/watch?v=Jdm8qnlnzqc) | **Fastest-growing (~880k/day).** "Banned" plus an absurdly low price, the same formula as British Vehicles |
| 2,141,983 | 6.8 d | 23:51 | WhistlinDiesel 1000 | [Are Subaru's Actually Meant to be Rally Cars?](https://www.youtube.com/watch?v=1SzJ1j1q-_k) | Tests a common belief |
| 2,106,551 | 9.1 d | 9:24 | DRIVETRIBE | [Richard Hammond Drives the 2,000HP Lotus Evija](https://www.youtube.com/watch?v=TYjgYby8NaA) | Big number in the title |
| 1,398,197 | 1.7 d | 35:16 | Cleetus McFarland | [Leroy Made MASSIVE GAINS Testing For World Cup!](https://www.youtube.com/watch?v=nw0OGUxbhIg) | Fan base, drag-racing series |

**Faceless or narrated channels in our lane** (smaller, but the same format as ours):

| Views | Age | Channel | Title |
|---|---|---|---|
| 944,548 | 7.0 d | CAR TV | [2028 Tesla Roadster - This Car Can FLY! (Elon Musk's Insane Flying Supercar)](https://www.youtube.com/watch?v=UJWPXUBKVFg) |
| 667,101 | 7.0 d | the SUV geek | [The 2026 Pickup Truck Market Just Hit a BREAKING POINT / And It's Getting Ugly](https://www.youtube.com/watch?v=bs8XPd3AK4Y) |
| 539,930 | 4.8 d | Dotts Lots | [The Chevrolet Dealer Who Kept 500 Cars Hidden for Decades](https://www.youtube.com/watch?v=xTkWf1t6tHY) |
| 403,623 | 9.8 d | Chevy Central | [The Truth About 0W-20 vs 5W-30 Oil (All Chevy Engines Tested)](https://www.youtube.com/watch?v=YBdvcNHYuGQ) |

## Shorts picks

| Views | Age | Channel | Title |
|---|---|---|---|
| 40,178,552 | 9.1 d | Car Clips | [Gap sports cars while at work...](https://www.youtube.com/watch?v=JoN0lAzJfSI) |
| 18,836,215 | 2.5 d | Facts' Mine | [This Flying Car Mocks Elon Musk's New Tesla Roadster](https://www.youtube.com/watch?v=ZLAIN7gfyBc) (~7.5M/day) |
| 15,740,854 | 8.9 d | carshorts | [Officer Stops Monster Truck](https://www.youtube.com/watch?v=8qWaYgiQVLo) |
| 10,381,966 | 5.9 d | Brake Zone | [Tesla's Underside Looks Nothing Like Volvo's or Toyota's](https://www.youtube.com/watch?v=xmr8FrTyjmg) |
| 9,827,281 | 7.8 d | Light Ride | [These Trucks Look INSANE With Blue LED Eyes!](https://www.youtube.com/watch?v=5cFNl0NmT9U) |
| 8,032,640 | 2.8 d | Crash | [We're So Cooked #tesla #teslaroadster](https://www.youtube.com/watch?v=jIprtyrpx7E) |
| 4,147,182 | 2.7 d | Exotic Rubber | [Old School Mercedes Were Cooler](https://www.youtube.com/watch?v=PkIEsz73oSI) |
| 2,908,808 | 3.9 d | Exotic Rubber | [The Reality Of Owning a Corvette](https://www.youtube.com/watch?v=iNSsd185-e8) |
| 1,047,396 | 5.3 d | BaemNG | [Which American Truck Survives a 33,000-LB Steel Coil Drop?](https://www.youtube.com/watch?v=sWJCHl-YIXQ) |

## Patterns

1. **One event can eat the whole category.** The Roadster reveal drove at least 15 videos past 4M views in a week. Big reveals are the moment to publish fast.
2. **Impossible claim, then the reality check.** "It can fly", "My honest reaction" and "Expectation vs reality" all work, and the skeptic version holds up as well as the hype version.
3. **Banned or forbidden, plus an absurd price** (Rich Rebuilds' $2,000 banned car) is the fastest-growing long video of the week. It is the British Vehicles formula.
4. **Comparisons that show a hidden difference** (the Tesla underside vs Toyota, "Which American truck survives...") do well as Shorts.
5. **New exotic plus a crown claim** ("SUPERCAR KING", "Finally built a supercar").

## Proposed Pickup Reality angles (title first; every fact must be sourced before scripting)

| # | Proposed title | Source viral | Facts to lock down |
|---|---|---|---|
| 1 | **Tesla Promised This Car in 2017. Here's Every Promise It Broke** | Roadster reveal (MKBHD, CNET) | 620→300 mi, 2+2→2 seats, 2020→2028, $50k deposit with no price (Electrek, TechCrunch) |
| 2 | **2 Things Nobody Tells You About the "Flying" Tesla Roadster** | Roadster reveal | The Rocket trim is not street-legal; the thrusters run on 600 L of compressed air in COPVs |
| 3 | **The Roadster Jumped a Cybertruck. Here's What the Cybertruck Promised in 2019 vs What You Got** | Roadster demo (it hopped over a Cybertruck) | 2019 launch claims vs the 2023-2026 price, range and specs (to verify) |
| 4 | **The Chinese Pickup America Banned, and What It Costs Everywhere Else** | Rich Rebuilds "Banned Chinese Car" | BYD Shark and the US rule on Chinese connected-car software (to verify dates and prices) |
| 5 | **Porsche's New Supercar vs Corvette ZR1: The Difference Is Shocking** | Porsche Mission S (carwow, Top Gear) | Mission S is a concept with no price; ZR1 specs; frame it as concept vs production |
| 6 | **The 2027 Pickup Market Is Breaking: 5 Trucks That Got Worse and 2 That Didn't** | the SUV geek (667k/7d, our exact niche) | 2026-2027 average truck prices and model-year changes |
| 7 | **The Dealer Who Hid 500 Cars for 50 Years: What Those Trucks Sold For** | Dotts Lots (540k/4.8d) | Lambrecht Chevrolet auction, 2013 (to verify sale prices) |
| 8 | **Your Truck Is Watching You: What Ford, GM and Tesla Cameras Actually Record** | "Tesla Saves Owner From Prison" (9.3M) | OEM camera and data-retention facts (to verify) |
| Short | **What an F-150 vs a Cybertruck Look Like From Underneath** | Brake Zone underside Short (10.4M) | Real underbody photos only |
| Short | **The Reality of Owning a Ram TRX** (reality-of-owning series) | Exotic Rubber Corvette Short | Fuel, insurance and price figures, sourced |

Timing note: angles 1-3 depend on the news and lose value every week. The other angles also fit the post-February 2027 formats ("two things you don't know", "differences between models", "exotic cars").
