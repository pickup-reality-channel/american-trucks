import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One electric truck lost seventy-nine percent of its sales in a single year, and it is the best-known electric pickup in America. Another one was cancelled before a single customer got it. A third one has a price tag of twenty-four thousand, nine hundred fifty dollars, and nobody has driven it yet. This is what really happened to the electric truck boom.""",
   "Ford F-150 Lightning electric pickup", "EV TRUCK BOOM: WHAT HAPPENED")

# ---------- COLD OPEN ----------
sc("""Just a few years ago, every carmaker promised the same future. The pickup truck, the most profitable vehicle in America, was going electric. Ford built a plant for it. General Motors built a factory for it. Tesla built a futuristic truck out of stainless steel. Billions of dollars were committed. Then, in twenty twenty-five and twenty twenty-six, the plans started to fall apart, one by one.""",
   "Ford F-150 Lightning pickup", "THE PROMISE: AN ELECTRIC FUTURE")
sc("""Here is the number that shows how big the gap is. Through the first nine months of twenty twenty-six, Ford sold five hundred fifty-six thousand, seven hundred thirty-eight F-Series trucks, not counting the electric Lightning. Now take the four electric truck lines that report numbers, the Lightning, the Silverado EV, the Sierra EV and the Hummer EV, and add them together. Nineteen thousand, eight hundred twenty-six. Less than four percent of the F-Series alone.""",
   "Ford F-150 pickup truck", "9 MONTHS 2026: F-SERIES 556,738")
sc("""So the electric truck boom did not slow down. In most cases, it simply stopped. But the real story is not that one company made a mistake. Every electric truck has its own twist, and some of them are strange. One was killed by its own success. One was cancelled and then came back as something else. And the last one on this list might be the most interesting, because it is not from Detroit at all.""",
   "Chevrolet Silverado EV", "EVERY EV TRUCK HAS A TWIST")
sc("""Stay with me, because by the end of this video you will know exactly which electric trucks are still being built, which ones are gone, and what the numbers say about buying one in twenty twenty-seven. Every figure comes from a published source, and the sources are listed in the description. If a number could not be confirmed, we left it out. Let's begin with the biggest fall of all.""",
   "Ford F-150 Lightning charging", "EVERY NUMBER IS SOURCED")

# ---------- 1. FORD F-150 LIGHTNING ----------
sc("""Number one is the Ford F-150 Lightning. It was the electric truck everyone expected to win. It had the best-selling truck name in America on its tailgate. Its best year was twenty twenty-four, when Ford sold thirty-three thousand, five hundred ten of them, according to Pickup Truck Talk. In twenty twenty-five, sales fell to about twenty-seven thousand, three hundred, a drop of eighteen percent, according to Electrek.""",
   "Ford F-150 Lightning", "LIGHTNING: 33,510 IN 2024")
sc("""Then came the announcement. On December sixteenth, twenty twenty-five, Ford said it would take a nineteen point five billion dollar charge as it changed its electric strategy. About five and a half billion dollars of that was cash. Ford also ended production of the all-electric Lightning, and dropped a planned second generation that was going to be fully electric. Less than five years after launch, the truck was finished.""",
   "Ford Rouge Complex Dearborn factory", "FORD: $19.5 BILLION CHARGE")
sc("""Here is the first twist. Ford did not abandon the name. The Lightning is planned to return as an extended-range electric truck, built at the Rouge plant in Dearborn. That means a gas engine that charges the battery, and an electric motor that drives the wheels. The company that spent billions on a pure electric truck is now saying the future looks different. Ford's chief executive, Jim Farley, said hybrids have been more popular than the company ever expected.""",
   "Ford Rouge Complex Dearborn", "LIGHTNING RETURNS: GAS-POWERED GENERATOR")
