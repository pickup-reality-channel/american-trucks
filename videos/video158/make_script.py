import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Two Koenigsegg hybrids, one very different idea. The Regera has no gearbox in the usual sense, and sold out in two years. The Gemera has four seats, and took six years to reach production. They look like cousins, but the numbers say they were built for different jobs. We compare them side by side, and every figure comes from a named source.""",
   "Gemera vs Regera", "KOENIGSEGG GEMERA vs REGERA: THE REAL DIFFERENCE")
sc("""Our sources are Wikipedia's pages on the Gemera, the Regera and Koenigsegg, a March twenty twenty-six report on AOL, Motor1, InsideHook and the RM Sotheby's catalogue for a twenty twenty Regera. Where they disagree, we show both figures. Our own maths is labelled as our arithmetic. Anything we could not find is flagged.""",
   "Gemera and Regera", "SOURCES: WIKIPEDIA · AOL (30 MAR 2026) · MOTOR1 · INSIDEHOOK · RM SOTHEBY'S (MONTEREY 2024) · DISAGREEMENTS SHOWN · OUR ARITHMETIC LABELLED")

ch("Round one: the seats")
sc("""Start with the biggest difference you can see. The Regera is a two-seater. Wikipedia lists its dimensions as four thousand five hundred sixty millimetres long, two thousand fifty wide and eleven hundred ten tall, on a wheelbase of twenty-six sixty-two. The Gemera is four thousand nine hundred seventy-five long, nineteen eighty-eight wide and twelve ninety-five tall, on a three thousand millimetre wheelbase.""",
   "Size", "WIKIPEDIA REGERA: L 4,560 · W 2,050 · H 1,110 · WB 2,662 MM · GEMERA: L 4,975 · W 1,988 · H 1,295 · WB 3,000 MM")
sc("""By our arithmetic, the Gemera is four hundred fifteen millimetres longer, three hundred thirty-eight millimetres longer in the wheelbase, and one hundred eighty-five millimetres taller. But it is sixty-two millimetres narrower. In inches, that is about sixteen point three longer and seven point three taller. It is a longer, taller, slimmer car, built to fit four people.""",
   "The difference", "4,975 − 4,560 = 415 MM · 3,000 − 2,662 = 338 MM · 1,295 − 1,110 = 185 MM · 1,988 − 2,050 = −62 MM (OUR ARITHMETIC) · 415 MM = 16.3 IN; 185 MM = 7.3 IN (OUR CONVERSIONS)")
sc("""Wikipedia calls the Gemera the first four-seat Koenigsegg, with two doors, no B-pillar and dihedral synchro-helix doors. The Regera, according to the same encyclopedia, is a two-seat grand tourer. The Gemera's grand-touring idea was a cited headline calling it a Mega GT. The Regera's door design is not described in the paragraphs we used, so we make no claim.""",
   "Seats and doors", "WIKIPEDIA: GEMERA — FIRST 4-SEAT KOENIGSEGG, 2 DOORS, NO B-PILLAR, DIHEDRAL SYNCHRO-HELIX DOORS · REGERA — 2-SEAT GRAND TOURER · REGERA DOOR DESIGN: NOT IN THE PASSAGES WE USED")

ch("Round two: the engine")
sc("""Both cars have a five-litre twin-turbo V8 in their top form, at least on paper. Wikipedia says the Regera's V8 makes eleven hundred horsepower on regular fuel and fifteen hundred on E85. The Gemera's V8 version is also a five-litre twin-turbo on E85, and Wikipedia gives its total system output as twenty-three hundred horsepower.""",
   "The engines", "WIKIPEDIA: REGERA 5.0 L TWIN-TURBO V8 — 1,100 HP (1,500 HP ON E85) · GEMERA V8 VERSION — 5.0 L TWIN-TURBO V8 ON E85 · SYSTEM 2,300 HP · 2,750 N·M (2,028 LB-FT)")
sc("""There is a catch. The Regera's fifteen hundred horsepower is, in Wikipedia's infobox, the combined total with the electric motors. The text on the same page says one thousand seven hundred ninety-seven. And the eleven hundred and fifteen hundred figures for the V8 are quoted for the engine alone. So the Regera page contains three different power numbers.""",
   "Regera's three numbers", "WIKIPEDIA (REGERA): V8 1,100 HP (PUMP) / 1,500 HP (E85) · COMBINED 1,500 HP (INFOBOX) vs 1,797 HP (TEXT) → THE PAGE GIVES MORE THAN ONE TOTAL")
sc("""The Gemera had its own version. The original three-cylinder car had a two-litre twin-turbo inline three making six hundred horsepower, and Wikipedia says it was dropped in July twenty twenty-four for lack of demand. So today, the real comparison is the V8 Gemera against the V8 Regera, and both run on E85 for their biggest numbers.""",
   "Gemera engines", "WIKIPEDIA: I3 (2.0 L TFG, 600 HP) DROPPED JULY 2024 — 'LACK OF DEMAND' · V8 VERSION IS THE ONE IN PRODUCTION · INSIDEHOOK: V8-ONLY, HOLDOUTS PERSUADED")
sc("""By our arithmetic, the Gemera's twenty-three hundred is fifty-three percent above the Regera's fifteen hundred and twenty-eight percent above the seventeen ninety-seven. If you subtract the Gemera's eight-hundred-horsepower electric motor, you get fifteen hundred from the V8. That matches the Regera's engine on E85. In our reading, the two V8s are in the same class.""",
   "Power comparison", "2,300 ÷ 1,500 = +53.3% · 2,300 ÷ 1,797 = +28.0% · 2,300 − 800 = 1,500 HP (OUR ARITHMETIC) · 'SAME CLASS' = OUR READING; NO SOURCE COMPARES THE TWO ENGINES DIRECTLY")

ch("Round three: how they use electricity")
sc("""The electric side is where the two cars part ways. Wikipedia says the Regera has three YASA electric motors with a combined six hundred ninety-seven horsepower, a direct-drive system with a single two point seven three to one ratio, and a four-and-a-half kilowatt-hour battery from Rimac weighing seventy-five kilograms.""",
   "Regera electrics", "WIKIPEDIA (REGERA): 3 YASA MOTORS · 697 HP COMBINED · DIRECT DRIVE 2.73:1 · 4.5 KWH BATTERY (RIMAC), 75 KG")
sc("""The Gemera has an eight-hundred-fifty-volt, fourteen-kilowatt-hour battery, and a Dark Matter front motor of eight hundred horsepower. By our arithmetic, its battery is three point one times bigger than the Regera's, and its electric power eight hundred against six ninety-seven, fifteen percent higher. That is why the Gemera can drive fifty kilometres on electricity alone.""",
   "Gemera electrics", "WIKIPEDIA (GEMERA): 850 V, 14 KWH · FRONT 'DARK MATTER' MOTOR 600 KW (800 HP) · 50 KM ELECTRIC RANGE · 14 ÷ 4.5 = 3.1× · 800 ÷ 697 = +14.8% (OUR ARITHMETIC)")
