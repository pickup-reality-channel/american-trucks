import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In twenty ten, Ferrari's chairman stood at the Geneva Motor Show next to a green Ferrari and promised that hybrid versions of all its models would arrive within three or four years. It did not happen. It took almost a decade, a hypercar, the death of the company's most powerful boss, and a new chief executive from a tobacco company before Ferrari finally built its first plug-in hybrid.""",
   "Ferrari 599 HY-KERS", "THE INSANE STORY OF FERRARI'S FIRST PLUG-IN")
sc("""That car was the SF90 Stradale. Almost one thousand horsepower, three electric motors, and a battery you plug into the wall. Today, about half of the cars Ferrari delivers are hybrids. But the road from that green concept to the SF90 was much stranger than most people know.""",
   "Ferrari SF90 Stradale", "FROM CONCEPT TO SF90")
sc("""This is the story of how the most traditional sports car brand in the world learned to plug in. Every date and number comes from a published source, and the list is in the description.""",
   "Ferrari Maranello gate", "EVERY DATE IS SOURCED")
sc("""And here is the first twist. The technology that started this story did not come from Ferrari's road car engineers. It came from Formula One, from a rule change that many fans did not even like.""",
   "Ferrari Formula One 2009", "IT STARTED IN FORMULA ONE")

# ---------- 1. KERS ----------
ch("Formula One's battery")
sc("""In two thousand nine, Formula One allowed teams to use K E R S, the kinetic energy recovery system. Under braking, a motor captured some of the car's energy and stored it. Then the driver could press a button for a short burst of extra power. Driven, a New Zealand outlet, describes the LaFerrari's hybrid system as inspired by that F1 technology.""",
   "Ferrari F60 Formula One", "2009: KERS IN FORMULA ONE")
sc("""For Ferrari, this was more than a racing rule. It forced its engineers to learn how to package batteries, electric motors, and control electronics into a car where every kilogram and every centimeter matter. That knowledge would soon move from the race track to the road.""",
   "Ferrari Formula One pit", "LEARNING TO PACKAGE BATTERIES")
sc("""And it worked on track. In twenty nine, Kimi Raikkonen won the Belgian Grand Prix at Spa for Ferrari, in a car using K E R S, the team's only win that season. The system was not used in twenty ten, after teams agreed to drop it, and it returned in twenty eleven. But the lesson stayed in Maranello.""",
   "Kimi Raikkonen Ferrari 2009 Spa", "SPA 2009: A KERS FERRARI WINS")
sc("""From twenty fourteen, Formula One went further, with turbocharged one point six liter V6 engines combined with powerful hybrid systems. Every Ferrari race car from then on was a hybrid. So by the time Ferrari's road cars went hybrid, its racing engineers had been living with batteries and electric motors for years.""",
   "Ferrari Formula One 2014", "2014: F1 GOES FULL HYBRID")
sc("""And it came at a time when the pressure on carmakers was growing. Emission rules were becoming stricter, and governments were asking even small, luxury brands to cut carbon dioxide. A Ferrari with a big V12 was exactly the kind of car regulators were watching.""",
   "Ferrari V12 engine", "PRESSURE TO CUT EMISSIONS")

# ---------- 2. THE GREEN CONCEPT ----------
ch("The green concept")
sc("""So at the Geneva Motor Show in March twenty ten, Ferrari showed a test car. It was a five ninety-nine G T B Fiorano, the front-engined V12 grand tourer, fitted with a hybrid system. Ferrari called it the five ninety-nine HY dash KERS, a Vettura Laboratorio, which means a laboratory car.""",
   "Ferrari 599 GTB Fiorano HY-KERS", "2010: THE 599 HY-KERS")
sc("""CAR Magazine reported the details. Flat lithium-ion batteries sat under the floor, keeping the weight low. An electric motor of about forty kilograms, producing more than one hundred horsepower, was mounted on the back of the seven-speed dual-clutch gearbox. Ferrari's target was one extra horsepower for every kilogram the hybrid system added.""",
   "Ferrari 599 HY-KERS detail", "40 KG MOTOR, 100+ HP")
sc("""Motor Authority reported that Ferrari claimed the system could cut carbon dioxide emissions by as much as thirty-five percent on the European combined cycle, compared with a normal five ninety-nine. It could give short bursts of power when accelerating or overtaking, and even drive the car on electricity alone for brief moments.""",
   "Ferrari 599 GTB Fiorano", "UP TO 35% LESS CO2")
