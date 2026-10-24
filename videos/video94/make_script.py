import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Two American supercars, both with a six-speed Tremec manual gearbox. One has a supercharged six point two litre V eight. The other has an eight point four litre V ten, and no turbochargers at all. One is the Chevrolet Corvette Z R one, the other the Dodge Viper A C R. And according to published Nürburgring times, the car with less power was the one that lapped faster. This is the real difference between them.""",
   "Dodge Viper ACR and Corvette ZR1", "DODGE VIPER ACR VS CORVETTE ZR1")
sc("""Here is the twist. The Z R one had more power than the Viper that it raced against. It was also almost the same weight as the track-only Viper. Yet the numbers show a gap of seven and a half seconds on the Nürburgring, in the Viper's favour. We will show you where those numbers come from, and why you should read them carefully.""",
   "Nürburgring Nordschleife", "MORE POWER, SLOWER LAP")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. Let us meet the two cars.""",
   "Corvette ZR1", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE CARS ----------
ch("Two American legends")
sc("""The Corvette Z R one is part of the sixth generation, the C six. Wikipedia says GM confirmed the programme in April two thousand seven, and officially introduced the car on the nineteenth of December two thousand seven. Inside General Motors, it was code named Blue Devil, after Rick Wagoner's university, Duke.""",
   "Chevrolet Corvette ZR1 Blue Devil", "BLUE DEVIL: THE CORVETTE ZR1")
sc("""The Z R one name was not new. Wikipedia says it had been used on developmental cars in nineteen seventy-one, and on the top-line C four Corvette Z R dash one. So when GM called its new car a Z R one, it was reviving a name with decades of history behind it.""",
   "Corvette ZR-1 C4", "A NAME WITH A HISTORY")
sc("""The Dodge Viper, as Wikipedia explains, began with Chrysler president Bob Lutz asking for a modern Cobra. The A C R, short for American Club Racer, started as a package on the nineteen ninety-nine G T S, and grew into a car built for track days. The A C R that matches the Z R one in time is the fourth generation, from two thousand eight to twenty ten.""",
   "Dodge Viper ACR", "ACR = AMERICAN CLUB RACER")
sc("""That timing matters for fairness. The Corvette Z R one was built from two thousand nine to two thousand thirteen. The fourth-generation Viper ended in July twenty ten, and the fifth generation came in twenty thirteen. So the Z R one met the old Viper in its last years, and the new one right at the end of its own life.""",
   "Dodge Viper and Corvette ZR1", "THEY OVERLAPPED FROM 2009 TO 2013")

# ---------- 2. ENGINES ----------
ch("Round one: the engines")
sc("""Start with the Z R one's engine. Wikipedia lists the L S nine, a supercharged six point two litre V eight with six hundred thirty-eight horsepower at six thousand five hundred r p m, and six hundred four pound-feet of torque at three thousand eight hundred. Vette Vues adds an Eaton supercharger running ten and a half p s i of boost.""",
   "Corvette ZR1 LS9", "LS9: 6.2 L SUPERCHARGED · 638 HP")
sc("""The Viper's engine was the opposite. Wikipedia lists the fourth generation's eight thousand three hundred eighty-two cubic centimetre V ten, with six hundred horsepower at six thousand one hundred r p m, and five hundred sixty pound-feet at five thousand. It was naturally aspirated, which means no supercharger and no turbocharger.""",
   "Dodge Viper V10", "VIPER V10: 8.4 L NATURALLY ASPIRATED · 600 HP")
sc("""Do the arithmetic. By our own arithmetic, the Z R one has about six percent more power than the fourth-generation Viper, six hundred thirty-eight against six hundred. It has about eight percent more torque, six hundred four against five hundred sixty. The Corvette, on paper, is the stronger engine.""",
   "Corvette ZR1 vs Viper", "ZR1: +6% POWER, +8% TORQUE")
sc("""But it does that with a much smaller engine. By our arithmetic, the Viper's eight point four litres are about thirty-five percent bigger than the Corvette's six point two. Per litre, the Z R one makes about one hundred three horsepower, and the Viper about seventy-two. The supercharger does the work that displacement does in the Viper.""",
   "Engine comparison", "ZR1: 103 HP/L · VIPER: 72 HP/L")
