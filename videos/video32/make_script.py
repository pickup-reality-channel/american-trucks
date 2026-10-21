import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""A brand that has not sold a new vehicle since nineteen eighty is taking on Ford, GM and Ram, in the most profitable market in the American car business. It has a two billion dollar factory, more than one hundred sixty thousand reservations, and a truck that may not reach customers until twenty thirty. This is Scout Motors against the Big Three, and the numbers are not what you would expect.""",
   "Scout Terra concept", "SCOUT VS THE BIG THREE")

# ---------- COLD OPEN ----------
sc("""Scout is a famous old American name. International Harvester built the original Scout, and the Scout, Terra and Traveler names were used on its trucks and utility vehicles in the nineteen sixties and seventies. Today the brand belongs to the Volkswagen Group. Scout Motors was formed in twenty twenty-two to bring the name back, with a new electric pickup called the Terra and an SUV called the Traveler.""",
   "International Harvester Scout", "AN OLD AMERICAN NAME, RETURNING")
sc("""On paper, the plan is bold. A brand-new factory in South Carolina. A body-on-frame pickup that Scout says can tow more than ten thousand pounds. An optional gas range extender for road trips. And direct sales, with no traditional dealers. Each one of those choices is a direct challenge to how Ford, GM and Ram sell trucks.""",
   "Scout Traveler concept", "A DIRECT CHALLENGE")
sc("""In this video, we compare Scout's plan with what the Big Three are actually doing, using sales figures, published specs and the latest reporting on Scout's timeline. And we will see that the Big Three are already building the very kind of truck Scout promised, and in at least one case, sooner. Every number is sourced in the description.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE BIG THREE'S POSITION ----------
sc("""First, the size of the mountain Scout is trying to climb. In twenty twenty-five, Ford sold eight hundred one thousand, five hundred twenty-five F-Series trucks in the United States, up nine point five percent, according to CarScoops. It was the forty-ninth consecutive year the F-Series was America's best-selling truck.""",
   "Ford F-150 2025", "F-SERIES: 801,525 IN 2025")
sc("""Chevrolet sold five hundred seventy-seven thousand, four hundred thirty-four Silverados, up four point five percent. GMC sold three hundred forty-eight thousand, two hundred twenty-two Sierras, up seven point eight percent. And Ram sold three hundred seventy-four thousand and fifty-nine pickups, roughly flat.""",
   "Chevrolet Silverado 1500", "SILVERADO: 577,434")
sc("""Here is the first twist. Ford wins the nameplate race, but GM wins the company race. The Silverado and Sierra together sold nine hundred twenty-five thousand, six hundred fifty-six trucks, more than the F-Series, according to CarScoops. Add Ram, and the Big Three sold more than two million full-size pickups in a single year.""",
   "GMC Sierra 1500 Denali", "GM COMBINED: 925,656")
sc("""And the midsize market is booming too. The Toyota Tacoma sold two hundred seventy-four thousand, six hundred thirty-eight trucks in twenty twenty-five, up forty-two point four percent, according to CarScoops. So Scout is not entering a shrinking market. It is entering a growing one, where the incumbents are already winning more buyers every year.""",
   "Toyota Tacoma 2024", "TACOMA: +42.4% IN 2025")
sc("""Now compare that with Scout. Its South Carolina plant is planned for up to two hundred thousand vehicles a year, at full capacity, and those would be split between an SUV and a pickup. Reservations so far run about three to one in favor of the Traveler SUV over the Terra pickup, according to The Truth About Cars. So even in the best case, the Terra would be a tiny fraction of the full-size truck market.""",
   "Scout Motors factory", "PLANT CAPACITY: 200,000 A YEAR")

# ---------- 2. THE SCOUT TRUCKS ----------
sc("""So what exactly is Scout selling? The Terra pickup and the Traveler SUV were revealed as concepts on October twenty-fourth, twenty twenty-four, in Franklin, Tennessee. According to SC Biz News, the Terra is expected to tow more than ten thousand pounds, the Traveler more than seven thousand, and both are expected to carry nearly two thousand pounds of payload.""",
   "Scout Terra", "TERRA: 10,000+ LB TOWING")
