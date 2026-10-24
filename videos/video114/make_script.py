import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Two supercars from the same year, both born from the end of Group B racing. One has rear-wheel drive, a twin-turbo V eight and no radio. The other has all-wheel drive, an adjustable ride height and a flat six that Porsche built at a loss. One was made in over thirteen hundred copies. The other in fewer than three hundred. This is the real difference between the Ferrari F forty and the Porsche nine fifty-nine.""",
   "Ferrari F40 and Porsche 959", "FERRARI F40 VS PORSCHE 959")
sc("""Here is the twist. The Porsche was faster at Nardò, by eighteen kilometres per hour or more. It was also, on the sources we read, cheaper than it cost to build, by more than half. And the Ferrari, the simpler car, is the one that was built in larger numbers, and the one that people queued to buy. Let us go through the numbers, and where the sources disagree.""",
   "Supercars of 1987", "THE PORSCHE WAS FASTER · THE FERRARI SOLD MORE")
sc("""Every figure comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Ferrari F40 and Porsche 959", "EVERY NUMBER IS SOURCED")

ch("Two answers to the end of Group B")
sc("""Group B was a racing category that produced some of the wildest cars in rally history. Wikipedia says it was cancelled, and both cars were shaped by that. For Porsche, the page says Group B was cancelled a year before the nine fifty-nine was homologated, ending the company's participation. For Ferrari, the category ended before the nineteen eighty-six season, leaving five Evoluzione cars with nowhere to race.""",
   "Group B rally", "GROUP B ENDED BEFORE EITHER CAR COULD RACE IT")
sc("""The Porsche project came first. Wikipedia says development began in nineteen eighty-one under managing director Peter Schutz, with chief engineer Helmuth Bott leading the project, originally called Gruppe B. The Group B prototype was unveiled at the nineteen eighty-three Frankfurt Motor Show. The road version debuted at Frankfurt in nineteen eighty-five, as a nineteen eighty-six model.""",
   "Porsche 959 prototype", "PORSCHE: STARTED 1981 · SHOWN 1983 · ROAD CAR 1985")
sc("""Production was delayed by more than a year, the page says, and customer deliveries began in nineteen eighty-seven. By our arithmetic, that is about six years from the start of development to the first customer car. The Ferrari, by comparison, took thirteen months from the tenth of June, nineteen eighty-six to its unveiling on the twenty-first of July, nineteen eighty-seven.""",
   "Porsche 959 delivery", "959: ~6 YEARS TO FIRST CUSTOMER CAR · F40: 13 MONTHS")
sc("""So the two cars arrived in the same year, nineteen eighty-seven, by completely different routes. One was a six year engineering project, the other a thirteen month adaptation. That difference shows in almost everything that follows. The Porsche is a showcase of technology. The Ferrari is a distillation of an existing recipe. Neither claim is a criticism.""",
   "Ferrari F40 and Porsche 959", "SIX YEARS VS THIRTEEN MONTHS (OUR ARITHMETIC)")

ch("Round one: the engines")
sc("""The F forty's engine is the F one twenty A, a two thousand, nine hundred thirty-six cubic centimetre twin-turbocharged, intercooled ninety-degree V eight. Wikipedia lists four hundred seventy-eight metric horsepower at seven thousand r p m and five hundred seventy-seven newton-metres at four thousand. The U S version is listed at four hundred eighty-four.""",
   "Ferrari F40 engine", "F40: 2.9 L V8 · 478 PS · 577 NM")
sc("""The nine fifty-nine's engine is a two thousand, eight hundred forty-nine cubic centimetre twin-turbocharged flat six, with four valves per cylinder. Wikipedia lists four hundred fifty metric horsepower at six thousand five hundred r p m and five hundred newton-metres at five thousand. It also lists the same rating as four hundred forty-four horsepower. The sequential turbos gave smoother power than Porsche's other turbo engines of the era.""",
   "Porsche 959 engine", "959: 2.85 L FLAT-SIX · 450 PS · 500 NM · SEQUENTIAL TURBOS")
