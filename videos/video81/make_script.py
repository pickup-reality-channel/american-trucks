import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The McLaren F one was built with a small amount of real gold inside its engine bay. Not as decoration. As a heat shield. And the same car, a road car with a luggage set and air conditioning, went on to win the twenty-four hours of Le Mans at its very first attempt, even though its creator never wanted it to race. Those are the two things you probably did not know about the McLaren F one.""",
   "McLaren F1", "2 THINGS YOU DIDN'T KNOW ABOUT THE McLAREN F1")
sc("""Here is the twist. The first fact explains why the second one was possible. Because the same obsession that led to gold foil, an obsession with weight and heat, is what made a road car light enough and reliable enough to beat purpose-built prototypes in the rain.""",
   "McLaren F1 engine bay", "THE GOLD AND THE RACE ARE CONNECTED")
sc("""Every figure in this video comes from a published source, listed in the description. Where a number is an estimate, or our own arithmetic, we will say so. Let's start with the gold.""",
   "McLaren F1 front", "EVERY FIGURE IS SOURCED")

# ---------- THING ONE ----------
ch("Thing one: the gold")
sc("""Wikipedia says that to protect the car from the heat of its own engine, the designers lined the engine bay with a highly efficient heat reflector, gold foil. The page adds a precise number. Approximately sixteen grams, about half an ounce, of gold was used in each car.""",
   "McLaren F1 gold foil engine bay", "~16 GRAMS OF GOLD IN EVERY CAR")
sc("""Why gold? Because it reflects heat extremely well. And the F one needed that, because of where the engine sits. Another source, the Gooding and Company auction coverage, explains that gold foil was used in specific areas to reduce heat transfer, an important consideration in a car where the V twelve sat just behind the cabin.""",
   "McLaren F1 engine", "GOLD REFLECTS HEAT")
sc("""That engine matters too. Wikipedia says it was a BMW S seventy slash two, a sixty-degree V twelve of six thousand sixty-four cubic centimeters, designed by BMW's motorsport division under Paul Rosche. It made six hundred eighteen horsepower at seven thousand four hundred r p m, and four hundred seventy-nine pound-feet of torque at five thousand six hundred.""",
   "BMW S70/2 V12", "BMW V12: 618 HP, 6.1 LITERS")
sc("""The engine alone weighed two hundred sixty-six kilograms, or five hundred eighty-six pounds, according to Wikipedia. And it was not McLaren's first choice. Gooding and Company says that McLaren's Formula One cars used Honda engines in the late nineteen eighties, but Honda would not build an engine for the road car.""",
   "McLaren Honda Formula One 1988", "HONDA SAID NO")
sc("""So designer Gordon Murray shopped around, the article says, and found a collaborator in BMW's motorsport division. One of Murray's non-negotiables was that the engine had to be naturally aspirated, with no turbos. And the result made far more power than planned. The car's original goal was five hundred fifty horsepower. The engine delivered six hundred twenty-seven metric horsepower without further tuning.""",
   "BMW M engine workshop", "THE GOAL WAS 550 HP")
sc("""Do the arithmetic. Six hundred eighteen horsepower against a goal of five hundred fifty is about twelve percent more than planned, by our own arithmetic. But the engine also came in above Murray's planned weight limit, Gooding and Company says. Even in the best car of its time, there were trade-offs.""",
   "McLaren F1 rear", "12% MORE POWER THAN PLANNED")
sc("""Gooding and Company adds that the engine drove the rear wheels only, through a transversely mounted six-speed manual gearbox. And Wikipedia gives the compression ratio, eleven to one. A naturally aspirated sixty-degree V twelve, with a manual gearbox, in a car that cost five hundred forty thousand pounds. No turbos, no paddles.""",
   "McLaren F1 gearbox", "NO TURBOS. NO PADDLES.")
sc("""Now back to the gold. It was not the only precious thing in the car. Wikipedia says each F one came with a gold-plated Facom titanium tool kit and a first aid kit, both stored inside the car. A tool kit made of titanium and plated in gold, supplied with a road car.""",
   "McLaren F1 tool kit", "A GOLD-PLATED TITANIUM TOOL KIT")
sc("""And there was luggage. Wikipedia says the car came with tailored, proprietary luggage bags specially designed to fit its carpeted storage compartments. Gooding and Company says the compartments sat above the rear wheel arches, and that the fitted luggage set was standard with every road car.""",
   "McLaren F1 luggage compartment", "FITTED LUGGAGE, STANDARD")
