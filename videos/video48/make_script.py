import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In nineteen twenty-five, Ford's first factory pickup cost two hundred eighty-one dollars. In twenty twenty-six, a fully loaded Ford pickup can cost one hundred twenty-two thousand. The average full-size pickup in America now sells for more than sixty-seven thousand dollars. And at least nine pickups on sale right now cost more than ninety thousand. Here are the most expensive pickups you can buy, and the twist about who is actually buying them.""",
   "Ford F-150 Raptor R", "$281 IN 1925. $122,265 IN 2026")
sc("""This is not just a story about rich buyers. Rising prices at the top pull up prices for everyone. When top trims sell well, carmakers build more of them and fewer basic trucks, and the average price climbs. That is one reason the cheapest full-size trucks are harder to find at dealers today. What happens at the top of the market affects your price too.""",
   "Ford F-150 dealership lot", "THE TOP PULLS EVERYONE UP")
sc("""We ranked them by real numbers. Fully loaded prices for the half-ton trucks, and starting prices for the electric super trucks. We will show you where the money goes, which options add tens of thousands of dollars, and why one of these trucks has a rooftop tent on the options list. And at the end, the checklist that keeps you from overpaying for any truck, at any price.""",
   "GMC Sierra Denali", "WHERE THE MONEY GOES")
sc("""Every number in this video comes from a published source, listed in the description. Prices change often, so always check the current price before you buy. If we could not confirm a figure, we left it out. First, a reality check on what normal trucks cost in twenty twenty-six.""",
   "pickup trucks dealership", "EVERY NUMBER IS SOURCED")

# ---------- CONTEXT ----------
sc("""According to Kelley Blue Book data from Cox Automotive, the average transaction price for a full-size pickup in September twenty twenty-six was sixty-seven thousand, five hundred seventy-three dollars, up one point five percent from a year earlier. The average for all new vehicles was fifty thousand, five hundred sixty-two. So a normal full-size truck costs about seventeen thousand dollars more than the average new vehicle.""",
   "Ford F-150 Chevrolet Silverado", "FULL-SIZE PICKUP AVG: $67,573")
sc("""And the brands are not equal. In the same report, Ram had the highest average transaction price of the major truck brands, at sixty-eight thousand, three hundred fifty-one dollars, up four point six percent. GMC averaged sixty-five thousand, five hundred thirty-two. Ford averaged fifty-nine thousand, nine hundred sixty-three, and Chevrolet forty-nine thousand, four hundred sixty-five. Those are brand averages across every vehicle they sell, not just trucks.""",
   "Ram 1500 Limited", "RAM BRAND AVG: $68,351")
sc("""Why are trucks so expensive? Part of it is what buyers ask for. Crew cabs, four-wheel drive, big screens, leather, driver assistance systems and powerful engines all add cost. Part of it is inflation and tariffs on vehicles and parts. And part of it is simple business. Trucks are among the most profitable vehicles carmakers sell, and top trims are where the biggest profits are.""",
   "pickup truck interior screen", "WHY TRUCKS COST SO MUCH")
sc("""Here is the twist. Back in two thousand two, Lincoln tried to sell a luxury pickup called the Blackwood for fifty-two thousand dollars, and it flopped. Buyers said it was too expensive. Today, the average full-size pickup costs much more than that. The luxury truck that failed in two thousand two is cheaper than a normal truck in twenty twenty-six, at least on paper, before inflation.""",
   "Lincoln Blackwood", "TWIST: THE $52K FLOP")

# ---------- 5. ZR2 BISON ----------
sc("""Now the list. We start with the five most expensive half-ton pickups, ranked by Pickup Truck Talk in January twenty twenty-six, with every option and the destination fee added. Number five is the Chevrolet Silverado fifteen hundred Z R two A E V Bison, at ninety-two thousand, six hundred three dollars fully loaded.""",
   "Chevrolet Silverado ZR2", "5. SILVERADO ZR2 BISON: $92,603")
