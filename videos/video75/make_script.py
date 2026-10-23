import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Chevrolet Corvette Z06 is often called a supercar for the price of a sports car. Six hundred seventy horsepower, a hand-built engine, and a starting price around one hundred twenty thousand dollars. But what does it really cost to own one? Not just to buy it, but to insure it, fuel it, maintain it, and eventually sell it?""",
   "Chevrolet Corvette Z06", "WHAT A Z06 REALLY COSTS")
sc("""The answer has a twist. For some early buyers, the most expensive part of owning a Z06 was not fuel or tires. It was a decision they made at the dealership, before they ever drove the car. We will show you exactly what happened, with real auction results.""",
   "Corvette Z06 dealership", "THE MOST EXPENSIVE DECISION")
sc("""We will also look at the hidden tax on every Z06, the five-hundred-mile rule for new owners, the insurance numbers, and the recall that stopped sales in twenty twenty-five. Every number comes from a published source, listed in the description. Where a figure is an estimate or our own arithmetic, we will say so.""",
   "Corvette Z06 engine", "EVERY NUMBER IS SOURCED")
sc("""First, what you are buying. The Z06's five point five liter L T six V8 makes six hundred seventy horsepower, The Drive reported, and Chevrolet claims zero to sixty miles per hour in two point six seconds. Hagerty called it the most powerful naturally aspirated production V8 ever.""",
   "Corvette Z06 LT6", "670 HP, 0-60 IN 2.6 s")

# ---------- 1. THE PRICE ----------
ch("The sticker price")
sc("""Let's start with the sticker. Hagerty reported that the twenty twenty-three Z06 had a base price of about one hundred nine thousand three hundred dollars, including the gas guzzler charge, and that the twenty twenty-three model year sold out. By twenty twenty-six, GM Authority reported a base price of about one hundred nineteen thousand seven hundred dollars for the Z06 coupe, including destination.""",
   "Corvette Z06 window sticker", "$109,275 TO $119,695")
sc("""That is about ten thousand dollars more in three years. And that is the cheapest Z06 you can order. The options list is where the price climbs fast.""",
   "Corvette Z06 configurator", "+$10,000 IN THREE YEARS")
sc("""It helps to see how far the price has come. Hagerty reported that the original nineteen sixty-three Z06 racing package cost about one thousand eight hundred eighteen dollars on a coupe. The C six Z06 of twenty oh six started at about sixty-five thousand eight hundred dollars, and the C seven Z06 of twenty fifteen at about seventy-nine thousand. Now it is close to one hundred twenty thousand.""",
   "Corvette C6 Z06 and C7 Z06", "$65,800 (2006) TO $119,695 (2026)")
sc("""And the Z06 is not the only C eight Corvette. GM Authority listed twenty twenty-six prices of about seventy-two thousand dollars for the Stingray, and about one hundred eleven thousand for the hybrid, all-wheel-drive E Ray. So the Z06 costs about forty-eight thousand dollars more than a base Stingray. That premium buys the hand-built L T six and the wider body.""",
   "Corvette Stingray and E-Ray", "STINGRAY ~$72K, E-RAY ~$111K")
sc("""AutoMonitor, a valuation site, says the Z zero seven performance package costs about eight thousand nine hundred dollars, and includes carbon-ceramic brakes and track-focused tuning. Carbon fiber wheels, a carbon aero package, and premium interiors add more. AutoMonitor puts a loaded Z06 at about one hundred forty thousand to one hundred sixty thousand dollars.""",
   "Corvette Z06 Z07 package", "Z07: ~$8,900")
sc("""CarScoops gave a real example. A twenty twenty-five Z06 convertible with the Z zero seven package, carbon aero, carbon-ceramic Brembo brakes, a front lift system, and forged wheels had a sticker price of about one hundred sixty-nine thousand nine hundred dollars. That is about fifty thousand dollars above the base coupe.""",
   "Corvette Z06 convertible", "LOADED: ~$169,875")
