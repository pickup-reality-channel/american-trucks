import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""One of these cars has a battery that weighs seven hundred kilograms. The other has an engine with sixteen cylinders that weighs two hundred fifty-two. One costs about two million euros. The other costs three point eight million. And, by our own arithmetic, the one with less power is the one with more power for every kilogram it carries. This is the Rimac Nevera against the Bugatti Tourbillon.""",
   "Rimac Nevera and Bugatti Tourbillon", "ELECTRIC VS V16")
sc("""Here is the twist that most comparisons miss. Both cars come from the same company family. Mate Rimac, who built the Nevera, is also the chief executive of Bugatti Rimac, the company behind the Tourbillon. So one man is behind both answers to the same question: what is the future of the hypercar?""",
   "Mate Rimac", "ONE MAN BEHIND BOTH CARS")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. Let us start with the cars.""",
   "Rimac Nevera", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE TWO CARS ----------
ch("Two answers to one question")
sc("""Wikipedia says the Rimac Nevera was first shown as the C Two at the Geneva Motor Show in twenty eighteen, and was later renamed Nevera. The name refers to sudden short storms that hit the Adriatic Sea. Rimac plans to build one hundred fifty of them.""",
   "Rimac Nevera", "RIMAC NEVERA: 150 CARS")
sc("""It has four electric motors, one for each wheel. Wikipedia lists a total of one thousand eight hundred eighty-eight horsepower, or one thousand nine hundred fourteen metric horsepower, and two thousand three hundred sixty newton-metres of torque. The power comes from a one hundred twenty kilowatt-hour battery.""",
   "Rimac Nevera motors", "4 MOTORS · 1,888 HP")
sc("""The Bugatti Tourbillon is the opposite idea. Wikipedia says it was unveiled on the twentieth of June, twenty twenty-four, for three point eight million euros, about four point one million dollars. Bugatti plans to build two hundred fifty, in Molsheim, France, with production starting in twenty twenty-six.""",
   "Bugatti Tourbillon", "BUGATTI TOURBILLON: 250 CARS")
sc("""Its heart is a naturally aspirated sixteen-cylinder engine of eight thousand three hundred fifty-five cubic centimetres, developed with Cosworth. It revs to nine thousand r p m and makes about one thousand metric horsepower. Three electric motors add eight hundred more.""",
   "Bugatti Tourbillon V16", "V16 + 3 ELECTRIC MOTORS")
sc("""So here is the setup. One car says the future is a battery and four motors. The other says the future still has a sixteen-cylinder engine in it, helped by electricity. Both claim to be the ultimate hypercar. Let us see which numbers back them up, starting with the one everybody asks about first: power.""",
   "Rimac Nevera vs Bugatti Tourbillon", "SAME QUESTION, OPPOSITE ANSWERS")

# ---------- 2. POWER ----------
ch("Round one: power")
sc("""The Nevera has one thousand nine hundred fourteen metric horsepower on Wikipedia's page. The Tourbillon has one thousand eight hundred. By our own arithmetic, that makes the Nevera about six point three percent stronger on paper. Not a huge gap, but a gap.""",
   "Rimac Nevera", "1,914 PS VS 1,800 PS")
sc("""Where the power comes from is very different. Wikipedia says the Tourbillon's engine makes about one thousand metric horsepower, and the three motors add eight hundred. So more than half of the Tourbillon's power comes from the engine you can hear. In the Nevera, all of it comes from electricity.""",
   "Bugatti Tourbillon engine", "55% FROM THE ENGINE")
sc("""Torque tells another story. Wikipedia lists two thousand three hundred sixty newton-metres for the Nevera and two thousand three hundred for the Tourbillon. These are close, in our reading, but they are delivered very differently. Electric motors give torque instantly. An engine that revs to nine thousand has to climb there.""",
   "Rimac Nevera", "2,360 NM VS 2,300 NM")
