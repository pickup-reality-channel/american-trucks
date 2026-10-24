import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Dodge Viper, one of the loudest and most brutal American sports cars ever made, started with no door handles, no airbags, no traction control and no A B S. Its V ten engine was partly cast by Lamborghini. And in the end, the car that began with no safety equipment at all was killed by a safety rule. There are two things about the Viper that you probably did not know, and both are in published sources.""",
   "Dodge Viper", "2 THINGS YOU DIDN'T KNOW ABOUT THE DODGE VIPER")
sc("""The first is about who really helped build that engine, and how small the team was. The second is about what the Viper did not have for twenty-one years, and the date when it finally got it. Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will say so.""",
   "Dodge Viper V10", "THE ENGINE · THE MISSING SAFETY KIT")

# ---------- 1. THE CAR ----------
ch("What the Viper was")
sc("""Wikipedia says the Dodge Viper was built from nineteen ninety-one to twenty seventeen, about twenty-six years. In that time, thirty-one thousand, nine hundred eighty-nine cars were made. By our own arithmetic, that is about twelve hundred thirty a year on average, which is small for a car company and enormous for a sports car with this kind of reputation.""",
   "Dodge Viper", "31,989 BUILT · 1991–2017")
sc("""It started with a simple brief. Chrysler president Bob Lutz asked designer Tom Gale to consider a modern Cobra, Wikipedia says. A clay model followed, and a concept was shown at the nineteen eighty-nine North American International Auto Show. The public reaction was so strong that the project was approved for production.""",
   "Dodge Viper concept 1989", "A MODERN COBRA")
sc("""The approval was slow, though. Wikipedia says chairman Lee Iacocca delayed the seventy million dollars needed until May nineteen ninety. Production cars reached reviewers in November nineteen ninety-one, and retail shipments began in January nineteen ninety-two, as the R T ten roadster, at fifty-two thousand dollars.""",
   "Dodge Viper RT/10", "JANUARY 1992: THE RT/10 AT $52,000")
sc("""The numbers of the first car were big. Wikipedia lists an eight litre V ten with four hundred horsepower and four hundred sixty-five pound-feet of torque, a curb weight of one thousand four hundred ninety kilograms, zero to a hundred kilometres per hour in four point two seconds, and a quarter mile in twelve point six.""",
   "Dodge Viper 1992", "400 HP · 0–100 IN 4.2 SECONDS")

sc("""The concept itself was made by hand. Wikipedia says Metalcrafters built the show car in sheet metal, and that the project was developed by a company that had never built a car like it. Then Carroll Shelby, who made the original Cobra, drove a pre-production car as the Indianapolis five hundred pace car in nineteen ninety-one, replacing the Dodge Stealth after complaints from the United Auto Workers.""",
   "Carroll Shelby", "BUILT BY HAND IN SHEET METAL")
sc("""Production began at the New Mack Assembly plant, from nineteen ninety-one to nineteen ninety-five, according to Wikipedia. Then it moved to Conner Avenue Assembly in Detroit, from October nineteen ninety-five. So, by our arithmetic, the Viper had two homes in twenty-six years, and the second home lasted twenty-two years.""",
   "New Mack Assembly", "NEW MACK 1991–95 · CONNER AVENUE 1995–2017")
# ---------- 2. THING ONE ----------
ch("Thing one: Lamborghini helped build the engine")
sc("""Now the first thing most people do not know. At the time, Chrysler owned Lamborghini. Wikipedia says Lamborghini cast a prototype aluminium engine block for the Viper, and helped design the V ten. An American muscle car, with a heart developed with the help of an Italian supercar maker.""",
   "Lamborghini engine", "CHRYSLER OWNED LAMBORGHINI")
sc("""Wikipedia says the development group was called Team Viper. Chief engineer Roy Sjoberg chose eighty-five engineers, and development began in March nineteen eighty-nine. Dick Winkles, the chief power engineer, was a major contributor. By modern standards, eighty-five engineers is a small team for an entire car.""",
   "Team Viper", "85 ENGINEERS · MARCH 1989")
sc("""Think about the scale. The page says the project needed seventy million dollars. By our own arithmetic, that is about eight hundred twenty thousand dollars for each of the eighty-five engineers. That is not a precise measure of anything, but it gives a sense of how little money the Viper had compared with a normal new car programme.""",
   "Dodge Viper engineering", "$70M ÷ 85 ENGINEERS ≈ $820K EACH")
sc("""The engine was massive. Wikipedia lists the first V ten's weight at three hundred twenty-three kilograms, which is about twenty-two percent of the car's curb weight of one thousand four hundred ninety, by our arithmetic. The engine was almost a quarter of the whole car. And it made four hundred horsepower at only four thousand six hundred r p m.""",
   "Dodge Viper V10", "THE ENGINE = 22% OF THE CAR'S WEIGHT")
sc("""That low r p m is the clue to its character. The first Viper's peak torque, four hundred sixty-five pound-feet, arrived at three thousand six hundred r p m. This was a big, slow-revving engine, built for push rather than screaming speed. The Corvette Z R one's supercharged V eight, by comparison, made its power at six thousand five hundred.""",
   "Dodge Viper engine", "PEAK POWER AT JUST 4,600 RPM")
sc("""Over the years the engine grew. Wikipedia lists eight litres at launch, seven thousand nine hundred ninety cubic centimetres in the GTS, eight point three litres in the third generation, and eight point four litres in the last two. By our arithmetic, the fifth generation's six hundred forty horsepower is about seventy-six horsepower per litre, against fifty per litre in the first car.""",
   "Dodge Viper V10 evolution", "50 HP/L → 76 HP/L")