sc("""CAR Magazine added an important detail. Ferrari said the hybrid system added little weight compared with a normal V12 five ninety-nine, and that the car's center of gravity was even lower than the petrol model's, because the batteries sat so low. For Ferrari, this was the key. A hybrid did not have to make the car worse to drive.""",
   "Ferrari 599 GTB Fiorano side", "A LOWER CENTER OF GRAVITY")
sc("""Ferrari was careful to call it strictly a concept. But its chairman at the time, Luca di Montezemolo, went further. AutoGuide reported that he said Ferrari planned to offer hybrid versions of all of its models in the next three or four years. He called the car the start of a long project.""",
   "Luca di Montezemolo", "HYBRIDS FOR ALL MODELS?")
sc("""Here is the twist. That promise would have meant hybrid Ferraris across the range by about twenty fourteen. Instead, the first Ferrari hybrid would arrive in twenty thirteen as one very exclusive hypercar, and the first plug-in hybrid series car would not arrive until twenty nineteen. The long project turned out to be very long indeed.""",
   "Ferrari 599 HY-KERS rear", "THE PROMISE THAT TOOK A DECADE")

# ---------- 3. LAFERRARI ----------
ch("LaFerrari")
sc("""The first production Ferrari hybrid was not a family-friendly Ferrari at all. It was LaFerrari, unveiled in twenty thirteen. Driven lists five hundred coupes, and later two hundred ten open Aperta versions, built from twenty thirteen to twenty sixteen. It was the successor to the Enzo, the most extreme Ferrari of its time.""",
   "Ferrari LaFerrari", "2013: LAFERRARI")
sc("""LaFerrari used a big naturally aspirated V12 with an electric motor, a hybrid system Ferrari also called HY dash KERS, the same name as the green concept. But it was not a plug-in. The battery was charged by the car itself, under braking and from the engine, just like in Formula One.""",
   "Ferrari LaFerrari engine", "HY-KERS, BUT NO PLUG")
sc("""The numbers were wild for twenty thirteen. LaFerrari combined a six point three liter V12 of about eight hundred metric horsepower with an electric motor of about one hundred sixty-three, for a total of about nine hundred sixty-three. It was the most powerful road car Ferrari had built until then, and it used the battery for performance, not for silent driving.""",
   "Ferrari LaFerrari side", "963 CV FROM V12 + MOTOR")
sc("""And here is the twist. That same year, McLaren launched its own hybrid hypercar, the P1, built in a run of three hundred seventy-five cars, according to Wikipedia. Porsche had the nine eighteen Spyder. Three rival brands had all reached the same conclusion. The fastest road cars of the future would be hybrids.""",
   "McLaren P1 and LaFerrari", "P1, 918, LAFERRARI")
sc("""But LaFerrari was a tiny run of cars for a tiny group of buyers. It proved that Ferrari could make a hybrid that people wanted. It did not change the cars most Ferrari customers actually bought. For that, Ferrari needed something else.""",
   "Ferrari LaFerrari Aperta", "ONLY 710 CARS")
sc("""There was also a technical gap. LaFerrari's battery was small and designed for bursts of power, not for driving on electricity. To build a plug-in hybrid that could cover several kilometers in silence, Ferrari needed a larger battery, a charging system, and motors strong enough to move the car by themselves. That meant starting much of the hybrid system from scratch.""",
   "Ferrari LaFerrari rear", "A DIFFERENT KIND OF HYBRID")

# ---------- 4. MARCHIONNE ----------
ch("The Marchionne years")
sc("""By then, Ferrari had a powerful new boss. Sergio Marchionne, who also ran Fiat Chrysler, became Ferrari's chairman in twenty fourteen, after Montezemolo left. He was famous for his black sweaters, his long working hours, and his ambition to grow Ferrari's profits.""",
   "Sergio Marchionne", "SERGIO MARCHIONNE")
sc("""Under Marchionne, Ferrari was listed on the New York Stock Exchange in October twenty fifteen, under the ticker R A C E, and was then separated from Fiat Chrysler, according to Wikipedia. Ferrari was no longer just a car company. It was a public company with investors who expected growth.""",
   "New York Stock Exchange", "2015: FERRARI GOES PUBLIC")
sc("""Growth meant more cars, and more cars meant more emissions to manage. A plug-in hybrid series car made sense on both sides. It could be faster than a normal Ferrari, which pleased customers, and it could cut official emissions, which pleased regulators. The idea from twenty ten was finally becoming urgent.""",
   "Ferrari production line", "GROWTH NEEDED HYBRIDS")
