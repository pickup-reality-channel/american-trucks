import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Thirty-two years separate the McLaren F one and the McLaren W one. The W one has about twice the horsepower, goes from zero to sixty in two point seven seconds, and costs several times more. And yet there is one important number where the old car still wins. Today we compare the two, line by line, and explain the difference that nobody explains.""",
   "McLaren F1", "McLAREN F1 vs McLAREN W1")
sc("""Here is the hint. McLaren itself calls the new W one the fastest-accelerating road-legal car it has ever built. But the F one has a top speed record that the W one does not even try to match. So which one is really the better car? The honest answer depends on what you mean by better.""",
   "McLaren W1", "WHICH IS BETTER?")
sc("""Every figure in this video comes from a published source, listed in the description. Where a number is an estimate, or our own arithmetic, we will say so. Let's start with where these two cars came from.""",
   "McLaren F1 and McLaren W1", "EVERY FIGURE IS SOURCED")

# ---------- 1. TWO CARS, ONE NAME ----------
ch("Two cars, one story")
sc("""The F one came first. Wikipedia says designer Gordon Murray conceived it as an exercise in creating the ultimate road-going sports car, and describes his design concept simply: low weight and high power. Production ran from nineteen ninety-two to nineteen ninety-eight, and only one hundred six cars were manufactured.""",
   "McLaren F1", "THE ORIGINAL: LOW WEIGHT, HIGH POWER")
sc("""The W one is the new one. Wikipedia says it was unveiled on the sixth of October, twenty twenty-four, and calls it the successor to the McLaren P one. Production was scheduled to begin in twenty twenty-five and was limited to three hundred ninety-nine units, though the page tags that date as needing an update.""",
   "McLaren W1", "THE NEW ONE: UNVEILED OCTOBER 2024")
sc("""Car and Driver, in a story republished by the Daily Maverick, says the W one arrives for the fiftieth anniversary of McLaren's first Formula One constructors' championship, won with driver Emerson Fittipaldi, who also won the drivers' championship in nineteen seventy-four. The company, the story says, has Formula One on the brain.""",
   "Emerson Fittipaldi McLaren 1974", "50 YEARS SINCE McLAREN'S FIRST TITLE")
sc("""McLaren's own chief executive, Michael Leiters, called the W one a celebration of both the iconic McLaren F one and the McLaren P one, according to GoAuto. So the new car is meant to honor the old one. That is exactly why the comparison is fair, and why the differences are so interesting.""",
   "McLaren P1", "A CELEBRATION OF THE F1 AND THE P1")
sc("""There was a middle step. Car and Driver says McLaren began developing the hybrid system more than ten years earlier with the nine hundred three horsepower P one, which launched in twenty thirteen. The W one has one thousand two hundred fifty-eight horsepower, about thirty-nine percent more than the P one, by our own arithmetic.""",
   "McLaren P1 front", "P1: 903 HP IN 2013")
sc("""Car and Driver lists the stops along the way. The Speedtail hybrid made its debut in twenty eighteen at two point three million dollars. The Artura, a less expensive hybrid, came out in twenty twenty-one at two hundred thirty-three thousand dollars. So the W one, at two point one million, actually starts below the Speedtail, by about nine percent, by our own arithmetic.""",
   "McLaren Speedtail rear", "SPEEDTAIL $2.3M, ARTURA $233K")
sc("""The two cars also had very different starts. Gooding and Company says McLaren Cars was set up in nineteen eighty-nine, production of the F one began in nineteen ninety-two, and the first cars reached customers in nineteen ninety-three. Motor Authority adds that the team that created it came together for the first time in nineteen ninety.""",
   "McLaren F1 factory Woking", "THE F1 TEAM FORMED IN 1990")

