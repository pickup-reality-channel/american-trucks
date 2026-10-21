import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One pickup keeps about eighty percent of its value after five years. The best-selling truck in America loses nearly thirty-nine percent. On a sixty thousand dollar truck, that is a difference of more than eleven thousand dollars. And the truck that holds its value best of all might not be the one you expect. Here are the trucks that hold their value, with the real numbers.""",
   "Toyota Tacoma pickup truck", "TRUCKS THAT HOLD THEIR VALUE")

# ---------- COLD OPEN ----------
sc("""When you buy a truck, the price you pay is only the first number. The second number is what it is worth when you sell it. And the gap between the two is the real cost of owning that truck. A truck that loses twenty percent of its value in five years costs you far less than one that loses forty, even if the sticker price is exactly the same on the day you sign.""",
   "Ford F-150 pickup truck", "THE SECOND NUMBER MATTERS")
sc("""The data we use comes from iSeeCars, which analyzed more than three million vehicles to calculate how much value each model keeps after five years. Their truck pages list the five-year resale value, which is the share of the original price a truck is still worth. We turn that into depreciation by subtracting from one hundred percent. And we use a May twenty twenty-six article from SlashGear for the dollar figures. Every source is listed in the description.""",
   "Chevrolet Silverado 1500 pickup", "SOURCE: ISEECARS, 3 MILLION+ VEHICLES")
sc("""A caution before we start. These are averages across a huge number of trucks, so your truck can be better or worse depending on the mileage, the condition, the trim, and the market where you sell. And the iSeeCars pages we read show only the top five trucks in each category, so some trucks you might expect to see, like the Chevrolet Silverado, are not in the part of the list that we could read. We will not guess their numbers.""",
   "Chevrolet Silverado pickup", "TOP 5 PER CATEGORY ONLY")
sc("""So here are six groups of trucks, and a twist in every one. One truck sits right behind a Porsche in the whole study. One sells in huge numbers and still loses almost forty percent. One small truck beats a bigger rival, and one truck that is falling in sales still holds its value. Stay with me, because the last twist is about the truck that most people buy, and it affects how you should think about a purchase.""",
   "Toyota Tundra pickup", "SIX GROUPS. SIX TWISTS.")

# ---------- 1. TOYOTA TACOMA ----------
sc("""Number one is the Toyota Tacoma, and it is the champion. According to the iSeeCars truck page, the Tacoma keeps eighty and a half percent of its value after five years, which is a depreciation of nineteen point five percent. That is the best of any midsize truck, by a very wide margin. The next one on the midsize list, the Ford Ranger, keeps sixty-eight point eight percent.""",
   "Toyota Tacoma pickup", "TACOMA: 80.5% RESALE AFTER 5 YEARS")
sc("""The SlashGear article, which cites the iSeeCars study of cars that hold their value, gives a slightly different figure, nineteen point nine percent, and that matches a drop of six thousand, four hundred twenty-six dollars from the original selling price. The two figures are close, and they come from different pages of the same study, so we show both. And here is the twist. The Tacoma holds its value better than almost every vehicle in the entire study, not just the trucks.""",
   "Toyota Tacoma TRD Pro pickup", "TACOMA: LOSES ~$6,426 IN 5 YEARS")
sc("""SlashGear calls the Tacoma the fourth-best vehicle outright. Only three cars held their value better than it, the Porsche seven eighteen Cayman, the Porsche nine eleven, and the Chevrolet Corvette. It even beat the Toyota GR Supra. A work truck for a few tens of thousands of dollars sits just behind a Porsche. And the article notes that Toyotas take nearly half of the twenty-five spots on the lowest-depreciation list.""",
   "Toyota Tacoma pickup truck", "ONLY 3 CARS BEAT IT: 2 PORSCHES, CORVETTE")

# ---------- 2. TOYOTA TUNDRA ----------
sc("""Number two is the Toyota Tundra, and it is the full-size champion by a huge margin. The iSeeCars truck page shows eighty and three tenths percent of its value after five years, a depreciation of nineteen point seven percent. The next full-size truck on the list is the Ram one thousand five hundred at sixty-one point eight percent. That is a gap of about eighteen points.""",
   "Toyota Tundra pickup", "TUNDRA: 80.3% RESALE")
sc("""The SlashGear article gives a slightly different number for the Tundra, twenty-one point two percent depreciation, which is a drop of eight thousand, seven hundred forty-six dollars from the original price. So between the two sources, the Tundra loses somewhere between nineteen and twenty-one percent. That is half of what its rivals lose. And here is the twist. The Tundra is not the best-selling full-size truck. It sold one hundred ten thousand and eighty through nine months of twenty twenty-six. It is the best at keeping its value.""",
   "Toyota Tundra 1794 pickup", "TUNDRA: LOSES ~$8,746")

# ---------- 3. HEAVY-DUTY TRUCKS ----------
sc("""Number three is a group, the heavy-duty trucks, and they are the surprise. On the iSeeCars list, the Ram three thousand five hundred keeps seventy-nine point eight percent of its value after five years. The Ford F-three-fifty Super Duty keeps seventy-nine point six. The Ford F-four-fifty keeps seventy-seven percent, the F-two-fifty seventy-five point seven, and the Ram two thousand five hundred seventy-four point nine.""",
   "Ram 3500 Heavy Duty pickup", "RAM 3500: 79.8%. F-350: 79.6%")
sc("""Look at the twist. The heavy-duty trucks hold their value almost as well as the Tacoma and the Tundra, with depreciation between twenty and twenty-five percent. That is much better than the half-ton trucks that sit next to them on the same lot. A buyer who needs a one-ton truck for work is also buying one of the best-protected assets on the list. These trucks are expensive, but they are slow to lose value.""",
   "Ford F-350 Super Duty pickup", "HEAVY DUTY: 20% TO 25% LOSS")

# ---------- 4. MIDSIZE REST ----------
sc("""Number four is the rest of the midsize group, and the order is different from the sales table. The Ford Ranger keeps sixty-eight point eight percent. The GMC Canyon keeps sixty-six point eight. The Jeep Gladiator keeps sixty-five point two. And the Nissan Frontier keeps sixty-three point four, which is the fifth entry on the list. All four are well behind the Tacoma, at eighty and a half percent.""",
   "Ford Ranger pickup", "RANGER 68.8%, CANYON 66.8%")
sc("""Here is the twist. The Nissan Frontier is the fastest-growing truck of the year, up almost forty percent through nine months. But in this list, it has the lowest resale value of the five. And the Jeep Gladiator, whose sales fell nearly twenty percent, still keeps more value than the Frontier. So sales and resale do not move together. A truck that is selling fast can still lose value quickly, and a truck that is selling slowly can keep it.""",
   "Nissan Frontier pickup", "FRONTIER: FAST SALES, LOWEST RESALE")

# ---------- 5. SMALL TRUCKS ----------
sc("""Number five is the small trucks, and there are only two on the list. The Ford Maverick keeps sixty-eight point two percent of its value after five years, a depreciation of thirty-one point eight percent. The Hyundai Santa Cruz keeps sixty-five point one, a depreciation of thirty-four point nine. So the Maverick is ahead, by about three points.""",
   "Ford Maverick pickup", "MAVERICK: 68.2%. SANTA CRUZ: 65.1%")
sc("""And here is the twist. The Santa Cruz sold fourteen thousand, eight hundred eleven trucks through nine months of twenty twenty-six, down twenty-eight percent, and reports say it is being phased out. Yet it still holds sixty-five percent of its value after five years, which is better than the Nissan Frontier and close to the Gladiator. A truck can be discontinued, and still keep a good share of its value. But the reports are unconfirmed, and the market will decide.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: STILL 65.1%")

