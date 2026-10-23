import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Bugatti Chiron exists because of a toy in a souvenir shop, a sketch on an envelope, and a brand that had died more than once. The company behind it lost a founder's son in a crash, went bankrupt in Italy, and was bought for its name alone. This is the insane story behind the Bugatti Chiron.""",
   "Bugatti Chiron", "THE STORY BEHIND THE CHIRON")
sc("""It is a story with a Monaco racing driver, a Formula One champion buying a car without asking for a discount, a former Formula One driver breaking a record without a helmet, and a car that ended up being sold by a company Volkswagen no longer owns.""",
   "Bugatti Chiron Molsheim", "MONACO, F1, AND A TOY")
sc("""Every fact in this video comes from a published source, listed in the description. And to understand the Chiron, we have to go back more than one hundred years, to a small town in Alsace.""",
   "Molsheim", "EVERY FACT IS SOURCED")
sc("""Here is the first twist. When Bugatti was born, its home town was not in France. It was in Germany.""",
   "Molsheim Alsace", "IT WAS NOT IN FRANCE")

# ---------- 1. ETTORE ----------
ch("Ettore and Molsheim")
sc("""Ettore Bugatti was born in Milan, Italy. In nineteen oh nine he founded his car company in Molsheim, in Alsace, which at that time was part of the German Empire. After the First World War, Alsace became part of France, and Bugatti became one of the great names of French motoring.""",
   "Ettore Bugatti", "ETTORE BUGATTI, 1909")
sc("""Bugatti built cars that were light, beautiful, and fast. The Type thirty-five became one of the most successful racing cars of its era. Bugattis won the Targa Florio road race in Sicily every year from nineteen twenty-five to nineteen twenty-nine.""",
   "Bugatti Type 35", "THE TYPE 35")
sc("""One of the drivers who made those cars famous was Louis Chiron. He was born in Monte Carlo on the third of August, eighteen ninety-nine. He started racing in nineteen twenty-three in a second-hand Bugatti Brescia, and in nineteen twenty-eight he became a Bugatti factory driver.""",
   "Louis Chiron", "LOUIS CHIRON, MONACO")
sc("""Chiron won the Italian Grand Prix in nineteen twenty-eight, the German Grand Prix in nineteen twenty-nine, the Belgian Grand Prix in nineteen thirty, and in nineteen thirty-one he won both the French Grand Prix and his home race, the Monaco Grand Prix. Wikipedia notes that he had the most podium finishes of any driver in Bugattis.""",
   "Monaco Grand Prix 1931", "MONACO GP WINNER, 1931")
sc("""And here is a twist. Chiron raced for an incredibly long time. In nineteen fifty-five, at fifty-five years old, he started the Monaco Grand Prix and finished sixth. He is still the oldest driver to start a Formula One race. And he was the only driver from Monaco to win the Monaco Grand Prix until Charles Leclerc did it in twenty twenty-four.""",
   "Louis Chiron 1955", "OLDEST F1 STARTER: 55")
sc("""Today a statue of Louis Chiron stands at the Monaco circuit, and one corner is named after him. So when Bugatti picked his name for its new hypercar, it was choosing the driver who, more than anyone, connected Bugatti with winning.""",
   "Louis Chiron statue Monaco", "A CORNER IN HIS NAME")

# ---------- 2. THE TRAGEDY ----------
ch("Victory and tragedy")
sc("""In the late nineteen thirties, Ettore's son Jean Bugatti was the rising star of the company. He developed the chassis of the Type fifty-seven C, and a streamlined race version known as the Tank was built for Le Mans.""",
   "Bugatti Type 57", "JEAN BUGATTI")
sc("""On the eighteenth of June nineteen thirty-nine, a Type fifty-seven C Tank won the twenty-four hours of Le Mans. The drivers were Jean-Pierre Wimille and Pierre Veyron. According to Bugatti, they covered three thousand three hundred fifty-four kilometers at an average of about one hundred thirty-nine kilometers per hour, and the mechanics never had to open the hood.""",
   "Bugatti Type 57C Tank", "LE MANS WINNERS, 1939")
