import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""To buy a new Ford GT, money was not enough. You had to apply, wait to be chosen, and sign a contract promising not to sell the car for two years. One famous owner broke that promise, and Ford took him to court. Today we look at the real cost of a Ford GT, from the price on the contract to what it costs to keep one running, and why that contract existed at all.""",
   "Ford GT 2017", "THE REAL COST OF A FORD GT")
sc("""Here is the twist. The car that Ford sold for around half a million dollars was later valued much higher. So for most owners, the biggest cost of a Ford GT was not depreciation. It was everything else. Insurance, storage, tires, brakes, and the rules that came with it.""",
   "Ford GT parked garage", "IT DIDN'T LOSE VALUE")
sc("""Every number in this video comes from a published source, listed in the description. Where a figure is an estimate, or our own arithmetic, we will say so clearly. Let's start with the price.""",
   "Ford GT front", "EVERY NUMBER IS SOURCED")
sc("""First, a reminder of what you get. A carbon fiber, mid-engined supercar with a three point five liter twin-turbo V6, six hundred forty-seven horsepower, a top speed of two hundred sixteen miles per hour, and zero to sixty in two point nine seconds, according to Gear Patrol. Wikipedia says power rose to six hundred sixty horsepower for twenty twenty.""",
   "Ford GT EcoBoost V6", "647-660 HP, 216 MPH")

# ---------- 1. THE PRICE ----------
ch("The price")
sc("""Gear Patrol listed the twenty seventeen Ford GT at a starting price of about four hundred fifty thousand dollars, and Jalopnik also reported a starting price of four hundred fifty thousand. Car Showroom, an Australian outlet, said Ford's estimate for later cars was around five hundred thousand dollars, with a slight increase expected for the twenty nineteen batch.""",
   "Ford GT price", "~$450,000 TO ~$500,000")
sc("""Compare that with the first-generation Ford GT. Wikipedia says the two thousand five GT had a suggested retail price of about one hundred forty thousand dollars. In about twelve years, the price of a new Ford GT more than tripled. The new car was a very different machine, with a carbon fiber body and a racing program behind it.""",
   "Ford GT 2005", "2005 GT: $139,995")
sc("""And compare it with the original. Wikipedia says the nineteen sixties G T forty, built for competition, had a purchase price of about five thousand two hundred pounds. Of course, money had very different value then. But it shows how Ford's Le Mans car moved from a racing tool to a collector's object.""",
   "Ford GT40 1960s", "GT40: £5,200")
sc("""Then there were the special editions. Wikipedia lists a twenty twenty Liquid Carbon edition, with exposed carbon fiber bodywork, at about seven hundred fifty thousand dollars. The track-only GT Mark two, forty-five built, at about one point two million each. And the final GT Mark four, with sixty-seven planned at about one point seven million dollars.""",
   "Ford GT Liquid Carbon", "SPECIAL EDITIONS: $750K TO $1.7M")
sc("""Think about what those special editions mean. The Mark two is track-only, so for about one point two million dollars, you get a Ford GT you cannot legally drive on a public road. Wikipedia says only forty-five were built. The Mark four, with sixty-seven planned, costs about one point seven million, close to four times the price of a regular GT, by our own arithmetic.""",
   "Ford GT Mk II track", "TRACK-ONLY FOR $1.2M")
sc("""For comparison, the U S Census Bureau reported a median household income of about eighty thousand six hundred dollars in twenty twenty-three. So a regular Ford GT cost more than five and a half years of a typical household's income, by our own arithmetic, before taxes and running costs.""",
   "American suburb", "~5.5 YEARS OF MEDIAN INCOME")

# ---------- 2. THE APPLICATION ----------
ch("You had to apply")
sc("""Now, why could you not simply buy one? Car Showroom reported that buyers had to submit an application to Ford for review. If accepted, they received further instructions. Ford reportedly favored buyers who would drive the car rather than treat it as a status symbol, and previous ownership of Ford performance cars helped.""",
   "Ford GT application", "AN APPLICATION, NOT A PURCHASE")
sc("""Production was deliberately small. Car Showroom said Ford began with five hundred cars, then doubled to one thousand, then added three hundred fifty more. When the extra cars were announced, the application window reopened from the eighth of November to the seventh of December. Demand, the outlet said, was out of control all over the world.""",
   "Ford GT production line", "1,350 CARS FOR THE WORLD")
