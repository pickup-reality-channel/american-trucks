import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Two plug-in hybrid supercars. Both arrived in the same era, both have a battery of under eight kilowatt hours, both can drive on electricity alone, and both have thrown away the reverse gear. The Ferrari SF90 Stradale and the McLaren Artura look like the same idea. But one costs about twice as much as the other, and the reason is the difference nobody explains.""",
   "Ferrari SF90 Stradale", "SF90 vs ARTURA")
sc("""On paper, the SF90 has almost one thousand horsepower and all-wheel drive. The Artura has about six hundred eighty, a V6, and rear-wheel drive. So the easy answer is that the Ferrari is simply more car. But that answer misses the real story, which is about what each company was trying to build, and what each one risked.""",
   "McLaren Artura", "THE EASY ANSWER IS WRONG")
sc("""Because here is the twist. The Artura was never really built to fight the SF90. Its true rival is a different Ferrari, one that shares its engine layout almost exactly. And the SF90 was never Ferrari's answer to McLaren. It was Ferrari's new flagship, aimed at a different buyer entirely.""",
   "Ferrari 296 GTB", "THE REAL RIVAL IS ANOTHER FERRARI")
sc("""Along the way, you will hear about the McLaren launch that went wrong, the Ferrari recall that told owners to park their cars, and what happened to both companies after these cars came out. Every number here is from a published source, listed in the description.""",
   "McLaren Artura Spider", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE TWO CARS ----------
ch("Two cars, one idea")
sc("""Start with the Ferrari. The SF90 Stradale was unveiled in Maranello on the twenty-ninth of May twenty nineteen, Reuters reported, as the first Ferrari hybrid built for wider series production. The name marks ninety years of Scuderia Ferrari, the racing team.""",
   "Ferrari SF90 Stradale red", "FERRARI SF90: MAY 2019")
sc("""It combines a four liter twin-turbo V8 with three electric motors. Wikipedia lists about seven hundred sixty-nine horsepower from the engine, and about nine hundred eighty-six combined, with eight hundred newton meters of torque. Zero to one hundred kilometers per hour takes two point five seconds, and top speed is three hundred forty.""",
   "Ferrari SF90 engine", "986 HP, V8 + 3 MOTORS")
sc("""Ferrari treated the launch like an event. Reuters reported that about two thousand selected customers were invited to Maranello to see the car and reserve one, with deliveries expected within twelve months. Ferrari's chief executive at the time, Louis Camilleri, called it astounding, fast, and completely revolutionary. This was not a quiet entry model. It was a statement.""",
   "Ferrari Maranello", "2,000 CUSTOMERS INVITED")
sc("""Now the McLaren. Wikipedia says the Artura was announced on the twenty-third of November twenty twenty and unveiled in February twenty twenty-one. It replaced the five seventy S as McLaren's entry series car, and it was McLaren's third hybrid, after the P1 hypercar and the Speedtail.""",
   "McLaren Artura orange", "McLAREN ARTURA: 2021")
sc("""And this rivalry is older than these two cars. In twenty thirteen, McLaren and Ferrari each launched a hybrid hypercar. McLaren had the P1, built in a run of three hundred seventy-five cars. Ferrari had the LaFerrari, with five hundred coupes, according to Driven. The SF90 and the Artura are what happened when both companies took that hybrid idea from hypercars into their regular model lines.""",
   "McLaren P1 and LaFerrari", "2013: P1 vs LAFERRARI")
sc("""The name blends two words, art and future. Its engine is a three liter twin-turbo V6, coded M six thirty, with its two banks of cylinders set at one hundred twenty degrees. It makes about five hundred eighty-five metric horsepower on its own. An electric motor adds ninety-five more, for about six hundred eighty combined, with seven hundred twenty newton meters of torque.""",
   "McLaren Artura engine", "680 PS, V6 + 1 MOTOR")
sc("""Why a V6 with such a wide angle? With the cylinder banks set one hundred twenty degrees apart, there is room to place the two turbochargers inside the V, between the banks. Engineers call this a hot vee. It keeps the engine short, low, and compact, which helps a mid-engined car carry its weight lower and closer to the center.""",
   "McLaren M630 V6", "120 DEGREES: A HOT VEE")