sc("""Now look at the collapse in the numbers. In the third quarter of twenty twenty-five, Ford sold ten thousand and five Lightnings. In the third quarter of twenty twenty-six, it sold two hundred eighty-nine. That is a drop of ninety-seven percent in one year. Through the first nine months of twenty twenty-six, the Lightning sold four thousand, seven hundred seventy, compared with twenty-three thousand and thirty-four a year earlier. Down seventy-nine percent.""",
   "Ford F-150 Lightning pickup", "Q3: 10,005 TO 289")
sc("""And here is the second twist, the one nobody expected. Ford's own electric truck was outsold by a truck that Ford was no longer building at full speed, and by trucks from companies that spent far less on advertising. Because when a company stops building something, sales do not fade slowly. They drop off a cliff. Buyers stop trusting a truck that is about to disappear, and the used market stops trusting it too.""",
   "Ford F-150 Lightning Platinum", "WHEN PRODUCTION ENDS, SALES VANISH")

# ---------- 2. RAM 1500 REV ----------
sc("""Number two is the Ram 1500 REV, the electric truck that never went on sale. In September of twenty twenty-five, Ram cancelled the battery-only version before the first customer received one. The truck had already been delayed, from twenty twenty-four to twenty twenty-five, then to early twenty twenty-six. And then, in a move that surprised the industry, the company kept the name but changed the truck completely.""",
   "Ram 1500 pickup truck", "RAM 1500 REV: CANCELLED BEFORE SALES")
sc("""The new Ram 1500 REV is a range-extended truck. According to reporting by TruckDaily, a four hundred volt battery drives the electric motors, and a three point six liter Pentastar V six engine runs only as a generator. It never turns the wheels. It will be built at the Sterling Heights Assembly Plant in Michigan. And Ram has not published the price, the electric range, or the towing capacity.""",
   "Stellantis Sterling Heights Assembly Plant", "THE NEW REV: V6 GENERATOR ONLY")
sc("""Here is the twist. According to a supplier memo reviewed by Automotive News, the launch has now slipped to mid-April twenty twenty-seven. The reason given was more time for a smooth rollout of the new shared powertrain. Ram's official statement is shorter. It says plans continue to be a twenty twenty-seven arrival. That means a truck announced for twenty twenty-four may reach customers three years later, and as a different truck.""",
   "Ram 1500 pickup truck dealership", "REV LAUNCH: MID-APRIL 2027")
sc("""And here is the part that explains the whole industry. While the electric Ram was being cancelled, the regular Ram pickups were selling better than ever. Through the first nine months of twenty twenty-six, Ram pickups sold three hundred twenty-five thousand, three hundred forty-eight, up twenty-four percent. The light-duty Ram one thousand five hundred jumped forty-one percent. The gas truck was winning, while the electric one was being rewritten.""",
   "Ram 1500 Big Horn pickup", "RAM LD: UP 41% IN 2026")

# ---------- 3. SILVERADO EV AND SIERRA EV ----------
sc("""Number three is the pair that tells the most honest story, the Chevrolet Silverado EV and the GMC Sierra EV. These are the electric trucks from General Motors, built in Detroit at a plant called Factory Zero. And their numbers have a strange shape. The Silverado EV sold four hundred sixty-one in twenty twenty-three, seven thousand, four hundred twenty-eight in twenty twenty-four, and eleven thousand, two hundred seventy-five in twenty twenty-five.""",
   "Chevrolet Silverado EV", "SILVERADO EV: 11,275 IN 2025")
sc("""That looks like growth. And for two years, it was. The Sierra EV went from one thousand, seven hundred eighty-eight in twenty twenty-four to seven thousand, nine hundred ninety-six in twenty twenty-five, according to GM Authority. But then the year changed, and the direction changed with it. Through the first nine months of twenty twenty-six, the Silverado EV sold five thousand, three hundred twenty-seven, down forty-three percent. The Sierra EV sold four thousand, seven hundred five, down twenty-three percent.""",
   "GMC Sierra EV", "2026: SILVERADO EV DOWN 43%")
