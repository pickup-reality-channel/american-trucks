import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In May twenty twenty-one, Lamborghini's boss made a promise that sounded impossible. The brand of screaming V12s would electrify its entire lineup, cut the CO2 of its cars in half, and still build the wildest supercars in the world. Two years later, the answer rolled out of Sant'Agata Bolognese. This is why Lamborghini built the Revuelto the way it did.""",
   "Lamborghini Revuelto", "WHY LAMBORGHINI BUILT IT THIS WAY")
sc("""It is a story about a tractor maker who wanted to beat Ferrari, a company that changed owners again and again, a hybrid named after a lightning bolt, and a team of engineers who refused to put a turbocharger on their V12. And every decision they made is hidden somewhere in the shape of this car.""",
   "Lamborghini Revuelto rear", "A STORY HIDDEN IN THE SHAPE")
sc("""Every fact in this video comes from a published source, listed in the description. And to understand why the Revuelto looks the way it does, we need to start sixty years earlier, with a man who already had a successful business and decided to build cars anyway.""",
   "Lamborghini Sant'Agata", "EVERY FACT IS SOURCED")
sc("""Here is the first twist. The Revuelto is called Lamborghini's first true hybrid. But it was not Lamborghini's first hybrid. That was another car, named after a flash of lightning.""",
   "Lamborghini Sian", "NOT THE FIRST HYBRID")

# ---------- 1. FERRUCCIO ----------
ch("A tractor maker's V12")
sc("""Ferruccio Lamborghini was an industrialist. According to Wikipedia, he made tractors, boilers, and air conditioners, and his tractor company, Lamborghini Trattori, was founded in nineteen forty-eight. In nineteen sixty-three he founded Automobili Lamborghini, with a clear goal, to compete with Ferrari.""",
   "Ferruccio Lamborghini", "FERRUCCIO LAMBORGHINI, 1963")
sc("""His first series car, the three fifty G T, had a V12 designed by Giotto Bizzarrini. The chassis was developed by Gian Paolo Dallara and Paolo Stanzani. From the very first car, the V12 was the heart of the brand, and every Lamborghini built since then has come from the same town, Sant'Agata Bolognese.""",
   "Lamborghini 350 GT", "THE 350 GT")
sc("""Then came the car that changed the industry. In nineteen sixty-six, the Miura placed its V12 behind the driver, in a mid-engine, rear-wheel-drive layout. That layout became the template for what people now call a supercar. And Lamborghini started naming cars after fighting bulls, a tradition that continues with the Revuelto.""",
   "Lamborghini Miura", "1966: THE MIURA")
sc("""Then the Countach broke the rule. Named in nineteen seventy-four, its name is not a bull, but a Piedmontese expletive, according to Wikipedia. It became the poster car of a generation, with sharp edges and scissor doors that opened upward. Those doors and those edges are still in the Revuelto today.""",
   "Lamborghini Countach", "THE COUNTACH")

# ---------- 2. OWNERS ----------
ch("A company that kept changing hands")
sc("""Behind the poster cars, the company was in trouble. Wikipedia lists Ferruccio as owner until nineteen seventy-two, then Swiss investors Georges-Henri Rossetti and Rene Leimer until nineteen seventy-seven. Then came receivership, and a bankruptcy in nineteen seventy-eight.""",
   "Lamborghini Countach LP400", "BANKRUPT IN 1978")
sc("""After that, Patrick Mimran owned the company from nineteen eighty-four to nineteen eighty-seven. Then Chrysler bought it, and owned it until nineteen ninety-four. Then came Indonesian investors, through MegaTech, V'Power, and Mycom Sedtco. Through all of it, Lamborghini kept building V12 flagships, like the Diablo, named after a fighting bull.""",
   "Lamborghini Diablo", "CHRYSLER, THEN INDONESIA")
sc("""In nineteen ninety-eight, Audi, part of the Volkswagen Group, bought Lamborghini. And that brought stability and money. The Murcielago followed, then the Aventador in twenty eleven. Reports at the end of the Aventador's run, in twenty twenty-two, put its production at about eleven thousand four hundred sixty-five cars.""",
   "Lamborghini Murcielago", "AUDI, 1998")
