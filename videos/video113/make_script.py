import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The Ferrari F forty was built in thirteen months, from the leftovers of a racing programme that had been cancelled. And it had no door handles, no glove box, no leather and no sound system. Yet it cost about four hundred thousand dollars, roughly five times the car it replaced, and speculators sold some for more than seven times list price. These are the two secrets hidden inside the Ferrari F forty.""",
   "Ferrari F40", "2 SECRETS HIDDEN INSIDE THE FERRARI F40")
sc("""Here is the twist. Ferrari planned to build four hundred of them. It built more than thirteen hundred. And the same page that tells us all that also says only about ten percent of the cars delivered were used for regular driving. Stay to the end, because the sources disagree on several numbers, and we will show you where.""",
   "Ferrari F40", "PLANNED: 400 · BUILT: 1,311+")
sc("""Every figure comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Ferrari F40", "EVERY NUMBER IS SOURCED")

ch("Secret one: a car made from leftovers")
sc("""Start with how it began. Wikipedia says Nicola Materazzi proposed the concept to Enzo Ferrari in nineteen eighty-four, and that the car grew out of the two eighty-eight G T O Evoluzione. The Group B racing category ended before the nineteen eighty-six season, leaving Ferrari with five Evoluzione development cars and nowhere to race them.""",
   "Ferrari 288 GTO Evoluzione", "1984: MATERAZZI'S PROPOSAL · 5 LEFTOVER EVOLUZIONE CARS")
sc("""Project work on the F forty began on the tenth of June, nineteen eighty-six, according to the same page. Enzo Ferrari wanted the car done in about eleven months. The car was unveiled on the twenty-first of July, nineteen eighty-seven, in Maranello. By the page's own account, development took thirteen months from inception to launch.""",
   "Maranello", "PROJECT BEGAN 10 JUNE 1986 · UNVEILED 21 JULY 1987")
sc("""By our own arithmetic, from the tenth of June nineteen eighty-six to the twenty-first of July nineteen eighty-seven is thirteen months and eleven days. That agrees with the page. Compare it with the other cars in this series. The Lexus LFA took about ten and a half years from start to production. The Mercedes-AMG One took more than five years from its reveal to its first delivery.""",
   "Ferrari F40 prototype", "13 MONTHS (OUR ARITHMETIC) VS LFA ~10.5 YEARS")
sc("""A caution. One of our sources, Classic Motorsports, says the F forty was presented in nineteen eighty-seven for Ferrari's fortieth anniversary. Another source, a vehicle archive page, says Enzo Ferrari presented the car at Maranello in June nineteen eighty-seven. Wikipedia gives the twenty-first of July. We use July, since Wikipedia is specific, and we flag the difference.""",
   "Ferrari F40 launch", "SOURCES DIFFER: JUNE 1987 VS 21 JULY 1987")
sc("""The F forty was built to mark Ferrari's fortieth anniversary and was the last Ferrari that Enzo Ferrari personally approved, Wikipedia says. Classic Motorsports adds that he died in nineteen eighty-eight at the age of ninety. The vehicle archive page says the car was presented fourteen months before his death. By our arithmetic, that puts his death in about August nineteen eighty-eight.""",
   "Enzo Ferrari", "THE LAST FERRARI ENZO APPROVED · HE DIED IN 1988 AT 90")
sc("""The engine was inherited too. Wikipedia describes the F one twenty A, a two thousand, nine hundred thirty-six cubic centimetre, twin-turbocharged, intercooled ninety-degree V eight, an enlarged version of the two eighty-eight G T O's engine. It claims four hundred seventy-eight metric horsepower at seven thousand r p m and five hundred seventy-seven newton-metres at four thousand. The U S version is listed at four hundred eighty-four.""",
   "Ferrari F120A engine", "2.9 L TWIN-TURBO V8 · 478 PS @ 7,000 RPM · 577 NM")