sc("""Look at the third quarter by itself. The Silverado EV sold one thousand, six hundred fifty-five, down fifty-eight percent from the same quarter a year earlier. The Sierra EV sold one thousand, six hundred sixty-one, down almost fifty-one percent. And here is the twist. Those two trucks were growing until the federal electric vehicle tax credit of seven thousand, five hundred dollars disappeared. A truck that grows only with a subsidy has a hard future.""",
   "GMC Sierra EV Denali", "Q3 2026: DOWN 58% AND 51%")
sc("""Now the part that matters most. According to a report from Crain's Detroit Business, citing Automotive News, General Motors has indefinitely delayed the next generation of its electric trucks. They were originally expected in twenty twenty-eight. Suppliers were reportedly told that development was paused with no end date. That report rests on anonymous insiders, and GM has not confirmed it. A GM spokesperson said only that the company has not disclosed plans or timing.""",
   "General Motors Factory Zero Detroit", "NEXT-GEN GM EV TRUCKS: DELAYED")
sc("""The same report says insiders expect the Silverado and Sierra EVs to become plug-in hybrids on a new combustion platform. Again, that is not confirmed. What GM has said publicly is different. GM Authority reported in August that Factory Zero is running a single shift, and GM's chief executive, Mary Barra, has called electric vehicles the company's north star. She also said, in January, that reaching that goal would take longer without incentives.""",
   "Chevrolet Silverado EV Detroit", "BARRA: EVS TAKE LONGER")

# ---------- 4. GMC HUMMER EV ----------
sc("""Number four is the GMC Hummer EV, the loudest electric truck of them all. It weighs more than most houses have ever had in their driveways, it can drive sideways, and it was meant to be proof that an electric truck could be fun. GM does not split the pickup from the SUV in its numbers, so the figures we have combine both. Through the first nine months of twenty twenty-five, they sold thirteen thousand, two hundred thirty-three.""",
   "GMC Hummer EV pickup -H2", "HUMMER EV: 13,233 IN 9 MONTHS")
sc("""Through the first nine months of twenty twenty-six, the same figure was five thousand and twenty-four. Down sixty-two percent. In the third quarter alone, GM sold one thousand, four hundred twenty-three, compared with five thousand, two hundred forty-six a year earlier, a fall of almost seventy-three percent. This is the steepest fall among the General Motors electric trucks, and it happened with no change in the truck itself.""",
   "GMC Hummer EV", "Q3 2026: DOWN 73%")
sc("""So why did it fall faster? Because the Hummer was the most expensive of the group, and it depended the most on buyers who did not need to count every dollar. Once the tax credit was gone, even those buyers waited. There is a lesson here for every truck, not just electric ones. The more a truck costs, the more its sales depend on the mood of the market. And in twenty twenty-six, the mood changed.""",
   "GMC Hummer EV pickup", "WHY THE FALL WAS SO STEEP")

# ---------- 5. TESLA CYBERTRUCK ----------
sc("""Number five is the Tesla Cybertruck. It is the most famous electric truck on earth, and the numbers around it are the hardest to pin down, because Tesla does not report Cybertruck sales. So we use estimates, and we say so. According to InsideEVs, citing Cox Automotive, Tesla sold about twenty thousand, two hundred Cybertrucks in the United States in twenty twenty-five. In twenty twenty-four, it sold about thirty-nine thousand.""",
   "Tesla Cybertruck", "CYBERTRUCK: ~39,000 TO ~20,200")
sc("""Estimates differ. GM Authority put the twenty twenty-five total closer to twenty-five thousand. Either way, the direction is the same. And in the first quarter of twenty twenty-six, Cox Automotive data posted by Sawyer Merritt showed the Cybertruck at three thousand, five hundred nineteen, down forty-five percent from a year earlier. That is still the top seller among electric pickups that quarter. The best-selling electric truck was selling less than four thousand in three months.""",
   "Tesla Cybertruck stainless steel", "Q1 2026: 3,519 (-45%)")