# ---------- 2. ENGINES ----------
ch("The engines")
sc("""Start with the F one's engine. Wikipedia says it was a BMW S seventy slash two, a sixty-degree V twelve of six thousand sixty-four cubic centimeters, designed by BMW's motorsport division. It made six hundred eighteen horsepower at seven thousand four hundred r p m, and four hundred seventy-nine pound-feet of torque at five thousand six hundred.""",
   "BMW S70/2 V12", "F1: 6.1L V12, 618 HP")
sc("""It was naturally aspirated, which Gooding and Company says was one of Gordon Murray's non-negotiables. No turbochargers. It was also, Wikipedia says, a heavy piece of equipment by racing standards, at two hundred sixty-six kilograms, five hundred eighty-six pounds. But for the nineteen nineties, it was extremely light for a V twelve.""",
   "BMW V12 engine", "NATURALLY ASPIRATED, NO TURBOS")
sc("""Now the W one. Wikipedia says its engine is the McLaren M H P eight, a three thousand nine hundred eighty-eight cubic centimeter twin-turbo V eight. GoAuto adds that it is a ninety-degree V eight with a flat-plane crank, redlining at nine thousand two hundred r p m, and producing six hundred eighty-two kilowatts.""",
   "McLaren MHP-8 V8", "W1: 4.0L TWIN-TURBO V8")
sc("""Six hundred eighty-two kilowatts is about nine hundred fifteen horsepower, by our own arithmetic. That means the W one's gasoline engine alone makes about forty-eight percent more power than the entire F one. And that is before the electric motor. GoAuto says the engine's output per liter is a new record for McLaren, at one hundred seventy-one kilowatts per liter.""",
   "McLaren engine dyno", "THE V8 ALONE: ~915 HP")
sc("""Then comes the electric part. Wikipedia says the W one's E-module contributes up to two hundred fifty-five kilowatts, about three hundred forty-seven metric horsepower. Together, the engine and motor produce one thousand two hundred seventy-five metric horsepower, which Wikipedia converts to one thousand two hundred fifty-eight brake horsepower.""",
   "McLaren W1 hybrid powertrain", "+ 255 kW ELECTRIC MOTOR")
sc("""The torque tells the same story. Wikipedia lists one thousand three hundred forty newton-meters, about nine hundred eighty-eight pound-feet, for the W one. The F one made six hundred fifty newton-meters. By our own arithmetic, the new car has roughly twice the torque of the old one, and about twice the power.""",
   "McLaren W1 rear", "1,340 Nm vs 650 Nm")
sc("""The power per liter shows how different the philosophies are. The F one made about one hundred two horsepower per liter, by our own arithmetic, from its six point one liter V twelve. The W one's whole system, engine and motor together, makes about three hundred fifteen horsepower per liter of engine displacement.""",
   "McLaren engine comparison", "~102 HP/L vs ~315 HP/L (OUR MATH)")
sc("""Even the engine speed has changed. The F one's rev limiter was raised to eight thousand three hundred r p m for the record run, Wikipedia says, and peak power came at seven thousand four hundred. The W one's V eight redlines at nine thousand two hundred, which is about eleven percent higher than that raised limit, by our own arithmetic.""",
   "McLaren tachometer", "9,200 RPM REDLINE")

# ---------- 3. WEIGHT ----------
ch("The weight")
sc("""Now the weight, where the F one's design shows. Wikipedia lists eleven hundred forty kilograms dry, two thousand five hundred thirteen pounds, and twelve hundred sixty kilograms ready to drive. The W one, Wikipedia says, has a dry weight of thirteen hundred ninety-nine kilograms, three thousand eighty-four pounds.""",
   "McLaren F1 weight", "1,140 KG vs 1,399 KG")
sc("""The difference is two hundred fifty-nine kilograms, about twenty-three percent more, by our own arithmetic. A new car that is two hundred sixty kilograms heavier than a nineteen nineties car sounds like a step backward. But look at what the extra weight carries.""",
   "McLaren W1 carbon chassis", "+259 KG, +23% (OUR MATH)")
