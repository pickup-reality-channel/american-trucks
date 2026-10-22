import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Ford just cut the price of two Maverick trims by thousands of dollars, and at the same time, took the turbo engine away from two others. The truck that started at twenty-two thousand, five hundred dollars in twenty twenty-two is changing again for twenty twenty-seven. And the numbers behind it explain why. Here is what changed on the twenty twenty-seven Ford Maverick, and who should buy it.""",
   "Ford Maverick pickup", "2027 FORD MAVERICK: WHAT CHANGED")

# ---------- COLD OPEN ----------
sc("""The Ford Maverick is the cheapest truck you can actually buy in America, and one of the fastest-growing. Through nine months of twenty twenty-six, Ford sold one hundred twenty-three thousand, six hundred eighty-one of them, up two point three percent, and seventy-four thousand, three hundred were hybrids. In the third quarter alone, it sold forty-one thousand, nine hundred seventy, up twenty point four percent.""",
   "Ford Maverick Hybrid pickup", "MAVERICK: 123,681 IN 9 MONTHS")
sc("""For the twenty twenty-seven changes, our main source is a report by The Truth About Cars, published on August twenty-eighth, twenty twenty-six, which covers a pricing document for the new model year. We also use Autoblog and Ford's own sales releases, plus iSeeCars for resale. Pricing documents can change before the trucks arrive, so treat the twenty twenty-seven prices as reported, not final. Every source is listed in the description.""",
   "Ford Maverick Lariat pickup", "SOURCE: TRUTH ABOUT CARS, AUG 28, 2026")
sc("""There is a twist in each change. One price cut is about four thousand dollars. One engine disappears from the cheapest trims. One towing package finally reaches the hybrid. And one very small number tells you how much this truck has changed since it launched. Stay with me, because the last twist is about what you should do before you order.""",
   "Ford Maverick Lobo pickup", "FOUR CHANGES. FOUR TWISTS.")

# ---------- 1. LOBO PRICE CUT ----------
sc("""Change number one is the price of the Lobo. According to The Truth About Cars, the twenty twenty-seven Maverick Lobo starts at thirty-two thousand, one hundred fifty-five dollars, without destination. That is about thirty-eight hundred dollars less than for twenty twenty-six. It is a higher trim, and the cut brings it much closer to the rest of the range.""",
   "Ford Maverick Lobo pickup", "LOBO: $32,155, ABOUT $3,800 LESS")
sc("""The twist is the Lobo High, the more equipped version. The article says it is about four thousand, three hundred dollars cheaper than before, but it does not give an exact price. And that matters, because a bigger cut on a more expensive trim brings the whole range closer together. A buyer who was choosing between a basic Maverick and a Lobo may find that the gap is much smaller than last year.""",
   "Ford Maverick Lobo High pickup", "LOBO HIGH: ABOUT $4,300 LESS")

# ---------- 2. TREMOR PRICE CUT ----------
sc("""Change number two is the Tremor. The off-road version drops to thirty-seven thousand, one hundred fifty-five dollars, about thirty-five hundred dollars less than earlier this year, according to The Truth About Cars. That is still the most expensive Maverick, and it is still a truck that costs more than the starting price of a Toyota Tacoma, which Autoblog lists at thirty-two thousand, one hundred forty-five.""",
   "Ford Maverick Tremor pickup", "TREMOR: $37,155, ABOUT $3,500 LESS")
sc("""Here is the twist. In a year when the average price of a full-size truck rose to sixty-seven thousand, four hundred forty-six dollars, and TFL Car found that the popular full-size trims rose between six and twelve percent over two years, Ford is making its small truck cheaper in the trims that cost the most. That is a very different direction from the rest of the market, and it says something about where Ford sees the competition.""",
   "Ford Maverick Tremor off-road pickup", "FORD CUTS WHILE THE MARKET RISES")

