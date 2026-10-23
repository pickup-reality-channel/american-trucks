import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""A Bugatti Chiron started at two point four million euros. That is the number everyone knows. But the price on the order form was only the entry ticket. One owner's normal annual service was about eleven thousand five hundred dollars. A single taillight was quoted at more than ten thousand dollars. And a replacement engine was listed at about eight hundred fifty-six thousand dollars. So what does a Chiron really cost to own?""",
   "Bugatti Chiron", "WHAT A CHIRON REALLY COSTS")
sc("""Today we follow the money from the first deposit to the day you sell. The buying, the options, the insurance, the service, the parts that wear, the fuel, and the surprise at the end, because for many owners, the Chiron did something almost no car does. It made money.""",
   "Bugatti Chiron rear", "FROM DEPOSIT TO RESALE")
sc("""Every figure in this video comes from a published source, and the full list is in the description. Some numbers come from owners, some from insurers, and some from estimates. We will tell you which is which, because with a car like this, the difference matters.""",
   "Bugatti Chiron Sport", "WE SAY WHERE EVERY NUMBER COMES FROM")
sc("""And here is the first twist. To buy a Chiron, money was not enough. You had to be fast. The first two hundred cars were sold before the first car was even delivered.""",
   "Bugatti Chiron Geneva", "MONEY WAS NOT ENOUGH")

# ---------- 1. GETTING ONE ----------
ch("Getting one")
sc("""The Chiron was revealed at the Geneva Motor Show on the first of March twenty sixteen. According to Wikipedia, the base price was two point four million euros, and buyers had to place a deposit of two hundred thousand euros just to reserve a build slot.""",
   "Bugatti Chiron Geneva 2016", "€200,000 DEPOSIT")
sc("""Two hundred thousand euros is the price of a nice house in many places, and it only bought a place in line. The first three customer cars were delivered in March twenty seventeen, a year after the reveal, and by then the first two hundred cars had already been sold.""",
   "Bugatti Chiron delivery", "200 CARS SOLD BEFORE DELIVERY")
sc("""In the United States, the price was higher once you added options and import costs. When the first Chiron ordered for America was sold at RM Sotheby's in December twenty seventeen, duPont Registry reported that it went for about six hundred thousand dollars over its sticker price. That implies a sticker of roughly three point one seven million dollars.""",
   "Bugatti Chiron American", "ABOUT $3.17 MILLION IN THE US")
sc("""And that was a base car with options. Special versions cost much more. The Chiron Sport added about four hundred thousand dollars. The Chiron Noire started at about three point three million dollars. And the Super Sport three hundred plus was announced at three point five million euros before tax.""",
   "Bugatti Chiron Sport 110 ans", "SPECIALS COST MORE")
sc("""Then there is Sur Mesure, Bugatti's personalization program. A customer can choose custom paint, special leather, and unique details. The last fifteen hundred metric horsepower Chiron was a base car customized through that program. Motor1 reported that it cost upwards of three million dollars, based on a price its owner shared online.""",
   "Bugatti Chiron custom", "PERSONALIZATION ADDS MORE")
sc("""And here is the twist. For a Chiron, options are not small. A paint job, a carbon finish, or a special interior can cost as much as a whole normal car. So two cars that look almost the same can have very different prices. The base price tells you very little about what a specific Chiron cost.""",
   "Bugatti Chiron carbon", "OPTIONS COST LIKE CARS")

# ---------- 2. INSURANCE ----------
ch("Insurance")
sc("""Now, insurance. In twenty nineteen, Motor1 cited a ValuePenguin estimate for a Chiron Sport one hundred ten Ans, a special edition with an asking price of about three point two six million dollars. The estimated insurance cost was about fifty thousand two hundred fifty-one dollars per year, or roughly four thousand one hundred eighty-eight dollars a month.""",
   "Bugatti Chiron Sport 110 ans blue", "$50,251 A YEAR TO INSURE")
