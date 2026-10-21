import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The trucks that keep their value best, and the trucks most likely to last two hundred fifty thousand miles, are not the ones most people buy. They are heavy-duty pickups. And their sales are falling. In nine months, the three biggest heavy-duty lines lost more than twenty-two thousand sales. One heavy truck was just discontinued. Here is what the numbers say about heavy-duty trucks heading into twenty twenty-seven.""",
   "Ford F-350 Super Duty pickup", "HEAVY-DUTY TRUCKS IN 2027")

# ---------- COLD OPEN ----------
sc("""A heavy-duty pickup is the truck behind the truck. It is the one with the dual rear wheels, the big diesel, and a bed that carries a ton. The model names are the two fifty, three fifty, and four fifty at Ford, and the two thousand five hundred and three thousand five hundred at Chevrolet, GMC and Ram. These are work trucks, and the people who buy them are often buying a tool for a business.""",
   "Ram 2500 Heavy Duty pickup", "THE TRUCK BEHIND THE TRUCK")
sc("""For this video, we gathered five kinds of numbers. Sales, from the Pickup Truck Talk table for the first nine months of twenty twenty-six. Resale value, from iSeeCars. Longevity, from the iSeeCars study reported by Work Truck Online. Ford's production figures, from Ford Authority. And the medium-duty trucks, from Motor One and GM Authority. Every source is listed in the description, and every number is labeled.""",
   "Chevrolet Silverado 2500HD pickup", "SALES, RESALE, LONGEVITY, PRODUCTION")
sc("""There is a twist in every one of these trucks. One is growing while its rivals shrink. One is losing sales and still sits in the top group for lasting. One is the most expensive to lose value on, and the cheapest to keep. And one is a truck that you can no longer order. Stay with me, because the last twist is about the whole class, and what it means if you are thinking of buying a work truck.""",
   "Ford F-250 Super Duty pickup", "FIVE TWISTS ON HEAVY-DUTY TRUCKS")

# ---------- THE CLASS AS A WHOLE ----------
sc("""First, the whole class. Through nine months of twenty twenty-six, the three heavy-duty lines in the table, the Chevrolet Silverado HD, the GMC Sierra HD and the Ram HD, sold three hundred thirty-five thousand, two hundred sixteen. A year earlier, it was three hundred fifty-seven thousand, six hundred twenty-five. That is a fall of six point three percent, or twenty-two thousand, four hundred nine trucks.""",
   "Heavy duty pickup trucks", "HD: 335,216 (-6.3%)")
sc("""The third quarter was weaker still. Those three lines sold one hundred thirteen thousand, nine hundred eighty-nine in the quarter, compared with one hundred twenty-three thousand, six hundred seventy-one a year earlier, a fall of about seven point eight percent. Ford does not split its Super Duty sales in the sources we found, so it is not in these totals. Ford Authority reports only that Super Duty production in the quarter was one hundred ten thousand, two hundred seventy-five, up four point four percent.""",
   "Ford Super Duty pickup", "Q3: HD DOWN ~7.8%")

# ---------- 1. RAM HD ----------
sc("""Number one is the Ram heavy-duty, and it is the one growing. Through nine months, Ram sold one hundred twenty-three thousand, two hundred one heavy-duty trucks, up three point four percent from one hundred nineteen thousand, one hundred twenty-two. In a class that fell more than six percent, a gain of three point four is a clear lead.""",
   "Ram 2500 pickup", "RAM HD: +3.4%")
sc("""The twist is in the quarter. In the third quarter, the Ram HD sold forty-one thousand, one hundred seven, down six percent from forty-three thousand, seven hundred seventeen. So the growth was in the first half, and it slowed. Even so, the Ram is the only heavy-duty line in the table with a gain for the nine months. That is a very different picture from the Chevrolet and the GMC.""",
   "Ram 3500 pickup truck", "Q3: RAM HD -6.0%")
sc("""And it does very well on the iSeeCars lists. The Ram three thousand five hundred keeps seventy-nine point eight percent of its value after five years, the best of any heavy-duty truck, and the Ram two thousand five hundred keeps seventy-four point nine. In the longevity study, the Ram three thousand five hundred is first of all trucks, with a thirty-one point nine percent chance of reaching two hundred fifty thousand miles, nearly three times the truck average.""",
   "Ram 3500 Heavy Duty", "RAM 3500: 79.8% RESALE, 31.9% LONGEVITY")

# ---------- 2. CHEVROLET SILVERADO HD ----------
sc("""Number two is the Chevrolet Silverado heavy-duty, and its numbers tell a harder story. Through nine months, Chevrolet sold one hundred thirty-three thousand, seven hundred sixty-nine, down thirteen percent from one hundred fifty-three thousand, seven hundred fifty. That is a loss of nearly twenty thousand trucks in a year, the biggest fall of any heavy-duty line in the table.""",
   "Chevrolet Silverado HD pickup", "SILVERADO HD: -13.0%")
