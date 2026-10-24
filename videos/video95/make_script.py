import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""A price guide says a Dodge Viper ACR is worth between one hundred thirty and one hundred sixty-five thousand dollars. But in twenty twenty-five, eight Viper ACRs actually sold at auction for an average of two hundred ninety-three thousand, eight hundred forty-six dollars. The guide was off by a lot. This is what it really costs to own a Viper today, and why the usual price guides may be wrong.""",
   "Dodge Viper ACR", "THE REAL COST OF OWNING A VIPER TODAY")
sc("""Here is the twist. The running costs of a Viper, insurance, servicing and tyres, are modest compared with what the car itself can gain or lose in value. In a market that moved from tens of thousands to hundreds of thousands, the biggest cost of owning a Viper may be what you did not buy five years ago.""",
   "Dodge Viper ACR", "THE BIGGEST COST ISN'T FUEL")
sc("""Every figure in this video comes from published sources, listed in the description. Where a number comes from a price guide, we call it an estimate. Where we do the maths ourselves, we say so. And where sources disagree, we tell you.""",
   "Dodge Viper", "EVERY NUMBER IS SOURCED")

# ---------- 1. WHAT IT COST NEW ----------
ch("What a Viper cost new")
sc("""Start with the original prices. Wikipedia says the first Viper, the R T ten roadster, shipped in January nineteen ninety-two for fifty-two thousand dollars. In April nineteen ninety-eight, the G T two Champion Edition, with four hundred sixty horsepower and only one hundred built, had its price approved at eighty-five thousand, two hundred dollars.""",
   "Dodge Viper RT/10", "1992: $52,000 · 1998: $85,200")
sc("""The track-only A C R-X, introduced in twenty ten, cost one hundred ten thousand dollars, according to Wikipedia. And the Viper G T three R race car was estimated at four hundred fifty-nine thousand dollars. The sources we read do not give the new price of the road-going two thousand sixteen and twenty seventeen A C R, so we cannot compare it with its present value.""",
   "Dodge Viper ACR-X", "ACR-X: $110,000 · GT3-R: ~$459,000")
sc("""For comparison, the Corvette Z R one started at one hundred three thousand, three hundred dollars in two thousand nine, including destination, according to Autoblog. A Viper A C R and a Z R one competed for the same buyers, and cost roughly similar amounts when new, by what our sources show.""",
   "Corvette ZR1", "ZR1 WHEN NEW: $103,300")
sc("""By our own arithmetic, the Viper's price rose about sixty-four percent from the R T ten's fifty-two thousand to the G T two's eighty-five thousand two hundred, in six years. That is the kind of price increase that a company makes when it knows its audience will follow. And the audience followed.""",
   "Dodge Viper GT2", "+64% IN SIX YEARS")

# ---------- 2. THE USED MARKET ----------
ch("What a Viper sells for now")
sc("""Now what they sell for. Classic dot com shows eight sales of fifth-generation Viper A C Rs between May and November twenty twenty-five. The lowest was one hundred eighty-seven thousand dollars for a two thousand sixteen A C R with eleven thousand miles, on the first of November in Texas. The highest was four hundred six thousand five hundred.""",
   "Dodge Viper ACR auction", "8 ACR SALES IN 2025: $187,000 TO $406,500")
sc("""The highest-priced car was a twenty seventeen G T C A C R with the Extreme Aero Package, with one hundred thirteen miles, sold in Monterey County, California, on the fourteenth of August. The second was another twenty seventeen A C R Extreme Aero, with three hundred fifty miles, at three hundred fifty-seven thousand dollars on the same day.""",
   "Dodge Viper ACR Extreme Aero", "113 MILES: $406,500")
sc("""By our own arithmetic, the eight sales add up to two million, three hundred fifty thousand, seven hundred sixty-seven dollars, and the average is two hundred ninety-three thousand, eight hundred forty-six. That average is the number that gave us the title of this video. It is more than double the price guide's range for a two thousand sixteen or seventeen A C R coupé.""",
   "Dodge Viper ACR", "AVERAGE OF 8 SALES: $293,846")
sc("""The same site lists three cars that did not sell. A twenty seventeen G T C A C R one twenty-eight Edition reached a highest bid of two hundred thirty-one thousand, one hundred twenty-eight dollars in June. A twenty sixteen A C R Extreme reached two hundred sixty-six thousand in July. And a twenty seventeen A C R reached two hundred fifty thousand in May.""",
   "Dodge Viper ACR unsold", "3 CARS UNSOLD: BIDS OF $231K, $250K, $266K")
