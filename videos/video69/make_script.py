import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Ferrari SF90 Stradale has almost one thousand horsepower, it reaches one hundred kilometers per hour in two and a half seconds, and when it arrived it was faster around Ferrari's own test track than the LaFerrari hypercar. But it hides two facts that most people, even many Ferrari fans, have never heard. One of them is about going backward. The other is about which wheels move the car.""",
   "Ferrari SF90 Stradale", "2 THINGS YOU DIDN'T KNOW ABOUT THE SF90")
sc("""Here is the hint. The SF90 has eight forward gears, and not a single reverse gear. And in one of its modes, this mid-engined Ferrari becomes a front-wheel-drive car. Both facts sound like mistakes. They are actually two of the smartest decisions Ferrari ever made.""",
   "Ferrari SF90 Stradale rear", "NO REVERSE GEAR?")
sc("""Along the way, you will see the recall that told owners not to drive their cars, the extreme XX version limited to seven hundred ninety-nine cars, and the car that replaced the SF90 sooner than many expected. Every number in this video comes from a published source, and the list is in the description.""",
   "Ferrari SF90 XX Stradale", "EVERY NUMBER IS SOURCED")
sc("""And one more twist before we start. The SF90 was not Ferrari's first hybrid. But it was the first one Ferrari built for more than a few hundred customers, and that changed the company.""",
   "Ferrari LaFerrari", "NOT THE FIRST FERRARI HYBRID")

# ---------- 1. THE CAR ----------
ch("Ninety years of racing")
sc("""The name tells a story. S F ninety refers to the ninetieth anniversary of Scuderia Ferrari, the company's racing team, and Stradale means made for the road. Ferrari unveiled it on Wednesday, the twenty-ninth of May twenty nineteen, at its home in Maranello, Italy, according to Reuters.""",
   "Ferrari Maranello", "SF90: 90 YEARS OF SCUDERIA FERRARI")
sc("""Ferrari's chief executive at the time, Louis Camilleri, called the car astounding, fast, and completely revolutionary. Reuters reported that about two thousand selected customers were invited to view and reserve it, with deliveries due within twelve months. It was a bigger audience than any Ferrari hybrid before it.""",
   "Ferrari SF90 Stradale red", "ASTOUNDING, FAST, REVOLUTIONARY")
sc("""The earlier LaFerrari, built from twenty thirteen to twenty sixteen, was a hybrid too, but a limited series. Driven, a New Zealand outlet, lists five hundred coupes and two hundred ten Aperta roadsters. Its hybrid system was inspired by the K E R S energy recovery technology that came into Formula One in two thousand nine. The SF90 took that idea to series production.""",
   "Ferrari LaFerrari Aperta", "LAFERRARI: A LIMITED HYBRID")
sc("""The numbers are serious. A three point nine nine liter twin-turbo V8, the F one fifty-four, makes about seven hundred sixty-nine horsepower on its own. Three electric motors add about two hundred seventeen more. Total output is about nine hundred eighty-six horsepower, or one thousand metric horsepower, with eight hundred newton meters of torque.""",
   "Ferrari SF90 engine", "986 HP")
sc("""Zero to one hundred kilometers per hour takes two point five seconds, zero to two hundred takes six point seven, and top speed is three hundred forty kilometers per hour, or two hundred eleven miles per hour. The battery is seven point nine kilowatt hours, and the gearbox is an eight-speed dual-clutch unit. And that gearbox is where the first secret hides.""",
   "Ferrari SF90 Stradale side", "0-100 IN 2.5 SECONDS")
sc("""Before the secrets, a quick word on how a dual-clutch gearbox works, because it matters for secret number one. It has two clutches, one for the odd gears and one for the even gears. While you drive in one gear, the next one is already selected and waiting. That is why the shifts are so fast. Design News reported that this new eight-speed unit, built with Magna, is about seven kilograms lighter than the seven-speed gearbox it replaced, and its clutches are twenty percent smaller in diameter.""",
   "Ferrari SF90 Stradale gear selector", "TWO CLUTCHES, EIGHT GEARS")