sc("""Other sources describe the same engine differently. The vehicle archive says about five hundred brake horsepower at seven thousand r p m, with two water-cooled I H I turbochargers at one point one bar. Classic Motorsports says four hundred seventy-eight horsepower at a factory boost of about eight point seven psi, or point six bar, and over five hundred at one bar. The sources disagree about boost, and we cannot resolve it.""",
   "Ferrari F40 turbo", "BOOST: 0.6 BAR (CLASSIC MOTORSPORTS) VS 1.1 BAR (ARCHIVE)")
sc("""So the first secret is this. The most famous Ferrari of the nineteen eighties was not designed on a clean sheet. It was assembled from a cancelled racing programme, an existing engine and a very short deadline, by a team that included Materazzi as chief engineer. Pininfarina's Pietro Camardella designed the body under Aldo Brovarone's supervision, according to Wikipedia.""",
   "Ferrari F40", "BUILT FROM A CANCELLED RACING PROGRAMME (OUR READING)")
sc("""Does that make it a lesser car? The evidence says no. Wikipedia lists an independent test at four point seven seconds from zero to a hundred kilometres per hour with a top speed of three hundred twenty-one kilometres per hour, about one hundred ninety-nine miles per hour. Road and Track measured three hundred fifteen, and Car and Driver three hundred seventeen. A quick project does not mean a slow car.""",
   "Ferrari F40 test", "0–100 IN 4.7 S · 321 KM/H (WIKIPEDIA)")
sc("""The archive page goes further. It says the F forty was the first production car to pass two hundred miles per hour, at two hundred one. The Wikipedia page, by contrast, lists measured top speeds below two hundred, one ninety-six and one ninety-seven, from magazine tests. A claim and a measurement are different things. We report both, and we note that the claim is the one that made the headlines.""",
   "Ferrari F40 speed", "CLAIM: 201 MPH (ARCHIVE) · MEASURED: 196–197 MPH (R&T, C&D)")

ch("Secret two: what was left out")
sc("""Now the second secret. Wikipedia describes the interior. The cars had moderate air conditioning but no sound system, no door handles, no glove box, no leather, no carpets and no door panels. The first fifty cars had sliding Lexan windows. Later cars had wind-down windows. Pirelli developed a special P Zero tyre for the car.""",
   "Ferrari F40 interior", "NO DOOR HANDLES · NO GLOVE BOX · NO LEATHER · NO CARPETS")
sc("""The body was made of Kevlar, carbon fibre and aluminium, the page says, with polycarbonate windows. The vehicle archive describes eleven composite panels of Nomex, Kevlar and carbon, a tubular steel chassis with bonded composite inserts, and a ventilated Plexiglas rear screen. It calls the F forty the first car whose bodywork was made entirely of composites.""",
   "Ferrari F40 body", "BODYWORK ENTIRELY COMPOSITE: KEVLAR, CARBON, NOMEX")
sc("""Weight shows the result. Wikipedia lists one thousand, two hundred fifty-four kilograms for Europe and one thousand, three hundred sixty-nine for the United States. The archive says one thousand, two hundred two. Classic Motorsports says about three thousand pounds for the U S car, which is about one thousand, three hundred sixty kilograms. Three different weights, and the differences are over a hundred and fifty kilograms.""",
   "Ferrari F40 weight", "1,202 / 1,254 / 1,369 KG: THREE SOURCES, THREE WEIGHTS")
sc("""Here is the twist about price. Wikipedia says the launch price was about four hundred thousand dollars, roughly five times the price of the two eighty-eight G T O, which the page converts to about one million, one hundred thirty thousand dollars today. A car with fewer features than its predecessor cost five times as much. That is the second secret: the lack of luxury was not a discount, it was the point.""",
   "Ferrari F40", "$400,000 NEW · ~5× THE 288 GTO")
