import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The Mercedes-AMG One costs about two point seven million dollars. And a rumour says that after about fifty thousand kilometres, its engine needs a full factory rebuild that costs around eight hundred fifty thousand euros. Top Gear says that rumour is not quite accurate. So what does a Formula One car for the road really cost to own? This is what the sources say, and what they do not.""",
   "Mercedes-AMG One", "THE REAL COST OF A FORMULA 1 CAR FOR THE ROAD")
sc("""Here is the twist. The price on the window is not even the biggest number in this story. A build slot for this car was once listed for nearly double the original price, before a single car was built. And one of the most important costs of all, the engine rebuild, has no published price anywhere that we could verify.""",
   "Mercedes-AMG One", "THE BIGGEST NUMBER ISN'T THE PRICE")
sc("""Every figure comes from a published source, listed in the description. Where a figure is a rumour, we call it a rumour. Where we do the maths ourselves, we say so. We have not owned an AMG One, and we will not invent costs we cannot source.""",
   "Mercedes-AMG One", "EVERY NUMBER IS SOURCED")

ch("The price on the window")
sc("""Start with the sticker. Wikipedia lists two point seven two million dollars. Motor1, in twenty eighteen, said two point seven million. Top Gear lists a base price of two point four million pounds, which it says is two point two seven five million euros plus local taxes, before options such as special liveries or magnesium wheels. Different currencies, same order of money.""",
   "Mercedes-AMG One price", "~$2.7M · £2.4M · €2.275M + TAXES")
sc("""Production was capped at two hundred seventy-five cars. By our own arithmetic, at two point seven million dollars each, the full run is worth about seven hundred forty-three million dollars at list price. That is the scale of the whole project: less than a billion dollars in total sales, for a car that took more than five years to bring to market.""",
   "Mercedes-AMG One production", "275 × $2.7M ≈ $743M (OUR ARITHMETIC)")
sc("""And the demand. Wikipedia says Mercedes-AMG received more than four times as many orders as it could build, and refused to raise the limit. Top Gear says all two hundred seventy-five had already sold. So the list price was not a market price. It was the price of the right to join the queue, and for many buyers there was no queue to join.""",
   "Mercedes-AMG One buyers", "ALL 275 SOLD · 4× MORE ORDERS THAN CARS")
sc("""Options cost extra. Top Gear mentions special liveries and magnesium wheels, and does not give a price for either. So the final price any owner paid is not in the sources we have. We can say only that the list price is a starting point, which by our reading is how it works for most cars in this class.""",
   "Mercedes-AMG One livery", "OPTIONS EXTRA · NO PRICES PUBLISHED")

ch("The price of the queue")
sc("""Now the number nobody put on the window. Motor1 reported in August twenty eighteen that Mercedes-AMG would not allow buyers to flip their cars for a quick profit, according to a report in Auto Motor und Sport. Contract clauses reportedly stop owners from reselling quickly, and the company monitors the market for resale activity.""",
   "Mercedes-AMG One contract", "AMG REPORTEDLY BANNED QUICK FLIPPING")
sc("""The same article says that in November twenty seventeen, a Project One build slot was listed on Mobile dot de for about five point two million dollars, nearly double the original price. That listing was removed. A later one, with a delivery date of the fifteenth of June, twenty nineteen, had the same asking price including taxes.""",
   "Mobile.de listing", "BUILD SLOT LISTED AT ~$5.2M (REMOVED)")
sc("""By our own arithmetic, five point two million divided by two point seven million is one point nine three. So the asking price was about ninety-three percent above the list price. Remember that these were asking prices, not completed sales, and that the listings were removed. They show what some people hoped to get, not what anyone paid.""",
   "Mercedes-AMG One build slot", "ASKING 1.93× LIST (OUR ARITHMETIC)")
sc("""Compare that with a later data point. In April twenty twenty-four, Motor1 reported a car with just fifty-five miles being offered by SBX Cars at auction. The highest bid at the time of writing was one hundred twenty-eight thousand dollars, and the article expected it to reach seven figures. We do not know the final price, because the article was written before the auction ended.""",
   "Mercedes-AMG One for sale", "APRIL 2024: 55-MILE CAR AT AUCTION")

ch("The engine bill")
sc("""Here is the cost that matters most. Wikipedia says the engine has a lifespan of about fifty thousand kilometres, after which owners must return the car for engine refurbishment. Motor1 says the one-point-six-litre V six must be rebuilt once every thirty-one thousand miles, which is the same distance. Neither gives a cost.""",
   "Mercedes-AMG One engine", "REBUILD EVERY ~50,000 KM · COST NOT PUBLISHED")
sc("""Top Gear addresses the rumour directly. It says a rumour claimed the Formula One derived V six needs a full factory rebuild after about fifty thousand kilometres, costing around eight hundred fifty thousand euros. And it says that is not quite accurate. Engineers told them that each engine's life depends on how the owner has used it.""",
   "Mercedes-AMG One engineers", "RUMOUR: €850,000 · TOP GEAR: NOT QUITE ACCURATE")
