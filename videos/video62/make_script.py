import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""One of these cars has sixteen cylinders, four turbochargers, and weighs about two tons. The other has eight cylinders, two turbochargers, and weighs about thirty percent less. One comes from a brand owned for decades by the biggest carmaker in Europe. The other comes from a man who started a car company at twenty-two. This is the Bugatti Chiron against the Koenigsegg Jesko, and the real difference between them is not the one you think.""",
   "Bugatti Chiron", "CHIRON vs JESKO")
sc("""Most comparisons stop at horsepower and top speed. But these two cars were built on opposite ideas about what a hypercar should be. One tries to make extreme speed feel calm and luxurious. The other tries to make every gram and every millisecond count.""",
   "Koenigsegg Jesko", "TWO OPPOSITE IDEAS")
sc("""In this video we go through the engines, the gearboxes, the weight, the aerodynamics, the records, and the people behind them. And at the end, we will show you the one difference that actually decides which car is better for which buyer. Every number is sourced in the description.""",
   "Koenigsegg Jesko Attack", "THE ONE DIFFERENCE THAT MATTERS")
sc("""First twist, before we even start. The Chiron is no longer in production. The last of the five hundred left the factory in May twenty twenty-four. The Jesko arrived later. So this is not a fight between two cars on sale at the same time. It is a fight between two philosophies.""",
   "Bugatti Chiron Super Sport", "NOT ON SALE AT THE SAME TIME")

# ---------- 1. TWO COMPANIES ----------
ch("Two companies")
sc("""Let's start with who built them. Bugatti, as it exists today, was revived by the Volkswagen Group. Ferdinand Piech bought the name in nineteen ninety-eight, and the Veyron and then the Chiron were built in Molsheim, France, with the resources of one of the largest carmakers on earth behind them.""",
   "Bugatti Molsheim", "BUGATTI: THE VW REVIVAL")
sc("""Koenigsegg is the opposite story. Christian von Koenigsegg founded it in Sweden in nineteen ninety-four, when he was twenty-two years old. The company started in Olofstrom, then moved to Angelholm. After a fire damaged a production building in February twenty-oh-three, Koenigsegg moved onto a former Swedish Air Force airfield.""",
   "Koenigsegg Angelholm", "KOENIGSEGG: STARTED AT 22")
sc("""That is why Koenigsegg cars carry a ghost symbol. It was the emblem of the air force squadron that used those hangars, and Koenigsegg adopted it as a tribute. Every Jesko is built in a converted hangar, with that ghost on the car.""",
   "Koenigsegg ghost logo", "THE GHOST IN THE HANGAR")
sc("""And the names tell you a lot. The Chiron is named after Louis Chiron, a racing driver from Monaco from Bugatti's golden era. The Jesko is named after Jesko von Koenigsegg, the founder's father. One looks back at a brand's history. The other is a family name.""",
   "Louis Chiron", "TWO NAMES, TWO STORIES")
sc("""Scale is the twist here. According to Wikipedia's model table, Koenigsegg had built or planned a little over eight hundred cars in total across all its models. Bugatti built five hundred Chirons alone. So a single Bugatti model is close to the size of Koenigsegg's entire history.""",
   "Koenigsegg CC8S", "ONE MODEL vs A WHOLE HISTORY")

# ---------- 2. THE ENGINES ----------
ch("The engines")
sc("""Now the engines. The Chiron uses an eight-liter W16, quad-turbocharged. That means sixteen cylinders arranged like two V8s joined together, with four turbos. The standard car makes one thousand four hundred seventy-nine horsepower and one thousand six hundred newton meters of torque.""",
   "Bugatti W16 engine", "CHIRON: 8.0L W16, 4 TURBOS")
sc("""The Jesko uses a five-liter twin-turbo V8 with a flat-plane crankshaft. On regular gasoline it makes one thousand two hundred eighty horsepower. On E eighty-five biofuel, it makes one thousand six hundred horsepower, and one thousand five hundred newton meters of torque. It revs to eight thousand five hundred r p m.""",
   "Koenigsegg V8 engine", "JESKO: 5.0L V8, 1,600 HP ON E85")
