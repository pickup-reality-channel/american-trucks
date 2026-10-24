import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Mercedes-AMG One has a Formula One engine in it. Not an engine inspired by Formula One. A road-going version of the one-point-six-litre turbo V six from Mercedes' own Formula One cars. And hidden inside that fact are two secrets that almost nobody talks about. One of them explains why the car arrived years late. The other explains a bill that every owner has to face.""",
   "Mercedes-AMG One", "2 SECRETS HIDDEN INSIDE THE MERCEDES-AMG ONE")
sc("""Here is the twist. Wikipedia says the engine lasts about fifty thousand kilometres, after which owners must return the car to be refurbished. And the other secret is a number that sounds tiny. It is twelve hundred. Stay to the end, because twelve hundred is the reason this car was late.""",
   "Mercedes-AMG One engine", "SECRET ONE: ABOUT 50,000 KM. SECRET TWO: 1,200.")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Mercedes-AMG One", "EVERY NUMBER IS SOURCED")

# ---------- 1. ORIGIN ----------
ch("A concept that became a promise")
sc("""The story begins in two thousand seventeen. Wikipedia says the Project One concept was unveiled at the International Motor Show Germany, in Frankfurt, by Lewis Hamilton and Dieter Zetsche. It was a Formula One engine in a road car, and Mercedes said it would build it. Nobody outside the company knew how hard that would turn out to be.""",
   "Lewis Hamilton Mercedes", "2017: PROJECT ONE UNVEILED IN FRANKFURT")
sc("""The car was developed at Mercedes-AMG in Affalterbach, Germany. The production version was unveiled on the first of June, twenty twenty-two. Production began in August twenty twenty-two, according to Wikipedia, and the first customer delivery came on the sixteenth of January, twenty twenty-three, in a livery inspired by the Formula One car W twelve E Performance.""",
   "Mercedes-AMG Affalterbach", "FIRST DELIVERY: 16 JANUARY 2023")
sc("""By our own arithmetic, the gap between the unveiling in twenty seventeen and the first delivery in January twenty twenty-three is more than five years. That is a long time even for a hypercar. And CarAdvice, quoting the company, says production was originally due in twenty nineteen. By our arithmetic that makes the car about four years late, and we will come back to why.""",
   "Mercedes-AMG One timeline", "2017 CONCEPT → JAN 2023 FIRST DELIVERY")
sc("""The numbers behind the car are enormous. Wikipedia says only two hundred seventy-five were built, all by hand. The price listed on Wikipedia is two point seven two million dollars each. CarAdvice, in an earlier article, gave two point two seven million euros. Different currencies and different dates, so we will say only that it cost around two and a half million.""",
   "Mercedes-AMG One production", "275 BUILT · ~$2.7M EACH")
sc("""And the demand was larger than the supply. Wikipedia says Mercedes-AMG received more than four times as many orders as there were cars, and refused to raise the limit. By our arithmetic, that is more than eleven hundred requests for two hundred seventy-five cars. Every one of those buyers wanted the same thing, which was a Formula One engine they could register.""",
   "Mercedes-AMG One", "4× MORE ORDERS THAN CARS")

# ---------- 2. SECRET ONE ----------
ch("Secret one: the engine has an expiry date")
sc("""Now the first secret. According to Wikipedia, the engine in the AMG One has a lifespan of about fifty thousand kilometres, which is about thirty-one thousand miles. After that, owners must return the car for engine refurbishment. Most road car engines are designed to run for hundreds of thousands of kilometres. This one is not.""",
   "Mercedes-AMG One engine", "ENGINE LIFE: ~50,000 KM (31,000 MI)")
sc("""The reason is what it is. Wikipedia lists the engine as the P U one oh six B hybrid, a one-point-six-litre turbocharged V six with a ninety-degree layout, modified from the Mercedes Formula One engine. Output from the combustion engine alone is four hundred twenty-two kilowatts, or five hundred seventy-four metric horsepower. The redline is eleven thousand r p m.""",
   "Mercedes F1 engine", "1.6 L V6 · 574 PS · REDLINE 11,000 RPM")
sc("""On top of that sits a hybrid system. The page lists an M G U K of one hundred twenty kilowatts connected to the crankshaft, and an M G U H of ninety kilowatts connected to the turbocharger. The M G U H is the part many road cars never use. It recovers energy from exhaust gas, the same idea as in the Formula One cars of that era.""",
   "Mercedes F1 hybrid system", "MGU-K 120 KW · MGU-H 90 KW")
