import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""In twenty seventeen, Mercedes-AMG promised a Formula One car for the road, and said it would arrive in twenty nineteen. It arrived in January twenty twenty-three. And when it did, several numbers that were promised in the early reports had changed. The weight, the gearbox, the acceleration. This is the story of why the Mercedes-AMG One took years longer than promised, and what changed on the way.""",
   "Mercedes-AMG One", "WHY THE MERCEDES-AMG ONE TOOK YEARS LONGER THAN PROMISED")
sc("""Here is the twist. The company itself never hid the delay. Its boss said there was no excuse on the company's side. Its chief executive joked that they must have been drunk when they said yes. And the delay was not caused by one problem. It was caused by at least four, and one of them was a number so small it fits in a sentence. Twelve hundred.""",
   "Mercedes-AMG One engine", "FOUR PROBLEMS · ONE SMALL NUMBER")
sc("""Every claim in this video comes from published sources, listed in the description. Where sources disagree, we will say so. Where we do the maths ourselves, we will say that too.""",
   "Mercedes-AMG One", "EVERY NUMBER IS SOURCED")

ch("The promise")
sc("""Wikipedia says the Project One concept was unveiled at the International Motor Show Germany in twenty seventeen, by Lewis Hamilton and Dieter Zetsche. The idea was radical: put a road-legal version of the Mercedes Formula One power unit into a production car, with a hybrid system, and sell two hundred seventy-five of them.""",
   "Lewis Hamilton Mercedes", "2017: PROJECT ONE UNVEILED IN FRANKFURT")
sc("""Motor1's report of the second of August, twenty eighteen, gives the expectations at that time. Deliveries to begin in early twenty nineteen. Output of one thousand to one thousand, one hundred horsepower from the engine and four electric motors. A top speed above three hundred fifty kilometres per hour. Autocar also says the car was originally due in early twenty nineteen.""",
   "Mercedes-AMG Project One", "2018 EXPECTATION: DELIVERIES EARLY 2019")
sc("""Those early reports also gave expectations for the car's body. Motor1 said the expected weight was one thousand, three hundred to one thousand, four hundred kilograms. Expected downforce was about six hundred seventy-five kilograms. Zero to two hundred kilometres per hour in under six seconds. And an eight-speed automatic transmission. These were expectations in a news report, not final specifications.""",
   "Mercedes-AMG Project One prototype", "2018 EXPECTED: 1,300–1,400 KG · 0–200 IN <6 S · 8-SPEED")
sc("""The price was clear from the start. Motor1 gave two point seven million dollars, and said all two hundred seventy-five cars had sold. The company also reportedly told buyers they could not flip the cars for a quick profit. So customers had paid a huge sum, signed contracts, and were waiting for a car they were told would arrive in about a year.""",
   "Mercedes-AMG Project One buyers", "$2.7M · SOLD OUT · ARRIVAL: ABOUT A YEAR")

ch("The calendar of delays")
sc("""Now follow the dates. Top Gear, in September twenty nineteen, said the car would arrive in the first quarter of twenty twenty-one, in time for the new hypercar class at Le Mans. Autocar later said customers had been told by letter that production would begin in twenty twenty-two, and that the company expected to start around the middle of that year.""",
   "Mercedes-AMG One timeline", "2019: Q1 2021 · LATER: 2022")
sc("""Wikipedia then says the production version was unveiled on the first of June twenty twenty-two, production began in August twenty twenty-two, and the first customer delivery was on the sixteenth of January twenty twenty-three. By our own arithmetic, that is almost four years after the first delivery date of early twenty nineteen.""",
   "Mercedes-AMG One delivery", "FIRST DELIVERY: 16 JANUARY 2023")
sc("""Put the steps in order, as our own arithmetic. Early twenty nineteen, the original promise. First quarter of twenty twenty-one, about two years later. Middle of twenty twenty-two, about three and a half years later. And January twenty twenty-three, almost four years later. Each new date was a promise that was not kept, and each one was explained.""",
   "Calendar", "2019 → 2021 → 2022 → 2023 (OUR ARITHMETIC)")
sc("""It is worth saying that the delay was not hidden. Motor1's April twenty twenty-four article records that idle speed work delayed development by nine months. CarAdvice quotes Tobias Moers saying the company lost maybe nine months or so, and that customers had been told about the delay. He called it not a secret. A company in trouble would have tried to hide it.""",
   "Tobias Moers", "\"NOT A SECRET\" — MOERS ON THE DELAY")