sc("""So here is the first surprise. On the right fuel, the Jesko has more horsepower than the standard Chiron, with half the cylinders and almost three liters less displacement. Even the Chiron Super Sport, at one thousand five hundred seventy-eight horsepower, comes in just below the Jesko on E eighty-five.""",
   "Koenigsegg Jesko rear", "HALF THE CYLINDERS, MORE POWER")
sc("""But the twist is fuel. That headline number depends on E eighty-five, a fuel blend that is not available at every gas station. On normal gasoline, the Jesko drops to one thousand two hundred eighty horsepower, about two hundred less than the Chiron. So the answer to which car is more powerful depends on where you fill up.""",
   "E85 fuel pump", "IT DEPENDS ON THE FUEL")
sc("""The engines also sound and feel completely different. The Chiron uses a two-stage system. Two turbos work from launch, and the other two join at about three thousand eight hundred r p m, giving peak torque from two thousand to six thousand r p m. It is designed to feel like a wave that never ends.""",
   "Bugatti Chiron engine bay", "CHIRON: A WAVE OF TORQUE")
sc("""The Jesko is designed to rev. The flat-plane crank is lighter, about five kilograms lighter than the previous Agera crank according to Wikipedia, and The Drive reported the claim that it is the lightest V8 crankshaft in the world. A high redline and a light crank make the engine react faster.""",
   "Koenigsegg Jesko engine", "JESKO: BUILT TO REV")

# ---------- 3. THE GEARBOXES ----------
ch("The gearboxes")
sc("""This is where the cars split hardest. The Chiron uses a seven-speed dual-clutch gearbox developed with Ricardo. A dual-clutch gearbox pre-selects the next gear, so shifts are fast and smooth. It is strong enough to handle sixteen hundred newton meters, all day.""",
   "Bugatti Chiron interior", "CHIRON: 7-SPEED DUAL-CLUTCH")
sc("""The Jesko uses something Koenigsegg calls the Light Speed Transmission. It has nine forward gears and, as The Drive reported, seven clutches. Instead of only pre-selecting the next gear, it can jump to almost any gear almost instantly, for example straight from seventh to second.""",
   "Koenigsegg Jesko interior", "JESKO: 9 SPEEDS, 7 CLUTCHES")
sc("""According to Wikipedia, the gearbox weighs about ninety kilograms and shifts in twenty to thirty milliseconds. And the paddles have two levels. A light pull shifts one gear. A hard pull jumps to the best gear for maximum acceleration. Koenigsegg calls it Ultimate Power On Demand.""",
   "Koenigsegg Jesko steering wheel", "ULTIMATE POWER ON DEMAND")
sc("""Here is the twist. Koenigsegg's previous big car, the Regera, had no traditional gearbox at all. It used a direct drive system with electric motors. Then, for the Jesko, Koenigsegg went the other way and built one of the most complicated gearboxes ever put in a road car. The same company solved the same problem in two opposite ways.""",
   "Koenigsegg Regera", "NO GEARBOX, THEN 9 GEARS")

# ---------- 4. WEIGHT AND GRIP ----------
ch("Weight and grip")
sc("""Now weight. Wikipedia lists the Chiron at an estimated one thousand nine hundred ninety-six kilograms. The Jesko Attack is listed at one thousand four hundred twenty kilograms with fluids, and the Jesko Absolut at one thousand three hundred ninety. That is a difference of almost six hundred kilograms, or about one thousand three hundred pounds.""",
   "Bugatti Chiron side view", "~600 KG DIFFERENCE")
sc("""Why is the Chiron so heavy? Part of it is the engine and the cooling. It has ten radiators. Part of it is all-wheel drive. And part of it is luxury. Bugatti wanted a car that could cross a continent with leather, sound insulation, and air conditioning, at speeds most cars cannot reach at all.""",
   "Bugatti Chiron cockpit", "WHY THE CHIRON IS HEAVY")
sc("""The Jesko is rear-wheel drive and has active rear-wheel steering as standard. It uses Koenigsegg's Triplex suspension, which adds a third damper to control the car as it squats and dives. And Michelin Pilot Sport Cup two tires are standard, with track-only Cup two R tires as an option.""",
   "Koenigsegg Jesko wheel", "REAR DRIVE, REAR STEER")