sc("""Where does the power arrive? The Z R one makes its peak torque at three thousand eight hundred r p m, while the Viper makes its at five thousand. Vette Vues says every L S nine was meticulously hand-built at the Performance Build Center. The Drive says the Viper's V ten was built by hand at Conner Avenue. So both American engines were assembled by hand.""",
   "Hand-built engine", "BOTH ENGINES WERE HAND-BUILT")
sc("""And the gearbox is a surprise. Wikipedia says the fourth-generation Viper used a new Tremec T R six zero six zero six-speed manual. Vette Vues says the Z R one used a Tremec T R six zero six zero six-speed manual too. The same gearbox family, in two cars from rival companies, with very different engines in front of them.""",
   "Tremec TR6060 gearbox", "BOTH USE A TREMEC TR6060 6-SPEED")

sc("""Here is a striking coincidence. The fifth-generation Viper of twenty thirteen had six hundred forty horsepower and six hundred pound-feet, according to Wikipedia. The twenty thirteen Corvette Z R one had six hundred thirty-eight horsepower and six hundred four pound-feet. By our arithmetic, the two cars were separated by two horsepower and four pound-feet. From two rival companies.""",
   "Dodge Viper and Corvette ZR1 2013", "2013: 640 HP VS 638 HP")
sc("""The Z R one also had family. Wikipedia lists the Z oh six, with a seven litre L S seven V eight making five hundred five horsepower, and a weight of three thousand one hundred thirty pounds. By our arithmetic, the Z R one has about twenty-six percent more power than the Z oh six, and weighs about seven percent more. The extra power came with extra weight.""",
   "Corvette Z06", "ZR1 VS Z06: +26% POWER, +7% WEIGHT")
sc("""The Z oh six reached sixty in three point six seconds, according to a Car and Driver test quoted by Wikipedia, and the quarter mile in eleven point seven at one hundred twenty-five. The Z R one's eleven point two at one hundred thirty point five is about half a second and five and a half miles per hour better. The step from Z oh six to Z R one was real.""",
   "Corvette Z06", "Z06: 11.7 S · ZR1: 11.2 S")
# ---------- 3. WEIGHT AND SPEED ----------
ch("Round two: weight and straight-line speed")
sc("""Weight next. Wikipedia lists the Z R one at three thousand, three hundred fifty pounds, or one thousand five hundred twenty kilograms. Vette Vues says three thousand, three hundred twenty-four. The two sources differ by twenty-six pounds, which is under one percent. For the Viper's A C R, the best published weight is for the track-only A C R-X, at three thousand three hundred pounds.""",
   "Corvette ZR1 weight", "ZR1: ~3,330 LB · ACR-X: 3,300 LB")
sc("""By our own arithmetic, the A C R-X is lighter than the Z R one by somewhere between twenty-four and fifty pounds, depending on which source you use. That is less than two percent. A track-only Viper and a road-going Corvette, with a supercharger and carbon-ceramic brakes, weigh almost the same.""",
   "Dodge Viper ACR-X", "ACR-X VS ZR1: WITHIN 2%")
sc("""Now acceleration. Motor Trend tested the Z R one in October two thousand eight, and recorded zero to sixty in three point three seconds and the quarter mile in eleven point two seconds at one hundred thirty point five miles per hour, according to Wikipedia. GM itself claimed three point four, according to Autoblog.""",
   "Corvette ZR1 acceleration", "0–60 IN 3.3 SECONDS · QUARTER IN 11.2")
sc("""The Viper's best published figure is for the fifth generation. Wikipedia lists zero to sixty-two miles per hour in three and a half seconds, and a top speed of two hundred six. The Z R one's top speed was two hundred five, according to GM. Autoblog and Wikipedia both quote it. By our arithmetic, the two cars are within one mile per hour of each other.""",
   "Dodge Viper top speed", "TOP SPEED: 205 MPH VS 206 MPH")
sc("""The Viper A C R sacrificed some of that. Wikipedia says the last A C R's top speed fell by up to twenty miles per hour, because of the aero. In exchange, it produced fifteen hundred pounds of downforce in corners, and two thousand with the Extreme Aero Package. The Corvette has no published downforce figure in the sources we read.""",
   "Dodge Viper ACR aero", "ACR: UP TO 2,000 LB OF DOWNFORCE")