sc("""There are also two electric motors on the front axle, one hundred twenty kilowatts each. Wikipedia gives the total system output as one thousand sixty-three metric horsepower, or one thousand forty-nine horsepower. Note that the same page also lists a combined figure for the four motors that does not match its own individual numbers, so we use the headline total.""",
   "Mercedes-AMG One front motors", "SYSTEM OUTPUT: 1,063 PS / 1,049 HP")
sc("""The battery is an eight hundred volt lithium-ion pack, and the electric range is eighteen point one kilometres, about eleven miles. The gearbox is a seven-speed single-clutch automated manual with a four-disc carbon clutch. It drives the rear wheels, with the front motors adding all-wheel drive. This is not a road car engine with a few changes. It is a racing engine with road equipment.""",
   "Mercedes-AMG One battery", "800 V BATTERY · 18.1 KM ELECTRIC RANGE")
sc("""So what does fifty thousand kilometres mean in practice? By our own arithmetic, a car driven five thousand kilometres a year would reach the limit in ten years. But a hypercar driven hard on a track could reach it much sooner. We do not know how many owners will do either, and the source does not say what the refurbishment costs, so we will not guess.""",
   "Mercedes-AMG One owner", "50,000 KM = 10 YEARS AT 5,000 KM/YEAR (OUR ARITHMETIC)")
sc("""There is a comparison worth making. A typical road car engine is built to run far beyond fifty thousand kilometres without any rebuild. That is why this detail surprises people. The owner of an AMG One buys a car with a service schedule closer to a race team than a family sedan. The price of the engine is only part of the price of owning it.""",
   "Mercedes-AMG One engine bay", "A RACE-TEAM SERVICE SCHEDULE")

# ---------- 3. SECRET TWO ----------
ch("Secret two: the number twelve hundred")
sc("""Now the second secret, the number twelve hundred. CarAdvice quotes Mercedes-AMG boss Tobias Moers, speaking to Top Gear, saying the company lost maybe nine months. The reason, the article explains, is that making a Formula One engine work on the road is difficult. Emissions rules require a stable idle of twelve hundred r p m.""",
   "Tobias Moers", "\"WE LOST MAYBE NINE MONTHS OR SO\"")
sc("""A Formula One engine idles at around five thousand r p m. A road car must idle at about twelve hundred, quietly, without stalling, while meeting emissions rules. CarAdvice says the idle was lowered from the Formula One figure of five thousand to twelve hundred, and the redline from fourteen thousand to eleven thousand. Wikipedia lists the idle as twelve hundred eighty.""",
   "Engine rev counter", "IDLE: 5,000 RPM (F1) → ~1,200 RPM (ROAD)")
sc("""Note the small discrepancy. CarAdvice says twelve hundred. Wikipedia says twelve hundred eighty. We think both are describing the same target, but we cannot tell you which is exact, so we say about twelve hundred. What matters is the size of the change. By our arithmetic, the idle speed fell by about seventy-five percent.""",
   "Mercedes-AMG One", "TWO SOURCES: 1,200 AND 1,280 RPM")
sc("""And that was only one of the problems. Another CarAdvice article, quoting chief executive Ola Källenius, says meeting the European W L T P emissions rules with a petrol particulate filter, without hurting performance too much, pushed the timeline back. Adapting how the engine revs for road use was another major challenge. Each fix took months.""",
   "Ola Källenius", "WLTP + PARTICULATE FILTER = MORE DELAY")
sc("""Källenius even joked about the decision. CarAdvice quotes him saying he was sure the company was drunk when it said yes to the project. He said the idea was pitched to the board about four years before the reveal. It is a joke, and we should treat it as one, but it tells you how hard the engineers found the task.""",
   "Ola Källenius", "\"I'M SURE WE WERE DRUNK WHEN WE SAID YES\"")
sc("""Moers also said, in the Top Gear interview, that he expected a time with major issues that had to be solved, and that customers had been told about the delay. He called it not a secret. That openness is worth noting. The company did not hide a problem. It simply took the time it needed to make the engine legal and usable.""",
   "Mercedes-AMG engineers", "CUSTOMERS WERE TOLD ABOUT THE DELAY")