sc("""So the real range for a new Z06 runs from about one hundred twenty thousand to about one hundred seventy thousand dollars. For this video, let's use one hundred forty thousand as a typical, well-equipped example. Then we add the costs nobody puts on the window sticker.""",
   "Corvette Z06 Torch Red", "OUR EXAMPLE: $140,000")

# ---------- 2. THE HIDDEN TAX ----------
ch("The hidden tax")
sc("""Here is the first hidden cost. Every Z06 carries a federal gas guzzler tax, a charge the United States applies to cars that use too much fuel. GM Authority reported that the twenty twenty-four Z06 paid two thousand six hundred dollars without the carbon aero package, and three thousand dollars with it. For twenty twenty-five, every Z06 paid three thousand dollars.""",
   "Corvette Z06 window sticker gas guzzler", "GAS GUZZLER TAX: $3,000")
sc("""Why? GM Authority listed the twenty twenty-five Z06 at twelve miles per gallon in the city, twenty on the highway, and fourteen combined, according to the E P A. A high-revving, naturally aspirated V8 with five point five liters is thirsty, and the tax is the government's way of saying so.""",
   "Corvette Z06 fuel gauge", "12 CITY / 20 HWY / 14 COMBINED")
sc("""Then comes sales tax, which depends on the state. Here is our own example. At a seven percent rate, a one hundred forty thousand dollar Z06 would carry about nine thousand eight hundred dollars in sales tax. Add registration, and a buyer could easily be past one hundred fifty thousand dollars before driving away.""",
   "sales tax receipt", "EXAMPLE: ~$9,800 SALES TAX")
sc("""What about financing? Here is another example using our own arithmetic. Put twenty percent down on a one hundred forty thousand dollar Z06, which is twenty-eight thousand dollars, and borrow one hundred twelve thousand over six years at an assumed seven percent interest rate. The monthly payment would be about one thousand nine hundred dollars.""",
   "car loan paperwork", "LOAN EXAMPLE: ~$1,900/MONTH")
sc("""Over six years, you would pay about one hundred thirty-seven thousand dollars on that loan, which means about twenty-five thousand dollars in interest alone. Interest is a real cost of ownership that many people forget to count. Paying cash avoids it, but most buyers do not pay cash for a car like this.""",
   "Corvette Z06 keys", "~$25,000 IN INTEREST (EXAMPLE)")

# ---------- 3. THE MARKUP TWIST ----------
ch("The markup trap")
sc("""Now the twist from the start of this video. When the Z06 launched, demand was enormous, and dealers knew it. AutoMonitor says markups in twenty twenty-three and twenty twenty-four ran from about thirty thousand to one hundred thousand dollars over sticker. CarScoops said that not long ago, dealers were asking tens of thousands over sticker.""",
   "Corvette Z06 dealer markup", "MARKUPS: $30K-$100K")
sc("""Then the market turned. In August twenty twenty-five, Motorious reported that GM's own inventory tracker showed about one thousand seven hundred Z06s sitting at American dealers, with discounts of up to twelve thousand dollars. One example was a Riptide Blue coupe with a sticker of about one hundred nineteen thousand eight hundred dollars, listed at about one hundred seven thousand five hundred.""",
   "Corvette dealership lot", "2025: UP TO $12,000 OFF")
sc("""Think about what that means. A buyer who paid fifty thousand dollars over sticker in twenty twenty-three, and a buyer who got twelve thousand dollars off in twenty twenty-five, could own almost identical cars. The difference between them would be more than sixty thousand dollars. That is the most expensive decision a Z06 owner can make.""",
   "two Corvette Z06 cars", "A $60,000 DIFFERENCE")
sc("""And it gets worse on resale. CarScoops reported a Z06 coupe with an original sticker of about one hundred forty-six thousand dollars and two thousand one hundred miles that sold on Bring a Trailer for one hundred eighteen thousand. A Z06 convertible with a sticker of about one hundred thirty-nine thousand and one thousand miles sold for one hundred twelve thousand.""",
   "Corvette Z06 auction Bring a Trailer", "$146K STICKER, $118K SALE")