sc("""The Z R two is Chevy's serious off-road truck, and the Bison package, built with the off-road company A E V, adds armor, special bumpers and skid plates. The loaded truck uses the six point two liter V eight. Pickup Truck Talk added an eight hundred fifty dollar air intake and a one hundred ninety-five dollar active exhaust. According to CarGurus, the regular Silverado Z R two starts at seventy-four thousand five hundred ninety-five.""",
   "Chevrolet Silverado ZR2 Bison", "ZR2 BASE: $74,595")
sc("""The Bison is also a reminder of how much off-road capability now costs. Twenty years ago, an off-road package might add a few thousand dollars for skid plates and better shocks. Today, a full off-road truck with armor, special suspension and big tires sits near the top of the price list. Off-road is no longer an option. It is a luxury category of its own.""",
   "Chevrolet Silverado ZR2 Bison off-road", "OFF-ROAD IS A LUXURY NOW")
sc("""And here is the twist. Pickup Truck Talk called it the most affordable half-ton for twenty twenty-six with all options added. Read that again. The cheapest truck on a list of the most expensive trucks still costs more than ninety-two thousand dollars. That tells you how high the ceiling has climbed.""",
   "Chevrolet Silverado ZR2 off-road", "THE 'CHEAPEST' IS $92K")

# ---------- 4. TUNDRA CAPSTONE ----------
sc("""Number four is the Toyota Tundra Capstone, at ninety-eight thousand, four hundred forty-one dollars fully loaded. The Capstone is Toyota's luxury Tundra, with a hybrid powertrain. According to CarGurus, it starts at eighty-two thousand, nine hundred ninety-five dollars, and the i-Force Max hybrid makes four hundred thirty-seven horsepower and five hundred eighty-three pound-feet of torque.""",
   "Toyota Tundra Capstone", "4. TUNDRA CAPSTONE: $98,441")
sc("""How does a Tundra get to almost one hundred thousand dollars? The options. According to Pickup Truck Talk, they included a two thousand five hundred dollar Dometic rooftop tent, a one thousand seven hundred nine dollar A R B fridge and freezer, and a nine hundred ninety dollar A R B portable compressor. Toyota offers so many accessories that the Tundra slipped past the Chevy.""",
   "Toyota Tundra rooftop tent", "A $2,500 ROOFTOP TENT")
sc("""This shows a new trend in expensive trucks: the overlanding lifestyle. Buyers want a truck that can take them into the wilderness and let them sleep there. Rooftop tents, fridges and air compressors used to be aftermarket products. Now some carmakers sell them right on the order sheet, and roll them into the truck loan.""",
   "overlanding truck camping", "THE OVERLANDING BOOM")
sc("""The twist is that the Tundra is not a big seller next to the Detroit trucks. According to autoevolution, it sold one hundred ten thousand and eighty units through September twenty twenty-six. But Toyota has found that the buyers it does have are willing to spend a lot. The brand's average transaction price, across all its vehicles, rose four point nine percent in September, the biggest increase of the major truck brands.""",
   "Toyota Tundra 2026", "TOYOTA ATP: +4.9%")

# ---------- 3. DENALI ULTIMATE ----------
sc("""Number three is the G M C Sierra fifteen hundred Denali Ultimate, at ninety-nine thousand, six hundred thirty-nine dollars fully loaded. According to Pickup Truck Talk, it starts at eighty-four thousand four hundred, and the author called it a luxurious dream. It has open-pore wood, premium leather and a huge screen. It is G M C's answer to the luxury car.""",
   "GMC Sierra Denali Ultimate", "3. SIERRA DENALI ULTIMATE: $99,639")
sc("""The options say a lot about this buyer. Pickup Truck Talk added a one thousand ninety-five dollar Glacier White Tricoat paint and a three thousand eight hundred ninety-five dollar Brembo brake upgrade. And according to CarGurus, the Denali Ultimate can be ordered with a three liter Duramax diesel inline six, with three hundred five horsepower and four hundred ninety-five pound-feet of torque.""",
   "GMC Sierra Denali", "$3,895 BRAKES, $1,095 PAINT")
sc("""The Denali Ultimate is aimed at a buyer who might otherwise buy a luxury S U V. It offers the same kind of interior quality, with the added ability to tow and haul. For many families, it is a single vehicle that replaces two. That is the argument G M C makes, and it is why the brand can charge so much.""",
   "GMC Sierra Denali Ultimate interior", "ONE VEHICLE REPLACES TWO")
