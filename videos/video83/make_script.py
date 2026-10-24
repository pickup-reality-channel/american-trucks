import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In twenty twenty-one, a McLaren F one sold at auction for twenty point four six five million dollars. That is more than two hundred fifty years of the median American household income, by our own arithmetic. But the purchase price is only the beginning. Today we work out what it really costs to own a McLaren F one, from the sticker price in nineteen ninety-two to the insurance bill.""",
   "McLaren F1", "WHAT IT REALLY COSTS TO OWN A McLAREN F1")
sc("""Here is the twist. For the first fourteen years of its life, the F one barely gained any value. Then it became one of the best-performing cars in history. So the real cost of owning one depends enormously on when you bought it, and the people who paid the original price got a very different deal from the people buying today.""",
   "McLaren F1 auction", "IT WAS FLAT FOR 14 YEARS")
sc("""Every figure in this video comes from a published source, listed in the description. Many of the running costs come from AutoMonitor, a valuation site that does not cite its sources, so we will label those as estimates. Hagerty, auction houses and Wikipedia give the harder numbers. Let's begin with the sticker price.""",
   "McLaren F1 front", "EVERY FIGURE IS SOURCED")

# ---------- 1. THE STICKER PRICE ----------
ch("The sticker price")
sc("""Top Gear says the McLaren F one launched at five hundred forty thousand pounds, which the Bank of England puts at a little over one point one million pounds in two thousand twenty money. AutoMonitor gives an approximate dollar figure of nine hundred seventy thousand dollars, and says the car launched in nineteen ninety-four, while Top Gear says nineteen ninety-two.""",
   "McLaren F1 launch", "£540,000 NEW")
sc("""Gooding and Company, which sold one of the cars, says the starting price was five hundred forty thousand pounds in nineteen ninety-three. And it adds something remarkable. It is alleged that, despite this whopping price tag, McLaren lost money on the F one project. A car that cost more than half a million pounds still lost money for its maker.""",
   "McLaren F1 factory", "McLAREN ALLEGEDLY LOST MONEY")
sc("""For that money, what did a buyer get? Wikipedia says a six thousand sixty-four cubic centimeter BMW V twelve making six hundred eighteen horsepower, in a car weighing eleven hundred forty kilograms dry, with the driver in the middle. At the launch price, that is about eight hundred seventy-four pounds per horsepower, by our own arithmetic.""",
   "BMW V12 McLaren F1", "618 HP FOR £540,000")
sc("""Performance matched the price. SlashGear says zero to sixty takes three point two seconds. Wikipedia says that on the thirty-first of March, nineteen ninety-eight, the F one reached an independently measured two hundred forty point one miles per hour. The car was not expensive for no reason. It was the fastest production car in the world.""",
   "McLaren F1 speed record", "THE FASTEST CAR IN THE WORLD")
sc("""Production was small. Wikipedia says only one hundred six cars were manufactured. AutoMonitor says McLaren originally planned to build three hundred road cars, but only sixty-four were completed. By our own arithmetic, that is about twenty-one percent of the original plan.""",
   "McLaren F1 production", "64 BUILT OF 300 PLANNED")
sc("""And who bought them? Wikipedia lists notable owners, past and present, including Lewis Hamilton, Elon Musk, Rowan Atkinson, Jay Leno, George Harrison, Ralph Lauren, Nick Mason, and the Sultan of Brunei. The page says chassis zero six seven was previously owned by Elon Musk, and chassis zero six one was sold to Rowan Atkinson.""",
   "McLaren F1 owners", "HAMILTON, MUSK, ATKINSON, LENO")

# ---------- 2. THE FLAT YEARS ----------
ch("The flat years")
sc("""For years, the F one was not a great investment. Top Gear says that, according to Hagerty, F ones changed hands for roughly the original asking price until about two thousand six. AutoMonitor says that by the late nineteen nineties some examples traded for as little as six hundred thousand to eight hundred thousand dollars.""",
   "McLaren F1 1990s", "NO GAIN UNTIL ~2006")
sc("""Think about what that means. Someone who bought a new F one in nineteen ninety-three and sold it in two thousand six, after thirteen years of ownership, would have roughly broken even in nominal terms, according to Hagerty. After thirteen years of inflation, that is a loss in real terms, by our own reasoning. Insurance, storage and service would have been costs on top of that.""",
   "McLaren F1 old", "13 YEARS WITH NO GAIN")