# ---------- 3. THE TURBO ----------
sc("""Change number three is the engine. For twenty twenty-seven, the two liter turbo is removed as an option from the XL and the Lariat. The article says it is now available only on the more expensive trims. The turbo makes two hundred fifty horsepower and two hundred seventy-seven pound-feet, with an eight-speed automatic, or a seven-speed on the Lobo. The hybrid makes one hundred ninety-one horsepower combined with a CVT.""",
   "Ford Maverick turbo engine", "TURBO REMOVED FROM XL AND LARIAT")
sc("""The twist is the price of the turbo. With the XL and the Lariat losing it, the cheapest way to get the turbo is the XLT, and the article says an all-wheel drive XLT with the turbo should start at about thirty-three thousand dollars, including destination. So adding the turbo gets harder, and a few thousand dollars more expensive. The cheapest Maverick you can buy in twenty twenty-seven will be a hybrid, and that matches what buyers are already choosing.""",
   "Ford Maverick XLT pickup", "CHEAPEST TURBO: XLT, ~$33,000")
sc("""And buyers are choosing the hybrid in huge numbers. Ford sold seventy-four thousand, three hundred Maverick Hybrids through nine months, about sixty percent of all Mavericks. In the third quarter, it was twenty-seven thousand, seven hundred ninety-three, a record, up fifty-nine point six percent. So Ford is removing an option that fewer people choose, and putting more attention on the one that most people choose. That is a business decision with the data to support it.""",
   "Ford Maverick Hybrid pickup", "HYBRID: ~60% OF MAVERICKS")

# ---------- 4. THE TOWING PACKAGE ----------
sc("""Change number four is the towing package. According to The Truth About Cars, the four thousand pound towing package, which was previously available only with the turbo, is now also available on the hybrids. That is a real change for buyers who want the fuel economy of the hybrid and a trailer. Autoblog lists the hybrid at forty-two miles per gallon in the city, and a payload of fifteen hundred pounds.""",
   "Ford Maverick towing trailer", "4,000-LB TOW PACKAGE NOW ON HYBRIDS")
sc("""The twist is the size of the number. Four thousand pounds is a small trailer, much less than the thirteen thousand, five hundred pounds that Ford quotes for the best F-one-fifty, or the six thousand, five hundred that Autoblog lists for the Tacoma. For a Maverick, it is enough for a small boat, a camper trailer or a utility trailer. For anything heavier, you need a bigger truck. So the news is good, but it should be read carefully.""",
   "Ford Maverick pickup truck", "4,000 LB: A SMALL TRAILER")

# ---------- THE PRICE HISTORY ----------
sc("""Now the number that tells you how the Maverick has changed. The article notes that the twenty twenty-two launch price was twenty-two thousand, five hundred dollars, including destination. Autoblog lists the Maverick Hybrid XL at twenty-eight thousand, one hundred forty-five dollars in June of twenty twenty-six. That is an increase of about five thousand, six hundred dollars, or about twenty-five percent, over four years, though the sources are not directly comparable.""",
   "Ford Maverick first generation pickup", "2022: $22,500. 2026: $28,145.")
sc("""Why does that matter? Because it shows what happened to the cheapest truck in America. It got more expensive, and it also got more popular. Ford sold more than one hundred twenty thousand in nine months, and the hybrid took the lead. That tells you something about the buyers. They did not leave when the price went up. They chose the hybrid, and they accepted the rise. The question for twenty twenty-seven is whether the price cuts on the Lobo and Tremor bring a new group of buyers.""",
   "Ford Maverick pickup", "BUYERS ACCEPTED THE RISE")


# ---------- THE SALES YEAR ----------
sc("""To understand the changes, look at how the Maverick sold through the year. In the first half of twenty twenty-six, Ford sold eighty-one thousand, seven hundred eleven Mavericks, down five percent. In the second quarter alone, forty-seven thousand, eight hundred fifty, down four tenths of a percent. Then came the third quarter, with forty-one thousand, nine hundred seventy, up twenty point four percent. So the year started soft and finished strong.""",
   "Ford Maverick pickup truck", "H1: -5.0%. Q3: +20.4%.")