sc("""Here is the twist. The Sierra is built on the same basic platform as the Chevrolet Silverado. So G M C is selling the same engineering for much more money, by changing the brand, the interior and the image. And it works. In September twenty twenty-six, G M C's average transaction price was sixty-five thousand, five hundred thirty-two dollars, far above Chevrolet's forty-nine thousand, four hundred sixty-five.""",
   "GMC Sierra Chevrolet Silverado", "SAME PLATFORM, $16K MORE (AVG)")

# ---------- 2. RAM RHO ----------
sc("""Number two is the Ram fifteen hundred R H O, at one hundred thousand, four hundred fifty-nine dollars fully loaded. It is the first truck on the list to break one hundred thousand. According to Pickup Truck Talk, the R H O starts just north of seventy-three thousand dollars, and the author added a nine thousand nine hundred ninety-five dollar R H O Level One Equipment Group.""",
   "Ram 1500 RHO", "2. RAM 1500 RHO: $100,459")
sc("""The R H O is Ram's high-performance off-road truck, powered by the high output version of the three liter Hurricane inline six. According to CarGurus, that engine makes five hundred forty horsepower and five hundred twenty-one pound-feet of torque. It replaced the supercharged T R X for a year, as Ram's answer to the Ford Raptor.""",
   "Ram 1500 RHO off-road", "HURRICANE HO: 540 HP")
sc("""And here is the twist. Ram is not stopping there. In January twenty twenty-six, according to Pickup Truck Talk, Ram announced the return of the T R X for the twenty twenty-seven model year, with a supercharged six point two liter V eight, seven hundred seventy-seven horsepower, and a price just shy of one hundred thousand dollars before destination fees and likely dealer markups. Pickup Truck Talk noted that the T R X will obviously change this list for twenty twenty-seven.""",
   "Ram TRX", "2027 TRX: 777 HP, ~$100K")
sc("""Think about what this means for the Ford Raptor. For years, Ford had the high-performance off-road truck market almost to itself. Now Ram has both the R H O and the returning T R X. The fight over the fastest, most extreme pickup is one of the most expensive arms races in the car business, and every new round pushes prices higher.""",
   "Ford F-150 Raptor Ram TRX", "THE $100K ARMS RACE")
sc("""Ram also has the Tungsten, its most luxurious fifteen hundred. According to CarGurus, it starts at ninety-one thousand, five hundred ninety-five dollars. That makes Ram the brand with two different trucks starting around or above ninety thousand: one for luxury, one for speed. It also helps explain why Ram has the highest average transaction price of the big truck brands.""",
   "Ram 1500 Tungsten", "RAM TUNGSTEN: $91,595 START")

# ---------- 1. RAPTOR R ----------
sc("""Number one among the half-tons is the Ford F-one-fifty Raptor R, at one hundred twenty-two thousand, two hundred sixty-five dollars fully loaded, according to Pickup Truck Talk. It has a five point two liter supercharged V eight with seven hundred twenty horsepower. It is a desert racing truck that you can buy at a Ford dealer.""",
   "Ford F-150 Raptor R", "1. F-150 RAPTOR R: $122,265")
sc("""How much do the options add? According to Pickup Truck Talk, nearly forty thousand dollars. That is more than the price of many new cars, just in options. A buyer could buy a whole Ford Maverick for the cost of the extras on this one truck. According to The Truth About Cars, the Maverick currently starts at about thirty thousand dollars.""",
   "Ford Maverick", "OPTIONS: NEARLY $40,000")
sc("""The Raptor R also shows how performance trucks hold their appeal. The original S V T Lightning from the nineties went from about twenty thousand dollars to forty-eight thousand seven hundred for good examples between twenty sixteen and twenty twenty-four, according to Ford Authority. Special, limited performance trucks can become collectibles. That does not happen to every expensive truck, but it does happen to some.""",
   "Ford SVT Lightning", "SOME BECOME COLLECTIBLES")