# ---------- 2. SECRET ONE ----------
ch("Secret 1: no reverse gear")
sc("""Secret number one. The SF90 has no reverse gear. Its eight-speed dual-clutch gearbox only goes forward. duPont Registry and InsideEVs both reported that when an SF90 backs out of a parking space, it is the front electric motors that do the work, spinning backward.""",
   "Ferrari SF90 Stradale parking", "SECRET 1: NO REVERSE GEAR")
sc("""InsideEVs explained that reverse works only in the electric eDrive mode, powered by the front motors, so the car can move at low speed without even starting the V8. In other words, every time an SF90 reverses, it is behaving like an electric car.""",
   "Ferrari SF90 front", "REVERSE IS ELECTRIC")
sc("""Why would Ferrari remove a reverse gear from a car that costs half a million dollars? Weight and space. A reverse gear needs its own gear set and shafts inside the gearbox. If electric motors can already move the car backward, that hardware becomes dead weight. Removing it makes the gearbox lighter and more compact.""",
   "Ferrari SF90 gearbox", "WHY? WEIGHT AND SPACE")
sc("""Design News put a number on it. According to its report, eliminating the reverse gear saved about ten kilograms on its own, on top of the weight already saved by the new design. The complete eight-speed transmission weighs about one hundred thirty-eight kilograms. In a car where every kilogram was fought for, ten kilograms from one missing gear is a real win.""",
   "Ferrari SF90 Stradale rear diffuser", "REVERSE GONE: ~10 KG SAVED")
sc("""And Ferrari was not alone. The McLaren Artura, another plug-in hybrid supercar, also uses its electric motor in place of a reverse gear, according to Wikipedia. Once a car has strong electric motors, the old reverse gear starts to look like a part from another era.""",
   "McLaren Artura", "McLAREN DID IT TOO")
sc("""Here is the twist. Weight mattered a lot, because the hybrid system is heavy. InsideEVs reported that the hybrid components add about two hundred seventy kilograms. That is roughly the weight of three or four adult passengers. Ferrari had to save weight everywhere else just to keep the car competitive, and dropping the reverse gear was one of those savings.""",
   "Ferrari SF90 carbon", "HYBRID PARTS: ~270 KG")
sc("""Here is a way to picture it. Every forward gear in a gearbox is a pair of gears in mesh. Reverse needs an extra gear in between, an idler, to flip the direction of rotation, plus the parts to engage it. In the SF90, all of that simply is not there. When the driver selects reverse, the computer asks the front motors to turn the other way.""",
   "Ferrari SF90 Stradale cockpit", "NO IDLER GEAR, NO REVERSE")
sc("""There is even a small, very Ferrari detail. In the SF90, the gear selector on the center tunnel was designed to look like the classic Ferrari open gate, the metal grid that guided the gear lever in older manual Ferraris. Autobuzz, reporting Ferrari's own launch details, said the selector draws on the manual gearbox lever gate, with past and present merging. So the most modern Ferrari of its time reverses electrically, while its selector imitates a manual gearbox from decades ago.""",
   "Ferrari gated shifter", "A NOD TO THE OPEN GATE")
sc("""InsideEVs said Ferrari kept the dry weight at one thousand five hundred seventy kilograms, which means about one point five seven kilograms for every metric horsepower. For a car carrying a battery, three motors, and power electronics, that is a remarkable result.""",
   "Ferrari SF90 Assetto Fiorano", "1.57 KG PER HORSEPOWER")

# ---------- 3. SECRET TWO ----------
ch("Secret 2: front-wheel drive")
sc("""Secret number two. In one of its modes, the SF90 is a front-wheel-drive car. In eDrive mode, the V8 is switched off, and the car moves only on its two front electric motors. InsideEVs reported that in eDrive the SF90 uses only the front axle, with a range of up to about twenty-five kilometers.""",
   "Ferrari SF90 Stradale electric", "SECRET 2: FRONT-WHEEL DRIVE")