sc("""Here is the twist. The same company that bought Lamborghini also owned Bugatti. Ferdinand Piech, the Volkswagen Group chairman who revived Bugatti, also oversaw the purchase of Lamborghini. And years later, Lamborghini would name a car after him.""",
   "Ferdinand Piech", "A CAR NAMED AFTER PIECH")

# ---------- 3. THE PROBLEM ----------
ch("The emissions problem")
sc("""By the late twenty tens, Lamborghini faced a problem that money could not simply solve. Hagerty described how new exhaust emission laws in Europe, the United Kingdom, and California were pushing the combustion engine out, and how some form of electric driving was becoming non-negotiable in those markets.""",
   "Lamborghini Aventador S", "THE EMISSIONS WALL")
sc("""Many brands answered the same problem by downsizing. Smaller engines, turbochargers, and hybrid systems. Ferrari moved much of its range to turbocharged V8s and V6 hybrids. A big naturally aspirated V12 was starting to look like a dinosaur.""",
   "V12 engine", "DOWNSIZE OR DIE?")
sc("""And the Aventador, for all its success, was aging. It used a seven-speed single-clutch automated gearbox called the I S R for more than a decade, and many reviewers found it harsh. The next flagship had to be cleaner, faster, smoother, and still unmistakably a V12 Lamborghini.""",
   "Lamborghini Aventador SVJ", "THE AGING AVENTADOR")

sc("""The Aventador itself had been a huge step when it arrived in twenty eleven, with a carbon fiber monocoque and a V12 that grew more powerful over its life, ending with the Ultimae. Its replacement had to beat the most extreme Aventador, the S V J, while also cutting emissions. That was the brief the engineers were given.""",
   "Lamborghini Aventador LP 780-4 Ultimae", "BEAT THE SVJ, CUT EMISSIONS")
# ---------- 4. THE LIGHTNING BOLT ----------
ch("The lightning bolt")
sc("""Lamborghini's first answer came in twenty nineteen. On the third of September, it revealed the Sian F K P thirty-seven, and showed it at the Frankfurt Motor Show in electric gold paint. Sian means a flash of lightning in the Bolognese dialect, according to Wikipedia.""",
   "Lamborghini Sian FKP 37", "SIAN: A FLASH OF LIGHTNING")
sc("""The name F K P thirty-seven honored Ferdinand Karl Piech, the late Volkswagen Group chairman, born in nineteen thirty-seven. And the Sian was Lamborghini's first hybrid production car. Instead of a lithium-ion battery, it stored energy in a supercapacitor, which Wikipedia says provides three times the power of a lithium battery of the same weight.""",
   "Lamborghini Sian rear", "NAMED AFTER PIECH")
sc("""The Sian's electric motor was small, a forty-eight volt unit in the gearbox adding thirty-four horsepower to a V12 of about seven hundred seventy-four. Only sixty-three coupes and nineteen roadsters were built, and all were sold. It was an experiment, proof that a Lamborghini V12 could carry electric help without losing its soul.""",
   "Lamborghini Sian Roadster", "63 COUPES, 19 ROADSTERS")
sc("""And then, in twenty twenty-one, Lamborghini used the same supercapacitor idea in another tribute car, the Countach L P I eight hundred dash four, a modern reinterpretation of the poster car from the nineteen seventies. Two limited cars tested the waters. The Revuelto would be the real thing.""",
   "Lamborghini Countach LPI 800-4", "THE NEW COUNTACH, 2021")

# ---------- 5. THE PROMISE ----------
ch("The promise")
sc("""Then came the plan. On the twenty-first of May twenty twenty-one, WardsAuto reported, Lamborghini CEO Stephan Winkelmann presented a roadmap called Direzione Cor Tauri. Cor Tauri is the brightest star in the constellation of Taurus, the bull. The plan was to electrify the entire range by the end of twenty twenty-four.""",
   "Stephan Winkelmann", "DIREZIONE COR TAURI")