sc("""Then the market woke up. Top Gear says that by the end of two thousand eight, prices had roughly tripled to around one point five million pounds. AutoMonitor says by two thousand five clean examples traded at one and a half to two million dollars, and by two thousand eight the best pushed past three million, despite the financial crisis.""",
   "McLaren F1 2008", "2008: ABOUT £1.5 MILLION")

# ---------- 3. THE CLIMB ----------
ch("The climb")
sc("""Top Gear says that by two thousand fourteen values reached five million pounds. In twenty fifteen, Rowan Atkinson sold his car, which he had crashed twice, for eight million pounds. Wikipedia lists chassis zero six one at twelve point two million dollars at auction in twenty fifteen. A car that had been crashed twice sold for almost fifteen times its original price, by our own arithmetic.""",
   "Rowan Atkinson McLaren F1", "ATKINSON SOLD HIS CRASHED F1 FOR £8M")
sc("""Gooding and Company says that in twenty thirteen, one of the last F ones built sold for eight million four hundred seventy thousand dollars at auction, and a nineteen ninety-five example went for fifteen million six hundred twenty thousand dollars four years later. So the price almost doubled in four years.""",
   "McLaren F1 auction 2013", "$8.47M IN 2013, $15.62M IN 2017")
sc("""Top Gear says chassis zero four four sold at auction in twenty seventeen for just under twelve million pounds, with the buyer reportedly Lewis Hamilton. AutoMonitor lists the same sale at fifteen point six million dollars, then a record, at Bonhams, for a low-mileage car. And Wikipedia lists the same chassis at fifteen point six two million dollars.""",
   "Lewis Hamilton McLaren F1", "CHASSIS 044: $15.6 MILLION")
sc("""In twenty nineteen, AutoMonitor says chassis zero six nine sold for nineteen point eight million dollars at RM Sotheby's in Monterey. Then, in twenty twenty-one, the record rose again. Gooding and Company sold chassis zero two nine for twenty point four six five million dollars, a new auction record for a McLaren F one.""",
   "McLaren F1 Monterey", "2019: $19.8M. 2021: $20.5M")
sc("""That car had just three hundred ninety kilometers on the odometer. Gooding and Company says it spent its first twenty years in Japan, came to the United States in twenty thirteen, and for the past decade had been maintained and regularly started, but never driven. A twenty million dollar car that, for a decade, was started but never driven.""",
   "McLaren F1 chassis 029", "390 KM. NEVER DRIVEN.")
sc("""And the record went higher. Wikipedia lists chassis zero one four at twenty-five point three one seven five million dollars, in twenty twenty-five. That is the highest price for a road F one that we found in our sources. Hagerty, as reported by Top Gear, valued a normal car at around sixteen million pounds in twenty twenty.""",
   "McLaren F1 record sale", "2025: $25.3 MILLION")
sc("""Do the arithmetic. From five hundred forty thousand pounds to sixteen million pounds is about thirty times the launch price in nominal terms. Adjusted for inflation, using the Bank of England figure of one point one million, it is about fourteen and a half times. Either way, one of the best-performing cars ever built.""",
   "McLaren F1 value chart", "30x NOMINAL, ~14.5x REAL (OUR MATH)")
sc("""Wikipedia's table of auction results gives a way to measure the climb. Chassis zero six one sold for twelve point two million dollars in twenty fifteen. Chassis zero one four sold for twenty-five point three million in twenty twenty-five. That is about two point one times in ten years, or roughly seven point six percent a year, by our own arithmetic.""",
   "McLaren F1 auction results", "$12.2M (2015) TO $25.3M (2025)")
sc("""Here is the whole timeline in one place. About nine hundred seventy thousand dollars at launch, according to AutoMonitor. One and a half to two million in two thousand five. Over three million in two thousand eight. Fifteen point six million in twenty seventeen. Twenty point five million in twenty twenty-one. Twenty-five point three million in twenty twenty-five. That is about twenty-six times the launch price, by our own arithmetic.""",
   "McLaren F1 price chart", "~$0.97M TO $25.3M: ABOUT 26x")
