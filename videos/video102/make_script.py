import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Two hypercars, both limited to exactly two hundred seventy-five cars. One has a Formula One engine, a turbocharged V six with a hybrid system. The other has a naturally aspirated V twelve that Wikipedia says makes about a thousand horsepower on its own. One came from Mercedes, the other from Aston Martin and Red Bull. This is the real difference between the Mercedes-AMG One and the Aston Martin Valkyrie.""",
   "Mercedes-AMG One and Aston Martin Valkyrie", "AMG ONE VS ASTON MARTIN VALKYRIE")
sc("""Here is the twist. Both were built in the same number, two hundred seventy-five. Both were late. Both cost about the same order of money. Yet the two engines could hardly be more different, and the Valkyrie's own sources disagree about how much it weighs, by more than three hundred kilograms. We will go through the numbers, and say where they conflict.""",
   "Hypercars", "SAME NUMBER BUILT · VERY DIFFERENT ENGINES")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Hypercar", "EVERY NUMBER IS SOURCED")

ch("Two projects with one number in common")
sc("""The Mercedes-AMG One began as the Project One concept, shown in twenty seventeen, according to Wikipedia. It was developed in Affalterbach, Germany, unveiled in production form on the first of June twenty twenty-two, and first delivered on the sixteenth of January twenty twenty-three. Production was limited to two hundred seventy-five cars, all hand-built.""",
   "Mercedes-AMG One", "AMG ONE: 275 CARS · FIRST DELIVERY JAN 2023")
sc("""The Aston Martin Valkyrie was built by Aston Martin Lagonda with Red Bull Racing Advanced Technologies and other suppliers. It was codenamed Nebula, then A M R B zero zero one. Wikipedia credits the concept to Adrian Newey, Andy Palmer, Christian Horner and Simon Sproule. Newey was Red Bull's chief technical officer at the time and contributed directly to the design.""",
   "Aston Martin Valkyrie", "VALKYRIE: DESIGNED WITH ADRIAN NEWEY OF RED BULL")
sc("""The Valkyrie was first shown in July twenty sixteen as a non-working full-scale model, and the name was announced in March twenty seventeen. Production ran from November twenty twenty-one to December twenty twenty-four. The total was two hundred seventy-five: one hundred fifty coupés, eighty-five Spiders and forty track-only A M R Pro cars.""",
   "Aston Martin Valkyrie production", "VALKYRIE: 150 COUPÉS + 85 SPIDERS + 40 AMR PRO = 275")
sc("""By our own arithmetic, the Valkyrie's first show was a year before the AMG One concept, but its production ended in December twenty twenty-four. The AMG One's production, per Wikipedia, ran from August twenty twenty-two to twenty twenty-five. The two cars were being built at about the same time, and both were competing for the same small group of buyers.""",
   "Hypercar factory", "BUILT IN THE SAME ERA FOR THE SAME BUYERS")
sc("""Both cars sold out. Wikipedia says all two hundred seventy-five AMG One cars sold, with more than four times as many orders, and that Mercedes refused to raise the limit. For the Valkyrie, the page says Aston Martin stated that all production had been sold, and that the Spider was twice oversubscribed. Demand exceeded supply on both sides.""",
   "Hypercar customers", "BOTH SOLD OUT · BOTH OVERSUBSCRIBED")

ch("Round one: the engines")
sc("""The AMG One uses a one-point-six-litre turbocharged V six, the P U one oh six B, modified from the Mercedes Formula One engine. Wikipedia lists four hundred twenty-two kilowatts, or five hundred seventy-four metric horsepower, at a redline of eleven thousand r p m. It sits with a hybrid system of an M G U K and an M G U H.""",
   "Mercedes-AMG One engine", "AMG: 1.6 L TURBO V6 · 574 PS · 11,000 RPM")