sc("""Rear motors are a point of confusion. Wikipedia's Gemera text describes two rear motors of five hundred horsepower each plus the front one, but its table lists only the single front motor, and AOL says the three motors were replaced by one in twenty twenty-three. So the production Gemera most likely has one motor, though the encyclopedia page keeps both descriptions.""",
   "Which Gemera?", "WIKIPEDIA TEXT: FRONT 800 HP + 2 REAR 500 HP EACH · TABLE: SINGLE MOTOR · AOL: 2023 CHANGE TO ONE 800 HP MOTOR · 'MOST LIKELY ONE MOTOR' = OUR READING OF THESE SOURCES")
sc("""Battery range matters here. The Gemera claims fourteen hundred sixty-three kilometres in total, nine hundred nine miles, with fifty kilometres on electricity alone. The Regera has no electric-only range in the sources we have: its battery is only four and a half kilowatt-hours. We have not found a published electric range for it.""",
   "Electric range", "WIKIPEDIA: GEMERA TOTAL RANGE 1,463 KM (909 MI), ELECTRIC 50 KM (31 MI) · REGERA ELECTRIC-ONLY RANGE: NOT IN OUR SOURCES")

ch("Round four: the transmission")
sc("""The Regera is the car with no conventional gearbox. Wikipedia describes a direct-drive system with a single fixed ratio of two point seven three to one, linking the engine and electric motors to the wheels. We use that description as the page gives it; the encyclopedia does not explain how the clutch works, and neither do our other sources.""",
   "Direct drive", "WIKIPEDIA (REGERA): DIRECT DRIVE, RATIO 2.73:1 · CLUTCH OPERATION / ENGAGEMENT DETAILS: NOT DESCRIBED IN OUR SOURCES")