sc("""It carries a hybrid system, an electric motor, a battery, and enough structure to survive twice the power and far higher aerodynamic loads. GoAuto says the W one has a best-in-class power-to-weight ratio of six hundred seventy kilowatts per tonne. Wikipedia says nine hundred eleven metric horsepower per tonne.""",
   "McLaren W1 battery hybrid", "RECORD POWER-TO-WEIGHT")
sc("""Now the same calculation for the F one. Six hundred eighteen horsepower divided by eleven hundred forty kilograms is about point five four horsepower per kilogram. The W one, at twelve hundred fifty-eight horsepower on thirteen hundred ninety-nine kilograms, is about point nine, by our own arithmetic. That is roughly sixty-six percent higher.""",
   "McLaren power to weight", "0.54 vs 0.90 HP/KG (OUR MATH)")
sc("""Both cars used expensive materials to save weight. Gooding and Company says the F one used carbon fiber, titanium, magnesium and Kevlar. Wikipedia adds the engine bay's gold foil, about sixteen grams per car. The W one's equivalent is its carbon monocoque and forged wheels. The principle is the same, but the budget per gram has grown.""",
   "McLaren F1 gold foil", "TITANIUM, KEVLAR, GOLD FOIL")

# ---------- 4. ACCELERATION ----------
ch("Acceleration")
sc("""Now to speed. The F one's zero to sixty time is three point two seconds, according to SlashGear, which does not name the tester. Gooding and Company gives zero to one hundred kilometers per hour in three point three seconds. In nineteen ninety-two, those numbers were unmatched.""",
   "McLaren F1 acceleration", "F1: 0-60 IN 3.2 SECONDS")
sc("""The W one is quicker. Car and Driver, republished by the Daily Maverick, says zero to sixty miles per hour takes two point seven seconds. Zero to one hundred twenty-four miles per hour, which is two hundred kilometers per hour, takes five point eight seconds, and zero to one hundred eighty-six miles per hour takes twelve point seven.""",
   "McLaren W1 launch", "W1: 0-60 IN 2.7 SECONDS")
sc("""Car and Driver says that makes it quicker than the McLaren Speedtail. And McLaren's chief executive claimed, in GoAuto's report, that the W one is the company's fastest-lapping and fastest-accelerating road-legal car ever. So on acceleration, the new car clearly wins.""",
   "McLaren Speedtail", "FASTEST-ACCELERATING McLAREN EVER")
sc("""Put the first number in perspective. The W one's zero to sixty time is half a second shorter than the F one's, three point two against two point seven. That is about sixteen percent less time, by our own arithmetic. Thirty-two years of progress, and the improvement in the first few seconds is smaller than the improvement in power.""",
   "McLaren F1 launch control", "0.5 SECOND FASTER TO 60 (OUR MATH)")
sc("""SlashGear says the F one takes twenty-eight seconds to reach two hundred miles per hour, without citing a source. The W one reaches one hundred eighty-six in twelve point seven. Those are not the same speeds, so we cannot compare them directly. But they show where the new car's advantage grows. The higher the speed, the more the electric boost matters.""",
   "McLaren speed run", "F1: 200 MPH IN 28 SEC. W1: 186 MPH IN 12.7")

# ---------- 5. TOP SPEED ----------
ch("Top speed: the twist")
sc("""Now the number where the old car wins. Wikipedia says that on the thirty-first of March, nineteen ninety-eight, Andy Wallace drove an F one prototype at Volkswagen's Ehra-Lessien test track. The two-way average was two hundred forty point one miles per hour, with a peak of two hundred forty-three.""",
   "Ehra-Lessien test track McLaren F1", "F1: 240.1 MPH RECORD")
sc("""The page adds that for the run, the rev limiter was raised to eight thousand three hundred r p m. Gooding and Company says the production F one was electronically limited to two hundred thirty-one miles per hour, and that the car held the record for the world's fastest production car from nineteen ninety-eight until two thousand five.""",
   "McLaren F1 record run", "THE LIMITER WAS RAISED FOR THE RECORD")
