import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Behind the seats of the Rimac Nevera, there is a fire extinguisher with a strap that says, in case of hill climb, extinguish fire. It is a joke, and it points to one of the most famous crashes in television history. And that is only the first of two things you probably did not know about the world's most powerful electric hypercar.""",
   "Rimac Nevera", "2 THINGS YOU DIDN'T KNOW ABOUT THE RIMAC NEVERA")
sc("""Here is the second hint. A car built to set acceleration records also carries a full set of self-driving sensors, and an artificial intelligence coach that can teach you how to drive on a track, without a human instructor beside you. A fire joke and a robot coach, inside the same car.""",
   "Rimac Nevera interior", "A FIRE JOKE AND A ROBOT COACH")
sc("""Every figure in this video comes from a published source, listed in the description. Where sources disagree, or a number is our own arithmetic, we will say so. Let's start with the joke.""",
   "Rimac Nevera front", "EVERY FIGURE IS SOURCED")

# ---------- THING ONE ----------
ch("Thing one: the fire joke")
sc("""Wikipedia says that a fire extinguisher is mounted in the rear of the Nevera, with a strap reading, in case of hill climb, extinguish fire. The page explains the reference. It points to Richard Hammond, who crashed a Rimac Concept One during a hill climb, after which the car caught fire. He survived with a broken leg.""",
   "Rimac Nevera fire extinguisher", "\"IN CASE OF HILL CLIMB, EXTINGUISH FIRE\"")
sc("""Electrek reports the crash happened on the tenth of June, twenty seventeen, in Switzerland, while Hammond was filming the second season of The Grand Tour for Amazon Prime. It took place after the Hemberg hill climb. The car, the article says, was completely destroyed.""",
   "Hemberg hill climb Switzerland", "JUNE 10, 2017, SWITZERLAND")
sc("""The show's statement said Hammond was conscious and talking, and climbed out of the car himself before it burst into flames. He was flown by air ambulance to a hospital in St. Gallen, and was found to have a fractured knee, Electrek says. The cause was unknown and under investigation.""",
   "air ambulance helicopter", "HE CLIMBED OUT BEFORE THE FIRE")
sc("""Jeremy Clarkson, who witnessed the crash, was quoted by Electrek saying it was the biggest crash he had ever seen and the most frightening. Yet Clarkson also said Richard seemed to be mostly okay. A destroyed car, a broken knee, and a presenter who walked away.""",
   "Jeremy Clarkson", "CLARKSON: \"THE MOST FRIGHTENING\"")
sc("""The car was the Rimac Concept One. Electrek says it cost about one million dollars, was built in Croatia, and in its upgraded form, with a ninety kilowatt-hour battery pack, made nine hundred kilowatts, or twelve hundred twenty-four horsepower. It could go from zero to sixty miles per hour in two point four seconds.""",
   "Rimac Concept One", "THE CONCEPT ONE: 1,224 HP")
sc("""The Concept One was the company's first car. Wikipedia's page on Mate Rimac says it was presented at the twenty eleven Frankfurt Motor Show, and that the company grew from its first employees in twenty eleven to more than one thousand by twenty twenty. A tiny team in Croatia had built a car that could take on the world.""",
   "Rimac Concept One Frankfurt 2011", "THE FIRST CAR: FRANKFURT 2011")
sc("""Rimac told Electrek it planned to make only eight units of the updated version. So the car that burned in Switzerland was one of an extremely small number. And PopSci says the crash gave the little Croatian company global attention, when the prototype, as it puts it, caught fire and was destroyed in dramatic fashion.""",
   "Rimac Concept One prototype", "ONLY 8 UPDATED CARS PLANNED")
sc("""Compare the two cars. The Concept One made twelve hundred twenty-four horsepower and cost about one million dollars, according to Electrek. The Nevera makes eighteen hundred eighty-eight horsepower, according to Wikipedia, and costs a little over two point one million dollars, according to CNBC. That is about fifty-four percent more power for about twice the price, by our own arithmetic.""",
   "Rimac Concept One and Nevera", "+54% POWER FOR ~2x THE PRICE (OUR MATH)")
sc("""And the acceleration improved. Electrek lists the Concept One at two point four seconds to sixty miles per hour. Rimac claims one point seven four seconds for the Nevera to ninety-seven kilometers per hour, which is sixty miles per hour. That is about twenty-seven percent less time, by our own arithmetic, within a few years.""",
   "Rimac acceleration comparison", "2.4 s TO 1.74 s (-27%)")
