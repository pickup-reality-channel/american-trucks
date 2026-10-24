import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""A new Lamborghini Urus costs two hundred seventy-six thousand, seven hundred forty-one dollars, according to CARFAX. A used one from twenty nineteen has a median asking price of about one hundred sixty-eight thousand dollars. So the question is not whether you can afford the car. The question is what it costs you after the keys are in your hand. This is what the sources say about the real cost of owning a Lamborghini Urus.""",
   "Lamborghini Urus", "THE REAL COST OF A LAMBORGHINI URUS")
sc("""Here is the twist. The used price does not fall the way most people assume. The median asking price rises with every model year, and the newest cars are the most expensive. And the one cost that every source agrees on is the one nobody puts in the advert. We will go through all of it, and tell you what we could not find.""",
   "Lamborghini Urus used", "THE USED PRICE DOES NOT FALL THE WAY YOU THINK")
sc("""Every figure comes from a published source, listed in the description. Where a source is only an estimate, we label it as an estimate. Where we do the maths ourselves, we say so. We have not owned an Urus, and we will not invent costs we cannot source.""",
   "Lamborghini Urus", "EVERY NUMBER IS SOURCED")

ch("What it costs new")
sc("""CARFAX lists a starting M S R P of two hundred seventy-six thousand, seven hundred forty-one dollars for the twenty twenty-six Lamborghini Urus S E. That is the only trim CARFAX lists for that year. The S and the Performante, which were the earlier versions, are no longer offered, according to the same page.""",
   "2026 Lamborghini Urus SE", "2026 URUS SE · MSRP $276,741 (CARFAX)")
sc("""Premier Auto Miami, a rental company, gives estimates for the earlier cars. It puts the base Urus at roughly two hundred forty-one thousand, eight hundred dollars, and the S E at about two hundred sixty-two thousand, six hundred thirty. It says a loaded car can reach three hundred to three hundred forty thousand. These are estimates from a commercial page, not the manufacturer.""",
   "Lamborghini Urus price", "ESTIMATES: BASE ~$241.8K · SE ~$262.6K · LOADED $300–340K")
sc("""Motor1, reporting on the Ferrari Purosangue, described a standard Urus as costing roughly one hundred seventy thousand dollars less than the Ferrari's three hundred ninety-three thousand, three hundred fifty. By our own arithmetic, that suggests a base price near two hundred twenty-three thousand at the time. Prices have moved since then, and the twenty twenty-six car is more expensive.""",
   "Lamborghini Urus", "OUR ARITHMETIC: ~$223K AT THE TIME OF THAT REPORT")
sc("""Options matter. Premier Auto Miami says the range between a base car and a loaded one is around sixty to one hundred thousand dollars, by our arithmetic, comparing its base estimate with its loaded range. That is more than many people pay for an entire car. And options are also what you pay for twice, because they decide what the car is worth later.""",
   "Lamborghini Urus interior", "BASE TO LOADED: ~$58K–$98K (OUR ARITHMETIC)")

ch("What it costs used")
sc("""VinAssessment analysed eight hundred forty-eight dealer asking prices on the twenty-second of October, twenty twenty-six. The medians by model year are as follows. Twenty nineteen, one hundred sixty-eight thousand, six hundred ninety-six dollars. Twenty twenty, one hundred seventy-nine thousand, nine hundred ninety-seven. Twenty twenty-one, one hundred ninety-four thousand, nine hundred ninety.""",
   "Lamborghini Urus used", "MEDIAN ASKING: 2019 $168,696 · 2020 $179,997 · 2021 $194,990")
sc("""Twenty twenty-two, two hundred twelve thousand, nine hundred ninety-nine. Twenty twenty-three, two hundred fifty-three thousand, one hundred twelve. Twenty twenty-four, two hundred seventy-nine thousand, five hundred sixty-seven. Twenty twenty-five, two hundred ninety-five thousand, three hundred sixty-six. And twenty twenty-six, three hundred thirty-seven thousand, seven hundred twenty-five.""",
   "Lamborghini Urus dealership", "2022 $212,999 · 2023 $253,112 · 2024 $279,567 · 2025 $295,366 · 2026 $337,725")
sc("""By our own arithmetic, the median for a twenty twenty-five car is about fifteen percent below the twenty twenty-six median. And the twenty nineteen car, the oldest, is about half of the twenty twenty-six figure. So each year of age is worth roughly ten to fifteen percent less, as a rough average. These are asking prices, not what buyers actually paid.""",
   "Used car prices", "ASKING PRICES, NOT SALE PRICES")