sc("""Here is the twist. In September of twenty twenty-five, Tesla dropped the cheapest version of the Cybertruck, the one that was supposed to bring the price down. According to Electrek, sales in the second quarter of that year were around five thousand. The truck that was meant to be the future of the pickup became a niche product, loved by some owners and ignored by most buyers.""",
   "Tesla Cybertruck pickup", "CHEAPEST VERSION DROPPED")
sc("""One more note on honesty. For the third quarter of twenty twenty-six, Pickup Truck Talk estimates about three thousand, seven hundred, and about eleven thousand for the first nine months. The article itself calls that a low-confidence estimate based on the earlier run rate. We include it because it points the same way as everything else. But it is an estimate, not a reported sales number.""",
   "Tesla Cybertruck front", "2026: ESTIMATE ONLY, NOT REPORTED")

# ---------- 6. RIVIAN R1T ----------
sc("""Number six is the Rivian R1T, and its story is the quietest one on this list. Rivian is a startup, not a Detroit giant, and it was the first company to put an electric pickup on sale in volume. According to Cox Automotive data posted by Sawyer Merritt, the R1T sold one thousand, six hundred fifty-eight in the first quarter of twenty twenty-six, down just four percent from a year earlier.""",
   "Rivian R1T", "R1T Q1 2026: 1,658 (-4%)")
sc("""Four percent is a small fall, and next to the Cybertruck at forty-five percent and the Silverado EV at forty-one percent in the same quarter, it looks almost calm. The twist is that the smallest company held up best. The R1T is expensive, it is not aimed at work, and its buyers are not the same people who buy a Silverado. That might be why it did not fall as hard. A smaller audience can be a steadier one.""",
   "Rivian R1T pickup", "THE SMALLEST COMPANY HELD UP BEST")

# ---------- 7. SLATE ----------
sc("""Number seven is not a truck that failed. It is a truck that has not been delivered yet, and it might be the most important one. On June twenty-fourth, twenty twenty-six, Slate Auto revealed the price of its electric truck. It starts at twenty-four thousand, nine hundred fifty dollars, not including taxes, registration and destination fees. Preorders opened that same day.""",
   "Slate Auto electric truck", "SLATE TRUCK: FROM $24,950")
sc("""The truck is as simple as a modern truck can be. According to Electrek, it has a sixty-five kilowatt-hour battery, a rear motor of one hundred eighty-one horsepower, and an estimated range of two hundred five miles. It comes as a two-seat pickup that owners can turn into a five-seat SUV themselves. It has no infotainment screen, and one gray body finish. Slate plans to sell wraps instead of paint.""",
   "Slate Auto truck", "205 MILES. NO SCREEN.")
sc("""Now the twist. Slate originally pitched the truck at under twenty thousand dollars, but that price assumed the seven thousand, five hundred dollar federal tax credit, which no longer exists. The company has raised about one point four billion dollars, and it plans to sell directly to customers, with no dealerships. First deliveries are still expected by the end of twenty twenty-six. But Electrek notes that electric startups have often failed to deliver affordable vehicles at scale.""",
   "Slate Auto", "UNDER $20,000 BECAME $24,950")


# ---------- THE BIGGER PICTURE ----------
sc("""Before the close, let's put the whole market on one table, because the pattern gets clearer when you see it side by side. Through the first nine months of twenty twenty-six, according to Pickup Truck Talk, the Chevrolet Silverado sold four hundred thirteen thousand, three hundred eighty-three trucks, down less than one percent. The GMC Sierra sold two hundred fifty-two thousand, six hundred thirty-nine, flat. Even Ford's F-Series, down six point eight percent, still sold more than half a million.""",
   "Chevrolet Silverado 1500 pickup", "9 MONTHS 2026: SILVERADO 413,383")
sc("""Now compare those numbers with the electric ones. The gas and diesel trucks barely moved, or grew. The electric trucks fell by forty, sixty, even ninety percent. That is the real twist of this whole story. The pickup truck market did not shrink. A small slice of it, the slice that was supposed to be the future, shrank while everything around it held steady. The buyers did not leave trucks. They left the electric version of trucks.""",
   "GMC Sierra pickup", "TRUCKS HELD. EV TRUCKS FELL.")
