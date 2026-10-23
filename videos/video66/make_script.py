import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Two Italian supercars. Two six point five liter V12 engines. Both revealed within about a year of each other, both with eight-speed dual-clutch gearboxes, and both priced like a house. On paper, the Lamborghini Revuelto and the Ferrari twelve Cilindri look like twins. In reality, they are built on opposite answers to the same question.""",
   "Lamborghini Revuelto", "REVUELTO or 12CILINDRI?")
sc("""The question is simple. How do you keep a V12 alive in a world of emissions rules and electric cars? Lamborghini added three electric motors and a battery. Ferrari added nothing electric at all. And that single decision changes everything about how these two cars look, drive, and cost.""",
   "Ferrari 12Cilindri", "ONE ADDED ELECTRICITY. ONE DIDN'T.")
sc("""In this video we compare the engines, the layouts, the weight, the speed, the prices, and the verdict from a test that put both on the same track. And at the end, we will show you the real difference, the one that decides which car makes sense for which buyer. Every number is sourced in the description.""",
   "Ferrari 12Cilindri front", "THE REAL DIFFERENCE")
sc("""And here is the first twist. One of these cars has its V12 in front of the driver. The other has it behind. And that is not a styling choice. It goes back almost sixty years, to two rival companies and a tractor maker who wanted to beat Ferrari.""",
   "Lamborghini Revuelto rear", "FRONT vs BEHIND")

# ---------- 1. TWO FAMILIES OF V12 ----------
ch("Two families of V12")
sc("""Ferrari's V12 story starts at the very beginning of Ferrari. According to Ferrari's own magazine, Gioachino Colombo joined Enzo Ferrari in nineteen forty-six, and when Ferrari described a one point five liter engine plan, Colombo said he should be making a twelve-cylinder. The first prototype ran without bodywork on the twelfth of March, nineteen forty-seven.""",
   "Ferrari 125 S", "FERRARI'S FIRST V12, 1947")
sc("""Enzo Ferrari later called the V12 the crowning glory of his ambitions. It powered legends like the two fifty G T O, the Testarossa, and the Daytona S P three. And the twelve Cilindri's name says it all. It is Italian for twelve cylinders.""",
   "Ferrari 250 GTO", "THE CROWNING GLORY")
sc("""Lamborghini's V12 story starts as a challenge to Ferrari. Ferruccio Lamborghini, who made tractors, boilers, and air conditioners, founded Automobili Lamborghini in nineteen sixty-three to compete with Ferrari. His first series car, the three fifty G T, used a V12 designed by Giotto Bizzarrini.""",
   "Lamborghini 350 GT", "LAMBORGHINI'S V12, 1963")
sc("""Then, in nineteen sixty-six, Lamborghini placed the V12 behind the driver in the Miura, creating the layout most people now picture when they hear the word supercar. Since then, every flagship Lamborghini, the Countach, Diablo, Murcielago, Aventador, and now the Revuelto, has had a V12 behind the cabin.""",
   "Lamborghini Miura", "1966: THE V12 MOVES BEHIND")
sc("""So the twist is this. Ferrari's flagship V12 grand tourers kept the engine in front, in the tradition of the Daytona and the eight twelve Superfast. Lamborghini's V12 flagships put it in the middle. Two companies, less than an hour's drive apart in Italy, building the same kind of engine in opposite places for six decades.""",
   "Ferrari 812 Superfast", "A FEW KILOMETERS, OPPOSITE IDEAS")

# ---------- 2. THE ENGINES ----------
ch("The engines")
sc("""The Revuelto uses a six point five liter V12 called the L five forty-five, a reworked version of the Aventador's engine according to Top Gear. It makes about eight hundred fourteen horsepower on its own at nine thousand two hundred fifty r p m. With three electric motors, total output is one thousand and one horsepower.""",
   "Lamborghini Revuelto V12", "REVUELTO: 1,001 HP HYBRID")