sc("""A newer estimate from MoneyGeek, updated in April twenty twenty-six, put full coverage for a twenty twenty-five Chiron at about three thousand fifty-six dollars a month, for a forty-year-old driver with a clean record. If you multiply that by twelve, it is about thirty-six thousand seven hundred dollars a year. That multiplication is ours, not MoneyGeek's.""",
   "Bugatti Chiron road", "ABOUT $3,056 A MONTH")
sc("""But here is the twist. MoneyGeek's model assumes twelve thousand miles a year, and the site itself says that does not reflect typical Bugatti owners, many of whom drive less than one thousand miles a year. Owners of cars like this often use specialty collector insurers, and the price can change a lot depending on how the car is used and stored.""",
   "Bugatti Chiron garage", "MOST OWNERS BARELY DRIVE IT")
sc("""So the honest answer is that insurance for a Chiron is somewhere in the tens of thousands of dollars a year, depending on the car, the driver, and the policy. That is more than many Americans earn in a year, just to protect a car that sits in a garage most of the time.""",
   "Bugatti Chiron parked", "TENS OF THOUSANDS A YEAR")

# ---------- 3. SERVICE ----------
ch("Service")
sc("""Now, service. The clearest numbers come from collector Steve Hamilton, who shared his Chiron costs on video. The Drive summarized them in January twenty twenty-three. The normal annual service was about eleven thousand five hundred dollars.""",
   "Bugatti Chiron service", "ANNUAL SERVICE: $11,500")
sc("""Every four years there is a major service, which Hamilton put at about thirty-four thousand dollars. In his case it was covered by the factory warranty. Then there is an extended warranty. The Drive listed an additional four-year bumper-to-bumper warranty at about two hundred four thousand dollars.""",
   "Bugatti Chiron engine cover", "4-YEAR SERVICE: $34,000")
sc("""The Drive also did a calculation. Six years of maintenance after the first warranty, which means five annual services and one major service, adds up to about ninety-one thousand five hundred dollars. And that is just maintenance, before anything breaks.""",
   "Bugatti Chiron workshop", "6 YEARS: ~$91,500")
sc("""Why so much? Part of it is the engine. The Veyron, which used an earlier version of the same W16 design, was famous for its oil changes. In a twenty twenty video covered by The Drive, the owner of Royalty Exotic Cars in Las Vegas explained that a Veyron's dry-sump system has sixteen drain plugs.""",
   "Bugatti Veyron", "16 DRAIN PLUGS")
sc("""To reach them, the tires, the rear fender liners, and the rear deck have to come off. The shop estimated the job at more than twenty thousand dollars for that Veyron. A widely shared estimate from Singapore also listed sixteen drain plugs for a Chiron first service, at almost twenty-five thousand dollars, but that one was converted through two currencies and should be read as a rough guide.""",
   "Bugatti Veyron rear", "AN OIL CHANGE OVER $20,000")
sc("""Here is the twist. Bugatti owners do not just pay for parts. They pay for a team. Only a small number of specialist technicians in the world are trained to work on these cars, and jobs that take minutes on a normal car can mean removing large parts of the body. You are paying for time and for rare expertise.""",
   "Bugatti technician", "YOU PAY FOR THE EXPERTS")

# ---------- 4. PARTS THAT WEAR ----------
ch("Parts that wear")
sc("""Now the parts that wear out. Start with brakes. The Drive listed the Chiron's front carbon ceramic rotors at more than eighteen thousand dollars, with the rear rotors at a similar price. Front brake pads were about six thousand seven hundred dollars, and rear pads about four thousand.""",
   "Bugatti Chiron brakes", "FRONT ROTORS: $18,000+")
sc("""Those brakes are not ordinary. According to Bugatti, the discs are four hundred twenty millimeters at the front and four hundred at the rear, with eight titanium pistons per front caliper and six at the rear. They were designed to stop the car from four hundred kilometers per hour in about nine seconds. You are paying for that capability every time you replace them.""",
   "Bugatti Chiron brake caliper", "8 TITANIUM PISTONS")