sc("""The hybrid tells the same story, only louder. In the second quarter, Ford sold twenty-nine thousand, four hundred fifty-seven Maverick Hybrids, a second-quarter record, up nineteen point three percent. In the first half, forty-six thousand, five hundred seven. And in the third quarter, twenty-seven thousand, seven hundred ninety-three, up fifty-nine point six percent. By the end of September, seventy-four thousand, three hundred, a record for the model.""",
   "Ford Maverick Hybrid pickup", "HYBRID RECORDS: Q2 AND Q3")
sc("""Now the twist inside those numbers. If the hybrid sold seventy-four thousand, three hundred, and the whole Maverick sold one hundred twenty-three thousand, six hundred eighty-one, then the non-hybrid Maverick, the one with the turbo, sold about forty-nine thousand, three hundred eighty-one. That is about forty percent of the total. So the turbo is not a small niche. It is two out of every five Mavericks. Removing it from the XL and the Lariat will affect a lot of buyers.""",
   "Ford Maverick XLT pickup", "TURBO: ~49,381, ABOUT 40% OF SALES")
sc("""That is an important detail, because it changes how to read the news. The report says that the turbo is removed from two trims, and that it remains on others. So the buyers who want it can still get it, but they will pay for a higher trim. For a buyer who wanted a basic truck with the stronger engine, the twenty twenty-seven Maverick makes that choice more expensive. And for Ford, that could mean more money per truck.""",
   "Ford Maverick pickup", "A STRONGER ENGINE COSTS MORE")

# ---------- PRICE COMPARISON ----------
sc("""Let's compare the Maverick's price with the trucks near it, using the Autoblog list of cheapest trucks, published in June. The Maverick Hybrid XL, twenty-eight thousand, one hundred forty-five. The Hyundai Santa Cruz SE, twenty-nine thousand, seven hundred fifty. The Toyota Tacoma SR XtraCab, thirty-two thousand, one hundred forty-five. The Chevrolet Colorado, thirty-two thousand, four hundred. The Ford Ranger XL, thirty-three thousand, three hundred fifty.""",
   "Ford Maverick Toyota Tacoma Ford Ranger pickups", "PRICES: MAVERICK $28,145 TO RANGER $33,350")
sc("""The gap between the Maverick and the Ranger, a truck from the same company, is five thousand, two hundred five dollars. And the gap to the Tacoma is four thousand dollars. A buyer who chooses the Maverick is not only choosing a smaller truck. They are saving about four to five thousand dollars at purchase. And as we saw in the resale numbers, the Maverick holds about sixty-eight percent of its value, so the savings do not disappear later.""",
   "Ford Ranger pickup", "MAVERICK SAVES $4,000-$5,200")
sc("""But the Tacoma keeps eighty and a half percent. If you buy a Maverick for twenty-eight thousand, one hundred forty-five and a Tacoma for thirty-two thousand, one hundred forty-five, the estimate for five-year value is about nineteen thousand, one hundred ninety-five dollars for the Maverick, and twenty-five thousand, eight hundred seventy-seven for the Tacoma. The Maverick loses about eight thousand, nine hundred fifty. The Tacoma loses about six thousand, two hundred sixty-eight. The cheaper truck can lose more.""",
   "Toyota Tacoma pickup", "5-YEAR LOSS: MAVERICK ~$8,950. TACOMA ~$6,268.")
sc("""That does not make the Maverick a bad choice. It makes it a different choice. The Maverick costs less to buy, and the hybrid uses less fuel, forty-two miles per gallon in the city, according to Autoblog. The Tacoma costs more, tows more, and holds its value better. Which one is cheaper to own depends on how much you drive, how long you keep the truck, and what you need it to do. Both are reasonable answers.""",
   "Ford Maverick Hybrid pickup", "DIFFERENT TRUCKS, DIFFERENT MATH")