sc("""One caution. The twenty twenty-six figure includes the plug-in hybrid, which is a different and more expensive car than the earlier ones. So the step between twenty twenty-five and twenty twenty-six partly reflects a change in the model, not only age. That is why comparing across years can mislead, and why we call these medians directional.""",
   "Lamborghini Urus SE", "2026 MEDIAN INCLUDES THE PLUG-IN HYBRID")
sc("""What does the gap mean for a buyer? By our arithmetic, a twenty twenty-three car asking two hundred fifty-three thousand sits only about twenty-three thousand dollars below the two hundred seventy-six thousand M S R P of a new twenty twenty-six S E. A three-year-old Urus saves you far less than you might expect.""",
   "Lamborghini Urus", "A 2023 URUS ASKS ONLY ~$23K LESS THAN A NEW SE (OUR ARITHMETIC)")

ch("Insurance and fuel")
sc("""Premier Auto Miami estimates insurance at five thousand to ten thousand dollars or more a year. It is a rough range from a rental company. The real figure depends on your age, your record, your state and your insurer. We found no independent source that gives an average, so please treat this as an order of magnitude only.""",
   "Insurance", "INSURANCE EST.: $5,000–$10,000+ A YEAR")
sc("""On fuel, CARFAX lists the twenty twenty-six S E at forty-eight miles per gallon equivalent combined, and twenty miles per gallon using petrol alone. It has a thirty-five mile electric range. The same page says the car has five seats and sixteen cubic feet of cargo space. Premier Auto Miami adds that the car needs high-octane petrol.""",
   "Lamborghini Urus SE fuel", "SE: 48 MPGE · 20 MPG ON PETROL · 35 MILES ELECTRIC")
sc("""A rough calculation, our own arithmetic. At twenty miles per gallon, twelve thousand miles a year uses six hundred gallons. At an assumed four dollars a gallon, which is our own assumption and not a sourced price, that is two thousand, four hundred dollars. With the battery used for some of those miles, the cost would be lower. Change the price, and the result changes.""",
   "Petrol pump", "12,000 MILES AT 20 MPG = 600 GALLONS (OUR ARITHMETIC)")

ch("Reliability and recalls")
sc("""Wikipedia lists two Urus recalls. In November twenty twenty, two thousand, eight hundred thirty-one vehicles were recalled for a fuel line issue. In May twenty twenty-four, two thousand, one hundred thirty-three vehicles were recalled because of rivets in the hood latch. Recalls are repaired by the manufacturer at no cost, but you must have the work done.""",
   "Lamborghini Urus recall", "RECALLS: NOV 2020 (2,831) · MAY 2024 (2,133)")
sc("""We found no dependable source for average repair costs. Premier Auto Miami says maintenance on an exotic costs more than on an ordinary car, but gives no figure we could verify. We will not invent one. Our advice is simply to ask for the full service history, and to ask a franchised Lamborghini dealer to price any work before you buy.""",
   "Mechanic", "WE FOUND NO RELIABLE REPAIR-COST FIGURE")
sc("""Here is what is true about the engine. Wikipedia says it is a four litre twin-turbo V eight from Audi, built in Hungary, and the platform is shared with the Audi Q seven, Bentley Bentayga, Porsche Cayenne and Volkswagen Touareg. That does not make parts cheap, but it does mean the underlying hardware is used across a very large number of cars.""",
   "Lamborghini Urus engine", "SHARED PLATFORM: MLB EVO")

ch("Depreciation, put together")
sc("""Let us put the numbers together, as our own arithmetic. A new twenty twenty-six S E lists at two hundred seventy-six thousand. A median twenty twenty-five car asks two hundred ninety-five thousand, which is higher than that list price, because the median includes optioned cars and dealer premiums. So the used market does not fit a simple depreciation story.""",
   "Lamborghini Urus", "A 2025 MEDIAN ASKS MORE THAN THE 2026 SE'S LIST PRICE")
sc("""The oldest cars show the pattern better. The twenty nineteen median is one hundred sixty-eight thousand. If a base car cost around two hundred twenty-three thousand at the time, as our arithmetic suggested, that is about a quarter off over seven years. But the starting price in twenty nineteen is not in our sources, so treat that as a rough guide only.""",
   "Lamborghini Urus 2019", "2019: ~$169K MEDIAN ASKING")