sc("""Wikipedia lists zero to one hundred in about three seconds, and a top speed of three hundred thirty kilometers per hour. So the Ferrari is about half a second quicker to one hundred, and ten kilometers per hour faster at the top. Those gaps sound small. The price gap is not.""",
   "McLaren Artura side", "0-100 IN ~3.0 SECONDS")

# ---------- 2. THE PRICE ----------
ch("The price gap")
sc("""In the United States, CarGurus listed the twenty twenty-three SF90 Stradale starting at about five hundred twenty thousand dollars. Kelley Blue Book listed the twenty twenty-five Artura at about two hundred fifty-four thousand dollars, and the Artura Spider at about two hundred seventy-nine thousand.""",
   "Ferrari SF90 Stradale and McLaren Artura", "$520K vs $254K")
sc("""So for the price of one SF90, you could almost buy two Arturas. That is the first difference nobody explains properly. These two cars are not competitors in the showroom. They sit in completely different price classes, even though they share a lot of technology.""",
   "McLaren Artura rear", "ONE SF90 = TWO ARTURAS")
sc("""Here is why that matters. Ferrari had a cheaper hybrid planned too. The two hundred ninety-six G T B, revealed in twenty twenty-one, uses a twin-turbo V6 with a one hundred twenty degree angle between its cylinder banks, a plug-in battery, and an electric motor. That is almost exactly the Artura's recipe.""",
   "Ferrari 296 GTB", "THE 296 GTB: SAME RECIPE")
sc("""Carwow Spain compared them at launch. It listed the two ninety-six at eight hundred thirty metric horsepower combined, and the Artura at six hundred eighty. It listed a starting price in Spain of about two hundred sixty-nine thousand euros for the Ferrari, and about two hundred thirty-five thousand for the McLaren. Those two really are rivals.""",
   "Ferrari 296 GTB and McLaren Artura", "296 GTB vs ARTURA")
sc("""So the honest comparison is this. The SF90 sits above both of them, as Ferrari's flagship. The Artura and the two ninety-six fight each other one level lower. When people put the SF90 and the Artura side by side, they are comparing a Ferrari flagship with a McLaren entry model. That is the twist behind the price.""",
   "Ferrari SF90 Stradale front", "FLAGSHIP vs ENTRY MODEL")
sc("""Carwow's launch comparison also showed how close the two ninety-six and the Artura are. It listed the Ferrari at two point nine seconds to one hundred and three hundred forty kilometers per hour, with about twenty-five kilometers of electric range. It listed the McLaren at three seconds, three hundred thirty, and about thirty kilometers of range. Both weighed about one and a half tonnes ready to drive.""",
   "Ferrari 296 GTB rear", "296 vs ARTURA: NECK AND NECK")

# ---------- 3. THE HYBRID SYSTEMS ----------
ch("Two ways to build a hybrid")
sc("""Now look inside, because the hybrid systems are where these cars really differ. The SF90 has three electric motors. Two are on the front axle, one for each front wheel. The third sits between the V8 and the gearbox. That layout gives the Ferrari electric all-wheel drive.""",
   "Ferrari SF90 chassis", "SF90: THREE MOTORS")
sc("""The Artura has just one electric motor, an axial flux design built into the gearbox housing, according to Wikipedia. It drives the rear wheels with the engine. There is nothing at the front. The Artura stays rear-wheel drive, like almost every McLaren road car before it.""",
   "McLaren Artura chassis", "ARTURA: ONE MOTOR, RWD")
sc("""Axial flux is worth a short explanation. In a typical electric motor, the magnetic field runs from the center outward. In an axial flux motor, it runs along the axis, so the motor can be shaped like a thick disc instead of a long cylinder. That makes it short and compact, which is why McLaren could fit it between the engine and the gearbox.""",
   "electric motor axial flux", "WHAT IS AXIAL FLUX?")
sc("""And here is what they share. Both cars dropped the reverse gear. Design News reported that removing reverse from the SF90's eight-speed gearbox saved about ten kilograms, because the front motors move the car backward. Wikipedia says the Artura does the same thing with its single motor, which also replaces the reverse gear.""",
   "Ferrari SF90 Stradale rear", "NEITHER HAS A REVERSE GEAR")