sc("""Yes, that Veyron. Pierre Veyron, the co-winner of that race, is the man the Bugatti Veyron was named after, decades later. The two hypercars of the modern Bugatti era carry the names of two of its racing drivers.""",
   "Pierre Veyron", "THE REAL VEYRON")
sc("""But less than two months after that victory, the story turned dark. On the eleventh of August nineteen thirty-nine, Jean Bugatti died while testing a Type fifty-seven tank-bodied race car near the Molsheim factory. He was the heir to the company.""",
   "Bugatti Molsheim factory", "AUGUST 11, 1939")
sc("""Weeks later, the Second World War began. The war left the Molsheim factory in ruins, and the company lost control of the property. Ettore Bugatti died on the twenty-first of August, nineteen forty-seven. The golden age of Bugatti was over.""",
   "Molsheim ruins", "WAR AND RUIN")
sc("""In nineteen sixty-three, what remained of the company was sold to Hispano-Suiza, mainly for its aircraft parts business. For years, the name Bugatti meant old masterpieces in museums and auctions, not new cars.""",
   "Bugatti Royale", "A NAME IN MUSEUMS")

# ---------- 3. THE ITALIAN REVIVAL ----------
ch("The Italian revival")
sc("""Then came the first revival. In nineteen eighty-seven, Italian entrepreneur Romano Artioli acquired the Bugatti brand and founded Bugatti Automobili S p A. He built a new factory in Campogalliano, in Italy, on a large site near Ferrari, Maserati, and Lamborghini. People called it the Blue Factory.""",
   "Bugatti Campogalliano factory", "THE BLUE FACTORY")
sc("""The result was the E B one ten, presented in Paris on the fifteenth of September nineteen ninety-one, the day Ettore Bugatti would have turned one hundred ten. It had a three point five liter V12 with four turbochargers, all-wheel drive, and, according to Bugatti, the first series-production carbon chassis. Top speed was over three hundred fifty-one kilometers per hour.""",
   "Bugatti EB110", "EB110, 1991")
sc("""The Blue Factory itself was a statement. Bugatti says it stood on a site of about two hundred forty thousand square meters, and it was designed by Artioli's cousin, Giampaolo Benedini, who also reworked the first design of the E B one ten. It was meant to be the most modern supercar plant of its time, and it sat in the heart of Italy's supercar valley.""",
   "Bugatti Campogalliano", "240,000 SQUARE METERS")
sc("""Artioli also had bigger plans. Bugatti was developing the E B one twelve, a super saloon with a six liter V12 and a carbon chassis. It was almost finished, but it never launched. If the company had survived, Bugatti might have become a maker of fast luxury sedans, not hypercars.""",
   "Bugatti EB112", "THE EB112 THAT NEVER LAUNCHED")
sc("""And here is a great detail. After testing the E B one ten against rivals, Formula One champion Michael Schumacher bought a yellow Super Sport. According to Bugatti, he did it without even asking for a discount.""",
   "Bugatti EB110 Super Sport", "SCHUMACHER'S BUGATTI")
sc("""But the business did not survive. Artioli also invested in Lotus, which added to the company's debts. Only about one hundred twenty-eight E B one tens were built. Bugatti Automobili filed for bankruptcy on the twenty-third of September nineteen ninety-five. Bugatti says Artioli paid his two hundred twenty employees until the last day.""",
   "Bugatti EB110 GT", "BANKRUPT, 1995")
sc("""Twist number two. The Bugatti brand had now died twice. Once after the war, and once in Italy. When Volkswagen came looking, there was no factory to buy and no product line. There was only a name.""",
   "Bugatti logo", "THE BRAND DIED TWICE")

# ---------- 4. PIECH ----------
ch("A toy and a sketch")
sc("""This is where Ferdinand Piech enters the story. He was the engineer who ran the Volkswagen Group, and the grandson of Ferdinand Porsche. According to Top Gear, his son Gregor saw a toy Bugatti Type fifty-seven S C Atlantic in a souvenir shop in Majorca. Piech bought two, one for his son, and one for the Volkswagen executive board.""",
   "Ferdinand Piech", "A TOY IN MAJORCA")