sc("""Inside Maranello, the engineers had a clear path. Ferrari's mid-engined V8 sports car had already moved to turbocharging with the four eighty-eight G T B of twenty fifteen. The next step was to add electric motors to that V8 and make the car plug-in. That combination would become the heart of the SF90.""",
   "Ferrari 488 GTB", "TURBO V8, THEN HYBRID")
sc("""Then came the shock. In July twenty eighteen, Ferrari announced that Marchionne would be unable to return to work, after complications following shoulder surgery. Autosport reported that he died a few days later, at the age of sixty-six. Ferrari had lost its leader at one of the most important moments in its history.""",
   "Ferrari flag Maranello", "JULY 2018: MARCHIONNE DIES")

# ---------- 5. CAMILLERI ----------
ch("A new boss")
sc("""His replacement surprised many people. Bloomberg reported that Ferrari chose Louis Camilleri, a veteran of Philip Morris, the tobacco company behind the Marlboro brand, which had sponsored Ferrari in Formula One for decades. John Elkann, from the Agnelli family, became chairman.""",
   "Louis Camilleri Ferrari", "THE TOBACCO EXECUTIVE")
sc("""Just two months later, in September twenty eighteen, Camilleri and Elkann presented Ferrari's plan to investors at a capital markets day. ANSA reported that Ferrari would launch fifteen new models between twenty nineteen and twenty twenty-two, and that Camilleri expected around sixty percent of Ferrari's cars to be hybrids by the end of the plan.""",
   "Ferrari capital markets day", "SEPT 2018: 15 NEW MODELS")
sc("""Motor1 reported that Elkann said Marchionne had played a fundamental role in making this future possible. Ferrari's chief technology officer, Michael Leiters, explained the engine technology. And ANSA said the plan also included the Purosangue, which Camilleri insisted should not be called an S U V.""",
   "Ferrari Purosangue", "THE PLAN AFTER MARCHIONNE")
sc("""The capital markets day also showed how fast Ferrari wanted to move. At its close, ANSA reported, Ferrari unveiled the Monza S P one and S P two, open-top limited series cars inspired by classic racing Ferraris. Old-school V12 roadsters on the same stage as a hybrid plan. It was a perfect picture of a company trying to keep its past while changing its future.""",
   "Ferrari Monza SP2", "MONZA SP1 AND SP2")
sc("""Here is the twist. Sixty percent hybrids by twenty twenty-two was an enormous change for Ferrari, a brand built on the sound of its engines. And the first car of this new era would have to convince the most traditional customers in the world. That car was the SF90.""",
   "Ferrari SF90 Stradale red", "60% HYBRIDS?")

# ---------- 6. THE REVEAL ----------
ch("The reveal")
sc("""On the twenty-ninth of May twenty nineteen, in Maranello, Ferrari unveiled the SF90 Stradale. The name honored ninety years of Scuderia Ferrari. Reuters reported that Camilleri called it astounding, fast, and completely revolutionary, and that about two thousand selected customers were invited to see it and reserve one.""",
   "Ferrari SF90 Stradale reveal", "MAY 29, 2019: SF90 REVEALED")
sc("""Reuters called it Ferrari's first hybrid for wider production, and InsideEVs called it the first series production plug-in hybrid Ferrari. A four liter twin-turbo V8, three electric motors, and a seven point nine kilowatt hour battery, for about one thousand metric horsepower in total.""",
   "Ferrari SF90 Stradale engine", "1,000 CV PLUG-IN HYBRID")
sc("""Look how the green concept's ideas came back. The batteries sat low in the chassis. An electric motor sat at the back, between the engine and the gearbox. But now there were two more motors at the front, giving the car electric all-wheel drive, and a plug to charge the battery from the grid.""",
   "Ferrari SF90 chassis", "THE CONCEPT'S IDEAS RETURN")
sc("""The car could even drive on electricity alone. InsideEVs reported up to about twenty-five kilometers of electric range in eDrive mode, using only the front motors, at up to about one hundred thirty-five kilometers per hour. And it had no reverse gear at all. Its front electric motors moved it backward.""",
   "Ferrari SF90 Stradale city", "25 KM ON ELECTRICITY")