sc("""So the F one was a car with a gold-lined engine bay, gold-plated tools and bespoke luggage. And yet it was also a car with no airbags, Wikipedia says. This was a machine built around weight, so every system that was not essential was left out, and every part that remained was made as light as possible.""",
   "McLaren F1 interior", "GOLD INSIDE, BUT NO AIRBAGS")
sc("""The same obsession shows in the seating. Wikipedia says the driver's seat is positioned in the middle of the car, ahead of the fuel tank and ahead of the engine. Gooding and Company says it was a three-seat layout, with the driver front and centre, flanked by two passengers set slightly behind.""",
   "McLaren F1 central seat", "DRIVER IN THE MIDDLE")
sc("""And here is a detail many fans miss. Gooding and Company says Ferrari's Tre Posti three-seat three sixty-five P Berlinetta Speciale from nineteen sixty-six had used a similar layout, but that car was essentially a coachbuilt special, not a production car the way the F one would be. The idea was not new. Making it a production car was.""",
   "Ferrari 365 P Berlinetta Speciale", "A 1966 FERRARI HAD DONE IT FIRST")
sc("""Wikipedia says Murray described his design concept as a common one among designers of high-performance cars: low weight and high power. He conceived the F one as an exercise in creating the ultimate road-going sports car. Low weight and high power. The gold foil was one small way of making that work.""",
   "Gordon Murray McLaren F1", "LOW WEIGHT, HIGH POWER")
sc("""The numbers show how far that went. Wikipedia lists the F one at eleven hundred forty kilograms dry, or two thousand five hundred thirteen pounds, and twelve hundred sixty kilograms ready to drive. The SlashGear website points out that is just over twenty-five hundred pounds, lighter than a new Toyota Corolla at over twenty-nine hundred.""",
   "McLaren F1 side profile", "1,140 KG DRY")
sc("""Now put the weight and the power together. Six hundred eighteen horsepower divided by eleven hundred forty kilograms is about point five four horsepower per kilogram, by our own arithmetic. That is the kind of ratio that, in the early nineteen nineties, almost nothing on the road could match.""",
   "McLaren F1 on road", "~0.54 HP PER KILOGRAM")
sc("""And there is one more story about this car's toughness, from the very beginning. Wikipedia reports that a test driver, wearing just shorts and a T-shirt, hit a rock and rolled the first prototype car several times. The car was built to a very high standard, and that incident showed what its carbon fiber body could take.""",
   "McLaren F1 prototype XP1", "THE PROTOTYPE THAT ROLLED")
sc("""Gooding and Company says the F one was the first road car with a full carbon fiber chassis, with titanium, magnesium and Kevlar used in other areas to provide strength without adding weight. So the same materials that make the car light also protect the people inside it.""",
   "carbon fiber monocoque", "FIRST ROAD CAR WITH A FULL CARBON CHASSIS")
sc("""Wikipedia lists the tires, too. Two hundred thirty-five forty-five seventeen at the front, and three hundred fifteen forty-five seventeen at the rear. A rear tire three hundred fifteen millimeters wide is about twelve point four inches, by our own arithmetic. Wide rubber for a car with six hundred eighteen horsepower.""",
   "McLaren F1 wheel", "315 MM REAR TIRES")
sc("""Murray also wanted carbon fiber brakes, Gooding and Company says, but the technology was still in its infancy. Here is the twist. The racing version, the GTR, did get carbon brakes, Wikipedia says. And Wikipedia's page on the nineteen ninety-five race says those lighter carbon brakes would not need changing through the entire race.""",
   "McLaren F1 GTR brakes", "CARBON BRAKES ARRIVED ON THE RACE CAR")
sc("""The design of the body came from Peter Stevens, Gooding and Company says. It describes the exterior as simpler and more elegant than most other supercars of its era, with a shape not only dictated by aerodynamics. The car looked calm, even though it was extreme underneath.""",
   "McLaren F1 design Peter Stevens", "A CALM SHAPE, AN EXTREME CAR")
sc("""That is thing number one. A car that spent gold on heat, and spent carbon fiber on weight, because every gram and every degree mattered. And that is exactly the reason it turned out to be better at racing than anybody expected, including the man who designed it.""",
   "McLaren F1 detail", "THING ONE: EVERY GRAM MATTERED")

# ---------- THING TWO ----------
ch("Thing two: the race car nobody wanted")
sc("""Now thing number two. Wikipedia's page on the F one GTR says Gordon Murray originally saw his creation as the ultimate road car, with no intention of racing it. Racing teams and private owners wanted a GT one car. And a Le Mans winner named John Nielsen turned to Murray, trying to convince him to offer factory backing.""",
   "McLaren F1 GTR", "MURRAY DID NOT WANT TO RACE IT")