sc("""Around a year before Volkswagen bought Bugatti, Piech sketched an eighteen-cylinder engine on an envelope while riding a Japanese express train. In nineteen ninety-eight, Volkswagen bought the Bugatti name for an estimated fifty million dollars. It got only the trademark.""",
   "Bugatti Type 57 SC Atlantic", "A SKETCH ON A TRAIN")
sc("""Bugatti then showed a series of concept cars, all powered by a six point two five liter W18 engine with about five hundred fifty-five horsepower. The E B one eighteen, the E B two eighteen, and at the Frankfurt Motor Show in nineteen ninety-nine, a car called the eighteen slash three Chiron.""",
   "Bugatti 18/3 Chiron", "THE FIRST CHIRON, 1999")
sc("""So the name Chiron was used for a Bugatti concept seventeen years before the production Chiron arrived. Then came the E B eighteen slash four Veyron at the Tokyo show, almost identical to the car that would reach production. At Geneva in two thousand, Piech promised more than one thousand horsepower and more than four hundred kilometers per hour.""",
   "Bugatti EB 18/4 Veyron", "THE PROMISE: 1,000 HP, 400 KM/H")

# ---------- 5. THE VEYRON ----------
ch("The Veyron problem")
sc("""The engine lost two cylinders and became the quad-turbo eight-liter W16. Top Gear wrote that the engine was not even the hardest part. The gearbox, the tires, and the aerodynamics were harder. Development took years and enormous sums of money.""",
   "Bugatti Veyron engine", "THE W16 IS BORN")
sc("""Assembly of the Veyron began in September twenty oh five, in a new Molsheim factory. Bugatti was back home in Alsace. The car had one thousand one metric horsepower, and in twenty ten a Veyron sixteen point four Super Sport reached four hundred thirty-one kilometers per hour.""",
   "Bugatti Veyron Molsheim", "BACK IN MOLSHEIM, 2005")
sc("""But in twenty thirteen, evo reported an estimate from analysts at Sanford C. Bernstein. Volkswagen had lost about three point nine million pounds on every Veyron sold, and about one point four three billion pounds in total. The last Veyron was sold in February twenty fifteen.""",
   "Bugatti Veyron Grand Sport", "£3.9 MILLION LOST PER CAR")
sc("""So the Chiron's mission was impossible on paper. It had to be faster than a car that had already broken records. It had to be more powerful, more usable, and more profitable. And it had to keep the same basic engine idea, because the W16 was now the heart of the brand.""",
   "Bugatti Veyron Super Sport", "AN IMPOSSIBLE BRIEF")

# ---------- 6. THE CHIRON ARRIVES ----------
ch("The Chiron arrives")
sc("""The answer was revealed on the first of March twenty sixteen at the Geneva Motor Show. It was previewed by the Bugatti Vision Gran Turismo concept, a car first created for a video game, shown at Frankfurt in twenty fifteen. The design team was led by Achim Anscheidt.""",
   "Bugatti Vision Gran Turismo", "PREVIEWED BY A VIDEO GAME CAR")
sc("""The Chiron kept the eight-liter W16 and its four turbochargers, but Motor Authority reported that almost every part was redesigned. Output rose to fifteen hundred metric horsepower, or one thousand four hundred seventy-nine horsepower, with one thousand six hundred newton meters of torque.""",
   "Bugatti Chiron engine", "1,500 PS")
sc("""The design was a team effort. Wikipedia credits Achim Anscheidt as head of design, with Frank Heyl, Sasha Selipanov, and Etienne Salome. The most famous design element is the C-shaped line on the side, a curve that runs from the roof down around the door. It became the signature of the car, the line people recognize from across a parking lot.""",
   "Bugatti Chiron side", "THE C-LINE")
sc("""Underneath, the engineers were fighting heat. Motor Authority reported that the engine generates more than three thousand horsepower worth of heat, so the Chiron has ten radiators, a water pump moving about eight hundred liters per minute, and more than sixty thousand liters of air flowing through the engine every minute at full power. Making the power was hard. Surviving it was harder.""",
   "Bugatti Chiron rear diffuser", "10 RADIATORS")