ch("Problem one: the idle")
sc("""The first problem is the one in the title of the Top Gear and Autocar stories. A Formula One engine idles at about five thousand r p m. A road car must idle at about twelve hundred. Autocar called it a tremendous challenge. Wikipedia lists the idle at twelve hundred eighty, CarAdvice says twelve hundred. The two numbers describe the same target.""",
   "Engine rev counter", "IDLE: ~5,000 RPM → ~1,200 RPM")
sc("""Why is this so hard? Top Gear explains that the engine was originally designed for high revs, fourteen to fifteen thousand r p m, and that there were airflow problems at twelve hundred. In other words, the engine breathes in a way that works at high speed. At low speed, the airflow is wrong. Fixing it means changing how the engine breathes, not just how it is controlled.""",
   "Engine airflow", "DESIGNED FOR 14,000–15,000 RPM · AIRFLOW PROBLEMS AT 1,200")
sc("""By our arithmetic, the idle speed was cut by about seventy-six percent, from five thousand to twelve hundred. And the redline, according to CarAdvice, fell from fourteen thousand to eleven thousand. A change of that size touches almost everything: fuelling, valve timing, lubrication, cooling, and software. It is not a modification. It is a redesign.""",
   "Mercedes F1 engine", "IDLE −76% · REDLINE −21% (OUR ARITHMETIC)")

ch("Problem two: emissions")
sc("""The second problem was emissions. Autocar says meeting W L T P emissions standards with a petrol particulate filter, without losing performance, was a major hurdle. CarAdvice quotes chief executive Ola Källenius saying the same, and says adapting the engine's revving characteristics for road use was another major challenge.""",
   "Exhaust", "WLTP + PETROL PARTICULATE FILTER")
sc("""Top Gear adds that emissions certification for the engine took a while. A petrol particulate filter must be fitted into the exhaust of a car that is already packaged to the millimetre. It restricts the flow of exhaust gas, which a turbocharged hybrid system depends on. Keeping performance while adding that restriction is what Autocar calls the hurdle.""",
   "Exhaust system", "A FILTER IN A CAR PACKAGED TO THE MILLIMETRE (OUR READING)")
sc("""The official result is in Top Gear's buying guide. Fuel economy of thirty-two miles per gallon and carbon dioxide emissions of one hundred ninety-eight grams per kilometre. Those figures would have been unthinkable for the original racing engine, which does not run on those terms. They are what the engineers delivered at the end of the process.""",
   "Mercedes-AMG One emissions", "OFFICIAL: 32 MPG · 198 G/KM CO2")

ch("Problem three: noise")
sc("""The third problem was noise. Top Gear lists noise control, both inside the cabin and for drive-by noise under new regulations. A Formula One engine is loud. A road car must pass a drive-by noise test, and a hypercar has to be comfortable enough inside that the owner can use it. The sources do not give decibel figures, so we will not guess any.""",
   "Mercedes-AMG One exhaust", "CABIN NOISE + DRIVE-BY NOISE RULES")
sc("""This was a regulation that changed over the course of the project. Top Gear says new regulations applied, which implies that the target moved while the engineers were working. We cannot say exactly which regulation, because the source does not name it. But the pattern is common in long projects: the longer the delay, the more rules there are to satisfy.""",
   "Regulations", "NEW RULES APPLIED DURING DEVELOPMENT (TOP GEAR)")

ch("Problem four: the hybrid and the car around it")
sc("""The fourth problem is the hardest to see. Autocar says adapting the Formula One derived hybrid powertrain for road use was an engineering problem that pushed the date back. The final system has an M G U K, an M G U H, two front motors and an eight hundred volt battery, according to Wikipedia. Packaging all of it in a road car is a project in itself.""",
   "Mercedes-AMG One hybrid system", "MGU-K + MGU-H + 2 FRONT MOTORS + 800 V BATTERY")
sc("""Look at how the car changed between the early reports and the final specification. Motor1 expected one thousand, three hundred to one thousand, four hundred kilograms in twenty eighteen. Wikipedia lists one thousand, six hundred ninety-five kilograms. By our arithmetic, that is at least two hundred ninety-five kilograms, or about twenty-one percent, more than the upper expectation of fourteen hundred.""",
   "Mercedes-AMG One weight", "EXPECTED ≤1,400 KG (2018) → LISTED 1,695 KG")