sc("""Those bids tell us something important. A seller refused to sell at two hundred sixty-six thousand dollars, and another at two hundred fifty. So the sold prices of one hundred eighty-seven to four hundred six thousand are not floor prices. They are results of negotiation between sellers who wanted more and buyers who wanted less.""",
   "Auction hammer", "SELLERS HOLDING OUT FOR MORE")
sc("""The site also lists asking prices for cars that were taken down. It shows three hundred eighty-nine thousand, eight hundred eighty-eight dollars in Red Deer County in September, three hundred eighty-nine thousand, eight hundred in West Chicago, three hundred nineteen thousand, nine hundred in Cleveland, and two hundred seventy-nine thousand, eight hundred in Naperville.""",
   "Dodge Viper for sale", "LAST ASKING PRICES: $279,800 TO $389,888")
sc("""Currently listed A C Rs range from two hundred eleven thousand, nine hundred dollars to four hundred ninety-nine thousand, eight hundred. And the benchmark value on the site is two hundred fifty-three thousand, four hundred eighty-nine dollars. Notice that this benchmark is lower than the average of the eight sales, which tells you the market includes several lower-priced cars.""",
   "Classic.com Viper ACR", "BENCHMARK: $253,489")

# ---------- 3. MILEAGE ----------
ch("What miles do to the price")
sc("""Mileage is the biggest driver in this list, though with a caution. The site's listings show two mileage numbers for each car, and the page does not label them. We read the second one as the mileage, and the first, which is the same for every listing, as likely an error. So treat the mileage figures here as indicative.""",
   "Odometer", "A CAUTION ABOUT THE MILEAGE DATA")
sc("""With that caution, look at the three twenty seventeen cars with the Extreme Aero Package and under four hundred miles: one hundred thirteen, two hundred eighty-one and three hundred fifty. They sold for four hundred six thousand five hundred, three hundred twenty-nine thousand, sixty-seven, and three hundred fifty-seven thousand dollars. By our arithmetic, the average is about three hundred sixty-four thousand, one hundred eighty-nine.""",
   "Dodge Viper ACR Extreme Aero", "2017 EXTREME AERO, UNDER 400 MILES: ~$364,000")
sc("""Now the cars with five thousand to eleven thousand miles: two hundred thirty-eight thousand, one hundred eighty-seven thousand, three hundred thousand and two hundred forty-two thousand dollars. By our arithmetic, the average of those four is about two hundred forty-one thousand, seven hundred fifty. The low-mileage Extreme cars sold for about fifty percent more.""",
   "Dodge Viper ACR high mileage", "5,000–11,000 MILES: AVERAGE ~$241,750")
sc("""But mileage is not the whole story. One twenty sixteen A C R coupé with only thirty-nine miles sold in Miami Gardens in May for two hundred ninety-one thousand, two hundred dollars, lower than the three Extreme Aero cars with a few hundred miles. So the trim and the year matter too. The comparison is suggestive, not proof.""",
   "Dodge Viper ACR 2016", "39 MILES, 2016: $291,200")
sc("""That fifty percent gap, roughly one hundred twenty-two thousand dollars, mixes mileage, year and equipment, so we cannot call it the price of driving. But it is large enough to make a point. For the most valuable cars, every mile may cost real money, which is why many of these cars are kept in garages.""",
   "Dodge Viper ACR", "THE GAP: ~$122,000 (MILEAGE + TRIM + YEAR)")
sc("""There are modifications to consider. The list marks some cars as modified and some as original. A twenty sixteen A C R in Texas with eleven thousand miles, labelled original, sold for one hundred eighty-seven thousand. A modified car in Iowa with eight thousand miles sold for two hundred thirty-eight thousand. So originality did not always command a premium in this small sample.""",
   "Modified Viper ACR", "ORIGINAL $187K · MODIFIED $238K")

# ---------- 4. OTHER VIPERS ----------
ch("What about older and cheaper Vipers?")
sc("""Not every Viper costs a quarter of a million. Automonitor, a price guide, lists estimates for other generations. A first generation R T ten from nineteen ninety-two to nineteen ninety-five: sixty thousand to one hundred ten thousand dollars. A fourth generation S R T ten coupé, from two thousand eight to twenty ten: fifty-five to ninety thousand.""",
   "Dodge Viper RT/10", "RT/10: $60K–$110K · SRT-10 COUPE: $55K–$90K")
