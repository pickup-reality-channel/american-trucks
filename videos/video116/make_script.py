import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""In nineteen eighty-seven, Ferrari unveiled a car that broke almost every rule of the road car. No door handles. No carpets. No sound system. It was the last Ferrari approved by Enzo Ferrari himself, and it was built in thirteen months. This is the story of the F forty, from a cancelled racing category to a car that now sells for millions.""",
   "Ferrari F40", "THE INSANE STORY BEHIND THE LAST CAR ENZO FERRARI APPROVED")
sc("""The story starts with a car that was never allowed to race. It involves a rivalry with Porsche, a deadline set by a man in his late eighties, a car that was planned for four hundred buyers and built for over thirteen hundred, and speculators who sold cars at seven times the list price. We will tell it in order, and say where our sources disagree.""",
   "Maranello", "A CAR THAT NEVER RACED, A DEADLINE, AND A BUBBLE")
sc("""Every fact comes from a published source, listed in the description. Where we do the maths ourselves, we say so. Where sources disagree, we tell you. And where we offer our own reading rather than a fact, we label it. Let us begin in nineteen eighty-four.""",
   "Ferrari F40", "EVERY CLAIM IS SOURCED")

ch("1984: The Evoluzione")
sc("""Wikipedia says the idea for the F forty was proposed by Nicola Materazzi in nineteen eighty-four. The car grew out of the two eighty-eight G T O Evoluzione, a development of the two eighty-eight G T O that Ferrari built for the Group B racing category. The page says the Evoluzione was a test bed for what would become the F forty.""",
   "Ferrari 288 GTO", "1984: MATERAZZI PROPOSES THE CAR · IT GROWS FROM THE 288 GTO EVOLUZIONE")
sc("""Group B was the racing category for powerful, lightly regulated cars, best known for rallying. Wikipedia says the category was ended before the nineteen eighty-six season, so the Ferrari Evoluzione never raced. Five Evoluzione cars were built and left with nowhere to compete. That is the first twist: the F forty exists because a racing rule book was torn up.""",
   "Group B rally", "GROUP B ENDED BEFORE 1986 · 5 EVOLUZIONE CARS LEFT WITH NOWHERE TO RACE")
sc("""By our arithmetic, five cars is a tiny number, less than half of one percent of the one thousand, three hundred eleven F forty cars that were eventually built. The Evoluzione was the experiment, and the F forty was what Ferrari did with it. The sources do not say who first suggested turning the experiment into a customer car, so we do not claim to know.""",
   "Ferrari Evoluzione", "5 EVOLUZIONE CARS ≈ 0.4% OF 1,311 F40s (OUR ARITHMETIC)")

ch("The man and the anniversary")
sc("""The F forty was built for a date. Wikipedia says Ferrari's fortieth anniversary was approaching, and the car was meant to celebrate it. The page says it was the last Ferrari to be approved by Enzo Ferrari. Classic Motorsports adds that Enzo died in nineteen eighty-eight, at the age of ninety. By our arithmetic, that puts his birth around eighteen ninety-eight.""",
   "Enzo Ferrari", "BUILT FOR FERRARI'S 40TH ANNIVERSARY · ENZO DIED IN 1988 AT 90")
sc("""The DK Engineering archive says the car was presented fourteen months before Enzo's death. Wikipedia says it was unveiled on the twenty-first of July, nineteen eighty-seven in Maranello. The archive says June of that year. The sources agree on the year, not the month. If Wikipedia's date is right, Enzo lived about a year after the unveiling, by our reckoning.""",
   "Maranello factory", "UNVEILED JULY 21, 1987 (WIKIPEDIA) OR JUNE 1987 (DK ENGINEERING)")
sc("""Here is a point we have to be careful about. Many retellings say Enzo personally pushed the project. Our sources say he approved it, and Wikipedia says he wanted it finished in about eleven months. We do not have a source for any quotation from him, so we do not attribute any words to him. We tell you only what the sources say.""",
   "Enzo Ferrari", "WHAT THE SOURCES SAY: HE APPROVED IT AND WANTED IT IN ~11 MONTHS")