sc("""Lamborghini said it would invest more than one point five billion euros over four years, the largest investment in its history. It set an internal target to cut the CO2 emissions of its products by fifty percent by the beginning of twenty twenty-five. And the first fully electric Lamborghini was planned for the second half of the decade.""",
   "Lamborghini Sant'Agata factory", "€1.5 BILLION, -50% CO2")
sc("""Winkelmann summed it up in one line. We did not want to be the first company making electric cars, but we will be the best. In other words, Lamborghini would not rush. It would electrify on its own terms, starting with the most important car in its range, the V12 flagship.""",
   "Lamborghini Aventador Ultimae", "NOT FIRST, BUT THE BEST")
sc("""Here is the twist. A plan to cut emissions in half usually means smaller engines. Lamborghini decided to do it while building a brand new V12. The answer would be a plug-in hybrid, with a battery and motors helping the V12, instead of replacing it.""",
   "Lamborghini V12 engine", "A NEW V12 TO CUT EMISSIONS")

# ---------- 6. NO TURBO ----------
ch("No turbo")
sc("""The first big decision was what not to do. Hagerty wrote that rather than downsizing or adding forced induction, like many other carmakers, Lamborghini kept a naturally aspirated V12 and made it all new. The engineers wanted the Revuelto to stay close to Lamborghini's heritage, and to that sound.""",
   "Lamborghini Revuelto engine", "NO TURBOCHARGERS")
sc("""Rouven Mohr, then head of Lamborghini's research and development, explained the changes to Hagerty. We designed a new valvetrain to increase the redline, he said. It is now set at nine thousand five hundred r p m, which was not possible with the old engine. The engine block casting is different, and the cylinder heads are different as well.""",
   "Lamborghini Revuelto V12 engine bay", "REDLINE: 9,500 RPM")
sc("""Car and Driver, via Yahoo Autos, reported that the new V12 is thirty-seven pounds lighter than the Aventador's. Hagerty listed a new intake, a new exhaust manifold, and a modified crankshaft for faster revving. So the hybrid car got a better combustion engine, not a weaker one.""",
   "Lamborghini Revuelto exhaust", "37 POUNDS LIGHTER")
sc("""And Mohr described the philosophy behind the hybrid system in one sentence. This is basically like a naturally aspirated car that is much faster. He also said there is no combustion-only mode, but that the system's basic layout is absolutely combustion-dominated. The electric motors are there to serve the V12.""",
   "Lamborghini Revuelto track", "COMBUSTION-DOMINATED")

# ---------- 7. THE PACKAGING ----------
ch("Moving everything")
sc("""The second big decision was where to put everything. The Aventador's gearbox sat in front of the engine, in the middle of the car. For the Revuelto, Lamborghini moved a new eight-speed dual-clutch gearbox behind the engine and turned it sideways. Car and Driver reported this was done to optimize the center of gravity and free up space for a working diffuser.""",
   "Lamborghini Revuelto rear diffuser", "THE GEARBOX MOVED BEHIND")
sc("""That move freed the central tunnel. Lamborghini filled it with the three point eight kilowatt hour battery, running lengthwise between the seats, like a spine. One electric motor sits on the gearbox, and two more sit at the front, one per wheel, for all-wheel drive and torque vectoring. Total output reached one thousand and one horsepower.""",
   "Lamborghini Revuelto cockpit", "THE BATTERY BECAME THE SPINE")
sc("""The engineers also worried about feel. Mohr told Hagerty that they put a lot of effort into making the boost from the electric motors linear, so the car does not feel like it suddenly jumps. And they worked on brake feel, with software deciding when the motors recover energy and when the carbon-ceramic brakes take over.""",
   "Lamborghini Revuelto brakes", "MAKING ELECTRIC FEEL NATURAL")
sc("""The body changed too. Lamborghini built a new carbon fiber monocoque that Car and Driver reported is ten percent lighter and twenty-five percent stiffer than the Aventador's. Hagerty reported that the front structure, made of Forged Composites carbon, is twenty percent lighter than the Aventador's aluminium front structure.""",
   "Lamborghini Revuelto carbon fiber", "10% LIGHTER, 25% STIFFER")