sc("""So on straights, the Z R one is likely the stronger, with more power at nearly the same weight. In corners, the A C R has aerodynamics that the Corvette does not advertise. That sets up the track result. A car with less power but more downforce could, in theory, be quicker on a long lap.""",
   "Corvette ZR1 and Viper ACR", "STRAIGHTS VS CORNERS")

# ---------- 4. NURBURGRING ----------
ch("Round three: the Nürburgring")
sc("""Now the lap times, with every warning attached. Vette Vues says that in twenty eleven, driver Jim Mero set a seven nineteen point six three on the Nordschleife in a completely stock factory production Z R one. That is the best published production Corvette time in our sources.""",
   "Corvette ZR1 Nürburgring", "ZR1: 7:19.63 (JIM MERO, 2011)")
sc("""For the Viper, Wikipedia says that on the fourteenth of September, twenty eleven, a two thousand ten A C R set a seven twelve point one three lap. The page calls it the sixth-fastest street-legal lap of the time, though three faster laps had been set earlier. It was a street-legal car on the same track in the same year.""",
   "Dodge Viper ACR Nürburgring", "ACR: 7:12.13 (14 SEPTEMBER 2011)")
sc("""By our own arithmetic, seven nineteen point six three minus seven twelve point one three is seven and a half seconds. That is about one point seven percent of the lap. A gap of seven and a half seconds on a lap of more than seven minutes is meaningful, but it is not huge.""",
   "Nürburgring Nordschleife", "ACR FASTER BY 7.5 SECONDS (1.7%)")
sc("""But we must be careful. These two laps were set by different drivers, with different tyres and different conditions, and the sources do not tell us whether the lengths of the lap were measured identically. Nürburgring times are a notorious problem. They are fun to compare, and they are not a controlled test. We report them, and we do not claim they settle anything.""",
   "Nürburgring pit lane", "DIFFERENT DRIVERS, DIFFERENT CONDITIONS")
sc("""The Viper went faster still. Wikipedia says the track-only A C R-X did seven oh three point oh five eight in February twenty twelve. And a fifth-generation A C R with the Extreme Aero Package did an unofficial seven oh one point six seven in October twenty fifteen, driven by Dominik Farnbacher. The Z R one, by comparison, was no longer in production by then.""",
   "Dodge Viper ACR-X", "ACR-X: 7:03 · LATE ACR: 7:01.67")
sc("""By our arithmetic, the late A C R's seven oh one point six seven is about eighteen seconds faster than the Z R one's seven nineteen point six three. That is about four percent. Again, it is a different car, a different year and a different driver. But the direction of the evidence is consistent: the Viper A C R was quicker on the Ring.""",
   "Dodge Viper ACR 2015", "~18 SECONDS FASTER THAN THE ZR1 (UNOFFICIAL)")
sc("""On another track, the Viper has a clean record. Wikipedia says Kuno Wittmer drove a street-legal two thousand ten A C R to one fifty-nine point nine nine five on the three mile Outer Course at Miller Motorsports Park, the first production car under two minutes there. We have no Corvette time for that track in our sources.""",
   "Miller Motorsports Park", "FIRST PRODUCTION CAR UNDER 2:00 AT MILLER")

sc("""The Z R one was also a small part of a large programme. Wikipedia says the whole C six generation sold two hundred fifteen thousand, two hundred twenty-three cars from two thousand five to two thousand thirteen. By our arithmetic, the four thousand, six hundred eighty-four Z R ones were only about two percent of those. It was a halo car on a big family.""",
   "Chevrolet Corvette C6", "ZR1 = ~2% OF ALL C6 CORVETTES")
sc("""By contrast, every Viper was a halo car. The Drive calls it the Dodge halo car for twenty-five years. Wikipedia counts thirty-one thousand, nine hundred eighty-nine cars over twenty-six years. That is smaller than the C six's two hundred fifteen thousand by a factor of about seven, by our arithmetic, although the Corvette's run was only nine years long.""",
   "Dodge Viper halo car", "VIPER: 31,989 IN 26 YEARS")