sc("""The project began on the tenth of June, nineteen eighty-six, according to Wikipedia. It was unveiled thirteen months later. By our arithmetic, that is about two months over Enzo's eleven-month wish, a delay of roughly eighteen percent. Not bad for a car that had to be designed, engineered, tested and ready to build, in a period shorter than a typical school year.""",
   "Ferrari F40 development", "JUNE 10, 1986 → JULY 21, 1987: 13 MONTHS vs 11 REQUESTED (OUR ARITHMETIC)")

ch("The rival in Stuttgart")
sc("""There was a rival, and it was Porsche. Wikipedia says the nine fifty-nine, a Group B-derived all-wheel-drive car, began development in nineteen eighty-one, was shown at Frankfurt in nineteen eighty-three as a prototype, and reached customers in nineteen eighty-seven. Our sources do not say that Ferrari built the F forty to beat it, so we do not claim that.""",
   "Porsche 959", "PORSCHE 959: 1981 START · 1983 PROTOTYPE · 1987 DELIVERIES")
sc("""What the sources do say is that both cars arrived in nineteen eighty-seven and that they were then compared. Wikipedia lists the Porsche as faster at Nardò: three hundred thirty-nine kilometres per hour for the nine fifty-nine S, against a limit of three hundred twenty-one for the Ferrari. By our arithmetic, that is eighteen kilometres per hour, about five and a half percent.""",
   "Nardò Ring", "NARDÒ: 959 S 339 KM/H · F40 NOT OVER 321 KM/H")
sc("""But the F forty was lighter, simpler and, on paper, more powerful. Four hundred seventy-eight metric horsepower against four hundred fifty. One thousand, two hundred fifty-four kilograms against one thousand, four hundred fifty. Rear-wheel drive against all-wheel drive. By our arithmetic, the Ferrari was about thirteen and a half percent lighter. The two cars represent two philosophies.""",
   "Ferrari F40 and Porsche 959", "F40 478 PS / 1,254 KG · 959 450 PS / 1,450 KG")
sc("""The prices tell a story too. Wikipedia says the Porsche cost four hundred thirty-one thousand, five hundred fifty Deutsche Marks, about two hundred twenty-five thousand dollars, less than half of what it cost Porsche to make. The F forty launched at about four hundred thousand dollars. By our arithmetic, the Ferrari cost about seventy-eight percent more than the Porsche, and so, presumably, it made money.""",
   "Ferrari F40 and Porsche 959 price", "F40 ~$400K · 959 ~$225K (DM 431,550) · 959 PRICE < HALF OF BUILD COST")

ch("How the car was made")
sc("""Wikipedia says the body was designed by Pietro Camardella under Aldo Brovarone at Pininfarina. The result is a low, wide car: four thousand, four hundred thirty millimetres long, one thousand, nine hundred seventy wide, one thousand, one hundred twenty-four tall. Its drag coefficient is listed at point three four. The page says the shape was driven by aerodynamics and cooling.""",
   "Pininfarina", "DESIGNED BY PIETRO CAMARDELLA UNDER ALDO BROVARONE · Cd 0.34")
sc("""The engine is the F one twenty A, a two thousand, nine hundred thirty-six cubic centimetre twin-turbocharged V eight with four hundred seventy-eight metric horsepower at seven thousand r p m and five hundred seventy-seven newton-metres at four thousand. The U S version is rated at four hundred eighty-four. Power goes to the rear wheels through a five-speed manual gearbox, Wikipedia says.""",
   "Ferrari F120A engine", "F120A: 2.9 L TWIN-TURBO V8 · 478 PS · 577 NM · 5-SPEED MANUAL, RWD")
sc("""The DK Engineering archive says the body uses eleven composite panels. Classic Motorsports calls the car very durable. Wikipedia describes the interior in negatives: no door handles, no glove box, no leather, no carpets, no door panels and no sound system. By our reading, this is a car where every missing part was a decision to save weight.""",
   "Ferrari F40 interior", "11 COMPOSITE PANELS · NO HANDLES · NO CARPETS · NO SOUND SYSTEM")