sc("""Scout announced two powertrains. A fully electric version with up to about three hundred fifty miles of range, and an extended-range version called Harvester, with a gas engine that recharges the battery, for more than five hundred miles of total range. According to AutoGuide, the electric version uses a battery of about one hundred twenty kilowatt-hours, and is expected to reach sixty miles per hour in about three and a half seconds.""",
   "Scout Traveler", "EV: 350 MI. HARVESTER: 500+ MI.")
sc("""Interestingly, AutoGuide compared Scout's Harvester layout to the system in the Ram fifteen hundred Ramcharger, the truck we will meet again in a moment. Both use an engine that only makes electricity. And that comparison is the key to this whole story, because the truck Scout is promising has a direct rival from one of the Big Three.""",
   "Scout Terra concept front", "SAME IDEA AS RAM'S RAMCHARGER")
sc("""The Harvester engine is a naturally aspirated four-cylinder from Volkswagen, built at the Volkswagen Group's plant in Silao, Mexico, according to AutoGuide, citing VW's chief financial officer. It sits behind the rear axle and is not connected to the wheels. It only acts as a generator. With a battery about half the size, the Harvester version is expected to have about one hundred fifty miles of pure electric range, and to be roughly one second slower to sixty.""",
   "Volkswagen engine", "HARVESTER: A VW FOUR-CYLINDER")
sc("""InsideEVs later reported more detail on the range-extended version, a lithium iron phosphate battery of about sixty-three kilowatt-hours, about one hundred fifty miles of electric range, and about five hundred miles in total. That matters because the range extender is now the version Scout plans to launch first, and the version most reservation holders chose.""",
   "Scout Traveler side view", "EREV: ~63 kWh, ~150 MI ELECTRIC")
sc("""And the price. At the reveal, Scout said Terra entry models would start at fifty-one thousand, five hundred dollars with incentives, and Traveler entry models at fifty thousand with incentives, with retail prices starting under sixty thousand, according to SC Biz News. Here is the twist. The incentive in those numbers was the federal EV tax credit, which, as we covered in our last video, has since been abolished. So the realistic starting point is the under sixty thousand dollar retail figure, not fifty.""",
   "Scout Terra pickup concept", "UNDER $60,000 (RETAIL)")

# ---------- 3. THE FACTORY ----------
sc("""The factory is real and it is big. Scout announced about two billion dollars for South Carolina, on a one thousand one hundred acre site in Blythewood, near Columbia, off Interstate seventy-seven, according to SC Biz News. Officials estimate about four thousand jobs at full capacity.""",
   "Columbia South Carolina", "$2 BILLION, 4,000 JOBS")
sc("""But here is the twist. Scout's original plan was to begin production in twenty twenty-seven. In March twenty twenty-six, CEO Scott Keogh said he expects customers to receive vehicles sometime in twenty twenty-eight, according to Electrive. He said he did not want to commit to an exact launch day. And Scout planned to build its first prototypes at Blythewood by the end of twenty twenty-six.""",
   "Scout Motors Blythewood", "2027 BECAME 2028")
sc("""Then came a bigger blow for truck buyers. In April twenty twenty-six, forecasting firm AutoForecast Solutions reported that Traveler production had moved from March to September twenty twenty-eight, and Terra pickup production had moved from March twenty twenty-eight all the way to March twenty thirty, according to The Truth About Cars. Scout said it had nothing additional to share about production timing.""",
   "Scout Terra rear", "TERRA PICKUP: MARCH 2030?")
sc("""Why the delay? Sam Fiorani of AutoForecast Solutions said engineers are reworking the vehicles to launch the range-extended version first. He said, quote, when the vehicle was originally announced, it was going to be fully electric. And that change follows the customers. Of about one hundred sixty thousand reservations, about eighty-seven percent chose the range extender, according to Electrive.""",
   "Scout Traveler concept rear", "87% WANT THE RANGE EXTENDER")
sc("""And in September twenty twenty-six, Scout showed two new Traveler concepts, a rugged Trail-Ready version with thirty-five-inch BFGoodrich mud-terrain tires, beadlock wheels and a winch, and a more luxurious Mountainside version with twenty-two-inch wheels. Motor Illustrated reported a launch of mid twenty twenty-eight at the earliest. Scout keeps showing trucks. It is not yet building them for customers.""",
   "Scout Traveler concept", "NEW CONCEPTS, NO DELIVERIES YET")