sc("""Production helps explain it. Wikipedia lists seven thousand, two hundred sixty-five Urus built in twenty twenty-five and forty-three thousand, two hundred fifty-four in total since twenty seventeen, by our arithmetic. A car built in numbers that large is not rare. That limits how much a used Urus can rise, and it means you can compare many cars before you buy.""",
   "Lamborghini Urus production", "43,254 BUILT SINCE 2017 (OUR SUM OF WIKIPEDIA'S FIGURES)")


ch("What you are actually buying")
sc("""Before the money, the car. Wikipedia says the Urus concept was shown at the Beijing motor show on the twenty-third of April, twenty twelve, with a five point two litre V ten from the Gallardo, six hundred metric horsepower and all-wheel drive. That V ten never reached production. The production car, unveiled on the fourth of December, twenty seventeen, got a V eight instead.""",
   "Lamborghini Urus concept", "2012 CONCEPT: V10 · 2017 PRODUCTION CAR: V8")
sc("""The production car was designed by Mitja Borkert, building on the concept by Filippo Perini, according to Wikipedia. Deliveries began in early twenty eighteen, with a target of about three thousand, five hundred cars a year. By our arithmetic, in twenty twenty-five the factory built more than twice that target, which tells you how many are out there to buy.""",
   "Mitja Borkert", "DESIGNED BY MITJA BORKERT")
sc("""The base engine is a four litre twin-turbo V eight. Wikipedia lists six hundred fifty metric horsepower at six thousand r p m and eight hundred fifty newton-metres from two thousand, two hundred fifty to four thousand, five hundred r p m. The same page says it is uprated by a hundred metric horsepower and eighty newton-metres over the Porsche Cayenne Turbo's version.""",
   "Lamborghini Urus engine", "650 PS · 850 NM · 4.0 L TWIN-TURBO V8")
sc("""Performance claims, again from Wikipedia. Zero to a hundred kilometres per hour in three point six seconds, zero to two hundred in twelve point eight, and a top speed of about three hundred five or three hundred six kilometres per hour, depending on the page. The weight is listed as under two thousand, two hundred kilograms. These are manufacturer claims, not our tests.""",
   "Lamborghini Urus acceleration", "0–100 KM/H: 3.6 S · 0–200: 12.8 S")
sc("""The Performante version, Wikipedia says, adds sixteen metric horsepower for six hundred sixty-six, cuts forty-seven kilograms, and claims three point three seconds to a hundred. The S T-X, a track-focused model, is described as twenty-five percent lighter. These are the cars that the used market lists at premiums, and CARFAX says the Performante is no longer sold new.""",
   "Lamborghini Urus Performante", "PERFORMANTE: 666 PS · 47 KG LIGHTER · 3.3 S")
sc("""The newest car is the S E, a plug-in hybrid. Wikipedia lists a V eight at six hundred twenty horsepower plus an electric motor of one hundred eighty-nine, for seven hundred ninety-nine horsepower in total, with nine hundred fifty newton-metres and a twenty-five point nine kilowatt-hour battery. CARFAX gives seven hundred eighty-nine horsepower. The two sources disagree by ten.""",
   "Lamborghini Urus SE", "SE: 799 HP (WIKIPEDIA) VS 789 HP (CARFAX)")
sc("""The extra hardware has a price in weight. Wikipedia says the S E is about three hundred kilograms heavier than the earlier car, because of the battery and motor. In exchange, it claims zero to a hundred in three point four seconds and a top speed of three hundred twelve kilometres per hour. By our arithmetic, that is a faster car, but one carrying an extra three hundred kilograms.""",
   "Lamborghini Urus SE battery", "+300 KG FOR THE BATTERY")

ch("The people who sold it, and the numbers behind it")
sc("""Lamborghini's own growth tells you what the owner community looks like. Company deliveries were three thousand, eight hundred fifteen in twenty seventeen, and ten thousand, seven hundred forty-seven in twenty twenty-five. Carscoops reported that in twenty nineteen the Urus was four thousand, nine hundred sixty-two cars, or sixty-one percent of the company's sales that year.""",
   "Lamborghini sales", "2019: URUS = 61% OF LAMBORGHINI SALES")
sc("""That matters to a buyer for a practical reason. When a car is sixty-one percent of a company's sales, the company has every reason to keep supporting it. Dealers see it every day, and technicians are trained on it. We cannot prove that this lowers your repair bill, and no source we found says so. But it is a reason to expect that help exists.""",
   "Lamborghini dealership", "A BIG-SELLER MEANS WELL-KNOWN CAR (OUR REASONING)")