sc("""Both also use eight-speed dual-clutch gearboxes. Both use small batteries. InsideEVs listed the SF90's at seven point nine kilowatt hours. Wikipedia lists the Artura's at about seven point four, weighing about eighty-eight kilograms. Neither car is trying to be an electric car. Both use electricity to add punch, and a few silent miles.""",
   "McLaren Artura interior", "7.9 kWh vs 7.4 kWh")

# ---------- 4. ELECTRIC MODE ----------
ch("Silent mode")
sc("""On electricity alone, the two cars behave differently, and this is the twist most people miss. The SF90's electric mode uses only its front motors, InsideEVs reported. So in eDrive, a mid-engined Ferrari becomes a front-wheel-drive car, with up to about twenty-five kilometers of range and a top speed of about one hundred thirty-five kilometers per hour.""",
   "Ferrari SF90 Stradale city", "SF90 eDRIVE: FRONT-WHEEL DRIVE")
sc("""The Artura's electric mode uses its rear motor, so it stays rear-wheel drive even in silence. Wikipedia lists an electric range of about thirty-one kilometers on the European cycle. Kelley Blue Book lists about twenty-one miles for the American version, which is about thirty-four kilometers. Either way, it can go a little further on electricity than the Ferrari.""",
   "McLaren Artura city", "ARTURA EV: ~21 MILES")
sc("""So the cheaper car has the longer electric range. That sounds strange, but it makes sense. The Ferrari spends its electricity on performance, with three motors and much more combined power. The McLaren's single motor is less powerful, so the same amount of battery lasts longer.""",
   "McLaren Artura charging", "CHEAPER CAR, LONGER EV RANGE")
sc("""Fuel economy follows the same logic. CarGurus listed the SF90 coupe at up to fifty-one M P G e, a combined figure that includes electric driving. These figures depend heavily on how often the car is plugged in. A plug-in hybrid that is never charged simply carries its battery as extra weight.""",
   "Ferrari SF90 charging port", "UP TO 51 MPGe")

# ---------- 5. WEIGHT ----------
ch("The weight war")
sc("""Weight is where McLaren put up its strongest fight. The Artura is built on a new carbon fiber structure called the McLaren Carbon Lightweight Architecture, or M C L A. Wikipedia lists its lightest curb weight at about one thousand four hundred ninety-eight kilograms, ready to drive.""",
   "McLaren Artura carbon tub", "McLAREN MCLA CARBON CHASSIS")
sc("""Ferrari quotes the SF90 in a different way. InsideEVs reported a dry weight of one thousand five hundred seventy kilograms, which means without fluids like fuel and oil. A dry weight is always lower than a curb weight. So the SF90 is clearly the heavier car, by more than the numbers first suggest.""",
   "Ferrari SF90 Stradale side view", "DRY WEIGHT vs CURB WEIGHT")
sc("""InsideEVs said the SF90's hybrid parts add about two hundred seventy kilograms. That is the price of three motors and all-wheel drive. The SF90 uses that extra hardware to put almost one thousand horsepower onto the road. The Artura uses lightness instead, and lets the rear tires do the work.""",
   "Ferrari SF90 Stradale cornering", "SF90: +270 KG OF HYBRID")
sc("""So the difference in philosophy is clear. Ferrari built a heavier car with more power and four driven wheels. McLaren built a lighter car with less power and two. Both are fast. They just get there in opposite ways.""",
   "McLaren Artura cornering", "POWER vs LIGHTNESS")

# ---------- 6. CORNERING ----------
ch("How they turn")
sc("""In corners, Ferrari uses its front motors for torque vectoring. The system can send different amounts of power to each front wheel, helping pull the nose of the car into a turn. duPont Registry described this as Ferrari's R A C dash e system.""",
   "Ferrari SF90 track", "FERRARI: ELECTRIC TORQUE VECTORING")
sc("""McLaren went a different way. Wikipedia says the Artura was the first modern McLaren with an electronically controlled differential, which manages how power is split between the two rear wheels. It is a less exotic solution than Ferrari's front motors, but it is lighter, and it keeps the car's handling closer to a classic rear-wheel-drive supercar.""",
   "McLaren Artura track", "McLAREN: AN E-DIFF")