sc("""A caution. These are different cars, with different histories, mileage and condition, sold by different auction houses. So the seven point six percent is not a pure market return. It is just a rough sign of the direction. AutoMonitor's own estimate of three to eight percent a year is in the same range, but it does not cite its method.""",
   "McLaren F1 condition inspection", "DIFFERENT CARS, DIFFERENT PRICES")
sc("""The same year can show very different prices. Wikipedia lists chassis zero four two at sixteen point five five million dollars in twenty twenty-one, and chassis zero two nine at twenty point four six five million the same year. That is almost four million dollars more, about twenty-four percent, by our own arithmetic, for the car with three hundred ninety kilometers.""",
   "McLaren F1 chassis 042", "SAME YEAR, $4 MILLION APART")
sc("""So mileage, history and condition matter enormously. Top Gear also notes that Hagerty's sixteen million pound figure is for a normal F one, and that especially special examples would likely fetch more. A buyer is not choosing between one price and another. They are choosing among cars that can differ by millions of dollars.""",
   "McLaren F1 low mileage", "A \"NORMAL\" F1 IS ABOUT £16M")
sc("""Top Gear puts the whole story in context. It says most nineteen nineties supercars are worth more now than when new, but the F one has risen far more than most. And it calls the original price favorable compared with today's hypercars, a car that was expensive in nineteen ninety-two, and now looks like the cheapest part of the deal.""",
   "nineties supercars", "THE ORIGINAL PRICE LOOKS CHEAP")

# ---------- 4. WHAT IT COSTS EACH YEAR ----------
ch("The yearly bill")
sc("""Now the part nobody likes. AutoMonitor estimates that an annual service at McLaren's special operations division in Woking costs fifteen thousand to thirty thousand dollars. It says a major service costs fifty thousand to a hundred thousand dollars or more, every five years or as needed. These are estimates, not published price lists.""",
   "McLaren Special Operations Woking", "SERVICE: $15K-$30K A YEAR (EST.)")
sc("""Insurance, AutoMonitor estimates, runs forty thousand to eighty thousand dollars a year, on an agreed-value policy with limited mileage. That is for a car valued at eighteen to twenty-five million dollars. By our own arithmetic, the premium would be between about one sixth and less than half of one percent of the car's value each year.""",
   "McLaren F1 insurance", "INSURANCE: $40K-$80K A YEAR (EST.)")
sc("""Storage adds twelve thousand to thirty-six thousand dollars a year, AutoMonitor estimates, in a climate-controlled, secured facility. The site also lists shipping. A cross-country move within the United States typically costs five to eight thousand dollars with a specialized carrier, and international shipping, with export licenses and customs, takes weeks and costs twenty-five to fifty thousand.""",
   "climate controlled car storage", "STORAGE: $12K-$36K A YEAR (EST.)")
sc("""Add the three yearly items, and the estimated bill is sixty-seven thousand to one hundred forty-six thousand dollars a year for service, insurance and storage, by our own arithmetic. Over five years that is three hundred thirty-five thousand to seven hundred thirty thousand, plus a major service of fifty to a hundred thousand.""",
   "McLaren F1 garage", "~$67K-$146K A YEAR (OUR MATH)")
sc("""Put that against the median household income. KTVU, citing the Census Bureau, reported a median of eighty thousand six hundred ten dollars. So the F one's running costs alone are about eighty-three percent to one hundred eighty-one percent of that income every year, by our own arithmetic, before you even buy the car.""",
   "American family", "RUNNING COSTS vs MEDIAN INCOME")
sc("""AutoMonitor also describes where the market is. It says F one values remain within five percent of their all-time peaks, and that the market has stabilized at what appear to be sustainable levels. Those are the site's own words, and it does not cite a source. But it matches what Hagerty and the auction results suggest.""",
   "McLaren F1 collector", "VALUES NEAR ALL-TIME PEAKS (EST.)")

# ---------- 5. THE BUYING COSTS ----------
ch("The cost of buying")
sc("""There are also buying costs. AutoMonitor says that sales tax alone can exceed one point five million dollars, depending on jurisdiction. On a twenty point four six five million dollar car, that is about seven percent, by our own arithmetic. That is a sum larger than the entire launch price of the car.""",
   "tax paperwork", "SALES TAX CAN EXCEED $1.5M")