sc("""Wikipedia lists the Urus build numbers by year. One hundred twenty-one in twenty seventeen. Two thousand, five hundred sixty-five in twenty eighteen. Five thousand, two hundred thirty-three in twenty nineteen. Four thousand, three hundred sixty-four in twenty twenty. Five thousand, two hundred forty in twenty twenty-one. Five thousand, seven hundred eighty-five in twenty twenty-two. Six thousand in twenty twenty-three. Six thousand, six hundred eighty-one in twenty twenty-four.""",
   "Lamborghini Urus production", "URUS BUILT: 121 · 2,565 · 5,233 · 4,364 · 5,240 · 5,785 · 6,000 · 6,681")
sc("""There is a lesson in the dip. Production fell from five thousand, two hundred thirty-three in twenty nineteen to four thousand, three hundred sixty-four in twenty twenty. By our arithmetic that is a drop of about seventeen percent, in the year the pandemic began. Then it recovered. For used buyers, the early cars are common and the later ones are more plentiful still.""",
   "Lamborghini factory Sant'Agata", "2020 PRODUCTION DIPPED ~17% (OUR ARITHMETIC)")
sc("""Compare that with a rival. Motor1 says Ferrari caps its Purosangue at twenty percent of production, and Marque Cars estimates about two thousand, seven hundred to two thousand, eight hundred cars a year. The same guide says optioned used cars exceed four hundred fifty thousand dollars. Next to that, a three-hundred-thousand-dollar Urus is the one you can actually find.""",
   "Ferrari Purosangue", "PUROSANGUE USED: $450K+ (MARQUE CARS)")
sc("""For context, Motor1 says the Ferrari costs more than forty thousand dollars above a base Rolls-Royce Cullinan, and more again than an Aston Martin D B X or a Bentley Bentayga Speed. So the Urus sits in a market where the ticket is already extraordinary. Everything in this video should be read against that background.""",
   "Rolls-Royce Cullinan", "THE SEGMENT: ULTRA-LUXURY SUVS")


ch("Reading the used-price table")
sc("""Look at the VinAssessment table as a whole. The twenty twenty-six median, three hundred thirty-seven thousand, seven hundred twenty-five dollars, is almost exactly double the twenty nineteen median of one hundred sixty-eight thousand, six hundred ninety-six. By our own arithmetic the ratio is two point zero zero. Seven model years of difference, and the price doubles.""",
   "Used car price table", "2026 MEDIAN ≈ 2.00 × 2019 MEDIAN (OUR ARITHMETIC)")
sc("""The twenty twenty-five median is about one point seven five times the twenty nineteen one, by our arithmetic. So a car that is six years old asks for roughly three-quarters more than the oldest one. This is the opposite of what many people expect from a luxury car, where age usually pulls the price down much faster.""",
   "Lamborghini Urus 2025", "2025 ≈ 1.75 × 2019 (OUR ARITHMETIC)")
sc("""Why might that be? We do not have a source that explains it, so this is only a possibility. New cars have been priced higher each year, and the used market follows. Wikipedia and CARFAX both show the model changing over time, with the Performante and the S E arriving. Newer cars simply are not the same product as the oldest ones.""",
   "Lamborghini Urus models", "OUR READING, NOT A SOURCED CLAIM")
sc("""And remember the limits of the data. VinAssessment's numbers are asking prices from dealers, collected on one day, the twenty-second of October, twenty twenty-six. They are not auction results. They are not private sales. If you want a true value for one particular car, you need comparable sales for that car, not a median for a year.""",
   "Dealer lot", "ONE DAY'S ASKING PRICES · NOT SALES")
sc("""There is also what the table cannot tell you. Mileage, condition, options and history all move a price, and a median hides them. Two cars from the same year can differ by tens of thousands of dollars. So use the table to see where the market is, and use inspections and quotes to see what your car is worth.""",
   "Car inspection", "MEDIANS HIDE MILEAGE, OPTIONS AND CONDITION")

ch("A year of ownership, with the numbers we can source")
sc("""Let us build a rough year, clearly labelled as our own arithmetic with an assumed car. Say you buy a twenty twenty-three Urus at the median asking price of two hundred fifty-three thousand, one hundred twelve dollars. If it loses ten percent a year, which is our own assumption, that is about twenty-five thousand dollars in a year. The assumption could be wrong in either direction.""",
   "Lamborghini Urus", "OUR ARITHMETIC: 10% OF $253K ≈ $25K (ASSUMED RATE)")
