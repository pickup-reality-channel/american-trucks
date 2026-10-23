import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Could a normal person ever afford a Ferrari SF90? The sticker price is more than half a million dollars. But the sticker price is only the beginning. There is insurance, maintenance, tires, options, a battery that Ferrari plans to replace, and one number that surprises almost everyone. Today we do the math, using real published figures.""",
   "Ferrari SF90 Stradale", "CAN A NORMAL PERSON AFFORD AN SF90?")
sc("""Here is a hint about the surprise. One of the most expensive parts of owning many supercars is how much value they lose. And for the SF90, that number looks very different from what most people expect. We will get to it.""",
   "Ferrari SF90 Stradale rear", "THE NUMBER THAT SURPRISES EVERYONE")
sc("""We will also look at the SF90 that crashed in Finland, the insurance payout that followed, and why the electric range on the American sticker is so much shorter than the one Ferrari advertised in Europe. Every figure is from a published source, listed in the description. Where a number is an estimate, we will say so.""",
   "Ferrari SF90 Spider", "EVERY NUMBER IS SOURCED")
sc("""First, a quick reminder of what you would be buying. The SF90 Stradale has a twin-turbo V8 and three electric motors, about nine hundred eighty-six horsepower combined, and it reaches one hundred kilometers per hour in two point five seconds, according to Wikipedia. It was Ferrari's first plug-in hybrid series production car.""",
   "Ferrari SF90 Stradale engine", "986 HP PLUG-IN HYBRID")

# ---------- 1. THE PRICE ----------
ch("The sticker price")
sc("""Let's start with the price. AutoMonitor, a car valuation site, says the SF90 Stradale had a manufacturer's suggested retail price of about five hundred seven thousand dollars when it launched. By the twenty twenty-four model year, Kelley Blue Book lists the Stradale coupe at about five hundred twenty-nine thousand dollars.""",
   "Ferrari SF90 Stradale red", "STARTS AT ~$529,000 (2024)")
sc("""Want the open-top version? Kelley Blue Book lists the twenty twenty-four SF90 Spider at about five hundred eighty-four thousand dollars. That is about fifty-five thousand dollars more, for a retractable hard top. Fifty-five thousand dollars is close to the price of a well-equipped new pickup truck.""",
   "Ferrari SF90 Spider roof", "SPIDER: ~$584,000")
sc("""Then come the options. AutoMonitor says option packages can add thirty thousand to eighty thousand dollars. One single option shows how fast it adds up. CarGurus reported that the Assetto Fiorano package, the track pack with special shock absorbers, carbon fiber parts, and a titanium exhaust, costs about fifty thousand dollars.""",
   "Ferrari SF90 Assetto Fiorano", "ASSETTO FIORANO: ~$50,000")
sc("""Here is the twist on the purchase price. Kelley Blue Book lists a fair purchase price for the twenty twenty-four Stradale of about four hundred ninety-four thousand dollars, which is below the sticker price. In other words, the market price can sit below the list price, which is not always true for a Ferrari.""",
   "Ferrari dealership", "FAIR PRICE: ~$494,000")
sc("""But the Spider tells a different story. Kelley Blue Book lists a fair purchase price for the twenty twenty-four SF90 Spider of about five hundred eighty-eight thousand dollars, slightly above its own list price of about five hundred eighty-four thousand. So the open car was in higher demand. Buyers were paying more than the sticker for the version with the folding roof.""",
   "Ferrari SF90 Spider open", "SPIDER: ABOVE STICKER")
sc("""So a realistic starting point for a well-optioned SF90 Stradale in America is somewhere around five hundred fifty thousand dollars before taxes and fees. Let's use that as our target, and see what it takes to get there.""",
   "Ferrari SF90 Stradale yellow", "TARGET: ~$550,000")
sc("""And that is before sales tax. Sales tax depends on the state, so here is a simple example with our own arithmetic. At a seven percent rate, a five hundred fifty thousand dollar car would carry about thirty-eight thousand five hundred dollars in sales tax. That alone is almost half of the median household income for a full year.""",
   "sales tax receipt", "EXAMPLE: 7% TAX = ~$38,500")