sc("""The Gemera does have a gearbox. Wikipedia says the V8 version uses a nine-speed Light Speed Tourbillon Transmission, a modified version of the unit in the Jesko. InsideHook quotes Autoblog calling the Gemera's version smaller, lighter and better. That is the outlet's opinion, and we have no measured data on its weight.""",
   "Gemera gearbox", "WIKIPEDIA: GEMERA V8 — 9-SPEED LIGHT SPEED TOURBILLON TRANSMISSION (LSTT), MODIFIED JESKO UNIT · INSIDEHOOK / AUTOBLOG: 'SMALLER, LIGHTER, BETTER' (OPINION) · TRANSMISSION WEIGHT: NOT IN OUR SOURCES")
sc("""So one car relies on a single ratio and the other on nine. By our arithmetic, that is eight more gears. The sources do not say which approach is quicker, and we do not know of a head-to-head test. What they do say is the Regera's own acceleration claims, which we cover next.""",
   "One ratio vs nine", "9 − 1 = 8 MORE GEARS (OUR ARITHMETIC) · HEAD-TO-HEAD TEST: NOT IN OUR SOURCES")

ch("Round five: speed claims")
sc("""Acceleration numbers from Wikipedia. The Regera: zero to one hundred kilometres per hour in two point eight seconds, zero to two hundred in six point six, zero to three hundred in ten point nine, zero to four hundred in twenty. The Gemera's claim is one point nine seconds to one hundred, but for the three-cylinder car that is no longer offered.""",
   "Acceleration claims", "WIKIPEDIA: REGERA 0–100 2.8 S · 0–200 6.6 S · 0–300 10.9 S · 0–400 20 S · GEMERA 0–100 1.9 S (I3 VERSION, DROPPED) · V8 GEMERA 0–100: NOT IN OUR SOURCES")
sc("""The Regera also has a record. Wikipedia says that on the sixteenth of June twenty twenty-three at Örebro, it went from zero to four hundred and back to zero in twenty-eight point eight one seconds, regaining the record from the Rimac Nevera at twenty-nine point nine three seconds in May. In September twenty nineteen it had done thirty-one point four nine.""",
   "The 0–400–0 record", "WIKIPEDIA: 23 SEP 2019 — 31.49 S (RÅDA) · 16 JUN 2023 — 28.81 S (ÖREBRO), REGAINED FROM RIMAC NEVERA 29.93 S (MAY 2023)")
sc("""By our arithmetic, the Regera improved its own record by two point six eight seconds between twenty nineteen and twenty twenty-three, or eight and a half percent, and beat the Nevera by one point one two seconds. The Gemera has no record claimed in any of our sources, so on that scoreboard the Regera wins by default.""",
   "How big a record", "31.49 − 28.81 = 2.68 S (−8.5%) · 29.93 − 28.81 = 1.12 S (OUR ARITHMETIC) · GEMERA RECORD CLAIMS: NONE IN OUR SOURCES")
sc("""Top speeds. Wikipedia lists a claimed four hundred kilometres per hour for the three-cylinder Gemera, and three hundred in electric mode. For the Regera, the sources we fetched list acceleration to four hundred, but no separate top-speed figure. That means we cannot say which is faster flat out, only which has more published claims.""",
   "Top speed", "WIKIPEDIA: GEMERA I3 400 KM/H CLAIM; 300 KM/H ELECTRIC MODE · REGERA TOP SPEED: NOT SEPARATELY LISTED IN THE PASSAGES WE USED (0–400 KM/H IN 20 S IS LISTED) · FASTER FLAT-OUT CAR: CANNOT BE SAID")