sc("""By our own arithmetic, the Ferrari makes about six percent more power, four seventy-eight against four fifty, and about fifteen percent more torque, five seventy-seven against five hundred. It does so with a larger displacement, about three percent more, and reaches its torque peak at four thousand r p m, a thousand lower than the Porsche. On paper, the F forty is the stronger engine.""",
   "Engine comparison", "F40: +6% POWER · +15% TORQUE (OUR ARITHMETIC)")
sc("""Per litre, the Ferrari makes about one hundred sixty-three horsepower and the Porsche about one hundred fifty-eight, by our arithmetic. The two are close. Both used turbochargers to get more than a normally aspirated engine of the same size could. The Porsche's sequential system used two turbos in sequence for smoother delivery. The Ferrari used two turbos in parallel, as the archive describes, for brute force.""",
   "Turbocharged engines", "F40 ~163 PS/L · 959 ~158 PS/L (OUR ARITHMETIC)")
sc("""Porsche offered more. Wikipedia says an optional upgrade raised the power to five hundred thirty metric horsepower. A claimed top speed of three hundred thirty-six kilometres per hour, and zero to a hundred in three point four seconds, according to Paul Frère. And the nine fifty-nine S, with five hundred fifteen horsepower, of which twenty-nine were built, reached three hundred thirty-nine at Nardò in nineteen eighty-eight.""",
   "Porsche 959 S", "959 OPTION: 530 PS · 959 S: 515 PS, 29 BUILT, 339 KM/H")

ch("Round two: drivetrain and technology")
sc("""Here is the biggest difference. The F forty is rear-wheel drive with a five-speed manual, Wikipedia says. The nine fifty-nine has Porsche-Steuer Kupplung all-wheel drive, the P S K system, which can send up to eighty percent of the power to the rear under hard acceleration. Its six-speed manual has a first gear labelled gelände, German for terrain.""",
   "Porsche 959 drivetrain", "F40: RWD, 5-SPEED · 959: ALL-WHEEL DRIVE, 6-SPEED")
sc("""The nine fifty-nine also has adjustable ride height as standard on the road car, Wikipedia says. The F forty did not, until, according to the archive, adjustable suspension became an option from nineteen ninety-one. And Sotheby's describes a U S-spec F forty as having non-adjustable suspension. So the Porsche was a technology showcase that the Ferrari did not try to be.""",
   "Porsche 959 suspension", "959: ADJUSTABLE RIDE HEIGHT STANDARD · F40: OPTIONAL FROM 1991")
sc("""Look at what the F forty did not have. No door handles, no glove box, no leather, no carpets, no door panels, no sound system, according to Wikipedia. And according to Classic Motorsports, no A B S. The nine fifty-nine, by contrast, is a car in which Porsche put its latest ideas, though our sources do not list its comfort features. Porsche later built eight Komfort cars, which suggests that comfort was an issue.""",
   "Ferrari F40 interior", "F40: NO HANDLES, NO LEATHER, NO ABS · 959: LATEST TECHNOLOGY")
sc("""Wikipedia says that in nineteen ninety-two and ninety-three, eight more Komfort cars were assembled from spare parts, at seven hundred forty-seven thousand, five hundred Deutsche Marks each. Car and Driver, the page says, measured zero to sixty miles per hour in three point six seconds in Komfort trim. A Komfort version existed from the start, which means the nine fifty-nine was available with more comforts than the Ferrari ever offered.""",
   "Porsche 959 Komfort", "8 KOMFORT CARS ASSEMBLED 1992/93 AT DM 747,500 EACH")

ch("Round three: weight and speed")
sc("""Weight. Wikipedia lists the F forty at one thousand, two hundred fifty-four kilograms for Europe and one thousand, three hundred sixty-nine for the United States. The nine fifty-nine is listed at one thousand, four hundred fifty. By our arithmetic, the Ferrari is a hundred ninety-six kilograms, or about thirteen and a half percent, lighter in its European form, and eighty-one kilograms, or about five and a half percent, lighter in its U S form.""",
   "Ferrari F40 weight", "F40 196 KG LIGHTER (EU) OR 81 KG (US) THAN THE 959 (OUR ARITHMETIC)")