sc("""So before the car leaves the dealer, a buyer could already be close to six hundred thousand dollars, once options, tax, registration, and delivery are added. That is the real entry ticket. Now let's put that number next to a normal paycheck.""",
   "Ferrari SF90 delivery", "~$600,000 OUT THE DOOR")

# ---------- 2. THE INCOME MATH ----------
ch("The income math")
sc("""How does that compare with a normal income? The U S Census Bureau reported that the median American household income in twenty twenty-three was about eighty thousand six hundred dollars. That means half of households earn less than that, and half earn more.""",
   "American suburb houses", "MEDIAN HOUSEHOLD: ~$80,600")
sc("""The Census figure was eighty thousand six hundred ten dollars, a four percent rise from about seventy-seven thousand five hundred forty in twenty twenty-two. That is the income of a real middle-class household, often with two working adults. Keep that number in mind, because we will compare every cost in this video against it.""",
   "family home driveway", "UP 4% FROM 2022")
sc("""At that income, a five hundred fifty thousand dollar Ferrari is almost seven years of total household income, before taxes, and before spending a single dollar on food, housing, or anything else. Just to be clear, this is simple arithmetic, not a financial recommendation.""",
   "family budget calculator", "~7 YEARS OF INCOME")
sc("""What about a loan? Here is an example, using our own arithmetic. Put one hundred thousand dollars down, borrow four hundred thousand, and pay it back over seven years at an assumed interest rate of seven percent. The monthly payment would be about six thousand dollars. That is about seventy-two thousand dollars a year, close to the entire median household income.""",
   "car loan paperwork", "LOAN EXAMPLE: ~$6,000/MONTH")
sc("""And the hundred thousand dollar down payment is more than a full year of median income on its own. So for a household near the median, the honest answer is no. The payment alone would take almost everything. But the payment is not the only cost. Now let's look at the running costs.""",
   "Ferrari SF90 Stradale front", "THE HONEST ANSWER")

# ---------- 3. INSURANCE ----------
ch("Insurance")
sc("""Insurance is the first big running cost. AutoMonitor estimates that an SF90 typically costs ten thousand to sixteen thousand dollars a year to insure, depending on location, driving record, and coverage. It does not list a source for that range, so treat it as an estimate.""",
   "Ferrari SF90 Stradale garage", "INSURANCE: ~$10K-$16K/YEAR (EST.)")
sc("""To understand why, look at what happened in Finland. ClubAlfa reported in March twenty twenty-four that an SF90 hydroplaned on a highway in heavy rain, while driving within the speed limit, and left the road. Nobody was hurt, and no other cars were involved. But the car was badly damaged.""",
   "Ferrari SF90 Stradale rain", "THE FINLAND CRASH")
sc("""The insurer decided not to repair it. Instead, it bought the car back and sold its salvageable parts. ClubAlfa said the owner received about five hundred thirty thousand euros, down from an original value of about seven hundred fifty thousand euros, because the car had covered fifty-three thousand kilometers in two years.""",
   "Ferrari SF90 Stradale damaged", "€530,000 PAYOUT")
sc("""ClubAlfa said the claim was only resolved after months of waiting. Think about what that means for an owner. Months without the car, an insurer deciding the car was not worth repairing, and a payout about two hundred twenty thousand euros below its original value. Even with full insurance, a crash in an SF90 can be very expensive.""",
   "insurance claim paperwork", "MONTHS OF WAITING")
sc("""ClubAlfa also gave examples of Ferrari part prices. About thirty thousand euros for a convertible top, about thirty thousand for a rear diffuser, and up to eighty thousand for a rear bumper. A single body part can cost as much as an entire new family car. That is why insurers charge so much.""",
   "Ferrari SF90 rear diffuser", "A BUMPER: UP TO €80,000")