# ---------- 6. FULL-SIZE BIG THREE ----------
sc("""Number six is the group that most people buy, the full-size half-ton trucks from Detroit. On the iSeeCars list, the Ram one thousand five hundred keeps sixty-one point eight percent of its value. The Ford F-one-fifty keeps sixty-one point four. The GMC Sierra one thousand five hundred Limited keeps sixty-one point one, and the regular Sierra one thousand five hundred sixty point five. Those are depreciations of about thirty-eight and a half to almost forty percent.""",
   "Ford F-150 pickup", "F-150: 61.4%. RAM 1500: 61.8%")
sc("""Now the final twist, and it matters most. The three best-selling truck lines in America, the Ford F-Series, the Chevrolet Silverado and the Ram, together made up fifty-nine percent of the sales of the top ten trucks this year. And in this list, the two of them that we could read lose close to forty percent of their value. A truck that sells in huge numbers is easy to buy, and easy to sell. But it is not a truck that holds its price.""",
   "Ram 1500 pickup truck", "BEST SELLERS LOSE ~39% IN 5 YEARS")
sc("""Let's put that in dollars, with an example that is clearly an example. Imagine a truck that costs fifty thousand dollars new. At the Tundra's rate, nineteen point seven percent, it would be worth about forty thousand, one hundred fifty dollars after five years. At the F-one-fifty's rate, thirty-eight point six percent, it would be worth about thirty thousand, seven hundred. That is a difference of nine thousand, four hundred fifty dollars, on the same starting price.""",
   "Ford F-150 Toyota Tundra pickups", "EXAMPLE: $50,000 TRUCK")


# ---------- MONEY EXAMPLES ----------
sc("""To make this real, let's run four examples. These are examples, not real quotes, and we use the iSeeCars percentages. First, a midsize truck that costs forty thousand dollars new. The Tacoma, at nineteen point five percent depreciation, would lose seven thousand, eight hundred dollars, and be worth thirty-two thousand, two hundred after five years. The Ranger would lose twelve thousand, four hundred eighty dollars.""",
   "Toyota Tacoma pickup", "EXAMPLE 1: $40,000 MIDSIZE TRUCK")