sc("""Then there is downforce. The Jesko Attack has a huge rear wing and front splitter. Koenigsegg claims about eight hundred kilograms of downforce at two hundred forty-nine kilometers per hour, one thousand kilograms at two hundred seventy-five, and about one thousand four hundred at top speed. That is the weight of a small car pushing it into the road.""",
   "Koenigsegg Jesko Attack rear wing", "UP TO 1,400 KG OF DOWNFORCE")
sc("""The Chiron uses its wing in a different way. In Top Speed mode it hides much of its aero to cut drag, and under hard braking the wing stands up as an air brake. In Bugatti's zero to four hundred to zero test, the wing went to forty-nine degrees and added about nine hundred kilograms of rear downforce while stopping.""",
   "Bugatti Chiron rear wing", "A WING THAT BRAKES")
sc("""The twist on grip is this. There are actually two Jeskos. The Attack is the downforce car for tracks. The Absolut is the low-drag car for top speed. It replaces the big wing with two rear fins, and its downforce drops to about one hundred fifty kilograms, with a drag coefficient of zero point two seven eight. Koenigsegg built two different answers inside one model name.""",
   "Koenigsegg Jesko Absolut", "TWO JESKOS IN ONE")

# ---------- 5. THE SPEED WAR ----------
ch("The speed war")
sc("""Now the question everyone asks. Which one is faster? Let's go through the record history, because it is a story of the two brands taking turns. In twenty seventeen, Bugatti set a zero to four hundred to zero record with the Chiron, at forty-one point nine six seconds, with Juan Pablo Montoya driving.""",
   "Bugatti Chiron on track", "2017: CHIRON, 41.96 S")
sc("""Weeks later, Koenigsegg answered. Top Gear reported that the Agera RS beat the Chiron's zero to four hundred to zero time by more than five seconds. Then, on the fourth of November twenty seventeen, on a closed stretch of Nevada highway between Las Vegas and Pahrump, the Agera RS averaged two hundred seventy-seven point nine miles per hour in two directions.""",
   "Koenigsegg Agera RS", "2017: AGERA RS, 277.9 MPH")
sc("""Then came Bugatti's response. On the second of August twenty nineteen, at Ehra-Lessien, Andy Wallace drove a pre-production Chiron Super Sport three hundred plus to three hundred four point seven seven three miles per hour. It was the first car of its kind past three hundred.""",
   "Ehra-Lessien", "2019: CHIRON, 304.773 MPH")
sc("""But here is the detail that matters. Bugatti's run was in one direction. Koenigsegg's Nevada record was an average of two runs in opposite directions, which is the traditional way to cancel out wind and slope. So each brand can say it holds a different kind of record, and both are telling the truth.""",
   "Bugatti Chiron Super Sport 300+", "ONE WAY vs TWO WAYS")
sc("""After that, Bugatti's president said the company would stop chasing top speed records. And Koenigsegg's answer was the Jesko Absolut. Its maker estimates about five hundred kilometers per hour, and simulations shared by Koenigsegg put the theoretical figure around three hundred thirty miles per hour.""",
   "Koenigsegg Jesko Absolut rear", "JESKO ABSOLUT: 330 MPH IN THEORY")
sc("""But there is a big twist. As of the reports we found, that top speed has not been proven in a real run. Koenigsegg itself called the three hundred thirty figure a theoretical number, and said finding a road or track long and smooth enough is the hard part. The Absolut's fastest numbers are still on paper.""",
   "Koenigsegg Jesko Absolut blue", "STILL ON PAPER")
sc("""Where the Jesko has proven itself is acceleration. On the twenty-sixth of June twenty twenty-four, at Orebro airport in Sweden, a Jesko Absolut ran zero to four hundred to zero kilometers per hour in twenty-seven point eight three seconds. Then, on the seventh of August twenty twenty-five, it improved to twenty-five point two one seconds.""",
   "Koenigsegg Jesko Absolut track", "25.21 SECONDS")
sc("""Compare that with the Chiron's forty-one point nine six seconds in twenty seventeen. The Jesko cut more than sixteen seconds. That is not a small win. And it tells you exactly what each car was optimized for. One for top speed with comfort, the other for violent acceleration with low weight.""",
   "Bugatti Chiron vs Koenigsegg", "16 SECONDS FASTER")