sc("""The cabin changed too. Autobuzz, reporting Ferrari's launch details, described a sixteen-inch curved digital display behind the wheel, controlled with touch pads and haptic buttons on the steering wheel, and no central infotainment screen. And the gear selector on the center tunnel was styled after the metal gate of Ferrari's old manual gearboxes. Past and present in the same car.""",
   "Ferrari SF90 interior", "16-INCH SCREEN, CLASSIC GATE")
sc("""Ferrari also offered a track version from the start, the Assetto Fiorano package, with special shock absorbers, carbon fiber parts, and a titanium exhaust. Wikipedia says it saves about thirty kilograms. CarGurus later listed it at about fifty thousand dollars in America. Even Ferrari's first plug-in had a hardcore option.""",
   "Ferrari SF90 Assetto Fiorano", "ASSETTO FIORANO PACKAGE")
sc("""Here is the twist that made the traditional customers listen. The SF90 was faster than LaFerrari. Wikipedia says it was, as of twenty twenty, the fastest Ferrari road car ever around the Fiorano test track, seven tenths of a second quicker than the hybrid hypercar. A plug-in series car had beaten the brand's flagship.""",
   "Fiorano circuit", "FASTER THAN LAFERRARI")
sc("""For Ferrari's customers, that was the argument that mattered. Nobody had to be told that a hybrid was good for the planet or good for regulations. They only had to see the lap time. A Ferrari with a plug was faster than the hypercar many of them could never buy. The battery had become a performance part.""",
   "Ferrari SF90 Stradale track", "THE BATTERY AS A PERFORMANCE PART")

# ---------- 7. THE TURBULENCE ----------
ch("Turbulence")
sc("""Then the world changed. The SF90's deliveries began as the coronavirus pandemic spread. And on the tenth of December twenty twenty, Ferrari announced that Camilleri had resigned, effective immediately, for personal reasons, The Race reported. John Elkann became interim chief executive.""",
   "Ferrari Maranello headquarters", "DEC 2020: CAMILLERI RESIGNS")
sc("""So in just over two years, Ferrari had lost Marchionne, gained Camilleri, launched its first plug-in hybrid, and lost Camilleri too. The SF90 was born in one of the most unstable periods in the company's modern history.""",
   "Ferrari SF90 Stradale yellow", "THREE BOSSES IN TWO YEARS")
sc("""And here is a twist few people noticed. Michael Leiters, the chief technology officer who had presented Ferrari's engine plans in twenty eighteen, later left Maranello. Road and Track reported in twenty twenty-two that he had become the chief executive of McLaren, Ferrari's old rival, which was then struggling with the launch of its own plug-in hybrid, the Artura.""",
   "McLaren Artura", "FERRARI'S CTO GOES TO McLAREN")
sc("""In twenty twenty-one, Ferrari named a new chief executive, Benedetto Vigna, who came from the semiconductor industry rather than the car industry, according to Wikipedia. It was another sign that the future of Ferrari would be about electronics and software, as much as engines.""",
   "Benedetto Vigna Ferrari", "A CHIP EXPERT IN CHARGE")
sc("""And the SF90 had its own problems. In October twenty twenty-three, Motor Authority reported a recall of six hundred fourteen SF90s in the United States, because turbo oil delivery pipes could leak and cause a fire. Owners were told not to drive their cars until the pipes were replaced. The trouble, ironically, was in the old-fashioned part of the car, the turbo engine.""",
   "Ferrari SF90 engine bay", "2023 RECALL: 614 CARS")

# ---------- 8. THE FAMILY GROWS ----------
ch("The family grows")
sc("""Despite the turbulence, the SF90 family kept growing. There was the SF90 Spider, which Wikipedia calls Ferrari's first plug-in hybrid convertible. Then in twenty twenty-three came the SF90 X X Stradale and X X Spider, with about one thousand sixteen horsepower. Evo India called it the first road-legal model in Ferrari's X X program.""",
   "Ferrari SF90 XX Stradale", "SPIDER, THEN XX")
sc("""Ferrari also launched a smaller plug-in hybrid, the two ninety-six G T B, with a V6 instead of a V8. And in October twenty twenty-four, it revealed the F eighty hypercar, the successor to LaFerrari, with a hybrid V6 and a production run of seven hundred ninety-nine cars, according to Wikipedia.""",
   "Ferrari F80", "296 GTB, THEN F80")