sc("""The twelve Cilindri uses Ferrari's six point five liter F one forty V12. Top Gear says that engine family traces its roots back to the Ferrari Enzo and is more than twenty years old. In the twelve Cilindri it makes eight hundred thirty metric horsepower, which is eight hundred nineteen horsepower, at nine thousand two hundred fifty r p m, with a redline of nine thousand five hundred.""",
   "Ferrari 12Cilindri engine", "12CILINDRI: 819 HP, NO HYBRID")
sc("""Look closely and the V12s are almost identical in size and power. The Lamborghini engine makes about eight hundred fourteen horsepower, and the Ferrari makes about eight hundred nineteen. So the gap of almost two hundred horsepower between the cars comes entirely from Lamborghini's electric motors.""",
   "Ferrari 12Cilindri rear", "THE GAP IS ALL ELECTRIC")
sc("""And here is the twist about the Ferrari. Autocar reported that Ferrari invested heavily to make its biggest engine meet new emissions rules, so it could keep selling a pure V12 to customers who wanted one. Ferrari did not avoid the future by accident. It paid to keep the past alive.""",
   "Ferrari 12Cilindri Miami", "FERRARI PAID TO KEEP IT PURE")
sc("""Top Gear's verdict on the engines was clear. In its twenty twenty-five Performance Car of the Year test, the writer judged the Ferrari's V12 the best engine of the three cars tested, and called it the world's greatest powerplant. The Revuelto had more power, but the Ferrari had the engine people talked about.""",
   "Ferrari V12 engine", "THE WORLD'S GREATEST POWERPLANT?")

sc("""Both cars also replaced famous predecessors. The twelve Cilindri replaced the eight twelve Superfast, and Top Gear noted that Ferrari's V12 has gained about ninety horsepower since twenty fifteen. The Revuelto replaced the Aventador, which was built from twenty eleven to twenty twenty-two, about eleven thousand four hundred sixty-five cars in total, and Lamborghini's V12 output has grown by about three hundred eleven horsepower since twenty fifteen, according to the same test.""",
   "Lamborghini Aventador", "+90 HP vs +311 HP SINCE 2015")
sc("""That one comparison sums up the two strategies. Ferrari added a little power to an already great engine, year by year. Lamborghini made a giant leap by adding electric motors. Since twenty fifteen, one brand refined, and the other transformed.""",
   "Ferrari 812 Superfast", "REFINE vs TRANSFORM")
# ---------- 3. THE LAYOUTS ----------
ch("Layout and weight")
sc("""Now the layout. The twelve Cilindri is front-engined and rear-wheel drive, with four-wheel steering, according to Wikipedia. The V12 sits ahead of the driver, behind the front axle, and all the power goes to the rear wheels.""",
   "Ferrari 12Cilindri side view", "FERRARI: FRONT ENGINE, REAR DRIVE")
sc("""The Revuelto puts the V12 behind the driver, with an eight-speed dual-clutch gearbox mounted sideways behind the engine. It has one electric motor on the gearbox and two at the front, one per wheel, so it is all-wheel drive. Its small battery runs through the center tunnel between the seats.""",
   "Lamborghini Revuelto side view", "LAMBORGHINI: MID ENGINE, ALL WHEELS")
sc("""Weight follows from those choices. Motor1 lists the twelve Cilindri at one thousand five hundred sixty kilograms, and the Revuelto at one thousand seven hundred seventy-two kilograms, both dry. That is a difference of more than two hundred kilograms, or about four hundred seventy pounds, and most of it is the hybrid system and all-wheel drive.""",
   "Lamborghini Revuelto carbon", "212 KG DIFFERENCE")
sc("""The shapes are different too. The Revuelto is lower and wider, about one point one six meters tall, while the twelve Cilindri is about one point two nine meters. The Lamborghini is a wedge. The Ferrari has a long hood and a cabin set far back, which is the classic shape of a front-engined grand tourer.""",
   "Ferrari 12Cilindri profile", "A WEDGE vs A LONG HOOD")
sc("""And the twist in design is a tribute. Wikipedia says the twelve Cilindri's design pays tribute to the Ferrari three sixty-five G T B four Daytona, including a black band across the hood that cannot be removed or recolored. The Revuelto continues the sharp-edged style that goes back to Marcello Gandini's Lamborghinis, with Y-shaped lights front and rear.""",
   "Ferrari Daytona 365 GTB/4", "A TRIBUTE TO THE DAYTONA")