sc("""There is also the racetrack. Wikipedia lists the Jesko Attack at two minutes fifty-six point nine seven seconds at the Gotland Ring in Sweden, and one minute twenty-four point eight six at Laguna Seca. Bugatti never built the standard Chiron for lap records. For corners it created the Pur Sport, about fifty kilograms lighter with a higher redline.""",
   "Laguna Seca", "THE JESKO OWNS THE CORNERS")

# ---------- 6. MONEY AND RARITY ----------
ch("Money and rarity")
sc("""Now rarity. Bugatti built five hundred Chirons in many versions, from the base car to one-offs. Koenigsegg plans one hundred twenty-five Jeskos, built at about forty to fifty per year, plus a separate run of thirty Sadair's Spear cars. Every Jesko build slot was sold by March twenty nineteen, right after the Geneva reveal.""",
   "Koenigsegg Jesko orange", "500 vs 125")
sc("""Price is harder to compare, because Koenigsegg does not quote list prices the way a normal brand does, and options change everything. The Chiron launched at two point four million euros before options. Special Chirons went much higher, like the Super Sport three hundred plus at three point five million euros before tax.""",
   "Bugatti Chiron price", "CHIRON FROM €2.4 MILLION")
sc("""And the twist is what happened later. A one-off Chiron Profilee sold at auction in Paris in February twenty twenty-three for nine million seven hundred ninety-two thousand five hundred euros, which Hagerty called a record for a new car at auction. Rarity, not speed, set the highest price ever paid for a Chiron.""",
   "Bugatti Chiron Profilee", "RARITY BEAT SPEED")
sc("""Ownership costs are also different in style. Chiron owner Steve Hamilton reported an annual service of about eleven thousand five hundred dollars, and The Drive listed a replacement engine at about eight hundred fifty-six thousand dollars. A Jesko has a smaller engine and fewer cylinders, but it is built in tiny numbers by a small company, and parts are made in small batches.""",
   "Bugatti Chiron service", "OWNERSHIP IS NOT CHEAP")

# ---------- 6b. FROM REVEAL TO DELIVERY ----------
ch("From reveal to delivery")
sc("""Here is a difference almost nobody talks about. Time. The Chiron was revealed at the Geneva Motor Show on the first of March twenty sixteen, and the first three customer cars were delivered in March twenty seventeen, about a year later. By then, according to Wikipedia, the first two hundred cars had already been sold.""",
   "Bugatti Chiron Geneva 2016", "CHIRON: REVEAL TO DELIVERY IN 1 YEAR")
sc("""The Jesko was revealed at Geneva in March twenty nineteen. Koenigsegg showed a pre-series car in July twenty twenty-one, and the first customer car was delivered in June twenty twenty-three. That is more than four years from reveal to the first delivery, in the middle of a pandemic and a global parts shortage.""",
   "Koenigsegg Jesko Geneva 2019", "JESKO: MORE THAN 4 YEARS")
sc("""That gap says a lot about the two companies. Bugatti could lean on the testing facilities, suppliers, and engineering teams of a giant group. Koenigsegg develops a huge share of its technology in-house, from the engine to the gearbox, and The Drive reported that the Jesko's crankshaft is milled by a small manufacturer in southern Sweden.""",
   "Koenigsegg factory", "A GIANT vs A SMALL TEAM")
sc("""And here is the twist. The slower company built the more radical car. The Light Speed Transmission, the flat-plane crank, and the Triplex suspension are Koenigsegg's own ideas. The Chiron is an evolution of the Veyron's formula, with the same displacement and the same number of turbos, but almost every part redesigned. One brand perfected an idea. The other kept reinventing.""",
   "Koenigsegg Jesko gearbox", "PERFECT vs REINVENT")

# ---------- 6c. THE SPECIAL VERSIONS ----------
ch("The special versions")
sc("""Both cars also spawned special versions, and they reveal what each brand values. Bugatti's specials were mostly about design, materials, and stories. The Chiron Noire was a tribute to the nineteen thirty-six Type fifty-seven S C. The Les Legendes du Ciel cars honored early aviators. And the Sport one hundred ten Ans celebrated Bugatti's anniversary.""",
   "Bugatti Chiron Sport 110 ans", "BUGATTI: SPECIALS FOR STORIES")