sc("""The guide lists the fourth-generation roadster at fifty to eighty-five thousand dollars, and a first-year nineteen ninety-two launch edition at eighty to one hundred twenty thousand. These are estimates from a guide that does not show its sources, so treat them as a rough range, not a quote.""",
   "Dodge Viper roadster", "LAUNCH EDITION: $80K–$120K (ESTIMATE)")
sc("""By our own arithmetic, the first Viper cost fifty-two thousand dollars new, and the guide values it today at sixty to one hundred ten thousand. That is a gain of about fifteen to one hundred twelve percent in thirty years, before inflation. Inflation, which we have not adjusted for, would consume a large part of that gain.""",
   "Dodge Viper 1992", "RT/10: +15% TO +112% IN 30 YEARS (NOMINAL)")
sc("""There is one more oddity in that guide. It lists values for a fifth-generation Viper roadster. But Wikipedia says the fifth generation was sold only as a coupé, and that convertibles ended in twenty ten. We did not use those roadster values. It is a reminder that online price guides can contain errors, and that a number is only as good as its source.""",
   "Dodge Viper coupe", "A GUIDE WITH AN ERROR: GEN-5 \"ROADSTERS\"")
sc("""The same guide lists the Final Edition from twenty seventeen at one hundred forty to one hundred eighty thousand, and a one twenty-eight Edition A C R at one hundred fifty to one hundred eighty. We compare that with the actual unsold bid for a one twenty-eight Edition of two hundred thirty-one thousand. The guide's range sits below what the owners were willing to accept.""",
   "Dodge Viper 1:28 Edition", "GUIDE: $150K–$180K · BID: $231K, UNSOLD")

# ---------- 5. RUNNING COSTS ----------
ch("What it costs to run")
sc("""Now the yearly costs. Automonitor says insurance runs three thousand to six thousand dollars a year, depending on age, location, record and model year. It gives a nineteen ninety-five R T ten at twenty-five hundred to thirty-five hundred, and a twenty sixteen A C R at forty-five hundred to sixty-five hundred.""",
   "Insurance", "INSURANCE: $3,000–$6,000 A YEAR (ESTIMATE)")
sc("""For maintenance, the guide says routine costs are three thousand to eight thousand dollars a year, depending on mileage and driving style. It breaks that down: oil changes, two hundred to three hundred dollars; a fluid service, eight hundred to twelve hundred a year; spark plugs, six hundred to nine hundred a set; filters, two hundred to four hundred.""",
   "Viper maintenance", "MAINTENANCE: $3,000–$8,000 A YEAR (ESTIMATE)")
sc("""By our own arithmetic, insurance and maintenance together run six thousand to fourteen thousand dollars a year for a typical Viper, going by the guide. For an A C R, with higher insurance, it is about seventy-five hundred to fourteen thousand five hundred. Over ten years, that comes to seventy-five thousand to one hundred forty-five thousand dollars.""",
   "Dodge Viper", "10 YEARS: $75K–$145K (OUR ARITHMETIC)")
sc("""Tyres are the next cost. The guide says a set of four costs two thousand to thirty-five hundred dollars and should be replaced every eight thousand to fifteen thousand miles, or five thousand to eight thousand on track days. By our arithmetic, that is about thirteen to forty-four cents a mile on the road, and twenty-five to seventy cents a mile on the track.""",
   "Dodge Viper tyres", "TYRES: 13–44 CENTS A MILE")
sc("""Fuel economy is the one number from official sources. Wikipedia says the first Viper was rated twelve miles per gallon in the city and twenty on the highway. Autoblog quotes thirteen and twenty-two for the Viper in two thousand eight. And in twenty fifteen, Wikipedia says the highway figure was still twenty.""",
   "Fuel pump", "12/20 MPG IN 1992 · 20 MPG HWY IN 2015")
sc("""We do not give a fuel bill, because the sources we read do not give a price for fuel, and prices change. But a car that gets twelve or thirteen miles per gallon in town will use roughly twice as much fuel as one that gets twenty-five, by our simple arithmetic. If you drive a Viper rarely, that matters little. If you drive it every day, it matters a lot.""",
   "Dodge Viper", "RARELY DRIVEN CARS BARELY NOTICE FUEL")

sc("""Express those costs as a share of the car. Insurance of forty-five hundred to sixty-five hundred dollars on a car worth two hundred ninety-three thousand, eight hundred forty-six is about one and a half to two and a quarter percent a year, by our arithmetic. Maintenance of three to eight thousand is about one to two and three-quarters percent.""",
   "Dodge Viper ACR", "INSURANCE ≈ 1.5–2.2% OF THE CAR PER YEAR")