# ---------- 5. TECHNOLOGY ----------
ch("Round four: technology")
sc("""Now the equipment. The Z R one, Wikipedia says, used carbon fibre for the roof, hood, fenders, front splitter and rocker mouldings. It had carbon-ceramic brakes with blue calipers, and Magnetic Selective Ride Control, in which sensors adjust the dampers based on road conditions. A polycarbonate window in the hood shows the intercooler.""",
   "Corvette ZR1 carbon fibre", "CARBON PARTS · MAGNETIC RIDE · HOOD WINDOW")
sc("""Vette Vues lists Brembo carbon-ceramic rotors of fifteen and a half inches at the front and fifteen at the rear, and tyres of two eighty-five thirty nineteen at the front and three thirty-five twenty-five twenty at the rear. Wikipedia says they were the largest wheels ever fitted to a production Corvette.""",
   "Corvette ZR1 brakes", "15.5-INCH CARBON-CERAMIC DISCS")
sc("""The Viper's approach was different. In the fourth generation, the sources we read describe no magnetic dampers and no carbon body. What it had was an engine, a manual gearbox, and aero. Wikipedia says the fifth generation moved to a carbon fibre and aluminium body, and added electronic stability control, traction control and A B S for the first time.""",
   "Dodge Viper cockpit", "VIPER: LESS TECH, MORE AERO")
sc("""So the Corvette was the more technological car, in the sense of having its electronic dampers and carbon parts. The Viper was the more mechanical car. That distinction is the real difference. Both have manuals, and both are fast. One of them thinks for you, and the other waits for you to think.""",
   "Corvette ZR1 and Dodge Viper", "ELECTRONIC DAMPERS VS RAW MECHANICS")

sc("""Size matters too. Wikipedia lists the Z R one at seventy-five point nine inches wide and one hundred seventy-five point six long, shared with the Z oh six and Grand Sport. The Viper's measurements are not in our sources, so we do not compare them.""",
   "Corvette ZR1 dimensions", "ZR1: 75.9 IN WIDE · 175.6 IN LONG")
sc("""The Z R one ended with a celebration. Vette Vues says the two thousand thirteen sixtieth anniversary edition came in Arctic White with Pearl Silver Blue stripes and a Diamond Blue leather interior. And the same year's Z R one was the Indianapolis five hundred pace car. The Viper, too, had been a pace car, in nineteen ninety-one and nineteen ninety-six.""",
   "Corvette ZR1 60th Anniversary", "BOTH CARS PACED THE INDY 500")
# ---------- 6. PRICE AND PRODUCTION ----------
ch("Round five: price and numbers")
sc("""Now the price. Autoblog says the two thousand nine Corvette Z R one started at one hundred three thousand, three hundred dollars including an eight hundred fifty dollar destination charge. There was a one thousand seven hundred dollar gas-guzzler tax, a ten thousand dollar interior package, and chrome wheels at two thousand were the only other option.""",
   "Corvette ZR1 price", "ZR1: $103,300 · INTERIOR PACKAGE $10,000")
sc("""The same article lists fuel economy: fourteen city and twenty highway for the Corvette, thirteen and twenty-two for the Dodge Viper. So the Viper used more fuel in town and less on the highway. Nobody bought either car to save fuel, but the numbers are close.""",
   "Fuel gauge", "ZR1 14/20 MPG · VIPER 13/22 MPG")
sc("""Production numbers show a bigger difference. Vette Vues lists Z R one production of one thousand four hundred fifteen in two thousand nine, one thousand five hundred seventy-seven in twenty ten, eight hundred six in twenty eleven, four hundred four in twenty twelve, and four hundred eighty-two in twenty thirteen. A total of four thousand, six hundred eighty-four.""",
   "Corvette ZR1 production", "4,684 ZR1s BUILT, 2009–2013")
sc("""Good Car Bad Car lists United States Viper sales of four hundred eighty-two in two thousand nine, three hundred ninety-two in twenty ten, one hundred ninety-seven in twenty eleven and twenty in twenty twelve. By our arithmetic, over the four years from two thousand nine to twenty twelve, the Viper sold one thousand ninety-one cars. The Corvette Z R one was built in nearly four times that number, four thousand, two hundred two, from two thousand nine to twenty twelve.""",
   "Dodge Viper sales", "VIPER 2009–2012: 1,091 SOLD IN THE US")