sc("""Think about that. A mid-engined Ferrari, with its V8 behind the driver, pulling itself through a city with its front wheels, silently. With the V8 off, InsideEVs said the SF90 can reach about one hundred thirty-five kilometers per hour, which is about eighty-four miles per hour, on electricity alone.""",
   "Ferrari SF90 city", "135 KM/H ON ELECTRICITY")
sc("""Reuters explained the reason. The electric-only mode lets the car run quietly through city centers. In some European cities, there are growing limits on noise and emissions. A Ferrari that can enter a historic center in silence, and then wake up its V8 on the open road, fits into that world.""",
   "Ferrari SF90 historic city", "SILENT IN THE CITY")
sc("""And when the V8 is running, those front motors do something else entirely. They give the car all-wheel drive and torque vectoring. duPont Registry described Ferrari's R A C dash e system, which can send different amounts of power to each front wheel to help the car turn into a corner.""",
   "Ferrari SF90 cornering", "RAC-e TORQUE VECTORING")
sc("""So the twist is that the same front motors that make the SF90 a quiet city car also make it a faster track car. One part of the car, two completely different personalities. Ferrari calls its drive modes eDrive, Hybrid, which is the default, Performance, and Qualify, which uses the full power of all three motors and the V8.""",
   "Ferrari SF90 steering wheel", "eDRIVE TO QUALIFY")
sc("""And here is a detail that makes this even stranger. The third electric motor is not at the front at all. Wikipedia describes it as sitting between the V8 and the gearbox, at the back of the car, where it helps the engine and recharges the battery. So the SF90 can be a silent front-wheel-drive car, a hybrid all-wheel-drive car, or a full-power track car, depending on the button you press.""",
   "Ferrari SF90 Stradale yellow", "THREE CARS IN ONE")
sc("""Now, how useful is twenty-five kilometers of electric range in real life? It is about fifteen miles. That is enough to leave a city center, cross a quiet neighborhood early in the morning, or arrive at a hotel without waking anyone. It is not enough for a long commute. Ferrari never sold the SF90 as an electric car. It sold it as a Ferrari that can choose when to be silent.""",
   "Ferrari SF90 Stradale night", "~15 MILES OF SILENCE")
sc("""And the battery is small for a reason. At seven point nine kilowatt hours, it is a fraction of the size of a typical electric car battery. A bigger battery would add range, but also weight, and weight is the enemy of a supercar. Ferrari chose just enough battery to make the front motors useful, and no more.""",
   "Ferrari SF90 chassis", "7.9 kWh: JUST ENOUGH")

# ---------- 4. THE TRACK ----------
ch("Faster than LaFerrari")
sc("""So did all this make the SF90 fast? Wikipedia says that as of twenty twenty it was the fastest Ferrari road car around Fiorano, Ferrari's own test track, seven tenths of a second faster than LaFerrari. InsideEVs listed a Fiorano lap of about seventy-nine seconds.""",
   "Fiorano circuit", "7 TENTHS FASTER THAN LAFERRARI")
sc("""That is a big statement. The LaFerrari was a limited-edition hypercar. The SF90 was a series production car that more customers could buy. Ferrari built a car for a wider audience and it beat the brand's flagship on its own circuit.""",
   "Ferrari LaFerrari track", "SERIES CAR BEATS HYPERCAR")
sc("""And in twenty twenty, Wikipedia says, the SF90 lapped the Top Gear test track in one minute eleven point three seconds, the fastest car to lap it at that time. Its aerodynamics helped. Ferrari claims three hundred ninety kilograms of downforce at two hundred fifty kilometers per hour.""",
   "Ferrari SF90 aerodynamics", "TOP GEAR LAP: 1:11.3")