sc("""Then there are tires. This is where the Chiron improved on the Veyron. Motor1 reported that a Veyron tire set cost around thirty thousand to forty-two thousand dollars, and the Veyron's tires had to be replaced about every two thousand five hundred miles. A Bugatti engineer said the Chiron's tires are much cheaper, use standard mounting, and can be changed almost anywhere.""",
   "Bugatti Chiron tire", "TIRES: CHEAPER THAN THE VEYRON")
sc("""The same engineer said the Chiron's rim is now a lifetime part. That is important, because on the Veyron the wheels were part of the expensive replacement cycle. But the Singapore estimate we mentioned listed Chiron tire sets from about eight thousand dollars for comfort tires to about forty-two thousand for track tires. So the tire bill depends on how you use the car.""",
   "Bugatti Chiron wheel", "FROM $8,000 TO $42,000")
sc("""And then the scary list. The Drive reported a replacement engine for the quad-turbo W16 at about eight hundred fifty-six thousand dollars. A dual-clutch gearbox at about one hundred eighty-five thousand. And a single taillight at more than ten thousand dollars. A small parking mistake can cost more than a new pickup truck.""",
   "Bugatti Chiron taillight", "$856,000 ENGINE, $185,000 GEARBOX")
sc("""Here is the twist. Most of those big numbers are rare events. Engines and gearboxes rarely need full replacement, and warranty covers much of the early risk. The costs that every owner really pays are the service, the insurance, and the wear items. The scary list is the reason the warranty costs two hundred thousand dollars.""",
   "Bugatti Chiron front", "THE WARRANTY EXISTS FOR A REASON")

# ---------- 5. FUEL ----------
ch("Fuel")
sc("""Now fuel. The official mixed consumption for the Chiron is twenty-two point five liters per one hundred kilometers, which is about ten and a half miles per gallon. That is the calm, mixed-driving number. At full power, consumption is in a different universe.""",
   "Bugatti Chiron fuel", "~10.5 MPG MIXED")
sc("""Motor Authority wrote that the Veyron could empty its tank in about twelve minutes at full throttle, and expected the Chiron to drink even faster. The engine moves more than sixty thousand liters of air per minute and uses thirty-two fuel injectors. At top speed, a Chiron burns fuel faster than almost any road car ever sold.""",
   "Bugatti Chiron engine", "32 INJECTORS")
sc("""But here is the twist. For a Chiron owner, fuel is one of the smallest costs. Let's do a simple example. If an owner drives one thousand miles a year at ten and a half miles per gallon, that is about ninety-five gallons. Even at five dollars a gallon, that is under five hundred dollars a year, less than a single brake pad.""",
   "Bugatti Chiron gas station", "FUEL IS THE CHEAP PART")
sc("""That example is ours, with a simple assumption, but it shows the strange math of hypercar ownership. The more expensive the car, the less the fuel matters. What matters is time. Every year a car like this exists, it needs service, insurance, and storage, whether it moves or not.""",
   "Bugatti Chiron garage storage", "TIME COSTS MORE THAN MILES")

# ---------- 6. STORAGE AND LIVING ----------
ch("Storage and living with it")
sc("""Storage is part of the cost. Most owners keep these cars in climate-controlled garages, with battery tenders and car covers. The Singapore estimate even listed a yearly upkeep figure for a car that is not driven at all, of about one hundred five thousand dollars per fourteen months, though again it was a rough conversion.""",
   "Bugatti Chiron covered", "COSTS EVEN WHEN IT SITS")
sc("""Then there is transport. Many owners move their cars on enclosed trucks to events, tracks, and service centers, instead of driving them. And there is care. The Singapore estimate said the manufacturer advises against jet washing, and listed a full repaint at about fifty-five thousand dollars.""",
   "enclosed car transporter", "NO JET WASH")