sc("""Power to weight, ours. The F forty at four hundred seventy-eight horsepower and one thousand, two hundred fifty-four kilograms is about point three eight horsepower per kilogram. The Porsche at four hundred fifty over one thousand, four hundred fifty is about point three one. The F forty has about twenty-three percent better power to weight, in European form. The Porsche's all-wheel drive adds traction, but it adds weight too.""",
   "Power to weight", "F40 0.38 PS/KG · 959 0.31 PS/KG (OUR ARITHMETIC)")
sc("""Acceleration. The earliest independent test of the F forty, Wikipedia says, was zero to a hundred kilometres per hour in four point seven seconds. The page lists the nine fifty-nine at three point four seconds, per Paul Frère on the five hundred thirty horsepower car, and three point seven in an Auto Motor und Sport test of the same car. Car and Driver's three point six was zero to sixty miles per hour.""",
   "Porsche 959 launch", "0–100 KM/H: F40 4.7 S · 959 (530 PS) 3.4–3.7 S")
sc("""The comparison is not like for like, since the Porsche figures are for the more powerful car. But the direction is clear: the nine fifty-nine's all-wheel drive let it launch much harder. By our arithmetic, the best nine fifty-nine figure, three point four, is about twenty-eight percent quicker to a hundred than the F forty's four point seven. That is the P S K system at work.""",
   "Porsche 959 acceleration", "959 ≈ 28% QUICKER TO 100 THAN THE F40 (OUR ARITHMETIC)")
sc("""Top speed. Wikipedia lists the F forty at three hundred twenty-one kilometres per hour in the earliest test, with Road and Track at three hundred fifteen and Car and Driver at three hundred seventeen. The Porsche is listed at three hundred seventeen at launch, three hundred eighteen in an Auto Motor und Sport test, and up to three hundred thirty-nine for the S. Classic Motorsports gives two hundred two miles per hour against one ninety-seven.""",
   "Nardò test track", "TOP SPEED: F40 315–321 KM/H · 959 317–339 KM/H")
sc("""The Nardò comparison is the cleanest. Wikipedia says Ferrari's two cars could not exceed three hundred twenty-one kilometres per hour at Nardò, while the nine fifty-nine S reached three hundred thirty-nine. By our arithmetic, that is a difference of eighteen kilometres per hour, about five and a half percent. The page adds that the Ruf C T R reached three hundred forty-two.""",
   "Nardò Ring", "NARDÒ: F40 321 · 959 S 339 · RUF CTR 342 KM/H")
sc("""Note the caveat. The nine fifty-nine S was a limited version, twenty-nine built, with five hundred fifteen horsepower, and not the standard car. The standard nine fifty-nine, with four hundred fifty, is listed at three hundred seventeen to three hundred eighteen, which is about the same as the F forty's three hundred fifteen to three hundred twenty-one. So the standard cars are evenly matched in top speed.""",
   "Porsche 959 S", "STANDARD CARS ARE EVENLY MATCHED ON TOP SPEED")

ch("Round four: price and what it cost to make")
sc("""Price. Wikipedia says the F forty's launch price was about four hundred thousand dollars. The nine fifty-nine's launch price was four hundred thirty-one thousand, five hundred fifty Deutsche Marks, which the page converts to about two hundred twenty-five thousand dollars. By our arithmetic, the Ferrari cost about seventy-eight percent more than the Porsche in dollar terms, at launch.""",
   "Ferrari F40 and Porsche 959 price", "F40 ≈ $400,000 · 959 ≈ $225,000 (DM 431,550)")
sc("""But that is not the whole story. The page says the nine fifty-nine's price was less than half of Porsche's build cost for each car. By our arithmetic, that means each car cost Porsche more than four hundred fifty thousand dollars to make, since two hundred twenty-five thousand is less than half of it. The Ferrari's price was higher than the Porsche's, and so, probably, was its profit.""",
   "Porsche factory", "959 PRICE < HALF OF BUILD COST → BUILD COST > $450K (OUR ARITHMETIC)")
sc("""Wikipedia adds that Porsche lost about two hundred thousand dollars per car on U S sales because of the unfavourable exchange rate. We should be careful: the page gives the loss on U S sales, not on all sales. And it does not say how many of the two hundred ninety-two cars were sold in the United States, so we cannot compute a total. We only note that the car was a money-loser by design.""",
   "Porsche 959 exchange rate", "US SALES: ~$200,000 LOSS PER CAR (EXCHANGE RATE)")