sc("""Acceleration changed too. Motor1 reported an expectation of zero to two hundred kilometres per hour in under six seconds. Wikipedia lists seven point zero. And where the early report said an eight-speed automatic, the final car has a seven-speed single-clutch automated manual with a carbon clutch. We report the numbers, and let you draw the conclusion.""",
   "Mercedes-AMG One transmission", "0–200: <6 S (2018) → 7.0 S (WIKIPEDIA)")
sc("""A fair reading is that the road-legal car is heavier and slower than the early expectations. But it is still extraordinarily fast. Wikipedia lists two point nine seconds to a hundred, fifteen point six to three hundred, and a top speed of three hundred fifty-two. The early expectations were targets, and in a project that long, targets move.""",
   "Mercedes-AMG One", "TARGETS MOVE IN A LONG PROJECT (OUR READING)")
sc("""There is a reason this matters. The company did not just fix the engine. It rebuilt the idea of the car. A weight increase of roughly three hundred kilograms is the sort of change that follows from adding a particulate filter, noise insulation, a larger battery, and equipment to satisfy regulations. But the sources do not state this cause directly, so it is our reading.""",
   "Mercedes-AMG One", "WHY IS IT HEAVIER? THE SOURCES DON'T SAY (OUR READING)")

ch("Testing: the road to the road")
sc("""The testing itself was long and public. Motor1's twenty eighteen report says track testing with camouflaged prototypes had started in the United Kingdom and Spain. Autocar adds that the car was spied testing on public roads and was shown on Mercedes-AMG's stand at the Munich motor show, and that an official video showed it driving at speed on a test track.""",
   "Camouflaged prototype", "PROTOTYPES TESTED IN THE UK AND SPAIN")
sc("""Autocar also notes the car adopted the E Performance name, which would replace E Q Power Plus for the brand's performance hybrids. The article says the car was meant to showcase the performance potential of Mercedes-AMG's hybrid and electrified technology. So the delay was not only about the engine. It was about a product that was meant to represent a whole new line.""",
   "Mercedes-AMG E Performance", "E PERFORMANCE NAME REPLACES EQ POWER+ (AUTOCAR)")
sc("""Along the way, the company made decisions about what the car would not be. Top Gear says Moers did not want to race it at Le Mans, because he disliked spending heavily on a series using balance of performance rules. He also said he was not interested in a speed competition. Each decision narrowed the project and, by our reading, kept the delay from growing longer.""",
   "Le Mans", "NO LE MANS · NO SPEED-RECORD CHASE")
sc("""Top Gear's buying guide includes a warning from AMG about the original racing engine. It says the engine needs a team of experts to start and must be discarded after a handful of races. That is the source material the engineers had. Turning a part with that life into one that survives about fifty thousand kilometres of road use is a measure of the work involved.""",
   "Mercedes F1 engine", "F1 ENGINE: DISCARDED AFTER A HANDFUL OF RACES (TOP GEAR)")
sc("""By our arithmetic we can express the improvement in one line. A road car engine that lasts fifty thousand kilometres is not a long-lived engine by road standards. But set against an engine that is discarded after a handful of races, it is a huge step. The delay bought durability as much as it bought legality. That is our reading, not a claim from the sources.""",
   "Mercedes-AMG One engine", "DURABILITY WAS PART OF THE WORK (OUR READING)")

sc("""One more detail about the source engine, because the sources disagree. Motor1's twenty eighteen report says it is based on the unit from Lewis Hamilton's twenty fifteen Formula One car. Wikipedia names the W oh six, the twenty fifteen car, through Ola Källenius. Autocar says it is adapted from the twenty seventeen championship-winning car. Two sources point to twenty fifteen and one to twenty seventeen.""",
   "Lewis Hamilton Formula One car", "2015 CAR (WIKIPEDIA, MOTOR1) VS 2017 CAR (AUTOCAR)")
sc("""Why does the year matter for the delay? Because a Formula One engine develops every season, and a road car programme that starts from one version and ends years later is chasing a moving target. We cannot tell from the sources whether the engineers updated the design as it went. But the disagreement itself shows how hard it is to describe a project that long.""",
   "Mercedes F1 engine", "A MOVING TARGET (OUR READING)")

ch("A hypercar is not just an engine")
sc("""Wikipedia lists what else the car had to do. Active front diffuser flaps, a two-part extendable rear wing, adjustable front louvres. Driving modes called Race Safe, Race, E V, Race Plus, Strat Two and Individual. Race Plus and Strat Two raise total downforce by up to five times. All of it had to be designed, tested and certified for the road.""",
   "Mercedes-AMG One aerodynamics", "ACTIVE AERO · SIX DRIVING MODES")