ch("Round six: weight")
sc("""Weight is awkward because both pages give more than one figure. For the Regera, Wikipedia lists fourteen seventy kilograms dry, fifteen ninety kerb and fifteen seventy elsewhere. For the Gemera, nineteen eighty-eight for the twenty twenty prototype and twenty forty-two for twenty twenty-three production.""",
   "Weights", "WIKIPEDIA: REGERA 1,470 KG DRY · 1,590 KG KERB · 1,570 KG (THREE FIGURES) · GEMERA 1,988 KG (2020 PROTOTYPE) · 2,042 KG (2023 PRODUCTION)")
sc("""By our arithmetic, the Gemera is at least four hundred fifty-two kilograms heavier than the Regera. The Gemera carries two extra seats, a bigger battery and a longer body. Our reading is that the weight difference is the price of space. No source states that reason.""",
   "Heavier by", "2,042 − 1,590 = 452 KG; 2,042 − 1,570 = 472 KG; 2,042 − 1,470 = 572 KG (OUR ARITHMETIC; DRY vs KERB NOT LIKE-FOR-LIKE) · 'PRICE OF SPACE' = OUR READING, NOT STATED BY ANY SOURCE")
sc("""Power to weight, by our arithmetic and with the caveats, comes out like this. Gemera V8: twenty-three hundred over twenty forty-two is one point one three horsepower per kilogram. Regera: fifteen hundred over fifteen ninety is zero point nine four. By that measure the Gemera wins on paper, thanks to its bigger electric system.""",
   "Power to weight", "GEMERA 2,300 ÷ 2,042 = 1.13 HP/KG · REGERA 1,500 ÷ 1,590 = 0.94 HP/KG (OUR ARITHMETIC; MIXED SOURCE FIGURES) · RESULT IS ONLY AS GOOD AS THE CLAIMS")

ch("Round seven: production")
sc("""How many were made? Wikipedia's Regera infobox says eighty were built. The body of the article says eighty-five. RM Sotheby's, selling a twenty twenty car in twenty twenty-four, says eighty-five. The Regera was unveiled in Geneva in March twenty fifteen, produced from March twenty sixteen to twenty twenty-two, and sold out on the thirteenth of June twenty seventeen.""",
   "Regera production", "WIKIPEDIA: INFOBOX 80 BUILT · TEXT 85 BUILT · RM SOTHEBY'S: 85 BUILT · UNVEILED MARCH 2015 · PRODUCTION MARCH 2016–2022 · SOLD OUT 13 JUNE 2017")
sc("""The Gemera is limited to three hundred, according to both Wikipedia and AOL. AOL says all of them are spoken for. By our arithmetic, that is three point five times as many as the eighty-five Regeras. Koenigsegg's total output per year is not given, and neither are the deliveries to date.""",
   "Gemera production", "WIKIPEDIA + AOL: LIMITED TO 300 · AOL: ALL SPOKEN FOR · 300 ÷ 85 = 3.5× (OUR ARITHMETIC) · ANNUAL OUTPUT / DELIVERIES TO DATE: NOT IN OUR SOURCES")
sc("""Timing is the sharpest contrast. By our arithmetic, the Regera sold out about two years and three months after its reveal. The Gemera was revealed on the third of March twenty twenty, was originally scheduled for production in twenty twenty-two, and began production in March twenty twenty-six, six years later, according to AOL and Wikipedia.""",
   "Timeline", "REGERA: MARCH 2015 → SOLD OUT 13 JUNE 2017 ≈ 2 YR 3 MO (OUR ARITHMETIC) · GEMERA: REVEAL 3 MAR 2020 → PRODUCTION ANNOUNCED 30 MAR 2026 ≈ 6 YR (OUR ARITHMETIC) · ORIGINALLY SCHEDULED 2022")

ch("Round eight: price")
sc("""Prices. For the Gemera, Motor1 reported in April twenty twenty that Christian von Koenigsegg told Top Gear the U.S.-spec car starts at one point seven million dollars. InsideHook reports a rumoured four hundred thousand dollar premium for the V8. For the Regera, Wikipedia's citation titles carry nineteen hundred thousand dollars, and one point five million pounds.""",
   "Prices", "MOTOR1 (13 APR 2020): GEMERA U.S.-SPEC FROM $1.7 M · INSIDEHOOK (29 JULY 2024): RUMOURED +$400,000 FOR V8 · WIKIPEDIA REGERA CITATION TITLES: $1.9 M AND £1.5 M (NO LIST PRICE IN THE TEXT)")