sc("""And here is a detail most people miss. That owner drove fifty-three thousand kilometers in two years, about thirty-three thousand miles. Many SF90s are driven far less. The Finnish owner was actually using the car, and the mileage cut the payout by a large amount.""",
   "Ferrari SF90 Stradale highway", "53,000 KM IN TWO YEARS")

# ---------- 4. MAINTENANCE ----------
ch("Maintenance")
sc("""Now maintenance, and this is where Ferrari helps more than most people know. Ferrari's official website describes its Genuine Maintenance program, which covers regular scheduled maintenance for the first seven years of a new car, with original parts and Ferrari technicians.""",
   "Ferrari service center", "7 YEARS OF SCHEDULED MAINTENANCE")
sc("""Ferrari says owners can choose to service the car either every twelve thousand five hundred miles, or once a year, with no mileage limit on the yearly option. So for the first seven years, routine servicing is part of the deal. That is a big deal for a car with a V8, three motors, and a high-voltage battery.""",
   "Ferrari SF90 engine bay", "EVERY 12,500 MILES OR ONCE A YEAR")
sc("""After that, the bills begin. AutoMonitor estimates that annual service at an authorized dealer typically costs four thousand five hundred to seven thousand dollars, and that a major service can cost six thousand to twelve thousand dollars. Again, these are estimates without a listed source.""",
   "Ferrari mechanic", "AFTER YEAR 7: ~$4.5K-$7K/YEAR (EST.)")
sc("""Tires are a separate cost. AutoMonitor estimates three hundred fifty to six hundred dollars per tire, or about one thousand eight hundred to three thousand dollars for a full set. Drive the car hard on a track, and a set may not last long.""",
   "Ferrari SF90 wheel tire", "TIRES: ~$1,800-$3,000 A SET")
sc("""And there is the warranty. Kelley Blue Book lists a three-year, unlimited-mile basic warranty on the twenty twenty-four SF90. Ferrari's website says that can be extended in blocks, and offers a paid program called Power sixteen that can cover major parts like the engine and transmission, renewed yearly up to the sixteenth year of the car's life.""",
   "Ferrari SF90 Stradale side", "3-YEAR WARRANTY, EXTENDABLE")

# ---------- 5. THE BATTERY ----------
ch("The battery question")
sc("""Now the question every hybrid buyer asks. What happens to the battery? The SF90 has a seven point nine kilowatt hour battery, InsideEVs reported. All batteries lose capacity over time. So what does Ferrari do about it?""",
   "Ferrari SF90 battery", "WHAT ABOUT THE BATTERY?")
sc("""In twenty twenty-four, Bloomberg reported that Ferrari planned a battery service subscription for its hybrids and electric cars, at around seven thousand euros, about seven thousand five hundred dollars, a year. For hybrids like the SF90, Bloomberg said the plan included a battery replacement after eight years.""",
   "Ferrari SF90 Stradale plug", "BATTERY PLAN: ~$7,500/YEAR")
sc("""ClubAlfa described two options, called Hybrid Warranty and Power Hybrid. It said that under the Hybrid Warranty, Ferrari commits to replacing the high-voltage battery free of charge at the eighth year, and that Power Hybrid covers major hybrid components from year eight to year sixteen. ClubAlfa noted that the price was based on reports, not confirmed.""",
   "Ferrari SF90 Spider rear", "NEW BATTERY AT YEAR 8")
sc("""Now imagine keeping the car for sixteen years, the full length of Ferrari's hybrid coverage. At about seven thousand five hundred dollars a year, a battery subscription would add up to about one hundred twenty thousand dollars over that time, by our own arithmetic. That is more than the price of many luxury sedans, spent just on keeping the hybrid system covered.""",
   "Ferrari SF90 Stradale classic", "16 YEARS: ~$120,000 (EXAMPLE)")
sc("""Of course, an owner does not have to buy the plan. But the alternative is to carry the risk of a hybrid system failure alone, on a car with three motors, power electronics, and a high-voltage battery. For most SF90 owners, paying for peace of mind will probably be the easier choice.""",
   "Ferrari SF90 motor", "PEACE OF MIND HAS A PRICE")