sc("""The W one's top speed is lower. Wikipedia gives an estimated top speed of three hundred fifty kilometers per hour, about two hundred seventeen miles per hour. GoAuto calls it electronically limited. So a car with twice the power tops out slower than the nineteen nineties record run, by about twenty-three miles per hour, by our own arithmetic.""",
   "McLaren W1 speed", "W1: 217 MPH (350 KM/H)")
sc("""Why? Because the cars are built for different jobs. Wikipedia says the W one has maximum total downforce of one thousand kilograms in internal wind tunnel tests. GoAuto says it lowers its ride height by thirty-seven millimeters at the front and seventeen at the rear, and has an active long tail rear wing that extends three hundred millimeters.""",
   "McLaren W1 active rear wing", "1,000 KG OF DOWNFORCE")
sc("""That wing can act as a downforce aid, an air brake, and a D R S mode, Wikipedia says, with its motors controlled electrically. A car designed to make grip at high speed in corners will not always chase the highest straight-line number. Chief executive Michael Leiters said the design allows a supreme track driving experience from the same car.""",
   "McLaren W1 DRS wing", "DESIGNED FOR CORNERS, NOT A RECORD")
sc("""McLaren's director of product planning, Jamie Corstorphine, told Car and Driver that these are the first principles of a real supercar. Leiters called the W one a car that only McLaren could create. Whatever you think of the marketing, both cars share a principle. Build around the driver, and let physics set the rest.""",
   "McLaren design studio", "\"THE FIRST PRINCIPLES OF A REAL SUPERCAR\"")

# ---------- 6. THE CAR AROUND THE DRIVER ----------
ch("The cockpit and the chassis")
sc("""Now the way you sit. The F one's most famous feature is that the driver sits in the middle. Wikipedia says the seat is positioned in the middle of the car, ahead of the fuel tank and the engine. Gooding and Company says it is a three-seat layout, with two passengers flanking the driver.""",
   "McLaren F1 central driving position", "F1: DRIVER IN THE MIDDLE")
sc("""The W one is different. GoAuto says its seats, pedals, steering wheel and primary controls can all be moved. The articles we found do not describe the seating layout in more detail. So we will not claim anything about it, except that the car was designed around the driver's position in a very different way.""",
   "McLaren W1 cockpit", "W1: SEATS AND PEDALS MOVE")
sc("""Both cars are built around carbon fiber. Gooding and Company says the F one was the first road car with a full carbon fiber chassis. GoAuto says the W one's chassis is called a McLaren Aerocell and is a carbon fiber monocoque, with anhedral doors optimized for aerodynamic performance.""",
   "McLaren Aerocell carbon monocoque", "BOTH BUILT ON CARBON FIBER")
sc("""Brakes show how technology moved on. Gooding and Company says Murray wanted carbon brakes for the F one, but the technology was still in its infancy. The W one has carbon ceramic discs, three hundred ninety millimeters at the front and rear, GoAuto says, with nineteen-inch forged wheels at the front and twenty-inch wheels at the rear.""",
   "McLaren carbon ceramic brakes", "CARBON CERAMIC, 390 MM")
sc("""The F one's tires were two hundred thirty-five forty-five seventeen at the front, and three hundred fifteen forty-five seventeen at the rear, Wikipedia says. The W one wears Pirelli P Zero Trofeo tires on wheels two or three inches larger. Even the tires show how much more the new car has to handle.""",
   "Pirelli tire McLaren", "17-INCH WHEELS vs 19/20-INCH")
sc("""And the gearbox. The F one had a transversely mounted six-speed manual, Gooding and Company says, driving the rear wheels. The W one has an eight-speed transmission with an electric reverse and a hydraulic electronic differential, GoAuto says. One car you shift yourself. The other shifts for you.""",
   "McLaren F1 gearbox shifter", "6-SPEED MANUAL vs 8-SPEED")