sc("""The driver controls all of this through modes. Car and Driver listed Strada, Sport, Corsa, and Ego, plus a new mode called Citta, Italian for city, that drives on electricity alone for an estimated six miles or so. Knobs on the steering wheel set both the driving mode and how the hybrid system uses its energy, recharging, holding, or spending the battery.""",
   "Lamborghini Revuelto steering wheel", "STRADA, SPORT, CORSA, CITTA")
sc("""That electric mode was not a gimmick. It answered a real problem. Some cities and regions are moving toward zones where only cars that can drive without emissions are welcome. A V12 supercar that can arrive at a hotel or leave a quiet street in electric mode fits into a world that is changing around it.""",
   "Lamborghini Revuelto city street", "A V12 THAT CAN TIPTOE")
sc("""The numbers that came out of all this were huge. Wikipedia lists zero to one hundred kilometers per hour in two point five seconds, zero to two hundred in six point six seconds, zero to three hundred in fifteen point three, and a top speed of about three hundred fifty kilometers per hour. And Car and Driver reported Lamborghini's claim that it is quicker than the Aventador S V J, on track and in a straight line.""",
   "Lamborghini Revuelto acceleration", "FASTER THAN THE SVJ")
# ---------- 8. THE DESIGN ----------
ch("The design")
sc("""Then came design. Mitja Borkert, Lamborghini's design chief, told Hagerty that the team's challenge was to design the next Lamborghini flagship, following the brand's design DNA while adding an unexpected element. Car and Driver reported that executives wanted to avoid a car that looked like a reskinned Sian.""",
   "Lamborghini Revuelto design", "MITJA BORKERT")
sc("""The result has Y-shaped lights front and rear, a nod to Lamborghini's hexagon and Y design language. The exhaust pipes sit high, between the taillights. Hagerty pointed out that this is not just for looks. It shortens the path from the cylinder heads to the outlets. And the engine bay is left open for everyone to see the V12.""",
   "Lamborghini Revuelto taillights", "Y-SHAPED LIGHTS, HIGH EXHAUSTS")
sc("""And owners shaped the interior. Hagerty wrote that customers wanted more space, and Lamborghini delivered, with a wheelbase about three inches longer and a roof about an inch taller than the Aventador. The monocoque was made bigger to fit taller drivers, and it still came out lighter.""",
   "Lamborghini Revuelto interior", "CUSTOMERS WANTED MORE SPACE")
sc("""Finally, the name. Revuelto was a Spanish fighting bull that fought in the Barcelona arena in the eighteen eighties, according to Wikipedia. After the Countach, the Sian, and other exceptions, the flagship went back to the oldest Lamborghini tradition of all, a bull's name.""",
   "Lamborghini Revuelto badge", "BACK TO A BULL'S NAME")

sc("""Inside, the Revuelto shows how much the brand changed. Car and Driver listed a twelve point three inch driver display, an eight point four inch vertical central screen, and a nine point one inch passenger screen, a first for Lamborghini. But the start button still sits under a red flap, like the switch of a fighter jet. New technology, old theater.""",
   "Lamborghini Revuelto dashboard", "NEW SCREENS, OLD THEATER")
# ---------- 9. THE REVEAL ----------
ch("The reveal")
sc("""The Revuelto was revealed online on the twenty-ninth of March twenty twenty-three. Full production started by July, and first deliveries came in the last quarter of twenty twenty-three. Motor Authority reported in July twenty twenty-three that the car was already sold out for about two years, before a single customer had driven one.""",
   "Lamborghini Revuelto reveal", "MARCH 29, 2023")
sc("""The pace of electrification followed the plan. Car and Driver's roadmap at the reveal said a hybrid Urus would follow in twenty twenty-four, then a hybrid replacement for the Huracan. Today, Lamborghini's lineup is the Revuelto, the Temerario plug-in hybrid V8, and the Urus, according to Wikipedia. The promise of Direzione Cor Tauri largely came true.""",
   "Lamborghini Temerario", "THE WHOLE RANGE ELECTRIFIED")