sc("""The Chiron also introduced a detail owners love. In normal driving, the car is limited to about three hundred eighty kilometers per hour. To unlock its full limit of four hundred twenty, the driver needs a special speed key. Even a car this powerful came with a lock on its top speed, mainly because of the limits of road tires.""",
   "Bugatti Chiron interior", "THE SPEED KEY")
sc("""The price was two point four million euros, with a two hundred thousand euro deposit. And the plan was to build five hundred cars. The first three were delivered in March twenty seventeen, and by then the first two hundred were already sold.""",
   "Bugatti Chiron Geneva 2016", "€2.4 MILLION, 500 CARS")
sc("""Here is the twist. The car named after a Monaco racing hero was never built to win races. It was built to be the fastest, most luxurious way to cross a continent. Bugatti's racing past gave the name. Its future was speed and luxury.""",
   "Bugatti Chiron road", "A RACING NAME, A ROAD CAR")

# ---------- 7. THE RECORD YEARS ----------
ch("The record years")
sc("""In August twenty seventeen, Bugatti put Juan Pablo Montoya in a Chiron. Montoya had won the Monaco Grand Prix in Formula One and the Indianapolis five hundred twice. The test was zero to four hundred kilometers per hour and back to zero. He did it in forty-one point nine six seconds, without a helmet or racing suit, according to Bugatti.""",
   "Juan Pablo Montoya", "MONTOYA, 41.96 SECONDS")
sc("""Bugatti's own press release adds more detail. Montoya reached four hundred twenty kilometers per hour that weekend and went past four hundred kilometers per hour seventeen times. His previous personal best had been four hundred seven kilometers per hour, in an IndyCar. The run was certified by S G S T U V Saar, and Bugatti president Wolfgang Durheimer said three hundred of the five hundred Chirons had already been sold.""",
   "Bugatti Chiron 0-400-0", "17 TIMES OVER 400 KM/H")
sc("""The car itself showed off a new trick. Under braking from four hundred kilometers per hour, the rear wing stood up to forty-nine degrees as an air brake, less than a second after Montoya hit the pedal. Bugatti said it added about nine hundred kilograms of downforce at the rear and helped the car slow at about two g. The Chiron was proving it could stop as hard as it could go.""",
   "Bugatti Chiron rear wing", "THE WING BECOMES A BRAKE")
sc("""But a small Swedish company answered within weeks. Koenigsegg's Agera RS beat the Chiron's time by more than five seconds, and in November twenty seventeen it averaged two hundred seventy-seven point nine miles per hour on a closed highway in Nevada. Bugatti now had a rival that took records personally.""",
   "Koenigsegg Agera RS", "KOENIGSEGG STRIKES BACK")
sc("""Bugatti answered on the second of August twenty nineteen. At Ehra-Lessien in Germany, Andy Wallace drove a pre-production Chiron Super Sport three hundred plus to three hundred four point seven seven three miles per hour. It was the first time a near-production car broke three hundred miles per hour.""",
   "Ehra-Lessien", "304.773 MPH")
sc("""And then came the twist nobody expected. Bugatti president Stephan Winkelmann said the goal had been to be the first to reach three hundred miles per hour, and that Bugatti would now focus on other areas. The company that had defined the top speed war walked away from it, at the very top.""",
   "Bugatti Chiron Super Sport 300+", "BUGATTI WALKS AWAY")

# ---------- 8. THE ONE-OFFS ----------
ch("The one-offs")
sc("""What came next was a new kind of Bugatti business. Instead of chasing speed, the company built rarer and rarer versions. Thirty Super Sport three hundred plus cars at three point five million euros. Sixty Pur Sports for handling. Twenty Chiron Noire cars as a tribute to the nineteen thirty-six Type fifty-seven S C.""",
   "Bugatti Chiron Pur Sport", "RARER AND RARER")
sc("""Then the one-offs. La Voiture Noire, unveiled in twenty nineteen, was inspired by the lost Type fifty-seven S C Atlantic that belonged to Jean Bugatti, and Wikipedia says it was sold for about nine and a half million pounds. Then the Chiron Profilee, which sold at RM Sotheby's in February twenty twenty-three for nine million seven hundred ninety-two thousand five hundred euros.""",
   "Bugatti La Voiture Noire", "LA VOITURE NOIRE")