sc("""Here is the twist. The F-one-fifty is the best-selling truck line in America, with eight hundred twenty-eight thousand, eight hundred thirty-two F-Series sold in twenty twenty-five, according to Ford. The same nameplate covers trucks from the basic work truck to a one hundred twenty thousand dollar Raptor R. That range is one of the secrets of the F-Series. There is an F-one-fifty for almost every budget.""",
   "Ford F-150 XL work truck", "ONE NAME, $40K TO $122K")

# ---------- EV SUPER TRUCKS ----------
sc("""Now the electric super trucks, because they push the price even higher. According to CarGurus in June twenty twenty-six, the G M C Hummer E V Pickup three X starts at one hundred seven thousand, nine hundred ninety-five dollars. It has three motors, one thousand horsepower, more than one thousand pound-feet of torque, and about three hundred fifty miles of range.""",
   "GMC Hummer EV pickup", "HUMMER EV 3X: $107,995")
sc("""The Chevrolet Silverado E V R S T Max Range is listed by CarGurus at one hundred eight thousand, four hundred forty-five dollars. The Tesla Cybertruck Cyberbeast is listed at one hundred eight thousand, seven hundred sixty, with zero to sixty in two point six seconds. And the most expensive of all is the Rivian R one T Quad, at one hundred fifteen thousand, nine hundred ninety dollars plus destination, with one thousand twenty-five horsepower.""",
   "Rivian R1T", "RIVIAN R1T QUAD: $115,990")
sc("""And here is the biggest twist of the video. These are some of the most powerful pickups ever built, and they are struggling to sell. According to Cox Automotive estimates reported by InsideEVs, Cybertruck sales fell to about twenty thousand two hundred in twenty twenty-five. Ford ended the all-electric F-one-fifty Lightning after a nineteen point five billion dollar charge, according to Fox Business. The most expensive trucks are not always the ones buyers want.""",
   "Tesla Cybertruck", "MOST POWERFUL, HARDEST TO SELL")
sc("""The electric trucks are also the most powerful on the list by far. One thousand horsepower in the Hummer and more than one thousand in the Rivian. That is more than double many supercars from twenty years ago. But truck buyers do not buy on horsepower alone. They buy on towing range, charging, and price, and that is where the electric trucks lose ground.""",
   "Rivian R1T GMC Hummer EV", "1,000 HP ISN'T ENOUGH")
sc("""Why? Price is part of it. When a truck costs more than one hundred thousand dollars, the buyer pool gets tiny. And the end of the federal electric vehicle tax credit in twenty twenty-five made the gap wider. A gas Raptor R or a Denali Ultimate sells to a buyer who already loves trucks. An electric super truck has to convince that buyer to change everything at once.""",
   "Chevrolet Silverado EV", "WHY $100K EVs STRUGGLE")

# ---------- WHO BUYS ----------
sc("""Here is a quick way to compare all of these trucks. Divide the fully loaded price by the horsepower. The Raptor R, at about one hundred twenty-two thousand dollars and seven hundred twenty horsepower, costs about one hundred seventy dollars per horsepower. The Rivian, at about one hundred sixteen thousand dollars and more than one thousand horsepower, costs much less per horsepower. Numbers like that show why buyers do not choose trucks on power alone.""",
   "Ford F-150 Raptor R Rivian R1T", "PRICE PER HORSEPOWER")
sc("""And price per capability tells another story. A heavy-duty diesel truck can tow far more than any of these half-ton trucks, often for less money. If towing is the job, the most expensive half-ton is rarely the best tool. The top trims on this list are about luxury, speed and image as much as work.""",
   "Ram 3500 towing", "WHAT ARE YOU PAYING FOR?")
sc("""So who is buying ninety and one hundred thousand dollar pickups? For many, a top-trim truck replaces a luxury car. It carries the family, tows the boat, and has the leather and screens of a premium sedan. For business owners, a truck can also come with tax and business-use considerations, which is something to discuss with an accountant, not a salesperson.""",
   "GMC Sierra Denali interior", "WHO BUYS $100K TRUCKS?")
sc("""And here is the twist on financing. Most buyers do not pay cash. A higher price means a bigger loan and more interest. A truck that looks affordable as a monthly payment can cost far more over a long loan. That is why the sticker price is only the beginning of the real cost of an expensive truck.""",
   "car loan paperwork", "THE PAYMENT TRAP")