sc("""That quote matters, so we repeat it. According to Top Gear, an engine used often on track would need a teardown sooner than one used only at casual meets. So fifty thousand kilometres is a guideline, not a clock. It also means the true cost per kilometre is not fixed. It depends on whether the car is driven or kept.""",
   "Track day", "\"EACH ENGINE'S LIFE WILL DEPEND ON HOW THE OWNER HAS USED IT\"")
sc("""Now our arithmetic, using the rumour only to show scale. Eight hundred fifty thousand euros over fifty thousand kilometres is seventeen euros per kilometre. Against the base price of two point two seven five million euros, it would be about thirty-seven percent. We stress again that the figure is a rumour, and that Top Gear said it was not quite right.""",
   "Calculator", "IF THE RUMOUR WERE TRUE: €17/KM · 37% OF PRICE (OUR ARITHMETIC)")
sc("""What can we say with confidence? That the car goes back to the manufacturer for the work. Motor1's 2018 report says owners must contact AMG for the service. Top Gear says the engine needs a team of experts to start. This is a service model closer to a racing team than to an ordinary garage, whatever the final invoice turns out to be.""",
   "Mercedes-AMG service", "OWNERS MUST CONTACT AMG FOR THE REBUILD")
sc("""Compare it with a rival. Fortune, citing Bloomberg, reported that servicing the Aston Martin Valkyrie could cost close to four hundred fifty thousand dollars over three years, or three hundred forty thousand on a cheaper plan. That figure is published. For the AMG One, we found only the rumour. So it is honest to say that the Valkyrie is better documented, not necessarily cheaper.""",
   "Aston Martin Valkyrie service", "VALKYRIE: ~$450K / 3 YEARS (BLOOMBERG)")

ch("Fuel and running costs")
sc("""Top Gear lists official fuel economy of thirty-two miles per gallon and carbon dioxide emissions of one hundred ninety-eight grams per kilometre. The electric range is about eleven miles from an eight point four kilowatt-hour battery, and the fuel tank holds fifty-five litres. Note that Wikipedia lists the electric range as eighteen point one kilometres, which is consistent with eleven miles.""",
   "Mercedes-AMG One fuel", "32 MPG · 198 G/KM · 55 L TANK · 11 MILES ELECTRIC")
sc("""By our arithmetic, fifty-five litres is about fourteen and a half US gallons. At thirty-two miles per gallon, that is around four hundred sixty-five miles on a full tank, if the official figure holds. A car driven to its limits will do far worse. And remember this is a test-cycle number for a car with more than a thousand horsepower.""",
   "Petrol pump", "55 L ≈ 14.5 US GAL ≈ 465 MILES (OUR ARITHMETIC)")
sc("""A rough annual fuel cost, as our arithmetic. Five thousand miles a year at thirty-two miles per gallon is about one hundred fifty-six gallons. At an assumed four dollars a gallon, which is our own assumption and not a sourced price, that is about six hundred twenty-five dollars. Against the price of the car, the fuel is the smallest line of all.""",
   "Fuel cost", "5,000 MILES/YEAR ≈ 156 GAL ≈ $625 (ASSUMED $4/GAL)")
sc("""Top Gear also notes something about the engine: the Formula One version idles at five thousand r p m and needs a team of experts to start, while the road car idles at twelve hundred. That work is why the car can be driven at all. It is also why fuel, not engine hours, is not the cost to worry about.""",
   "Mercedes-AMG One engine", "F1: 5,000 RPM IDLE · ROAD CAR: 1,200 RPM")