# ---------- 4. THE BIG THREE'S ANSWER ----------
sc("""Now here is the twist that changes the whole comparison. Scout's best idea, a full-size truck with a battery and a gas generator, is not unique anymore. Ram unveiled the Ram fifteen hundred Ramcharger with that layout in twenty twenty-three. And in September twenty twenty-five, Stellantis canceled its fully electric Ram fifteen hundred REV, and gave the REV name to the range-extended truck instead, according to InsideEVs.""",
   "Ram 1500 Ramcharger", "RAM GOT THERE FIRST")
sc("""The production twenty twenty-seven Ram fifteen hundred REV has a ninety-two kilowatt-hour battery, front and rear electric motors making a combined six hundred forty-seven horsepower and six hundred ten pound-feet, and a three point six liter Pentastar V6 that drives a generator, with no mechanical link to the wheels. Stellantis claims up to six hundred ninety miles of total range, with about one hundred forty-five miles in electric mode, according to InsideEVs.""",
   "Ram 1500 2025", "RAM 1500 REV: 647 HP, 690 MI")
sc("""And the work numbers are serious. Towing is targeted at up to fourteen thousand pounds with a Class five hitch, and payload at up to two thousand, six hundred twenty-five pounds, according to InsideEVs. DC fast charging reaches one hundred forty-five kilowatts. It is built at Sterling Heights, Michigan, with production slated for the second half of twenty twenty-six as a twenty twenty-seven model. Price had not been announced.""",
   "Ram 1500 towing trailer", "14,000 LB TOWING TARGET")
sc("""Compare that with Scout. The Terra is expected to tow more than ten thousand pounds and to go more than five hundred miles with the range extender. The Ram REV targets fourteen thousand pounds and claims six hundred ninety miles. And it is scheduled to reach production years before the latest reported date for the Terra.""",
   "Ram 1500 Laramie", "RAM: 14,000 LB / 690 MI. TERRA: 10,000+ / 500+")
sc("""But Ram's own path shows how hard this is. When the Ramcharger was unveiled in twenty twenty-three, it was targeted for the end of twenty twenty-four. It was then pushed to twenty twenty-five, then to early twenty twenty-six, as Stellantis cited a longer validation phase for quality, according to ClubAlfa, and InsideEVs later reported production in the second half of twenty twenty-six. Even an established truck maker with an existing plant needed years of extra time.""",
   "Ram Sterling Heights Assembly", "RAM'S EREV: DELAYED 3 TIMES")
sc("""Ford is heading the same way. After discontinuing the F-150 Lightning, Ford is developing an extended-range electric F-150. CEO Jim Farley described it as, quote, seven hundred miles on a tank of gas, and for ninety percent of the time, is all-electric, according to Electrek. InsideEVs lists it as replacing Ford's canceled Project T three electric truck. Ford has not given a final on-sale date.""",
   "Ford F-150 Lightning", "FORD F-150 EREV: 700+ MI")
sc("""And GM? Its answer for twenty twenty-seven is different. The redesigned Silverado and Sierra launched with two new V8s, a five point seven and a six point six liter, and there is no plug-in hybrid Silverado yet, according to Motor Illustrated. GM is betting that many full-size truck buyers still want gas, and its twenty twenty-five sales growth suggests it may be right, for now.""",
   "Chevrolet Silverado 2027", "GM BETS ON NEW V8s")
sc("""And GM is planning for volume, not caution. According to reporting on its investor presentation, GM aims to build about two million full-size trucks and SUVs in twenty twenty-seven, as it expands U.S. capacity. That is ten times the full annual capacity of Scout's South Carolina plant, from just one part of GM's lineup.""",
   "GMC Sierra 1500 2027", "GM GOAL: ~2 MILLION IN 2027")
sc("""Here is the twist. In twenty twenty-four, a range-extended pickup sounded like Scout's secret weapon. By twenty twenty-six, it is becoming the industry standard. Ram has one heading to production. Ford is building one for its best-selling truck. And Scout, which moved to a range extender first, now has to arrive later with an idea its rivals copied, or developed in parallel.""",
   "Ford F-150 2024", "THE SECRET WEAPON IS NOW STANDARD")