# ---------- RESALE AND COMPETITION ----------
sc("""Let's put the Maverick in context. It keeps sixty-eight point two percent of its value after five years, according to iSeeCars, the best of the compact trucks. The Hyundai Santa Cruz keeps sixty-five point one. The Santa Cruz sold fourteen thousand, eight hundred eleven through nine months, down twenty-eight percent, and twenty twenty-six is reported to be its last model year. So the Maverick is nearly alone in its class.""",
   "Hyundai Santa Cruz pickup", "MAVERICK RESALE: 68.2%")
sc("""And a new rival is coming. The Slate electric truck was priced at twenty-four thousand, nine hundred fifty dollars in June, with an estimated range of two hundred five miles, and first deliveries expected by the end of twenty twenty-six. That is about thirty-two hundred dollars below the Maverick Hybrid. It has no screen, one body color, and it is sold directly, without dealers. If it arrives as promised, the Maverick will have its first real rival in the low-price class.""",
   "Slate Auto electric truck", "SLATE: $24,950, NOT YET DELIVERED")

# ---------- WHO SHOULD BUY ----------
sc("""So who should buy the twenty twenty-seven Maverick? A city driver, a first-time buyer, or someone who wants a simple, efficient truck for light work. The hybrid is the sensible default, and the price is the lowest of any new truck you can drive off a lot. And who should not? Someone who tows more than four thousand pounds, someone who needs a large bed, or someone who wants the turbo and does not want to pay for the XLT.""",
   "Ford Maverick Hybrid pickup", "WHO: CITY DRIVERS. NOT: HEAVY TOWERS.")
sc("""The final twist is about the Lobo and Tremor price cuts. They are the most visible news, and they are the least likely to matter to most buyers. Most Mavericks sold are hybrids, so the cuts may matter less to most buyers. The real value of the cuts is that they show Ford is willing to move prices to keep volume. And that gives a buyer room to negotiate. When a company cuts the price of two trims, the other trims may also get better offers.""",
   "Ford Maverick Lobo pickup", "CUTS SIGNAL ROOM TO NEGOTIATE")
sc("""Before you order, check three things. First, the real price with the destination fee, because the prices in the pricing document exclude it, and Ford's fee was not stated in the report we used. Second, the exact engine you are getting, because the turbo is now on fewer trims. And third, whether the towing package is included, because it is an option. The Maverick is a simple truck, but its options are not always simple.""",
   "Ford Maverick XLT pickup", "CHECK PRICE, ENGINE AND TOW PACKAGE")

# ---------- BUYER GUIDE: HOW TO USE THESE NUMBERS ----------
sc("""Before the checklist, a word about how to read these prices. They come from a pricing document reported on August twenty-eighth, and The Truth About Cars says they can change before the trucks arrive. They also leave out the destination fee. So a thirty-two thousand, one hundred fifty-five dollar Lobo is a starting point, and not a quote. The practical rule is to ask for the out-the-door price in writing, with the destination fee, the taxes and the options on separate lines, and to check the date on the quote.""",
   "Ford Maverick Lobo pickup", "PRICES ARE AS REPORTED, NOT FINAL")
sc("""Now the price cuts. The Lobo is about thirty-eight hundred dollars lower, and the Tremor is about thirty-five hundred lower. Those are real savings, but they only help if you want those trims. The way to test is to put the trims side by side at one dealer on one day, and ask what each one costs with the same options. If the gap between two trims is small, the more equipped one may be the better value. If it is large, the cheaper one may give you everything you actually use.""",
   "Ford Maverick Tremor pickup", "LINE UP THE TRIMS ON THE SAME DAY")
sc("""Let's think about hybrid versus turbo as a decision and not as a spec sheet. The hybrid makes one hundred ninety-one horsepower and gets forty-two miles per gallon in the city, according to Autoblog. The turbo makes two hundred fifty horsepower and two hundred seventy-seven pound-feet. If most of your driving is in town, the hybrid is the sensible default. If you want quicker passing and more power with a trailer, the turbo is the one. Drive both, back to back, because the numbers do not tell you which one you will enjoy.""",
   "Ford Maverick Hybrid pickup", "HYBRID OR TURBO: DRIVE BOTH")