sc("""And sales did not suffer. In twenty twenty-four, Lamborghini delivered a record ten thousand six hundred eighty-seven cars, more than six percent above twenty twenty-three, according to duPont Registry. Wikipedia lists one thousand four hundred six Revueltos built that year. The hybrid V12 did not scare buyers away.""",
   "Lamborghini Urus", "RECORD SALES IN 2024")
sc("""The critics were impressed too. In Top Gear's twenty twenty-five Performance Car of the Year, the Revuelto beat the Ferrari twelve Cilindri and the Aston Martin Vanquish on track. Top Gear said its chassis can keep pace with its engine, and that the car is still loud and dramatic even in electric mode.""",
   "Lamborghini Revuelto track", "TOP GEAR'S TRACK WINNER")

sc("""And the car is still built the old way. Motor Authority reported that the Revuelto is largely hand-built, by around five hundred people at Sant'Agata Bolognese, the same town where every Lamborghini has been built since nineteen sixty-three, according to Hagerty. That is one reason supply stayed tight, and the waiting list stayed long.""",
   "Lamborghini Sant'Agata Bolognese factory", "500 PEOPLE, BUILT BY HAND")
sc("""Lamborghini also used the Revuelto as a canvas. Its Ad Personam department created one-off Opera Unica cars with hand-painted liveries, including one inspired by the Taurus constellation, the same constellation behind the name Direzione Cor Tauri. There was a collaboration with Ducati, and in twenty twenty-six, Revuelto Italia editions for the Winter Olympics and for the anniversary of Italian unification.""",
   "Lamborghini Revuelto Opera Unica", "A CAR FOR THE TAURUS CONSTELLATION")
sc("""The rival chose a different path. In May twenty twenty-four, Ferrari revealed the twelve Cilindri in Miami Beach, a front-engined V12 grand tourer with no hybrid system at all. Autocar reported that Ferrari invested heavily to make its biggest engine meet new emissions rules. So the two great Italian V12 brands answered the same pressure in opposite ways.""",
   "Ferrari 12Cilindri", "FERRARI WENT THE OTHER WAY")
sc("""Top Gear measured the difference in its twenty twenty-five test. Since twenty fifteen, it said, Ferrari's V12 had gained about ninety horsepower. Lamborghini's V12 car had gained about three hundred eleven, thanks to the electric motors. And on track, the Revuelto came out on top. The bet on electricity paid off in performance.""",
   "Lamborghini Revuelto vs Ferrari", "+311 HP SINCE 2015")
sc("""We compare those two cars in detail in another video of this series. But for this story, the point is simple. Lamborghini did not hybridize because it had to give up. It hybridized to win, and in the most respected comparison test of its year, it did.""",
   "Lamborghini Revuelto win", "IT HYBRIDIZED TO WIN")
# ---------- 10. NOT PERFECT ----------
ch("Not perfect")
sc("""It was not all perfect. In twenty twenty-five, AutoGuide reported a recall of twenty-seven United States Revueltos, because pins on the gas springs holding up the scissor doors could have been installed incorrectly. A door could drop suddenly, or become hard to open from inside. Dealers inspected and replaced the pins for free.""",
   "Lamborghini Revuelto doors", "THE DOOR RECALL")
sc("""And here is the twist. The scissor doors are a design element going back to the Countach of the nineteen seventies. Fifty years later, they are still one of the most complex and expensive features on the car. Tradition is part of why people buy a Lamborghini, and tradition has a cost.""",
   "Lamborghini Countach doors", "TRADITION HAS A COST")

# ---------- 11. THE SV AND THE FUTURE ----------
ch("What came next")
sc("""In August twenty twenty-six, at Monterey Car Week, Lamborghini revealed the Revuelto S V. Auto123 reported about one thousand fifty-one horsepower, eighty percent more downforce, and a lap of the Hockenheimring in one minute forty-one point six seconds, the fastest production car time there. Production is limited to one thousand nine hundred sixty-three, the year Ferruccio founded the company.""",
   "Lamborghini Revuelto SV", "THE SV: 1,963 CARS")