sc("""Performance, per Wikipedia. The first independent test recorded zero to a hundred kilometres per hour in four point seven seconds and a top speed of three hundred twenty-one. Road and Track measured three hundred fifteen, Car and Driver three hundred seventeen. The drag coefficient and the power are known; the top speed varies by test, which is typical for cars at this level.""",
   "Ferrari F40 test", "0–100 KM/H 4.7 S · 315–321 KM/H DEPENDING ON THE TEST")
sc("""The famous claim is that it was the first production car to reach two hundred miles per hour. The DK Engineering archive says two hundred one, and Classic Motorsports two hundred two. But Wikipedia's measured figures, three hundred fifteen to three hundred seventeen kilometres per hour, work out at about one ninety-six to one ninety-seven miles per hour, by our arithmetic. The legend and the measurements do not quite match.""",
   "Ferrari F40 speedometer", "THE '200 MPH' CLAIM VS MEASURED ~196–197 MPH (OUR ARITHMETIC)")

ch("The plan for four hundred")
sc("""Wikipedia says Ferrari planned to build four hundred F forty cars. The launch price was about four hundred thousand dollars, around five times the price of the two eighty-eight G T O. The company expected, by our reading, that the car would sell to a small circle of customers. The sources do not say what the sales forecast was, so we leave it there.""",
   "Ferrari F40", "PLANNED PRODUCTION: 400 CARS · PRICE ~5× THE 288 GTO")
sc("""Demand was far higher than that. Wikipedia says production ended with one thousand, three hundred eleven cars, with some sources saying up to one thousand, three hundred fifteen. By our arithmetic, that is more than three times the original plan. Two hundred thirteen of them were for the United States, according to Wikipedia and Sotheby's, though the DK Engineering archive says about six hundred.""",
   "Ferrari production line", "BUILT: 1,311 (UP TO 1,315) · US: 213 (WIKIPEDIA) VS ~600 (DK ENGINEERING)")
sc("""The cars were all painted Rosso Corsa and built with left-hand drive, Wikipedia says, except for at least seven right-hand-drive cars for the Sultan of Brunei. That detail is easy to repeat and hard to check, so we note that the page gives it as at least seven, not exactly seven. It is the sort of fact that a source can only partly support.""",
   "Rosso Corsa", "ALL ROSSO CORSA, LEFT-HAND DRIVE · AT LEAST 7 RHD FOR BRUNEI")

ch("The bubble")
sc("""Then came the speculators. Wikipedia says that in nineteen eighty-nine, cars were sold at up to more than seven times the list price. By our arithmetic, seven times four hundred thousand is at least two million, eight hundred thousand dollars. A new car's price had gone up sevenfold in about two years. It is a classic bubble pattern, and it did not last.""",
   "Ferrari F40 speculators", "1989: SOLD AT UP TO 7× LIST PRICE ≈ $2.8M+ (OUR ARITHMETIC)")
sc("""Nigel Mansell's F forty sold for one million pounds in nineteen ninety, Wikipedia says. In twenty fourteen it sold again, at Bonhams, for five hundred forty-three thousand, three hundred seventy-five pounds. By our arithmetic, that is a drop of about forty-six percent in nominal pounds across twenty-four years. The bubble that began in nineteen eighty-nine had a long and painful hangover.""",
   "Nigel Mansell", "MANSELL'S F40: £1M (1990) → £543,375 (2014)")
sc("""Wikipedia adds a detail about use. By a nineteen ninety estimate, only about ten percent of owners drove their cars regularly. That is the other half of the bubble story: cars bought to be kept, not driven. Lee Iacocca's car, according to Autopian, covered sixty-five miles between two thousand six and twenty twelve, which is about eleven miles a year, by our arithmetic.""",
   "Lee Iacocca", "~10% OF OWNERS DROVE THEIR CARS (1990 EST.) · IACOCCA'S CAR: 65 MILES IN 6 YEARS")