sc("""Bugatti did build performance specials too. The Pur Sport, sixty cars, was built for handling, with a higher redline of six thousand nine hundred r p m and about fifty kilograms less weight. The Super Sport, eighty cars, had a longer tail and a limit of four hundred forty kilometers per hour.""",
   "Bugatti Chiron Pur Sport", "PUR SPORT AND SUPER SPORT")
sc("""Koenigsegg's special Jesko is the Sadair's Spear, limited to thirty cars. It is named after a horse that Jesko von Koenigsegg rode in his final race as a jockey. Wikipedia lists it at up to one thousand six hundred twenty-five horsepower on E eighty-five, and its top speed is lowered to about three hundred sixty kilometers per hour for track work.""",
   "Koenigsegg Jesko Sadair's Spear", "THE SADAIR'S SPEAR")
sc("""And it was faster on track. Wikipedia says the Sadair's Spear lapped the Gotland Ring one point one seconds quicker than the Jesko Attack. So even Koenigsegg's special edition is defined by a stopwatch, while many of Bugatti's are defined by a color, a material, or a tribute.""",
   "Gotland Ring", "DEFINED BY A STOPWATCH")

# ---------- 6d. THE RECORDS THEY BEAT ----------
ch("The records they beat")
sc("""To understand why speed records matter so much to these two brands, look at what came before. In twenty ten, the Bugatti Veyron Super Sport averaged two hundred sixty-nine point eight six miles per hour at Ehra-Lessien. In twenty fourteen, the Hennessey Venom G T hit two hundred seventy point four nine in one direction at the Kennedy Space Center in Florida.""",
   "Hennessey Venom GT", "THE RECORDS BEFORE THEM")
sc("""Then the Agera RS changed the game in Nevada. Top Gear reported that it was a customer car, driven by Koenigsegg test driver Niklas Lilja on an eleven-mile closed stretch of Highway one sixty. One run reached two hundred eighty-four point five five miles per hour. The other, uphill and into a headwind, reached two hundred seventy-one point one nine.""",
   "Nevada State Route 160", "284.55 MPH ONE WAY")
sc("""So when Bugatti came back in twenty nineteen with three hundred four miles per hour, it was answering a challenge from Sweden. And when Koenigsegg built the Jesko Absolut, it was answering that answer. This back and forth pushed both cars further than either brand might have gone alone.""",
   "Bugatti Chiron Super Sport 300+ orange", "A RIVALRY THAT PUSHED BOTH")

# ---------- 7. WHO OWNS THEM NOW ----------
ch("Who owns the brands now")
sc("""There is one more difference that most comparisons miss, and it is about the companies. In twenty nineteen, Koenigsegg sold a twenty percent stake to the Chinese-backed company NEVS for one hundred seventy-one million dollars. In twenty twenty-one, it bought that stake back. Today the company is again fully independent.""",
   "Christian von Koenigsegg", "KOENIGSEGG: INDEPENDENT")
sc("""Bugatti went the other way. In twenty twenty-one, Volkswagen moved Bugatti into a joint venture with the Croatian electric car maker Rimac. Rimac held fifty-five percent and Porsche forty-five. Then, in September twenty twenty-six, Carscoops reported that a group of investors bought Porsche's stakes, and Mate Rimac became Bugatti's president.""",
   "Mate Rimac", "BUGATTI: NOW RUN BY RIMAC")
sc("""So the twist is that today, both of these brands are run by a founder figure from a small country. A Swede who started at twenty-two, and a Croatian who founded his own electric car company and now runs the most famous hypercar brand in the world. The Volkswagen era of Bugatti, the era that created the Chiron, is over.""",
   "Bugatti Tourbillon", "TWO FOUNDERS, TWO SMALL COUNTRIES")
sc("""And the next battle has already started. Bugatti's successor, the Tourbillon, uses a naturally aspirated V16 with three electric motors and about one thousand seven hundred seventy-five horsepower. Koenigsegg has said the Absolut is the fastest Koenigsegg it will ever try to make. Both brands are stepping away from the pure top speed war, in different directions.""",
   "Bugatti Tourbillon rear", "THE NEXT ROUND")