sc("""So the hybrid idea now ran through the whole range, from the smaller V6 sports car to the hypercar at the top. Montezemolo's twenty ten promise of hybrids for every model had not happened in three or four years. But more than a decade later, it was close to reality.""",
   "Ferrari 296 GTB and SF90", "THE PROMISE, FINALLY")
sc("""And the numbers proved it. Motor Authority reported that Ferrari delivered a record thirteen thousand seven hundred fifty-two cars in twenty twenty-four, and that fifty-one percent of them were hybrids. For the first time, hybrids made up more than half of Ferrari's deliveries.""",
   "Ferrari delivery center", "2024: 51% HYBRIDS")
sc("""Think about that. In twenty nineteen, Ferrari had no plug-in hybrid series car. Five years later, more than half of its deliveries were hybrids, and the brand still set a delivery record. The fear that customers would reject electric motors in a Ferrari had turned out to be wrong.""",
   "Ferrari SF90 Stradale and 296 GTB", "CUSTOMERS SAID YES")

# ---------- 9. THE END AND THE NEXT ----------
ch("The end and the next step")
sc("""The SF90's time at the top was short. On the tenth of September twenty twenty-five, Motoring Research reported, Ferrari revealed the eight forty-nine Testarossa as its replacement. It keeps the same basic layout, a twin-turbo V8 and three electric motors, with about one thousand fifty horsepower combined.""",
   "Ferrari 849 Testarossa", "2025: 849 TESTAROSSA")
sc("""It brought back two things from the past. One is the Testarossa name, from the famous Ferrari of the nineteen eighties. The other is physical buttons. Motoring Research reported that the eight forty-nine returned to physical switches on the steering wheel, instead of the SF90's haptic touch controls. Not every new idea from the SF90 survived.""",
   "Ferrari Testarossa 1984", "THE TESTAROSSA NAME RETURNS")
sc("""And then came the biggest step of all. Ferrari's first fully electric car, the Luce. Electra's summary says Ferrari showed the technology in October twenty twenty-five, revealed the name and interior in San Francisco in February twenty twenty-six, with design by LoveFrom, the studio of Jony Ive and Marc Newson, and showed the exterior in Rome in May twenty twenty-six.""",
   "Ferrari Luce", "FERRARI LUCE: FULLY ELECTRIC")
sc("""Electra lists four motors, more than one thousand horsepower in boost mode, a battery of one hundred twenty-two kilowatt hours, and first deliveries from October twenty twenty-six. From a forty kilogram motor on a green test car, to a Ferrari with no engine at all, in about sixteen years.""",
   "Ferrari Luce electric", "16 YEARS: CONCEPT TO EV")
sc("""And notice the connection. The SF90's front axle used two electric motors to drive the front wheels independently. The Luce, according to Electra, uses four motors. The idea of controlling each wheel with electricity, first tested at scale on the SF90, became the foundation of Ferrari's first electric car.""",
   "Ferrari Luce front", "FROM 3 MOTORS TO 4")

# ---------- 10. WHY IT MATTERS ----------
ch("Why it matters")
sc("""So here is the insane story behind Ferrari's first plug-in hybrid. It began with a Formula One rule in twenty nine. It became a green laboratory car in twenty ten, with a promise that took a decade to keep. It passed through LaFerrari, a stock market listing, the sudden loss of Ferrari's most powerful boss, and a new leader from the tobacco industry.""",
   "Ferrari 599 HY-KERS and SF90", "THE STORY IN ONE MINUTE")
sc("""And when it finally arrived, the SF90 was not a compromise. It was faster around Fiorano than LaFerrari, it had no reverse gear, and it could become a silent front-wheel-drive car in the city. It convinced the most traditional buyers in the car world that a plug could belong in a Ferrari.""",
   "Ferrari SF90 Stradale", "NOT A COMPROMISE")
sc("""What do you think? Was the SF90 the most important Ferrari of its generation, or just a step toward the electric Luce? Tell us in the comments. In the other videos of this series, we reveal two things you didn't know about the SF90, compare it with the McLaren Artura, and ask whether a normal person could ever afford one.""",
   "Ferrari SF90 Spider", "THE MOST IMPORTANT FERRARI?")