sc("""Motor Sport magazine tells a slightly different version. It says Ron Dennis, the head of McLaren, had an F one road car on order himself and wanted to go racing with it. Dennis asked his friend, racer Ray Bellm, for one million pounds to fund a one-off racing version. Bellm declined, and Dennis suggested he find other investors.""",
   "Ron Dennis McLaren", "DENNIS ASKED FOR £1 MILLION")
sc("""Bellm went to Thomas Bscher, a German banker and historic racer, and brought in Lindsay Owen-Jones. Meanwhile, McLaren's composites department head, Jeff Hazell, had put together a proposal after a fact-finding trip to Le Mans in nineteen ninety-three. A more modest plan was approved after Hazell and Murray visited the May nineteen ninety-four Dijon round of what became the global endurance GT series.""",
   "Dijon-Prenois circuit", "A FACT-FINDING TRIP TO DIJON")
sc("""Eventually, Wikipedia says, Murray relented and agreed to modify the F one into a racing car. McLaren used an unused chassis, number nineteen, as a development prototype. The bodywork gained cooling ducts, a large central nose duct and a large adjustable rear wing.""",
   "McLaren F1 GTR prototype", "MURRAY RELENTED")
sc("""The page says even the nineteen ninety-five version generated enough downforce to run along the ceiling at one hundred miles per hour. The interior was stripped of luxuries and given a full racing cage. Carbon brakes replaced the stock units. But the central seat, butterfly doors and standard gearbox stayed.""",
   "McLaren F1 GTR interior cage", "DOWNFORCE TO DRIVE ON THE CEILING")
sc("""The money was modest. Motor Sport says the initial development budget was seven hundred fifty thousand pounds, and a production run of five cars at six hundred twenty-five thousand pounds each funded the program. Customers included the Fayed family of Harrods and gentleman racer Jean-Luc Maury-Laribière. By comparison, the road car had launched at five hundred forty thousand pounds, according to Top Gear.""",
   "Harrods McLaren F1 GTR", "5 CARS AT £625,000 EACH")
sc("""And the team did not expect to win. Motor Sport says Hazell recalled that not much was done to the car for nineteen ninety-five. The team removed the suspension and engine subframe rubber, added a cage, fitted a rear wing, and raced. The transmission from the road car was the weak link, and Hazell remembered many late nights working on the gearbox.""",
   "McLaren F1 GTR gearbox", "THE GEARBOX WAS THE WEAK LINK")
sc("""Hazell also described why racing looked possible. Motor Sport quotes him saying the team found a friendly series in which no one had really pushed the boat out in terms of preparation and development. So the team believed the car could be made competitive without much work. That belief was tested sooner than anyone expected.""",
   "BPR Global GT Series 1995", "A FRIENDLY SERIES")
sc("""And it was quick from the start. Wikipedia's page on the race car says the McLarens took the first three qualifying places at Jerez, and reached two hundred eighty-one kilometers per hour on the Mulsanne straight in practice at Le Mans. Wikipedia's Le Mans page says the cars won six of the seven races of the nineteen ninety-five BPR series up to that point.""",
   "Jerez circuit", "6 WINS IN 7 RACES BEFORE LE MANS")
sc("""Hazell said the team knew they could validate a car for four hours, but not twenty-four. So customers paid for a long-distance kit that included a contribution toward a twenty-four-hour test. Motor Sport says that test took place at Magny-Cours, and nine drivers completed it, expecting the car to break.""",
   "Magny-Cours circuit", "A 24-HOUR TEST WITH 9 DRIVERS")
sc("""Wikipedia's page on the nineteen ninety-five race says the F one GTRs were not expected to win. It says the lighter weight and better downforce of the prototypes were expected to prove superior. And it adds that in April's test, the cars were not on the pace of the Ferraris.""",
   "1995 24 Hours of Le Mans", "NOT EXPECTED TO WIN")
sc("""Then the weather decided. The page describes one of the wettest races in the event's history, with about seventeen hours of steady rain. Wikipedia says the extensive period of rain proved a bigger equalizer and took pressure off the delicate McLaren drivetrains.""",
   "Le Mans rain 1995", "17 HOURS OF RAIN")