sc("""The Daytona nickname itself has a great story. Ferrari says that at the twenty-four hours of Daytona on the fourth of February nineteen sixty-seven, three Ferraris crossed the line side by side, one, two, three, as payback after Ford's GT40 beat Ferrari in nineteen sixty-six. The three sixty-five G T B four, launched in nineteen sixty-eight, became known as the Daytona.""",
   "Ferrari 330 P4", "DAYTONA 1967: 1-2-3")

# ---------- 4. SPEED ----------
ch("Speed")
sc("""Now speed. On the official numbers, the Revuelto is quicker. It reaches one hundred kilometers per hour in two point five seconds, versus two point nine for the twelve Cilindri. Top speed is about three hundred fifty kilometers per hour for the Lamborghini and three hundred forty for the Ferrari.""",
   "Lamborghini Revuelto acceleration", "2.5 vs 2.9 SECONDS")
sc("""Zero to two hundred tells the same story. Wikipedia lists six point six seconds for the Revuelto and seven point nine for the twelve Cilindri. Part of that is power, and part is traction. With all-wheel drive and electric motors at the front, the Revuelto can put its power down from a standstill much more easily.""",
   "Ferrari 12Cilindri acceleration", "6.6 vs 7.9 SECONDS TO 200")
sc("""But the twist came on the racetrack. Top Gear called the Revuelto its winner on track, and said its chassis can keep pace with its engine. It praised the car's balance and composure despite one thousand and one horsepower.""",
   "Lamborghini Revuelto track", "TOP GEAR: REVUELTO WINS ON TRACK")
sc("""The Ferrari got a harder review on track. Top Gear praised its engine, throttle response, gearbox, and brakes, but criticized a chassis that magnifies steering inputs and oversteers at track speeds, calling it the hardest of the three to drive quickly. So the car with the best engine was not the best car on a circuit.""",
   "Ferrari 12Cilindri track", "BEST ENGINE, HARDEST TO DRIVE FAST")
sc("""And Lamborghini has gone further since. In August twenty twenty-six, it revealed the Revuelto S V, with about one thousand fifty-one horsepower and about eighty percent more downforce. Auto123 reported that it lapped the Hockenheimring in one minute forty-one point six seconds, the fastest production car time there. Ferrari's twelve Cilindri has no answer of that kind yet.""",
   "Lamborghini Revuelto SV", "THE SV RAISES THE STAKES")

# ---------- 4b. BRAKES, AERO AND TIRES ----------
ch("Brakes, aero and tires")
sc("""The details under the skin show the same split. The twelve Cilindri uses brake-by-wire, with discs of three hundred ninety-eight millimeters at the front and three hundred sixty at the rear, according to Wikipedia. Brake-by-wire means the pedal sends an electronic signal, and the system decides how hard to squeeze the discs.""",
   "Ferrari 12Cilindri brakes", "FERRARI: BRAKE-BY-WIRE")
sc("""The Revuelto's brakes are even bigger, because the car is heavier and faster. Wikipedia lists carbon-ceramic discs of four hundred ten millimeters at the front with ten-piston calipers, and three hundred ninety millimeters at the rear. And its front electric motors can also slow the car by recovering energy, which helps refill the small battery.""",
   "Lamborghini Revuelto brakes", "LAMBORGHINI: 10-PISTON CALIPERS")
sc("""Aerodynamics are a big difference. Motor1 said the Revuelto's active rear spoiler is the main aerodynamic difference between the two cars. Car and Driver reported that the Revuelto makes seventy percent more downforce than the Aventador. The Ferrari takes a quieter approach. Wikipedia says the sides of its rear spoiler can tilt up to ten degrees, creating about fifty kilograms of downforce at high speed.""",
   "Lamborghini Revuelto rear wing", "ACTIVE AERO vs HIDDEN AERO")