sc("""Here is the twist. Some of these costs exist because owners are protecting value. A Chiron with low mileage, perfect paint, and a full service history is worth more when sold. So many owners treat the car less like transportation and more like an investment that they also get to drive sometimes.""",
   "Bugatti Chiron low mileage", "TREATED LIKE AN INVESTMENT")

# ---------- 7. RESALE ----------
ch("The resale surprise")
sc("""And that brings us to the biggest surprise. Most cars lose value the moment they leave the dealer. The Chiron often did the opposite. In November twenty seventeen, evo reported that a used Chiron with about one thousand three hundred thirty miles was being offered for three point six million pounds, against an original price of about two point five million pounds.""",
   "Bugatti Chiron blue", "USED FOR MORE THAN NEW")
sc("""The next month, in December twenty seventeen, the first Chiron ordered for the United States sold at RM Sotheby's for three million seven hundred seventy-two thousand five hundred dollars. It had only about two hundred fifty test miles and had never been registered for the road. duPont Registry reported that the price was about six hundred thousand dollars over its sticker.""",
   "RM Sotheby's auction", "$3,772,500 AT AUCTION")
sc("""Then came the most extreme case. The Chiron Profilee, a one-off car, sold at RM Sotheby's in Paris in February twenty twenty-three for nine million seven hundred ninety-two thousand five hundred euros. Hagerty reported it was the most valuable new car ever sold at auction, beating the previous record held by a Ferrari LaFerrari Aperta.""",
   "Bugatti Chiron Profilee", "€9.79 MILLION: AUCTION RECORD")
sc("""Why did prices rise? Because supply was fixed. Bugatti built five hundred Chirons and stopped. The last base-spec Chiron was built in September twenty twenty-three, and the five hundredth and final Chiron, the Super Sport L'Ultime, left Molsheim in May twenty twenty-four. The W16 is now gone from new Bugattis.""",
   "Bugatti Chiron L'Ultime", "ONLY 500, AND NO MORE")
sc("""And the successor costs more. The Bugatti Tourbillon, revealed in June twenty twenty-four, is priced at about three point eight million euros before taxes, with first deliveries expected in twenty twenty-six. When the new car costs more than the old one, the old one tends to look like a better deal on the used market.""",
   "Bugatti Tourbillon", "THE SUCCESSOR COSTS €3.8 MILLION")
sc("""But here is the twist. Resale gains are not guaranteed. The cars that rose the most were early, low-mileage, or one-off cars. A Chiron that has been driven, damaged, or poorly serviced can be a very different story. And every year of service, insurance, and storage eats into any gain.""",
   "Bugatti Chiron dark", "GAINS ARE NOT GUARANTEED")

# ---------- 7b. WHAT IT COST BUGATTI ----------
ch("What it cost Bugatti")
sc("""Now flip the question around. What did these cars cost the company that built them? With the Veyron, the answer was shocking. In October twenty thirteen, evo reported an estimate from analysts at Sanford C. Bernstein. They calculated that Volkswagen lost about three point nine million pounds on every Veyron sold, and about one point four three billion pounds on the Veyron overall.""",
   "Bugatti Veyron 16.4", "£3.9 MILLION LOST PER VEYRON")
sc("""That estimate spreads the huge development cost over a small number of cars, so it is not the same as losing money on each car's parts. But the message was clear. The Veyron was a statement, paid for by one of the largest car companies in the world. Bugatti had to make the next car a better business.""",
   "Volkswagen headquarters Wolfsburg", "A STATEMENT, NOT A BUSINESS")
sc("""The Chiron's plan looked different. Higher prices, a higher production limit of five hundred cars, and a long list of special versions and one-offs that sold for much more than the base car. That is why there were so many versions. Every variant was a way to sell the same engineering at a new price.""",
   "Bugatti Chiron Pur Sport", "EVERY VERSION, A NEW PRICE")