ch("The racing afterlife")
sc("""The car that was born from a cancelled racing category did get to race. Wikipedia says the F forty L M debuted at Laguna Seca on the fifteenth of October, nineteen eighty-nine, and finished third. Ten Competizione-specification cars were built, two L M and eight Competizione, with seven hundred horsepower. The G T E, with six hundred twenty horsepower, followed.""",
   "Laguna Seca", "F40 LM DEBUT: LAGUNA SECA, OCT 15, 1989 · 3RD · 10 COMPETIZIONE-SPEC CARS")
sc("""Seven G T E cars were built, Wikipedia says, and they won the four hours of Anderstorp in nineteen ninety-five and nineteen ninety-six. In all, nineteen racing cars were built. By our arithmetic, that is about one and a half percent of the production. A road car designed for a category that vanished eventually found racing elsewhere.""",
   "Anderstorp", "GTE: 7 BUILT · ANDERSTORP WINS 1995, 1996 · 19 RACING CARS IN ALL")
sc("""The most valuable of them, per Sotheby's, is a nineteen ninety-three F forty L M by Michelotto. It sold for eleven million, five thousand dollars in August twenty twenty-five, and it has about seven hundred sixty horsepower. Sotheby's says it is one of nineteen Michelotto examples. The racing version, which Enzo never saw, now sets the price record in our sources.""",
   "Ferrari F40 LM", "2025: 1993 F40 LM BY MICHELOTTO SOLD FOR $11,005,000")

ch("From bubble to blue chip")
sc("""Classic Motorsports tracks the price after the bubble. About one million dollars in twenty nineteen. A Mecum sale at two and a half million in twenty twenty-two. Around four million in twenty twenty-three, it says. By our arithmetic, that is a fourfold rise in four years. The car that once lost nearly half its value in pounds had become a blue-chip collectible.""",
   "Ferrari F40 value", "~$1M (2019) → $2.5M (2022) → ~$4M (2023)")
sc("""Sotheby's lists the sales of twenty twenty-five. Alain Prost's nineteen ninety car, three million, eight hundred eighty-six thousand, two hundred fifty dollars, with two thousand, nine hundred sixty-one miles. A nineteen ninety storage car, three million, eight hundred fifty-five thousand dollars, with three hundred sixty kilometres. A U S-specification car, three million, five hundred eighty thousand dollars.""",
   "Alain Prost", "2025: PROST'S CAR $3.89M · STORAGE CAR $3.86M · US-SPEC $3.58M")
sc("""A Swiss car sold for two million, nine hundred fifty-eight thousand, one hundred twenty-five francs, and a restored car for two million, eight hundred seventeen thousand, five hundred euros. Autopian reports a nineteen ninety-two car at five million, two hundred thirty thousand dollars in February twenty twenty-six. These are separate sales, not an index, and the range is wide.""",
   "Ferrari F40 auction", "CHF 2,958,125 · €2,817,500 · $5,230,000 (FEB 2026)")
sc("""By our arithmetic, the Prost sale is about nine and three-quarter times the launch price of four hundred thousand dollars, in nominal terms. The ModaMiami sale is about thirteen times. Those multiples are not adjusted for inflation, because our sources give no inflation figure, and the comparison is rough. Still, the direction is unmistakable.""",
   "Ferrari F40", "PROST ≈ 9.7× LAUNCH PRICE · MODAMIAMI ≈ 13× (OUR ARITHMETIC, NOMINAL)")

ch("Living with the legend")
sc("""Owners do not just buy the story; they maintain it. Classic Motorsports says the belts are replaced every three years, with the engine in place but the seats and rear firewall removed. Fluids are changed yearly, for about one thousand dollars. Fuel bladders can leak after about ten years, though U S cars had aluminium tanks. It calls the car cheaper to run than the F fifty.""",
   "Ferrari F40 service", "BELTS EVERY 3 YEARS · FLUIDS YEARLY ~$1,000 · FUEL BLADDERS ~10 YEARS")