ch("Insurance, storage and the unsourced lines")
sc("""What about insurance, storage, tyres and brakes? We found no published figures for the AMG One. Anyone who tells you a precise number for these has not got it from the sources we used. We know that the car has carbon fibre bodywork and chassis, and that only two hundred seventy-five exist, which would affect repair and replacement. But we cannot put a price on it.""",
   "Mercedes-AMG One carbon fibre", "INSURANCE, TYRES, BRAKES: NOT SOURCED")
sc("""Parts and repairs are the same. Wikipedia lists a carbon fibre body and chassis, active aerodynamic parts, a two-part extendable rear wing and adjustable front louvres. Each is a component that few other cars share. By our reading, replacing any of them would be expensive and slow. But that is reasoning, not a quotation.""",
   "Mercedes-AMG One rear wing", "COMPONENTS SHARED WITH NO OTHER CAR (OUR READING)")
sc("""There is also the matter of ownership rules. We have seen that the company reportedly discouraged flipping. We have not seen any source on whether it restricts how the car is used, stored or transported. Owners will have signed contracts we have not read, so we cannot tell you what they say.""",
   "Contract", "WE HAVEN'T SEEN THE OWNER CONTRACT")

ch("What each pound and each horsepower costs")
sc("""Some unit costs, all our own arithmetic, from sourced figures. Wikipedia lists two point seven two million dollars and one thousand sixty-three metric horsepower. Divide, and each horsepower costs about two thousand, five hundred fifty-nine dollars. That is a hypercar number, of course, but it gives you a way to compare cars that otherwise have nothing in common.""",
   "Mercedes-AMG One power", "$2.72M ÷ 1,063 PS ≈ $2,559 PER PS (OUR ARITHMETIC)")
sc("""Per kilogram, using the lowest listed kerb weight of one thousand, six hundred ninety-five, the same price works out at about sixteen hundred dollars for every kilogram of car. Compare it with a family pickup, which we leave to the other videos of this channel. The point is not that the AMG One is good or bad value, only that value is not the reason anyone buys one.""",
   "Mercedes-AMG One weight", "≈ $1,600 PER KILOGRAM OF CAR (OUR ARITHMETIC)")
sc("""And per second. Wikipedia lists two point nine seconds from zero to a hundred. Spread the price over the acceleration, if you like, and it comes to around nine hundred thirty-eight thousand dollars for each second of that sprint. This is not a serious measure, and no buyer used it. We include it only to show how far the price sits from any practical benchmark.""",
   "Mercedes-AMG One acceleration", "$2.72M ÷ 2.9 S ≈ $938K PER SECOND (OUR ARITHMETIC)")

ch("Three owners, three bills")
sc("""Let us imagine three owners, using the engine guideline of fifty thousand kilometres. These are scenarios, not real people, and the numbers are our arithmetic. The first drives five thousand kilometres a year, a collector who rarely takes the car out. By the guideline, that owner reaches the rebuild point in ten years.""",
   "Collector garage", "OWNER 1: 5,000 KM/YEAR → REBUILD IN 10 YEARS")
sc("""The second owner drives twenty thousand kilometres a year. That is still low for an ordinary car, but high for a hypercar. By the guideline, the rebuild point arrives in two and a half years. If the rumoured eight hundred fifty thousand euro figure were true, which Top Gear says is not quite accurate, that owner would face about three hundred forty thousand euros for each year of driving.""",
   "Mercedes-AMG One road", "OWNER 2: 20,000 KM/YEAR → REBUILD IN 2.5 YEARS")
sc("""The third owner takes the car to the track, where, according to Top Gear, engine life depends heavily on use. We cannot assign a number to that owner, because the sources do not give one. What we can say is that the rebuild point could arrive earlier, and that the cost per kilometre would rise. Each lap is not free.""",
   "Racing circuit", "OWNER 3: TRACK USE → EARLIER TEARDOWN (TOP GEAR)")
sc("""The lesson from the three owners is that the engine bill is a cost of use, not a cost of time. A car in a garage costs little in engine terms. A car on the road costs more. A car on the track costs more still. That is the opposite of the way most expensive cars work, where depreciation, not use, is the main bill.""",
   "Mercedes-AMG One owners", "A COST OF USE, NOT OF TIME (OUR READING)")