sc("""Hagerty reported that the Profilee became the most valuable new car ever sold at auction. Think about the circle here. A Type fifty-seven toy inspired Piech to revive Bugatti. Decades later, a tribute to the Type fifty-seven became one of the most expensive new cars in the world.""",
   "Bugatti Chiron Profilee", "THE CIRCLE CLOSES")

# ---------- 9. THE END ----------
ch("The end of the W16")
sc("""Before the end, there was one more symbol. In twenty eighteen, Lego and Bugatti built a full-size, drivable Chiron from more than one million Lego Technic pieces, powered by two thousand three hundred four small electric motors. It made an estimated five point four horsepower and reached about twenty kilometers per hour. A brand that started with a toy in a shop had become a toy itself.""",
   "Lego Bugatti Chiron", "A TOY AGAIN")
sc("""Bugatti sold out the Chiron by January twenty twenty-two. By then, it had also used the Chiron's foundations for other cars, like the Divo, built for corners, and the Centodieci, a tribute to the E B one ten from the Italian era. So even the bankrupt chapter of Bugatti's history was brought back, on top of a Volkswagen-era Chiron.""",
   "Bugatti Centodieci", "A TRIBUTE TO THE EB110")
sc("""The last base-spec Chiron was built in September twenty twenty-three. In January twenty twenty-four, Motor1 reported the delivery of the last fifteen hundred metric horsepower Chiron to a Canadian buyer. And in May twenty twenty-four, the five hundredth and final Chiron left Molsheim.""",
   "Bugatti Chiron Molsheim factory", "THE LAST CHIRONS")
sc("""It was a Super Sport called L'Ultime. Top Gear reported that its two-tone blue paint recalls the first Chiron of twenty sixteen, and its sides list places from the car's story. Geneva, Paul Ricard, Ehra-Lessien, Molsheim. The number five hundred is engraved on the engine cover.""",
   "Bugatti Chiron Super Sport blue", "L'ULTIME: No. 500")
sc("""Two of the places on that livery tell a story of their own. Chateau Saint Jean and Cape Canaveral are listed by Top Gear as the sites of customer top speed runs. In other words, owners took their Chirons to private roads and to a former space launch area to reach the limit. Bugatti put those places on its last car as part of the Chiron's history.""",
   "Cape Canaveral", "CAPE CANAVERAL")
sc("""The W16 did not disappear at once. It lived on in the Bolide track car and the open Mistral. But the Chiron was the last main Bugatti built around it. One engine idea, born on an envelope on a train, powered the brand for almost two decades.""",
   "Bugatti Mistral", "THE W16'S LAST CHAPTER")

# ---------- 10. A NEW OWNER ----------
ch("A new owner")
sc("""Meanwhile, the company changed hands again. In twenty twenty-one, Volkswagen moved Bugatti into a joint venture with Rimac, the Croatian electric hypercar maker founded by Mate Rimac. Rimac held fifty-five percent, and Porsche forty-five.""",
   "Mate Rimac", "BUGATTI RIMAC, 2021")
sc("""In June twenty twenty-four, the new company revealed the Chiron's successor, the Tourbillon. It uses a naturally aspirated eight point three liter V16 developed with Cosworth, plus three electric motors, for about one thousand seven hundred seventy-five horsepower. Its price is about three point eight million euros before taxes.""",
   "Bugatti Tourbillon", "THE TOURBILLON")
sc("""And then, in September twenty twenty-six, Carscoops reported that a group of investors had bought Porsche's stakes in both Rimac and Bugatti Rimac. Volkswagen and Porsche now own nothing of Bugatti. Mate Rimac became Bugatti's president, and Porsche earned about one billion euros from the deal.""",
   "Bugatti Tourbillon rear", "VW IS OUT, 2026")
sc("""Here is the final twist. Volkswagen bought Bugatti in nineteen ninety-eight for just the name, and turned it into the most famous hypercar brand in the world. Twenty-eight years later, it walked away completely. The Chiron was the peak of that era, the car that made the Volkswagen-era Bugatti a real business.""",
   "Bugatti Chiron front", "THE PEAK OF AN ERA")

