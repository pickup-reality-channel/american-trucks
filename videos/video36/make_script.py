import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Ford sold almost eighty-five thousand hybrid F-150s in a single year. Toyota made its biggest truck a hybrid. Stellantis canceled its plug-in hybrids and its electric Ram. And General Motors, the company that sells more full-size pickups than anyone, does not sell a single hybrid truck. Twenty twenty-seven is the year of the hybrid truck war. Here is who is winning.""",
   "Ford F-150 PowerBoost", "THE HYBRID TRUCK WAR")

# ---------- COLD OPEN ----------
sc("""The shift is happening across the whole market. According to Cox Automotive data cited by The Washington Post, hybrid sales rose more than eighty percent from twenty twenty-three to twenty twenty-six, reaching a pace of more than two million vehicles a year. In the first quarter of twenty twenty-six, hybrids hit a record fourteen point one percent of new vehicle sales, nearly three times the share of fully electric vehicles.""",
   "Toyota Tundra hybrid", "HYBRIDS: 14.1% OF SALES")
sc("""And it kept growing. According to AutoGuide, citing Cox Automotive, hybrids reached a record sixteen point three percent of U.S. sales in the second quarter of twenty twenty-six, up twenty-three percent from a year earlier, compared with about five point eight percent for electric vehicles. Edmunds' Joseph Yoon called it the stealth rise of hybrids.""",
   "Ford Maverick Hybrid", "Q2 2026: 16.3% HYBRID")
sc("""And in some models, the hybrid is now the main version. The Washington Post reported that most Toyota Highlanders sold earlier in twenty twenty-six were hybrids, as were many Hyundai Sonatas and Honda CR-Vs. When the hybrid outsells the gas-only version of the same vehicle, it has stopped being a niche. Trucks are next.""",
   "Toyota Highlander hybrid", "HYBRIDS NOW OUTSELL GAS VERSIONS")
sc("""In this video, we go company by company. Ford, Toyota, Stellantis and Ram, General Motors, and the newcomers. Who has a hybrid truck today, how good it is, who canceled what, and who is betting on what for twenty twenty-seven. And at the end, whether a hybrid truck actually makes sense for you. Every number is sourced in the description.""",
   "Ram 1500 2025", "COMPANY BY COMPANY")

# ---------- 1. WHY HYBRIDS ----------
sc("""First, why is this happening now? Because electric trucks struggled. U.S. electric vehicle sales fell twenty-seven percent in the first quarter of twenty twenty-six compared with a year earlier, according to Cox Automotive, as cited by The Washington Post. The seventy-five hundred dollar federal tax credit for new EVs expired in September twenty twenty-five.""",
   "Chevrolet Silverado EV", "EV SALES: -27% IN Q1 2026")
sc("""Even at their peak, electric vehicles were under ten percent of U.S. sales for a full year, a figure The Washington Post said had been boosted by tax credits. Hybrids, meanwhile, more than doubled their market share over three years, without the same level of federal support. Buyers were voting with their own money, and they voted for hybrids.""",
   "electric car charging station", "EVs UNDER 10%. HYBRIDS DOUBLED.")
sc("""And big electric trucks had specific problems. InsideEVs noted that battery costs remain high, and many electric trucks struggle to meet towing and hauling needs. Ford CEO Jim Farley said the fifty, seventy and eighty thousand dollar EVs just weren't selling. A hybrid avoids those problems. There is no charging, no range anxiety when towing, and the price premium is smaller.""",
   "Ford F-150 Lightning towing", "NO CHARGING. NO RANGE ANXIETY.")
sc("""The losses were enormous. Honda canceled three electric models for the U.S. market and took a nine billion dollar write-down, and Toyota abandoned an electrified Lexus, according to The Washington Post. Cox's Stephanie Valdez Streaty said of electric vehicles, the timeline has just shifted. And GM CEO Mary Barra pointed out the other side, that EV drivers don't often go back to combustion engines. Electric is not dead. It is just slower.""",
   "Honda Prologue", "HONDA: $9 BILLION WRITE-DOWN")
sc("""Regulation changed too. In December twenty twenty-five, the Trump administration announced it was rolling back fuel economy rules, according to reporting on Stellantis' plans. Without tougher fuel economy targets to meet, automakers have less pressure to sell electric vehicles at a loss. That is one more reason they are turning to hybrids, which buyers will pay for, instead of EVs they must discount.""",
   "Washington DC Capitol", "FUEL ECONOMY RULES ROLLED BACK")