sc("""Here is the twist. Ferrari is basically treating the battery like a service item, the same way it treats oil and filters. You pay a yearly fee, and Ferrari keeps the hybrid system fresh. For an owner, that removes the fear of a huge battery bill. But it adds one more yearly cost to the list.""",
   "Ferrari SF90 Stradale white", "THE BATTERY AS A SERVICE")

# ---------- 6. FUEL ----------
ch("Fuel and the range twist")
sc("""Fuel is the smallest cost on the list, but there is a twist hiding here. Ferrari's European figures, reported by InsideEVs, promised up to twenty-five kilometers of electric range, which is about fifteen miles. But Kelley Blue Book lists only eight miles of electric range for the twenty twenty-four SF90.""",
   "Ferrari SF90 Stradale charging", "15 MILES OR 8 MILES?")
sc("""That gap is a big one. Fifteen miles of silent driving can cover a short trip across town. Eight miles is closer to leaving your neighborhood quietly, before the V8 wakes up. For an owner who imagined running errands on electricity, the American number tells a more modest story.""",
   "Ferrari SF90 Stradale suburb", "8 MILES OF SILENCE")
sc("""Why the difference? Europe and the United States use different testing methods. The American E P A test is generally tougher on electric range than the European cycles used in many marketing claims. So the same car can show a much shorter range on an American window sticker.""",
   "Ferrari SF90 Stradale city street", "DIFFERENT TESTS, DIFFERENT NUMBERS")
sc("""What does it cost to charge? Here is our own example. A full charge of the seven point nine kilowatt hour battery, at an assumed home electricity price of seventeen cents per kilowatt hour, would cost about one dollar and thirty-four cents. Charging losses add a little. It is probably the cheapest thing you will ever do with a Ferrari.""",
   "home EV charger garage", "A FULL CHARGE: ~$1.34 (EXAMPLE)")
sc("""Kelley Blue Book lists combined fuel economy of about seventeen to eighteen miles per gallon on gasoline, with premium fuel recommended. CarGurus lists up to fifty-one M P G e, a figure that includes electric driving. In real life, that depends on how often the car is plugged in. Either way, at these prices, fuel is not what breaks the budget.""",
   "gas station premium fuel", "~17-18 MPG ON GASOLINE")
sc("""Here is a simple example, again our own arithmetic. Drive five thousand miles a year at about seventeen miles per gallon, and you would burn around two hundred ninety-four gallons. At an assumed four dollars a gallon for premium fuel, that is about one thousand two hundred dollars a year. Less than one month of the insurance estimate.""",
   "fuel pump premium", "FUEL: ~$1,200/YEAR (EXAMPLE)")

# ---------- 7. DEPRECIATION ----------
ch("The surprise: depreciation")
sc("""Now the number that surprises everyone. Depreciation, which means how much value a car loses over time. Many expensive cars lose a huge share of their price in the first few years. So how much does the SF90 lose?""",
   "Ferrari SF90 Stradale for sale", "HOW MUCH VALUE DOES IT LOSE?")
sc("""Kelley Blue Book lists a private party value of about four hundred seventy-eight thousand dollars for a twenty twenty-four SF90 Stradale. Compare that with the list price of about five hundred twenty-nine thousand. The difference is about fifty thousand dollars, or roughly ten percent.""",
   "Ferrari SF90 Stradale used", "RESALE: ~$478,000")
sc("""AutoMonitor goes further. It estimates that a well-maintained SF90, driven two thousand to four thousand miles a year, can keep seventy-five to ninety percent of its purchase price over five years. It also says used SF90s trade between about four hundred eighty thousand and six hundred fifty thousand dollars, depending on version and condition.""",
   "Ferrari SF90 XX Stradale", "USED: ~$480K-$650K")
sc("""Here is why that matters. Losing ten to twenty-five percent of half a million dollars is still a lot of money, between about fifty thousand and one hundred twenty-five thousand. But compared with many luxury cars, it is a relatively gentle drop. Ferrari limits supply, and that helps keep values up.""",
   "Ferrari Maranello factory", "LIMITED SUPPLY HOLDS VALUE")