sc("""Think of the two systems like this. In the Ferrari, electricity is used to steer the car through the corner, by pushing one front wheel harder than the other. In the McLaren, the differential uses clutches to manage grip at the rear. One is a new idea from the electric era. The other is a refined version of a solution that racing cars have used for decades.""",
   "Ferrari SF90 and McLaren Artura track", "ELECTRIC vs MECHANICAL")
sc("""On the track, the Ferrari had the numbers. Wikipedia says the SF90 was, as of twenty twenty, the fastest Ferrari road car ever around Ferrari's Fiorano test track, seven tenths of a second faster than LaFerrari. It also says the SF90 set the fastest lap on the Top Gear test track in twenty twenty, one minute eleven point three seconds.""",
   "Fiorano circuit Ferrari", "SF90: TRACK RECORDS")
sc("""The Artura was not built to chase those records. Its job was to make a hybrid McLaren usable every day, with rear-wheel drive feel and a lower price. And that job turned out to be much harder than anyone expected.""",
   "McLaren Artura road", "ARTURA'S REAL JOB")

# ---------- 7. THE LAUNCHES ----------
ch("A difficult launch")
sc("""Here is the twist in the McLaren story. Road and Track reported in June twenty twenty-two that Artura deliveries, first expected at the end of twenty twenty-one, were delayed until July twenty twenty-two. At the media drive, some test cars had problems, including dark screens and cars going into limp mode, a reduced power safety mode.""",
   "McLaren Artura launch", "DELAYS AND GLITCHES")
sc("""Road and Track also reported that a test car caught fire, and that McLaren blamed a nut on an oil cooler fuel line. For a brand launching a new hybrid with a new chassis, a new engine, and new electronics, it was a hard start.""",
   "McLaren Artura test", "A TEST CAR FIRE")
sc("""And the timing was terrible. Road and Track said McLaren's sales fell from four thousand six hundred sixty-two cars in twenty nineteen to one thousand six hundred fifty-nine in twenty twenty, during the pandemic, then recovered only to about two thousand one hundred thirty-eight in twenty twenty-one. McLaren even sold its headquarters and leased it back to raise money.""",
   "McLaren Technology Centre", "SALES: 4,662 TO 1,659")
sc("""To reassure buyers, McLaren offered a five-year warranty, a six-year warranty on the battery, and three years of free servicing, Road and Track reported. Kelley Blue Book still lists a five-year, unlimited-mile warranty on the twenty twenty-five Artura. McLaren knew it had to win back trust.""",
   "McLaren Artura showroom", "5-YEAR WARRANTY")
sc("""Ferrari had its problems too. In October twenty twenty-three, Motor Authority reported that six hundred fourteen SF90s from the twenty twenty-two to twenty twenty-four model years were recalled in America, because turbo oil delivery pipes could leak and cause a fire. Owners were told not to drive the cars until the pipes were replaced for free.""",
   "Ferrari SF90 Stradale recall", "SF90: 614 CARS RECALLED")
sc("""So both cars had trouble. But the difference was the company behind them. Ferrari's recall was an issue on a successful car from a profitable company. McLaren's problems arrived while the whole company was fighting for money.""",
   "Ferrari Maranello factory", "SAME PROBLEMS, DIFFERENT COMPANIES")

# ---------- 8. A FERRARI MAN AT McLAREN ----------
ch("A Ferrari man at McLaren")
sc("""And then came the most surprising twist. Road and Track reported that McLaren's new chief executive was Michael Leiters, the former chief technology officer of Ferrari. The man who had helped develop Ferrari's cars was now in charge of fixing McLaren's.""",
   "McLaren Artura front", "EX-FERRARI CTO RUNS McLAREN")
sc("""The ownership changed too. Autocar New Zealand reported that Bahrain's sovereign fund, Mumtalakat, took control of McLaren in early twenty twenty-four. Then, in October twenty twenty-four, Business Day reported a deal for McLaren Automotive to be bought by CYVN Holdings of Abu Dhabi, an investor in electric vehicles.""",
   "McLaren Woking", "NEW OWNERS: MIDDLE EAST")