sc("""For Ferrari, the sources give no cost per car. Wikipedia says the F forty's launch price was roughly five times that of the two eighty-eight G T O. Classic Motorsports says the F forty cost about one million dollars in September twenty nineteen, when its article first ran. So the market rose enormously, from four hundred thousand to a million in about thirty years, before rising further.""",
   "Ferrari F40 price history", "F40: ~$400K (1987) → ~$1M (2019, CLASSIC MOTORSPORTS)")

ch("Round five: production and rarity")
sc("""Production. Wikipedia lists the Ferrari at one thousand, three hundred eleven, with some sources saying up to one thousand, three hundred fifteen, from a plan of four hundred. The Porsche, according to the page, ended production in nineteen eighty-eight with two hundred ninety-two cars, or three hundred thirty-seven including thirty-seven prototypes and pre-production cars.""",
   "Ferrari and Porsche production", "F40: 1,311 · 959: 292 (337 WITH PROTOTYPES)")
sc("""By our arithmetic, the Ferrari was built in about four and a half times the number of the Porsche, one thousand, three hundred eleven over two hundred ninety-two. The nine fifty-nine S adds twenty-nine, and eight Komfort cars were assembled later. So the Porsche is the rarer car, by a wide margin, though neither is a common sight.""",
   "Porsche 959 rarity", "F40 ≈ 4.5× MORE NUMEROUS THAN THE 959 (OUR ARITHMETIC)")
sc("""There is a link to demand. Wikipedia says speculators sold F forty cars for up to more than seven times list price in nineteen eighty-nine. For the Porsche, the page gives no similar figure. Our sources do not tell us whether speculators bought nine fifty-nines at similar premiums. So we leave the question there, and note that rarity alone does not decide the price.""",
   "Car speculators", "F40 SPECULATORS: UP TO 7× LIST · 959: NO FIGURE IN OUR SOURCES")

ch("Round six: racing")
sc("""Racing is where the Porsche's story is stronger. Wikipedia says development cars, nine fifty-three, finished first, sixth and twenty-fifth in the nineteen eighty-four Paris-Dakar. In nineteen eighty-six the nine fifty-nine finished first with René Metge, second with Jacky Ickx and sixth. A nine fifty-nine also won the nineteen eighty-five Rallye des Pharaons. In nineteen eighty-six at Le Mans, the nine sixty-one finished first in its class and seventh overall.""",
   "Porsche Paris-Dakar", "PARIS-DAKAR 1986: 959 FIRST (METGE), SECOND (ICKX)")
sc("""The Ferrari raced later and on tracks. Wikipedia says the F forty L M debuted at Laguna Seca on the fifteenth of October, nineteen eighty-nine, and finished third overall. The G T E won the four hours of Anderstorp in nineteen ninety-five and ninety-six. Nineteen racing cars were built in all. The Porsche proved itself in rallies and endurance races. The Ferrari proved itself in sports car racing.""",
   "Ferrari F40 racing", "F40 LM: 3RD AT LAGUNA SECA 1989 · GTE WINS 1995, 1996")
sc("""Neither car raced in Group B itself. The category ended before they could. So the cars exist as results of a competition that never fully happened. By our reading, that makes them two of the last cars of an era. The sources do not say this directly, so it is our reading, but the dates are consistent with it.""",
   "Group B legacy", "NEITHER RACED IN GROUP B ITSELF (OUR READING)")

ch("Round seven: can you drive it in America?")
sc("""A real-world difference concerns the United States. Wikipedia says two hundred thirteen F forty cars were destined for the U S, and Sotheby's describes a U S-spec car as one of two hundred thirteen allocated for North America. The nine fifty-nine, by contrast, could not be federalised after the nineteen eighty-eight Imported Vehicle Safety Compliance Act, because Porsche tested it only to European standards.""",
   "US customs", "F40: 213 US CARS · 959: COULD NOT BE FEDERALISED AFTER 1988")