sc("""Here is the twist. The Ferrari's aero is designed to keep the shape clean. Its goal, according to Wikipedia, was to lower drag compared with the eight twelve Superfast. The Lamborghini wears its aero proudly, with a big active wing and a working diffuser made possible by its sideways gearbox. One car hides its tricks. The other shows them off.""",
   "Ferrari 12Cilindri rear", "ONE HIDES, ONE SHOWS OFF")
sc("""Tires tell the same story. The twelve Cilindri rides on twenty-one inch wheels at both ends, with Michelin Pilot Sport S five or Goodyear Eagle F one Supersport tires, according to Wikipedia. Those are road tires built for a grand tourer. The Revuelto's job on track asks for more grip, and its all-wheel drive spreads the load over four tires instead of two.""",
   "Ferrari 12Cilindri wheel", "21-INCH WHEELS")

# ---------- 4c. LIVING WITH THEM ----------
ch("Living with them")
sc("""Now everyday life. Kelley Blue Book lists the Revuelto at about twelve miles per gallon combined, ten in the city and seventeen on the highway, on premium fuel. Jalopnik's test car carried a gas guzzler tax of four thousand five hundred dollars. The small battery adds an electric city mode, but it is not built for long electric driving.""",
   "Lamborghini Revuelto city", "12 MPG COMBINED")
sc("""The warranty is similar on paper. Kelley Blue Book lists three years and unlimited miles of basic and powertrain coverage for both cars in the United States. In the United Kingdom, Autocar reported a four-year warranty for the Ferrari, plus the seven years of routine servicing.""",
   "Ferrari 12Cilindri parked", "3 YEARS, UNLIMITED MILES")
sc("""And the twist for daily use is the front end. A front-engined grand tourer like the twelve Cilindri has a long hood and a cabin that sits higher, at about one point two nine meters tall. The Revuelto sits about thirteen centimeters lower and opens its doors upward. One is easier to get in and out of every day. The other turns every arrival into a show.""",
   "Lamborghini Revuelto doors open", "EVERY ARRIVAL IS A SHOW")

# ---------- 5. INSIDE ----------
ch("Inside")
sc("""Inside, both cars are full of screens. Motor1 counted a fifteen point five inch driver display in the Ferrari, a ten point two five inch central screen, and an eight point eight inch passenger display. Wikipedia says it is the first Ferrari grand tourer without an analog gauge.""",
   "Ferrari 12Cilindri interior", "FERRARI: NO ANALOG GAUGE")
sc("""The Revuelto has a twelve point three inch driver display, an eight point four inch vertical central screen, and a nine point one inch passenger screen, according to Car and Driver. And it keeps a Lamborghini signature from the Aventador, a start button hidden under a red cover that you lift like a switch in a fighter jet.""",
   "Lamborghini Revuelto interior", "LAMBORGHINI: THE RED FLAP")
sc("""Here is the twist. Both brands added passenger screens, so the person in the right seat can see speed and data. It is a small detail, but it shows who these cars are for. They are not track tools for one driver. They are shows for two people.""",
   "Ferrari 12Cilindri passenger display", "A SHOW FOR TWO")
sc("""And one of them can open the sky. Ferrari offers the twelve Cilindri as a coupe and as a Spider with a retractable hard top. The Revuelto, in the versions covered by our sources, is a coupe. So if open-air V12 driving matters to you, the Ferrari is the one that offers it from the factory.""",
   "Ferrari 12Cilindri Spider", "COUPE AND SPIDER")

# ---------- 6. PRICE ----------
ch("Price")
sc("""Now the money. In the United States, Kelley Blue Book lists the twenty twenty-five twelve Cilindri coupe at a starting price of four hundred seventy-two thousand dollars, and the Spider at five hundred fifteen thousand.""",
   "Ferrari 12Cilindri price", "12CILINDRI FROM $472,000")
sc("""For the Revuelto, Kelley Blue Book lists a twenty twenty-six starting sticker of about six hundred seventy-three thousand dollars. Jalopnik's October twenty twenty-six test car had a base price of six hundred sixty-four thousand seven hundred ninety-nine dollars and came to eight hundred six thousand five hundred twenty-one with options, destination, and a gas guzzler tax.""",
   "Lamborghini Revuelto purple", "REVUELTO FROM ~$673,000")