sc("""Here is the twist. Many automakers spent years and billions of dollars preparing for electric trucks, and the technology buyers chose instead is one that Toyota and Ford have sold for more than two decades. Farley said Ford was really well positioned thanks to its hybrid leadership over the past twenty years, according to Auto123. Cox's Stephanie Valdez Streaty put it simply. Hybrids are definitely having their moment.""",
   "Toyota Prius", "\\u201CHYBRIDS ARE HAVING THEIR MOMENT\\u201D")

# ---------- 2. FORD ----------
sc("""Ford is the clear leader. In twenty twenty-five, Ford sold a record two hundred twenty-eight thousand and seventy-two hybrids, up twenty-one point seven percent, according to the company. The F-150 Hybrid set a record with eighty-four thousand, nine hundred thirty-four sales, up fifteen percent. That makes the F-150 PowerBoost one of the most popular hybrid vehicles in America, and by far the most popular hybrid pickup.""",
   "Ford F-150 Hybrid", "F-150 HYBRID: 84,934 IN 2025")
sc("""The PowerBoost pairs a three point five liter twin-turbo V6 with an electric motor, for up to four hundred thirty horsepower and five hundred seventy pound-feet of torque, according to Auto123. That made it the most powerful engine in the regular F-150 lineup when it launched. In twenty twenty-four, Farley said twenty to twenty-five percent of F-150s being produced had the hybrid system, double the share of about ten percent Ford had reported in twenty twenty-three.""",
   "Ford F-150 Platinum Hybrid", "430 HP, 570 LB-FT")
sc("""Ford has been steadily pushing the hybrid share up. At the twenty twenty-three Detroit Auto Show, Ford said it wanted to double the hybrid share of F-150 sales from about ten percent, and Auto123 reported in twenty twenty-four that the goal had been met. Farley also admitted EV adoption had been, quote, a little slower than we anticipated. Ford adjusted early, and that head start is paying off now.""",
   "Ford F-150 Lariat Hybrid", "HYBRID SHARE: 10% → 20-25%")
sc("""And the PowerBoost has a feature that sells it to working buyers. Ford's Pro Power Onboard turns the truck into a generator, powering tools and equipment from outlets in the bed. For a contractor, that means no separate generator to buy, carry and fuel. Here is the twist. Ford's most convincing argument for the hybrid F-150 was never fuel economy. It was a built-in power plant.""",
   "Ford F-150 Pro Power Onboard", "THE TRUCK IS THE GENERATOR")
sc("""Ford's smaller hybrid is even more important. The Maverick compact pickup sold a record one hundred fifty-five thousand and fifty-one trucks in twenty twenty-five. And through September twenty twenty-six, Maverick Hybrid sales hit a record seventy-four thousand, three hundred, with twenty-seven thousand, seven hundred ninety-three in the third quarter alone, up fifty-nine point six percent, according to Ford.""",
   "Ford Maverick Hybrid", "MAVERICK HYBRID: 74,300 (YTD 2026)")
sc("""So Ford has hybrids at both ends of its pickup range, the affordable Maverick and the full-size F-150. Ford has said it plans to offer a hybrid version of every model in its lineup by the end of the decade, according to Auto123. And it is adding an extended-range electric F-150, which Farley described as seven hundred miles on a tank of gas, and all-electric ninety percent of the time.""",
   "Ford Maverick and F-150", "A HYBRID FOR EVERY MODEL")
sc("""Here is the twist on Ford. The same company that killed the F-150 Lightning has the strongest electrified truck business in America. The difference is the type of electrification. Buyers rejected the expensive fully electric truck, and embraced the hybrid that works like a normal truck.""",
   "Ford F-150 Lightning and F-150 Hybrid", "KILLED THE EV. WON WITH HYBRIDS.")

# ---------- 3. TOYOTA ----------
sc("""Toyota is the other hybrid giant, and it went further than anyone. When the third-generation Tundra launched for twenty twenty-two, Toyota dropped the V8 entirely. The base engine became a twin-turbo three point five liter V6, and the top engine became the i-Force Max hybrid, with four hundred thirty-seven horsepower and five hundred eighty-three pound-feet of torque, according to reporting at the launch.""",
   "Toyota Tundra i-Force Max", "TUNDRA: NO MORE V8")
sc("""Even the non-hybrid Tundra changed. Its base twin-turbo V6 makes up to three hundred eighty-nine horsepower, with a ten-speed automatic, according to launch reporting. Toyota decided that a turbo V6, and a hybrid turbo V6 at the top, could replace its old V8 completely. It was the boldest powertrain bet in the full-size segment, years before anyone else made the move.""",
   "Toyota Tundra 2023 SR5", "BASE TUNDRA: TWIN-TURBO V6")