sc("""So buying one of these cars at the twenty twenty-one auction record means roughly twenty-two million dollars before the first year of running costs, by our own arithmetic, and that is without the auction house's own fees, which our sources do not list. The real entry ticket is higher than the hammer price.""",
   "auction gavel", "THE HAMMER PRICE IS NOT THE PRICE")
sc("""Gooding and Company's David Brynan described the car sold in twenty twenty-one as a tour de force of automotive engineering with an unmatched competition pedigree. And he called its low mileage and one-of-a-kind color combination an almost unheard-of opportunity. Buyers do not just pay for an F one. They pay for the rarest version of one.""",
   "McLaren F1 color auction lot", "\"AN ALMOST UNHEARD-OF OPPORTUNITY\"")
sc("""Divide the record price by the horsepower. Twenty point four six five million dollars for six hundred eighteen horsepower is about thirty-three thousand dollars per horsepower, by our own arithmetic. At launch, it was about eight hundred seventy-four pounds. The value of each horsepower has grown by tens of times, while the horsepower itself never changed.""",
   "McLaren F1 engine value", "~$33,000 PER HORSEPOWER (OUR MATH)")
sc("""And what about the price swings? AutoMonitor estimates the car's appreciation at three to eight percent a year, based on a ten-year trend. On an eighteen to twenty-five million dollar car, that is about five hundred forty thousand to two million dollars a year, by our own arithmetic, far more than the running costs.""",
   "McLaren F1 value", "VALUE CHANGES ARE BIGGER THAN COSTS")
sc("""Here is one more number. AutoMonitor says private sales are believed to have exceeded auction figures in several cases, with unconfirmed reports of L M cars trading above thirty million dollars. That means the public prices we have been quoting may not be the whole story. The true top of the market could be higher.""",
   "McLaren F1 private sale", "PRIVATE SALES MAY BE HIGHER")
sc("""That is the key insight. For a car like this, the running costs are small next to the value swings. A three percent change in value is bigger than the whole year's service, insurance and storage. So the real cost of ownership is the price you pay, and the price you sell at, and almost nothing else.""",
   "McLaren F1 investment", "THE REAL COST IS THE SPREAD")
sc("""Let's put the whole thing together with an example. Buy at the twenty twenty-one record of twenty point four six five million dollars, add one and a half million in sales tax, and five years of the estimated running costs plus one major service. By our own arithmetic, you have spent about twenty-two point three five to twenty-two point eight million.""",
   "McLaren F1 calculator", "5-YEAR TOTAL: ~$22.35M-$22.8M (OUR MATH)")
sc("""Now the value. If the car rises three percent a year, as AutoMonitor's low estimate suggests, it would be worth about twenty-three point seven million after five years. At eight percent it would be about thirty million. Those are illustrations, not predictions, and the market can fall. But they show why owners accept the costs.""",
   "McLaren F1 sale", "AT 3%: $23.7M. AT 8%: $30.1M (OUR MATH)")
sc("""In the low case, the car's rise would barely cover the costs, leaving a gain of about one to one and a half million dollars. In the high case, the gain would be more than seven million. And if the market fell, the owner would lose money. That is the real cost of an F one. Not the bills. The risk.""",
   "McLaren F1 risk", "THE REAL COST IS THE RISK")

# ---------- 6. THE REST OF THE FAMILY ----------
ch("The rest of the family")
sc("""The road car is not the only one. Wikipedia says five special L M cars were built in honor of the five GTRs that finished the nineteen ninety-five Le Mans. AutoMonitor puts their value of twenty-five to thirty-five million dollars, and reports unconfirmed sales above thirty million. In twenty fifteen, it says, an L M spec car sold for thirteen point eight million dollars at RM Sotheby's.""",
   "McLaren F1 LM", "F1 LM: $25M-$35M (EST.)")
sc("""Then the race cars. Wikipedia says twenty-eight F one GTR chassis were built, and lists chassis ten R as sold in twenty twenty-six for a record thirty-four point six five five million dollars. Motor Sport says the first five customer race cars of the nineteen ninety-five program cost six hundred twenty-five thousand pounds each.""",
   "McLaren F1 GTR race car", "A GTR SOLD FOR $34.7 MILLION")