sc("""Bill Gates bought a nine fifty-nine in nineteen eighty-eight, the page says, and customs stored it for thirteen years before the Show or Display law took effect on the thirteenth of August, nineteen ninety-nine. That law allowed limited use of two thousand, five hundred road miles a year. The page adds that cars over twenty-five years old are no longer subject to these restrictions.""",
   "Porsche 959 in the US", "13 YEARS IN CUSTOMS · SHOW OR DISPLAY: 2,500 MILES A YEAR")
sc("""The page also says that the claim that Porsche skipped U S crash tests is a myth, because the D O T does not conduct crash tests itself. It is the sort of detail that disappears in retellings. By our reading, the Ferrari's U S allocation made it the easier car to own in America, even in nineteen eighty-seven. The Porsche had to wait.""",
   "Porsche 959", "THE 'SKIPPED CRASH TESTS' CLAIM IS CALLED A MYTH (WIKIPEDIA)")

ch("The verdict")
sc("""So, which car wins? On power and torque, the Ferrari. On weight and power to weight, the Ferrari. On acceleration, the Porsche. On top speed, the standard cars are equal, and the Porsche S is faster. On technology, the Porsche. On price and what it cost to make, the Ferrari earned more, and the Porsche lost money. On rarity, the Porsche. On racing, the Porsche in rallies, the Ferrari on tracks.""",
   "Ferrari F40 and Porsche 959", "SCORECARD")
sc("""The real difference is the philosophy. Porsche used the project to show what technology could do, regardless of cost. Ferrari made the simplest, fastest car it could, with what it had. Both are legends. One lost money and gave its makers technology they could use later. The other made money and gave its makers a reputation. Both cars are remembered, and neither is better in every way.""",
   "Ferrari F40 and Porsche 959", "TECHNOLOGY SHOWCASE VS DISTILLED RECIPE (OUR READING)")
sc("""One caution. We have not driven either car. The Porsche's figures come from different versions, the Ferrari's weights differ by source, and some comparisons are our own arithmetic. We have tried to say so each time. If you have a verified detail, tell us in the comments, with where it comes from.""",
   "Ferrari F40 and Porsche 959", "NUMBERS, NOT A DRIVING VERDICT")
ch("Round eight: where the sources disagree")
sc("""Before the final verdict, a word about disagreements, because the F forty is full of them. Wikipedia lists its weight at one thousand, two hundred fifty-four kilograms for Europe. The DK Engineering archive lists one thousand, two hundred two. Our arithmetic says that is a fifty-two kilogram gap, about four percent, between two published figures for the same car. We use the Wikipedia numbers above, and flag the rest.""",
   "Ferrari F40 weight discrepancy", "F40 WEIGHT: 1,202 KG (DK) VS 1,254 KG (WIKIPEDIA)")
sc("""Boost pressure is another. The DK Engineering archive says the F forty made about five hundred brake horsepower at one point one bar of boost. Wikipedia's rating is four hundred seventy-eight metric horsepower. The sources do not explain the gap, and we do not guess. It may be a different rating method, a different version, or a rounded number. We simply report both figures as published.""",
   "Ferrari F40 boost", "F40 POWER: ~500 BHP AT 1.1 BAR (DK) VS 478 PS (WIKIPEDIA)")
sc("""Even the number of American cars is disputed. Wikipedia and Sotheby's say two hundred thirteen F forty cars were built for the United States. The DK Engineering archive says about six hundred of the thirteen hundred eleven went to the U S. Our arithmetic: two hundred thirteen is about sixteen percent of the total, six hundred is about forty-six percent. Those are very different pictures of the same market.""",
   "Ferrari F40 American market", "US CARS: 213 (WIKIPEDIA, SOTHEBY'S) VS ~600 (DK ENGINEERING)")
sc("""The unveiling date also differs. Wikipedia says the F forty was unveiled in Maranello on the twenty-first of July, nineteen eighty-seven. The DK Engineering archive says it was presented in June of that year. The archive adds that this was fourteen months before the death of Enzo Ferrari. Classic Motorsports says Enzo died in nineteen eighty-eight at the age of ninety. The sources agree on the year, not the month.""",
   "Maranello", "UNVEILING: JULY 21, 1987 (WIKIPEDIA) VS JUNE 1987 (DK ENGINEERING)")