sc("""That is more torque than Ford's PowerBoost. The i-Force Max uses an electric motor of forty-eight horsepower and one hundred eighty-four pound-feet, with a small nickel-metal hydride battery. And for twenty twenty-seven, Toyota is updating the Tundra TRD Pro, which comes with the hybrid, with Fox Q three S shocks and new IsoDynamic seats, according to SlashGear.""",
   "Toyota Tundra TRD Pro 2024", "I-FORCE MAX: 437 HP, 583 LB-FT")
sc("""At launch, Toyota expected about twenty-five percent of Tundra buyers to choose the hybrid. And the hybrids were compared directly. In the original EPA ratings reported at the Tundra's launch, the four-wheel-drive F-150 Hybrid was rated at twenty-four miles per gallon combined, versus twenty-one for most four-wheel-drive Tundra versions. Ford's hybrid was built more for efficiency. Toyota's was built more for torque.""",
   "Toyota Tundra 2022", "F-150 HYBRID 24 MPG VS TUNDRA 21")
sc("""Toyota brought the same idea to its midsize truck. The fourth-generation Tacoma offers an i-Force Max hybrid with three hundred twenty-six horsepower and four hundred sixty-five pound-feet, the most of any Tacoma. And the Tacoma had its best sales year ever in twenty twenty-five, with two hundred seventy-four thousand, six hundred thirty-eight sold, according to TFLtruck.""",
   "Toyota Tacoma hybrid", "TACOMA HYBRID: 326 HP")
sc("""Here is the twist on Toyota. Its hybrid trucks are built for power, not just fuel economy. The hybrid Tacoma tows up to six thousand pounds, according to published specs, five hundred less than the best gas Tacoma. And the Tundra, despite its hybrid, has struggled in sales. In the fourth quarter of twenty twenty-five, Tundra sales fell twelve point seven percent, according to Ford Authority. A hybrid alone does not win the full-size truck market.""",
   "Toyota Tundra 2025", "TUNDRA Q4 2025: -12.7%")
sc("""Across its whole lineup, Toyota is moving toward hybrids everywhere. The Washington Post reported that its fleet is moving to hybrid-only for several models, including the twenty twenty-six RAV four, now sold only as a hybrid. Toyota is betting that the hybrid is not a stepping stone to electric. For many buyers, it is the destination.""",
   "Toyota RAV4 hybrid", "TOYOTA: HYBRID-ONLY MODELS")

# ---------- 4. STELLANTIS / RAM ----------
sc("""Stellantis, Ram's parent company, has made the biggest U-turn. In September twenty twenty-five, it canceled the fully electric Ram fifteen hundred REV, according to InsideEVs. Then it announced it would end plug-in hybrid sales and production in North America, starting with the twenty twenty-six model year, discontinuing the Jeep Wrangler four-xe, the Grand Cherokee four-xe and the Chrysler Pacifica plug-in hybrid, according to Nasdaq.""",
   "Jeep Wrangler 4xe", "STELLANTIS ENDS PLUG-IN HYBRIDS")
sc("""Here is the twist. The Wrangler four-xe was the best-selling plug-in hybrid in America for three consecutive years after its twenty twenty-one debut. Stellantis said changing consumer preferences had significantly reduced demand for plug-in hybrids. It is focusing instead on conventional hybrids and extended-range electric vehicles.""",
   "Jeep Wrangler 4xe charging", "AMERICA'S #1 PHEV: CANCELED")
sc("""There were other pressures too. Nasdaq noted that recalls of roughly three hundred seventy-five thousand Jeep plug-in hybrids over battery failure and fire concerns added pressure, though Stellantis did not directly link its decision to them. Instead, Stellantis launched conventional hybrids, like the new Jeep Cherokee, with a one point six liter turbo four-cylinder hybrid rated at an estimated thirty-seven miles per gallon combined, starting at thirty-six thousand, nine hundred ninety-five dollars.""",
   "Jeep Cherokee 2026", "375,000 JEEP PHEVs RECALLED")
sc("""Stellantis CEO Antonio Filosa said, quote, we truly believe that hybrid is going to be one of the favorite powertrains in the U.S., according to Reuters reporting from December twenty twenty-five. And the Washington Post reported that Stellantis expects a twenty-six billion dollar charge, partly tied to overestimating the pace of the energy transition.""",
   "Stellantis headquarters", "$26 BILLION CHARGE")