sc("""Meanwhile, the Artura kept improving. For twenty twenty-five, McLaren raised its power to about six hundred ninety horsepower and added the Artura Spider, a convertible. The car that had a troubled start became a more complete product.""",
   "McLaren Artura Spider", "UPDATE: ~690 HP + SPIDER")
sc("""The open versions repeat the price gap. CarGurus listed the twenty twenty-three SF90 Spider at about five hundred seventy thousand dollars, with a retractable hard top. Kelley Blue Book listed the twenty twenty-five Artura Spider at about two hundred seventy-nine thousand. Once again, the Ferrari costs about twice as much.""",
   "Ferrari SF90 Spider", "SPIDERS: $570K vs $279K")
sc("""And Ferrari kept pushing the SF90 upward. In twenty twenty-three it revealed the SF90 X X Stradale and X X Spider. Evo India reported about one thousand sixteen horsepower, seven hundred ninety-nine Stradales and five hundred ninety-nine Spiders, all sold, and called it the first road-legal model in Ferrari's X X program. McLaren had nothing like that based on the Artura.""",
   "Ferrari SF90 XX Stradale", "SF90 XX: 1,016 HP")

# ---------- 9. WHAT CAME NEXT ----------
ch("What came next")
sc("""Ferrari moved on from the SF90 fast. On the tenth of September twenty twenty-five, Motoring Research reported, Ferrari revealed the eight forty-nine Testarossa as its replacement, with about one thousand fifty horsepower, about fifty more than the SF90. It keeps the V8, three electric motors, and a plug-in battery of about seven point four five kilowatt hours.""",
   "Ferrari 849 Testarossa", "SF90 REPLACED: 849 TESTAROSSA")
sc("""And Ferrari went further. Its first fully electric car, the Luce, has an interior designed by LoveFrom, the studio of Jony Ive and Marc Newson. Electra's summary lists four motors, more than one thousand horsepower in boost mode, and first deliveries from October twenty twenty-six.""",
   "Ferrari Luce", "FERRARI LUCE: FULLY ELECTRIC")
sc("""McLaren's future is less certain. Autoevolution reported in twenty twenty-six that the Artura could be dropped around twenty twenty-eight, and that a new hybrid supercar, code-named P thirty-four, is expected to debut in twenty twenty-seven. The Artura's story may end sooner than its fans would like.""",
   "McLaren Artura rear view", "ARTURA: EXIT IN 2028?")
sc("""So here is the twist at the end. The car that cost twice as much was replaced after about five years by a more powerful version of the same idea. The cheaper car survived its troubled launch, but its maker changed owners, changed bosses, and is now planning what comes next.""",
   "Ferrari SF90 and McLaren Artura", "TWO DIFFERENT ENDINGS")

# ---------- 10. THE DIFFERENCE ----------
ch("The real difference")
sc("""So what is the real difference between the Ferrari SF90 and the McLaren Artura? It is not just power. It is the job each car had. The SF90 was a flagship, built to prove that Ferrari could make a hybrid faster than its own hypercar. Three motors, all-wheel drive, almost one thousand horsepower, and a price to match.""",
   "Ferrari SF90 Stradale", "SF90: THE FLAGSHIP")
sc("""The Artura was an entry model, built to bring hybrid technology to McLaren's most affordable series car. One motor, rear-wheel drive, a new lightweight chassis, and a price about half of the Ferrari's. Its real rival was the Ferrari two ninety-six G T B, not the SF90.""",
   "McLaren Artura", "ARTURA: THE ENTRY HYBRID")
sc("""Even inside, the two cars feel different. Autobuzz described the SF90's cockpit as a sixteen-inch curved digital display behind the steering wheel, controlled through touch pads and haptic buttons, with no central infotainment screen at all. Ferrari later went back to physical buttons on the eight forty-nine Testarossa, Motoring Research reported. The SF90's cabin was a bold experiment, and not everyone liked it.""",
   "Ferrari SF90 interior", "SF90: A BOLD COCKPIT")
sc("""And they share one surprising idea. Neither has a reverse gear. Both rely on electric motors to back out of a parking space. Two rival companies, two different philosophies, and the same quiet decision deep inside the gearbox.""",
   "Ferrari SF90 and McLaren Artura parked", "BOTH: NO REVERSE GEAR")