sc("""And the quarter did not rescue it. In the third quarter, the Silverado HD sold forty-four thousand, two hundred seventy-eight, down ten point one percent. The twist is that the light-duty Silverado, the same brand's everyday truck, grew six point five percent through nine months. So the same company is gaining with one truck and losing with the other. The work truck is the one in decline.""",
   "Chevrolet Silverado 2500HD", "Q3: -10.1%. LD SILVERADO: +6.5%.")
sc("""On longevity, the Silverado two thousand five hundred HD is ninth, at fourteen point one percent, and the three thousand five hundred HD is twelfth at eleven point seven, barely above the truck average of eleven point one. In the earlier edition of the study, the two thousand five hundred HD was sixth, at forty-one point two percent. So the heavy-duty Silverado has slipped in the study, and it has slipped in sales.""",
   "Chevrolet Silverado 3500HD pickup", "SILVERADO 2500HD: 14.1%. 3500HD: 11.7%.")

# ---------- 3. GMC SIERRA HD ----------
sc("""Number three is the GMC Sierra heavy-duty. Through nine months, GMC sold seventy-eight thousand, two hundred forty-six, down seven point seven percent from eighty-four thousand, seven hundred fifty-three. In the third quarter, it sold twenty-eight thousand, six hundred four, down six point nine percent. A smaller fall than the Chevrolet, but a fall.""",
   "GMC Sierra HD pickup", "SIERRA HD: -7.7%")
sc("""Here is the twist. The Sierra three thousand five hundred HD is third in the longevity study, at twenty-six point two percent, about two and a half times the truck average. And the two thousand five hundred HD is fifth, at seventeen point two. So the GMC does much better than its Chevrolet twin on the longevity list, even though the two are built in the same way. A badge and a trim can matter more than the platform.""",
   "GMC Sierra 3500HD Denali pickup", "SIERRA 3500HD: 26.2% (3RD)")

# ---------- 4. FORD SUPER DUTY ----------
sc("""Number four is the Ford Super Duty. We have no sales number for it, because the sources we found do not split it from the F-Series. What we have is the production figure, one hundred ten thousand, two hundred seventy-five in the third quarter, up four point four percent, according to Ford Authority. In a quarter when the three Detroit-badge heavy-duty trucks we could measure were falling, Ford was building more.""",
   "Ford F-350 Super Duty pickup", "SUPER DUTY: Q3 PRODUCTION 110,275 (+4.4%)")
sc("""On resale, the Ford F-three-fifty keeps seventy-nine point six percent after five years, the F-four-fifty seventy-seven, and the F-two-fifty seventy-five point seven. Those are among the best numbers in the whole market. On longevity, the F-three-fifty is sixth at fifteen point one percent, the F-four-fifty seventh at fourteen point nine, and the F-two-fifty eleventh at thirteen point four. In the earlier edition, the F-three-fifty was first, at forty-nine point one.""",
   "Ford F-450 Super Duty pickup", "F-350: 79.6% RESALE")
sc("""The twist is the contrast. The Super Duty is strong on resale and middling on longevity in the latest edition. The Ram is strong on both. And the Chevrolet is weaker on both. So the three big companies, all selling similar trucks to similar buyers, have different strengths. A buyer who looks only at the brand's reputation, and not at the numbers for the specific truck, might miss that.""",
   "Ford F-250 Super Duty pickup", "THREE COMPANIES, THREE PROFILES")

# ---------- 5. SILVERADO MEDIUM-DUTY ----------
sc("""Number five is the truck you can no longer order, the Chevrolet Silverado medium-duty. According to Motor One, Chevrolet is ending the Silverado four thousand five hundred, five thousand five hundred and six thousand five hundred HD, built with International Motors in Ohio. Production ended after the September thirtieth conclusion of the manufacturing agreement, and International is selling the plant. The sale was announced on March thirtieth.""",
   "Chevrolet Silverado medium duty truck", "SILVERADO MEDIUM-DUTY: ENDED SEPT 30")
sc("""The sales explain why. Chevrolet sold eight thousand, three hundred forty-one medium-duty trucks in twenty twenty-five, down nineteen point two percent. And in the first three months of twenty twenty-six, it sold one thousand, two hundred seventy-three, down thirty-seven point four percent. For comparison, Ford sold two thousand, three hundred thirty-one heavy trucks in the same period. So the truck was shrinking before it ended.""",
   "International Motors truck plant Springfield Ohio", "2025: 8,341 (-19.2%). Q1 2026: 1,273 (-37.4%).")
sc("""And here is the twist about what comes next. GM says it is evaluating future portfolio options for medium-duty, and will share more later. So there is no announced successor. And the article does not say what happens to current owners, including warranty or service. If you own one, or buy one from stock, ask the dealer directly, in writing, how parts and service will be handled after the production ended.""",
   "Chevrolet Silverado medium duty", "NO ANNOUNCED SUCCESSOR")