sc("""Motor Sport says the best McLaren qualifying time, set by J J Lehto, was eleven seconds slower than the pole-winning WR-Peugeot, and eight and a half seconds behind the Courage-Porsche driven by Mario Andretti, Bob Wollek and Eric Hélary. On pure speed, the McLarens were not the fastest cars. But a McLaren led before the end of the first hour.""",
   "Courage Porsche Le Mans 1995", "ELEVEN SECONDS SLOWER IN QUALIFYING")
sc("""Motor Sport says John Nielsen led the West-liveried car at the top of each hour from seven in the evening, until clutch problems ended its run shortly before half distance. Wikipedia says Mass and Nielsen had the lead for over eight hours until a broken clutch stopped them at three in the morning. The race was a story of cars falling away.""",
   "Le Mans night 1995", "THE LEADERS KEPT BREAKING")
sc("""Later, the two Bells and Wallace fought with Lehto. Motor Sport says Derek Bell regained the lead over Lehto with about four hours left, after Lehto had been lapping about ten seconds faster than anyone else at one point. The page says Wallace praised Bell for stepping up his pace when he had a chance to win.""",
   "Derek Bell Andy Wallace", "BELL v LEHTO IN THE FINAL HOURS")
sc("""The race had drama on every lap. Motor Sport reports that Derek Bell inadvertently kinked the throttle cable while climbing into the Harrods car, costing two laps. His son Justin Bell came in after one hour when he was supposed to drive two, spooked by the night conditions. He said he had never been so frightened in his life.""",
   "Derek Bell Le Mans", "THE BELL FAMILY DRAMA")
sc("""Andy Wallace drove nearly fourteen hours in that Harrods car. Then the clutch bearing on the release slider failed. The team could not find a replacement, and could not fit a standard clutch. That left the car in direct drive, which caused problems with the gearbox. Wallace said he was using only fifth and sixth gears by the end.""",
   "Andy Wallace", "WALLACE DROVE NEARLY 14 HOURS")
sc("""Meanwhile, the Japanese-sponsored Kokusai Kaihatsu car, run by Lanzante, moved into the lead in the twenty-second hour. It survived a water pressure alarm that needed a quick stop after the final fuel stop. Lanzante said the strategy was simply to avoid the pits.""",
   "McLaren F1 GTR Kokusai Kaihatsu", "THE LEAD IN HOUR 22")
sc("""Wikipedia says the winners were J J Lehto, Yannick Dalmas and Masanori Sekiya. Dalmas brought the McLaren home to win by three-quarters of a lap. This was McLaren's first win at Le Mans, at its first attempt. The cars were untested over twenty-four hours, yet they led for all but thirteen laps.""",
   "Yannick Dalmas", "WON BY THREE-QUARTERS OF A LAP")
sc("""And the F one GTRs filled four of the first five places. Motor Sport says the Harrods car finished third, two laps behind. GTC Motorsport's best McLaren finished fourth after Ray Bellm crashed in the wet. The Giroix Racing Team car finished fifth after a new starter motor failed early on.""",
   "Le Mans 1995 podium", "4 OF THE FIRST 5 PLACES")
sc("""Wikipedia also gives a detail about one of the winning drivers. It says Masanori Sekiya had always been passionate about Le Mans, having got married in the town hall during the nineteen eighty-seven race week. Eight years later, he won the race.""",
   "Le Mans town hall", "HE MARRIED DURING LE MANS WEEK")
sc("""The win was not free of controversy. Motor Sport says the winning car was chassis zero zero one R, which had not raced in the global GT series, and was the car used in the Magny-Cours test. McLaren arranged for Lanzante's small team to run it, since McLaren could not run it from the factory.""",
   "McLaren F1 GTR 001R", "CHASSIS 001R")
sc("""Ray Bellm claimed a contract clause prevented McLaren from running a factory car against privateers. Motor Sport says no such clause existed, and that Bellm had to apologize to Ron Dennis. Lanzante said his squad was the smallest of the GTR teams, with only eight or nine people, and rejected the works allegation.""",
   "Lanzante Motorsport", "A SMALL TEAM, A BIG ARGUMENT")
sc("""Wikipedia's page on the F one says it was the last road-legal, series-produced sports car to win the twenty-four hours of Le Mans outright. The page says the GTR took first, third, fourth, fifth and thirteenth places in nineteen ninety-five.""",
   "McLaren F1 Le Mans trophy", "LAST ROAD-LEGAL CAR TO WIN LE MANS")
sc("""That is thing number two. A road car its creator never wanted to race, built by a team that did not expect to finish, ran in the rain for twenty-four hours and won. And those two things are linked. The same lightness and the same carbon structure that justified gold foil helped the car survive a race that wrecked cars built for it.""",
   "McLaren F1 GTR winner", "THING TWO: THE ACCIDENTAL CHAMPION")