sc("""Together, by our arithmetic, insurance and maintenance cost between two and a half and five percent of an average A C R's value every year. That is not small. But it is also not far from what the guide claims the car gains in value: four to eight percent a year. Whether the claim holds is the whole question.""",
   "Dodge Viper ACR", "RUNNING COSTS ≈ 2.5–4.9% OF VALUE A YEAR")
sc("""For an older car, the picture changes. A nineteen ninety-five R T ten has insurance of twenty-five hundred to thirty-five hundred dollars, according to the guide. On a car worth sixty to one hundred ten thousand, that is about two to six percent a year, by our arithmetic. Cheaper cars cost less in dollars, but not always less in proportion.""",
   "Dodge Viper RT/10", "RT/10 INSURANCE ≈ 2–6% OF VALUE")
sc("""Remember what the trim means. Wikipedia says the last A C R produced fifteen hundred pounds of downforce in corners, or two thousand with the Extreme Aero Package, and that its top speed fell by up to twenty miles per hour. So the most expensive Vipers are the ones with the most extreme aero. Buyers paid extra for the most track-focused version.""",
   "Dodge Viper ACR Extreme Aero", "EXTREME AERO: UP TO 2,000 LB OF DOWNFORCE")
sc("""There is also the question of supply. Good Car Bad Car lists United States Viper sales of five hundred ninety-one in twenty thirteen, seven hundred sixty in twenty fourteen, six hundred seventy-six in twenty fifteen, six hundred twenty-six in twenty sixteen, and five hundred eighty-five in twenty seventeen. That is three thousand, two hundred thirty-eight fifth-generation cars, by our arithmetic.""",
   "Dodge Viper VX", "5TH GEN US SALES: 3,238 (OUR SUM)")
sc("""Only some of those were A C Rs, and the sources we read do not say how many. But the supply is small and finite, and the plant closed in twenty seventeen. Classic dot com lists a hundred fifty-seven related listings for the fifth-generation A C R, though that number includes repeated listings of the same cars.""",
   "Dodge Viper ACR listings", "157 RELATED LISTINGS (INCLUDES REPEATS)")
# ---------- 6. DEPRECIATION & APPRECIATION ----------
ch("Does it lose value, or gain it?")
sc("""Automonitor makes two claims about value. First, that Vipers depreciate roughly two to three percent per ten thousand miles. And second, citing Bring a Trailer data, that Viper prices have appreciated four to eight percent annually. The guide says first-generation cars have appreciated eight to twelve percent a year since twenty twenty.""",
   "Dodge Viper value", "−2% TO −3% PER 10,000 MILES · +4% TO +8% A YEAR")
sc("""We cannot verify the Bring a Trailer data, because the guide does not show it. And the two claims pull in opposite directions. But they help frame the choice. A Viper that is driven loses value with miles. A Viper that is stored can gain it with time. The best value comes from not using the car, which defeats its purpose.""",
   "Dodge Viper garage", "DRIVE IT AND IT LOSES · STORE IT AND IT GAINS")
sc("""Do the arithmetic on the average A C R sale. Two percent to three percent of two hundred ninety-three thousand, eight hundred forty-six is five thousand, nine hundred to eight thousand, eight hundred dollars per ten thousand miles. Compare that with the guide's insurance and maintenance of seventy-five hundred to fourteen thousand five hundred a year. For a low-mileage owner, running costs would dominate.""",
   "Dodge Viper ACR", "~$6,000–$9,000 PER 10,000 MILES (OUR ARITHMETIC)")
sc("""Now the appreciation. Four to eight percent of two hundred ninety-three thousand, eight hundred forty-six is about eleven thousand, eight hundred to twenty-three thousand, five hundred dollars a year. Again, by our arithmetic. If true, that could be bigger than the annual running costs. But that is a very big if. It is a claim, not a promise.""",
   "Dodge Viper ACR", "4–8% OF $293,846 ≈ $11,800–$23,500 A YEAR")
sc("""The guide even gives a five-year figure for the two thousand sixteen A C R: appreciation of fifteen to twenty percent. By our arithmetic, that is three to four percent a year, a little below the four to eight percent claim. The guide does not reconcile its own numbers, which is another reason to treat them with caution.""",
   "Dodge Viper ACR 2016", "ACR 5-YEAR: +15–20%")