sc("""Both cars use all four wheels. The Nevera has a motor at each wheel, with a single-speed gearbox on each. The Tourbillon sends its power through a new eight-speed dual-clutch gearbox. Two engineering answers, and neither one is simple.""",
   "Bugatti Tourbillon gearbox", "1 SPEED PER WHEEL VS 8-SPEED DCT")
sc("""There is one more thing on power. Wikipedia says that in August twenty twenty-four, Rimac unveiled the Nevera R, with two thousand one hundred seven metric horsepower. So the Nevera family has already moved on from the number we just compared. The Tourbillon, for now, has not.""",
   "Rimac Nevera R", "NEVERA R: 2,107 PS")

# ---------- 3. WEIGHT ----------
ch("Round two: weight")
sc("""Now the twist. Sources give two different weights for the Nevera. Wikipedia lists two thousand three hundred kilograms. Top Gear lists two thousand one hundred fifty. The Tourbillon, according to Wikipedia and Automoblog, weighs one thousand nine hundred ninety-five kilograms. So the Tourbillon is lighter either way.""",
   "Rimac Nevera", "NEVERA: 2,150–2,300 KG")
sc("""Automoblog says the Tourbillon weighs less than the Veyron and the Chiron, which is remarkable for a car with a sixteen-cylinder engine, three electric motors and a battery. Bugatti used a carbon and aluminium structure, with a carbon composite called T eight hundred.""",
   "Bugatti Tourbillon carbon", "LIGHTER THAN THE CHIRON")
sc("""Here is the maths. Take Wikipedia's figures. The Nevera has one thousand eight hundred eighty-eight horsepower and weighs two thousand three hundred kilograms. That is about point eight two horsepower per kilogram. The Tourbillon has one thousand seven hundred seventy-five horsepower and weighs one thousand nine hundred ninety-five. That is about point eight nine.""",
   "Rimac Nevera vs Bugatti Tourbillon", "OUR OWN ARITHMETIC: 0.82 VS 0.89 HP/KG")
sc("""And if you use Top Gear's lighter figure for the Nevera, two thousand one hundred fifty kilograms, its number rises to about point eight eight. The Tourbillon still comes out slightly ahead. So the less powerful car has the better power-to-weight ratio. On paper, this is the Tourbillon's first win.""",
   "Bugatti Tourbillon", "THE WEAKER CAR IS THE LIGHTER ONE")
sc("""Why is the Tourbillon so light? Part of the answer is in the suspension. TechRadar says parts of the suspension and chassis are three-D printed in aluminium, using Divergent, a sister company of the American hypercar maker Czinger. Automoblog says this saves forty-five percent of unsprung weight compared with the Chiron.""",
   "Bugatti Tourbillon suspension", "3D-PRINTED SUSPENSION")
sc("""Now compare the heavy parts. Top Gear says the Nevera's battery pack holds six thousand nine hundred sixty cells and weighs seven hundred kilograms. Automoblog says the Tourbillon's entire sixteen-cylinder engine weighs two hundred fifty-two. By our own arithmetic, the Nevera's battery alone weighs almost three times as much as the Bugatti's V sixteen.""",
   "Rimac Nevera battery", "THE BATTERY WEIGHS 2.8× THE V16")
sc("""Put another way, seven hundred kilograms is about thirty-five percent of the Tourbillon's entire weight. A battery bigger than a third of a whole car. That is the price of going fully electric, and it is the reason the Nevera needs so much power to be this fast.""",
   "Rimac Nevera chassis", "700 KG = 35% OF A TOURBILLON")

sc("""Quickness off the line is another place to look. TechRadar says the Tourbillon's zero to sixty-two miles per hour in less than two seconds is faster than the Chiron, which takes two point four. And it says the car reaches one hundred eighty-six miles per hour in under ten seconds, against thirteen point one for its predecessor.""",
   "Bugatti Chiron", "FASTER THAN THE CHIRON")
sc("""How the hybrid part works matters here too. TechRadar says two electric motors sit on the front axle and one on the rear. Automoblog says the battery is an eight hundred volt, oil-cooled pack, and the motors use silicon carbide inverters. In electric mode, TechRadar says, the Tourbillon has about seven hundred eighty-nine brake horsepower to play with.""",
   "Bugatti Tourbillon hybrid system", "800 V · OIL-COOLED · 789 BHP IN EV MODE")