sc("""So the Lamborghini costs about two hundred thousand dollars more to start, in the United States. You could buy a Ferrari twelve Cilindri and still have enough left over for a very nice second sports car. That is the price of the hybrid system, the all-wheel drive, and the extra two hundred horsepower.""",
   "Lamborghini Revuelto and Ferrari", "~$200,000 DIFFERENCE")
sc("""Options are expensive on both. Autocar listed a bespoke Ferrari paint color at almost forty thousand pounds in the United Kingdom, and massaging seats at almost nine thousand pounds. Jalopnik listed two carbon fiber packs on the Revuelto at a combined fifty thousand six hundred one dollars, more than the average new car in America.""",
   "Ferrari 12Cilindri options", "OPTIONS COST LIKE CARS")
sc("""And there is one more money difference that most people miss. In the U K, Autocar said Ferrari covers all routine servicing for the first seven years on the twelve Cilindri. Lamborghini does not advertise the same kind of program in the sources we found. Over years of ownership, that can narrow the gap.""",
   "Ferrari service", "7 YEARS OF FREE SERVICING")

# ---------- 7. DEMAND AND VALUE ----------
ch("Demand and value")
sc("""Demand has been strong for both. Motor Authority reported in July twenty twenty-three that the Revuelto was sold out for about two years before deliveries began. Lamborghini built one thousand four hundred six Revueltos in twenty twenty-four, according to Wikipedia, and the brand delivered a record ten thousand six hundred eighty-seven cars that year.""",
   "Lamborghini Revuelto production", "SOLD OUT FOR 2 YEARS")
sc("""The twelve Cilindri was revealed in Miami Beach on the third of May twenty twenty-four, marking seventy years of Ferrari in the American market. That location was not an accident. America is one of the most important markets for both brands, and both cars are aimed straight at it.""",
   "Miami Beach", "REVEALED IN MIAMI")
sc("""On the used market, autoevolution reported in October twenty twenty-six that used Revueltos start around six hundred thousand dollars and can reach almost nine hundred thousand. A two-year-old Revuelto with six thousand miles was offered at about six hundred thirty thousand. That means many have held value close to their sticker.""",
   "Lamborghini Revuelto blue", "USED: $600K TO $900K")
sc("""And here is the twist about the future. Lamborghini has already shown a faster version, the S V, limited to one thousand nine hundred sixty-three cars. Ferrari's twelve Cilindri is still its pure V12 grand tourer. If emissions rules tighten further, a naturally aspirated V12 without a battery may become one of the rarest things in the car world.""",
   "Ferrari 12Cilindri red", "PURE V12: SOON TO BE RARE?")

# ---------- 8. THE OTHER RIVAL ----------
ch("The third V12")
sc("""There is also a third car in this fight. Top Gear's test included the Aston Martin Vanquish, with a twin-turbo V12. Autocar reported that it makes about eight hundred twenty-four horsepower, almost exactly the Ferrari's number, with broadly similar performance.""",
   "Aston Martin Vanquish", "THE ASTON MARTIN VANQUISH")
sc("""Top Gear's writer said the Aston was more satisfying than the Ferrari, although less intimidating and less agile, and praised its torque. So in one test, three V12 cars came to three very different verdicts. The Lamborghini won on track, the Ferrari had the best engine, and the Aston was the most satisfying to drive.""",
   "Aston Martin Vanquish rear", "THREE CARS, THREE VERDICTS")
sc("""That tells you something important. The V12 is no longer one formula. One brand added electricity. One stayed pure and naturally aspirated. One added turbochargers. They are all trying to keep twelve cylinders alive, and none of them agree on how.""",
   "V12 engine", "NO ONE AGREES ON THE V12")

# ---------- 9. THE REAL DIFFERENCE ----------
ch("The real difference")
sc("""So what is the real difference? It is not the engine size, because both are six point five liters. It is not even the V12 power, because they are within a few horsepower of each other. The real difference is what each brand added, or chose not to add, around that engine.""",
   "Lamborghini Revuelto front", "NOT SIZE, NOT V12 POWER")