sc("""The body and chassis are carbon fibre, with butterfly doors, according to Wikipedia. Gorden Wagener, head of design, and Hartmut Sinkwitz, who led interior design, were responsible for the look. A show car can be anything. A production car must pass crash tests, fit people, keep them comfortable and survive years of use. That transition takes time in any programme.""",
   "Mercedes-AMG One body", "FROM SHOW CAR TO CERTIFIED CAR (OUR READING)")
sc("""The scale of production was small, but not simple. Wikipedia says all two hundred seventy-five cars are hand-built, with production from August twenty twenty-two to twenty twenty-five. By our arithmetic, that is about three years for two hundred seventy-five cars, or around ninety cars a year. Hand-building at that rate means a long, careful process for each one.""",
   "Mercedes-AMG One production", "~90 CARS A YEAR, HAND-BUILT (OUR ARITHMETIC)")
sc("""So even after the engine was solved, the full run could not be delivered at once. A customer who ordered in twenty seventeen might not have received the car until much later than the first delivery in January twenty twenty-three. We do not know the order of delivery, and the sources do not say. But production time adds to the wait for the last buyers.""",
   "Mercedes-AMG One assembly", "FIRST DELIVERY ≠ LAST DELIVERY (OUR READING)")

ch("Not alone: the Valkyrie")
sc("""The AMG One was not the only hypercar to run late. Wikipedia says Aston Martin delivered only ten Valkyries in the fourth quarter of twenty twenty-one, fewer than planned, which caused it to miss its profit target. Autonews, citing unnamed sources, said electronics problems delayed the launch. Fortune said the launch was delayed repeatedly while the carmaker fixed electronics.""",
   "Aston Martin Valkyrie", "VALKYRIE: ONLY 10 DELIVERED IN Q4 2021")
sc("""The difference is in the explanation. For the AMG One, executives named the problems and described them, and the sources agree on the details. For the Valkyrie, our sources give less detail and rely on unnamed people. That does not mean one project was better managed. It means that, for the AMG One, we can tell you much more about why it was late.""",
   "Hypercars", "WE KNOW MORE ABOUT WHY THE AMG ONE WAS LATE")
sc("""Hypercars are late often enough that it looks like a pattern. The most radical cars take the most development, and radical means new technology, new regulations and untested packaging. A manufacturer that promises a date is making a forecast, not a measurement. In the AMG One's case, the forecast was off by years, and the company said so openly.""",
   "Hypercar development", "FORECASTS, NOT MEASUREMENTS (OUR READING)")

sc("""Consider the timing from the customers' side. Someone who ordered in twenty seventeen was told early twenty nineteen. In twenty nineteen they were told early twenty twenty-one. Later they were told twenty twenty-two. Each message came with an explanation and, according to Moers, no attempt to hide it. By our reading, honesty is what made the wait tolerable, because the order book stayed full.""",
   "Mercedes-AMG One customers", "HONESTY KEPT THE ORDER BOOK FULL (OUR READING)")
sc("""And the order book did stay full. Wikipedia says more than four times as many orders arrived as there were cars, and that Mercedes refused to raise the limit. Our sources show no sign that the company cut its price or added cars to keep buyers happy. For a delayed product, that is unusual, and it suggests how much people wanted this particular engine.""",
   "Mercedes-AMG One order book", "4× ORDERS · LIMIT KEPT AT 275")

ch("What it means for buyers")
sc("""If you are thinking about a limited car, the AMG One story has a lesson. A delivery date in an early report is a hope. A specification in an early report is a target. Both can move, and in this case both did. The only things that did not move were the price of about two point seven million dollars and the number, two hundred seventy-five.""",
   "Mercedes-AMG One", "DATES AND SPECS MOVED · PRICE AND QUANTITY DID NOT")
sc("""And the owners who waited gained something that cannot be bought later. Mercedes has, according to Motor1, ruled out putting a Formula One engine in a future road car. Whatever you think of the delay, the car that arrived is a rare thing, built at a time when a company still tried to do it. That is a fair reason to forgive a few years.""",
   "Mercedes-AMG One", "MOTOR1: NO F1 ENGINE IN A FUTURE ROAD CAR")

ch("What the bosses said")
sc("""The most interesting evidence is what the executives said. Tobias Moers told Top Gear in September twenty nineteen that there was no excuse on the company's side, and that it maybe underestimated the journey. He said the final engine had been specified and was on a dynamometer. It is rare to hear a company admit it underestimated a task.""",
   "Tobias Moers", "\"MAYBE WE UNDERESTIMATED THE JOURNEY\"")