sc("""And notice the condition in that estimate. Two thousand to four thousand miles a year. The Finnish car, driven fifty-three thousand kilometers in two years, lost far more value. The cheapest way to own an SF90, it seems, is to hardly drive it. That is the strange economics of a supercar.""",
   "Ferrari SF90 Stradale covered", "DRIVE LESS, LOSE LESS")

# ---------- 8. THE FULL BILL ----------
ch("The full bill")
sc("""So let's add it up, for five years, using the figures we have seen. These are rough estimates, not a quote. Insurance at ten to sixteen thousand a year adds about fifty to eighty thousand dollars. Scheduled maintenance is covered by Ferrari in the first seven years. Tires and other wear items might add several thousand more.""",
   "Ferrari SF90 Stradale", "5-YEAR ESTIMATE")
sc("""A battery subscription, if you choose it, at about seven thousand five hundred dollars a year, would add about thirty-seven thousand five hundred dollars over five years. And depreciation, based on AutoMonitor's estimate, could take another fifty to one hundred twenty-five thousand.""",
   "Ferrari SF90 Spider", "BATTERY + DEPRECIATION")
sc("""Put it together, and the cost of simply keeping an SF90 for five years, beyond the purchase price, could be somewhere around one hundred fifty thousand to two hundred fifty thousand dollars. That is two to three times the median annual household income, just to keep the car.""",
   "Ferrari SF90 Stradale night", "~$150K-$250K TO KEEP IT")
sc("""And remember the recall. In October twenty twenty-three, Motor Authority reported that six hundred fourteen SF90s in America were recalled for turbo oil pipes that could leak and start a fire. The repair was free. But owners were told not to drive their cars until it was done, a reminder that even a half-million-dollar car can sit in the garage.""",
   "Ferrari SF90 recall", "RECALL: 614 CARS")

# ---------- 9. WHO CAN ----------
ch("So who can afford it?")
sc("""So who can actually afford an SF90? Using a very rough rule of thumb that many personal finance writers share, a car should cost a small fraction of your income or wealth. By that logic, the SF90 is a car for people with millions in assets, not for someone earning even a high salary.""",
   "luxury mansion garage", "A CAR FOR MILLIONAIRES")
sc("""Ferrari also controls who gets the newest cars. When the SF90 launched, Reuters reported that about two thousand selected customers were invited to view and reserve it. For the X X version, Evo India reported that all seven hundred ninety-nine Stradales and five hundred ninety-nine Spiders were already sold. Money is not always enough. You also need to be on the list.""",
   "Ferrari SF90 XX Stradale track", "MONEY IS NOT ENOUGH")
sc("""Is there a cheaper way into this technology? Ferrari's two ninety-six G T B uses a plug-in hybrid V6. Carwow Spain listed it at about two hundred sixty-nine thousand euros at launch, roughly half the price of an SF90. Still not cheap, but a different world of cost.""",
   "Ferrari 296 GTB", "THE CHEAPER FERRARI HYBRID")
sc("""And there is the used market. AutoMonitor says used SF90s trade from about four hundred eighty thousand dollars. That saves some money, but the running costs do not get smaller with a used car. Insurance, tires, and the battery plan stay about the same, and an older car may be outside Ferrari's seven-year maintenance window.""",
   "used Ferrari dealer", "USED SF90: ~$480K AND UP")
sc("""And the SF90 itself has already been replaced. Motoring Research reported that the eight forty-nine Testarossa, revealed in September twenty twenty-five, takes its place with about one thousand fifty horsepower, at about four hundred thousand pounds for the coupe in Europe. As new models arrive, older SF90s will slowly become a little more reachable on the used market.""",
   "Ferrari 849 Testarossa", "REPLACED BY THE 849")

# ---------- 10. ANSWER ----------
ch("The answer")
sc("""So, can a normal person afford a Ferrari SF90? For a household near the median income, the honest answer is no. The purchase price is about seven years of total income, and the running costs alone could match two or three years of income over five years.""",
   "Ferrari SF90 Stradale red", "THE ANSWER: NO")
