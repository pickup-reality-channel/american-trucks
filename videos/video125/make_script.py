import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The Ford Mustang GTD has no useful trunk. The space where your luggage would go is taken up by a cooler for the gearbox. And its rear wing can flatten itself out like a drag-racing flap, while two flaps under the nose open to keep the car balanced. These are two secrets hidden inside the Ford Mustang GTD, a Mustang that costs more than three hundred thousand dollars.""",
   "Ford Mustang GTD", "2 SECRETS HIDDEN INSIDE THE FORD MUSTANG GTD")
sc("""One: the layout, with a gearbox at the back, a carbon-fibre driveshaft and a cooler where the cargo space should be. Two: the aerodynamics and ride height, which change shape when the car goes onto a track. Along the way we will look at the lap time, the price, and the racing car it came from. Every fact comes from a published source, listed in the description.""",
   "Ford Mustang GTD", "THE REAR GEARBOX · THE SHAPE-SHIFTING AERO")
sc("""Where sources disagree, we tell you. Where we do the maths, we label it as our own. And where a figure is a manufacturer's claim, rather than a measurement, we say so.""",
   "Ford Mustang GTD", "EVERY NUMBER IS SOURCED")

ch("What the GTD is")
sc("""Start with the car. Wikipedia says the current Mustang, the S six fifty, was unveiled on the fourteenth of September, twenty twenty-two, at the North American International Auto Show, and that production began on the first of May, twenty twenty-three, at Flat Rock Assembly. The GTD is the extreme version, unveiled on the seventeenth of August, twenty twenty-three, as a twenty twenty-five model.""",
   "Ford Mustang S650", "S650 MUSTANG UNVEILED SEPT 14, 2022 · GTD UNVEILED AUG 17, 2023 AS A 2025 MODEL")
sc("""Its engine is a five point two litre supercharged Predator V eight, five thousand, one hundred sixty-three cubic centimetres, rated at eight hundred fifteen horsepower at seven thousand, four hundred r p m and six hundred sixty-four pound-feet at four thousand, eight hundred, according to Wikipedia. The page gives a top speed of two hundred two miles per hour. Those figures are consistent with what Kelley Blue Book reported in September twenty twenty-four.""",
   "Ford Mustang GTD engine", "GTD: 5.2 L SUPERCHARGED V8 · 815 HP · 664 LB-FT · 202 MPH (WIKIPEDIA, KBB)")
sc("""Not every source agrees on the power. Design News calls it an eight hundred horsepower beast, and the Torque Café article says reportedly eight hundred. By our arithmetic, the difference between eight hundred and eight hundred fifteen is under two percent, so the sources are close, not contradictory. We use eight hundred fifteen, which Ford's own figure appears to be.""",
   "Ford Mustang GTD power", "815 HP (WIKIPEDIA, KBB, MOTOR1) vs ~800 HP (DESIGN NEWS, TORQUE CAFÉ) — A <2% DIFFERENCE (OUR ARITHMETIC)")
sc("""For scale, Wikipedia lists the ordinary Mustang GT at four hundred eighty horsepower and four hundred eighteen pound-feet, and the Dark Horse at five hundred. By our arithmetic, the GTD makes about seventy percent more power than the GT and about sixty-three percent more than the Dark Horse, and about fifty-nine percent more torque than either. It is not a tuned Mustang. It is a different car sharing a name.""",
   "Ford Mustang GT and GTD", "GTD vs GT: +70% POWER · vs DARK HORSE: +63% · +59% TORQUE (OUR ARITHMETIC)")

ch("Secret one: the missing trunk")
sc("""Here is the first secret. Wikipedia says the GTD has a rear-mounted transaxle, and Kelley Blue Book describes an eight-speed dual-clutch transaxle at the back, with a carbon-fibre driveshaft carrying power from the front-mounted engine. That is the same layout as some high-end sports cars: engine at the front, gearbox at the rear, to move weight rearward.""",
   "Ford Mustang GTD transaxle", "ENGINE UP FRONT · 8-SPEED DUAL-CLUTCH TRANSAXLE AT THE REAR · CARBON-FIBRE DRIVESHAFT")
sc("""The gearbox's maker is not named in the sources we read. Design News quotes Multimatic's chief technical officer, Holt, saying his team put a transaxle gearbox at the rear, without saying who built it. So we do not claim a manufacturer. A normal Mustang, by contrast, has the gearbox directly behind the engine, a six-speed manual or a ten-speed automatic, as Wikipedia lists.""",
   "Mustang GTD gearbox", "GEARBOX MAKER NOT NAMED IN OUR SOURCES · A STANDARD MUSTANG HAS A 6-SPEED MANUAL OR 10-SPEED AUTOMATIC")