sc("""Why go to all this trouble? Look at what happened with the first-generation GT. Wikipedia says that when the two thousand five car arrived, some buyers paid more than one hundred thousand dollars above the sticker price, and the first production car was sold at a charity auction for five hundred fifty-seven thousand dollars. The extra money went to sellers, not to Ford.""",
   "Ford GT 2005 dealer", "2005: +$100,000 OVER STICKER")
sc("""In our reading, the application process for the new GT was a response to that. Ford could not stop demand, but it could control who got the cars and when they could sell them. That is our interpretation, not an official Ford statement. But it explains why the second-generation GT came with so many rules.""",
   "Ford GT 2017 reveal", "LEARNING FROM 2005")
sc("""Jalopnik reported that the plan was to build two hundred fifty cars a year, but Ford built only one hundred thirty-eight for the twenty seventeen model year. Multimatic, the Canadian company that built the cars in Markham, Ontario, had never worked at that scale. So even approved buyers often had to wait.""",
   "Ford GT Multimatic", "138 BUILT IN YEAR ONE")
sc("""That means the real cost of a Ford GT also included time. Applying, waiting for an answer, and then waiting for a build slot at a factory that was building far fewer cars than planned. For a buyer, the question was not only, can I afford it. It was also, will Ford choose me, and how long will I wait.""",
   "Ford GT waiting", "THE COST OF WAITING")
sc("""Here is the twist. Choosing buyers is not only about rewarding fans. It protects the brand. A car that is driven at events, on tracks, and in public, by people who love it, is better publicity than one sitting in a speculator's warehouse. And that leads us to the contract.""",
   "Ford GT on track", "WHY FORD CHOSE ITS BUYERS")

# ---------- 3. THE CONTRACT ----------
ch("The contract")
sc("""Autoblog reported that buyers approved for the first five hundred Ford GTs agreed not to resell their cars for twenty-four months. The goal was simple. Stop flippers from buying a car at the list price and immediately selling it for a profit, while real fans waited.""",
   "Ford GT contract signing", "NO RESALE FOR 24 MONTHS")
sc("""Then John Cena, the wrestler and actor, became the most famous test of that rule. Autoblog reported that he received his Ford GT in late September twenty seventeen and sold it in October. In November, Ford sued him, seeking seventy-five thousand dollars in damages, and a buyback at the original price plus any profit he made.""",
   "John Cena", "FORD v JOHN CENA")
sc("""Cena first claimed he did not know about the resale restriction, Autoblog said, and in February twenty eighteen he asked a judge to dismiss the case. In June twenty eighteen, the case was settled out of court for an undisclosed amount. Cena's lawyers said Ford would donate that amount to charity. Cena said, I love the Ford GT and apologize to Ford.""",
   "courthouse", "SETTLED, MONEY TO CHARITY")
sc("""So the real cost of a Ford GT included something unusual. Your freedom to sell it. For two years, the car was legally yours to drive, but not to flip. For most owners, that was fine. For anyone hoping for a quick profit, it was a very expensive mistake.""",
   "Ford GT keys", "THE PRICE OF FREEDOM")

# ---------- 4. VALUE ----------
ch("What it's worth")
sc("""Now the twist from the start. What is a Ford GT worth today? Hagerty's valuation tool listed a twenty twenty-two Ford GT at about seven hundred eighty-eight thousand dollars in January twenty twenty-six, with a change of minus two percent at that time.""",
   "Ford GT 2022", "HAGERTY: ~$788,000")
sc("""AutoMonitor, a valuation site, gives much higher numbers. It estimates typical second-generation GTs at about nine hundred thousand to one point five million dollars, and Heritage editions at about one point two to one point eight million. AutoMonitor does not cite sources for most of these figures, so treat them as rough estimates. Hagerty's figure is the more conservative one.""",
   "Ford GT Heritage Edition", "AUTOMONITOR: $900K-$1.5M (EST.)")
sc("""Either way, the car did not lose value the way most new cars do. From a starting price of about four hundred fifty thousand to five hundred thousand dollars, a value of about seven hundred eighty-eight thousand is a gain of roughly fifty to seventy-five percent, by our own arithmetic.""",
   "Ford GT auction", "+50% TO +75%")