sc("""Then came the Assetto Fiorano package, a track pack with Multimatic shock absorbers, carbon fiber parts, a titanium exhaust, and carbon wheels. Wikipedia says it saves thirty kilograms. CarGurus reported that the package cost about fifty thousand dollars in America.""",
   "Ferrari SF90 Assetto Fiorano", "ASSETTO FIORANO: ~$50,000")

# ---------- 5. THE SPIDER AND XX ----------
ch("The Spider and the XX")
sc("""Ferrari also built an open version, the SF90 Spider, with a retractable hard top. Wikipedia says it was the first Ferrari plug-in hybrid offered as a convertible, and calls it the most powerful non-limited convertible in the world at the time.""",
   "Ferrari SF90 Spider", "SF90 SPIDER")
sc("""Then came the extreme versions. In twenty twenty-three, Ferrari revealed the SF90 X X Stradale and X X Spider, track-focused cars that are still road legal. Combined output rose to about one thousand sixteen horsepower. Production was set at seven hundred ninety-nine Stradales and five hundred ninety-nine Spiders, all pre-allocated to customers.""",
   "Ferrari SF90 XX Stradale", "XX: 799 + 599 CARS")
sc("""Here is the twist. The X X name comes from Ferrari's track-only program, where customers buy cars like the F X X K that cannot be driven on public roads. The SF90 X X was the first time Ferrari put the X X name on a car you could legally drive on the street.""",
   "Ferrari FXX-K", "XX ON THE STREET")
sc("""The X X also had to look different, and it does. Evo India reported that it is the first Ferrari with a fixed rear wing since the F50 of the nineteen nineties, and that the rear wing alone produces three hundred fifteen kilograms of downforce. The combustion engine also gained power, to about seven hundred eighty-six horsepower, for a total of about one thousand sixteen.""",
   "Ferrari F40 rear wing", "FIRST FIXED WING SINCE THE F40")

# ---------- 6. THE RECALL ----------
ch("The recall")
sc("""No car is perfect, and the SF90 had a serious recall. In October twenty twenty-three, Motor Authority reported that six hundred fourteen SF90s from the twenty twenty-two to twenty twenty-four model years were recalled in the United States.""",
   "Ferrari SF90 Stradale recall", "614 CARS RECALLED")
sc("""The problem was the turbocharger oil delivery pipes. Some may have been made with a notch or the wrong thickness, which could cause an oil leak and a fire. Ferrari and the National Highway Traffic Safety Administration urged owners not to drive the affected cars until dealers replaced the pipes, which they did for free.""",
   "Ferrari SF90 engine bay", "DON'T DRIVE IT")
sc("""It is a reminder that a hybrid supercar has two complex systems at once. A high-strung twin-turbo V8, and a high-voltage electric system. Both have to be perfect, and the SF90's recall was on the old-fashioned side, the turbo engine, not the battery.""",
   "Ferrari V8 engine", "THE PROBLEM WAS THE TURBO")
sc("""Recalls like this are actually common in the supercar world, because these cars are built in small numbers and pushed to extreme limits. What made this one notable was the instruction. Owners of half-million-dollar cars were told to leave them parked until the fix was done. For many, that meant weeks without their Ferrari.""",
   "Ferrari SF90 Stradale garage", "PARKED UNTIL FIXED")

# ---------- 7. LIVING WITH IT ----------
ch("Living with it")
sc("""What is it like to own? CarGurus listed the twenty twenty-three SF90 Stradale at a starting price of about five hundred twenty thousand dollars in the United States, and the Spider at about five hundred seventy thousand. It also listed fuel economy of up to fifty-one M P G e for the coupe, a rating that includes electric driving.""",
   "Ferrari SF90 Stradale price", "~$520,000 TO START")
sc("""Practicality is limited. CarGurus listed just two seats and two point six cubic feet of cargo space. It also noted that the car is not crash tested by the usual American safety agencies, which is normal for low-volume supercars. This is not a car you choose for weekend shopping.""",
   "Ferrari SF90 interior", "2.6 CUBIC FEET OF CARGO")