sc("""Now the trunk. Kelley Blue Book says the GTD has a pushrod rear suspension with hydraulics, and a transaxle cooler mounted where the cargo space would normally be. In other words, the part of the car that carries your bags now carries the cooling for the gearbox. A road-legal Mustang that has given up its boot to the racetrack.""",
   "Ford Mustang GTD cargo space", "HYDRAULICS AND A TRANSAXLE COOLER SIT WHERE THE CARGO SPACE WOULD BE (KBB)")
sc("""There is a small disagreement about the suspension. Kelley Blue Book and Motor One describe pushrod rear suspension, semi-active and inboard. Design News describes inboard suspension like many prototype race cars, with Multimatic's spool-valve dampers, and does not use the word pushrod. We think these descriptions are compatible, since pushrod systems are normally inboard, but the sources do not say so directly.""",
   "Ford Mustang GTD suspension", "PUSHROD / INBOARD / SPOOL-VALVE DAMPERS — DESCRIPTIONS DIFFER BY SOURCE")
sc("""Multimatic is the key name. Torque Café says it is a Canadian engineering and racing specialist that builds the Mustang GT3 race car, supplies the chassis for Porsche's nine sixty-three L M D h programme, and will assemble the GTD at its own facility rather than at Ford. Design News adds that it supplied the spool-valve shocks and notes it also built the Ford GT. The GTD is partly a Multimatic car.""",
   "Multimatic", "MULTIMATIC: BUILDS THE MUSTANG GT3 · CHASSIS FOR THE PORSCHE 963 · ASSEMBLES THE GTD AT ITS OWN FACILITY")
sc("""And every GTD, Design News says, has a lightweight carbon-fibre body. The Performance package adds magnesium wheels. The sources give no weight for the road car, so we cannot say how much lighter the GTD is than a regular Mustang. Wikipedia lists the standard Mustang GT at between three thousand, eight hundred twenty-seven and four thousand, twelve pounds. We leave the GTD's weight blank rather than guess.""",
   "Ford Mustang GTD carbon fibre", "CARBON-FIBRE BODY ON EVERY GTD · MAGNESIUM WHEELS WITH THE PERFORMANCE PACKAGE · WEIGHT NOT GIVEN")
sc("""Why put the gearbox at the back? None of our sources say so directly. The usual reason, which is our reading and not a quotation, is weight distribution: moving a heavy component rearward balances a front-engined car. We cannot prove it was Ford's reasoning. What the sources do say is that the layout comes from the Mustang GT3 racing programme, which we cover below.""",
   "Mustang GTD layout", "THE REASON IS NOT STATED — WEIGHT BALANCE IS OUR READING")

ch("Secret two: a car that changes shape")
sc("""The second secret is aerodynamic. Design News says the GTD has a dual-element rear wing with an active flap. In high-downforce mode, it generates a large amount of downforce, but also substantial drag. A drag-reduction mode flattens the flap for higher top speed. Kelley Blue Book calls this a Drag Reduction System, which changes the wing angle.""",
   "Ford Mustang GTD rear wing", "DUAL-ELEMENT ACTIVE WING · HIGH-DOWNFORCE MODE vs DRAG-REDUCTION MODE (DESIGN NEWS, KBB)")
sc("""It also has a large front underwing with two flaps that open to reduce front downforce, Design News says, balancing the car when the rear wing changes. In plain terms, when the rear flattens out for speed, the front is relieved too, so the car does not become unstable. Neither source gives downforce figures, so we cannot say how much force each mode produces.""",
   "Ford Mustang GTD front underwing", "FRONT UNDERWING WITH TWO FLAPS · NO DOWNFORCE FIGURES IN EITHER SOURCE")
sc("""The ride height changes too. Design News says the GTD has two ride heights and two sets of spring rates. In track mode, the front drops by forty millimetres and the rear by thirty, adding rake. The rear spring rate doubles, and the front rises by two point eight times. By our arithmetic, the front drops ten millimetres more than the rear, which tilts the car's nose downward.""",
   "Ford Mustang GTD track mode", "TRACK MODE: FRONT −40 MM · REAR −30 MM · REAR SPRING ×2 · FRONT SPRING ×2.8 (DESIGN NEWS)")