sc("""That changes the math of ownership completely. With most cars, depreciation is the biggest cost. With the Ford GT, the car itself could act like a store of value, as long as the owner followed the rules, kept the mileage reasonable, and kept the car in excellent condition.""",
   "Ford GT low mileage", "A STORE OF VALUE?")
sc("""And the first-generation GT followed the same path. AutoMonitor estimates a two thousand five GT in good condition at about three hundred fifty thousand to four hundred fifty thousand dollars, and mentions a low-mileage example that sold for six hundred sixty-five thousand dollars at auction in twenty twenty-four. That is several times its original price of about one hundred forty thousand.""",
   "Ford GT 2005 collector", "2005 GT: UP TO ~$665K")

# ---------- 5. RUNNING COSTS ----------
ch("Running costs")
sc("""So if the car holds its value, what does it actually cost to keep? Here we rely on AutoMonitor's estimates, which do not cite sources, so take them as a rough guide. Insurance first. AutoMonitor estimates about fifteen thousand to twenty-five thousand dollars a year to insure a second-generation Ford GT.""",
   "Ford GT insurance", "INSURANCE: ~$15K-$25K/YEAR (EST.)")
sc("""Why so much? Because the insured value is high, the car is rare, and parts are expensive. A carbon fiber body panel on a car built in small numbers is not something a local body shop keeps on the shelf. If a Ford GT is damaged, repairs can take a long time and cost a fortune.""",
   "Ford GT carbon body", "RARE PARTS, HIGH RISK")
sc("""Put that insurance estimate next to the car's value. Fifteen thousand to twenty-five thousand dollars a year, against a Hagerty value of about seven hundred eighty-eight thousand, is roughly two to three percent of the car's value every year, by our own arithmetic. That is the price of protecting an asset that cannot easily be replaced.""",
   "Ford GT detail", "~2-3% OF VALUE PER YEAR")
sc("""Routine maintenance, AutoMonitor estimates, costs about five thousand to ten thousand dollars a year. Tires are another five figures over time. AutoMonitor says the car uses Michelin Pilot Sport tires, typically replaced every eight thousand to twelve thousand miles, and estimates about two thousand to three thousand five hundred dollars a year.""",
   "Ford GT wheel tire", "MAINTENANCE: ~$5K-$10K/YEAR (EST.)")
sc("""Brakes can be one of the biggest single bills. AutoMonitor says the GT uses carbon-ceramic brakes, and estimates fifteen thousand to twenty thousand dollars for a full replacement, or about one thousand five hundred to two thousand five hundred dollars a year spread out over time.""",
   "Ford GT carbon ceramic brakes", "BRAKES: $15K-$20K FULL SET (EST.)")
sc("""Here is a detail that changes the tire math. If a set lasts eight thousand to twelve thousand miles, as AutoMonitor says, and an owner drives about three thousand miles a year, one set could last roughly three to four years, by our own arithmetic. But tires also age, so collectors often replace them for safety long before the tread is gone.""",
   "Ford GT Michelin tires", "ONE SET: ~3-4 YEARS AT 3,000 MI")
sc("""Fuel is next. AutoMonitor lists fuel economy of about eleven to fifteen miles per gallon, and estimates four thousand to seven thousand dollars a year for fuel. That depends heavily on how far you drive. Many GT owners drive their cars only a few thousand miles a year.""",
   "Ford GT gas station", "11-15 MPG (EST.)")
sc("""Some quick arithmetic of our own. At eleven to fifteen miles per gallon, three thousand miles a year would use roughly two hundred to two hundred seventy-five gallons of fuel. So AutoMonitor's estimate assumes much more driving than many collectors do. For a car that mostly sits in a garage, fuel is one of the smallest costs.""",
   "Ford GT fuel cap", "~200-275 GALLONS AT 3,000 MI")
sc("""And there is storage. A car like this needs a secure, climate-controlled garage. AutoMonitor estimates storage and climate control at about four thousand to eight thousand dollars a year, if you do not have the right space at home. Even parking a Ford GT costs money.""",
   "climate controlled car storage", "STORAGE: ~$4K-$8K/YEAR (EST.)")