sc("""For Ram, the bet is the extended-range Ram fifteen hundred REV, the former Ramcharger. It uses a ninety-two kilowatt-hour battery and a three point six liter V6 that only generates electricity, with a claimed six hundred ninety miles of total range and up to fourteen thousand pounds of towing, according to InsideEVs. Production was slated for the second half of twenty twenty-six, as a twenty twenty-seven model.""",
   "Ram 1500 Ramcharger", "RAM REV: 690 MILES")
sc("""But here is the other half of Ram's strategy. In twenty twenty-five, Stellantis announced the Hemi V8 would return for the twenty twenty-six Ram fifteen hundred. And the twenty twenty-seven Rumble Bee SRT uses a supercharged Hemi with seven hundred seventy-seven horsepower. Ram is betting on both extremes at once, a big V8 for traditional buyers, and a range-extended electric truck for everyone else.""",
   "Ram 1500 Hemi", "HEMI V8 + RANGE EXTENDER")

# ---------- 5. GM ----------
sc("""And now the company that is missing. According to AutoGuide in October twenty twenty-six, GM's only hybrid is a version of the Chevrolet Corvette. It does not sell a hybrid Silverado or Sierra. GM's propulsion engineering chief Mike Anderson restated plans to add hybrids, but gave no timeline. He said, quote, we're not tone deaf to our customers.""",
   "Chevrolet Corvette E-Ray", "GM'S ONLY HYBRID: A CORVETTE")
sc("""The plans keep moving. In mid twenty twenty-four, GM said plug-in hybrids would arrive by twenty twenty-seven. In January twenty twenty-six, CEO Mary Barra said GM was studying plug-in and traditional hybrids, and later told Bloomberg that a handful of models were coming. AutoForecast Solutions expects GM to begin selling plug-in hybrids in late twenty twenty-seven or early twenty twenty-eight, with about seventy miles of electric range, from the Equinox to the Silverado.""",
   "Chevrolet Silverado 2026", "GM HYBRIDS: LATE 2027 AT THE EARLIEST?")
sc("""Meanwhile, GM shelved a planned refresh of its electric full-size trucks and SUVs, including the Silverado EV, Sierra EV, Hummer EV and Escalade IQ, according to a Crain's Detroit Business report cited by AutoGuide in April twenty twenty-six. GM declined to comment on future products. Plug-in hybrid Silverado and Sierra models were reportedly under consideration for its Orion Assembly plant in Michigan, but that was unconfirmed.""",
   "GMC Sierra EV", "GM SHELVES EV TRUCK REFRESH")
sc("""GM is not abandoning EVs entirely, according to The Washington Post, and it will keep building its current electric trucks at Factory Zero in Detroit for now, according to AutoGuide. It is also adding capacity at its Flint, Michigan plant to meet demand for heavy-duty pickups. The money is going where the buyers are, into gas trucks, while hybrids wait.""",
   "GM Factory Zero", "MONEY GOES TO GAS TRUCKS")
sc("""Here is the twist on GM. The company without a hybrid truck is still winning on sales. GM's Silverado and Sierra together outsold the F-Series in twenty twenty-five. And GM's answer for twenty twenty-seven is two brand-new V8s, a five point seven and a six point six liter. So far, GM is proving that many full-size buyers still choose gas. The question is how long that lasts.""",
   "Chevrolet Silverado 2027", "NO HYBRID, STILL WINNING")

# ---------- 6. NEWCOMERS ----------
sc("""And the newcomers are betting on range extenders too. Scout Motors plans its Terra pickup and Traveler SUV with a Harvester range extender, and about eighty-seven percent of its reservation holders chose that version, according to Electrive. InsideEVs also listed a Kia pickup with extended-range and hybrid versions planned by the end of the decade.""",
   "Scout Terra concept", "SCOUT: 87% CHOSE THE RANGE EXTENDER")
sc("""And Hyundai has said its extended-range vehicles will cost less than comparable electric vehicles, according to InsideEVs. The pattern across the whole industry is the same. A battery for daily driving, and a gas engine for long trips and towing. The arguments are now about how much battery and how much engine, not whether to have both.""",
   "Hyundai Santa Cruz", "BATTERY + GAS ENGINE = THE NEW NORMAL")

# ---------- 7. HYBRID VS EREV ----------
sc("""It helps to understand the three kinds of electrified trucks you will see in twenty twenty-seven. A conventional hybrid, like the F-150 PowerBoost, Tundra and Tacoma i-Force Max, or the Maverick Hybrid, uses a small battery and electric motor to help a gas engine. You never plug it in. You just fill it with gas.""",
   "Ford Maverick Hybrid 2025", "1. HYBRID: NEVER PLUG IN")