# ---------- 5. ELECTRIC TRUCKS STRUGGLED ----------
sc("""Why did everyone move to range extenders? Because fully electric full-size trucks struggled. Ford discontinued the F-150 Lightning in December twenty twenty-five. Farley told CNBC that the very high-end EVs, the fifty, seventy and eighty thousand dollar vehicles, just weren't selling. And InsideEVs reported that Stellantis cited falling demand for big electric trucks in North America when it canceled the electric Ram.""",
   "Ford F-150 Lightning charging", "BIG EV TRUCKS STRUGGLED")
sc("""And price was part of it. According to Equipment World, the twenty twenty-five F-150 Lightning Pro, the cheapest work version, started at fifty-four thousand, seven hundred eighty dollars. That is the same territory as Scout's under sixty thousand dollar retail target. Ford's answer was to go smaller and cheaper, with the Fathom midsize electric pickup starting at twenty-eight thousand, three hundred fifty dollars, plus delivery, according to Electrek. Scout is aiming at the price point where Ford's electric truck failed to sell.""",
   "Ford F-150 Lightning Pro", "LIGHTNING PRO: $54,780")
sc("""InsideEVs also pointed to the practical problems. Battery costs remain high, and many electric trucks struggle to meet towing and hauling needs. Towing a heavy trailer can cut an electric truck's range dramatically, which is exactly the job truck buyers care about. A gas generator solves that for long trips, while keeping most daily driving electric.""",
   "electric pickup towing trailer", "TOWING KILLS EV RANGE")
sc("""And the market agreed. Only two electric vehicles made the top twenty-five best-sellers in America in twenty twenty-five, the Tesla Model Y and Model three, and both sold less than the year before, according to CarScoops. Meanwhile, the F-Series, Silverado and Sierra all grew. The buyers Scout wants are, for now, still buying gas trucks.""",
   "Ford F-150 dealership", "TRUCK BUYERS STILL BUY GAS")

# ---------- 6. DEALERS ----------
sc("""And Scout's competition is not only the Big Three. InsideEVs' list of extended-range vehicles coming to America includes the Jeep Grand Wagoneer EREV, with six hundred forty-seven horsepower and more than five hundred miles of combined range, a Hyundai Santa Fe EREV built in Alabama, and a Kia pickup with extended-range and hybrid versions planned by the end of the decade. By the time a Scout Terra is built, the range-extended truck may be a crowded market.""",
   "Jeep Grand Wagoneer", "A CROWDED EREV MARKET")
sc("""Scout has one more fight that the Big Three do not. It plans to sell directly to customers, without franchised dealers. According to Reuters, as cited by Electrive, two U.S. dealers sued Volkswagen over that plan, and the case could expand into a class action. Volkswagen declined to comment.""",
   "car dealership lot", "DEALERS SUED VOLKSWAGEN")
sc("""Here is why that matters for you. Ford, GM and Ram trucks are sold and serviced by thousands of dealers across the country, including in small towns where many truck owners live. Scout will have to build its own sales and service network from zero, while fighting legal challenges. For a truck you expect to tow with for fifteen years, where you get it fixed is as important as what it can do.""",
   "rural pickup truck service", "WHO FIXES IT IN A SMALL TOWN?")

# ---------- 7. WHERE SCOUT CAN WIN ----------
sc("""So can Scout win anything? Yes, and it is not small. The demand is real. More than one hundred sixty thousand people put down refundable one hundred dollar reservations, according to Electrive. That is not a sales number, but it shows that the Scout name, and its look, connects with buyers.""",
   "International Harvester Scout II", "160,000+ RESERVATIONS")
sc("""Scout's design is its strongest weapon. Motor Illustrated describes the cues, straight lines, rectangular headlamps, angled rear quarter windows and script logos taken from the old International Harvester Scouts. The Big Three sell incredible trucks, but most of them now look alike. Scout is selling heritage and personality, the same strategy that made the Ford Bronco a hit.""",
   "Ford Bronco 2021", "HERITAGE SELLS")
sc("""Scout also has time on its side in one way. By arriving later, it can learn from the first range-extended trucks on the road. If early Ram REV owners report problems, Scout can design around them. Being second is slower, but it can be safer, and as we have shown in our recall videos, the first model year of a new truck is often where problems appear.""",
   "Scout Terra front", "SECOND CAN BE SAFER")