sc("""Both of those are about twenty percent below the original sticker price, with almost no miles on the cars. If either owner had paid a markup on top of that, the loss would have been far bigger. CarScoops even described flippers learning the hard way what happens when the hype fades.""",
   "Corvette Z06 for sale", "~20% BELOW STICKER")
sc("""CarScoops added another example in October twenty twenty-five. A twenty twenty-five Z06 convertible with the Z zero seven package and one thousand three hundred miles, originally delivered to a dealer in North Carolina in late twenty twenty-four, sold on Bring a Trailer for one hundred thirty-seven thousand five hundred dollars. Its sticker had been about one hundred sixty-nine thousand nine hundred. That is a loss of about thirty-two thousand dollars in less than a year, by our own arithmetic.""",
   "Corvette Z06 convertible auction", "-$32,000 IN UNDER A YEAR")

# ---------- 4. DEPRECIATION ----------
ch("Depreciation")
sc("""So how much value does a Z06 lose over time? CarEdge, a car-buying site, estimates that a typically equipped new Z06, at about one hundred twenty-seven thousand dollars, will lose about sixty-five thousand eight hundred dollars in five years. That leaves an estimated value of about sixty-one thousand five hundred.""",
   "Corvette Z06 used", "5-YEAR LOSS: ~$65,838 (EST.)")
sc("""Put another way, using our own arithmetic, sixty-five thousand eight hundred dollars over five years is about one thousand one hundred dollars a month, just in lost value. That is more than the monthly payment on many new family cars, and the owner pays it whether the Z06 is driven or sitting in the garage.""",
   "Corvette Z06 garage parked", "~$1,100/MONTH IN LOST VALUE")
sc("""That is a loss of about fifty-two percent in five years, by CarEdge's estimate. CarEdge's model assumes fifteen thousand miles a year, which is a lot for a car like this. Owners who drive less may lose less. But the auction results we just saw show that even nearly new cars were selling well below sticker.""",
   "Corvette Z06 odometer", "ABOUT 52% IN FIVE YEARS")
sc("""Not every estimate is that gloomy. AutoMonitor projects that a Z06 bought at sticker might lose fifteen to twenty-five percent over five years once supply normalizes. These estimates are very different, which tells you something important. Nobody knows exactly where Z06 values will settle.""",
   "Corvette Z06 parked", "ESTIMATES: 15% TO 52%")
sc("""Here is the twist. Depreciation hurts the first owner, but it helps the second. If you buy a two-year-old Z06 at twenty percent below sticker, someone else has already paid for the biggest drop. For a used buyer, the Z06 can be one of the best performance bargains on the market.""",
   "used Corvette Z06 dealer", "GOOD NEWS FOR USED BUYERS")

# ---------- 5. INSURANCE ----------
ch("Insurance")
sc("""Next, insurance. CarEdge estimates about three thousand four hundred twenty-six dollars a year to insure a Z06, or about seventeen thousand one hundred dollars over five years. That estimate assumes a forty-year-old driver with full coverage, a good record, and good credit.""",
   "Corvette Z06 insurance", "INSURANCE: ~$3,426/YEAR (EST.)")
sc("""AutoMonitor gives a range of about two thousand five hundred to four thousand five hundred dollars a year. A younger driver, a city address, or a speeding ticket could push it much higher. But compared with many exotic cars, the Z06 is relatively affordable to insure, partly because Chevrolet parts and dealers are everywhere.""",
   "Chevrolet dealer service", "~$2,500-$4,500 RANGE")
sc("""That is one of the Corvette's quiet advantages. You can take it to a Chevrolet dealer in almost any American town. That network makes repairs easier to find, and it helps keep costs closer to normal cars than to Italian supercars.""",
   "Chevrolet dealership sign", "A DEALER IN EVERY TOWN")
sc("""The jump from older Z06s is still noticeable. AutoMonitor estimates about one thousand two hundred to two thousand dollars a year to insure a C seven Z06, and about two thousand five hundred to four thousand five hundred for a C eight. More power, a higher price, and newer, more expensive parts all push the premium up.""",
   "Corvette C7 Z06 and C8 Z06", "C8 INSURANCE: ~2X THE C7")