# ---------- 4. BATTERIES ----------
ch("Round three: batteries, range and charging")
sc("""Wikipedia lists the Nevera's battery at one hundred twenty kilowatt-hours. The Tourbillon's is a twenty-five kilowatt-hour pack, which Wikipedia puts at twenty-four point eight. By our arithmetic, the Nevera's battery is almost five times larger.""",
   "Rimac Nevera battery pack", "120 KWH VS 24.8 KWH")
sc("""Range follows. Wikipedia gives the Nevera four hundred ninety kilometres on the W L T P test, which is about three hundred four miles. For the Tourbillon, Automoblog and Wikipedia say up to sixty kilometres, about thirty-seven miles, in electric mode only.""",
   "Rimac Nevera range", "490 KM VS 60 KM ON ELECTRICITY")
sc("""There is a caveat. Wikipedia lists the Nevera's range as four hundred ninety kilometres on the W L T P cycle, and six hundred forty-seven on the older N E D C. Different tests give different numbers, and real driving at very high speed would use the battery far faster. We quote the official figures, and nothing more.""",
   "Electric car dashboard", "OFFICIAL TESTS, NOT REAL DRIVING")
sc("""Those two numbers show the philosophy. The Nevera is a car you can actually drive on electricity. The Tourbillon uses its battery as a power boost and for quiet short trips. When the battery runs out, the sixteen-cylinder engine is waiting.""",
   "Bugatti Tourbillon", "BATTERY AS A BOOSTER")
sc("""Charging is the other side. Wikipedia says the Nevera can fast-charge to eighty percent in under thirty minutes. The Tourbillon is a plug-in hybrid, so it can charge too, but we found no published fast-charging time for it, and we will not guess.""",
   "Electric car charging", "NEVERA: 80% IN UNDER 30 MIN")
sc("""What does a full charge cost? The American Energy Information Administration average, reported in March twenty twenty-five by This Old House, was seventeen point oh one cents per kilowatt-hour. By our own arithmetic, filling a hundred twenty kilowatt-hour battery at that price costs about twenty dollars and forty cents. Filling the Tourbillon's costs about four dollars twenty.""",
   "Home charging price", "OUR ARITHMETIC: ~$20 VS ~$4")
sc("""That is an estimate, using the national average. In Hawaii, the same source gives forty-one point one one cents, and in Nebraska ten point eight nine. But the point stands. Nobody buys a two million euro hypercar to save on fuel. They buy it for what the two cars can do.""",
   "Electric meter", "ENERGY PRICE VARIES BY STATE")
sc("""There is also the warranty, which is a hint of how Rimac sees its own battery. According to Indigo Auto Group, in January twenty twenty-four Rimac extended the Nevera's warranty to eight years with unlimited miles, with the battery guaranteed to keep at least seventy-five percent of its capacity.""",
   "Rimac Nevera warranty", "8 YEARS, UNLIMITED MILES")

# ---------- 5. SPEED ----------
ch("Round four: speed and records")
sc("""Now the question everyone wants answered. Wikipedia says the Nevera reached four hundred twelve kilometres per hour, about two hundred fifty-six miles per hour, in videos published in November twenty twenty-two. And in August twenty twenty-four, Rimac said the Nevera R reached four hundred thirty-one point six.""",
   "Rimac Nevera top speed", "412 KM/H · NEVERA R: 431.6")
sc("""The Tourbillon is different. Automoblog and Wikipedia say its top speed is electronically limited to three hundred eighty kilometres per hour, about two hundred thirty-six miles per hour. With a special speed key, the limit rises to four hundred forty-five kilometres per hour, about two hundred seventy-six miles per hour.""",
   "Bugatti Tourbillon top speed", "380 KM/H, OR 445 WITH THE KEY")