sc("""The engine also got lighter. Wikipedia says the third generation's V ten weighed about five hundred pounds, or two hundred thirty kilograms, against three hundred twenty-three for the first. By our arithmetic, that is about twenty-nine percent less weight while producing twenty-five percent more power, five hundred horsepower against four hundred.""",
   "Dodge Viper engine weight", "−29% WEIGHT, +25% POWER")
sc("""The last Viper's V ten was all aluminium. Wikipedia says the fifth generation used an all-aluminium eight point four litre engine with six hundred forty horsepower at six thousand one hundred fifty r p m, and six hundred pound-feet of torque. In twenty fifteen it rose to six hundred forty-five. The engine that began with Lamborghini's help ended as one of the biggest in the world.""",
   "Dodge Viper 8.4 V10", "THE FINAL V10: 8.4 L · 640–645 HP")
sc("""The Viper's V ten even lived on in a different way. The Drive says the Conner Avenue plant had built the Viper's V ten engine since two thousand one, and that all Vipers had been hand-built there since nineteen ninety-five. So a few dozen people in Detroit built both the car and its engine, one at a time.""",
   "Conner Avenue Assembly", "HAND-BUILT IN DETROIT")

sc("""Compare the Viper's engine with its great rival's. The Corvette Z R one had a supercharged six point two litre V eight with six hundred thirty-eight horsepower, according to Wikipedia. By our arithmetic, that is about one hundred three horsepower per litre, about thirty-five percent more than the last Viper's seventy-six. The Viper made its power the old way: with size.""",
   "Chevrolet Corvette ZR1", "ZR1: 103 HP/L · VIPER: 76 HP/L")
sc("""The generations after the first added power in steps. Wikipedia lists the GTS coupé of nineteen ninety-six with four hundred fifty horsepower from a seven thousand nine hundred ninety cubic centimetre engine, nicknamed the double bubble for its roof, inspired by the Shelby Daytona. It was chosen as the nineteen ninety-six Indianapolis five hundred pace car.""",
   "Dodge Viper GTS", "GTS: 450 HP · DOUBLE-BUBBLE ROOF")
sc("""The third generation, from two thousand three, had an eight point three litre engine, five hundred horsepower and five hundred twenty-five pound-feet, according to Wikipedia. The page says the chassis was about eighty pounds lighter. The coupé of two thousand six was rated at five hundred ten horsepower and five hundred thirty-five pound-feet.""",
   "Dodge Viper SRT-10", "2003: 8.3 L · 500 HP")
sc("""The fourth generation, from two thousand eight, gave six hundred horsepower at six thousand one hundred r p m, and five hundred sixty pound-feet at five thousand. Wikipedia lists a new Tremec six-speed gearbox, an improved valvetrain and dual electronic throttle bodies. A vented engine cover is the easiest way to tell it from the one before.""",
   "Dodge Viper ZB II", "2008: 600 HP")
# ---------- 3. THING TWO ----------
ch("Thing two: the safety kit it didn't have")
sc("""Now the second thing, and this one is hard to believe. Wikipedia says the first Viper had no exterior door handles, no airbags, no traction control and no A B S. It had canvas roofs and vinyl windows that zipped. Air conditioning was only an option, from nineteen ninety-four or ninety-five. It was a very pure, very raw car.""",
   "Dodge Viper cockpit", "NO DOOR HANDLES · NO AIRBAGS · NO ABS")