sc("""There is also depreciation. Expensive trucks often lose more dollars in value in their first years, simply because there are more dollars to lose. A one hundred thousand dollar truck that loses a third of its value has lost more than thirty thousand dollars. Some special models, like limited performance trucks, can hold value well. Many luxury trims do not.""",
   "used pickup trucks lot", "MORE DOLLARS TO LOSE")

# ---------- PATTERN ----------
sc("""And remember the heavy-duty trucks. Fully loaded versions of the Ford Super Duty, the Ram heavy-duty and the Silverado and Sierra heavy-duty trucks, with diesel engines and top trims, can also climb into six figures. For buyers who tow very heavy trailers, those trucks are tools, not toys, and the price reflects the engineering needed to pull that weight.""",
   "Ford F-450 Super Duty", "HEAVY-DUTY: ALSO SIX FIGURES")
sc("""So what is the pattern? The most expensive pickups fall into three groups. Luxury trucks, like the Denali Ultimate, the Tungsten and the Capstone. Performance off-road trucks, like the Raptor R, the R H O and the Z R two Bison. And electric super trucks, like the Hummer E V, the Cybertruck and the Rivian. Each group is chasing a different buyer.""",
   "Ford F-150 Raptor Ram RHO", "3 KINDS OF $100K TRUCKS")
sc("""And the final twist. The truck that made pickups popular, the Model T runabout, cost two hundred eighty-one dollars in nineteen twenty-five, according to The Henry Ford. It was built to be affordable for anyone who worked. One hundred years later, the most expensive pickups cost more than many houses did a few decades ago. The pickup went from the cheapest vehicle you could buy to one of the most expensive.""",
   "Ford Model T pickup", "FROM CHEAPEST TO PRICIEST")

# ---------- CLOSE ----------
sc("""So how do you avoid overpaying, at any price? First, compare the average transaction price, not the sticker. If full-size trucks average about sixty-seven thousand dollars, know where your truck sits against that. Second, look at what each option really costs. On a fully loaded truck, options can add tens of thousands of dollars that you may never use.""",
   "pickup truck window sticker", "CHECKS 1 AND 2: AVERAGE, OPTIONS")
sc("""A good test is to price the truck two ways. First, the exact truck you want, fully loaded. Then the same truck with only the options you will really use every week. The difference is often ten or twenty thousand dollars. Ask yourself whether those extras are worth that money over the years you will own the truck, including the interest on the loan.""",
   "pickup truck configurator", "PRICE IT TWO WAYS")
sc("""Also check the trims just below the top. A Lariat instead of a Platinum, an S L T instead of a Denali Ultimate, or a Laramie instead of a Tungsten often delivers most of the comfort for thousands of dollars less. The top trim is where carmakers make their biggest margins, and the step below is often where buyers get the best value.""",
   "Ford F-150 Lariat", "THE TRIM BELOW THE TOP")
sc("""Third, watch for dealer markups on hot models, like the new T R X. Fourth, compare the same engineering under different badges, like Silverado and Sierra. And fifth, count the full cost: loan interest, insurance, fuel and depreciation over five years. The real price of an expensive truck is much higher than the number on the window.""",
   "truck dealership negotiation", "CHECKS 3, 4 AND 5")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the numbers to compare and the questions to ask every dealer. The link is in the description and in the pinned comment. Subscribe for the next video, where we go to the other end of the market: the cheapest new trucks in America. Thanks for watching.""",
   "Ford F-150 Raptor R", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In nineteen twenty-five, Ford's first": "Intro", "According to Kelley Blue Book": "What a normal truck costs in 2026",
      "Now the list.": "5. Chevrolet Silverado ZR2 Bison", "Number four": "4. Toyota Tundra Capstone",
      "Number three": "3. GMC Sierra Denali Ultimate", "Number two": "2. Ram 1500 RHO (and the 2027 TRX)",
      "Number one among": "1. Ford F-150 Raptor R", "Now the electric super trucks": "The $100,000+ electric trucks",
      "So who is buying": "Who buys them and the real cost", "So how do you avoid": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video48", "length_scale": 1.4,
  "title": "The Most Expensive Pickups You Can Buy in 2026 (One Costs $122,265)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