sc("""Take an older Viper as a second example. Suppose a buyer pays seventy thousand dollars for a fourth-generation coupé, within the guide's range of fifty-five to ninety thousand. Add insurance and maintenance at six thousand to fourteen thousand a year, and ten years costs sixty to one hundred forty thousand more. The purchase price may be smaller than the cost of keeping the car, by our arithmetic.""",
   "Dodge Viper SRT-10", "A $70K VIPER CAN COST $60K–$140K TO KEEP")
sc("""The point of these examples is not to scare anyone. It is to show that the sticker is only one number. Insurers, mechanics and tyre makers all take a share every year. And the market takes its share too, up or down. The honest answer to what a Viper costs is always a range, never a single figure.""",
   "Dodge Viper garage", "A RANGE, NEVER ONE NUMBER")
# ---------- 7. THE REAL COST ----------
ch("Putting it together")
sc("""Let us build one example, with every caveat. A buyer pays the average two hundred ninety-three thousand, eight hundred forty-six dollars for an A C R. They insure it and maintain it for ten years, at seventy-five thousand to one hundred forty-five thousand dollars, by our arithmetic from the guide. They store it mostly, and drive a few thousand miles a year.""",
   "Dodge Viper ACR", "AN EXAMPLE BUYER")
sc("""If the car holds its value, the ten-year cost of ownership is the running costs, about seventy-five to one hundred forty-five thousand dollars. If it falls by a quarter, the cost goes up by about seventy-three thousand. If it rises by a quarter, the cost goes down by the same. That is how large the swing from the market can be.""",
   "Dodge Viper ACR", "±25% OF THE CAR = ±$73,000")
sc("""The Corvette Z R one gives a comparison. A twenty thirteen car sold for one hundred thirty-two thousand dollars at Mecum Indianapolis, according to Vette Vues, against a new price of one hundred three thousand three hundred in twenty nine. Its gain is about twenty-eight percent. The Viper A C R's gain over its price is not known, because we do not have its new price.""",
   "Corvette ZR1 Mecum", "ZR1 2013: $132,000")
sc("""So what does it cost to own a Viper today? For an older Viper, maybe fifty to ninety thousand dollars to buy, and six thousand to fourteen thousand dollars a year to run. For an A C R, about three hundred thousand dollars to buy, and the same running costs. The cost of owning one is smaller than the cost of getting one.""",
   "Dodge Viper", "ACCESS COSTS MORE THAN OWNING")
sc("""There is a human side too. Tim Kuniskis, the head of S R T, told The Drive in May twenty twenty-six that the Viper will not return, and that it reached the end of its life cycle. If true, every Viper is a finite number of cars: thirty-one thousand, nine hundred eighty-nine, according to Wikipedia. And they are not making more.""",
   "Dodge Viper", "NO SUCCESSOR · 31,989 CARS")
sc("""What did we not find? A price for a set of replacement brakes. An official service schedule. The cost of hard parts, since the Conner Avenue plant closed in twenty seventeen. We found no source on that, and we will not guess. If you own one, those are the numbers we would love to see in the comments.""",
   "Dodge Viper garage", "NOT PUBLISHED: BRAKES, PARTS, SERVICE SCHEDULE")
sc("""Do you think Viper prices will keep rising? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Viper, compare the Viper A C R with the Corvette Z R one, and tell why the Viper was killed twice.""",
   "Dodge Viper", "WILL VIPER PRICES KEEP RISING?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more honest numbers about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video95", "The Real Cost of Owning a Viper Today", [
    "Classic.com, Dodge Viper ACR VX I market: https://www.classic.com/m/dodge/viper/5th-gen/acr/",
    "Automonitor, How much does a Dodge Viper cost? Complete pricing guide 2026: https://automonitor.io/blog/how-much-does-a-dodge-viper-cost/",
    "Wikipedia, Dodge Viper: https://en.wikipedia.org/wiki/Dodge_Viper",
    "Autoblog, 2009 Corvette ZR1 starts at $103,300: https://www.autoblog.com/2008/06/17/2009-corvette-zr1-pricing-and-performance-numbers-released/",
    "Vette Vues, C6 Corvette ZR1 History (2009–2013): https://vette-vues.com/c6-corvette-zr1-history/",
    "Yahoo / The Drive, The Dodge Viper era is dead, head of SRT says (29 May 2026): https://autos.yahoo.com/people-and-culture/articles/dodge-viper-era-dead-head-164100036.html",
], "C")