sc("""Continue with the same forty thousand dollar truck. The Jeep Gladiator, at thirty-four point eight percent, would lose thirteen thousand, nine hundred twenty dollars. And the Nissan Frontier, at thirty-six point six, would lose fourteen thousand, six hundred forty. So between the Tacoma and the Frontier, the same starting price would leave you with a difference of six thousand, eight hundred forty dollars in what the truck is worth.""",
   "Nissan Frontier pickup", "TACOMA VS FRONTIER: $6,840 GAP")
sc("""Second example, a heavy-duty truck that costs seventy thousand dollars new. The Ram three thousand five hundred, at twenty point two percent, would lose fourteen thousand, one hundred forty dollars. The Ford F-three-fifty would lose fourteen thousand, two hundred eighty. The F-four-fifty would lose sixteen thousand, one hundred. The F-two-fifty, seventeen thousand and ten. And the Ram two thousand five hundred, seventeen thousand, five hundred seventy.""",
   "Ram 3500 pickup truck", "EXAMPLE 2: $70,000 HEAVY-DUTY TRUCK")
sc("""Third example, a small truck that costs thirty thousand dollars new. The Maverick, at thirty-one point eight percent, would lose nine thousand, five hundred forty dollars. The Santa Cruz, at thirty-four point nine, would lose ten thousand, four hundred seventy. The difference is nine hundred thirty dollars. Not very large, but it is money that comes back to you, or does not, on the day you sell.""",
   "Ford Maverick pickup truck", "EXAMPLE 3: $30,000 SMALL TRUCK")
sc("""Fourth example, the one that matters most, a full-size truck that costs sixty thousand dollars new. The Tundra, at nineteen point seven percent, would lose eleven thousand, eight hundred twenty dollars. The Ram one thousand five hundred would lose twenty-two thousand, nine hundred twenty. The F-one-fifty would lose twenty-three thousand, one hundred sixty. And the Sierra one thousand five hundred would lose twenty-three thousand, seven hundred.""",
   "Toyota Tundra pickup truck", "EXAMPLE 4: $60,000 FULL-SIZE TRUCK")
sc("""Look at the gap in that last example. Between the Tundra and the Ram, the difference in loss is eleven thousand, one hundred dollars. Between the Tundra and the Sierra, eleven thousand, eight hundred eighty. That is a large number, and it is the same size as a good used car. It is the reason why a buyer who plans to keep a truck for only five years should think about resale, and not only about the monthly payment.""",
   "Ram 1500 pickup truck", "TUNDRA VS RAM: $11,100 GAP")
sc("""Now the honest counterpoint. The Tundra and the Ram are different trucks, with different engines, different prices, and different features. A buyer who chooses the Ram because they prefer how it drives, or how much it can tow, or the price they were offered, is making a reasonable choice. Resale value is one number among many. It should be in your decision, but it should not be the only thing in it.""",
   "Ram 1500 Rebel pickup", "RESALE IS ONE NUMBER AMONG MANY")

# ---------- THE LESSON ----------
sc("""So what is the lesson? Resale value is part of the price. A cheaper truck that loses more is not always cheaper to own. And an expensive truck that keeps its value can cost less over five years than it looks like on the day of purchase. The heavy-duty trucks and the two Toyotas lose half as much as the typical half-ton, and that is a real, measurable difference in what you will pay to own the truck.""",
   "Toyota Tacoma Tundra pickups", "RESALE IS PART OF THE PRICE")
sc("""But there is a counter-argument, and it is fair. A truck that holds its value usually costs more to buy, and buyers pay for the reputation. SlashGear notes that pickups hold value best of all vehicle segments, slightly ahead of fuel-sipping hybrids and well ahead of SUVs. So every truck on this list is, on average, a better store of value than most cars. The question is only how much better.""",
   "Ford F-250 Super Duty pickup", "TRUCKS BEAT SUVS ON RESALE")
sc("""One more warning. These are averages for the truck as it sold in the past, and the future can change. Prices of new trucks are rising, with the average full-size pickup at sixty-seven thousand, four hundred forty-six dollars in August, according to Kelley Blue Book. Electric trucks are being cancelled and rewritten. And a model that is discontinued can lose value quickly, or slowly. So treat these numbers as a guide, not a promise.""",
   "Ford F-150 Lightning pickup", "AVERAGES, NOT PROMISES")

# ---------- CLOSE ----------
sc("""So what should you check before you buy in twenty twenty-seven? First, look up the five-year resale value of the exact model, not the brand. Second, compare the full cost over five years, including what you expect to get back when you sell. Third, check the mileage and condition rules that affect resale value, because a truck with high mileage is worth less than the average. And fourth, ask whether the truck is still being built.""",
   "Ford F-150 pickup", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Two pickup trucks cost": "Intro", "Number one": "1. Toyota Tacoma", "Number two": "2. Toyota Tundra",
      "Number three": "3. Heavy-duty trucks", "Number four": "4. The rest of the midsize trucks", "Number five": "5. Small trucks",
      "Number six": "6. The best-selling full-size trucks", "So what is the lesson": "The lesson",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video08", "length_scale": 2.0,
  "title": "6 Trucks That Hold Their Value After 5 Years (The Real Numbers)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