sc("""So on the face of it, the Gemera's base price is lower than the Regera's quoted figure. By our arithmetic, one point seven is eleven percent below one point nine. Add the rumoured four hundred thousand for the V8 and it becomes two point one million, which is eleven percent above. Neither number is an official production price list.""",
   "Which costs more?", "1.7 ÷ 1.9 = −10.5% · 2.1 ÷ 1.9 = +10.5% (OUR ARITHMETIC) · OFFICIAL PRODUCTION PRICE LISTS FOR EITHER CAR: NOT IN OUR SOURCES")
sc("""The used market gives a harder data point. RM Sotheby's offered a twenty twenty Regera with fifteen hundred twelve miles at Monterey in twenty twenty-four, estimating two point seven five to three point two five million dollars. It was not sold. There is no such auction record for the Gemera in our sources, since deliveries have only just begun.""",
   "The auction", "RM SOTHEBY'S MONTEREY 2024, LOT 240: 2020 REGERA, 1,512 MILES, CHASSIS 186, ESTIMATE $2.75–3.25 M, NOT SOLD · GEMERA AUCTION RESULTS: NONE IN OUR SOURCES")
sc("""The same lot lists about five hundred one thousand dollars of options, including a one hundred seventy thousand dollar clear carbon finish and fifty-seven thousand dollar wheels. Wikipedia mentions upgrades of seven hundred ten thousand dollars on another auctioned Regera. By our arithmetic, options of that scale are as much as a third of the Gemera's base price.""",
   "Options", "RM SOTHEBY'S LOT 240: OPTIONS ≈ $501,330 (CLEAR CARBON $170,000; TRESEX AIRCORE WHEELS $57,000) · WIKIPEDIA: UPGRADES $710,200 ON ONE AUCTIONED CAR · $501,330 ÷ $1.7 M = 29.5% (OUR ARITHMETIC; DIFFERENT CARS)")

ch("Round nine: what each car is for")
sc("""Put it together. The Regera is a two-seat hypercar built around direct drive and records. The Gemera is a four-seat grand tourer with a gearbox, a bigger battery and a limited run of three hundred. Wikipedia and the Car and Driver headline describe the Gemera as a Mega GT. The word GT is the encyclopedia's, not ours, and the company's own definition is not in our sources.""",
   "Different jobs", "SYNTHESIS FROM WIKIPEDIA (REGERA, GEMERA) · 'MEGA GT' = CAR AND DRIVER HEADLINE, CITED ON WIKIPEDIA · COMPANY'S OWN DEFINITION: NOT IN OUR SOURCES")
sc("""Where would you win a drag race? On the evidence we have, we cannot say. The Gemera has more power on paper and more weight. The Regera has a record and a direct-drive layout. No source we found puts the two on a track together, so any declared winner would be a guess. We prefer to leave that to a real test.""",
   "Who wins?", "NO HEAD-TO-HEAD TEST IN OUR SOURCES · GEMERA: MORE POWER, MORE WEIGHT · REGERA: PUBLISHED 0–400–0 RECORD · ANY WINNER = GUESS")
sc("""The Regera's reputation includes one more detail, its sell-out speed. Wikipedia says it sold out on the thirteenth of June twenty seventeen. By our arithmetic, selling eighty-five cars in about twenty-seven months is about three cars a month. The Gemera's three hundred cars, over its first six years, is about four cars a month, if you count orders from the reveal.""",
   "Sales pace", "REGERA: ~85 CARS ÷ ~27 MONTHS ≈ 3.1/MONTH · GEMERA: 300 ÷ ~72 MONTHS ≈ 4.2/MONTH (OUR ARITHMETIC; ASSUMES ALL 300 ORDERED SINCE REVEAL, WHICH SOURCES DO NOT STATE)")