sc("""If you are shopping for something a little more practical, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ferrari SF90 sunset", "SUBSCRIBE: PICKUP REALITY")

save("video72", "The Insane Story Behind Ferrari's First Plug-In Hybrid", [
    "Motor Authority, 2010 Geneva: Ferrari 599 HY-KERS concept: https://www.motorauthority.com/news/1042084_2010-geneva-motor-show-ferrari-599-hy-kers-concept",
    "CAR Magazine, Ferrari HY-KERS hybrid at Geneva 2010: https://carmagazine.co.uk/car-news/first-official-pictures/ferrari/ferrari-hy-kers-hybrid-2010-at-geneva-motor-show",
    "AutoGuide, Geneva 2010: Ferrari to offer hybrid versions of all models by 2014: https://www.autoguide.com/auto-news/2010/03/geneva-2010-ferrari-to-offer-hybrid-versions-of-all-models-by-2014.html",
    "Driven (NZ), LaFerrari was the world's first HEV hypercar: https://www.drivencarguide.co.nz/news/the-good-oil-laferrari-was-the-worlds-first-hev-hypercar/",
    "Wikipedia, McLaren P1: https://en.wikipedia.org/wiki/McLaren_P1",
    "Wikipedia, Ferrari (company history, IPO): https://en.wikipedia.org/wiki/Ferrari",
    "Autosport, Former Ferrari chief Sergio Marchionne dies (July 2018): https://www.autosport.com/f1/news/former-ferrari-chief-sergio-marchionne-dies-5297863/5297863/",
    "Bloomberg, Ferrari enlists Philip Morris veteran Camilleri as next CEO (July 2018): https://www.bloomberg.com/news/articles/2018-07-21/ferrari-proposes-camilleri-to-replace-ailing-marchionne-as-ceo",
    "ANSA, Ferrari to launch 15 new models (Sept 2018): https://www.ansa.it/english/news/business/2018/09/18/ferrari-to-launch-15-new-models_59177c10-40a0-4c24-8b57-1b918332cd04.html",
    "Motor1, Ferrari reveals roadmap with more hybrids (Sept 2018): https://www.motor1.com/news/266493/ferrari-reveals-roadmap-more-hybrids/",
    "Reuters via Euronews, Ferrari accelerates its move into hybrid cars (May 2019): https://www.euronews.com/2019/05/29/ferrari-accelerates-its-move-into-hybrid-cars",
    "InsideEVs, SF90 Stradale is Ferrari's first plug-in hybrid: https://insideevs.com/news/352375/sf90-stradale-first-ferrari-plugin-hybrid/",
    "Wikipedia, Ferrari SF90 Stradale: https://en.wikipedia.org/wiki/Ferrari_SF90_Stradale",
    "The Race, Ferrari CEO Camilleri resigns for personal reasons (Dec 2020): https://www.the-race.com/formula-1/ferrari-ceo-camilleri-resigns-for-personal-reasons/",
    "Wikipedia, Benedetto Vigna: https://en.wikipedia.org/wiki/Benedetto_Vigna",
    "Motor Authority, Ferrari SF90 recalled (Oct 2023): https://www.motorauthority.com/news/1141294_ferrari-sf90-recalled",
    "Evo India, SF90 XX Stradale revealed: https://www.evoindia.com/top-news/new-ferrari-sf90-xx-stradale-revealed",
    "Autobuzz, Facts & Figures: SF90 Stradale launched in Malaysia (2020): https://autobuzz.my/2020/09/18/facts-figures-ferrari-sf90-stradale-launched-in-malaysia/",
    "CarGurus, 2023 Ferrari SF90 pricing: https://www.cargurus.com/research/2023-Ferrari-SF90-c32760",
    "Road & Track via Yahoo, Fire, glitches, delays: McLaren after the Artura launch (June 2022): https://autos.yahoo.com/fire-glitches-delays-mclaren-post-202000664.html",
    "Wikipedia, Ferrari LaFerrari: https://en.wikipedia.org/wiki/LaFerrari",
    "Wikipedia, Kinetic energy recovery system (Formula One): https://en.wikipedia.org/wiki/Kinetic_energy_recovery_system",
    "Wikipedia, Ferrari F80: https://en.wikipedia.org/wiki/Ferrari_F80",
    "Motor Authority, Ferrari 2024 deliveries: 51% hybrids: https://www.motorauthority.com/news/1145679_ferrari-2024-hybrid-sales",
    "Motoring Research, Ferrari 849 Testarossa (Sept 2025): https://www.motoringresearch.com/car-news/2026-ferrari-849-testarossa/",
    "Electra, Ferrari Luce: everything we know: https://www.go-electra.com/en/newsroom/electric-ferrari-luce-price-power-and-everything-we-know/",
], "D")