sc("""Enzo Ferrari, Classic Motorsports says, reportedly wanted drivers to be terrified when they accelerated. The driver's experience, from the owner it quotes, includes minimal turbo lag and a strong push that builds toward seven thousand, five hundred r p m, a long clutch, a dog-leg manual gearbox, strong brakes with little feel and no A B S. It is a very direct car.""",
   "Ferrari F40 cockpit", "NO ABS · LITTLE BRAKE FEEL · A VERY DIRECT CAR")
sc("""Wikipedia does not mention A B S, and implies the car lacked a steering and brake servo, based on a Ferrari test driver's comment. We take Classic Motorsports' statement that there was no A B S as one source, and Wikipedia's implication about servos as another. Neither is a complete specification, so we say only that the car was basic by design.""",
   "Ferrari F40", "NO ABS (CLASSIC MOTORSPORTS) · NO SERVOS IMPLIED (WIKIPEDIA)")
sc("""There was a catalytic converter story too. Wikipedia says no catalytic converters were fitted until nineteen ninety, when U S rules required them. The vehicle archive says that from nineteen ninety-one, cars got catalytic converters, and adjustable suspension became an option. The U S market cars are described by Sotheby's as having non-adjustable suspension, so the options differed by market.""",
   "Ferrari F40 exhaust", "CATALYTIC CONVERTERS FROM 1990–91 · ADJUSTABLE SUSPENSION OPTIONAL")

sc("""Some arithmetic on the engine, all ours, from Wikipedia's figures. Four hundred seventy-eight metric horsepower from two point nine three six litres is about one hundred sixty-three horsepower per litre. That was a very high figure for a road car in nineteen eighty-seven, achieved with turbochargers. For comparison, the Lexus LFA's naturally aspirated V ten made about one hundred seventeen per litre, two decades later.""",
   "Ferrari F40 engine", "~163 PS PER LITRE (OUR ARITHMETIC)")
sc("""Power to weight. Four hundred seventy-eight horsepower over the European weight of one thousand, two hundred fifty-four kilograms is about point three eight horsepower per kilogram. Over the U S weight of one thousand, three hundred sixty-nine it is point three five. These are our sums. Wikipedia itself gives no power to weight ratio for the F forty, and the weights differ between sources.""",
   "Power to weight", "0.38 PS/KG (EUROPE) · 0.35 PS/KG (US) (OUR ARITHMETIC)")
sc("""Price per horsepower, again ours. Four hundred thousand dollars over four hundred seventy-eight horsepower is about eight hundred thirty-seven dollars per horsepower. The Lexus LFA, at three hundred seventy-five thousand and five hundred fifty-three horsepower, was about six hundred seventy-eight, twenty-three years later. The F forty was not cheap even for its time, and this shows it.""",
   "Calculator", "F40 ~$837/HP (1987) VS LFA ~$678/HP (2010) (OUR ARITHMETIC)")
sc("""The two eighty-eight G T O, by Wikipedia's account, cost about one fifth as much. By our arithmetic, one fifth of four hundred thousand is eighty thousand dollars. The page does not give the G T O's price directly, so that is a derived figure, not a quotation. The point is the multiple: a Ferrari that was five times the price of the previous one, and was sold out.""",
   "Ferrari 288 GTO", "288 GTO ≈ $80,000 (DERIVED FROM 'ROUGHLY 5×')")
sc("""The dimensions are those of a compact supercar. Wikipedia lists a wheelbase of two thousand, four hundred fifty millimetres, a length of four thousand, four hundred thirty, a width of one thousand, nine hundred seventy and a height of one thousand, one hundred twenty-four. The drag coefficient is point three four. It is low and wide, and by modern standards short.""",
   "Ferrari F40 side", "4,430 MM LONG · 1,124 MM TALL · Cd 0.34")