sc("""Ola Källenius, according to CarAdvice, joked that he was sure the company was drunk when it said yes. He said the idea was pitched about four years before the reveal. It is a joke, and should be read as one. But there is real information in it: the project was approved before the company understood how much work was needed.""",
   "Ola Källenius", "\"I'M SURE WE WERE DRUNK WHEN WE SAID YES\"")
sc("""Moers also said he expected a period of major issues that had to be solved. That tells us the engineers knew from the start that a Formula One engine would not simply fit. They just did not know how long the work would take. By our reading, that is the heart of the delay: a known problem, with an unknown schedule.""",
   "Mercedes-AMG engineers", "A KNOWN PROBLEM WITH AN UNKNOWN SCHEDULE (OUR READING)")

ch("Was the wait worth it?")
sc("""Judge the result by what the sources list. All two hundred seventy-five cars sold, with more than four times as many orders, according to Wikipedia. A Nürburgring lap of six minutes, twenty-nine point zero nine seconds in September twenty twenty-four. Production-car records at Monza and other circuits. A car that can be driven on public roads, with a plug-in range of about eighteen kilometres.""",
   "Mercedes-AMG One", "275 SOLD · NÜRBURGRING 6:29.09 · ROAD LEGAL")
sc("""The customers who waited did get the car. The first delivery on the sixteenth of January twenty twenty-three came in a livery inspired by the Formula One car W twelve E Performance. By our arithmetic, it came more than five years after the Frankfurt reveal in twenty seventeen.""",
   "Mercedes-AMG One delivery", "FRANKFURT SHOW TO FIRST DELIVERY: 5+ YEARS")
sc("""The price of the delay was paid by the company's schedule and by the customers' patience. The price of the solution, the engine's short service life, is paid by the owners. Wikipedia says the engine must be returned for refurbishment at about fifty thousand kilometres. A road car that needs that is the final consequence of making a racing engine street legal.""",
   "Mercedes-AMG One engine", "THE SOLUTION'S PRICE: A 50,000 KM ENGINE LIFE")
sc("""So why did it take years longer than promised? Because a Formula One engine had to learn to idle, pass emissions, stay quiet, and live inside a hybrid system, all at once, in a car that people would drive on public roads. Every one of those was solved, and every one took time. That is the whole story, and the sources support it.""",
   "Mercedes-AMG One", "IDLE · EMISSIONS · NOISE · HYBRID: ALL AT ONCE")
sc("""A last caution. We have not driven the car, and the early specifications in the 2018 reports were expectations, not promises. We have tried to show where the sources agree, where they disagree, and where our own arithmetic fills a gap. If you know a firsthand account, tell us in the comments, with where it comes from.""",
   "Mercedes-AMG One", "EXPECTATIONS ARE NOT SPECIFICATIONS")
sc("""In the other videos of this series, we reveal two secrets hidden inside the AMG One, compare it with the Aston Martin Valkyrie, and count the cost of a Formula One engine for the road. If you would rather spend your money on something you can drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video104", "Why the Mercedes-AMG One Took Years Longer Than Promised", [
    "Wikipedia, Mercedes-AMG One: https://en.wikipedia.org/wiki/Mercedes-AMG_One",
    "Top Gear, The Mercedes-AMG One won't compete at Le Mans (11 Sept 2019): https://www.topgear.com/car-news/frankfurt-motor-show/mercedes-amg-one-wont-compete-le-mans",
    "Top Gear, Mercedes-AMG One buying guide: https://www.topgear.com/car-reviews/mercedes-benz/amg-one/buying",
    "Autocar, Mercedes-AMG One delay: https://www.autocar.co.uk/node/102901",
    "CarAdvice, Mercedes-AMG One delayed nine months: https://www.caradvice.com.au/news/mercedes-amg-one-delayed/",
    "CarAdvice, Mercedes CEO: We were drunk when AMG One hypercar was approved: https://www.caradvice.com.au/news/mercedes-ceo-drunk-when-amg-one-approved/",
    "Motor1, Mercedes-AMG won't allow Project One owners to flip their cars (2 Aug 2018): https://www.motor1.com/news/260939/mercedes-amg-project-one/",
    "Motor1, This Mercedes-AMG One with 55 miles begs to be driven (12 Apr 2024): https://www.motor1.com/news/715837/amg-one-low-mileage-sale/",
], "D")