sc("""Hold on to what that means. The same car, parked in a driveway, rides like a road car, and on a circuit it changes its stance, its stiffness and its wings. Few road cars do all three. The sources do not give ride height numbers in normal mode, so we cannot tell you how high the car sits. Only the change is documented: forty millimetres at the front.""",
   "Ford Mustang GTD", "ONE CAR, TWO CHARACTERS: ROAD MODE AND TRACK MODE")
sc("""The sources also suggest the aerodynamics were part of a deliberate target. Design News quotes chief engineer Greg Goodall saying that all of it was in the quest for a sub-seven-minute lap of the Nürburgring, and that the Performance package is meant to deliver it. That target became public. Ford's chief executive, Jim Farley, promised at the car's August twenty twenty-three debut that it would break seven minutes, according to AutoGuide.""",
   "Greg Goodall", "TARGET: A SUB-SEVEN-MINUTE NÜRBURGRING LAP (GOODALL, DESIGN NEWS · FARLEY, AUTOGUIDE)")

ch("The lap")
sc("""The promise was kept. AutoGuide reports that the GTD set a certified lap of six minutes, fifty-seven point six eight seconds on the twelve point nine mile Nordschleife, on the seventh of August, twenty twenty-four, driven by Dirk Müller of Multimatic Motorsports. Wikipedia gives six fifty-seven point six eight five. Ford said the car was otherwise stock, with a roll cage, competition seat and five-point harness added for certification.""",
   "Nürburgring Nordschleife", "AUG 7, 2024: 6:57.68 (AUTOGUIDE) / 6:57.685 (WIKIPEDIA) · DIRK MÜLLER · ROLL CAGE + SEAT + HARNESS ADDED")
sc("""AutoGuide says Ford claimed it was the fastest American production car around the Nordschleife, the fifth-fastest production sports car on official records, and the second-fastest front-engined one. The previous American record, it says, was the Dodge Viper ACR's seven oh one point oh three in twenty seventeen. By our arithmetic, the GTD was about three point three seconds, or eight tenths of a percent, quicker.""",
   "Dodge Viper ACR", "PREVIOUS AMERICAN RECORD: VIPER ACR 7:01.03 (2017) · GTD ≈ 3.3 S QUICKER (OUR ARITHMETIC)")
sc("""The fastest front-engined car at that time was the Mercedes-AMG G T Black Series from twenty twenty, at six forty-eight point oh four, nine seconds faster, the article says. Other faster production cars it lists include two Porsche nine eleven G T threes with Manthey kits, a nine eleven G T three R S, and a nine nine one G T two R S with a Manthey kit. Porsche is the benchmark, even in a story about a Mustang.""",
   "Mercedes-AMG GT Black Series", "AMG GT BLACK SERIES 6:48.04 · FASTER: PORSCHE 911 GT3 (MANTHEY), GT3 RS, 991 GT2 RS (MANTHEY)")
sc("""The record did not last. Wikipedia says the GTD ran six fifty-two point oh seven two in May twenty twenty-five, and that the Corvette ZR1 and ZR1X, at six fifty point seven six three and six forty-nine point two seven five, beat it that July. Then, on the seventeenth of April, twenty twenty-six, a pre-production GTD Competition lapped in six forty point eight three five, with magnesium wheels, more power, dive planes and a modified wing.""",
   "Ford Mustang GTD Competition", "GTD 6:52.072 (MAY 2025) · ZR1 6:50.763 · ZR1X 6:49.275 (JULY 2025) · GTD COMPETITION 6:40.835 (APR 17, 2026)")
sc("""By our arithmetic, the GTD Competition was about sixteen point eight five seconds, or four percent, quicker than the original GTD's lap, and about ten seconds quicker than the ZR1. The page does not state how much power the Competition adds, or what tyres it uses, so we cannot attribute the gain to any one change. The point is that the same car kept getting faster.""",
   "Mustang GTD Competition", "GTD COMPETITION ≈ 16.85 S (4.0%) QUICKER THAN THE ORIGINAL (OUR ARITHMETIC) · POWER GAIN NOT STATED")

ch("The racing car behind it")
sc("""The GTD exists because of a race car. Wikipedia says the Mustang G T three was built by Ford and Multimatic, revealed in twenty twenty-three, and raced in I M S A and the World Endurance Championship. Proton Competition was the first customer team in the W E C. The car raced at Le Mans for the first time since nineteen ninety-seven, after a twenty-seven-year absence for a Mustang there.""",
   "Ford Mustang GT3", "MUSTANG GT3: FORD + MULTIMATIC · IMSA AND WEC · LE MANS RETURN AFTER 27 YEARS")