sc("""Read that carefully. Bugatti's number is a limit. The Nevera's four hundred twelve was a measured run. And TechRadar says that Bugatti is being coy about potential top speeds, and that the car has plenty left to chase the production car record. So nobody has yet shown what the Tourbillon can do.""",
   "Bugatti Tourbillon", "A LIMIT IS NOT A RECORD")
sc("""Acceleration is where the Nevera has already proved itself. Wikipedia says that on the seventeenth of May, twenty twenty-three, the Nevera set twenty-three records. It went from zero to one hundred kilometres per hour in one point eight two seconds, and ran the quarter mile in eight point two five.""",
   "Rimac Nevera acceleration", "0–100 KM/H IN 1.82 SECONDS")
sc("""The Tourbillon is expected to be as quick. Wikipedia says Bugatti expects zero to one hundred in under two seconds, zero to two hundred in under five, zero to three hundred in under ten, and zero to four hundred in under twenty-five. Notice the words: expects. These are targets, not measurements.""",
   "Bugatti Tourbillon acceleration", "TARGETS, NOT RESULTS")
sc("""And here is a trap. The Nevera's famous zero to four hundred and back to zero record, set at twenty-nine point nine three seconds, includes the braking. The Tourbillon's under twenty-five seconds is only the way up. They measure different things. Comparing them directly would be unfair, and we will not do it.""",
   "Rimac Nevera 0-400-0", "DIFFERENT TESTS, DIFFERENT RESULTS")
sc("""For the record, Wikipedia says the Nevera R then took twenty-four records on the tenth of July, twenty twenty-five, including zero to four hundred and back to zero in twenty-five point seven nine seconds. It says the previous holder, the Koenigsegg Jesko Absolut, took twenty-seven point nine three.""",
   "Rimac Nevera R record", "NEVERA R: 25.79 SECONDS")
sc("""On the track, the Nevera also has results. Wikipedia lists forty-nine point three two seconds at the Goodwood hillclimb, and seven minutes five point two nine eight seconds at the Nürburgring, set in August twenty twenty-three by Kodrić. We did not find a published lap time for the Tourbillon.""",
   "Nürburgring Nordschleife", "NÜRBURGRING: 7:05.298")

# ---------- 6. THE V16 ----------
ch("Why Bugatti kept the sixteen cylinders")
sc("""So why would Bugatti build a sixteen-cylinder engine in the age of electric cars? Wikipedia says the Tourbillon shares no parts with the Chiron, and its engine is all new, the first all-new Bugatti petrol engine since the Veyron and Chiron.""",
   "Bugatti Tourbillon V16", "AN ALL-NEW V16")
sc("""Automoblog says it has no turbochargers, unlike the Chiron. The Chiron's sixteen-cylinder engine was turbocharged. This one breathes naturally, and Automoblog notes that this means one thousand horsepower without any help from turbos, and a redline of nine thousand r p m.""",
   "Bugatti V16 engine bay", "NO TURBOS, 9,000 RPM")
sc("""Automoblog quotes Mate Rimac saying that beauty, performance and luxury formed the blueprint for the Tourbillon, a car more elegant, more emotive and more luxurious than anything before it. He also quotes Ettore Bugatti's mantras: if comparable, it is no longer Bugatti. And, nothing is too beautiful.""",
   "Ettore Bugatti", "\"IF COMPARABLE, IT IS NO LONGER BUGATTI\"")
sc("""Look at it from the Nevera's side. A car that makes eighteen hundred eighty-eight horsepower from batteries has no engine noise to give. Rimac's argument is that electricity delivers more. Bugatti's argument is that some things cannot be replaced. Neither company says it is wrong, and both can point to numbers.""",
   "Rimac Nevera", "TWO PHILOSOPHIES")

# ---------- 7. THE CABINS ----------
ch("Round five: what you touch and see")
sc("""Inside the Tourbillon, the first thing you notice is a watch. The name comes from a mechanism found in expensive mechanical watches. Automoblog says the instruments were designed and built with Swiss watchmakers and have more than six hundred parts, in titanium, sapphire and ruby.""",
   "Bugatti Tourbillon interior", "600+ PARTS · TITANIUM, SAPPHIRE, RUBY")