# ---------- CLOSE ----------
ch("Why the story matters")
sc("""So the story behind the Chiron is not only about horsepower. It is about a brand that died twice and came back three times. From Ettore in Molsheim, to Artioli in Italy, to Piech and his toy car, and now to Mate Rimac.""",
   "Bugatti Chiron dark", "DIED TWICE, BACK THREE TIMES")
sc("""And it is about names. The Veyron carries the name of a Le Mans winner. The Chiron carries the name of the oldest man to start a Formula One race, a Monaco hero who won in Bugattis. Every modern Bugatti is a reminder of the brand's racing past, even if it no longer races.""",
   "Louis Chiron", "NAMED AFTER RACERS")
sc("""Tell us in the comments which part of this story surprised you most. And watch the other videos in this Chiron series, two facts most people don't know, how it compares with the Koenigsegg Jesko, and what it really costs to own one.""",
   "Bugatti Chiron rear view", "WHICH PART SURPRISED YOU?")
sc("""If you are shopping for something more practical than a Bugatti, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the machines people really talk about.""",
   "Bugatti Chiron sunset", "SUBSCRIBE: PICKUP REALITY")

save("video64", "The Insane Story Behind the Bugatti Chiron", [
    "Wikipedia, Bugatti (company history): https://en.wikipedia.org/wiki/Bugatti",
    "Wikipedia, Louis Chiron: https://en.wikipedia.org/wiki/Louis_Chiron",
    "Bugatti newsroom, 80 years ago Bugatti wins Le Mans: https://newsroom.bugatti.com/press-releases/80-years-ago-bugatti-wins-24-hours-of-le-mans",
    "Bugatti newsroom, Romano Artioli, the man who breathed life into Bugatti: https://newsroom.bugatti.com/press-releases/romano-artioli-the-man-who-breathed-life-into-bugatti",
    "Top Gear, how the Bugatti Veyron became a thing: https://www.topgear.com/car-news/supercars/heres-how-bugatti-veyron-became-thing",
    "evo, true cost of the Veyron revealed (Oct 2013): https://evo.co.uk/news/evonews/290953/true_cost_of_the_veyron_revealed.html",
    "Wikipedia, Bugatti Chiron: https://en.wikipedia.org/wiki/Bugatti_Chiron",
    "Motor Authority, Chiron W16 engine: https://www.motorauthority.com/news/1102657_a-close-look-at-the-bugatti-chiron-s-monster-w-16-engine",
    "Bugatti newsroom, 0-400-0 km/h in 42 seconds: https://newsroom.bugatti.com/press-releases/0-400-0-km-h-in-42-seconds-bugatti-chiron-sets-world-record",
    "Top Gear, Koenigsegg Agera RS record (Nov 2017): https://www.topgear.com/car-news/supercars/koenigsegg-has-smashed-worlds-fastest-car-record",
    "Autocar, Chiron goes 304mph: https://www.autocar.co.uk/car-news/new-cars/bugatti-chiron-goes-304mph-set-hypercar-record",
    "Motor1, Bugatti retires from speed records: https://www.motor1.com/news/368539/bugatti-retires-chasing-speed-records/",
    "Hagerty UK, Chiron Profilee auction: https://www.hagerty.co.uk/articles/bugatti-chiron-profilee-record-breaking/",
    "Motor1, last 1,500-hp Chiron delivered (Jan 2024): https://www.motor1.com/news/704067/last-chiron-1500-delivered/",
    "Top Gear, the 500th and final Chiron (May 2024): https://www.topgear.com/car-news/first-look/it-final-500th-definitely-last-ever-bugatti-chiron",
    "Motor1, Rimac and Bugatti (55/45): https://www.motor1.com/news/755654/rimac-complete-control-bugatti/",
    "Car Throttle, Bugatti Tourbillon: https://www.carthrottle.com/news/bugatti-tourbillon-1775bhp-v16-salute-combustion",
    "Carscoops, Rimac finalizes Bugatti takeover (Sept 2026): https://carscoops.com/2026/09/rimac-finalizes-bugatti-takeover-ending-all-vw-ownership",
], "D")