# ---------- THE AFTERMATH ----------
ch("What happened next")
sc("""Wikipedia says that in total nine F one GTRs were built for the nineteen ninety-five season, nine more for nineteen ninety-six, and ten for nineteen ninety-seven. Twenty-eight race cars, plus the road cars and special versions. In all, only one hundred six cars were manufactured, the page says.""",
   "McLaren F1 GTR line up", "ONLY 106 CARS IN TOTAL")
sc("""On the road, the F one also set a record. Wikipedia says on the thirty-first of March, nineteen ninety-eight, Andy Wallace drove the five-year-old XP five prototype at Volkswagen's test track in Ehra-Lessien. The independently measured two-way average was two hundred forty point one miles per hour.""",
   "Ehra-Lessien test track", "240.1 MPH, MARCH 31, 1998")
sc("""The peak speed, the page says, was two hundred forty-three miles per hour, measured by McLaren, with the rev limiter raised to eight thousand three hundred r p m. And Gooding and Company notes the F one held the record for the world's fastest production car from nineteen ninety-eight to two thousand five.""",
   "McLaren F1 top speed run", "THE WORLD'S FASTEST CAR FOR 7 YEARS")
sc("""And the road car's price? Top Gear says the new price was five hundred forty thousand pounds, which the Bank of England put at a little over one point one million pounds in two thousand twenty money. Hagerty valued a normal F one at around sixteen million pounds in that article. Gooding and Company reported one sold in twenty twenty-one for twenty point four six five million dollars.""",
   "McLaren F1 auction", "£540,000 NEW. $20.5 MILLION SOLD")
sc("""Even the race car's value has soared. Wikipedia lists chassis ten R as sold in twenty twenty-six for a record thirty-four point six five five million dollars. For a car whose factory budget, according to Motor Sport, began with a development budget of seven hundred fifty thousand pounds.""",
   "McLaren F1 GTR 10R", "A GTR SOLD FOR $34.7 MILLION")
sc("""Both things are connected to one idea. When Murray made the F one, he did not follow a formula. He followed physics. He spent gold on heat and carbon on weight, he put the driver in the middle, and he used a naturally aspirated engine. And the result was a car that did things nobody planned.""",
   "Gordon Murray F1 design", "HE FOLLOWED PHYSICS, NOT A FORMULA")
sc("""The F one's creator himself later said that owning one became uncomfortable. Top Gear quoted Murray saying it became a little untenable to own. He used to drive his car on Sunday mornings, but once it was worth many millions, he was reluctant to risk damaging it.""",
   "Gordon Murray driving", "\"A LITTLE UNTENABLE TO OWN\"")

# ---------- THE ANSWER ----------
ch("Two things, one car")
sc("""So here are the two things again. First, the F one's engine bay was lined with about sixteen grams of gold, and the car came with a gold-plated titanium tool kit. Second, a road car that its designer never meant to race beat purpose-built prototypes at Le Mans, in the rain, on its first try.""",
   "McLaren F1", "THE TWO THINGS")
sc("""Which one surprised you more? Tell us in the comments. In the other videos of this series, we compare the McLaren F one with the new McLaren W one, we work out what it really costs to own an F one today, and we tell the story of the man who dreamed it up in an airport.""",
   "McLaren W1", "WHICH ONE SURPRISED YOU?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video81", "2 Things You Didn't Know About the McLaren F1", [
    "Wikipedia, McLaren F1: https://en.wikipedia.org/wiki/McLaren_F1",
    "Wikipedia, McLaren F1 GTR: https://en.wikipedia.org/wiki/McLaren_F1_GTR",
    "Wikipedia, 1995 24 Hours of Le Mans: https://en.wikipedia.org/wiki/1995_24_Hours_of_Le_Mans",
    "Motor Sport magazine, Won for the road: McLaren's unlikely 1995 Le Mans win (June 2005): https://www.motorsportmagazine.com/archive/article/june-2005/52/won-road/",
    "Gooding and Company coverage of F1 chassis 029, JustCars (Australia): https://www.justcars.com.au/news-and-reviews/feature-1995-mclaren-f1/924590",
    "Top Gear, McLaren F1s are now worth 16 million pounds: https://topgear.com.sg/features/mclaren-f1s-are-now-worth-ps16million",
    "SlashGear, Here's How Fast The McLaren F1 Really Is: https://www.slashgear.com/1105554/heres-how-fast-the-mclaren-f1-really-is",
], "A")