# ---------- 6. RUNNING COSTS ----------
ch("Fuel, tires, and brakes")
sc("""Now the running costs. Fuel first. With a combined rating of fourteen miles per gallon, here is our own example. Drive eight thousand miles a year and you would use about five hundred seventy gallons. At an assumed four dollars a gallon for premium, that is about two thousand three hundred dollars a year.""",
   "gas station premium fuel", "FUEL: ~$2,300/YEAR (EXAMPLE)")
sc("""Tires are next. The Z06 uses very wide tires. The Drive reported rear tires three hundred forty-five millimeters wide, and Hagerty said the standard tires are Michelin Pilot Sport four S, with stickier Michelin Cup two R tires on the Z zero seven. AutoMonitor estimates about one thousand five hundred to two thousand five hundred dollars a year for tires, spread out over time.""",
   "Corvette Z06 rear tire", "TIRES: ~$1,500-$2,500/YEAR (EST.)")
sc("""Brakes depend on how you drive. AutoMonitor estimates one thousand two hundred to two thousand dollars a year for brakes and pads. And if you drive on track days, everything wears faster. Tires that last years on the street can be finished in a few weekends at a circuit.""",
   "Corvette Z06 brakes", "BRAKES: ~$1,200-$2,000/YEAR (EST.)")
sc("""Maintenance has good news. Autoblog reported that GM says the L T six's valvetrain, with titanium intake valves and sodium-filled exhaust valves, never needs adjustment or maintenance over the engine's life. Some exotic engines need expensive valve adjustments. The Z06 does not.""",
   "Corvette LT6 valvetrain", "NO VALVE ADJUSTMENTS")
sc("""CarEdge estimates about three thousand two hundred fifty dollars in maintenance and repairs over the first five years. AutoMonitor estimates five hundred to eight hundred dollars a year for oil and fluids. Either way, routine maintenance is the smallest part of the bill.""",
   "Corvette oil change", "MAINTENANCE: ~$3,250 / 5 YEARS (EST.)")
sc("""AutoMonitor also adds up the yearly running costs for a C eight Z06 driven under ten thousand miles a year. Insurance, oil and fluids, tires, brakes, fuel, and registration come to about seven thousand eight hundred to fourteen thousand five hundred dollars a year, by its estimate. AutoMonitor does not name a source for these figures, so treat them as a rough guide.""",
   "Corvette Z06 garage", "~$7,800-$14,500/YEAR (EST.)")

# ---------- 7. THE OWNER RULES ----------
ch("The owner's rules")
sc("""There are also some rules for new owners. Autoblog reported that every L T six engine has a five-hundred-mile break-in period, with torque limited in first and second gear. So for the first five hundred miles, you cannot use all six hundred seventy horsepower.""",
   "Corvette Z06 tachometer", "500-MILE BREAK-IN")
sc("""Autoblog also said each engine is built by a single technician at Chevrolet's Performance Build Center in Bowling Green, Kentucky, in about three hours, and gets a twenty-minute full-load test. If you ever need engine work, you are dealing with a hand-built, race-derived engine. That is part of what you pay for.""",
   "Corvette engine builder", "A HAND-BUILT ENGINE")
sc("""And there was a recall. In August twenty twenty-five, Auto123 reported that about twenty-five thousand Corvettes, including twenty twenty-three to twenty twenty-five Z06 models, were recalled because fuel could spill onto the left radiator during refueling, creating a fire risk. Sales were suspended while GM worked on a fix. Recall repairs are free, but they can mean time without the car.""",
   "Corvette Z06 fuel filler", "RECALL: ~25,000 CARS")

# ---------- 8. THE FULL BILL ----------
ch("The full bill")
sc("""So let's add it up for five years, using the estimates we have seen. This is a rough example, not a quote. Depreciation, by CarEdge's estimate, about sixty-five thousand dollars. Insurance, about seventeen thousand. Maintenance and repairs, about three thousand two hundred fifty.""",
   "Corvette Z06 calculator", "5-YEAR EXAMPLE")