sc("""Now the towing package, and how to verify it. The four thousand pound package is now offered on the hybrid, but it is an option, and not every truck on the lot will have it. Ask for it in writing for the exact truck you are buying, and then check the door sticker for the towing and payload figures. Match them to your trailer, with some margin. Four thousand pounds is a small trailer, so weigh the trailer loaded, not empty. If it is close to the limit, you want a bigger truck.""",
   "Ford Maverick towing trailer", "CHECK THE STICKER FOR TOWING AND PAYLOAD")
sc("""A caution about the price history. The twenty twenty-two launch price of twenty-two thousand, five hundred dollars and the twenty twenty-six hybrid price of twenty-eight thousand, one hundred forty-five come from different sources, and the article says they are not directly comparable. So do not treat the difference as an exact measure of inflation. What matters for you is the quote in front of you today. Use the older figure only as a reminder that the cheapest truck in America has become more expensive, and that buyers kept coming anyway.""",
   "Ford Maverick first generation pickup", "DO NOT OVER-READ THE PRICE HISTORY")
sc("""What about the Slate and the Santa Cruz? The Slate was priced at twenty-four thousand, nine hundred fifty dollars and its first deliveries are expected by the end of twenty twenty-six, but it has not been delivered yet, and it is sold without dealers. If you can wait, watching its first owners is cheap. The Santa Cruz is reported to be ending after twenty twenty-six, so if you are looking at one, ask how parts and service will be handled. Neither changes the Maverick's position today, but both are worth knowing.""",
   "Slate Auto electric truck", "SLATE AND SANTA CRUZ: WORTH WATCHING")
sc("""And the mistakes we see with small trucks. Assuming the cheapest trim has the turbo, when the XL and the Lariat will not. Forgetting the destination fee. Stretching to the Tremor for looks, when the hybrid would do everything you need. Skipping a test drive of the other engine. And not asking for the towing package in writing. The Maverick is a simple truck, and a patient buyer with a written quote and a checked sticker will usually get the right one.""",
   "Ford Maverick XLT pickup", "COMMON BUYER MISTAKES")

sc("""To pull it together, here is a simple routine for ordering a Maverick. Decide first whether you need the turbo or the hybrid, and be honest about how you drive. Decide whether you will tow, and how heavy the trailer is. Then ask for the out-the-door price on the exact trim, in writing, with the destination fee. Compare it with the Ranger, the Tacoma and the Colorado prices from the Autoblog list, so you see the whole range. And if you are not in a hurry, check what the Slate does when it arrives. A small truck rewards a patient buyer more than a fast one.""",
   "Ford Maverick pickup", "A SIMPLE ROUTINE BEFORE YOU ORDER")
sc("""One more way to think about it. The Maverick costs less than most trucks, so a small mistake costs less too, but the numbers show that small mistakes still add up. A few thousand dollars on the wrong trim, a missing tow package, or a fee nobody mentioned can erase the savings you came for. That is why the written quote matters so much. It turns a friendly conversation into a number you can compare, and a number you can compare is the best tool a buyer has, no matter how cheap the truck is.""",
   "Ford Maverick Hybrid pickup", "A WRITTEN QUOTE IS YOUR BEST TOOL")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a small truck in twenty twenty-seven? First, the full price, with every fee. Second, the powertrain on the exact trim. Third, the towing and payload for your use. And fourth, the five-year resale value, and whether the model is still being built. We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Ford Maverick pickup", "CHECK 1, 2, 3 AND 4")
sc("""If you want to know how the Nissan Frontier changes for twenty twenty-seven, subscribe, because that is coming next. Thanks for watching.""",
   "Nissan Frontier pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Ford just cut the price": "Intro", "Change number one": "1. The Lobo price cut", "Change number two": "2. The Tremor price cut",
      "Change number three": "3. The turbo is removed", "Change number four": "4. The towing package",
      "Now the number that tells you": "The price history", "So who should buy": "Who should buy it",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video16", "length_scale": 1.55,
  "title": "2027 Ford Maverick: Price Cuts, No More Turbo on Cheap Trims (What Changed)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