sc("""The Valkyrie uses a six-point-five-litre naturally aspirated V twelve, tailored by Cosworth. Wikipedia lists about one thousand horsepower at ten thousand five hundred r p m, with a redline of eleven thousand one hundred. By our arithmetic, that is about one hundred fifty-four horsepower per litre, with no turbochargers at all.""",
   "Cosworth V12 engine", "VALKYRIE: 6.5 L V12 · ~1,000 HP · 11,100 RPM")
sc("""Compare engine only. The V twelve makes roughly one thousand horsepower, the V six five hundred sixty-six horsepower according to Wikipedia's mechanical figure. So the Valkyrie's combustion engine produces about seventy-six percent more, by our arithmetic. The AMG One's engine is smaller, turbocharged, and helped by a very large electric system to close the gap.""",
   "Engine comparison", "V12 MAKES ~76% MORE THAN THE V6 ALONE (OUR ARITHMETIC)")
sc("""The hybrid systems differ in scale. The AMG One has an M G U K of one hundred twenty kilowatts, an M G U H of ninety, and two front motors of one hundred twenty kilowatts each. The Valkyrie has an Integral Powertrain motor of about one hundred sixty horsepower and a one point three kilowatt-hour Rimac battery, in a K E R S style layout.""",
   "Hybrid systems", "AMG: 4 MOTORS · VALKYRIE: ONE MOTOR (~160 HP)")
sc("""The totals are close. Wikipedia lists the AMG One at one thousand sixty-three metric horsepower, or one thousand forty-nine horsepower. For the Valkyrie it lists a combined certified output of one thousand, one hundred sixty horsepower, which is one thousand, one hundred seventy-six metric horsepower. By our arithmetic, the Valkyrie has about eleven percent more power on paper.""",
   "Hypercar power", "AMG 1,063 PS · VALKYRIE 1,176 PS · +11% (OUR ARITHMETIC)")
sc("""Torque is listed for the Valkyrie only on our page, nine hundred newton-metres at six thousand r p m. The AMG One's torque is not listed in the sources we used, so we do not compare it. What we can say is that the Valkyrie reaches its peak at a high r p m, a trait of naturally aspirated engines, while a turbocharged engine usually peaks lower.""",
   "Engine dyno", "VALKYRIE TORQUE: 900 NM @ 6,000 RPM")
sc("""The gearboxes are similar. The AMG One has a seven-speed single-clutch automated manual with a carbon clutch. The Valkyrie has a seven-speed single-clutch automated manual supplied by Ricardo. Neither uses a conventional dual-clutch. Both chose a lighter, simpler, and more race-like design, and accepted what that means for smoothness at low speed.""",
   "Hypercar gearbox", "BOTH: 7-SPEED SINGLE-CLUTCH AUTOMATED MANUAL")

ch("Round two: weight and speed")
sc("""Now the discrepancy. Wikipedia's text for the Valkyrie cites one thousand and thirty kilograms at announcement, but its specification lists a kerb weight of one thousand, three hundred forty to one thousand, three hundred fifty-five. The two numbers conflict by more than three hundred kilograms, so we use the specification and flag the original claim as an announcement target.""",
   "Aston Martin Valkyrie weight", "VALKYRIE WEIGHT: 1,030 KG CLAIM VS 1,340–1,355 KG LISTED")
sc("""The AMG One weighs one thousand, six hundred ninety-five kilograms, with a listed range up to one thousand, seven hundred forty-five. By our arithmetic, that makes the Valkyrie about three hundred forty to three hundred fifty-five kilograms lighter, or about twenty percent lighter than the AMG One at its lowest figure.""",
   "Hypercar weights", "VALKYRIE ~20% LIGHTER (OUR ARITHMETIC)")
sc("""Power-to-weight tells the story. Taking one thousand, one hundred seventy-six metric horsepower over one thousand, three hundred forty-seven kilograms, the midpoint of the listed range, gives about point eight seven horsepower per kilogram. For the AMG One, one thousand sixty-three over one thousand, six hundred ninety-five gives about point six three. This is our arithmetic.""",
   "Power to weight", "VALKYRIE ~0.87 PS/KG · AMG ONE ~0.63 PS/KG (OUR ARITHMETIC)")