sc("""And Scout has a powerful parent. Volkswagen Group can supply engines, like the Harvester four-cylinder from Mexico, parts and engineering. The Truth About Cars also notes reports that a U.S.-oriented Volkswagen ID four is in development, and that some expect the Scout plant to build it. So the factory may have a future even if the Terra arrives late.""",
   "Volkswagen ID.4", "VOLKSWAGEN BEHIND IT")

# ---------- 8. WHAT IT MEANS FOR BUYERS ----------
sc("""Volkswagen's own American plans are shifting, too. The Truth About Cars reported that Volkswagen would end twenty twenty-six ID four production at its Chattanooga, Tennessee, plant, so the plant can focus on high-volume models like the twenty twenty-seven Atlas. Electric vehicles are not the easy win automakers expected a few years ago, and that pressure reaches Scout as well.""",
   "Volkswagen Chattanooga Assembly Plant", "VW ENDS 2026 ID.4 IN CHATTANOOGA")
sc("""Now what this means if you want a truck in twenty twenty-seven. If you were waiting for a Scout Terra, the honest answer is that you may be waiting a long time. The latest reported forecast puts Terra production in twenty thirty. That is a forecast, not an official date, but Scout itself only says customer deliveries are expected in twenty twenty-eight, and has not said which model comes first, beyond the Traveler.""",
   "Scout Terra concept side", "WAITING FOR A TERRA? IT'S A LONG WAIT")
sc("""If what you want is the range-extended idea, a big truck that drives electric most of the time and uses gas for long trips, the Ram fifteen hundred REV is scheduled to arrive first, with Ford's extended-range F-150 coming. And if you just want a dependable truck now, the conventional gas trucks are still where the Big Three's sales are growing.""",
   "Ram 1500 REV", "RAM REV ARRIVES FIRST")
sc("""And here is a practical warning. A reservation is not a price. Scout's under sixty thousand dollar figure dates from the twenty twenty-four reveal, before the delays, the change to range extenders first, and the end of the federal EV tax credit. The final price could be different. Never budget for a truck that has not been priced yet.""",
   "Scout Traveler interior", "A RESERVATION IS NOT A PRICE")

# ---------- CLOSE ----------
sc("""If you are thinking of reserving any new truck from a brand or a powertrain that is not on sale yet, ask three questions. Is the reservation refundable, and how fast? Where is the nearest place that will service it, and who owns that service network? And what is the confirmed price, not the reveal price? If the answer to any of those is that nobody knows yet, treat the reservation as a bet, not a purchase.""",
   "pickup truck dealership service", "3 QUESTIONS BEFORE YOU RESERVE")
sc("""So, Scout Motors versus the Big Three. The Big Three sold more than two million full-size pickups in twenty twenty-five, and GM's two trucks together outsold the F-Series. Scout has a two billion dollar plant, a famous name, one hundred sixty thousand reservations, and a pickup that may not enter production until twenty thirty, according to the latest forecast.""",
   "Chevrolet Silverado Ford F-150", "2 MILLION VS 0 (SO FAR)")
sc("""And the final twist. Scout's biggest impact may already have happened. By promising a rugged, range-extended American pickup, it showed the market wanted one. And now Ram is building it first and Ford is following. Scout may still win buyers with style and heritage. But it will have to win them in a market that took its best idea and moved faster.""",
   "Scout Terra", "THEY TOOK THE IDEA AND MOVED FASTER")
sc("""We put the twenty twenty-seven truck calendar, and a checklist for buying a first-year or range-extended truck, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we compare the Tacoma, Ranger and Colorado for twenty twenty-seven. And tell us in the comments, would you wait for a Scout? Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"A brand that has not sold": "Intro", "First, the size of the mountain": "The Big Three's 2025 sales", "So what exactly is Scout selling": "The Scout Terra and Traveler",
      "The factory is real": "The factory and the delays", "Now here is the twist that changes": "The Big Three's answer: range extenders",
      "Why did everyone move": "Why electric trucks struggled", "Scout has one more fight": "The dealer fight",
      "So can Scout win anything": "Where Scout can win", "Now what this means if you want": "What it means for buyers", "So, Scout Motors versus": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video32", "length_scale": 1.4,
  "title": "Scout Motors vs the Big Three: The Truck That Might Not Arrive Until 2030", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