ch("Where is it built, and who services it")
sc("""There is a small conflict in the sources worth noting. Wikipedia says the car was developed at Mercedes-AMG in Affalterbach, Germany. Top Gear says only two hundred seventy-five are being built at a special Formula One grade facility in the United Kingdom. Motor1's twenty eighteen report also said it would be built in the U.K. alongside Mercedes-AMG's Formula One engines.""",
   "Mercedes-AMG facility", "SOURCES DISAGREE: GERMANY VS UNITED KINGDOM")
sc("""We think the sources describe different stages, development in one place and the engine in another, but we cannot confirm that. Why does it matter? Because the service model depends on where the work is done. If owners must contact AMG for the rebuild, as Motor1 reports, then the location of the specialists affects shipping, time and cost.""",
   "Mercedes-AMG engineering", "WHERE IT IS BUILT AFFECTS WHERE IT IS SERVICED (OUR READING)")
sc("""Top Gear adds that Mercedes has no plans for a roadster or a Black Series version of the car. So the owners of two hundred seventy-five cars have no later version to trade up to, within the same model. For a collector, that supports the idea that the car will keep a particular place in the market. For a driver, it means no cheaper sibling will ever appear.""",
   "Mercedes-AMG One", "NO ROADSTER · NO BLACK SERIES")

ch("The Valkyrie as a yardstick")
sc("""Since the Valkyrie is the best-documented rival, use it as a yardstick. Fortune, citing Bloomberg, reports a price of at least three million dollars and a service plan of close to four hundred fifty thousand dollars over three years. Aston Martin's spokesman said the car needs motor-sport engineers for maintenance, and that the costs match other hypercar service charges.""",
   "Aston Martin Valkyrie", "VALKYRIE: $3M+ AND ~$450K SERVICE OVER 3 YEARS")
sc("""By our arithmetic, the Valkyrie's service plan is about fifteen percent of its three million dollar price over three years. If the AMG One's real rebuild bill were anywhere near the rumour, thirty-seven percent over one rebuild, it would be a heavier burden. But the rumour is disputed, and the periods are different, so this is only a way to think about scale.""",
   "Hypercar service plans", "VALKYRIE PLAN ≈ 15% OF PRICE OVER 3 YEARS (OUR ARITHMETIC)")
sc("""Fortune also says a Bugatti Chiron, at a similar price, costs around one hundred seventy thousand dollars to service over four years. So even among hypercars, the published service bills vary by a factor of more than three. The category is expensive, but it is not uniformly so. The more a car resembles a race car, the more its upkeep resembles a race team's.""",
   "Bugatti Chiron", "CHIRON: ~$170K OVER 4 YEARS (BLOOMBERG)")
sc("""And Aston Martin is not alone in having money troubles that sit behind a hypercar. Fortune says the company had a debt pile of about one point four billion dollars in February twenty twenty-four. Mercedes, by contrast, is a very large company. A project that needed two hundred seventy-five customers to pay millions each was affordable for Mercedes in a way it could not be for a smaller firm.""",
   "Mercedes-Benz", "MERCEDES CAN CARRY A LOW-VOLUME PROJECT (OUR READING)")

ch("What the money buys")
sc("""To be fair to the car, look at what the price buys. Wikipedia lists a Nürburgring Nordschleife lap of six minutes, twenty-nine point zero nine seconds in September twenty twenty-four, which the page describes as the first sub six-thirty lap by a road-legal production car. It also lists production-car records at Monza, in April twenty twenty-three, and at the Red Bull Ring.""",
   "Nürburgring Nordschleife", "6:29.09 NÜRBURGRING · MONZA RECORD (WIKIPEDIA)")
sc("""Wikipedia also lists zero to three hundred kilometres per hour in fifteen point six seconds, and a top speed of three hundred fifty-two, electronically limited. Tobias Moers told Top Gear he was not interested in a speed competition, and that the experience of driving a Formula One powertrain mattered more than top speed. The car is built for that experience, not for a number.""",
   "Mercedes-AMG One", "\"THE EXPERIENCE OF DRIVING A FORMULA 1 POWERTRAIN\"")
sc("""So what is the experience worth? That is a personal question, and we will not answer it for you. What we can do is describe it from the sources: a hybrid with an M G U H, a V six revving to eleven thousand r p m, active aerodynamics, a car that goes from a hundred to two hundred in about four seconds. By our arithmetic, seven point zero minus two point nine is four point one.""",
   "Mercedes-AMG One cockpit", "100 → 200 KM/H IN 4.1 S (OUR ARITHMETIC)")