sc("""The Revuelto added three electric motors, a battery, and all-wheel drive. That made it heavier and more expensive, but also faster, easier to use on track, and able to drive on electricity for a few miles. It is a supercar that uses technology to go further than any Lamborghini V12 before it.""",
   "Lamborghini Revuelto track", "REVUELTO: TECHNOLOGY TO GO FURTHER")
sc("""The twelve Cilindri kept its V12 pure, with the engine in front and power only to the rear wheels. That made it lighter, cheaper by about two hundred thousand dollars in the United States, and, according to Top Gear, home to the best engine of the test. But it is harder to drive quickly on a racetrack.""",
   "Ferrari 12Cilindri road", "12CILINDRI: A PURE V12")
sc("""So if you want the fastest, most dramatic V12 experience on a track, the Revuelto is the answer. If you want the purest V12 sound and response on long roads, in a grand tourer that pays tribute to the Daytona, the twelve Cilindri is the answer. Tell us in the comments which one you would choose.""",
   "Ferrari 12Cilindri and Lamborghini", "WHICH ONE WOULD YOU CHOOSE?")
sc("""And watch the other videos in this Revuelto series, two secrets hidden inside the car, what it really costs to own one, and the story of why Lamborghini built it this way. If you are shopping for something more practical, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Lamborghini Revuelto sunset", "SUBSCRIBE: PICKUP REALITY")

save("video66", "Lamborghini Revuelto or Ferrari 12Cilindri? The Real Difference", [
    "Wikipedia, Lamborghini Revuelto: https://en.wikipedia.org/wiki/Lamborghini_Revuelto",
    "Wikipedia, Ferrari 12Cilindri: https://en.wikipedia.org/wiki/Ferrari_12Cilindri",
    "Wikipedia, Lamborghini (history): https://en.wikipedia.org/wiki/Lamborghini",
    "Motor1, Ferrari 12Cilindri vs Lamborghini Revuelto (June 2024): https://www.motor1.com/news/723932/ferrari-12cilindri-versus-lamborghini-revuelto-comparison/",
    "Top Gear, PCOTY 2025: Vanquish vs 12Cilindri vs Revuelto: https://www.topgear.com/car-news/pcoty-2025/v12-victory-aston-martin-vanquish-vs-ferrari-12cilindri-vs-lamborghini-revuelto",
    "Ferrari magazine, Mythbusters: the first Ferrari V12: https://ferrari.com/en-CA/magazine/articles/mythbusters-the-first-ferrari-v12",
    "Ferrari magazine, the race that inspired an icon (Daytona 1967): https://www.ferrari.com/magazine/articles/the-race-that-inspired-an-icon",
    "Autocar, Ferrari 12Cilindri priced from £336,500: https://autocar.co.uk/car-news/new-cars/ferrari-12cilindri-priced-%C2%A3336500-spider-adds-%C2%A330k",
    "Kelley Blue Book, Ferrari 12Cilindri: https://www.kbb.com/ferrari/12cilindri/",
    "Kelley Blue Book, Lamborghini Revuelto: https://www.kbb.com/lamborghini/revuelto/",
    "Jalopnik, Revuelto carbon options (Oct 2026): https://www.jalopnik.com/2288310/lamborghini-revuelto-optional-carbon-fiber-costs-more-than-average-new-car/",
    "Car and Driver via Yahoo Autos, Revuelto: https://autos.yahoo.com/revuelto-1001-hp-hybrid-v-131900739.html",
    "Auto123, Revuelto SV debut (Aug 2026): https://www.auto123.com/en/news/lamborghini-revuelto-sv-debut-monterey/74145/",
    "Motor Authority, Revuelto sold out for 2 years: https://www.motorauthority.com/news/1140333_lamborghini-revuelto-already-sold-out-for-next-2-years",
    "duPont Registry, Lamborghini 2024 deliveries: https://news.dupontregistry.com/blogs/lamborghini-news/lamborghini-celebrates-a-record-breaking-year-with-10687-new-car-deliveries",
    "autoevolution, used Revuelto values (Oct 2026): https://www.autoevolution.com/news/how-much-is-a-2024-lamborghini-revuelto-worth-today-after-6000-miles-276767.html",
], "B")