sc("""Compare it with the Mercedes-AMG One from another video of this series, since both are mid-engined hypercars. The AMG One is four thousand, seven hundred fifty-six millimetres long and one thousand, two hundred sixty-one tall, according to Wikipedia. By our arithmetic, the F forty is three hundred twenty-six millimetres shorter and a hundred thirty-seven millimetres lower. It is the smaller car in every dimension we have.""",
   "Ferrari F40 and Mercedes-AMG One", "F40: 326 MM SHORTER · 137 MM LOWER THAN AN AMG ONE (OUR ARITHMETIC)")
sc("""The tyres were special. Wikipedia says Pirelli developed a special P Zero tyre for the car. Autopian reports the replacement sizes on a surviving car as two hundred forty-five over forty on seventeen inch wheels at the front and three hundred thirty-five over thirty-five at the back. A rear tyre of three hundred thirty-five millimetres is wide even now, and was extreme in nineteen eighty-seven.""",
   "Pirelli P Zero tyres", "245/40 R17 FRONT · 335/35 R17 REAR")
sc("""The F forty has a front boot, Classic Motorsports says, though it is small. It also says speed bumps can scrape the carbon sills, which is costly to repair, and that the nose can wander on uneven surfaces. These are the realities behind the legend. A car that was designed to be a racer, and then made legal, is not designed for car parks.""",
   "Ferrari F40 front", "SPEED BUMPS CAN SCRAPE THE CARBON SILLS")
sc("""Its handling carries a warning. Classic Motorsports quotes a specialist, Philippe Sébille: if you have it at an angle when the turbos kick in, it's gone. He also says to leave the hero stuff for the race tracks, where there is run-off. The quotes are from a specialist who services these cars, and they describe a car that rewards care and punishes carelessness.""",
   "Ferrari F40 turbo lag", "\"IF YOU HAVE IT AT AN ANGLE WHEN THE TURBOS KICK IN, IT'S GONE\"")
sc("""Yet the same specialist calls the car very durable, and says it is definitely cheaper to run than the F fifty that followed it. That is the third surprise, if you like: the stripped, difficult F forty is described as relatively robust and economical, compared with the more sophisticated car that replaced it. We return to costs in another video of this series.""",
   "Ferrari F40", "\"VERY DURABLE\" · \"CHEAPER TO RUN THAN THE F50\"")
sc("""Both secrets are really about the same thing, which is intention. A car made in thirteen months could only have what was necessary. A car with no luxuries could only be about driving. Ferrari did not apologise for either. Enzo Ferrari, who died the following year, never saw how the car would be remembered. The sources suggest it was remembered very well.""",
   "Enzo Ferrari and the F40", "INTENTION: ONLY WHAT WAS NECESSARY (OUR READING)")
sc("""A word on how we count. When we say a source says something, we mean that in the pages we read. We read Wikipedia, Classic Motorsports, Sotheby's, a vehicle archive and an Autopian article. We did not read the owner's manual, or Ferrari's own records. Where those might disagree with what we reported, they win. That is the honest limit of a video like this.""",
   "Research", "WHAT WE READ — AND WHAT WE DID NOT")
sc("""Now back to the numbers that will stay with you. Thirteen months from start to launch. Four hundred planned, thirteen hundred built. Four hundred thousand dollars new, five times the previous car. More than seven times list price for the speculators in nineteen eighty-nine. Ten percent used regularly. Eleven million dollars for a racing version in twenty twenty-five. Each is sourced above.""",
   "Ferrari F40", "13 MONTHS · 400 → 1,311 · $400K · 7× · 10% · $11M")

ch("A bonus: the numbers nobody planned")
sc("""And a bonus secret: the production. Wikipedia says planned production was four hundred units, and that the total was one thousand, three hundred eleven, with some sources saying up to one thousand, three hundred fifteen. Classic Motorsports also says four hundred planned and one thousand, three hundred fifteen built. By our arithmetic, that is about three and a quarter times the plan.""",
   "Ferrari F40 production", "PLANNED 400 · BUILT 1,311–1,315 (≈3.3× PLAN, OUR ARITHMETIC)")