sc("""AutoMonitor estimates the road-legal GTR at twelve to twenty million dollars and the long tail GTR at ten to eighteen million. The sources do not agree on every number, and many are estimates. But all point in the same direction. A family of cars that started at under a million pounds each now costs tens of millions.""",
   "McLaren F1 GTR Longtail", "GTR: $12M-$20M (EST.)")
sc("""AutoMonitor says the five L M cars, the special edition built to honor the race winners, are the most valuable of the road cars, at an estimated twenty-five to thirty-five million dollars. In twenty fifteen it reports an L M spec car sold for thirteen point eight million. That is a rise of roughly eighty to one hundred fifty percent, by our own arithmetic.""",
   "McLaren F1 LM", "LM: $13.8M (2015) TO $25M+ (EST.)")
sc("""And compare the F one with its successor. Car and Driver says the new McLaren W one starts at two point one million dollars. By our own arithmetic, the twenty-one million dollar F one record is about ten times that price, and the twenty-five million dollar sale is about twelve times, for a car with half the horsepower.""",
   "McLaren W1", "THE NEW W1: $2.1M")

# ---------- 7. THE OWNER'S DILEMMA ----------
ch("The owner's dilemma")
sc("""There is one more cost that does not appear on any invoice. Top Gear quotes Gordon Murray, the F one's designer, who owned the oldest surviving car and sold it. He said, it became a little untenable to own. He used to drive his car on Sunday mornings, but once it was worth many millions, he was reluctant to risk damaging it.""",
   "Gordon Murray", "\"UNTENABLE TO OWN\"")
sc("""That is the owner's dilemma. Drive it, and every mile risks a crash that could cost millions. Atkinson crashed his twice, and still sold it for eight million pounds. Park it, and you own a twenty million dollar sculpture, like chassis zero two nine, started regularly but never driven.""",
   "McLaren F1 in garage", "DRIVE IT OR PROTECT IT?")
sc("""Airbags are not present in the car, Wikipedia says. And Wikipedia reports the first prototype was rolled several times by a test driver in shorts and a T-shirt. The car was never meant to be a museum piece. It was meant to be driven fast. The market turned it into something that few dare to drive.""",
   "McLaren F1 interior no airbags", "NO AIRBAGS")

# ---------- 8. THE ANSWER ----------
ch("The real cost")
sc("""So what does it really cost to own a McLaren F one today? Sources give a range of eighteen to twenty-five million dollars for a road car, with a record of twenty-five million. Add sales tax of up to one and a half million, and yearly costs of about sixty-seven to one hundred forty-six thousand dollars, by AutoMonitor's estimates.""",
   "McLaren F1", "$18M-$25M + TAX + $67K-$146K/YEAR")
sc("""But the real cost depends on the spread. A buyer in nineteen ninety-three paid five hundred forty thousand pounds and saw sixteen million pounds by twenty twenty. A buyer in twenty twenty-five paid twenty-five million dollars and does not know where the price will go. Early owners made a fortune. Today's buyers are betting.""",
   "McLaren F1 investment value", "EARLY OWNERS WON. TODAY'S BUYERS BET.")
sc("""Would you buy a McLaren F one if you could? And would you drive it? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the F one, compare it to the new W one, and tell the story of the man who dreamed it up.""",
   "McLaren F1", "WOULD YOU DRIVE IT?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video83", "What It Really Costs to Own a McLaren F1 Today", [
    "Wikipedia, McLaren F1: https://en.wikipedia.org/wiki/McLaren_F1",
    "Wikipedia, McLaren F1 GTR: https://en.wikipedia.org/wiki/McLaren_F1_GTR",
    "Top Gear, McLaren F1s are now worth 16 million pounds: https://topgear.com.sg/features/mclaren-f1s-are-now-worth-ps16million",
    "Gooding and Company coverage of F1 chassis 029, JustCars (Australia): https://www.justcars.com.au/news-and-reviews/feature-1995-mclaren-f1/924590",
    "AutoMonitor, McLaren F1 price history (estimates, sources not cited): https://automonitor.io/blog/mclaren-f1-price-history/",
    "Motor Sport magazine, Won for the road (June 2005): https://www.motorsportmagazine.com/archive/article/june-2005/52/won-road/",
    "KTVU / Fox, Census 2023 median household income: https://ktvu.com/news/how-much-american-household-earned-2023-census",
], "C")