sc("""TechRadar says the driver wakes the V sixteen by pulling an organ stop lever, like an old choke, and the start button in the centre console is cut from crystal glass. The steering wheel turns around a fixed centre, so the gauges stay in view no matter how you steer.""",
   "Bugatti Tourbillon steering wheel", "THE WHEEL TURNS, THE GAUGES DON'T")
sc("""Automoblog adds that the stereo has no conventional speakers or subwoofers, and that a screen rises from the centre console only when wanted. TechRadar says the doors open upward, as dihedral doors, driven by electric motors. An old craft, and new technology, in one cabin.""",
   "Bugatti Tourbillon doors", "A SCREEN THAT HIDES")
sc("""The Nevera takes the opposite route. Rimac pushes technology to the front. We covered the Nevera's driver coach and sensors in another video of this series, and we will not repeat the details here. The point is that one cabin celebrates a mechanical past, and the other a digital future.""",
   "Rimac Nevera interior", "MECHANICAL PAST VS DIGITAL FUTURE")

# ---------- 8. PRICE ----------
ch("Round six: price and rarity")
sc("""Now money. CNBC puts the Nevera at about two million euros, or two point one million dollars. Motor1 reports a sticker price of two million one hundred thirty-six thousand euros in twenty twenty-three, with extras like a carbon package at eighty thousand. Top Gear gave the price as one point seven million pounds. Sources differ.""",
   "Rimac Nevera price", "NEVERA: ~€2M")
sc("""The Tourbillon starts at three point eight million euros, according to Wikipedia and Automoblog, which is about four point one million dollars. By our own arithmetic, that is between about one point eight and one point nine times the Nevera's price. A gap of roughly one point six million euros, using Motor1's figure.""",
   "Bugatti Tourbillon price", "TOURBILLON: €3.8M")
sc("""Rarity points the other way. Rimac plans one hundred fifty Neveras. Bugatti plans two hundred fifty Tourbillons. So the more expensive car is also the more common one. TechRadar says around eighty would be built per year. By our arithmetic, that is about three years of production.""",
   "Bugatti Molsheim", "150 NEVERAS · 250 TOURBILLONS")
sc("""Timing is not settled either. One source says first customer deliveries were expected in twenty twenty-six. TechRadar says some customers may get theirs as late as twenty thirty. We will not choose between them. The two sources disagree, and the car was still in testing when they wrote.""",
   "Bugatti Tourbillon testing", "WHEN DO DELIVERIES START?")
sc("""And the Nevera is already in customers' hands. Wikipedia says the first car went to Nico Rosberg in August twenty twenty-two, with deliveries in the United States starting in June twenty twenty-three. Motor1 reports a used one with just one thousand three hundred forty-one miles reaching a bid of over one million dollars on Bring a Trailer in March twenty twenty-five.""",
   "Nico Rosberg Rimac Nevera", "DELIVERED SINCE AUGUST 2022")
sc("""That bid is not a final price, and we do not claim it is. But it is a sign that a used Nevera, at that moment, was attracting serious money. For the Tourbillon, with deliveries only starting, there is no used market yet to compare.""",
   "Bring a Trailer auction", "USED NEVERA: $1M+ BID")

# ---------- 9. ONE MAN ----------
ch("The twist: one man behind both")
sc("""Here is the part that makes this comparison unusual. Wikipedia says Bugatti Rimac was formed in November twenty twenty-one. Rimac Group held fifty-five percent, and Porsche forty-five. Mate Rimac became its chief executive. So the same person is responsible for the electric hypercar and the one with a sixteen-cylinder engine.""",
   "Mate Rimac Bugatti", "BUGATTI RIMAC, NOVEMBER 2021")
sc("""Wikipedia says Rimac's story began with an old BMW E thirty, which he converted to electric power after its petrol engine blew up. Rivals called it a washing machine. Today the same man is chief executive of the company that built a sixteen-cylinder Bugatti. That is an unusual place for an electric pioneer.""",
   "Mate Rimac BMW E30", "FROM A GARAGE TO BUGATTI")