# ---------- 4. PERFORMANCE ----------
ch("What all that work produced")
sc("""The result is extraordinary. Wikipedia lists zero to a hundred kilometres per hour in two point nine seconds, zero to two hundred in seven point zero, and zero to three hundred in fifteen point six. The top speed is three hundred fifty-two kilometres per hour, electronically limited. These are manufacturer claims, listed on that page.""",
   "Mercedes-AMG One acceleration", "0–100: 2.9 S · 0–200: 7.0 S · 0–300: 15.6 S")
sc("""Look at the gap between two hundred and three hundred. By our own arithmetic, the car takes eight point six seconds to go from two hundred to three hundred kilometres per hour. Most cars cannot reach three hundred at all. This is where the Formula One hybrid system earns its place, adding electric torque while the engine climbs.""",
   "Mercedes-AMG One speed", "200 → 300 KM/H IN 8.6 S (OUR ARITHMETIC)")
sc("""On the Nürburgring Nordschleife, Wikipedia says Maro Engel drove a lap in six minutes, thirty-five point one eight three seconds in November twenty twenty-two, beating the Mercedes-AMG G T Black Series record by more than thirteen seconds. The page notes damp patches forced some lifting. So the car was not even at its limit.""",
   "Nürburgring Nordschleife", "NOV 2022: 6:35.183 (MARO ENGEL)")
sc("""In September twenty twenty-four, the car improved on its own record. The page lists six minutes, twenty-nine point zero nine seconds, about six seconds quicker, and says it was the first lap under six thirty by a road-legal production car. That is a claim on Wikipedia, and records in this category are contested, so we report it as stated.""",
   "Nürburgring record", "SEPT 2024: 6:29.09 · FIRST SUB-6:30 (PER WIKIPEDIA)")
sc("""The page lists other claimed records too. The Nürburgring Grand Prix circuit in one minute, fifty-six point zero nine six. Hockenheim in one thirty-eight point five six three. The Red Bull Ring in one twenty-six point eight four six. And Monza in one forty-three point nine zero two, in April twenty twenty-three, a production-car record.""",
   "Racing circuit", "RECORDS AT HOCKENHEIM, RED BULL RING, MONZA")

# ---------- 5. AERO ----------
ch("The aerodynamics nobody notices")
sc("""The car also carries Formula One ideas in its shape. Wikipedia lists active front diffuser flaps, a two-part extendable rear wing in the style of D R S, and adjustable front louvres. The body and chassis are carbon fibre, and the car has butterfly doors. Gorden Wagener was head of design, and Hartmut Sinkwitz led the interior.""",
   "Mercedes-AMG One rear wing", "ACTIVE AERO · CARBON FIBRE · BUTTERFLY DOORS")
sc("""There are driving modes called Race Safe, Race, E V, Race Plus, Strat Two, and Individual. According to the page, Race Plus and Strat Two raise the total downforce by up to five times. That is a statement about how much of the car's behaviour is controlled by software and active parts, not by fixed metal alone.""",
   "Mercedes-AMG One driving modes", "RACE PLUS / STRAT 2: UP TO 5× DOWNFORCE")
sc("""The dimensions are those of a low, wide car. Wikipedia lists a length of four thousand, seven hundred fifty-six millimetres, a width of two thousand and ten, a height of one thousand, two hundred sixty-one, and a wheelbase of two thousand, seven hundred twenty. The kerb weight is one thousand, six hundred ninety-five kilograms, with a range up to one thousand, seven hundred forty-five.""",
   "Mercedes-AMG One dimensions", "1,261 MM TALL · 1,695 KG KERB")
sc("""By our arithmetic, one thousand sixty-three metric horsepower divided by one thousand, six hundred ninety-five kilograms gives about point six three horsepower per kilogram. That is high, but notice what the weight tells you. The hybrid system, battery and motors are heavy. A Formula One car carries far less. The road equipment has a weight cost.""",
   "Mercedes-AMG One weight", "~0.63 PS PER KG (OUR ARITHMETIC)")
sc("""Which Formula One car? The sources disagree. Wikipedia says the engine and design are based on the Mercedes-AMG F one W oh six, per Ola Källenius. Autocar says it is adapted from the engine of Mercedes' twenty seventeen Formula One championship-winning car. We report both, because we cannot tell from here which description the company prefers.""",
   "Mercedes F1 car", "SOURCES DISAGREE: W06 (WIKIPEDIA) VS 2017 CAR (AUTOCAR)")