sc("""Where did they go? Wikipedia says two hundred thirteen cars were destined for the United States. The vehicle archive says about six hundred of the one thousand, three hundred eleven were for the U S A. Those cannot both be right, unless they count different things. Sotheby's, in a 2025 article, repeats the two hundred thirteen figure for the North American allocation. We use two hundred thirteen.""",
   "Ferrari F40 US market", "US CARS: 213 (WIKIPEDIA, SOTHEBY'S) VS ~600 (ARCHIVE)")
sc("""Every car was Rosso Corsa and left-hand drive, Wikipedia says, though at least seven were converted to right-hand drive for the Sultan of Brunei. The production years vary by source. The infobox says nineteen eighty-seven to nineteen ninety-six, the lead says nineteen eighty-seven to ninety-three for the road car, and Classic Motorsports says nineteen eighty-seven to ninety-two.""",
   "Ferrari F40 Rosso Corsa", "ALL ROSSO CORSA · LEFT-HAND DRIVE (7 CONVERTED FOR BRUNEI)")
sc("""Now the speculators. Wikipedia says speculators sold cars for up to more than seven times list price in nineteen eighty-nine. By our arithmetic, seven times four hundred thousand is two point eight million dollars. A nineteen ninety estimate, the page adds, said only about ten percent of delivered cars were used for regular driving. The rest were stored or traded.""",
   "Ferrari F40 speculators", "1989: UP TO 7× LIST (≈ $2.8M) · ONLY ~10% DRIVEN REGULARLY")
sc("""The page also says Nigel Mansell's car sold for a record one million pounds in nineteen ninety, and that the same car, in a two thousand fourteen Bonhams auction, reached five hundred forty-three thousand, three hundred seventy-five pounds. By our arithmetic, that is about forty-six percent lower, in pounds, over twenty-four years. A reminder that prices go down as well as up, at least for a while.""",
   "Nigel Mansell Ferrari F40", "MANSELL'S CAR: £1M (1990) → £543,375 (2014)")

sc("""Some more arithmetic on production. One thousand, three hundred eleven cars over five years, nineteen eighty-seven to ninety-two, is about two hundred sixty-two cars a year, by our arithmetic. The Lamborghini Urus, according to Wikipedia, was built at a rate of seven thousand, two hundred sixty-five in a single year in twenty twenty-five. The F forty's output was tiny by comparison.""",
   "Ferrari factory", "~262 F40S A YEAR VS 7,265 URUS IN 2025 (OUR ARITHMETIC)")
sc("""And the ten percent. If only about ten percent of delivered cars were used for regular driving, as a nineteen ninety estimate cited by Wikipedia says, then by our arithmetic about a hundred thirty-one of the one thousand, three hundred eleven were. That is an estimate of an estimate, so treat it as a feel for scale. The great majority were collected, stored or traded.""",
   "Ferrari F40 storage", "~131 OF 1,311 USED REGULARLY (OUR ARITHMETIC OF AN ESTIMATE)")
sc("""The dog-leg gearbox is one more detail from the owner's account. Classic Motorsports describes a dog-leg manual that shifts slowly but precisely, with reader comments saying it has five speeds, not six as the article states. Wikipedia lists a five-speed manual, rear-wheel drive. So the article's six is likely an error, though the article remains our source for the feel of the shift.""",
   "Ferrari F40 gearbox", "FIVE-SPEED DOG-LEG MANUAL (WIKIPEDIA) · ARTICLE'S 'SIX' CHALLENGED")
sc("""One last thing about the interior. The vehicle archive lists a tubular steel chassis with bonded composite inserts, mainly around the sills and the floor pan, and eleven body panels in Nomex, Kevlar and carbon. The sparse cabin was not an accident of cost. It was a consequence of a car designed around weight. Every handle and carpet was a kilogram that could be left out.""",
   "Ferrari F40 chassis", "EVERY HANDLE AND CARPET WAS WEIGHT (OUR READING)")