sc("""A plug-in hybrid has a bigger battery that you charge, for a few dozen miles of electric driving, and then works like a hybrid. That is what GM is reportedly planning, with about seventy electric miles, and what Stellantis just abandoned. And an extended-range electric truck, like the Ram REV, drives on electricity all the time, with a gas engine that only generates power. You can plug it in, or just fill the tank.""",
   "Ram 1500 REV", "2. PLUG-IN. 3. EXTENDED-RANGE.")
sc("""Here is the twist. Each company picked a different one. Ford sells hybrids now and is adding an extended-range F-150. Toyota bets on hybrids. Ram skipped hybrids and plug-ins for an extended-range truck. And GM, if forecasts are right, will go plug-in hybrid. In five years, we will know which bet was right. For now, buyers are clearly choosing the simplest option, the hybrid you never plug in.""",
   "Toyota Tundra Ford F-150 Ram 1500", "EVERY COMPANY PICKED A DIFFERENT BET")

# ---------- 8. SHOULD YOU BUY ONE ----------
sc("""And watch for one more thing in twenty twenty-seven, the price. As more hybrids and extended-range trucks arrive, automakers will compete on price. Hyundai has already said its extended-range models will cost less than comparable EVs. If GM's plug-in Silverado arrives in late twenty twenty-seven or twenty twenty-eight as forecast, it will compete directly with Ford's extended-range F-150 and the Ram REV. Competition is good for buyers.""",
   "Chevrolet Silverado Ford F-150 Ram", "COMPETITION = BETTER PRICES")
sc("""So should you buy a hybrid truck? Here is how to think about it. The best case is if you drive a lot in town, where hybrids save the most fuel, or if you need power at a job site, where the F-150's onboard generator replaces a separate one. And hybrids are popular, which tends to help resale value. Maverick Hybrid sales hit a record in twenty twenty-six, according to Ford.""",
   "Ford F-150 work site", "BEST FOR CITY + JOB SITE")
sc("""But know the trade-offs. Hybrid versions usually cost more than the gas version of the same trim. And hybrid systems add batteries, motors and electronics that can need repair as a truck ages. Check how long the hybrid components are under warranty, and check the recall history of the exact model, as we covered in our engine and recall videos.""",
   "Toyota Tundra hybrid battery", "CHECK THE HYBRID WARRANTY")
sc("""And if you tow heavy loads most of the time, compare carefully. The hybrid Tacoma is rated to tow less than the best gas Tacoma, according to published specs. A hybrid that spends most of its life towing near its limit will not save as much fuel as one that spends its life in traffic. Buy the truck for the job you actually do, not the job in the brochure.""",
   "Toyota Tacoma towing", "BUY FOR YOUR REAL JOB")

# ---------- CLOSE ----------
sc("""So who is winning the hybrid truck war? Ford, by a wide margin, with a record eighty-five thousand F-150 Hybrids in twenty twenty-five, and a record seventy-four thousand Maverick Hybrids in the first nine months of twenty twenty-six. Toyota, with hybrid power across its trucks. Ram, betting on an extended-range truck and the Hemi at the same time. And GM, with no hybrid truck at all, at least until late twenty twenty-seven, if forecasts are right.""",
   "Ford F-150 Hybrid 2025", "FORD LEADS. GM HAS NONE.")
sc("""And the final twist. The truck industry spent years arguing about gas versus electric. The winner, for now, is the truck that is both. Hybrids reached a record share of American sales in twenty twenty-six, and every major truck maker, including the ones that bet against them, is now racing to add a gas engine to its batteries, or a battery to its gas engines.""",
   "pickup trucks highway", "THE WINNER IS BOTH")
sc("""We put a hybrid versus gas cost calculator, and the warranty questions to ask, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we look at what happened to cheap trucks. And tell us in the comments, would your next truck be a hybrid? Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Ford sold almost eighty-five": "Intro", "First, why is this happening now": "Why hybrids, why now", "Ford is the clear leader": "Ford: the hybrid leader",
      "Toyota is the other hybrid giant": "Toyota: no more V8", "Stellantis, Ram's parent": "Ram and Stellantis: the U-turn",
      "And now the company that is missing": "GM: no hybrid truck yet", "And the newcomers": "Scout, Kia and Hyundai",
      "It helps to understand": "Hybrid vs plug-in vs extended-range", "So should you buy a hybrid truck": "Should you buy one?", "So who is winning": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video36", "length_scale": 1.4,
  "title": "The Hybrid Truck War of 2027: Ford Is Winning, and GM Doesn't Have One", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