ch("A timeline of slipping dates")
sc("""Let us follow the delivery date as it moved. Autocar says the car was originally due in early twenty nineteen. CarAdvice also says production was originally due in twenty nineteen. In September twenty nineteen, Top Gear reported that it would arrive in the first quarter of twenty twenty-one, in time for the new hypercar class.""",
   "Mercedes-AMG One timeline", "2019 PROMISED · Q1 2021 · THEN 2022")
sc("""Later, Autocar reports, Mercedes-AMG confirmed the car would enter production around the middle of the following year, and customers were told by letter that production of the first of two hundred seventy-five cars would begin in twenty twenty-two. Wikipedia says production did begin in August twenty twenty-two. So that promise, at least, was kept.""",
   "Mercedes-AMG One production", "AUGUST 2022: PRODUCTION BEGINS")
sc("""By our arithmetic, from early twenty nineteen to the first delivery in January twenty twenty-three is almost four years. And from the Top Gear target of the first quarter of twenty twenty-one, the slip is about two years. Each delay came with a reason, and the reasons are what make this story interesting, rather than just a calendar of apologies.""",
   "Calendar", "~4 YEARS LATE VS 2019 · ~2 YEARS VS Q1 2021 (OUR ARITHMETIC)")
sc("""Top Gear listed the causes in twenty nineteen. Emissions certification for the engine took a while. Noise control took time, both inside the cabin and for drive-by noise under new regulations. And the engine, designed for fourteen to fifteen thousand r p m, had airflow problems at twelve hundred. These are the details behind the twelve hundred secret.""",
   "Mercedes-AMG One testing", "EMISSIONS · NOISE · LOW-RPM AIRFLOW")
sc("""Tobias Moers was frank about it. Top Gear quotes him saying there was no excuse on the company's side, and that it maybe underestimated the journey. It is rare for a company to say that about a car it has already sold. And at that point, Top Gear says, the final engine had been specified and was running on a dynamometer.""",
   "Tobias Moers", "\"THERE'S NO EXCUSE ON OUR SIDE\"")
sc("""Autocar adds that the engine's task was to meet W L T P emissions with a petrol particulate filter without losing performance, and called getting a Formula One engine to idle at about twelve hundred instead of five thousand r p m a tremendous challenge. Three sources, three descriptions of the same problem. The agreement between them is the strongest evidence we have.""",
   "Mercedes-AMG engineers", "THREE SOURCES, ONE PROBLEM")
sc("""Another choice is easy to miss. Top Gear says Moers did not want the car to go racing at Le Mans, because he did not like spending heavily on a series that relied on balance of performance rules. And he said he was not interested in a speed competition, preferring the experience of driving a Formula One powertrain to chasing a top speed record.""",
   "Le Mans", "NO LE MANS · NO TOP-SPEED CHASE")
sc("""That tells you what the car is for. Moers said he was content with a top speed of three hundred fifty to four hundred kilometres per hour and a Nürburgring lap. The listed top speed is three hundred fifty-two, and the car did set Nürburgring records. By our reading, the company got what it said it wanted, even if later than promised.""",
   "Mercedes-AMG One Nürburgring", "TARGETS: ~350 KM/H AND A NÜRBURGRING LAP")

ch("Reading the engine in numbers")
sc("""Some arithmetic on the engine, clearly labelled as ours. Five hundred seventy-four metric horsepower from one point six litres is about three hundred fifty-nine horsepower per litre. The electric side adds the rest of the one thousand sixty-three total. So about fifty-four percent of the power comes from the combustion engine, and about forty-six percent from the electric side.""",
   "Mercedes F1 engine", "54% ENGINE · 46% ELECTRIC (OUR ARITHMETIC)")
sc("""And the revs. CarAdvice says the redline fell from fourteen thousand in Formula One to eleven thousand in the road car. By our arithmetic, that is about twenty-one percent lower. The idle fell by about seventy-five percent. Moderating a racing engine is not just a matter of turning it down. Every system around it has to work in a new range.""",
   "Engine rev counter", "REDLINE −21% · IDLE −75% (OUR ARITHMETIC)")
sc("""Engine life is the other half. Fifty thousand kilometres is a short life for a road car, but this is a very particular engine, handled by the company that built it. The owner does not rebuild it in a garage. The car goes back to the factory. That is a very different relationship with a manufacturer from the one most owners have.""",
   "Mercedes-AMG One workshop", "THE CAR GOES BACK TO THE FACTORY")