sc("""Here is what makes the joke clever. Rimac could have hidden the accident. Instead, it put the reference on a strap, inside the car it sells for two million euros. In our reading, many companies would avoid mentioning their most embarrassing moment. Rimac turned it into a feature.""",
   "Rimac Nevera rear", "RIMAC PUT THE JOKE ON THE CAR")
sc("""And the joke has a serious side. Wikipedia says crash testing of the Nevera for homologation finished in February twenty twenty-two, after four years. Four years of crash testing, for a car of which only one hundred fifty will be built. Every car had to be proven safe before any customer could drive it.""",
   "Rimac crash test", "4 YEARS OF CRASH TESTING")
sc("""Top Gear says the Nevera's structure is made entirely of carbon fiber, with a bonded roof, an integrated battery housing and a rear subframe. In other words, the battery is part of the car's skeleton. That matters in a crash, because the battery is the heaviest and most dangerous part of any electric car.""",
   "Rimac Nevera chassis", "THE BATTERY IS PART OF THE SKELETON")
sc("""Wikipedia also says the Nevera's doors are butterfly doors. PopSci adds that you have to elbow the flip-up scissor door like you mean it to get it to open. A car that is built to survive a crash, with doors that need a firm push, and a strap that reminds you of the car that did not.""",
   "Rimac Nevera butterfly door", "DOORS THAT NEED A FIRM ELBOW")

# ---------- THE NAME AND THE CAR ----------
ch("Meet the car")
sc("""Before the second thing, let's meet the car. Wikipedia says it was unveiled at the twenty eighteen Geneva Motor Show as the Rimac C Two, and renamed Nevera at launch. The name refers to sudden and short storms in Croatia, usually with lightning, mainly on the Adriatic coast.""",
   "Rimac C_Two Geneva 2018", "NAMED AFTER ADRIATIC STORMS")
sc("""The numbers are huge. Wikipedia lists four permanent magnet motors, one at each wheel, with a combined output of fourteen hundred seven point seven kilowatts, eighteen hundred eighty-eight horsepower, and twenty-three hundred sixty newton-meters of torque, from a one hundred twenty kilowatt-hour battery.""",
   "Rimac Nevera motors", "1,888 HP FROM 4 MOTORS")
sc("""Top Gear describes the battery as a six thousand nine hundred sixty-cell pack in an H shape along the spine and behind the cockpit, and says the pack weighs seven hundred kilograms. Wikipedia lists the car's curb weight at twenty-three hundred kilograms. Top Gear gives twenty-one hundred fifty. The sources disagree.""",
   "Rimac Nevera battery pack", "6,960 CELLS, 700 KG")
sc("""The range numbers vary by source. Wikipedia lists four hundred ninety kilometers on the W L T P test, about three hundred miles, and six hundred forty-seven kilometers on the older N E D C test. Top Gear lists five hundred forty-seven kilometers on W L T P. Different test versions and different sources, so treat every range figure as approximate.""",
   "Rimac Nevera range", "RANGE: 490-547 KM (SOURCES DIFFER)")
sc("""Charging is fast. Wikipedia says fast charging to eighty percent takes under thirty minutes. Top Gear says that on a five hundred kilowatt charger, the car goes from zero to eighty percent in nineteen minutes. And Top Gear's reviewers switched to range mode on a long drive and arrived with ninety-seven kilometers still on the range display.""",
   "electric hypercar charging", "0-80% IN ~19 MINUTES")
sc("""The chassis is more than carbon. Top Gear says the Nevera is suspended on double wishbones all round, with electronically controlled dampers and active ride height, so it is tolerably comfortable at everyday speeds, if occasionally crashy over sudden surface imperfections and potholes. A hypercar, but one that is meant to be driven on real roads.""",
   "Rimac Nevera suspension", "ACTIVE RIDE HEIGHT, REAL ROADS")
sc("""Rimac says the Nevera goes from zero to one hundred kilometers per hour in one point eight two seconds, and through the quarter mile in eight point two five seconds. On the seventeenth of May, twenty twenty-three, Rimac announced twenty-three records set in one day, including zero to four hundred and back to zero in twenty-nine point nine three seconds.""",
   "Rimac Nevera record run", "23 RECORDS IN ONE DAY")
sc("""PopSci adds details of the hardware. It lists fifteen point three inch Brembo carbon ceramic brakes with six-piston calipers, and Michelin Pilot Sport four S tires. And it says the rear wing deploys as an air brake after a drag run, which the author compares to a drag chute.""",
   "Rimac Nevera brakes", "THE WING THAT BRAKES LIKE A PARACHUTE")