sc("""Add insurance. Premier Auto Miami estimates five to ten thousand dollars or more. Add fuel. Our earlier arithmetic gave about two thousand, four hundred dollars for twelve thousand miles at twenty miles per gallon and an assumed four dollars a gallon, though a plug-in could use less. Together, that is a range of roughly thirty-two to thirty-seven thousand dollars before any service.""",
   "Calculator", "~$32K–$37K BEFORE SERVICE (OUR ARITHMETIC)")
sc("""Now add what we could not source. Service, tyres, brakes, repairs, registration, and the loan if there is one. We have no verified figures for them, so we leave them out. That is the honest limit of this video. Whatever the true annual figure is, it is at least what we calculated, and probably more, which is a reason to get real quotes.""",
   "Lamborghini service", "SERVICE, TYRES, REGISTRATION, FINANCE: NOT SOURCED")
sc("""One more way to see the scale. The Urus reached ten thousand cars in July twenty twenty, and twenty thousand by twenty twenty-two, the fastest any Lamborghini has reached that mark, according to Wikipedia. Owners are not a tiny club. There are tens of thousands of them, which is why the used market has real data, and why the medians in this video rest on eight hundred forty-eight listings.""",
   "Lamborghini Urus", "10,000 BY JULY 2020 · 20,000 BY 2022")

ch("Checklist before buying one")
sc("""If you are seriously considering an Urus, here is a checklist drawn from the sources. First, check which recalls apply. Wikipedia lists November twenty twenty for fuel lines and May twenty twenty-four for hood-latch rivets, and your dealer can tell you whether the work was done. Second, ask for the full service history.""",
   "Lamborghini Urus inspection", "CHECK RECALLS AND SERVICE HISTORY")
sc("""Third, know exactly which version you are buying. The base car, the Performante, the S T-X and the S E are different machines with different weights and different values. Fourth, remember that asking prices are not sale prices. VinAssessment's medians are what sellers want, and what buyers pay may be lower. Negotiate, and compare many cars.""",
   "Lamborghini Urus versions", "KNOW YOUR VERSION · ASKING IS NOT SOLD")
sc("""Fifth, get an insurance quote before you sign anything. Sixth, get a service estimate from a franchised dealer. Marque Cars gives the same advice for the Purosangue, and it applies equally here. Seventh, decide whether you want the plug-in, since the S E is now the only version CARFAX lists for twenty twenty-six, and it needs somewhere to charge.""",
   "Electric charging", "QUOTES FIRST · DECIDE ON THE PLUG-IN")
sc("""None of this says the Urus is a bad car. It says that the cost to own one is made up of many lines, and that we can source only some of them. If a video, a seller or a friend gives you a single confident number for the whole thing, ask where it comes from. We have tried to show you where ours comes from, and where it runs out.""",
   "Lamborghini Urus", "ASK WHERE A NUMBER COMES FROM")

ch("What we would do")
sc("""So what does it really cost? Using only sourced numbers, a new car is two hundred seventy-six thousand dollars or more, a used one is a hundred sixty-eight to three hundred thirty-eight thousand depending on the year, and insurance is estimated at five to ten thousand a year. Fuel depends on whether you plug it in. Repairs we could not price.""",
   "Lamborghini Urus", "THE SOURCED NUMBERS")
sc("""The honest answer is that the purchase price is only the first line. Insurance, fuel, service and tyres come on top every year, and we have sourced only two of those four. Before you buy any exotic, get a quote from your insurer, and a written service estimate from a franchised dealer. That costs nothing and tells you more than any video.""",
   "Lamborghini Urus owner", "GET QUOTES BEFORE YOU BUY")
sc("""Would you pay these prices for an Urus, or buy something else? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Urus, compare it with the Ferrari Purosangue, and tell why Lamborghini bet everything on an SUV.""",
   "Lamborghini Urus", "WOULD YOU BUY ONE?")
sc("""And if you would rather spend your money on something that earns its keep, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more real numbers on the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video99", "What It Really Costs to Own a Lamborghini Urus", [
    "CARFAX, 2026 Lamborghini Urus: https://www.carfax.com/Research-Lamborghini-Urus_w9540",
    "Premier Auto Miami, How much is a Lamborghini Urus: https://www.premierautomiami.com/how-much-is-a-lamborghini-urus/",
    "VinAssessment, Lamborghini Urus prices by year (22 Oct 2026): https://vinassessment.com/prices/lamborghini/urus",
    "Wikipedia, Lamborghini Urus: https://en.wikipedia.org/wiki/Lamborghini_Urus",
    "Motor1, 2024 Ferrari Purosangue is predictably expensive: https://www.motor1.com/news/652734/2024-ferrari-purosangue-suv-price/",
], "C")