sc("""Autopian itemised a preparation bill for Lee Iacocca's nineteen ninety-one car, chassis eighty-seven three forty-five, before a Monterey sale in twenty twenty-six: a coolant tank at four thousand, four hundred twenty-six dollars, engine service of nearly twenty-one thousand, tyres at two thousand, six hundred thirty-seven and a headlamp switch at four thousand, two hundred. About thirty-four thousand dollars in all.""",
   "Lee Iacocca's Ferrari F40", "IACOCCA CAR PREP ~$34K ITEMISED (ARTICLE'S HEADLINE AND BODY DISAGREE)")
sc("""That article is inconsistent. Its headline says sixty thousand dollars and its body says forty thousand, while the items add up to about thirty-four thousand. We cannot resolve it, so we use the itemised figures. It is a good example of how a story about this car can be repeated with the wrong numbers, which is why we keep showing where ours come from.""",
   "Autopian", "$60K HEADLINE · $40K BODY · ~$34K ITEMISED")

ch("Five Evoluzione cars and a question")
sc("""Return for a moment to the Evoluzione. Five cars were built and never raced. Wikipedia does not say what happened to them afterwards, and neither do our other sources, so we will not guess. What we can say is that the project to turn that experiment into a road car started on the tenth of June, nineteen eighty-six, and ended with an unveiling in Maranello.""",
   "Ferrari 288 GTO Evoluzione", "FIVE CARS BUILT FOR A CATEGORY THAT DISAPPEARED")
sc("""It is worth pausing on how short thirteen months is. By our arithmetic, that is about three hundred ninety days between the start of the project and the unveiling. Compare the Porsche, which Wikipedia says took from nineteen eighty-one to deliveries in nineteen eighty-seven, about six years by our arithmetic. The Ferrari took roughly one sixth of the time.""",
   "Ferrari F40 development", "13 MONTHS (~390 DAYS) VS ~6 YEARS FOR THE 959 (OUR ARITHMETIC)")
sc("""The reason, by our reading, is that the Ferrari had a head start. The Evoluzione existed, and so did the engine family. Our sources do not say which parts carried over, so we do not list them. They say only that the F forty grew out of the Evoluzione and that the project took thirteen months. The rest is inference, and we label it that way.""",
   "Ferrari engine", "A HEAD START FROM THE EVOLUZIONE (OUR READING)")

ch("The numbers that never added up")
sc("""The F forty is a car of disputed numbers, and the dispute is part of its story. Wikipedia lists its weight at one thousand, two hundred fifty-four kilograms for Europe and one thousand, three hundred sixty-nine for the United States. The DK Engineering archive says one thousand, two hundred two. By our arithmetic, the gap between the lowest and highest figure is one hundred sixty-seven kilograms, about thirteen and a half percent.""",
   "Ferrari F40 weight", "F40 WEIGHT: 1,202 KG (DK) · 1,254 KG (EU) · 1,369 KG (US) (WIKIPEDIA)")
sc("""The power figures differ as well. Wikipedia says four hundred seventy-eight metric horsepower, and four hundred eighty-four for the U S. The DK Engineering archive says about five hundred brake horsepower at one point one bar of boost. Our sources do not reconcile these, so we report them all. In a car this famous, even the basic specification depends on which source you open.""",
   "Ferrari F40 engine", "478 PS (EU) · 484 PS (US) · ~500 BHP AT 1.1 BAR (DK)")
sc("""The emissions equipment differs too. Wikipedia says the early cars had no catalytic converters until nineteen ninety. The DK Engineering archive says they arrived from nineteen ninety-one. One year apart, but a collector will tell you the difference matters. We do not know which is right, and we do not pretend to. We note it, and move on.""",
   "Ferrari F40 exhaust", "CATALYTIC CONVERTERS: 1990 (WIKIPEDIA) OR 1991 (DK ENGINEERING)")