sc("""Acceleration is listed for both. The AMG One does zero to a hundred in two point nine seconds, zero to two hundred in seven point zero, and zero to three hundred in fifteen point six, with a top speed of three hundred fifty-two, limited. The Valkyrie is listed at two point six seconds to a hundred. The page gives no top speed for the road car.""",
   "Hypercar acceleration", "0–100: AMG 2.9 S · VALKYRIE 2.6 S")
sc("""The Valkyrie wins on paper by three tenths of a second to a hundred, about ten percent, by our arithmetic. But note that we have no matching figures from the Valkyrie page for two hundred or three hundred kilometres per hour, so we cannot compare the harder part of the run. That is where the AMG One's figures are most impressive.""",
   "Hypercar launch", "VALKYRIE QUICKER TO 100 · NO MATCHING DATA ABOVE")
sc("""Downforce is listed for the Valkyrie at up to eighteen kilonewtons, which is eighteen hundred kilogram-force, at high speed. For the AMG One, Wikipedia says Race Plus and Strat Two raise total downforce by up to five times, but gives no kilonewton figure. So again, we can describe the approach, but we cannot compare the numbers.""",
   "Hypercar aerodynamics", "VALKYRIE DOWNFORCE: UP TO 18 KN")

ch("Round three: the track")
sc("""The AMG One has a published Nürburgring record. Wikipedia says six minutes, thirty-five point one eight three in November twenty twenty-two, and six minutes, twenty-nine point zero nine in September twenty twenty-four, the first sub six-thirty lap by a road-legal production car. It also lists records at Hockenheim, the Red Bull Ring and Monza.""",
   "Nürburgring Nordschleife", "AMG ONE: 6:29.09 NÜRBURGRING (2024)")
sc("""The Valkyrie's page, as we read it, lists no matching lap record. It does describe the track-only A M R Pro, which was introduced at the twenty eighteen Geneva motor show. The Pro uses the V twelve without the hybrid system, a modified engine rated at eleven hundred horsepower or more, and has a target top speed of four hundred two kilometres per hour.""",
   "Aston Martin Valkyrie AMR Pro", "VALKYRIE AMR PRO: 1,100+ HP · TARGET 402 KM/H")
sc("""The Pro was originally planned for twenty-five cars, all sold, and later raised to forty. The page also says it targets three point three G of lateral grip and three point five G under braking. Those are targets, not measured results. We report them as targets. And it was driven for two laps at the twenty twenty-two Bahrain Grand Prix.""",
   "Aston Martin Valkyrie AMR Pro", "AMR PRO: 3.3 G LATERAL · 3.5 G BRAKING (TARGETS)")
sc("""The Valkyrie has also gone racing. The page lists a race version, the Valkyrie A M R L M H, with the hybrid system removed, which made its racing debut at the twenty twenty-five Qatar eighteen twelve kilometres. Remember that Mercedes' Tobias Moers told Top Gear he did not want to race the AMG One at Le Mans. The two companies made opposite decisions.""",
   "Le Mans prototype", "VALKYRIE RACED · AMG ONE DID NOT (PER TOP GEAR)")

ch("Round four: price and running costs")
sc("""Money next. Wikipedia lists the AMG One at two point seven two million dollars. CarAdvice gives two point two seven million euros. For the Valkyrie, Autonews reports two point four million pounds, or three point two million dollars, and Fortune says at least three million dollars. By our arithmetic, the Valkyrie is the more expensive, by about half a million dollars.""",
   "Hypercar prices", "AMG ONE ~$2.7M · VALKYRIE ~$3.0–3.2M")
sc("""Running costs are where Fortune, citing Bloomberg, gives a figure. It says servicing the Valkyrie could cost close to four hundred fifty thousand dollars over three years, with a slightly cheaper plan at three hundred forty thousand, from a customer email Bloomberg saw. Owners who service elsewhere risk voiding their warranties.""",
   "Aston Martin Valkyrie service", "VALKYRIE SERVICE: ~$450K OVER 3 YEARS (BLOOMBERG)")