sc("""Those are different measures, production and sales, and the years do not match perfectly, so we keep the claim modest. But the direction is clear. The Z R one was the more common car, and the Viper the rarer one. And the Z R one's own numbers fell quickly too, from one thousand five hundred seventy-seven in twenty ten to four hundred four in twenty twelve.""",
   "Corvette ZR1 sales decline", "ZR1: 1,577 → 404 IN TWO YEARS")

# ---------- 7. USED PRICES ----------
ch("Round six: what they are worth now")
sc("""What about today? Vette Vues links to a sale of a two thousand thirteen Z R one at one hundred thirty-two thousand dollars at Mecum Indianapolis. By our arithmetic, that is about twenty-eight percent above the two thousand nine base price of one hundred three thousand three hundred, for a car sold four years later.""",
   "Corvette ZR1 auction", "2013 ZR1: $132,000 AT MECUM")
sc("""The Viper A C R has done much better. Classic dot com lists eight sales of fifth-generation A C Rs between May and November twenty twenty-five, from one hundred eighty-seven thousand dollars to four hundred six thousand five hundred. By our arithmetic, the average is two hundred ninety-three thousand, eight hundred forty-six.""",
   "Dodge Viper ACR auction", "ACR SALES 2025: AVERAGE $293,846")
sc("""So by our arithmetic, the average A C R in that list sold for about two point two times the Z R one's Mecum price. These are very different samples, the Viper A C R being the rarest and last Viper, with extreme aero. But it shows where the market has placed the two cars, and the Viper has moved ahead.""",
   "Dodge Viper ACR", "ACR ≈ 2.2× THE ZR1 AUCTION PRICE")
sc("""Collectors have also paid for the Corvette's story. Vette Vues says the first two thousand thirteen Z R one, V I N zero zero one in Cyber Gray Metallic, went to Jay Leno. And the two thousand thirteen Z R one was the pace car for the ninety-sixth Indianapolis five hundred. A car with a documented history can be worth more.""",
   "Corvette ZR1 Jay Leno", "VIN 001 WENT TO JAY LENO")

# ---------- 8. VERDICT ----------
ch("The verdict")
sc("""So who wins? On engine power, the Corvette Z R one, by about six percent. On engine efficiency per litre, the Corvette. On weight, a tie. On straight-line speed, effectively a tie. On the Nürburgring, the Viper A C R, by seven and a half seconds, with caveats. On downforce, the Viper. On technology, the Corvette. On price today, the Viper.""",
   "Corvette ZR1 and Dodge Viper ACR", "SCORECARD")
sc("""The real difference is philosophy. The Corvette used a supercharger, carbon parts and adjustable dampers to make a smaller engine and a clever car. The Viper used a huge engine and aerodynamics. One was made by a big company with a famous engineering group. The other was made by about eighty people in a small plant in Detroit.""",
   "Corvette ZR1 and Dodge Viper ACR", "TWO PHILOSOPHIES")
sc("""One final caution. Every comparison here uses published figures from different years, and some of them are unofficial. We have not driven either car, and we do not claim a verdict on which is better to drive. We claim only what the numbers show. And on the numbers, the Viper A C R lapped faster, while the Z R one was more powerful.""",
   "Nürburgring", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you choose, the Viper A C R or the Corvette Z R one? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Viper, work out what it really costs to own one today, and tell why the Viper was killed twice.""",
   "Dodge Viper ACR and Corvette ZR1", "VIPER ACR OR CORVETTE ZR1?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more comparisons between the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video94", "Dodge Viper ACR vs Corvette ZR1: The Real Difference", [
    "Wikipedia, Dodge Viper: https://en.wikipedia.org/wiki/Dodge_Viper",
    "Wikipedia, Chevrolet Corvette (C6): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C6)",
    "Autoblog, 2009 Corvette ZR1 starts at $103,300: https://www.autoblog.com/2008/06/17/2009-corvette-zr1-pricing-and-performance-numbers-released/",
    "Vette Vues, C6 Corvette ZR1 History (2009–2013): https://vette-vues.com/c6-corvette-zr1-history/",
    "Good Car Bad Car, Dodge Viper sales figures: https://www.goodcarbadcar.net/dodge-viper-sales-figures/",
    "Classic.com, Dodge Viper ACR VX I market: https://www.classic.com/m/dodge/viper/5th-gen/acr/",
], "B")