# ---------- HALF-TON VS HEAVY DUTY ----------
sc("""Let's put a half-ton and a heavy-duty truck side by side, using only the numbers we have. On resale, the Ford F-one-fifty keeps sixty-one point four percent after five years, and the F-three-fifty seventy-nine point six. The Ram one thousand five hundred keeps sixty-one point eight, and the Ram three thousand five hundred seventy-nine point eight. In both brands, the heavy-duty truck keeps about eighteen points more.""",
   "Ford F-150 Ford F-350 pickups", "RESALE: F-150 61.4% VS F-350 79.6%")
sc("""On longevity, the picture is more mixed. In the latest edition, the Ram three thousand five hundred is first at thirty-one point nine percent, while the Ram one thousand five hundred is not in the top twelve. The Ford F-three-fifty is sixth at fifteen point one, and the F-one-fifty is not in the top twelve either. So for both companies, the heavy-duty truck is more likely to go the distance than its half-ton cousin.""",
   "Ram 1500 Ram 3500 pickups", "LONGEVITY: HD ABOVE HALF-TON")
sc("""And on sales, the opposite holds. The Ford F-Series sold five hundred fifty-seven thousand through nine months, and the Silverado one thousand five hundred and two thousand five hundred together sold more than four hundred thousand. The half-tons dominate. So the market buys the truck that is easier to live with, and the truck that holds its value best is the one fewer people buy. That is a very old pattern in the truck business, and the numbers confirm it.""",
   "Ford F-150 pickup", "HALF-TONS WIN ON SALES")
sc("""So which should you buy? If you tow or haul heavy loads, every week, the heavy-duty truck is built for it, and the numbers on resale and longevity are on its side. If you use a truck mostly for commuting and family trips, with an occasional trailer, a half-ton is easier to drive, and often cheaper. The mistake is to buy the heavy-duty truck for the image, or to buy the half-ton and push it past its limits every weekend.""",
   "Ford F-250 Super Duty pickup", "BUY FOR THE JOB, NOT THE IMAGE")
sc("""There is one more thing to consider, and it is about timing. A heavy-duty truck costs more to buy, and the numbers say that it loses less value. That means the money you pay at the start comes back more fully at the end. For a business, that matters, because the truck can be an asset on the balance sheet. For a private buyer, it may matter less, because the cash you tie up in the truck cannot be used elsewhere.""",
   "Ram 3500 Laramie pickup", "MORE UPFRONT, MORE BACK LATER")
sc("""Finally, a word about the numbers in this video. Most of them are estimates or reported figures from third parties, and they were collected in the fall of twenty twenty-six. Sales tables are reasonably precise, but resale and longevity numbers are statistical estimates. Use them to narrow the list, and then check the exact truck. The best information about a used truck is its service record and a careful inspection.""",
   "Chevrolet Silverado 2500HD pickup", "ESTIMATES: USE THEM TO NARROW THE LIST")

# ---------- THE LESSON ----------
sc("""So what is the final twist? It is about why heavy-duty trucks are falling in sales, and the sources we found do not give a reason. We can offer what the numbers do say. The price of trucks has risen, the full-size average is sixty-seven thousand, four hundred forty-six dollars, and heavy-duty trucks are more expensive still. The market for work trucks may be more sensitive to price, and to the economy, than the market for family trucks. But that is an interpretation, not a finding.""",
   "Ram 3500 Heavy Duty pickup", "WHY ARE HD SALES FALLING?")
sc("""What the numbers do show is that the heavy-duty trucks are a very different asset. They lose about twenty to twenty-five percent in five years, compared with thirty-eight to forty percent for a half-ton. Take an example of a truck that costs seventy thousand dollars new. At the Ram's or the Ford's rate, that is a loss of about fourteen thousand to seventeen thousand dollars. At the F-one-fifty's rate, it is about twenty-seven thousand. A work truck can be a better store of value than a family truck.""",
   "Ford F-350 Super Duty pickup", "HD LOSES ~20-25%. HALF-TON ~39%.")
sc("""But a store of value is only useful if you can sell. In a market where the heavy-duty lines are shrinking, there may be fewer new trucks and fewer buyers, and that is something to watch. We do not have used price data in the sources we found. A careful buyer checks local prices for the exact truck, and compares the five-year picture to the cost of a lease or a rental, if the work is occasional.""",
   "Chevrolet Silverado HD pickup", "CHECK THE LOCAL USED MARKET")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a heavy-duty truck in twenty twenty-seven? First, whether you really need one, because a half-ton can do a lot. Second, the exact configuration, the engine, the axle, the payload and the towing figure on the door sticker. Third, the five-year resale value for that model. And fourth, whether the model is still being built, because the Silverado medium-duty shows that it can end.""",
   "Ford F-250 pickup", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The trucks that keep their value best": "Intro", "First, the whole class": "The whole class", "Number one": "1. Ram HD",
      "Number two": "2. Chevrolet Silverado HD", "Number three": "3. GMC Sierra HD", "Number four": "4. Ford Super Duty",
      "Number five": "5. Chevrolet Silverado medium-duty", "So what is the final twist": "The final twist",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video14", "length_scale": 2.0,
  "title": "Heavy-Duty Trucks in 2027: Sales Are Falling, But Why Do They Hold Value?", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