sc("""One caution about ownership. Wikipedia says that in April twenty twenty-six, Porsche sold its stake to H O F Capital. Ownership of the company may keep changing, so we will not state the current split as fact. What stays fixed is the point: these two cars are not rivals from two companies. They are siblings.""",
   "Bugatti Rimac Molsheim", "SIBLINGS, NOT RIVALS")
sc("""That helps explain the numbers. The Tourbillon is lighter and more refined. The Nevera is quicker off the line and has records. Neither car was designed to beat the other. They were designed to show two different roads to the same destination, by the same people.""",
   "Rimac Nevera and Bugatti Tourbillon", "TWO ROADS, ONE DESTINATION")

sc("""Think about what each car asks of its owner. The Nevera asks for a charger, and a warranty that covers the battery for eight years. The Tourbillon asks for petrol and a plug, and its sixteen-cylinder engine has to be serviced like any engine. We found no published service prices for either car, so we cannot compare running costs.""",
   "Hypercar garage", "RUNNING COSTS: NO PUBLISHED FIGURES")

# ---------- 10. VERDICT ----------
ch("The verdict")
sc("""So who wins? On power, the Nevera, by about six percent. On weight and power-to-weight, the Tourbillon. On battery and range, the Nevera, by far. On measured records, the Nevera, as the Tourbillon has none we could find. On price, the Nevera is cheaper. On cabin craft, the Tourbillon.""",
   "Rimac Nevera vs Bugatti Tourbillon", "SCORECARD")
sc("""But these numbers are only the start. A hypercar is not bought for a lap time. The Nevera is a showcase for what batteries and motors can do. The Tourbillon is a showcase for what a naturally aspirated engine can still do. Each one will matter to its fans for a different reason.""",
   "Hypercar side by side", "DIFFERENT REASONS TO WANT EACH")
sc("""We also want to be clear about what this video cannot tell you. The Tourbillon had not yet reached customers in the sources we read, so its real-world results are still to come. When owners and testers publish measured numbers, the scorecard may change. We will update our figures when they do.""",
   "Bugatti Tourbillon", "THE SCORECARD MAY CHANGE")
sc("""Which would you choose, the electric storm or the sixteen-cylinder watch? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Nevera, work out what an electric hypercar really costs, and tell the story of the kid from Croatia who ended up running Bugatti.""",
   "Rimac Nevera", "WHICH WOULD YOU CHOOSE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more comparisons between the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video86", "Rimac Nevera vs Bugatti Tourbillon: Electric vs V16", [
    "Wikipedia, Rimac Nevera: https://en.wikipedia.org/wiki/Rimac_Nevera",
    "Wikipedia, Bugatti Tourbillon: https://en.wikipedia.org/wiki/Bugatti_Tourbillon",
    "Wikipedia, Mate Rimac: https://en.wikipedia.org/wiki/Mate_Rimac",
    "Wikipedia, Bugatti Rimac: https://en.wikipedia.org/wiki/Bugatti_Rimac",
    "Automoblog, Bugatti Tourbillon: https://www.automoblog.com/bugatti-tourbillon/",
    "TechRadar, Meet Bugatti's new Tourbillon: https://www.techradar.com/vehicle-tech/hybrid-electric-vehicles/meet-bugattis-new-tourbillon-a-luxury-watch-inspired-hybrid-that-hits-1775bhp-and-rips-up-the-performance-car-rulebook",
    "Yahoo / Business Insider, Bugatti's $4 million hypercar: https://ca.news.yahoo.com/bugattis-4-million-hypercar-1-122818250.html",
    "Top Gear, Rimac Nevera review",
    "Indigo Auto Group, Rimac Nevera warranty extension (23 January 2024)",
    "CNBC, Rimac Nevera price coverage",
    "Motor1, Rimac Nevera pricing and Bring a Trailer sale (March 2025)",
    "This Old House, average electricity cost per kWh by state (EIA, March 2025)",
], "B")