ch("The people around the car")
sc("""Behind the car were several people. Nicola Materazzi, who proposed it. Pietro Camardella and Aldo Brovarone, who shaped the body for Pininfarina. Enzo Ferrari, who approved it. Our sources give no more detail about their roles, so we do not add any. A common mistake in retellings is to credit one person with everything. The sources point to a team.""",
   "Pininfarina", "MATERAZZI · CAMARDELLA · BROVARONE · ENZO FERRARI (WIKIPEDIA)")
sc("""Then there were the drivers and owners who gave the car its famous names. Alain Prost, whose nineteen ninety car sold in December twenty twenty-five. Nigel Mansell, whose car was sold in nineteen ninety and again in twenty fourteen. Lee Iacocca, whose nineteen ninety-one car was ordered in Modena. Our sources do not say how they drove the cars, only how the cars were sold.""",
   "Alain Prost", "PROST · MANSELL · IACOCCA: THREE FAMOUS OWNERS IN OUR SOURCES")
sc("""And the Sultan of Brunei, who according to Wikipedia received at least seven right-hand-drive cars. Beyond that, the page says nothing about what he did with them. In a story with so many famous names, the sources only support a handful of facts about each, and we have tried to stay inside them. Good stories attract embellishment; we would rather give you less and have it be right.""",
   "Sultan of Brunei", "AT LEAST 7 RIGHT-HAND-DRIVE CARS (WIKIPEDIA)")

ch("What the F40 left behind")
sc("""Wikipedia lists the F forty as the last Ferrari approved by Enzo Ferrari and the car that, by many accounts, set the template for the supercars that followed. The sources we read do not make that second claim in so many words, so we call it our reading: a stripped-down, turbocharged, rear-wheel-drive car with a manual gearbox, built to celebrate an anniversary.""",
   "Ferrari F40", "THE LAST FERRARI ENZO APPROVED (WIKIPEDIA) · THE TEMPLATE CLAIM IS OUR READING")
sc("""Classic Motorsports calls it very durable, and cheaper to run than the F fifty. Sotheby's treats it as the subject of a six-car list of record sales. The DK Engineering archive describes the car as it was sold in the nineteen nineties. Each source gives a different slice of the same life, from showroom to dealer to auction to garage.""",
   "Ferrari F40", "FIVE SOURCES, FIVE SLICES OF THE SAME CAR")
sc("""The numbers, one last time, with our arithmetic. Thirteen months of development. Four hundred planned, one thousand, three hundred eleven built. About four hundred thousand dollars new. A bubble at seven times that. A forty-six percent nominal drop for Mansell's car. And, in twenty twenty-five and twenty twenty-six, sales between roughly two point eight and five point two million dollars for standard road cars.""",
   "Ferrari F40", "13 MONTHS · 400 PLANNED · 1,311 BUILT · $400K NEW · $2.8M–$5.2M TODAY")
sc("""We should say what we cannot tell you. We do not have a source for what Enzo Ferrari thought of the finished car, how many of the one thousand, three hundred eleven survive, or how many miles most of them have covered. Where the sources are silent, we stay silent. If you know a published figure we missed, put it in the comments with the source.""",
   "Ferrari F40", "WHAT OUR SOURCES DO NOT TELL US")
sc("""What would you have done with an F forty in nineteen eighty-seven, driven it or kept it in a garage? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the F forty, compare it with the Porsche nine fifty-nine, and work out what it really costs to own one. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video116", "The Insane Story Behind the Last Car Enzo Ferrari Approved", [
    "Wikipedia, Ferrari F40: https://en.wikipedia.org/wiki/Ferrari_F40",
    "Wikipedia, Porsche 959: https://en.wikipedia.org/wiki/Porsche_959",
    "Classic Motorsports, Ferrari F40: the truth about living with a legend: https://classicmotorsports.com/articles/ferrari-f40-how-you-spend-million/",
    "Sotheby's, The six most expensive Ferrari F40s: https://www.sothebys.com/en/articles/the-six-most-expensive-ferrari-f40s",
    "DK Engineering, Ferrari F40 (1990) vehicle archive: https://www.dkeng.co.uk/Vehicle_Archive/797/ferrari_f40.html",
    "The Autopian, Lee Iacocca's Ferrari F40",
], "D")