sc("""The page quotes how the car was seen: an intimidating car to drive. It had four hundred horsepower, rear-wheel drive, and nothing electronic to catch a mistake. For a buyer in nineteen ninety-two, that was the appeal. For a driver in the rain, it was a risk. The Viper's reputation as a car that bites came from this.""",
   "Dodge Viper in the rain", "\"AN INTIMIDATING CAR TO DRIVE\"")
sc("""Safety equipment arrived slowly. Wikipedia says the GTS coupé of nineteen ninety-six was the first Viper with airbags, and also the first with standard air conditioning and power windows. By our own arithmetic, four years separated the first Viper and the first Viper with airbags.""",
   "Dodge Viper GTS 1996", "1996: FIRST AIRBAGS (4 YEARS LATE)")
sc("""Stability control, traction control and four-channel A B S took longer. Wikipedia says all three arrived with the fifth generation, which was revealed at the twenty twelve New York Auto Show and sold from twenty thirteen. They were firsts for the Viper. By our arithmetic, that is twenty-one years after the car began, in nineteen ninety-two.""",
   "Dodge Viper 2013", "ESC, TRACTION CONTROL, ABS: FIRST IN 2013")
sc("""We do not claim the Viper was dangerous, and the sources we read do not say so. They say what it lacked, and when it was added. The Viper was designed as a raw machine, and its makers chose to add equipment slowly. Owners and critics who loved it often loved it for exactly that reason, in our reading.""",
   "Dodge Viper", "A CAR THAT RESISTED ELECTRONICS")
sc("""Yet the irony is complete. According to Motor Authority and The Drive, the Viper was killed by a safety regulation, federal standard two twenty-six, which requires side curtain airbags. In twenty twenty-six, the head of S R T said the airbags would be right over the driver's ear. A car that began with no airbags was ended by airbags.""",
   "Side curtain airbag", "BORN WITHOUT AIRBAGS, KILLED BY AIRBAGS")
sc("""Tim Kuniskis told The Drive that the car reached the end of its life cycle, and that to stay competitive it would have needed to become an automatic or a dual-clutch. He called it analogue, with a manual transmission, and said it had downsides. That is the Viper in one sentence: a car with strong opinions.""",
   "Tim Kuniskis", "\"ANALOG\" AND MANUAL")

sc("""There is a final twist in the safety story. Wikipedia says the fifth generation Viper's body was carbon fibre and aluminium, and that it had a drag coefficient of point three six four. A modern body, stability control, traction control and four-channel A B S. The 2013 Viper had finally caught up with the rest of the car world, only for the airbag rule to catch up with it.""",
   "Dodge Viper VX", "FINALLY MODERN, THEN OUTLAWED")
# ---------- 4. WHAT IT DID ON TRACK ----------
ch("What the Viper did on the track")
sc("""In motorsport, the Viper was a giant. Wikipedia says the first race appearance at Le Mans came in nineteen ninety-four, when two R T tens ran for the French team Rent-A-Car Racing. The number forty car, driven by René Arnoux, Bertrand Balas and Justin Bell, finished twelfth overall and third in its class.""",
   "Le Mans 1994 Viper", "LE MANS 1994: 12TH OVERALL")
sc("""Chrysler then built the first G T S-R race car in nineteen ninety-six, with support from Oreca, Reynard and Riley and Scott. It debuted at the nineteen ninety-six twenty-four hours of Daytona. Three straight Le Mans class wins followed, in nineteen ninety-eight, nineteen ninety-nine and two thousand.""",
   "Dodge Viper GTS-R", "3 LE MANS CLASS WINS IN A ROW")
sc("""Wikipedia says the Viper also won the twenty-four hours of Daytona overall in two thousand, and the Spa twenty-four hours in two thousand one and two thousand two. Career totals: four hundred forty-five races, forty-seven championships, and one hundred sixty-two wins. A road car with no airbags had become a champion.""",
   "Dodge Viper racing", "162 WINS · 47 CHAMPIONSHIPS")
sc("""The road-going racer was the ACR, short for American Club Racer. Wikipedia says the first ACR was a package for the nineteen ninety-nine G T S, using G T two intake parts and BBS wheels. Over the years the ACR grew into a full aero-focused car, and the last one produced as much as two thousand pounds of downforce.""",
   "Dodge Viper ACR", "ACR: AMERICAN CLUB RACER")