sc("""The cockpit was also a break with the past. Autobuzz described a sixteen-inch curved digital instrument display behind the steering wheel, controlled through touch pads and haptic buttons on the wheel itself, and no central infotainment screen at all. The passenger gets only a small display, which shows the speed. The idea was that the driver should never have to look away from the road.""",
   "Ferrari SF90 dashboard", "16-INCH CURVED DISPLAY")
sc("""Inside, the SF90 introduced a new Ferrari cockpit, with a curved digital display and touch-sensitive controls on the steering wheel. And here is the twist. When Ferrari revealed the SF90's replacement in twenty twenty-five, Motoring Research reported that it went back to physical switches on the steering wheel instead of haptic touch controls, plus a physical start button. Owners had spoken.""",
   "Ferrari SF90 steering wheel", "BACK TO PHYSICAL BUTTONS")

# ---------- 8. THE REPLACEMENT ----------
ch("The replacement")
sc("""That replacement is the eight forty-nine Testarossa, revealed on the tenth of September twenty twenty-five. Motoring Research reported about one thousand fifty horsepower combined, about fifty more than the SF90, with an enhanced four liter twin-turbo V8 making about eight hundred thirty horsepower on its own.""",
   "Ferrari 849 Testarossa", "849 TESTAROSSA: 1,050 HP")
sc("""Motoring Research reported prices of about four hundred thousand pounds for the coupe and about four hundred thirty-five thousand pounds for the Spider in Europe, and a top speed of more than two hundred five miles per hour. In other words, more power and more downforce, at a price in the same territory as the car it replaces.""",
   "Ferrari 849 Testarossa Spider", "~£400,000 IN EUROPE")
sc("""It keeps the SF90's recipe of three electric motors and a plug-in battery of about seven point four five kilowatt hours, and claims zero to one hundred in under two point three seconds. It produces four hundred fifteen kilograms of downforce, twenty-five more than the SF90. And it revives one of Ferrari's most famous names, the Testarossa from the nineteen eighties.""",
   "Ferrari Testarossa 1984", "THE TESTAROSSA NAME RETURNS")
sc("""So the SF90's life as Ferrari's flagship series car lasted about five years, from first sales in twenty twenty to the reveal of its successor in twenty twenty-five. Short, but enormously important, because it proved that Ferrari buyers would accept a plug, a battery, and even a front-wheel-drive mode.""",
   "Ferrari SF90 Stradale and 849", "5 YEARS THAT CHANGED FERRARI")
sc("""And the next step was even bigger. Ferrari has since revealed its first fully electric car, the Luce, with an interior designed by LoveFrom, the studio of Jony Ive and Marc Newson. Electra's summary lists four motors, more than one thousand horsepower in boost mode, and first deliveries scheduled from October twenty twenty-six. The SF90's front motors were the first step on that road.""",
   "Ferrari Luce", "NEXT: THE ELECTRIC LUCE")
sc("""The Luce was revealed in steps. Electra's summary says the technology was shown in October twenty twenty-five, the name and interior in San Francisco in February twenty twenty-six, and the exterior in Rome on the twenty-fifth of May twenty twenty-six. It lists a battery of one hundred twenty-two kilowatt hours and up to five hundred thirty kilometers of range on the European W L T P cycle.""",
   "Ferrari Luce electric", "LUCE: 122 kWh, 530 KM")
sc("""Think about the path. LaFerrari, a limited hypercar with a small hybrid system. Then the SF90, a series production car that could drive on electricity for a few miles. Then the Luce, a Ferrari with no engine at all. In about thirteen years, Ferrari went from an electric boost to a fully electric car, and the SF90 sits right in the middle.""",
   "Ferrari LaFerrari SF90", "FROM BOOST TO FULLY ELECTRIC")