sc("""Torque Café quotes Jim Farley at the twenty twenty-two Mustang launch: to go to Le Mans you need a road car. It says the Mustang Dark Horse is the homologation model for the G T three entry, because the latest rules allow significant technical freedoms, and that Farley approved the road car after seeing early development work on the race car. The GTD is therefore the road version of a race programme.""",
   "Jim Farley", "'TO GO TO LE MANS YOU NEED A ROAD CAR' — JIM FARLEY (QUOTED BY TORQUE CAFÉ) · DARK HORSE = HOMOLOGATION MODEL")
sc("""Torque Café also quotes Ford Performance's global director, Mark Rushbrook, calling the GTD a passion product, and says Ford did not need to build it. The article says Ford requires buyers to submit an application to stop speculators. These are claims from a secondary source, but they match Kelley Blue Book's statement that buyers must apply for permission.""",
   "Mark Rushbrook", "'A PASSION PRODUCT' — MARK RUSHBROOK · BUYERS MUST APPLY (TORQUE CAFÉ, KBB)")
sc("""Ford has other Mustang racing programmes. Wikipedia says a G T four car, announced at the twenty twenty-three Spa twenty-four hours, debuted at the twenty twenty-four Michelin Pilot Challenge at Daytona, and that a Next Gen Dark Horse body was unveiled for NASCAR on the first of November, twenty twenty-three. There is also a track-only Dark Horse R for the I M S A Ford Mustang Challenge. The GTD is the top of a family.""",
   "Ford Mustang racing family", "GT4 (2024) · NASCAR NEXT GEN DARK HORSE (2024) · DARK HORSE R · GT3 · GTD")

ch("What it costs")
sc("""The price. Motor One reported on the twelfth of June, twenty twenty-five that the GTD officially starts at three hundred twenty-seven thousand, nine hundred sixty dollars, including fees and tax: a base price of three hundred eighteen thousand, seven hundred sixty, a five thousand, five hundred dollar destination fee and a three thousand, seven hundred dollar gas-guzzler tax. By our arithmetic, those three figures sum to the headline.""",
   "Ford Mustang GTD price", "$318,760 BASE + $5,500 DESTINATION + $3,700 GAS GUZZLER = $327,960 (OUR ARITHMETIC CONFIRMS)")
sc("""Ford first predicted three hundred thousand dollars, Motor One says, then three hundred twenty-five thousand. An owner's window sticker posted online showed red brake calipers at fifteen hundred dollars and an exposed carbon roof at ten thousand, for a total of three hundred thirty-nine thousand, four hundred sixty dollars. The Monroney label lists twelve miles per gallon combined, seventeen highway and ten city, per the article.""",
   "Ford Mustang GTD window sticker", "FORD'S EARLY ESTIMATES $300K → $325K · EXAMPLE STICKER $339,460 · 12 MPG COMBINED")
sc("""Motor One calls the GTD the most expensive Mustang ever sold, and says it is the most of any Mustang at the base price. We cover the full cost of owning one in another video in this series. For now, note only that the base price alone is more than three hundred thousand dollars, before the destination fee and the gas-guzzler tax.""",
   "Ford Mustang GTD", "THE MOST EXPENSIVE MUSTANG EVER SOLD (MOTOR1) · SEE THE COST VIDEO")

ch("The cheaper Mustang with nearly the same engine")
sc("""A twist. Wikipedia says that on the fifteenth of January, twenty twenty-six, Ford unveiled the Mustang Dark Horse S C, with the same five point two litre supercharged Predator V eight in a more conventional car. It makes seven hundred ninety-five horsepower and six hundred sixty pound-feet, against the GTD's eight hundred fifteen and six hundred sixty-four. By our arithmetic, the GTD has only two and a half percent more power.""",
   "Ford Mustang Dark Horse SC", "DARK HORSE SC (JAN 2026): 795 HP / 660 LB-FT vs GTD 815 HP / 664 LB-FT (+2.5% POWER, OUR ARITHMETIC)")