# ---------- 6. THE YEARLY BILL ----------
ch("The yearly bill")
sc("""Add it all up, and AutoMonitor estimates the yearly cost of running a second-generation Ford GT at about thirty-one thousand five hundred to fifty-six thousand dollars, not including depreciation or major repairs. In the best case, that is close to forty percent of the median household income every year. In the worst case, about seventy percent, by our own arithmetic.""",
   "Ford GT calculator", "~$31,500-$56,000 A YEAR (EST.)")
sc("""Now divide that by the miles. If an owner drives three thousand miles a year, thirty-one thousand five hundred to fifty-six thousand dollars works out to about ten dollars fifty cents to eighteen dollars seventy cents per mile, by our own arithmetic. Every trip to the grocery store in a Ford GT costs more than a nice dinner.""",
   "Ford GT road", "~$10.50-$18.70 PER MILE")
sc("""Over five years, that would be about one hundred fifty-seven thousand to two hundred eighty thousand dollars, by our own arithmetic. On top of a purchase price of around half a million. So a five-year Ford GT experience could involve roughly six hundred fifty thousand to seven hundred eighty thousand dollars of spending, before selling the car.""",
   "Ford GT five years", "5 YEARS: ~$157K-$280K TO RUN")
sc("""And measured against income, those five years of running costs alone equal about two to three and a half years of the median American household income, by our own arithmetic. That is before the purchase price, before taxes, and before any surprise repair on a carbon fiber supercar.""",
   "American family home", "2-3.5 YEARS OF MEDIAN INCOME")
sc("""But here is the twist again. If the car is then worth about seven hundred eighty-eight thousand dollars, as Hagerty's valuation suggested in twenty twenty-six, the owner could get much of that money back. The real cost of a Ford GT depends almost entirely on what it is worth when you sell it.""",
   "Ford GT sale", "THE RESALE DECIDES EVERYTHING")
sc("""Of course, values can fall. Hagerty's number in January twenty twenty-six was down two percent. Collector car markets go up and down, and nobody can promise what a car will be worth in five or ten years. Buying a Ford GT as an investment is a bet, not a guarantee.""",
   "Ford GT market", "A BET, NOT A GUARANTEE")
sc("""There is also a hidden trade-off. The more an owner drives the car, the more the running costs rise, and the more value the car may lose with every mile. So many owners face a strange choice. Enjoy the car and pay for it, or protect its value and barely use it. That tension is part of the real cost.""",
   "Ford GT odometer", "DRIVE IT OR PROTECT IT?")

# ---------- 7. THE CHEAPER WAYS ----------
ch("The cheaper ways in")
sc("""Is there a cheaper way to own a Ford GT? The first-generation car is the obvious option. Wikipedia says Ford built four thousand thirty-eight of them, with a supercharged five point four liter V8 making five hundred fifty horsepower. AutoMonitor's estimate of about three hundred fifty thousand to four hundred fifty thousand dollars is still a lot, but it is a fraction of a modern GT.""",
   "Ford GT 2005 red", "THE 2005 GT ROUTE")
sc("""And it has a very different character. The two thousand five GT was designed as a tribute to the G T forty, with a big V8 and a manual gearbox. The twenty seventeen car is a carbon fiber, turbocharged, race-bred machine with a seven-speed automatic, according to Gear Patrol. Two very different experiences under the same name.""",
   "Ford GT 2005 interior", "TRIBUTE vs RACE CAR")
sc("""And the special versions cost even more. Ford built Heritage editions in the famous Gulf racing colors of the G T forty. AutoMonitor's figure for second-generation Heritage editions is about one point two to one point eight million dollars. Again, these are estimates without cited sources.""",
   "Ford GT Gulf Heritage", "HERITAGE: $1.2M-$1.8M (EST.)")
sc("""For most people, though, the realistic way to experience a Ford GT is at a show, a museum, or a race. Ford built so few that most enthusiasts will never sit in one. That rarity is exactly what keeps their value high.""",
   "Ford GT car show", "MOST WILL NEVER SIT IN ONE")

# ---------- 8. WHAT FORD GOT ----------
ch("What Ford got out of it")
sc("""So why did Ford build a car that so few could buy? Because the GT was never about volume. Wikipedia says that in twenty sixteen, a Ford Chip Ganassi Racing GT won its class at Le Mans, exactly fifty years after the G T forty's nineteen sixty-six win. That result, and the story around it, was worth far more to Ford than the profit on a few cars.""",
   "Ford GT Le Mans 2016", "LE MANS 2016: THE REAL PRIZE")