sc("""PopSci also mentions that drag racing rules require a full roll cage for any vehicle running under ten seconds in the quarter mile. The Nevera runs the quarter mile in about eight point six seconds, according to the article, and eight point two five, according to Rimac. A road car that is faster than the rules for normal road cars.""",
   "NHRA drag strip", "FASTER THAN THE DRAG STRIP RULES")
sc("""The launch procedure is simple. PopSci says you hold the brake, floor the accelerator, then release the brake. The author describes it as high-g teleportation. And Top Gear says that the next ten or fifteen seconds are simply vaporized, and time ceases to exist.""",
   "Rimac Nevera launch", "\"HIGH-G TELEPORTATION\"")

# ---------- THING TWO ----------
ch("Thing two: the robot coach")
sc("""Now the second thing. PopSci reports that the Nevera comes with an artificial intelligence driver coach. It analyzes track driving using the car's sensors, and gives guidance to customers without a supervising instructor. So a two million dollar car comes with a teacher built in.""",
   "Rimac Nevera AI driver coach", "A BUILT-IN AI DRIVING COACH")
sc("""Top Gear says the car's sensor set is surprisingly large. It lists twelve ultrasonic sensors, thirteen cameras and six radars, which feed a Rimac version of the car's level four autonomy capability. Wikipedia confirms the Nevera includes sensors for S A E level four autonomy, with full driver assistance.""",
   "Rimac Nevera sensors", "12 ULTRASONIC, 13 CAMERAS, 6 RADARS")
sc("""That means a hypercar built for extreme performance has hardware for self-driving. Top Gear also says Rimac developed its own data system, and that almost everything in the cabin is proprietary, from the infotainment software to the switches. This is a technology company that happens to build a car.""",
   "Rimac Nevera technology", "A TECH COMPANY THAT BUILDS A CAR")
sc("""PopSci explains how the car's brain works. The Rimac all-wheel torque vectoring system replaces ordinary stability and traction control. The car's computer adjusts the power delivery to each wheel one hundred times a second, using the drive mode, throttle position, steering wheel angle and detected tire slip.""",
   "Rimac torque vectoring", "100 ADJUSTMENTS PER SECOND, PER WHEEL")
sc("""CNBC makes the same point, and adds the effect. The car's systems adjust each motor's power output one hundred times a second, yet it never feels uncontrollable, which the reviewer calls a significant engineering achievement. Top Gear says it makes one hundred calculations a second, working predictively and responsively.""",
   "Rimac Nevera cornering", "FAST, BUT NEVER UNCONTROLLABLE")
sc("""Braking is a second computer problem. Top Gear says the Nevera distributes braking force between its friction brakes and its regenerative braking, depending on which is thermally optimal at that moment, and has the highest amount of regenerative braking of any electric car on sale. It lets you drive in one-pedal mode on a twisty road.""",
   "Rimac Nevera regenerative braking", "THE MOST REGEN OF ANY EV ON SALE")
sc("""Top Gear also admits it is not perfect. The review says there is still work to be done blending the friction brakes with the regenerative braking, and that Rimac's engineers were still finessing it. A car with a computer making a hundred calculations a second still needs human engineers to make the brake pedal feel right.""",
   "Rimac engineers", "ENGINEERS STILL TUNING THE PEDAL")
sc("""PopSci lists the drive modes. Comfort balances mileage and performance. Sport sharpens throttle, brake and steering. Drift sends all power to the rear wheels. Track maximizes performance through all four wheels, and Range minimizes energy use. Top Gear says the modes effectively turn the Nevera into five cars in one.""",
   "Rimac Nevera drive modes", "FIVE CARS IN ONE")
sc("""Here is the twist. A car with this much computing power is easy to drive. CNBC says the Nevera is simple to operate and easy to see out of, with a rear window big enough for highway traffic. Top Gear says it can do a very reasonable impression of a Bentley Continental GT.""",
   "Rimac Nevera road", "EASY TO DRIVE LIKE A BENTLEY")

# ---------- QUIRKS ----------
ch("The quirks")
sc("""Not everything is perfect. CNBC notes that gears are shifted with a big knob to the left of the steering wheel, and that the power seat's adjustments are hidden in a touchscreen. Top Gear says the heating and cooling system is the only borrowed component, and comes from the Audi R eight.""",
   "Rimac Nevera cabin controls", "THE HVAC COMES FROM AN AUDI R8")