ch("A word on value")
sc("""Will the car hold its value? We cannot say, and we found no sale prices to prove either way. We have a build slot asking price from twenty seventeen, which was removed, and an auction bid from twenty twenty-four, which was a mid-auction figure on a fifty-five mile car. Neither is a price at which a car changed hands.""",
   "Mercedes-AMG One for sale", "NO CONFIRMED RESALE PRICES FOUND")
sc("""Collectors often assume that limited cars always rise. The sources we used do not say that. They say only that the car is limited, sold out and subject to contract rules. Whether the rebuild obligation hurts the value of a high-mileage car is another open question. By our reading, a car with a fresh engine might be worth more than one close to its limit.""",
   "Mercedes-AMG One collector", "A FRESH ENGINE MAY MATTER TO VALUE (OUR READING)")
sc("""So here is the honest summary. The price is about two point seven million dollars. The engine must be rebuilt at about fifty thousand kilometres by the manufacturer, at a price that is not published. Fuel is minor. Everything else is unknown. If someone gives you a single number for the cost of ownership, ask for the source. The sources we found do not give one.""",
   "Mercedes-AMG One", "THE HONEST SUMMARY")

ch("Putting it together")
sc("""Let us collect only what we can source. The price is about two point seven million dollars. The engine needs a factory rebuild at about fifty thousand kilometres, at a cost the sources do not give, and a rumour of eight hundred fifty thousand euros that Top Gear calls not quite accurate. Fuel is cheap by comparison. The rest is unknown.""",
   "Mercedes-AMG One", "WHAT THE SOURCES SAY")
sc("""A simple comparison, all our arithmetic. If the rumour were true and the car lived to exactly fifty thousand kilometres, the rebuild alone would be about thirty-seven percent of the purchase price. The Valkyrie's published service plan, at one hundred fifty thousand dollars a year, would reach four hundred fifty thousand in three years. Neither number is small. Neither is the whole bill.""",
   "Hypercar costs", "REBUILD RUMOUR 37% OF PRICE · VALKYRIE $150K/YEAR")
sc("""What does this tell a buyer? That the purchase price of an extreme car is just the entrance fee. The ownership model, factory service, limited supply and strict contracts, is the real product. Mercedes sold two hundred seventy-five people a relationship with a racing department, and the engine rebuild is one visible piece of it.""",
   "Mercedes-AMG One", "THE PRICE IS THE ENTRANCE FEE (OUR READING)")
sc("""Does it make financial sense? That is the wrong question for a car like this. The people who ordered it were buying a piece of Formula One engineering, and Motor1 reports that AMG has ruled out putting an F1 engine into a future road car. If that holds, the AMG One may remain the only road car of its kind from Mercedes, at least by that report.""",
   "Mercedes-AMG One", "MOTOR1: NO F1 ENGINE IN A FUTURE ROAD CAR")
sc("""A last caution. This video does not tell you what a Mercedes-AMG One costs per year. It tells you what is published, what is rumoured, and what we could not find. We think that is more useful than a confident number with no source behind it. If you know a verified figure, tell us in the comments, with where it comes from.""",
   "Mercedes-AMG One", "KNOW A SOURCED NUMBER? TELL US")
sc("""In the other videos of this series, we reveal two secrets hidden inside the AMG One, compare it with the Aston Martin Valkyrie, and explain why it took years longer than promised. And if you would rather spend your money on something you can drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video103", "The Real Cost of a Formula 1 Car for the Road", [
    "Wikipedia, Mercedes-AMG One: https://en.wikipedia.org/wiki/Mercedes-AMG_One",
    "Top Gear, Mercedes-AMG One buying guide: https://www.topgear.com/car-reviews/mercedes-benz/amg-one/buying",
    "Motor1, Mercedes-AMG won't allow Project One owners to flip their cars (2 Aug 2018): https://www.motor1.com/news/260939/mercedes-amg-project-one/",
    "Motor1, This Mercedes-AMG One with 55 miles begs to be driven (12 Apr 2024): https://www.motor1.com/news/715837/amg-one-low-mileage-sale/",
    "Fortune/Bloomberg, Aston Martin's most expensive Valkyrie supercar (23 Feb 2024): https://fortune.com/europe/2024/02/23/aston-martin-most-expensive-valkyrie-supercar-3-million-plus-450000-upkeep",
], "C")