sc("""Design is different too. Gooding and Company credits the F one's exterior to Peter Stevens, and describes a simple, elegant shape not dictated only by aerodynamics. Wikipedia credits the W one's interior to designer Alex Alexiev. One car was shaped to look calm. The other is shaped by active aerodynamics and a rear wing that moves.""",
   "McLaren F1 exterior design", "STEVENS (F1) vs ALEXIEV (W1)")

# ---------- 7. THE ELECTRIC QUESTION ----------
ch("The electric question")
sc("""The hybrid system raises a question. How far can the W one go on electric power? Car and Driver says less than two miles. An onboard charger can recharge it in twenty-two minutes, according to the story, and GoAuto says recharging to eighty percent can take as little as twenty-two minutes.""",
   "McLaren W1 charging", "LESS THAN 2 MILES ON ELECTRIC")
sc("""The electric part is there for performance, not economy. By comparison, Car and Driver says the cheaper McLaren Artura, with six hundred seventy-one horsepower, offers nineteen miles of electric-only driving. The W one gives up range because it wants the electric motor to be light and powerful, not heavy.""",
   "McLaren Artura", "THE ARTURA GOES 19 MILES")
sc("""McLaren has also said that a fully electric supercar is still far off. A spokesperson told Car and Driver that the company does not think the technology will be sufficiently mature until the end of the decade, and cited weight as a core concern. The F one's whole philosophy was avoiding weight.""",
   "McLaren engineering lab", "WEIGHT IS THE CORE CONCERN")

# ---------- 8. PRICE ----------
ch("Price and rarity")
sc("""Now the money. Top Gear says the F one's new price was five hundred forty thousand pounds, which the Bank of England puts at a little over one point one million pounds in two thousand twenty money. AutoMonitor gives an approximate dollar figure of nine hundred seventy thousand dollars.""",
   "McLaren F1 price", "F1 NEW: £540,000")
sc("""The W one starts at two point one million dollars, Car and Driver says. GoAuto gives a price of about two million pounds in Britain. So the new car costs about three point seven times the F one's original price in raw numbers, but only about one point eight times its price adjusted for inflation, by our own arithmetic.""",
   "McLaren W1 price", "W1 NEW: FROM $2.1 MILLION")
sc("""And production? The F one totals one hundred six cars, with sixty-four road cars, according to Wikipedia and AutoMonitor. The W one is limited to three hundred ninety-nine, and Car and Driver says all of them were allocated to specific customers. That means there will be about six times as many W ones as F one road cars, by our own arithmetic.""",
   "McLaren W1 production", "106 F1s vs 399 W1s")
sc("""The W one was effectively sold before most people saw it. GoAuto says all three hundred ninety-nine examples were spoken for before mere mortals got a whiff of its existence. Car and Driver says deliveries start in twenty twenty-six, and Wikipedia's infobox lists production from January twenty twenty-six.""",
   "McLaren W1 customer", "ALL 399 SPOKEN FOR")
sc("""And the F one's price did not stay where it started. Top Gear says F ones changed hands for roughly the original asking price until about two thousand six, then the price roughly tripled by the end of two thousand eight to around one point five million pounds. By two thousand fourteen it was five million.""",
   "McLaren F1 auction history", "F1 VALUE: £0.5M TO £5M")
sc("""Then came the big numbers. Gooding and Company reports a car sold in twenty twenty-one for twenty point four six five million dollars. Wikipedia lists chassis zero fourteen at twenty-five point three one seven five million dollars in twenty twenty-five. Hagerty valued a normal F one at around sixteen million pounds, Top Gear says.""",
   "McLaren F1 sold auction", "UP TO $25.3 MILLION")