sc("""Gear Patrol reported that the GT's racing success even pushed Porsche to redesign its nine eleven R S R race car for twenty seventeen, moving the engine to the middle of the car. And in April twenty twenty-six, Ford reported that the GT Mark four lapped the Nürburgring Nordschleife in six minutes fifteen point nine seven seven seconds, the third fastest car ever there.""",
   "Ford GT Mk IV Nürburgring", "MK IV: 6:15.977")
sc("""So the cost of a Ford GT to Ford itself was a racing program, a small factory partnership, and years of careful control over who got the cars. The return was a legend. And the application and contract were part of protecting that legend.""",
   "Ford GT40 and Ford GT", "PROTECTING A LEGEND")

# ---------- 9. THE ANSWER ----------
ch("The answer")
sc("""So what is the real cost of a Ford GT? About four hundred fifty thousand to five hundred thousand dollars to buy, if Ford accepted your application. A contract that stopped you from selling it for two years. And, by AutoMonitor's estimates, about thirty-one thousand to fifty-six thousand dollars a year to insure, maintain, fuel, and store it.""",
   "Ford GT", "THE REAL COST")
sc("""But unlike most new cars, the Ford GT did not simply lose value. Hagerty valued a twenty twenty-two car at about seven hundred eighty-eight thousand dollars in January twenty twenty-six. For owners who followed the rules, the biggest cost was keeping the car, not buying it. And for the one owner who broke the rules, the cost included a lawsuit.""",
   "Ford GT blue", "KEEPING IT COSTS MORE THAN BUYING IT")
sc("""In the end, the Ford GT had three prices. Money, to buy and maintain it. Time, to apply and wait. And freedom, because for two years you could not sell it. Most supercars only ask for the first. The Ford GT asked for all three, and that is exactly what made it special.""",
   "Ford GT rear", "MONEY, TIME, FREEDOM")
sc("""So if you ever see a Ford GT on the road, remember what it took. An application that Ford had to approve, a wait for one of only a few hundred cars a year, a two-year promise not to sell, and tens of thousands of dollars a year just to keep it ready to drive.""",
   "Ford GT highway", "REMEMBER WHAT IT TOOK")
sc("""Would you sign a two-year contract to buy a Ford GT? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Ford GT, compare it with the original G T forty, and tell the story of the man who made Ford beat Ferrari.""",
   "Ford GT40", "WOULD YOU SIGN IT?")
sc("""And if you want a Ford you can actually buy without an application, our twenty twenty-seven Truck Buyer's Guide is linked in the description, with real numbers on the trucks most people buy. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150 dealership", "SUBSCRIBE: PICKUP REALITY")

save("video79", "The Real Cost of a Ford GT (And Why Owners Had to Sign a Contract)", [
    "Gear Patrol, The car that forced Porsche to redesign its fastest 911 (May 2017): https://www.gearpatrol.com/cars/a352077/ford-gt-review-specs-images-porsche-911-ferrari-488gtb/",
    "Wikipedia, Ford GT: https://en.wikipedia.org/wiki/Ford_GT",
    "Wikipedia, Ford GT40: https://en.wikipedia.org/wiki/Ford_GT40",
    "Jalopnik, Ford missed its production target for the first year of the Ford GT: https://jalopnik.com/1827701915",
    "Car Showroom, Ford will build 350 more GTs: https://www.carshowroom.com.au/news/ford-will-build-350-more-gts-books-open-november-8th/",
    "Autoblog, John Cena and Ford settle over flipped GT (June 2018): https://www.autoblog.com/2018/06/19/john-cena-ford-gt-flip-settlement",
    "Hagerty valuation tools, 2022 Ford GT (Jan 2026): https://www.hagerty.com/valuation-tools/ford/gt/2022/2022-ford-gt",
    "AutoMonitor, How much does a Ford GT cost? (estimates, sources not cited): https://automonitor.io/blog/how-much-does-a-ford-gt-cost/",
    "KTVU / Fox, Census 2023 median household income: https://ktvu.com/news/how-much-american-household-earned-2023-census",
    "Ford, Ford GT Mk IV makes Nürburgring history (Apr 2026): https://www.at.ford.com/us/en/home/news-media/news/2026/4/ford-gt-mk-iv-makes-nuerburgring-history-with-third-fastest-lap-.html",
], "C")