sc("""That number closes a circle. Sixty-three years after a tractor maker built his first V12 to compete with Ferrari, Lamborghini built its fastest V12 car ever and limited it to a number that honors his founding year. The V12 survived, and it did it by adding electricity.""",
   "Lamborghini 350 GT and Revuelto", "A CIRCLE OF 63 YEARS")
sc("""And the next step is already planned. Car and Driver's twenty twenty-three roadmap said Lamborghini's first fully electric car was due in twenty twenty-eight. When it comes, the Revuelto will be remembered as the bridge, the car that proved a Lamborghini flagship could be electrified without losing its V12.""",
   "Lamborghini Lanzador", "THE BRIDGE TO ELECTRIC")

# ---------- CLOSE ----------
ch("Why it matters")
sc("""So why did Lamborghini build the Revuelto this way? Because it had promised to cut emissions in half, and it refused to give up the naturally aspirated V12. Every unusual feature follows from those two decisions. The sideways gearbox, the battery spine, the small battery, the front electric motors, and the high-revving new engine.""",
   "Lamborghini Revuelto front view", "TWO DECISIONS, ONE CAR")
sc("""In the rest of this Revuelto series, we reveal two secrets hidden inside the car, compare it with the Ferrari twelve Cilindri, and break down what it really costs to own one. Tell us in the comments if you think Lamborghini made the right choice, or if the V12 should have stayed pure.""",
   "Ferrari 12Cilindri", "DID THEY MAKE THE RIGHT CHOICE?")
sc("""If you are shopping for something more practical than a Lamborghini, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the machines people really talk about.""",
   "Lamborghini Revuelto sunset", "SUBSCRIBE: PICKUP REALITY")

save("video68", "Why Lamborghini Built the Revuelto the Way It Did", [
    "Wikipedia, Lamborghini (history and ownership): https://en.wikipedia.org/wiki/Lamborghini",
    "Wikipedia, Lamborghini Revuelto: https://en.wikipedia.org/wiki/Lamborghini_Revuelto",
    "Wikipedia, Lamborghini Sian FKP 37: https://en.wikipedia.org/wiki/Lamborghini_Si%C3%A1n_FKP_37",
    "WardsAuto, Lamborghini Direzione Cor Tauri plan (May 2021): https://www.wardsauto.com/news/archive-wards-lamborghini-plans-all-phev-lineup-by-2025-bev-to-follow/795220/",
    "Hagerty UK, Revuelto: Aventador heir is a 1001bhp V12 plug-in (Apr 2023): https://www.hagerty.co.uk/articles/lamborghini-revuelto-aventador-heir-is-a-1001bhp-v12-plug-in/",
    "Car and Driver via Yahoo Autos, Revuelto (Mar 2023): https://autos.yahoo.com/revuelto-1001-hp-hybrid-v-131900739.html",
    "TFLcar, Aventador production ends (Sept 2022): https://tflcar.com/2022/09/lamborghini-aventador-production-ends-news/",
    "Motor Authority, Revuelto sold out for 2 years: https://www.motorauthority.com/news/1140333_lamborghini-revuelto-already-sold-out-for-next-2-years",
    "duPont Registry, Lamborghini 2024 deliveries: https://news.dupontregistry.com/blogs/lamborghini-news/lamborghini-celebrates-a-record-breaking-year-with-10687-new-car-deliveries",
    "Top Gear, PCOTY 2025: https://www.topgear.com/car-news/pcoty-2025/v12-victory-aston-martin-vanquish-vs-ferrari-12cilindri-vs-lamborghini-revuelto",
    "AutoGuide, Revuelto door recall (July 2025): https://www.autoguide.com/auto/manufacturers/lamborghini/why-these-lambo-doors-could-fall-on-your-head-or-hold-you-hostage-44623369",
    "Auto123, Revuelto SV debut (Aug 2026): https://www.auto123.com/en/news/lamborghini-revuelto-sv-debut-monterey/74145/",
], "D")