sc("""Why does that matter? Because a truck buyer is a different kind of buyer. A truck is a tool. It tows a trailer on a Friday, hauls lumber on a Saturday, and sits in a driveway on Sunday. A buyer who does that cares about range with a trailer, charging on a job site, and what the truck costs per mile. When the tax credit disappeared, the electric truck lost its biggest argument, which was the price.""",
   "Ford F-250 Super Duty pickup", "A TRUCK IS A TOOL")
sc("""Look at what the carmakers chose to build next. Ford is bringing back the Lightning with a generator. Ram is rebuilding the one thousand five hundred REV with a V six that only charges the battery. GM insiders are reportedly looking at plug-in hybrids. Three different companies, three different plans, one shared idea. Keep the electric drive, but add something that does not depend on finding a charger.""",
   "Ram 1500 pickup", "THE NEW IDEA: ELECTRIC DRIVE + ENGINE")
sc("""There is a cost to that change, and it is not small. Ford took a nineteen point five billion dollar charge. General Motors said earlier in twenty twenty-six it would lose about six billion dollars from repealing its electric investments. That is more than twenty-five billion dollars between two companies, spent changing direction. And that is only what the companies announced. The real cost includes the jobs paused at Factory Zero and the workers sent home.""",
   "General Motors Factory Zero Detroit", "FORD $19.5B + GM ~$6B")
sc("""And what about the buyer who already owns one? This is a fair question, and it deserves a straight answer. A warranty normally stays valid on a discontinued model, and an electric truck still works the same on the day after the announcement. The risk is value. A truck with a famous name and no future often loses value faster than a truck that is still being built, so check resale numbers before you pay.""",
   "Ford F-150 Lightning pickup", "OWNING A DISCONTINUED TRUCK")

# ---------- CLOSE ----------
sc("""So what is the pattern across all seven? One electric truck was ended after a nineteen point five billion dollar charge. One was cancelled and came back as a hybrid. Two lost almost half their sales once the tax credit was gone. One lost sixty-two percent. One is a famous truck that sells in the thousands, not the tens of thousands. And one is still a promise. The lesson is not that electric trucks are doomed. It is that they were priced and planned for a world with a subsidy, and that world ended.""",
   "Ford F-150 Chevrolet Silverado pickups dealership lot", "THE PATTERN: BUILT FOR A SUBSIDY")
sc("""That matters if you are thinking about buying a truck in twenty twenty-seven. Here is what to check. First, find out whether the exact model is still being built, and for how long. A discontinued truck can lose value quickly, and parts and service attention can fade. Second, look at the sales trend of that model, not the brand. A truck that fell sixty percent in a year is telling you something.""",
   "Ford F-150 pickup", "CHECK 1 AND 2: BUILT? TREND?")
sc("""Third, ask what replaces it. Right now, the answer from Ford and Ram is a range-extended truck, and from GM it is still unclear. Fourth, count the full cost. Charging, fuel, insurance and what the truck will be worth in five years all belong on the same page. And fifth, never buy a truck because of a promise about next year. Buy the truck that exists today, with the numbers you can check.""",
   "Chevrolet Silverado 1500", "CHECK 3, 4 AND 5")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we just walked through. The link is in the description and in the pinned comment. If you want to see which trucks keep disappearing from dealer lots, subscribe, because the next video covers exactly that. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One electric truck lost": "Intro", "Number one": "1. Ford F-150 Lightning", "Number two": "2. Ram 1500 REV",
      "Number three": "3. Chevrolet Silverado EV and GMC Sierra EV", "Number four": "4. GMC Hummer EV",
      "Number five": "5. Tesla Cybertruck", "Number six": "6. Rivian R1T", "Number seven": "7. Slate truck",
      "So what is the pattern": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video02",
  "length_scale": 1.38, "title": "7 Electric Pickups Americans Stopped Buying (What Really Happened)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words ~", round(words/150, 1), "min")