sc("""One more number. Wikipedia lists a combined electric range of eighteen point one kilometres. By our arithmetic, that is about eleven miles, enough to drive out of a city quietly and then switch on the engine. It is a small detail, but it shows the hybrid system is not just there for power. It also lets the car do things a Formula One car never needed to.""",
   "Mercedes-AMG One electric mode", "18.1 KM IN ELECTRIC MODE")

ch("Who bought it")
sc("""Who are the owners? CarAdvice says eight of the cars were confirmed sold to buyers in Australia and New Zealand alone. By our arithmetic, that is about three percent of the two hundred seventy-five cars, in a region far from Affalterbach. It tells you the customer list was global, and that the order book was not a local affair.""",
   "Australia and New Zealand", "8 CARS CONFIRMED FOR AUSTRALIA / NEW ZEALAND")
sc("""Top Gear also notes that customers asked Moers about racing the Project One. He said no to Le Mans, but the question itself is revealing. People who ordered the car wanted it to behave like a race car, with a race car's engine, and they were prepared to wait years for it. Patience was part of the purchase.""",
   "Mercedes-AMG One customers", "OWNERS WANTED A RACE CAR THEY COULD REGISTER")
sc("""CarAdvice adds that the company's marketing head, Bettina Fetzer, reportedly said a documentary about the car's development was in the works. That fits the story. A project that begins as a Frankfurt show car, slips by years, and ends as a record-setting machine is the kind of story a company wants to tell, even after it joked about having said yes while drunk.""",
   "Mercedes-AMG documentary", "A DEVELOPMENT DOCUMENTARY WAS IN THE WORKS")

ch("What the two secrets tell you")
sc("""Put the two secrets together. The engine needs a refurbishment at about fifty thousand kilometres, and it took years longer than promised because the idle had to drop from five thousand r p m to around twelve hundred. Both facts come from the same cause. The engine was never designed for a road, and the work was making it behave like it was.""",
   "Mercedes-AMG One", "ONE CAUSE: A RACING ENGINE ON A ROAD")
sc("""This is a pattern in extreme cars. The closer a road car stays to a racing original, the more it costs to run and the longer it takes to make legal. Mercedes chose to stay close. The reward is performance that no ordinary road car can reach. The price is time, money and maintenance, and the owners accepted it with their eyes open.""",
   "Mercedes-AMG One", "CLOSE TO RACING = COSTLY TO RUN (OUR READING)")
sc("""Was it worth it? That depends on what you value. Wikipedia reports that all two hundred seventy-five cars sold, with more than four times as many orders. By that measure, buyers decided yes. But a few people at the company, as the Källenius joke suggests, were less sure at the time. We simply report what the sources say.""",
   "Mercedes-AMG One owners", "ALL 275 SOLD")
sc("""And it was not alone. Aston Martin's Valkyrie, with a Cosworth V twelve and a hybrid system, was built by a partnership with Red Bull Racing's Adrian Newey, and arrived late too. In another video of this series we compare the two cars directly. In another, we count the real cost of an engine that needs a rebuild every fifty thousand kilometres.""",
   "Aston Martin Valkyrie", "NEXT: AMG ONE VS ASTON MARTIN VALKYRIE")
sc("""A caution. We have not driven the car, and every figure comes from the sources in the description. Where Wikipedia and CarAdvice disagree, on the idle speed and the price, we told you. We do not know the cost of the engine refurbishment, so we did not make one up. Treat our arithmetic as arithmetic, not as a measurement.""",
   "Mercedes-AMG One", "WHAT WE DON'T KNOW: REFURBISHMENT COST")
sc("""Which secret surprised you more, the fifty thousand kilometre engine or the twelve hundred r p m idle? Tell us in the comments. If you would rather spend your money on something you can drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more of the cars people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video101", "2 Secrets Hidden Inside the Mercedes-AMG One", [
    "Wikipedia, Mercedes-AMG One: https://en.wikipedia.org/wiki/Mercedes-AMG_One",
    "CarAdvice, Mercedes-AMG One delayed nine months: https://www.caradvice.com.au/news/mercedes-amg-one-delayed/",
    "CarAdvice, Mercedes CEO: We were drunk when AMG One hypercar was approved: https://www.caradvice.com.au/news/mercedes-ceo-drunk-when-amg-one-approved/",
    "Wikipedia, Aston Martin Valkyrie: https://en.wikipedia.org/wiki/Aston_Martin_Valkyrie",
], "A")