sc("""The cabin is otherwise bespoke. Top Gear says the switches are made from billet aluminum, there are three high-definition screens running bespoke software, and there are no column stalks, with the indicators on buttons in Ferrari fashion. Rimac developed almost everything in-house, which is why the Audi air conditioning stands out.""",
   "Rimac Nevera dashboard", "BILLET ALUMINUM AND THREE SCREENS")
sc("""Storage is tiny. Top Gear says space is limited to a hundred liters behind the cockpit, above the central battery pack, soft bags only, rather than suitcases. And PopSci says the cabin is as cramped as a space capsule, with a shallow footwell and a rear bulkhead that limits seat recline.""",
   "Rimac Nevera luggage", "100 LITERS OF LUGGAGE SPACE")
sc("""There is also a noise problem. PopSci says road noise from the tires transmits through the rigid carbon structure, and adding sound deadening would add weight, so the author suggests turning up the audio. Top Gear says the structure is so stiff that engineers are still chasing noise ghosts in the machine.""",
   "Rimac Nevera carbon structure", "TOO STIFF TO BE QUIET")
sc("""The sound is not what you expect either. CNBC calls it mellifluous mechanical, loud enough to remind you that you are in a hypercar, but quiet enough to talk over. Top Gear says it does not sizzle like a V twelve, but actually sounds really good, an authentic mix of whoosh, whir and science fiction.""",
   "Rimac Nevera sound", "WHOOSH, WHIR AND SCI-FI")
sc("""That stiffness is a feature. Top Gear says the body's rigidity is seventy thousand newton-meters per degree, about twice as stiff as the Lamborghini Aventador, and Rimac claims it is the most rigid road car ever made. A one-piece carbon structure, with the battery as part of it.""",
   "Rimac Nevera carbon monocoque", "70,000 Nm/DEGREE: MOST RIGID CAR")
sc("""CNBC mentions a small design detail. The side intakes are styled to resemble a cravat, a nod to Croatian heritage. A car built in Croatia, with a necktie in the bodywork, and a company founded by a Croatian engineer.""",
   "Rimac Nevera side intake", "THE CRAVAT INTAKE")
sc("""Critics are not unanimous. Wikipedia says Top Gear gave the twenty twenty-one pre-production car nine out of ten, while The Verge criticized its looks as anonymous and unexciting. Top Gear's own review calls it a sort of techno Pagani, with as much focus on artistry as artificial intelligence.""",
   "Rimac Nevera design", "9/10 FROM TOP GEAR. \"ANONYMOUS\" FROM THE VERGE.")

# ---------- THE RECORDS ----------
ch("The records")
sc("""The Nevera's records keep growing. Wikipedia says that on the seventeenth of July, twenty twenty-three, it became the fastest production electric car at the Goodwood Festival of Speed, with forty-nine point three two seconds. A month later, on the eighteenth of August, Martin Kodrić set seven minutes five point two nine eight seconds at the Nürburgring.""",
   "Nürburgring Nordschleife", "NÜRBURGRING: 7:05.298")
sc("""Then came the Nevera R. Wikipedia says it was unveiled on the seventeenth of August, twenty twenty-four, with two thousand one hundred seven metric horsepower, a top speed of four hundred thirty-one point six kilometers per hour, and zero to three hundred in seven point eight nine seconds.""",
   "Rimac Nevera R", "NEVERA R: 2,107 PS")
sc("""On the tenth of July, twenty twenty-five, the R set twenty-four records at Papenburg, including zero to four hundred and back to zero in twenty-five point seven nine seconds. Wikipedia says that beat the Koenigsegg Jesko Absolut's twenty-seven point nine three seconds. Rimac had won back a record it had lost.""",
   "Papenburg test track", "0-400-0 KM/H IN 25.79 SECONDS")
sc("""The R is not just more power. Wikipedia says it has a fixed rear wing, a larger diffuser and a redesigned front bumper, with fifteen percent more downforce, and weighs about twenty-two hundred sixty-five kilograms. The standard car's top speed was shown at four hundred twelve kilometers per hour at Papenburg in videos released in November twenty twenty-two.""",
   "Rimac Nevera R rear wing", "NEVERA R: +15% DOWNFORCE")

# ---------- THE CAR'S PRICE AND OWNERSHIP ----------
ch("Owning one")
sc("""CNBC says the Nevera starts at two million euros, or just over two point one million dollars. PopSci says about two point two million dollars. Rimac plans to build just one hundred fifty. Wikipedia says the first production-spec car was delivered in August twenty twenty-two to Nico Rosberg, as car number one.""",
   "Nico Rosberg Rimac Nevera", "FROM €2 MILLION. CAR #1 TO NICO ROSBERG")