sc("""The records came in the end. Wikipedia says a two thousand ten ACR lapped the Nürburgring in seven twelve point one three in September twenty eleven. An ACR-X did seven oh three in twenty twelve, and the final ACR with the extreme aero package did an unofficial seven oh one point six seven in October twenty fifteen.""",
   "Nürburgring Viper ACR", "7:12 → 7:03 → 7:01.67")
sc("""By our own arithmetic, from seven twelve point one three to seven oh one point six seven is about ten and a half seconds quicker. In four years, the ACR improved by that much on the most famous test track in the world. And it did it without a hybrid motor, without a dual-clutch, and with a manual gearbox.""",
   "Dodge Viper ACR Nürburgring", "10.5 SECONDS FASTER IN 4 YEARS")
sc("""Wikipedia also says a street-legal two thousand ten ACR, driven by Kuno Wittmer, lapped Miller Motorsports Park in one fifty-nine point nine nine five, the first production car under two minutes there. That is a lap that the page calls a first. Another reminder that the Viper was not just a straight-line car.""",
   "Miller Motorsports Park", "FIRST PRODUCTION CAR UNDER 2:00")

sc("""There was also a racing offshoot for customers. Wikipedia lists the Viper G T three R of twenty thirteen, estimated at four hundred fifty-nine thousand dollars, with six hundred eighty horsepower. It won G T three class races in twenty fourteen and twenty fifteen. In twenty fourteen the Viper also took the drivers' and teams' titles in the United SportsCar Championship, with Kuno Wittmer.""",
   "Dodge Viper GT3-R", "GT3-R: 680 HP · EST. $459,000")
sc("""The track-only ACR-X, introduced in twenty ten, cost one hundred ten thousand dollars according to Wikipedia, weighed three thousand three hundred pounds and added about forty horsepower. It lapped the Nürburgring in seven oh three point oh five eight in February twenty twelve. It was a car for a track day, not for the street, and a very serious one.""",
   "Dodge Viper ACR-X", "ACR-X: $110,000 · 3,300 LB")
sc("""The last big attempt was funded by fans. Wikipedia says a crowdfunded attempt in twenty seventeen, organised by Russ Oasis through GoFundMe, brought Dominik and Mario Farnbacher and Lance David Arnold to the Nürburgring to beat the Lamborghini Huracán Performante's six fifty-two oh one. One car crashed, and the record stood.""",
   "Nürburgring Viper crowdfunded attempt", "A FAN-FUNDED RECORD ATTEMPT, 2017")
sc("""Even so, Wikipedia says the attempt made the Viper ACR the fastest American, rear-wheel-drive, manual-transmission car on that track at the time. The qualifiers are many. But they describe the Viper well: American, rear-wheel drive, manual. Everything about the car was a kind of choice, and the choices were deliberately old-fashioned.""",
   "Dodge Viper ACR", "AMERICAN · RWD · MANUAL")
sc("""The Viper also reached television. Wikipedia says the nineteen ninety-four to nineteen ninety-eight series Viper starred a modified R T ten called The Defender, and only fourteen were built. In the United Kingdom, the third generation was sold as the Dodge S R T ten, because Viper is a trademark there.""",
   "Dodge Viper TV series", "THE DEFENDER: 14 BUILT")
# ---------- 5. THE LAST ONE ----------
ch("The last Viper")
sc("""The last Viper was impressive. Wikipedia lists zero to sixty-two miles per hour in three and a half seconds, a top speed of two hundred six miles per hour, and a drag coefficient of point three six four. It was built of carbon fibre and aluminium, with a Tremec six-speed manual and a final drive of three fifty-five.""",
   "Dodge Viper 2017", "0–62 IN 3.5 S · 206 MPH · Cd 0.364")
sc("""Five years earlier the same car might not have existed. Wikipedia says production of the fourth generation ended on the first of July, twenty ten, with a gold car with orange stripes. Sergio Marchionne previewed a twenty twelve prototype only two months later, in September twenty ten. The Viper was never quite dead.""",
   "Dodge Viper 2010", "THE VIPER DIED IN 2010, THEN CAME BACK")
sc("""Then the final end came. The Drive says the Conner Avenue plant would close on the thirty-first of August, twenty seventeen, and that it employed just over eighty people. It was F C A's smallest plant in North America, according to the article. A tiny factory made one of America's most extreme cars.""",
   "Conner Avenue plant", "AUGUST 31, 2017: THE PLANT CLOSES")