sc("""By our own arithmetic, four hundred fifty thousand over three years is one hundred fifty thousand dollars a year. Fortune adds that a Bugatti Chiron costs around one hundred seventy thousand dollars to service over four years. So the Valkyrie's plan is about three and a half times the Chiron's yearly cost, by our arithmetic. An Aston Martin spokesman said the car needs motor-sport engineers.""",
   "Hypercar service costs", "$150K A YEAR VS ~$42.5K FOR A CHIRON (OUR ARITHMETIC)")
sc("""For the AMG One, our sources give no servicing price. They say only that the engine lasts about fifty thousand kilometres before owners must return the car for refurbishment. So we cannot compare the two on running costs. We can only say that both cars come with obligations that are closer to those of a racing team than those of an ordinary owner.""",
   "Hypercar maintenance", "AMG ONE: NO PUBLISHED SERVICE PRICE FOUND")

ch("Round five: delays")
sc("""Both were late. The AMG One was originally due in early twenty nineteen, according to Autocar, and was first delivered in January twenty twenty-three. By our arithmetic, almost four years. For the Valkyrie, Wikipedia says ten cars were delivered in the fourth quarter of twenty twenty-one, fewer than planned, which made Aston Martin miss its profit target.""",
   "Delayed hypercars", "AMG ONE: ~4 YEARS LATE · VALKYRIE: FEWER DELIVERIES THAN PLANNED")
sc("""The reasons differ. For the AMG One, the sources point to emissions certification, noise rules and low-r p m airflow at about twelve hundred r p m. For the Valkyrie, Autonews cites unnamed sources saying electronics problems delayed the launch, and Fortune repeats that the launch was delayed repeatedly while the company fixed electronics issues. Neither source gives details.""",
   "Hypercar engineers", "AMG: ENGINE · VALKYRIE: ELECTRONICS (UNNAMED SOURCES)")
sc("""Aston Martin's finances matter too. Fortune says the company had a debt pile of about one point four billion dollars in February twenty twenty-four, and that Lawrence Stroll rescued it in twenty twenty. Bloomberg Intelligence, it says, estimated in twenty twenty-one that one Valkyrie sale contributes the same earnings as twenty-one Vantage V eight cars.""",
   "Aston Martin factory", "ONE VALKYRIE = 21 VANTAGES IN EARNINGS (BLOOMBERG INTELLIGENCE EST.)")
sc("""So for Aston Martin, the Valkyrie was not just a halo car. It was important to its turnaround. For Mercedes, the AMG One was a showcase of what its hybrid technology could do. Different companies, different needs, but the same result, a hypercar delivered later than first promised and sold to buyers who waited.""",
   "Hypercar", "A TURNAROUND CAR VS A SHOWCASE CAR (OUR READING)")

ch("Round six: the open-top and the track toys")
sc("""The Valkyrie also comes in other forms. The Spider was announced in August twenty twenty-one for the twenty twenty-three model year, with a removable carbon fibre roof, and eighty-five were planned. Butterfly doors replace the coupé's gullwing doors. Wikipedia notes the Spider was twice oversubscribed. A later track-only Valkyrie L M was announced in June twenty twenty-five, limited to ten.""",
   "Aston Martin Valkyrie Spider", "VALKYRIE SPIDER: 85 · VALKYRIE LM: 10")
sc("""The AMG One, by comparison, has a single body style in our sources. A carbon fibre mid-engine coupé with butterfly doors, active front diffuser flaps, a two-part extendable rear wing and adjustable front louvres. It is a simpler range, with all two hundred seventy-five cars the same basic car, apart from what each owner specified.""",
   "Mercedes-AMG One", "ONE BODY STYLE · 275 OF THE SAME CAR")