sc("""There is also the claim that the F forty was the first production car to pass two hundred miles per hour. The DK Engineering archive gives two hundred one. Classic Motorsports gives two hundred two. But Wikipedia's measured figures are lower, three hundred fifteen to three hundred seventeen kilometres per hour in magazine tests, which is about one ninety-six to one ninety-seven miles per hour, by our arithmetic. So the famous number depends on whose test you trust.""",
   "Ferrari F40 top speed", "THE 200 MPH CLAIM VS MEASURED ~196–197 MPH (OUR ARITHMETIC)")
sc("""The Porsche has its own disagreements. Wikipedia gives its power as four hundred fifty metric horsepower, and also as four hundred forty-four horsepower, which is the same number in different units. It lists three hundred seventeen kilometres per hour at launch, three hundred eighteen in one test, and three hundred thirty-six with the optional upgrade. These are not contradictions. They are different cars and different tests.""",
   "Porsche 959 specifications", "959: 450 PS = 444 HP · 317 / 318 / 336 KM/H DEPENDING ON CAR AND TEST")
sc("""What does this teach us? That a comparison between two legends is built from sources that disagree, and that the honest way to present it is with the ranges. Where we say the Ferrari is lighter, we mean on the figures we used. Where we say the Porsche accelerates faster, we mean the best published figure. If a number matters to you, check the source, and tell us if we missed one.""",
   "Ferrari F40 and Porsche 959", "WHY WE SHOW RANGES, NOT SINGLE NUMBERS")

ch("A word on ownership")
sc("""Ownership is where the two cars part ways again. Classic Motorsports says the F forty's timing belts are replaced every three years, that the engine stays in the car, but the seats and the rear firewall come out. Fluids are changed yearly, for about one thousand dollars. Fuel bladders can leak after about ten years, though U S cars used aluminium tanks.""",
   "Ferrari F40 maintenance", "F40: BELTS EVERY 3 YEARS · FLUIDS YEARLY ~$1,000 (CLASSIC MOTORSPORTS)")
sc("""Classic Motorsports also calls the F forty cheaper to run than the F fifty, and very durable. For the nine fifty-nine, our sources have no maintenance figures at all, so we cannot compare running costs. We can only note that the Porsche's complexity, with its sequential turbos, all-wheel drive and adjustable suspension, means more systems to maintain than the Ferrari's simpler layout. That part is our reading, not a sourced fact.""",
   "Porsche 959 complexity", "959 MAINTENANCE COSTS: NOT IN OUR SOURCES · COMPLEXITY IS OUR READING")
sc("""Values today. Sotheby's lists the most expensive F forty sales of twenty twenty-five. A nineteen ninety-three F forty L M by Michelotto sold for eleven million, five thousand dollars in August. Alain Prost's nineteen ninety car sold for three million, eight hundred eighty-six thousand, two hundred fifty dollars in December. For the Porsche, our sources give no auction prices, so we leave that comparison out.""",
   "Ferrari F40 auction", "2025: F40 LM $11.0M · PROST'S F40 $3.89M (SOTHEBY'S)")

sc("""Which would you rather own, the Ferrari or the Porsche? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the F forty, work out what it really costs to own one, and tell the story of the last car Enzo Ferrari approved. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video114", "Ferrari F40 vs Porsche 959: The Difference Nobody Explains", [
    "Wikipedia, Ferrari F40: https://en.wikipedia.org/wiki/Ferrari_F40",
    "Wikipedia, Porsche 959: https://en.wikipedia.org/wiki/Porsche_959",
    "Classic Motorsports, Ferrari F40: the truth about living with a legend: https://classicmotorsports.com/articles/ferrari-f40-how-you-spend-million/",
    "Sotheby's, The six most expensive Ferrari F40s: https://www.sothebys.com/en/articles/the-six-most-expensive-ferrari-f40s",
    "DK Engineering, Ferrari F40 (1990) vehicle archive: https://www.dkeng.co.uk/Vehicle_Archive/797/ferrari_f40.html",
], "B")