sc("""That is a revealing comparison. Most of what makes the GTD special, by these numbers, is not the engine. It is the rear gearbox, the suspension, the aerodynamics, the carbon body and the dampers. Our sources do not give a Dark Horse S C price, so we cannot say how much of the GTD's price those parts represent. But the engine alone does not explain it.""",
   "Ford Mustang GTD", "THE ENGINE IS NOT THE DIFFERENCE: 795 vs 815 HP (OUR READING)")
sc("""The same page gives the ordinary Mustang's numbers: a five litre V eight with four hundred eighty horsepower at seven thousand, one hundred fifty r p m in the GT, or four hundred eighty-six with active exhaust. The Dark Horse has five hundred horsepower at seven thousand, two hundred fifty. Europe gets lower figures, four hundred forty-eight and four hundred fifty-three, which the page lists as separate ratings.""",
   "Ford Mustang GT and Dark Horse", "GT 480–486 HP · DARK HORSE 500 HP · EUROPE 448 / 453 HP (WIKIPEDIA)")
sc("""The transmissions differ too. The standard GT uses a Getrag six-speed manual, the Dark Horse a Tremec six-speed manual, and an optional ten-speed automatic is available on the EcoBoost and GT, Wikipedia says. The GTD, by contrast, has an eight-speed dual-clutch transaxle. A ten-speed automatic and an eight-speed dual-clutch are very different machines, even if both are automatic in the loose sense.""",
   "Ford Mustang transmissions", "GT: GETRAG 6-MANUAL · DARK HORSE: TREMEC 6-MANUAL · 10-SPEED AUTO OPTION · GTD: 8-SPEED DCT TRANSAXLE")

ch("The GTD and the Corvette")
sc("""The GTD's natural rival is the Corvette ZR1, and Wikipedia sets them side by side. The ZR1 makes one thousand, sixty-four horsepower and eight hundred twenty-eight pound-feet. By our arithmetic, that is about thirty-one percent more power and about twenty-five percent more torque than the GTD. The ZR1's top speed is two hundred thirty-three miles per hour in a GM test, against the GTD's two hundred two.""",
   "Ford Mustang GTD and Corvette ZR1", "ZR1: 1,064 HP / 828 LB-FT / 233 MPH · GTD: 815 HP / 664 LB-FT / 202 MPH (+31%, +25%, +15% FOR ZR1 — OUR ARITHMETIC)")
sc("""The prices are far apart as well. The ZR1 starts at one hundred seventy-four thousand, nine hundred ninety-five dollars with destination, according to GM, and the GTD's base is three hundred eighteen thousand, seven hundred sixty, according to Motor One. By our arithmetic, the GTD costs about one point eight times as much. The Corvette makes more power for less money. The Mustang is chasing something else.""",
   "Ford Mustang GTD and Corvette ZR1", "GTD BASE $318,760 vs ZR1 $174,995 ≈ 1.8× (OUR ARITHMETIC)")
sc("""What the Mustang is chasing is the Nürburgring and the track, with an active suspension and aerodynamics. Even there, Wikipedia says the Corvette got there first: the ZR1's six fifty point seven six three beat the GTD's six fifty-two point oh seven two in July twenty twenty-five. The Mustang GTD Competition then took the American lead back in April twenty twenty-six, according to the same page.""",
   "Nürburgring American record", "ZR1 6:50.763 BEAT GTD 6:52.072 (JULY 2025) · GTD COMPETITION 6:40.835 TOOK IT BACK (APR 2026)")

ch("A timeline")
sc("""Let us put the dates in order, using our sources. September twenty twenty-two, the S six fifty Mustang. August twenty twenty-three, the GTD debut, with Jim Farley's seven-minute promise. August seventh, twenty twenty-four, the certified lap. December twenty twenty-four, the announcement. June twenty twenty-five, the price. July twenty twenty-five, the Corvette beats its time. April twenty twenty-six, the Competition lap.""",
   "Ford Mustang GTD timeline", "SEP 2022 S650 · AUG 2023 GTD · AUG 7 2024 LAP · DEC 2024 ANNOUNCED · JUN 2025 PRICE · JUL 2025 ZR1 · APR 2026 COMPETITION")
sc("""By our arithmetic, the time from the GTD's debut in August twenty twenty-three to the Competition's lap in April twenty twenty-six is about two years and eight months. In that time, the Mustang's Nürburgring time fell from six fifty-seven point six eight five to six forty point eight three five. That is the whole story of a car that was never finished, only developed further.""",
   "Ford Mustang GTD development", "AUG 2023 → APR 2026 ≈ 2 YEARS 8 MONTHS · 6:57.685 → 6:40.835 (OUR ARITHMETIC)")