sc("""There is one more difference in character. The Valkyrie's V twelve is naturally aspirated, and Wikipedia says the Valkyrie's Le Mans hypercar project was cancelled in February twenty twenty and revived in twenty twenty-three. The AMG One is a turbocharged hybrid. One is the end of an era of large engines, the other a preview of what racing engines became.""",
   "Hypercar engines", "V12 ENDS AN ERA · HYBRID V6 PREVIEWS ONE (OUR READING)")

ch("Round seven: the people and the testing")
sc("""Both cars have famous names attached. The Valkyrie's first shakedown at Silverstone, Wikipedia says, involved Max Verstappen and Alexander Albon, two Red Bull Formula One drivers. The AMG One was unveiled in twenty seventeen by Lewis Hamilton and Dieter Zetsche. In both cases, the companies wanted the car's link to Formula One to be visible from the start.""",
   "Formula One drivers", "VALKYRIE: VERSTAPPEN + ALBON · AMG ONE: HAMILTON + ZETSCHE")
sc("""On the AMG One's side, Maro Engel drove the Nürburgring record lap in November twenty twenty-two, according to Wikipedia. The page also lists Gorden Wagener as head of design and Hartmut Sinkwitz for the interior. On the Valkyrie's side, Aston Martin under Miles Nurnberger oversaw much of the exterior design, while Red Bull Advanced Technologies handled the aerodynamic profile.""",
   "Car designers", "DESIGN: WAGENER (AMG) · NURNBERGER + RED BULL (ASTON)")
sc("""The Valkyrie's story is also a story of an engineer. Wikipedia says Adrian Newey was Red Bull Racing's chief technical officer and contributed directly to the design. The page lists him with Andy Palmer, Christian Horner and Simon Sproule as one of the people who conceived the car. It is unusual for a Formula One designer to put his name to a road car.""",
   "Adrian Newey", "ADRIAN NEWEY: RED BULL'S CHIEF TECHNICAL OFFICER")
sc("""The AMG One, by contrast, is credited to the company's engineering team in Affalterbach. Ola Källenius, according to Wikipedia, said the engine and design were based on the Formula One W oh six, while Autocar says the engine was adapted from the twenty seventeen championship car. We reported that disagreement earlier, and it remains unresolved in the sources we have.""",
   "Mercedes-AMG engineers", "SOURCES DISAGREE ON WHICH F1 CAR")

ch("Round eight: the electric side")
sc("""One feature is worth a closer look: the electric range. Wikipedia lists the AMG One's battery as an eight hundred volt lithium-ion pack, with an electric range of eighteen point one kilometres. For the Valkyrie, the page lists only a one point three kilowatt-hour battery from Rimac, and no electric range. By our arithmetic, that battery is a small fraction of a normal plug-in car's.""",
   "Hybrid battery", "AMG ONE: 18.1 KM ELECTRIC · VALKYRIE: 1.3 KWH, NO RANGE LISTED")
sc("""This shows the different jobs of the hybrid systems. The Valkyrie's is described as K E R S style, a boost of power. The AMG One's can propel the car on electricity for a short distance, and its front motors give it all-wheel drive. One hybrid is a booster. The other is closer to a second powertrain.""",
   "Hybrid hypercar", "BOOSTER VS SECOND POWERTRAIN (OUR READING)")
sc("""The weight of the AMG One's system is part of why it is the heavier car, though the sources do not say so directly. By our reading, it is a natural consequence of carrying a battery, four motors, and an all-wheel-drive system. The Valkyrie spends its mass budget on the engine and the carbon structure, and keeps electrical equipment small.""",
   "Hypercar", "WHERE EACH CAR SPENDS ITS WEIGHT (OUR READING)")