# ---------- 8. THE REAL DIFFERENCE ----------
ch("The real difference")
sc("""So what is the difference nobody explains? It is not horsepower, because the winner depends on the fuel. It is not top speed, because the records were set in different ways and the Jesko's highest number is still theoretical.""",
   "Bugatti Chiron front", "NOT HORSEPOWER, NOT SPEED")
sc("""The real difference is what each car does with its power. The Chiron uses its mass, its all-wheel drive, and its cooling to make extreme speed feel calm. It is a grand tourer that can touch two hundred sixty-one miles per hour in comfort, with a key to unlock it.""",
   "Bugatti Chiron highway", "CHIRON: SPEED MADE CALM")
sc("""The Jesko uses its lightness, its gearbox, and its downforce to make every input feel immediate. It is a car that wants a racetrack or a runway, and it proved it by cutting more than sixteen seconds from the Chiron's zero to four hundred to zero time.""",
   "Koenigsegg Jesko Attack track", "JESKO: SPEED MADE VIOLENT")
sc("""So if you wanted the most refined way to travel at a speed almost no one else can reach, the Chiron is the answer. If you wanted the most extreme driving machine with a license plate, the Jesko is the answer. They are both hypercars. They are not trying to win the same test.""",
   "Koenigsegg Jesko and Bugatti Chiron", "THEY ARE NOT TAKING THE SAME TEST")
sc("""Tell us in the comments which one you would pick, and why. And watch the other videos in this Chiron series, where we look at two little-known facts about the car, what it really costs to own one, and the full story of how it was made.""",
   "Bugatti Chiron blue", "WHICH ONE WOULD YOU PICK?")
sc("""If you are shopping for something more practical, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the machines people really talk about.""",
   "Koenigsegg Jesko front", "SUBSCRIBE: PICKUP REALITY")

save("video62", "Bugatti Chiron vs Koenigsegg Jesko: The Difference Nobody Explains", [
    "Wikipedia, Bugatti Chiron: https://en.wikipedia.org/wiki/Bugatti_Chiron",
    "Wikipedia, Koenigsegg Jesko: https://en.wikipedia.org/wiki/Koenigsegg_Jesko",
    "Wikipedia, Koenigsegg (company history, models, ownership): https://en.wikipedia.org/wiki/Koenigsegg",
    "The Drive, Koenigsegg Jesko reveal (Mar 2019): https://www.thedrive.com/news/26777/koenigsegg-jesko-a-swedish-megacar-with-1600-hp-seven-clutches-and-300-mph-top-speed",
    "AOL / Motor1, Jesko Absolut can do 330 mph in theory: https://www.aol.com/news/koenigsegg-jesko-absolut-330-mph-182000829.html",
    "Top Gear, Koenigsegg Agera RS 277.9 mph record (Nov 2017): https://www.topgear.com/car-news/supercars/koenigsegg-has-smashed-worlds-fastest-car-record",
    "Bugatti newsroom, 0-400-0 km/h in 42 seconds (Sept 2017): https://newsroom.bugatti.com/press-releases/0-400-0-km-h-in-42-seconds-bugatti-chiron-sets-world-record",
    "Autocar, Chiron goes 304mph: https://www.autocar.co.uk/car-news/new-cars/bugatti-chiron-goes-304mph-set-hypercar-record",
    "Motor1, Bugatti retires from speed records: https://www.motor1.com/news/368539/bugatti-retires-chasing-speed-records/",
    "Motor Authority, Chiron W16 engine: https://www.motorauthority.com/news/1102657_a-close-look-at-the-bugatti-chiron-s-monster-w-16-engine",
    "Hagerty UK, Chiron Profilee auction: https://www.hagerty.co.uk/articles/bugatti-chiron-profilee-record-breaking/",
    "The Drive, Chiron maintenance costs: https://www.thedrive.com/news/heres-what-it-cost-to-maintain-a-bugatti-chiron-over-10-years",
    "Motor1, Rimac and Bugatti (55/45 split): https://www.motor1.com/news/755654/rimac-complete-control-bugatti/",
    "Carscoops, Rimac finalizes Bugatti takeover (Sept 2026): https://carscoops.com/2026/09/rimac-finalizes-bugatti-takeover-ending-all-vw-ownership",
    "Car Throttle, Bugatti Tourbillon: https://www.carthrottle.com/news/bugatti-tourbillon-1775bhp-v16-salute-combustion",
], "B")