ch("Fuel and the guzzler tax")
sc("""One more number that surprised us. Motor One says the GTD's Monroney label shows twelve miles per gallon combined, seventeen on the highway and ten in the city, with a three thousand, seven hundred dollar gas-guzzler tax. By our arithmetic, the tax is about one point two percent of the base price. The Corvette ZR1, according to GM Authority, carries a three thousand dollar tax at fourteen miles per gallon combined.""",
   "Ford Mustang GTD fuel economy", "GTD: 12 MPG COMBINED · $3,700 GUZZLER TAX (≈1.2% OF BASE) · ZR1: 14 MPG · $3,000")
sc("""So the Mustang uses more fuel than the Corvette in the rating, by about two miles per gallon, and pays a higher tax. Neither is built to save fuel. But it is a reminder that a car which changes its aerodynamics and ride height for the track is also a car that makes compromises on the road. The sources do not say how much of the difference is the extra drag, the heavier gearbox or something else.""",
   "Ford Mustang GTD", "GTD ≈ 2 MPG BELOW THE ZR1 AND A HIGHER TAX · CAUSE NOT STATED")

ch("What we cannot tell you")
sc("""A number of things are missing from our sources. We did not find a sourced curb weight, a sourced zero to sixty time, the brake and tyre specification, downforce figures, or the number of cars to be built per year. Motor One's page carries a headline about fifty cars a year, but no detail in the text, so we do not repeat it. If you have a primary source, tell us in the comments.""",
   "Ford Mustang GTD", "NOT IN OUR SOURCES: WEIGHT · 0–60 · BRAKES · TYRES · DOWNFORCE · PRODUCTION RUN")
sc("""And a note on the two Wikipedia pages. The Mustang page gives the Porsche nine eleven G T three R S record as six forty-nine point three two eight, while the nine eleven G T three page gives six forty-four point eight four eight for the same car, set by Jörg Bergmeister on the fifth of October, twenty twenty-two. We cannot settle that. We flag it, and we cover the Porsche in the comparison video.""",
   "Porsche 911 GT3 RS", "WIKIPEDIA CONFLICT: GT3 RS NÜRBURGRING 6:49.328 (MUSTANG PAGE) vs 6:44.848 (GT3 PAGE)")

ch("Recap")
sc("""So, two secrets. First, the GTD is a front-engined car with an eight-speed dual-clutch transaxle at the back and a carbon driveshaft, and the space where a boot should be holds a cooler and hydraulics. Second, it changes shape on a circuit, with an active wing that flattens for speed, front flaps that open, and a body that drops forty millimetres at the nose.""",
   "Ford Mustang GTD", "1. GEARBOX AT THE BACK, COOLER WHERE THE TRUNK SHOULD BE · 2. A WING AND RIDE HEIGHT THAT CHANGE SHAPE")
sc("""Would you rather have a trunk or a lap record? Tell us in the comments, with a source if you have one. In the other videos of this series, we compare the GTD with the Porsche nine eleven G T three, work out what it really costs to own one, and tell why Ford built a Mustang to beat Porsche. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford Mustang GTD", "SUBSCRIBE: PICKUP REALITY")

save("video125", "2 Secrets Hidden Inside the Ford Mustang GTD", [
    "Wikipedia, Ford Mustang (seventh generation) and Mustang GTD: https://en.wikipedia.org/wiki/Ford_Mustang_GTD",
    "Kelley Blue Book, Ford drops details on GTD, the uber Mustang: https://www.kbb.com/car-news/ford-drops-details-on-gtd-the-uber-mustang",
    "Design News, Engineering the Maximum Mustang GTD: https://www.designnews.com/automotive-engineering/engineering-the-maximum-mustang-gtd",
    "AutoGuide, Ford Mustang GTD joins Nürburgring's sub-seven-minute club: https://www.autoguide.com/auto/manufacturers/ford/ford-mustang-gtd-joins-nrburgring-s-sub-seven-minute-club-44615074",
    "Torque Café, Why Ford built a race car for the road: https://archive.torquecafe.com/why-ford-built-a-race-car-for-the-road/",
    "Motor1, The Ford Mustang GTD is even more expensive than we thought: https://www.motor1.com/news/762588/ford-mustang-gtd-price-window-sticker/",
    "Wikipedia, Porsche 911 GT3: https://en.wikipedia.org/wiki/Porsche_911_GT3",
], "A")