sc("""Fuel, at our example of two thousand three hundred a year, about eleven thousand five hundred. Tires and brakes, using AutoMonitor's lower estimates, about thirteen thousand five hundred over five years. Then sales tax and registration on top.""",
   "Corvette Z06 fuel and tires", "FUEL + TIRES + BRAKES")
sc("""Put it together, and the cost of owning a new Z06 for five years could be roughly one hundred ten thousand to one hundred twenty thousand dollars, by our own arithmetic, with depreciation as the biggest part. That is close to the price of the car itself.""",
   "Corvette Z06 night", "~$110K-$120K OVER 5 YEARS")
sc("""Here is one more way to look at it, again our own arithmetic. If you drive eight thousand miles a year, five years adds up to forty thousand miles. Divide about one hundred fifteen thousand dollars of costs by forty thousand miles, and every mile in the Z06 costs close to three dollars. For a car that reaches sixty in two point six seconds, some owners will say that is a fair price.""",
   "Corvette Z06 highway", "~$3 PER MILE (EXAMPLE)")
sc("""For comparison, the U S Census Bureau reported a median household income of about eighty thousand six hundred dollars in twenty twenty-three. So five years of Z06 ownership could cost about one and a half years of a typical household's total income. Expensive, but far less than most exotic cars.""",
   "American suburb", "~1.5 YEARS OF MEDIAN INCOME")

# ---------- 9. VERSUS THE RIVALS ----------
ch("Compared with the rivals")
sc("""How does that compare with the Z06's famous rival, the Porsche nine eleven G T three R S? The Drive reported a starting price of about two hundred twenty-five thousand dollars for the twenty twenty-three G T three R S, close to twice the Z06's base price.""",
   "Porsche 911 GT3 RS", "GT3 RS: ~$225,250")
sc("""But here is the twist. The Porsche often holds its value. CarScoops reported a twenty twenty-four G T three R S with an original sticker of about three hundred nine thousand dollars that sold for three hundred fifty-one thousand, about forty-two thousand dollars above sticker. So the more expensive car to buy can be cheaper to own, if it holds its value and you can get one at sticker.""",
   "Porsche 911 GT3 RS auction", "SOLD ABOVE STICKER")
sc("""That is the strange economics of performance cars. The purchase price is only half the story. What matters is the gap between what you pay and what you get back. For the Z06, that gap has been large. For the most limited Porsches, it can even be negative.""",
   "Porsche and Corvette parked", "WHAT YOU GET BACK")
sc("""There is also a cheaper way into the Z06 name. Older generations cost far less. AutoMonitor lists early C seven Z06s, from twenty fifteen and twenty sixteen with forty thousand to sixty thousand miles, at about fifty-five thousand to seventy thousand dollars. That car had a supercharged six hundred fifty horsepower V8, according to Hagerty.""",
   "Corvette C7 Z06", "C7 Z06: ~$55K-$70K USED")
sc("""Go back further and the prices drop again. AutoMonitor lists early C six Z06s, with the seven liter, five hundred five horsepower V8, at about forty thousand to fifty-five thousand dollars. And the original C five Z06 from two thousand one, with three hundred eighty-five horsepower at launch, at about twenty-five thousand to thirty-five thousand.""",
   "Corvette C5 Z06", "C5 Z06: ~$25K-$35K USED")
sc("""AutoMonitor also estimates lower running costs for the older cars. For a C seven Z06, about five thousand one hundred to eight thousand seven hundred dollars a year. For a C five, about three thousand three hundred to five thousand seven hundred. Older cars may need more repairs as they age, but insurance and depreciation are usually lower.""",
   "Corvette C5 and C6", "OLDER Z06: LOWER COSTS")
sc("""So the real question is what you want. The C eight Z06 is the newest, the fastest, and the only Z06 with a hand-built, flat-plane V8 behind the seats. But if you want the Z06 badge and a lot of power for far less money, an older generation can cost a fraction of the price.""",
   "Corvette Z06 generations lineup", "WHICH Z06 DO YOU WANT?")