ch("The company behind both")
sc("""Both cars come from the same company. Wikipedia says Koenigsegg was founded in nineteen ninety-four by Christian von Koenigsegg, who was twenty-two, with sixty million kronor from investors. By end of twenty twenty-three it had just under eight hundred staff, and in July twenty twenty-three a new factory opened, doubling capacity.""",
   "Koenigsegg", "WIKIPEDIA: FOUNDED 1994 · CHRISTIAN von KOENIGSEGG, AGE 22 · KR 60,000,000 FROM INVESTORS · JUST UNDER 800 STAFF (END-2023) · NEW FACTORY JULY 2023 DOUBLED CAPACITY")
sc("""The company's lineup as of twenty twenty-six, in Wikipedia's account, is the Jesko, the Gemera and the CC850. The Regera has been out of production since twenty twenty-two. The Jesko Attack holds a Laguna Seca lap record of one minute twenty-four point eight six seconds, from August twenty twenty-four. The Gemera is not claimed to have one.""",
   "The lineup", "WIKIPEDIA: 2026 LINE-UP — JESKO, GEMERA, CC850 · REGERA PRODUCTION ENDED 2022 · JESKO ATTACK LAGUNA SECA 1:24.86 (18 AUG 2024) · GEMERA LAP RECORD: NONE CLAIMED IN OUR SOURCES")

ch("Round ten: living with them")
sc("""Use matters too. The Gemera is described by Wikipedia as a four-seat car with eight cup holders, four of them heated and four cooled, four touchscreens and eleven speakers. Nothing in our sources describes the Regera's cabin in comparable detail. So any comparison of comfort is one-sided: we know the Gemera's list, and we do not know the Regera's.""",
   "Cabin", "WIKIPEDIA (GEMERA): 8 CUP HOLDERS (4 HEATED, 4 COOLED) · 4 TOUCHSCREENS · 11 SPEAKERS · REGERA CABIN EQUIPMENT: NOT IN THE PASSAGES WE USED")
sc("""The wheels are listed for the Gemera: twenty-one inches at the front, twenty-two at the rear, on Michelin Pilot Sport 4S as standard or Cup 2R as an option. The Regera's wheel sizes are not in the passages we fetched, though RM Sotheby's lists optional Tresex AirCore wheels at fifty-seven thousand dollars. Those are the only wheel numbers we can cite for the Regera.""",
   "Wheels", "WIKIPEDIA (GEMERA): 21 IN FRONT, 22 IN REAR · MICHELIN PILOT SPORT 4S / CUP 2R · RM SOTHEBY'S (REGERA LOT 240): TRESEX AIRCORE WHEELS $57,000 (OPTION) · REGERA WHEEL SIZES: NOT IN OUR SOURCES")
sc("""Service costs are a fair comparison only on one side. RM Sotheby's reports that the Regera in lot two-forty had a third-year service and updates in spring twenty twenty-four costing nearly nineteen thousand dollars, including a technician flown in from Sweden. For the Gemera, no service cost is published in our sources, so we cannot compare.""",
   "Service", "RM SOTHEBY'S (REGERA LOT 240): THIRD-YEAR SERVICE + UPDATES, SPRING 2024, NEARLY $19,000, TECHNICIAN FLOWN FROM SWEDEN · GEMERA SERVICE COST: NOT IN OUR SOURCES")
sc("""One more point from the auction. The Regera for sale had a protective paint film applied in twenty twenty-one and clear carbon bodywork, which the catalogue lists at one hundred seventy thousand dollars. The Gemera has an optional Ghost package, but our sources do not describe it. So in finishes, we can only list the Regera's.""",
   "Finishes", "RM SOTHEBY'S (REGERA): PAINT FILM APPLIED 2021 · CLEAR CARBON $170,000 · DARK CARBON WITH GOLD DUST $62,000 · WIKIPEDIA (GEMERA): OPTIONAL GHOST PACKAGE, CONTENTS NOT DESCRIBED")
sc("""By our arithmetic, the three biggest options on that Regera, clear carbon at one hundred seventy thousand, dark carbon with gold dust at sixty-two thousand and the wheels at fifty-seven thousand, add up to two hundred eighty-nine thousand dollars. That is about fifty-eight percent of the catalogue's total options figure of five hundred one thousand.""",
   "Biggest options", "$170,000 + $62,000 + $57,000 = $289,000 · $289,000 ÷ $501,330 = 57.6% (OUR ARITHMETIC; RM SOTHEBY'S FIGURES)")