sc("""If you could have one, which would you choose? The flagship Ferrari with all-wheel drive, or the lighter rear-wheel-drive McLaren for half the price? Tell us in the comments. In the other videos of this series, we reveal two things most people don't know about the SF90, the real cost of owning one, and the story behind Ferrari's first plug-in hybrid.""",
   "Ferrari SF90 Stradale yellow", "WHICH WOULD YOU CHOOSE?")
sc("""And if your next vehicle is a truck instead of a supercar, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "McLaren Artura sunset", "SUBSCRIBE: PICKUP REALITY")

save("video70", "Ferrari SF90 vs McLaren Artura: The Difference Nobody Explains", [
    "Wikipedia, Ferrari SF90 Stradale: https://en.wikipedia.org/wiki/Ferrari_SF90_Stradale",
    "Wikipedia, McLaren Artura: https://en.wikipedia.org/wiki/McLaren_Artura",
    "Reuters via Euronews, Ferrari accelerates its move into hybrid cars (May 29, 2019): https://www.euronews.com/2019/05/29/ferrari-accelerates-its-move-into-hybrid-cars",
    "InsideEVs, SF90 Stradale is Ferrari's first plug-in hybrid: https://insideevs.com/news/352375/sf90-stradale-first-ferrari-plugin-hybrid/",
    "Design News, Magna 8-speed DCT in the SF90: https://www.designnews.com/automotive/ferrari-sf90-stradale-accelerates-through-gears-magnas-8-speed-dual-clutch-transmission",
    "duPont Registry, Ferrari SF90 Stradale review: https://news.dupontregistry.com/blogs/ferrari-news/ferrari-sf90-stradale-price-specs-photos-review",
    "CarGurus, 2023 Ferrari SF90 pricing: https://www.cargurus.com/research/2023-Ferrari-SF90-c32760",
    "Kelley Blue Book, 2025 McLaren Artura: https://www.kbb.com/mclaren/artura/2025/",
    "Carwow Spain, Ferrari 296 GTB vs McLaren Artura (June 2021): https://www.carwow.es/blog/comparativa-ferrari-296-gtb-vs-mclaren-artura",
    "Road & Track via Yahoo, Fire, glitches, delays: McLaren after the Artura launch (June 2022): https://autos.yahoo.com/fire-glitches-delays-mclaren-post-202000664.html",
    "Autobuzz, Facts & Figures: SF90 Stradale launched in Malaysia (2020): https://autobuzz.my/2020/09/18/facts-figures-ferrari-sf90-stradale-launched-in-malaysia/",
    "Evo India, SF90 XX Stradale revealed: https://www.evoindia.com/top-news/new-ferrari-sf90-xx-stradale-revealed",
    "Driven (NZ), LaFerrari was the world's first HEV hypercar: https://www.drivencarguide.co.nz/news/the-good-oil-laferrari-was-the-worlds-first-hev-hypercar/",
    "Wikipedia, McLaren P1: https://en.wikipedia.org/wiki/McLaren_P1",
    "Motor Authority, Ferrari SF90 recalled (Oct 2023): https://www.motorauthority.com/news/1141294_ferrari-sf90-recalled",
    "Autocar NZ, McLaren is now in Abu Dhabi hands: https://www.autocar.co.nz/mclaren-is-now-in-abu-dhabi-hands",
    "Business Day, McLaren Automotive to be bought by Abu Dhabi's CYVN Holdings (Oct 2024): https://www.businessday.co.za/bd/life/motoring/2024-10-31-mclaren-automotive-to-be-bought-by-abu-dhabis-cyvn-holdings/",
    "Autoevolution, Artura faces 2028 exit as P34 prepares for 2027 debut: https://www.autoevolution.com/news/v6-powered-mclaren-artura-faces-2028-exit-as-new-p34-hybrid-supercar-prepares-for-2027-debut-275652.html",
    "Motoring Research, Ferrari 849 Testarossa (Sept 2025): https://www.motoringresearch.com/car-news/2026-ferrari-849-testarossa/",
    "Electra, Ferrari Luce: everything we know: https://www.go-electra.com/en/newsroom/electric-ferrari-luce-price-power-and-everything-we-know/",
], "B")