sc("""Here is the twist. Some of the most valuable Chirons were the ones Bugatti built only once. The Profilee was meant as a small production run, but Bugatti built only one, and it sold for nearly ten million euros. The La Voiture Noire, a one-off inspired by the nineteen thirties Type fifty-seven S C Atlantic, was reported sold for about nine and a half million pounds. Exclusivity turned into the most profitable product of all.""",
   "Bugatti La Voiture Noire", "ONE-OFFS: THE MOST VALUABLE")

# ---------- 7c. COST PER MILE ----------
ch("Cost per mile")
sc("""Let's try one more way to see the cost, with a clearly simple example. Say an owner drives one thousand miles a year, pays about forty thousand dollars a year for insurance, and eleven thousand five hundred for the annual service. Those numbers come from the estimates we showed, and the total is fifty-one thousand five hundred dollars a year.""",
   "Bugatti Chiron road", "A SIMPLE EXAMPLE")
sc("""Spread over one thousand miles, that is about fifty-one dollars per mile, before brakes, tires, storage, or any repair. A ten-mile drive to dinner would cost about five hundred dollars in fixed costs alone. That is our own calculation from the figures in this video, not an official number, but it shows why so many owners barely drive.""",
   "Bugatti Chiron night", "ABOUT $51 PER MILE")
sc("""And here is the twist. The less you drive, the higher the cost per mile becomes, because the insurance and the service are still due. An owner who drives only one hundred miles a year would pay more than five hundred dollars per mile in fixed costs. In other words, keeping a Chiron parked does not make it cheap. It makes every mile more expensive.""",
   "Bugatti Chiron garage", "PARKED IS NOT CHEAP")
sc("""That math also explains why some owners do the opposite and drive their cars a lot. If the fixed costs are the same, using the car spreads them over more miles. The trade-off is resale value. More miles usually means a lower price when the car is sold, so every owner has to decide what the car is for, a drive or an asset.""",
   "Bugatti Chiron mountain road", "OR DRIVE IT AND ENJOY IT")

# ---------- 7d. THE WARRANTY DECISION ----------
ch("The warranty decision")
sc("""One decision shapes the whole cost of ownership, the extended warranty. Remember the numbers. About two hundred four thousand dollars for an extra four years of bumper-to-bumper cover, against a replacement engine at about eight hundred fifty-six thousand dollars and a gearbox at about one hundred eighty-five thousand.""",
   "Bugatti Chiron engine", "$204,000 WARRANTY")
sc("""If nothing major breaks, the warranty looks expensive. If one big part fails, it pays for itself several times. And there is another reason owners buy it. A Chiron with a full factory history and an active warranty is easier to sell, and buyers at this level pay for certainty.""",
   "Bugatti Chiron detail", "INSURANCE FOR THE ENGINE")
sc("""So the real cost of ownership depends on choices more than on the car. How much you drive, how you insure it, whether you buy the warranty, and whether you plan to sell. Two owners with the same Chiron can end up with completely different bills.""",
   "Bugatti Chiron two cars", "SAME CAR, DIFFERENT BILLS")

# ---------- 8. THE TOTAL ----------
ch("The real total")
sc("""So let's put it together, using only the numbers we have shown. A base Chiron in America had a sticker of roughly three point one seven million dollars before options. Insurance estimates range from about thirty-six thousand to fifty thousand dollars a year. Annual service is about eleven thousand five hundred, with a major service of about thirty-four thousand every four years.""",
   "Bugatti Chiron front view", "THE PIECES")
sc("""If you add an extended warranty at two hundred four thousand, and wear items like brakes and tires, a careful owner can easily spend several hundred thousand dollars over ten years, on top of the car itself. Fuel is a tiny part of it. Insurance and service are the big parts.""",
   "Bugatti Chiron road trip", "SEVERAL HUNDRED THOUSAND OVER 10 YEARS")