ch("Round nine: how many, and how they were shared out")
sc("""Both firms limited supply, but in different ways. Mercedes limited the AMG One to two hundred seventy-five and turned down orders far beyond that. Aston Martin split its two hundred seventy-five between three models, one hundred fifty coupés, eighty-five Spiders and forty A M R Pros. By our arithmetic, coupés are fifty-five percent of the total, Spiders thirty-one percent, and the Pros fifteen percent.""",
   "Hypercar production", "55% COUPÉ · 31% SPIDER · 15% AMR PRO (OUR ARITHMETIC)")
sc("""Fortune says Aston Martin delivered sixty-seven Valkyries in the first three quarters of twenty twenty-three. By our arithmetic, that is about twenty-two a quarter. At that pace, two hundred seventy-five cars take around twelve quarters, or three years. Wikipedia says production ran from November twenty twenty-one to December twenty twenty-four, which matches that estimate well.""",
   "Aston Martin Valkyrie deliveries", "67 DELIVERED IN 9 MONTHS OF 2023 → ~22 A QUARTER")
sc("""That matters when we ask how rare these cars really are. Two hundred seventy-five of each means there are at most five hundred fifty cars of these two models in the world, by our arithmetic. Compare that with the seven thousand, two hundred sixty-five Lamborghini Urus built in just the year twenty twenty-five, according to Wikipedia.""",
   "Hypercar rarity", "550 CARS VS 7,265 URUS BUILT IN ONE YEAR")

ch("The verdict")
sc("""So how do they compare? On combustion power, the Valkyrie. On total power, the Valkyrie, by about eleven percent. On weight, the Valkyrie, by about twenty percent. On acceleration to a hundred, the Valkyrie. On a published Nürburgring record, the AMG One. On engine technology, the AMG One. On price, the AMG One. On servicing, we only know the Valkyrie.""",
   "Mercedes-AMG One and Aston Martin Valkyrie", "SCORECARD")
sc("""The real difference is the idea. Mercedes took the hybrid system it used to win in Formula One and made it legal for the road. Aston Martin and Red Bull built a lightweight V twelve with minimal hybrid assistance, and a body shaped like a racing car. Both approaches produced cars that most people will only ever see in pictures.""",
   "Hypercars", "TWO WAYS TO BUILD A ROAD-GOING RACE CAR")
sc("""One caution. We have not driven either car. Every figure comes from published sources, some of which conflict, and some of the comparisons are our own arithmetic. We do not claim which is better. We only claim what the numbers show, and where they stop. The Valkyrie's weight alone could change the picture, and the sources do not agree on it.""",
   "Hypercars", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you choose, the AMG One or the Valkyrie? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the AMG One, count the cost of a Formula One engine for the road, and explain why the AMG One took years longer than promised.""",
   "Mercedes-AMG One and Aston Martin Valkyrie", "AMG ONE OR VALKYRIE?")
sc("""And if you would rather spend your money on something you can drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more comparisons between the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video102", "AMG One vs Aston Martin Valkyrie: The Real Difference", [
    "Wikipedia, Mercedes-AMG One: https://en.wikipedia.org/wiki/Mercedes-AMG_One",
    "Wikipedia, Aston Martin Valkyrie: https://en.wikipedia.org/wiki/Aston_Martin_Valkyrie",
    "Fortune/Bloomberg, Aston Martin's most expensive Valkyrie supercar (23 Feb 2024): https://fortune.com/europe/2024/02/23/aston-martin-most-expensive-valkyrie-supercar-3-million-plus-450000-upkeep",
    "Automotive News Europe, Aston Martin Valkyrie deliveries delayed by electronics issues: https://europe.autonews.com/automakers/aston-martin-valkyrie-deliveries-delayed-electronics-issues-report-says",
    "CarAdvice, Mercedes-AMG One delayed nine months: https://www.caradvice.com.au/news/mercedes-amg-one-delayed/",
    "Autocar, Mercedes-AMG One delay: https://www.autocar.co.uk/node/102901",
    "Top Gear, The Mercedes-AMG One won't compete at Le Mans (11 Sept 2019): https://www.topgear.com/car-news/frankfurt-motor-show/mercedes-amg-one-wont-compete-le-mans",
], "B")