# ---------- 9. RECAP ----------
ch("The two things, again")
sc("""So let's recap the two things most people don't know about the Ferrari SF90. Number one, it has no reverse gear. Its front electric motors drive it backward, which saved weight and space in the gearbox, in a car that had to carry about two hundred seventy kilograms of hybrid hardware.""",
   "Ferrari SF90 Stradale rear view", "1. NO REVERSE GEAR")
sc("""Number two, in eDrive mode it is a front-wheel-drive Ferrari, pulling itself silently through cities on its front motors for about twenty-five kilometers, at up to one hundred thirty-five kilometers per hour. Then those same motors give it all-wheel drive and torque vectoring on the track.""",
   "Ferrari SF90 Stradale front view", "2. A FRONT-WHEEL-DRIVE FERRARI")
sc("""Together, those two facts explain why the SF90 matters. It was not just a fast Ferrari. It was the car that taught Ferrari to use electric motors as a real part of the car, not an add-on. Everything that came after, from the eight forty-nine Testarossa to the Luce, builds on it.""",
   "Ferrari SF90 Stradale", "THE CAR THAT TAUGHT FERRARI")
sc("""In the other videos of this series, we compare the SF90 with the McLaren Artura, we ask whether a normal person could ever afford one, and we tell the story behind Ferrari's first plug-in hybrid. Tell us in the comments which fact surprised you more, the missing reverse gear or the front-wheel-drive mode.""",
   "McLaren Artura", "3 MORE ANGLES")
sc("""If you are shopping for something more practical than a Ferrari, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ferrari SF90 sunset", "SUBSCRIBE: PICKUP REALITY")

save("video69", "2 Things You Didn't Know About the Ferrari SF90", [
    "Wikipedia, Ferrari SF90 Stradale: https://en.wikipedia.org/wiki/Ferrari_SF90_Stradale",
    "Reuters via Euronews, Ferrari accelerates its move into hybrid cars (May 29, 2019): https://www.euronews.com/2019/05/29/ferrari-accelerates-its-move-into-hybrid-cars",
    "InsideEVs, SF90 Stradale is Ferrari's first plug-in hybrid (May 2019): https://insideevs.com/news/352375/sf90-stradale-first-ferrari-plugin-hybrid/",
    "duPont Registry, Ferrari SF90 Stradale price, specs, review: https://news.dupontregistry.com/blogs/ferrari-news/ferrari-sf90-stradale-price-specs-photos-review",
    "Design News, Magna 8-speed DCT in the SF90: https://www.designnews.com/automotive/ferrari-sf90-stradale-accelerates-through-gears-magnas-8-speed-dual-clutch-transmission",
    "Autobuzz, Facts & Figures: SF90 Stradale launched in Malaysia (2020): https://autobuzz.my/2020/09/18/facts-figures-ferrari-sf90-stradale-launched-in-malaysia/",
    "Evo India, SF90 XX Stradale revealed: https://www.evoindia.com/top-news/new-ferrari-sf90-xx-stradale-revealed",
    "Driven (NZ), LaFerrari was the world's first HEV hypercar: https://www.drivencarguide.co.nz/news/the-good-oil-laferrari-was-the-worlds-first-hev-hypercar/",
    "Wikipedia, McLaren Artura (electric motor replaces reverse gear): https://en.wikipedia.org/wiki/McLaren_Artura",
    "Motor Authority, Ferrari SF90 recalled (Oct 2023): https://www.motorauthority.com/news/1141294_ferrari-sf90-recalled",
    "CarGurus, 2023 Ferrari SF90 review and pricing: https://www.cargurus.com/research/2023-Ferrari-SF90-c32760",
    "Motoring Research, Ferrari 849 Testarossa replaces the SF90 (Sept 2025): https://www.motoringresearch.com/car-news/2026-ferrari-849-testarossa/",
    "Electra, Ferrari Luce: everything we know: https://www.go-electra.com/en/newsroom/electric-ferrari-luce-price-power-and-everything-we-know/",
], "A")