ch("The racing cars")
sc("""The road car also spawned racers. Wikipedia says the F forty L M debuted at Laguna Seca on the fifteenth of October, nineteen eighty-nine, and finished third overall. Ten competition-spec cars were built, two L M cars and eight Competizione cars. The Competizione is rated at seven hundred metric horsepower, with a reported top speed of about three hundred sixty-seven kilometres per hour.""",
   "Ferrari F40 LM", "F40 LM: 3RD AT LAGUNA SECA, 1989 · COMPETIZIONE: 700 PS")
sc("""The F forty G T E, Wikipedia says, had its engine enlarged from three litres to three point five in nineteen ninety-five and three point six in nineteen ninety-six, producing six hundred twenty metric horsepower. Seven were converted by Michelotto. The G T E won the four hours of Anderstorp in nineteen ninety-five and again in ninety-six. The page counts nineteen racing cars in total.""",
   "Ferrari F40 GTE", "F40 GTE: 620 PS · 7 BY MICHELOTTO · 19 RACING CARS IN ALL")
sc("""Sotheby's reports that in August twenty twenty-five an F forty L M by Michelotto sold at R M Sotheby's for eleven million, five thousand dollars. It was one of nineteen Michelotto-prepared examples, with about seven hundred sixty horsepower, the most powerful F forty variant. By our arithmetic, that is about twenty-seven and a half times the original four hundred thousand dollar price of a road car.""",
   "Ferrari F40 LM Michelotto", "AUG 2025: F40 LM SOLD FOR $11,005,000 (RM SOTHEBY'S)")

ch("The secret that did not change")
sc("""Look back at the two secrets. A car made in thirteen months from leftovers. A car stripped of comforts that cost five times its predecessor. Both are about restraint: of time and of equipment. Ferrari did less, faster, and charged more. And the customers, as the speculators show, would pay almost any price. That combination is difficult to repeat.""",
   "Ferrari F40", "LESS, FASTER, AT A HIGHER PRICE (OUR READING)")
sc("""The Nardò test is another reminder. Wikipedia says that at the Nardò track, Ferrari's two cars could not exceed three hundred twenty-one kilometres per hour, while the Porsche nine fifty-nine S reached three hundred thirty-nine. The F forty's reputation does not rest on being the fastest car on paper. In another video of this series, we compare the two cars directly.""",
   "Nardò ring", "NARDÒ: F40 321 KM/H · 959 S 339 KM/H")
sc("""One more caution. We have not driven an F forty. The sources disagree about weight, boost, production years and the number of U S cars, and we have said so. Where we did arithmetic, we labelled it. If you know a verified detail from a primary source, tell us in the comments, so that we can correct it.""",
   "Ferrari F40", "WEIGHT, BOOST, YEARS, US COUNT: SOURCES DISAGREE")
sc("""Which secret surprised you more, the thirteen months or the missing door handles? Tell us in the comments. In the other videos of this series, we compare the F forty with the Porsche nine fifty-nine, work out what it really costs to own one, and tell the story of the last car Enzo Ferrari approved. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video113", "2 Secrets Hidden Inside the Ferrari F40", [
    "Wikipedia, Ferrari F40: https://en.wikipedia.org/wiki/Ferrari_F40",
    "Classic Motorsports, Ferrari F40: the truth about living with a legend: https://classicmotorsports.com/articles/ferrari-f40-how-you-spend-million/",
    "Sotheby's, The six most expensive Ferrari F40s: https://www.sothebys.com/en/articles/the-six-most-expensive-ferrari-f40s",
    "DK Engineering, Ferrari F40 (1990) vehicle archive: https://www.dkeng.co.uk/Vehicle_Archive/797/ferrari_f40.html",
    "Wikipedia, Porsche 959: https://en.wikipedia.org/wiki/Porsche_959",
], "A")