sc("""But the surprise is that the SF90 is not the money pit people expect. Ferrari covers scheduled maintenance for seven years, offers a plan to replace the battery, and values have held up well for low-mileage cars. For the wealthy buyer, it can actually be one of the less painful ways to own a hypercar-level machine.""",
   "Ferrari SF90 Stradale yellow", "NOT THE MONEY PIT YOU EXPECT")
sc("""Tell us in the comments. If someone gave you an SF90 for free, could you afford to keep it? In the other videos of this series, we reveal two things you didn't know about the SF90, compare it with the McLaren Artura, and tell the story behind Ferrari's first plug-in hybrid.""",
   "Ferrari SF90 Spider sunset", "COULD YOU AFFORD TO KEEP IT?")
sc("""If you want a vehicle you can actually afford to buy and own, our twenty twenty-seven Truck Buyer's Guide is linked in the description, with real numbers on the trucks most people buy. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "pickup truck dealership", "SUBSCRIBE: PICKUP REALITY")

save("video71", "Can a Normal Person Afford a Ferrari SF90?", [
    "Wikipedia, Ferrari SF90 Stradale: https://en.wikipedia.org/wiki/Ferrari_SF90_Stradale",
    "Kelley Blue Book, 2024 Ferrari SF90 (MSRP, fair price, resale value, warranty, EV range): https://www.kbb.com/ferrari/sf90/2024/",
    "AutoMonitor, How much does a Ferrari SF90 Stradale cost? (estimates, no sources listed): https://automonitor.io/blog/how-much-does-a-ferrari-sf90-stradale-cost/",
    "CarGurus, 2023 Ferrari SF90 review and pricing: https://www.cargurus.com/research/2023-Ferrari-SF90-c32760",
    "U.S. Census Bureau, Income in the United States: 2023: https://www.census.gov/library/publications/2024/demo/p60-282.html",
    "KTVU / Fox, How much the typical American household earned in 2023 (Census data): https://ktvu.com/news/how-much-american-household-earned-2023-census",
    "ClubAlfa, A Ferrari SF90 Stradale crash has become one of the most costly ever (Mar 2024): https://www.clubalfa.it/en/a-ferrari-sf90-stradale-crash-has-become-one-of-the-most-costly-ever-2625",
    "Ferrari, Warranty and maintenance (Genuine Maintenance, Power16): https://www.ferrari.com/en-US/auto/car-part-services-warranty-maintenance",
    "Bloomberg, Ferrari plans $7,500 hybrid, EV battery service subscription (June 2024): https://www.bloomberg.com/news/articles/2024-06-26/ferrari-plans-7-500-hybrid-ev-battery-service-subscription",
    "ClubAlfa, Ferrari offers up to 16 years of warranty for its hybrids (July 2024): https://www.clubalfa.it/en/ferrari-offers-up-to-16-years-of-warranty-for-its-hybrids-and-8-for-electric-cars-6380",
    "InsideEVs, SF90 Stradale is Ferrari's first plug-in hybrid: https://insideevs.com/news/352375/sf90-stradale-first-ferrari-plugin-hybrid/",
    "Motor Authority, Ferrari SF90 recalled (Oct 2023): https://www.motorauthority.com/news/1141294_ferrari-sf90-recalled",
    "Reuters via Euronews, Ferrari accelerates its move into hybrid cars (May 2019): https://www.euronews.com/2019/05/29/ferrari-accelerates-its-move-into-hybrid-cars",
    "Evo India, SF90 XX Stradale revealed: https://www.evoindia.com/top-news/new-ferrari-sf90-xx-stradale-revealed",
    "Carwow Spain, Ferrari 296 GTB vs McLaren Artura (June 2021): https://www.carwow.es/blog/comparativa-ferrari-296-gtb-vs-mclaren-artura",
    "Motoring Research, Ferrari 849 Testarossa (Sept 2025): https://www.motoringresearch.com/car-news/2026-ferrari-849-testarossa/",
], "C")