sc("""Mileage is a quiet detail. The auctioned Regera had fifteen hundred twelve miles. By our arithmetic, over four years from its twenty twenty model year to the auction in twenty twenty-four, that is about three hundred seventy-eight miles a year. These cars are often kept more than driven, but the catalogue does not say how this one was used.""",
   "Mileage", "RM SOTHEBY'S LOT 240: 1,512 MILES · 2020 → 2024 = 4 YEARS · 1,512 ÷ 4 = 378 MI/YR (OUR ARITHMETIC) · USAGE PATTERN: NOT STATED")

ch("Round eleven: the numbers that do not line up")
sc("""A summary of the disagreements we found. Regera build count: eighty or eighty-five. Regera combined power: fifteen hundred or seventeen ninety-seven. Regera weight: fourteen seventy dry, fifteen seventy or fifteen ninety kerb. Gemera weight: nineteen eighty-eight or twenty forty-two. Gemera motors: one or three. Gemera V8 power: twenty-three hundred or twenty-two sixty-nine.""",
   "The conflicts", "CONFLICTS IN OUR SOURCES: REGERA BUILT 80 / 85 · REGERA POWER 1,500 / 1,797 HP · REGERA WEIGHT 1,470 / 1,570 / 1,590 KG · GEMERA WEIGHT 1,988 / 2,042 KG · GEMERA MOTORS 1 / 3 · GEMERA V8 2,300 / 2,269 HP")
sc("""Why so many? Part of the answer is time. The Gemera was revised between twenty twenty and twenty twenty-three, and the Wikipedia page keeps older and newer figures side by side. The Regera's differences look more like different counting rules. But our sources do not say why the numbers differ, so that explanation is our reading, not a fact.""",
   "Why they differ", "GEMERA: 2020 PROTOTYPE vs 2023 PRODUCTION FIGURES ON ONE PAGE · REGERA: CAUSE OF DIFFERENCES NOT STATED · 'COUNTING RULES' = OUR GUESS")
sc("""For the viewer, the practical rule is simple. When you see a hypercar number quoted without a source and a date, treat it as a claim. A press release, a catalogue, and an encyclopedia page can all disagree. In this video we gave you the range of figures instead of picking the one that makes the best story.""",
   "How to read the numbers", "RULE OF THUMB = OUR EDITORIAL POSITION · FIGURES SHOWN AS RANGES WHERE SOURCES DISAGREE")
sc("""One last comparison, our own. Add the production counts: eighty-five Regeras and three hundred Gemeras make three hundred eighty-five cars. By our arithmetic, the Gemera is seventy-eight percent of that combined total. If every Gemera is delivered, Koenigsegg will have built more than three times as many of this hybrid family in the Gemera as in the Regera.""",
   "Combined", "85 + 300 = 385 · 300 ÷ 385 = 77.9% · 300 ÷ 85 = 3.5× (OUR ARITHMETIC; ASSUMES 85 REGERAS AND ALL 300 GEMERAS DELIVERED)")

ch("Round twelve: the engineering choices")
sc("""One more way to compare is by what each car chose to leave out. The Regera left out a conventional multi-speed gearbox, using a single fixed ratio. The Gemera left out its original three-cylinder and its three electric motors. Both are cases of simplification, though in the Gemera's case the sources say it happened after the first reveal, not before it.""",
   "What was left out", "WIKIPEDIA (REGERA): FIXED 2.73:1 DIRECT DRIVE · AOL + WIKIPEDIA (GEMERA): I3 AND 3-MOTOR LAYOUT DROPPED 2023–2024 · 'SIMPLIFICATION' = OUR WORD; AOL SAYS THE 2023 CHANGE CUT 'WEIGHT AND COMPLEXITY'")
sc("""A note on E85. Both cars reach their headline power on E85, an ethanol blend. Wikipedia says so for the Regera's fifteen hundred and the Gemera's twenty-three hundred. On ordinary pump fuel, the Regera's V8 is rated at eleven hundred. The Gemera's pump-fuel V8 figure is not in our sources, so we cannot say how much power an owner loses on regular gas.""",
   "E85", "WIKIPEDIA: REGERA V8 1,100 HP (PUMP) / 1,500 HP (E85) · GEMERA V8 SYSTEM 2,300 HP ON E85 · GEMERA PUMP-FUEL FIGURE: NOT IN OUR SOURCES")