sc("""And then, for many owners, the market paid them back. That is the strange truth about the Chiron. It is one of the most expensive cars on earth to keep, and also one of the few new cars that many owners could sell for more than they paid.""",
   "Bugatti Chiron Super Sport", "EXPENSIVE TO KEEP, VALUABLE TO SELL")
sc("""Which is why the real cost of a Chiron is not just money. It is access. You needed the money, the speed to get a build slot, the patience to wait, and the discipline to keep it perfect. That is what you were really buying.""",
   "Bugatti Chiron Molsheim", "THE REAL COST IS ACCESS")
sc("""Tell us in the comments: if someone gave you a Chiron but you had to pay to keep it, would you keep it or sell it? And watch the other videos in this Chiron series. Two facts most people don't know about the car, how it really compares with the Koenigsegg Jesko, and the full story of how it was made.""",
   "Koenigsegg Jesko", "KEEP IT OR SELL IT?")
sc("""And if your next vehicle is a little more down to earth, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more honest numbers about the cars and trucks people really talk about.""",
   "Bugatti Chiron sunset", "SUBSCRIBE: PICKUP REALITY")

save("video63", "What It Really Costs to Own a Bugatti Chiron", [
    "Wikipedia, Bugatti Chiron (price, deposit, deliveries, variants, production): https://en.wikipedia.org/wiki/Bugatti_Chiron",
    "The Drive, what it cost to maintain a Chiron (Jan 2023, Hamilton Collection): https://www.thedrive.com/news/heres-what-it-cost-to-maintain-a-bugatti-chiron-over-10-years",
    "Motor1, Chiron Sport 110 Ans costs $50K per year to insure (Apr 2019, ValuePenguin): https://www.motor1.com/news/347085/bugatti-chiron-sport-insurance-cost/",
    "MoneyGeek, Bugatti Chiron insurance (updated Apr 2026): https://www.moneygeek.com/insurance/auto/bugatti-chiron-insurance/",
    "Motor1, Chiron tires won't cost $42,000: https://www.motor1.com/news/180923/bugatti-chiron-tires-cost/",
    "Driven Car Guide (NZ), Singapore Chiron service cost estimate (Sept 2021, indicative): https://www.drivencarguide.co.nz/news/bugatti-owner-reveals-the-mind-blowing-services-costs-behind-3-million-hypercar/",
    "The Drive, $21,000 Veyron oil change (Dec 2020): https://www.thedrive.com/news/37983/this-is-what-a-21000-oil-change-on-a-bugatti-veyron-looks-like",
    "Bugatti newsroom, 0-400-0 record (brake specs): https://newsroom.bugatti.com/press-releases/0-400-0-km-h-in-42-seconds-bugatti-chiron-sets-world-record",
    "Motor Authority, Chiron W16 engine (air, injectors, fuel): https://www.motorauthority.com/news/1102657_a-close-look-at-the-bugatti-chiron-s-monster-w-16-engine",
    "Motor1, last 1,500-hp Chiron delivered (Jan 2024): https://www.motor1.com/news/704067/last-chiron-1500-delivered/",
    "evo, first used Chiron (Nov 2017): https://evo.co.uk/bugatti/chiron/20283/first-used-bugatti-chiron-aims-for-1m-profit",
    "duPont Registry, first US Chiron sells at RM Sotheby's (Dec 2017): https://news.dupontregistry.com/bugatti/first-us-chiron-sells-rm-sothebys-12072017",
    "Hagerty UK, Chiron Profilee auction record (Feb 2023): https://www.hagerty.co.uk/articles/bugatti-chiron-profilee-record-breaking/",
    "Top Gear, the 500th and final Chiron (May 2024): https://www.topgear.com/car-news/first-look/it-final-500th-definitely-last-ever-bugatti-chiron",
    "Car Throttle, Bugatti Tourbillon price and deliveries: https://www.carthrottle.com/news/bugatti-tourbillon-1775bhp-v16-salute-combustion",
], "C")