sc("""The Viper's numbers at the end were not terrible. Good Car Bad Car lists five hundred eighty-five sales in twenty seventeen and six hundred twenty-six in twenty sixteen. And the used market has been kind. Classic dot com shows Viper ACRs selling for between one hundred eighty-seven thousand and four hundred six thousand five hundred dollars in twenty twenty-five.""",
   "Dodge Viper ACR 2025", "ACR SALES 2025: $187K TO $406K")

sc("""Dodge's concept cars showed where the Viper might have gone. Wikipedia lists the S R T ten Carbon Concept at the two thousand three SEMA show with six hundred twenty-five horsepower, and the Viper Mopar Concept of two thousand seven with six hundred seventy-five. It also lists the Dodge Copperhead, a V six concept, and the Chrysler Firepower, with a Hemi V eight and an automatic.""",
   "Dodge Viper concepts", "CONCEPTS: 625 HP · 675 HP · COPPERHEAD")
sc("""Compare that with the Viper in the end. In twenty fifteen, Wikipedia says, it was renamed S R T Viper, and power rose to six hundred forty-five horsepower. The page says highway economy was twenty miles per gallon. That is the same highway figure as the first Viper in nineteen ninety-two, despite more than fifty percent more power, by our arithmetic.""",
   "SRT Viper 2015", "20 MPG HIGHWAY IN 1992 AND IN 2015")
sc("""The racing story ended quietly. Wikipedia says the Viper finished eighth in its class at Le Mans in twenty thirteen, and withdrew in twenty fourteen. Earlier, the page lists the G T two Champion Edition of nineteen ninety-eight, with four hundred sixty horsepower and only one hundred built, as a road-going celebration of the racing success.""",
   "Dodge Viper GT2 Champion Edition", "2013: 8TH IN CLASS AT LE MANS")
sc("""Add the numbers up, by our own arithmetic. A car that began with four hundred horsepower reached six hundred forty-five, a gain of about sixty-one percent. It won three Le Mans class races, took a Daytona overall win, and set Nürburgring times near seven minutes. And it did all of that while being built by about eighty people.""",
   "Dodge Viper", "+61% POWER · 162 RACE WINS · ~80 BUILDERS")
# ---------- 6. THE POINT ----------
ch("Why it matters")
sc("""So here are the two things again. The Viper's engine was developed with help from Lamborghini, by a team of just eighty-five engineers. And the Viper went twenty-one years without stability control, traction control or A B S, and ended because of an airbag rule. Both facts come from published sources, and both make the Viper more surprising, not less.""",
   "Dodge Viper", "THE TWO THINGS, AGAIN")
sc("""The Viper survives as a symbol of an era. A manual gearbox, a huge naturally aspirated engine, and a driver who had to be paying attention. Whether you call that thrilling or dangerous is a matter of taste. The record shows it won at Le Mans and set times at the Nürburgring. It did what it was made for.""",
   "Dodge Viper ACR", "A CAR THAT DEMANDED ATTENTION")
sc("""Which of the two things surprised you more, the Lamborghini connection or the missing safety equipment? Tell us in the comments. In the other videos of this series, we compare the Viper ACR with the Corvette Z R one, work out what it really costs to own a Viper today, and tell why the Viper was killed twice.""",
   "Dodge Viper", "WHICH SURPRISED YOU MORE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video93", "2 Things You Didn't Know About the Dodge Viper", [
    "Wikipedia, Dodge Viper: https://en.wikipedia.org/wiki/Dodge_Viper",
    "Motor Authority, Dodge Viper production ending due to airbag regulations: https://www.motorauthority.com/news/1101880_dodge-viper-production-ending-due-to-airbag-regulations",
    "The Drive, Dodge Viper factory to close August 31: https://www.thedrive.com/article/12390/dodge-viper-factory-to-close-august-31",
    "Yahoo / The Drive, The Dodge Viper era is dead, head of SRT says (29 May 2026): https://autos.yahoo.com/people-and-culture/articles/dodge-viper-era-dead-head-164100036.html",
    "Good Car Bad Car, Dodge Viper sales figures: https://www.goodcarbadcar.net/dodge-viper-sales-figures/",
    "Classic.com, Dodge Viper ACR VX I market: https://www.classic.com/m/dodge/viper/5th-gen/acr/",
    "Wikipedia, Chevrolet Corvette (C6): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C6)",
], "A")