sc("""By our arithmetic, the Regera loses about twenty-seven percent of its V8 power on pump fuel compared with E85: eleven hundred is seventy-three percent of fifteen hundred. That matters for buyers in places where E85 is not sold. Neither the Gemera nor the Regera page says how many owners actually run E85.""",
   "Pump fuel penalty", "1,100 ÷ 1,500 = 73.3% → −26.7% (OUR ARITHMETIC; WIKIPEDIA FIGURES) · OWNERS' ACTUAL FUEL USE: NOT IN OUR SOURCES")
sc("""There is also the question of where each car sits in the Koenigsegg story. Wikipedia's company page lists the Agera, Regera, Jesko, Gemera and CC850 among the models. The Regera arrived in twenty fifteen, the Gemera in twenty twenty. By our arithmetic, that is five years between reveals, and the Gemera's production start came eleven years after the Regera's reveal.""",
   "Where they sit", "WIKIPEDIA: REGERA REVEAL MARCH 2015 · GEMERA REVEAL MARCH 2020 · GEMERA PRODUCTION MARCH 2026 · 2015 → 2020 = 5 YR · 2015 → 2026 = 11 YR (OUR ARITHMETIC)")
sc("""So if you are choosing, ask what you want the car for. Four seats and a gearbox point to the Gemera. A two-seat record holder with direct drive points to the Regera. The prices, in the sources we found, are of similar size, from about one point seven to two point one million for the Gemera and nearly two million for the Regera. Our advice is to read the specifications, not the headlines.""",
   "Choosing", "GEMERA $1.7–2.1 M (MOTOR1; INSIDEHOOK, V8 PREMIUM RUMOURED) · REGERA ≈ $1.9 M (WIKIPEDIA CITATION TITLE) · ADVICE = OUR EDITORIAL OPINION, NOT BUYING ADVICE")

ch("What the sources do not say")
sc("""What is missing. A measured head-to-head test. A reconciled weight for the production Gemera. An official production price for either car. The Regera's top speed. The V8 Gemera's zero to one hundred time. And the split of Gemeras between V8 and the old three-cylinder. If you have a primary source for any of these, put it in the comments.""",
   "Gemera and Regera", "NOT IN OUR SOURCES: HEAD-TO-HEAD TEST · RECONCILED GEMERA WEIGHT · OFFICIAL PRICES · REGERA TOP SPEED · V8 GEMERA 0–100 · V8/I3 SPLIT")
sc("""So the real difference is not speed, because the sources do not settle that. It is purpose. The Regera is a two-seat record car with direct drive and eighty-five units. The Gemera is a four-seat grand tourer with a gearbox and three hundred units. In the other videos, we count the cost of owning a Koenigsegg and tell why they build cars in a fighter-jet hangar. Subscribe to Pickup Reality.""",
   "Gemera and Regera", "SUBSCRIBE: PICKUP REALITY")

save("video158", "Koenigsegg Gemera vs Regera: The Real Difference", [
    "Wikipedia, Koenigsegg Gemera: https://en.wikipedia.org/wiki/Koenigsegg_Gemera",
    "Wikipedia, Koenigsegg Regera: https://en.wikipedia.org/wiki/Koenigsegg_Regera",
    "Wikipedia, Koenigsegg: https://en.wikipedia.org/wiki/Koenigsegg_Automotive",
    "AOL (Car and Driver), The Koenigsegg Gemera is finally starting production, six years after it was revealed, 30 Mar 2026: https://www.aol.com/articles/koenigsegg-gemera-finally-starting-production-210300723.html",
    "Motor1, Koenigsegg Gemera build slot already available at McLaren dealer, 13 Apr 2020: https://www.motor1.com/news/409351/koenigsegg-gemera-build-slot-sale/",
    "InsideHook (Tobias Carroll), V8 Koenigsegg supercar buyers pay an extra $400,000, 29 Jul 2024: https://www.insidehook.com/autos/v8-koenigsegg-supercar-buyers-extra-400000/amp",
    "RM Sotheby's, 2020 Koenigsegg Regera, Monterey 2024, lot 240",
], "B")