sc("""That raises the obvious question. Will the W one become as valuable as the F one? Nobody can know. The F one's rise took decades, and Top Gear points out that most nineties supercars are worth more now than when new, but the F one rose far more than most. We will not guess the W one's future price.""",
   "McLaren W1 and McLaren F1", "WILL THE W1 FOLLOW?")
sc("""Now a twist on price. In inflation-adjusted terms, the F one cost about one point one million pounds per Top Gear, for six hundred eighteen horsepower, about seventeen hundred eighty pounds per horsepower. The W one at about two million pounds for one thousand two hundred fifty-eight horsepower is about fifteen hundred ninety pounds per horsepower, by our own arithmetic.""",
   "McLaren W1 price tag", "PER HORSEPOWER, THE W1 IS CHEAPER (OUR MATH)")
sc("""Ownership has changed as well. GoAuto says the W one comes with a four-year vehicle warranty, a six-year warranty on the hybrid battery and a four-year service plan. For the F one, AutoMonitor estimates an annual service at McLaren's special operations division in Woking costing fifteen to thirty thousand dollars, and treats that as an estimate.""",
   "McLaren Special Operations Woking", "W1 WARRANTY: 4 YEARS. F1 SERVICE: EST. $15-30K")

# ---------- 9. THE ANSWER ----------
ch("The real difference")
sc("""So what is the real difference? The W one is better at the numbers. Twice the horsepower, quicker acceleration, about sixty-six percent more power per kilogram, and far more downforce. McLaren says it is its fastest-lapping and fastest-accelerating road car ever. On paper, it beats the F one in almost everything but weight and top speed.""",
   "McLaren W1 hypercar", "THE W1 WINS THE NUMBERS")
sc("""The F one is better at the idea. It was lighter by two hundred fifty-nine kilograms. It had no turbos and no electric motor. It put the driver in the middle, and it held the top speed record for seven years. It was not designed to win a spreadsheet. It was designed to be the ultimate road-going sports car.""",
   "McLaren F1 gold", "THE F1 WINS THE IDEA")
sc("""And here is the final twist. The F one's own numbers are no longer extreme by today's standards, but its value keeps rising. The W one's numbers are extreme, but its value is unknown. Sometimes, being the first at something matters more than being the best.""",
   "McLaren F1 and W1 side by side", "FIRST vs BEST")
sc("""Which one would you choose, the F one or the W one? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the F one, work out what it really costs to own one today, and tell the story of the man who dreamed it up.""",
   "McLaren F1", "F1 OR W1?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video82", "McLaren F1 vs McLaren W1: The Real Difference", [
    "Wikipedia, McLaren F1: https://en.wikipedia.org/wiki/McLaren_F1",
    "Wikipedia, McLaren W1: https://en.wikipedia.org/wiki/McLaren_W1",
    "Car and Driver via Daily Maverick, McLaren introduces $2.1 million W1 hybrid supercar (Oct 2024): https://www.dailymaverick.co.za/article/2024-10-06-mclaren-introduces-2-1-million-w1-hybrid-supercar-to-honor-f1-history/",
    "GoAuto, McLaren raises hypercar bar with new W1 (Oct 2024): https://goauto.com.au/amp/mclaren/w1/mclaren-raises-hypercar-bar-with-new-w1/2024-10-08/94971.html",
    "Gooding and Company coverage of F1 chassis 029, JustCars (Australia): https://www.justcars.com.au/news-and-reviews/feature-1995-mclaren-f1/924590",
    "Top Gear, McLaren F1s are now worth 16 million pounds: https://topgear.com.sg/features/mclaren-f1s-are-now-worth-ps16million",
    "SlashGear, Here's How Fast The McLaren F1 Really Is: https://www.slashgear.com/1105554/heres-how-fast-the-mclaren-f1-really-is",
    "AutoMonitor, McLaren F1 price history (estimates): https://automonitor.io/blog/mclaren-f1-price-history/",
], "B")