sc("""Top Gear says Rimac planned to make fifty cars a year for the next three years. By our own arithmetic, that is a hundred fifty cars, exactly the planned total. Top Gear adds that Rimac set up a global dealer network of nineteen sites. Wikipedia says U S deliveries began in June twenty twenty-three.""",
   "Rimac dealership", "50 PER YEAR FOR 3 YEARS = 150")
sc("""CNBC notes that Rimac is Croatia's first and only automaker, founded in two thousand nine by Mate Rimac, and that it also consults for automakers such as Aston Martin and Koenigsegg. A company that builds hypercars also sells its technology to other car companies. That is a second business, behind the car you see.""",
   "Rimac Technology battery", "CROATIA'S ONLY AUTOMAKER")
sc("""In January twenty twenty-four, Rimac extended the Nevera battery warranty to eight years with unlimited mileage, covering major battery faults and guaranteeing at least seventy-five percent of the original capacity. A commercial director said the electric motors are maintenance free for life. That is an unusual promise for a hypercar.""",
   "Rimac Nevera warranty", "8-YEAR BATTERY WARRANTY, UNLIMITED MILES")
sc("""The warranty says something about the battery. A Bugatti Rimac commercial director said a lot of mass market electric vehicles cover their batteries for around eight years, limiting mileage to roughly the one hundred thousand mark. So for Rimac, extending to eight years and unlimited miles was, in his words, hugely significant.""",
   "electric car battery warranty", "\"HUGELY SIGNIFICANT\"")
sc("""Deliveries were slower than Rimac planned. Wikipedia says that in May twenty twenty-four, Mate Rimac said more than fifty cars had been delivered, which was slower than expected. A car that takes time to build, with a factory that is still growing, for a company that began in a garage.""",
   "Rimac factory Croatia", "50 DELIVERED BY MAY 2024")
sc("""The pre-sales were strong. The Croatian news site N one info reported in March twenty twenty-three that the Nevera's starting price was two million euros and fifty had already been sold. Wikipedia says the factory in Veliko Trgovišće opened in June twenty twenty. So a third of the planned cars were sold before most customers had taken delivery.""",
   "Rimac campus Croatia", "50 SOLD BY MARCH 2023")

# ---------- THE ANSWER ----------
ch("Two things, one car")
sc("""So here are the two things again. First, the Nevera carries a fire extinguisher strap that jokes about Richard Hammond's crash in Switzerland in twenty seventeen. Second, it has a full set of self-driving sensors and an artificial intelligence coach that teaches you how to drive it on a track.""",
   "Rimac Nevera", "THE TWO THINGS")
sc("""When Rimac announced the Nevera, PopSci quotes Mate Rimac saying this is the car he had in mind when he embarked on the impossible journey. A fire joke, a robot coach, a necktie-shaped air intake and a record book. It is a car that is serious about speed, and does not take itself too seriously.""",
   "Mate Rimac", "\"THE CAR I HAD IN MIND\"")
sc("""Which one surprised you more? Tell us in the comments. In the other videos of this series, we compare the Nevera with the new Bugatti Tourbillon, work out what an electric hypercar really costs, and tell the story of the Croatian kid who ended up running Bugatti.""",
   "Bugatti Tourbillon", "WHICH ONE SURPRISED YOU?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video85", "2 Things You Didn't Know About the Rimac Nevera", [
    "Wikipedia, Rimac Nevera: https://en.wikipedia.org/wiki/Rimac_Nevera",
    "Electrek, Richard Hammond crash, Rimac Concept One (June 2017): https://electrek.co/2017/06/10/richard-hammond-crash-rimac-concept_one-all-electric-supercar/",
    "CNBC, Rimac Nevera review (Sept 2023): https://www.cnbc.com/2023/09/16/rimac-nevera-ev-review-powerful-easy-to-drive.html",
    "Popular Science, Driving the Rimac Nevera: https://www.popsci.com/technology/rimac-nevera-ev-first-drive/",
    "Top Gear Malaysia, Rimac Nevera review: https://topgear.com.my/reviews/rimac-nevera-review-a-hypercar-sensation",
    "Indigo Auto Group, Rimac extends Nevera battery warranty to 8 years (Jan 2024): https://news.indigoautogroup.com/blog-posts/rimac-has-enhanced-the-neveras-battery-warranty-to-8-years",
], "A")