# ---------- 10. THE ANSWER ----------
ch("The answer")
sc("""So what does it really cost to own a Corvette Z06? Around one hundred twenty thousand to one hundred seventy thousand dollars to buy, plus a gas guzzler tax of about three thousand, plus roughly one hundred ten thousand to one hundred twenty thousand over five years in depreciation and running costs, using the estimates in this video.""",
   "Corvette Z06", "THE REAL COST")
sc("""The biggest cost is not fuel, tires, or insurance. It is depreciation. And the biggest mistake an owner could make was paying a huge markup when the hype was at its peak. If you buy a Z06 at the right price, or buy one used, it can be one of the most affordable ways to own a race-derived, hand-built V8.""",
   "Corvette Z06 Torch Red", "BUY AT THE RIGHT PRICE")
sc("""Would you buy a new Z06, or wait for a used one? Tell us in the comments. In the other videos of this series, we reveal two things you didn't know about the Z06, compare it with the Porsche nine eleven G T three R S, and tell the insane story behind the mid-engine Corvette.""",
   "Corvette Z06 convertible", "NEW OR USED?")
sc("""And if you are budgeting for a truck instead, our twenty twenty-seven Truck Buyer's Guide is linked in the description, with real numbers on the trucks most people buy. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "pickup truck dealership", "SUBSCRIBE: PICKUP REALITY")

save("video75", "What It Really Costs to Own a Corvette Z06", [
    "The Drive, 2023 Chevy Corvette Z06: 670 hp from a naturally aspirated flat-plane V8: https://www.thedrive.com/news/42882/2023-chevy-corvette-z06-670-hp-from-a-naturally-aspirated-flat-plane-v8",
    "Hagerty, How the Corvette Z06 went from '60s racing package to modern monster: https://hagerty.com/media/?p=257365",
    "Hagerty, 2023 Corvette Z06 arrives: https://www.hagerty.com/media/?p=179871",
    "GM Authority, 2026 Corvette pricing uncovered: https://gmauthority.com/blog/2025/06/2026-corvette-pricing-uncovered/",
    "GM Authority, 2025 Corvette Z06 gets revised fuel economy ratings (Sept 2024): https://gmauthority.com/blog/2024/09/2025-corvette-z06-gets-revised-fuel-economy-ratings/",
    "AutoMonitor, How much does a Corvette Z06 actually cost? (estimates): https://automonitor.io/blog/how-much-does-a-chevrolet-corvette-z06-cost/",
    "CarEdge, Corvette Z06 cost to own (estimates): https://caredge.com/chevrolet/corvette-z06/costs",
    "Motorious, Over 1,700 Corvette Z06s sit unsold (Aug 2025): https://www.motorious.com/articles/news/dealers-offer-deep-discounts-as-over-1-700-chevrolet-corvette-z06s-sit-unsold",
    "CarScoops, Corvette Z06 prices crashing on the used market (Aug 2025): https://www.carscoops.com/2025/08/corvette-z06-prices-crashing-used-market-losses/",
    "CarScoops, Corvette Z06 flippers learn what happens when the hype fades (Oct 2025): https://www.carscoops.com/2025/10/corvette-z06-flippers-are-learning-the-hard-way-what-happens-when-the-hype-fades/",
    "Autoblog, 2023 Chevy Corvette Z06: the 9 coolest things: https://www.autoblog.com/2022/02/18/2023-chevy-corvette-z06-coolest-9-things/",
    "Auto123, Corvette Z06 and ZR1 recall (Aug 2025): https://www.auto123.com/en/news/chevrolet-corvette-recall-z06-zr1/73126",
    "KTVU / Fox, Census 2023 median household income: https://ktvu.com/news/how-much-american-household-earned-2023-census",
    "The Drive, 2023 Porsche 911 GT3 RS specs and price: https://www.thedrive.com/news/2023-porsche-911-gt3rs-specs-debut-reveal-price.md",
    "CarScoops, Porsche 911 GT3 RS sold for $40k profit (May 2025): https://www.carscoops.com/2025/05/this-porsche-911-gt3-rs-was-sold-for-40k-profit-after-1-4k-miles/",
], "C")
