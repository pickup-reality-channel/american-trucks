import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""A Ferrari F forty cost about four hundred thousand dollars when it was new. Today the sources we read show sale prices from about three and a half million dollars to eleven million. But the purchase price is only the beginning. One recent preparation bill for a low-mileage F forty, itemised line by line, ran to tens of thousands of dollars before the car even went on sale. This is what it really costs to own a Ferrari F forty.""",
   "Ferrari F40", "WHAT IT REALLY COSTS TO OWN A FERRARI F40")
sc("""We will go through the purchase price, the recent auction results, the maintenance schedule, and the itemised bills we could find. Every figure comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. And where a source gives no figure, we will not invent one.""",
   "Ferrari F40", "EVERY NUMBER IS SOURCED")

ch("What it cost new")
sc("""Start with the original price. Wikipedia says the F forty's launch price was about four hundred thousand dollars, roughly five times the price of the two eighty-eight G T O. The car was built for the fortieth anniversary of Ferrari, and it was the last car approved by Enzo Ferrari. Production was planned at four hundred cars, and in the end one thousand, three hundred eleven were built.""",
   "Ferrari F40 launch", "F40 NEW: ~$400,000 (WIKIPEDIA)")
sc("""Demand outran supply immediately. Wikipedia says that in nineteen eighty-nine, speculators sold cars for up to more than seven times the list price. By our arithmetic, seven times four hundred thousand is at least two million, eight hundred thousand dollars. That was the first price spike, in the very first years of the car's life, and it did not last.""",
   "Ferrari F40 speculators", "1989: UP TO 7× LIST PRICE ≈ $2.8M+ (OUR ARITHMETIC)")
sc("""Wikipedia gives two more data points. Nigel Mansell's F forty sold for one million pounds in nineteen ninety. In twenty fourteen, the same page says, Mansell's car sold at Bonhams for five hundred forty-three thousand, three hundred seventy-five pounds. The pound figures are in different years, so we do not convert them. We only note that the price fell by nearly half between those two sales.""",
   "Nigel Mansell", "MANSELL'S F40: £1M (1990) → £543,375 (2014, BONHAMS)")
sc("""By our arithmetic, five hundred forty-three thousand is about fifty-four percent of one million, so the drop was about forty-six percent in nominal pounds. That is a reminder that the F forty has not gone up in a straight line. A buyer in nineteen ninety might have lost money by twenty fourteen, before the car became the multi-million dollar machine it is today.""",
   "Ferrari F40 price history", "A 46% NOMINAL DROP IN £ BETWEEN THOSE TWO SALES (OUR ARITHMETIC)")

ch("The price curve")
sc("""Classic Motorsports puts the F forty at about one million dollars in twenty nineteen. It then reports a Mecum sale at two and a half million dollars in twenty twenty-two, and says values were four million dollars or so in twenty twenty-three. By our arithmetic, that is two and a half times the twenty nineteen price by twenty twenty-two, and a fourfold increase by twenty twenty-three.""",
   "Ferrari F40 value", "~$1M (2019) → $2.5M (2022) → ~$4M (2023) · CLASSIC MOTORSPORTS")
sc("""Now the twenty twenty-five results from Sotheby's. A nineteen eighty-nine Swiss car sold for two million, nine hundred fifty-eight thousand, one hundred twenty-five Swiss francs in October, with eleven thousand, eight hundred eighty-two kilometres. A restored nineteen eighty-nine car sold for two million, eight hundred seventeen thousand, five hundred euros in May. Both are in the same range as the twenty twenty-two Mecum result.""",
   "Ferrari F40 auction", "2025: 1989 SWISS CAR CHF 2,958,125 · RESTORED 1989 CAR €2,817,500")
sc("""A nineteen ninety-one U S-specification car sold for three million, five hundred eighty thousand dollars in February twenty twenty-five, with three thousand, four hundred thirty-five miles. Sotheby's notes it has non-adjustable suspension. A nineteen ninety car with about thirty-five years in storage and three hundred sixty kilometres sold for three million, eight hundred fifty-five thousand dollars in August.""",
   "Ferrari F40 US-spec", "2025: 1991 US-SPEC $3.58M (3,435 MI) · 1990 STORAGE CAR $3.855M (360 KM)")
sc("""Alain Prost's nineteen ninety F forty sold for three million, eight hundred eighty-six thousand, two hundred fifty dollars in December, with two thousand, nine hundred sixty-one miles. By our arithmetic, that is about thirty-one thousand dollars above the storage car, a little under one percent more. Celebrity provenance mattered less here than the very low mileage that the two cars shared.""",
   "Alain Prost", "PROST'S 1990 F40: $3,886,250 · +$31K OVER THE STORAGE CAR (OUR ARITHMETIC)")
sc("""At the top, a nineteen ninety-three F forty L M built by Michelotto sold for eleven million, five thousand dollars in August. Sotheby's says it has about seven hundred sixty horsepower and is one of nineteen Michelotto examples. That is a racing derivative, not a road car. Our own arithmetic puts it at more than two and a half times a standard car's sale price.""",
   "Ferrari F40 LM", "1993 F40 LM BY MICHELOTTO: $11,005,000 (AUG 2025)")
sc("""Autopian reports one more: a nineteen ninety-two F forty sold for five million, two hundred thirty thousand dollars at ModaMiami in February twenty twenty-six. By our arithmetic, that is about thirty-five percent above Prost's car, and the highest standard road car result in our sources. So a standard car today ranges from about three and a half to over five million, depending on mileage, year and condition.""",
   "ModaMiami", "FEB 2026: 1992 F40 SOLD FOR $5,230,000 (AUTOPIAN)")
sc("""Let us be careful with that range. These are individual sales, not an index. Different years, different mileage, different countries, different currencies, different auction houses. We have not found a source that publishes a median or an average, so we do not claim one. The honest statement is that standard cars have recently sold between roughly two point eight million and five point two million.""",
   "Ferrari F40 market", "RANGE, NOT AN AVERAGE: ~$2.8M TO ~$5.2M (OUR SUMMARY OF CITED SALES)")

ch("The Iacocca car")
sc("""Autopian tells the story of one particular car. Lee Iacocca's nineteen ninety-one F forty, chassis eighty-seven three forty-five, was delivered in December nineteen ninety, ordered at Modena. It sold for over one million dollars with two hundred eighteen miles in two thousand six, then again at RM Auctions in January twenty twelve with two hundred eighty-three miles.""",
   "Lee Iacocca", "IACOCCA'S 1991 F40: 218 MI (2006) → 283 MI (2012)")
sc("""By our arithmetic, the car covered sixty-five miles in six years. That is about eleven miles a year. It is a collector's car in the purest sense: bought to be preserved, not driven. And in twenty twenty-six, with three hundred twenty miles, it was prepared for sale at Monterey. By our arithmetic, thirty-seven miles in about fourteen years.""",
   "Ferrari F40 mileage", "65 MILES IN 6 YEARS · 37 MILES IN ~14 YEARS (OUR ARITHMETIC)")
sc("""And here is the bill. Autopian itemised the preparation at about thirty-four thousand dollars. A coolant tank, four thousand, four hundred twenty-six. Engine service, nearly twenty-one thousand. Tyres, two thousand, six hundred thirty-seven. A headlamp switch, four thousand, two hundred. Those four items alone add up to about thirty-two thousand dollars, by our arithmetic.""",
   "Ferrari F40 service bill", "COOLANT TANK $4,426 · ENGINE SERVICE ~$21K · TYRES $2,637 · SWITCH $4,200")
sc("""A caution on that article. Its headline says sixty thousand dollars and its body says forty thousand, while the itemised list totals about thirty-four thousand. We cannot tell which is right, so we use the itemised figures, which we can add up. The lesson stands either way: a car that barely moved can still need tens of thousands of dollars of work before a sale.""",
   "Autopian F40 article", "ARTICLE FIGURES DISAGREE: $60K HEADLINE · $40K BODY · ~$34K ITEMISED")
sc("""An earlier invoice helps with scale. Autopian says the same car had a service in two thousand eight that cost about twelve thousand, six hundred dollars. By our arithmetic, the twenty twenty-six preparation was about two and three-quarter times that, in nominal dollars. We do not adjust for inflation, since our sources do not, and the two jobs may not cover the same work.""",
   "Ferrari F40 service history", "2008 SERVICE ~$12,600 → 2026 PREP ~$34K (OUR ARITHMETIC)")

ch("The maintenance schedule")
sc("""Classic Motorsports describes the routine. The timing belts are replaced every three years. The engine can stay in the car, but the seats and the rear firewall must come out to reach them. Fluids are changed yearly, which it prices at about one thousand dollars. It calls the F forty very durable, and cheaper to run than the F fifty.""",
   "Ferrari F40 service", "BELTS EVERY 3 YEARS · FLUIDS YEARLY ~$1,000 (CLASSIC MOTORSPORTS)")
sc("""Fuel is the long-term issue. Classic Motorsports says the fuel bladders can leak after about ten years, though U S cars had aluminium tanks. Fuel lines are replaced about every ten years. The cars are now nearly forty years old, so every owner has to deal with this, and the cost depends on the car, the market and the shop.""",
   "Ferrari F40 fuel system", "FUEL BLADDERS CAN LEAK AFTER ~10 YEARS · LINES ~EVERY 10 YEARS")
sc("""Italpassion, in May twenty twenty-five, gives a European view. It cites an unnamed YouTuber who quoted a small inspection at seventy thousand euros, covering belts, fluids and fuel tanks. Treat that figure with caution: it is a single anonymous claim, and the itemised list from the same article does not obviously add up to it, as we will see.""",
   "Italpassion", "'SMALL INSPECTION' €70,000 (UNNAMED YOUTUBER, VIA ITALPASSION)")
sc("""The itemised list. An annual overhaul, three to seven thousand euros. Timing belts, eight to ten thousand. Gearbox or clutch work, fifteen thousand euros or more. Fuel tanks, fifteen to twenty thousand euros per pair. Pirelli tyres, two thousand, five hundred euros. The article values the car at two to four million euros.""",
   "Italpassion F40 costs", "ANNUAL €3–7K · BELTS €8–10K · GEARBOX/CLUTCH €15K+ · TANKS €15–20K · TYRES €2.5K")
sc("""Add up the belts, the tanks and the overhaul, by our arithmetic: eight plus fifteen plus three is twenty-six thousand euros at the low end, and ten plus twenty plus seven is thirty-seven thousand at the high end. That is well short of seventy thousand. Adding a gearbox job of fifteen thousand and tyres brings the high end to about fifty-four and a half thousand.""",
   "Italpassion arithmetic", "BELTS+TANKS+OVERHAUL: €26K–€37K · WITH CLUTCH AND TYRES: UP TO ~€54.5K (OUR ARITHMETIC)")
sc("""So the itemised figures do not reach seventy thousand euros, even at the top. That does not prove the claim wrong. The inspection may have included other work that the article does not list. It does show that the seventy thousand figure is not supported by the article's own line items, and we would not plan a budget around it without a quote.""",
   "Ferrari F40 cost check", "THE €70K CLAIM IS NOT SUPPORTED BY THE ARTICLE'S OWN LINE ITEMS (OUR ARITHMETIC)")

ch("Putting it in perspective")
sc("""Now our own arithmetic on the running cost, using Classic Motorsports' yearly fluids, one thousand dollars, and the belt interval of three years. Over thirty years, that is ten belt services and thirty fluid services. Our sources do not give a price for the belt job in dollars, so we cannot total it. The fluid service alone comes to thirty thousand dollars over thirty years.""",
   "Ferrari F40 running cost", "30 YEARS OF FLUID SERVICES ≈ $30,000 (OUR ARITHMETIC) · BELT COST NOT IN OUR SOURCES")
sc("""Compare the maintenance to the price. Using the thirty-four thousand dollar preparation as a single big bill against a three point eight eight six million dollar sale, by our arithmetic, that is about zero point nine percent of the car's value. Using the Italpassion high end of fifty-four and a half thousand euros against a two million euro low value, it is about two and three-quarter percent.""",
   "Ferrari F40 ownership", "BIG SERVICE ≈ 0.9%–2.7% OF CAR VALUE (OUR ARITHMETIC)")
sc("""That is the odd thing about owning an F forty. The service bills are large for a normal car, but small against the value. The real cost is the money tied up in the car, and what the market does with it. The nineteen ninety to twenty fourteen drop on Mansell's car shows that this risk is real, even though the recent trend was upward.""",
   "Ferrari F40 investment", "THE BIGGEST COST IS THE MONEY TIED UP IN THE CAR (OUR READING)")
sc("""Compare with a truck. Our twenty twenty-seven Truck Buyer's Guide covers what a new pickup costs. A top-trim full-size truck costs a small fraction of the cheapest F forty sale in our sources. We do not quote a truck price here since the guide has them, but the contrast is the point: this is a different kind of purchase, closer to art than to transport.""",
   "Ford F-150", "A TRUCK IS A DIFFERENT KIND OF PURCHASE — SEE THE TRUCK BUYER'S GUIDE")
sc("""The F forty is also, per Wikipedia, a car with no door handles, no carpets and no sound system, so the cost of ownership does not buy comfort. It buys a way of driving, a place in history, and for some owners, a stored asset. Wikipedia quotes a nineteen ninety estimate that only about ten percent of owners used their cars regularly.""",
   "Ferrari F40 interior", "~10% OF OWNERS DROVE THEIR CARS REGULARLY (1990 ESTIMATE, WIKIPEDIA)")
sc("""Before the verdict, what we could not find. We could not find a published average price, a published figure for the timing belt job in dollars, or insurance and storage costs. We also could not verify the seventy thousand euro inspection. If you own an F forty, or work on them, we would be glad to hear from you in the comments, with where your figure comes from.""",
   "Ferrari F40", "WHAT OUR SOURCES DO NOT TELL US")

ch("The real cost")
sc("""So what does it really cost? A purchase price that, in our sources, ranges from about two point eight to five point two million dollars for standard road cars. Annual fluids of about one thousand dollars. Belts every three years. Fuel tanks every ten or so, with a euro quote of fifteen to twenty thousand per pair. And large bills when a low-mileage car is prepared.""",
   "Ferrari F40", "PURCHASE $2.8M–$5.2M · FLUIDS ~$1K/YR · BELTS EVERY 3 YRS · TANKS EVERY ~10 YRS")
sc("""The recent headline price is about three point nine million dollars, from Prost's car. We use that as our reference figure, since it is a documented sale of a standard road car with very low mileage and a famous owner. It is a single data point, and your result could differ by a million dollars either way, as the other sales show.""",
   "Alain Prost's Ferrari F40", "REFERENCE PRICE: ~$3.9M (PROST'S CAR, DEC 2025)")
ch("The price per horsepower")
sc("""Here is a way to see the price curve. At launch, about four hundred thousand dollars for four hundred seventy-eight metric horsepower is about eight hundred thirty-seven dollars per horsepower, by our arithmetic. At Prost's sale price, three million, eight hundred eighty-six thousand dollars, it is about eight thousand, one hundred thirty dollars per horsepower.""",
   "Ferrari F40 engine", "PRICE PER HP: ~$837 (NEW) → ~$8,130 (PROST'S CAR) (OUR ARITHMETIC)")
sc("""By our arithmetic, Prost's sale price is about nine and three-quarter times the launch price, in nominal dollars. We do not adjust for inflation, because our sources do not give an inflation figure. A buyer who paid list price in nineteen eighty-seven would, on a car sold at that price, have multiplied the original money by nearly ten, before any maintenance bills.""",
   "Ferrari F40 return", "PROST'S SALE ≈ 9.7× THE LAUNCH PRICE, NOMINAL (OUR ARITHMETIC)")
sc("""Now the racing derivative. The F forty L M that sold for eleven million, five thousand dollars is described by Sotheby's as having about seven hundred sixty horsepower. By our arithmetic, that is about fourteen thousand, four hundred eighty dollars per horsepower, almost twice the figure for Prost's road car. Racing history carries a premium, but the sources do not say how much of the price is the engine.""",
   "Ferrari F40 LM", "F40 LM: ~$14,480 PER HP (OUR ARITHMETIC)")

ch("Price per mile")
sc("""Another lens is price per distance driven. The storage car sold for three million, eight hundred fifty-five thousand dollars with three hundred sixty kilometres on the clock. By our arithmetic, that is about ten thousand, seven hundred dollars for every kilometre it has ever travelled. The sale price makes it a very expensive way to cover ground.""",
   "Ferrari F40 mileage", "STORAGE CAR: ~$10,700 PER KILOMETRE EVER DRIVEN (OUR ARITHMETIC)")
sc("""Prost's car sold with two thousand, nine hundred sixty-one miles. By our arithmetic, that is about one thousand, three hundred thirteen dollars per mile. The U S-specification car, with three thousand, four hundred thirty-five miles, works out at about one thousand, forty-three dollars per mile. Lower mileage did not lower the price; if anything, as these cases show, it was the reverse.""",
   "Ferrari F40 odometer", "PROST: ~$1,313/MILE · US-SPEC: ~$1,043/MILE (OUR ARITHMETIC)")
sc("""A note on method. These ratios are not a valuation. A price per mile ignores condition, history, specification and the mood of the room on auction day. We show them only to illustrate that the people paying these prices are not buying transport. They are buying a very particular object, and, on the evidence of these cars, a particularly unused one.""",
   "Ferrari F40", "RATIOS ILLUSTRATE, THEY DO NOT VALUE (OUR READING)")

ch("What the whole fleet is worth")
sc("""Here is a thought experiment, labelled as such. Wikipedia counts one thousand, three hundred eleven cars. If every one were worth Prost's three million, eight hundred eighty-six thousand dollars, the fleet would be worth about five billion dollars, by our arithmetic. That is a toy number: the cars differ widely, and the racing derivatives are worth much more.""",
   "Ferrari F40 production", "1,311 × $3.89M ≈ $5.1 BILLION — A THOUGHT EXPERIMENT (OUR ARITHMETIC)")
sc("""It does show scale. Four hundred cars were planned. Wikipedia says the final count was one thousand, three hundred eleven, some sources say up to one thousand, three hundred fifteen. By our arithmetic, that is more than three times the plan. A car built in that quantity is not a unique object, and yet buyers are paying millions for each one.""",
   "Ferrari F40 production", "PLANNED 400 · BUILT 1,311 (UP TO 1,315): 3.3× THE PLAN (OUR ARITHMETIC)")
sc("""The sources disagree on how many were American. Wikipedia and Sotheby's say two hundred thirteen. The DK Engineering archive says about six hundred. That matters for ownership, because Sotheby's says the U S cars have a non-adjustable suspension and aluminium tanks, which affects both the bills and the market. We cannot settle the count, so we report both.""",
   "Ferrari F40 United States", "US CARS: 213 (WIKIPEDIA, SOTHEBY'S) VS ~600 (DK ENGINEERING)")
sc("""The sources also differ on emissions equipment. Wikipedia says the early cars had no catalytic converters until nineteen ninety. The DK Engineering archive says catalytic converters arrived from nineteen ninety-one. A one-year difference, but for a collector it matters: it can change which car is considered the most original, and what a service involves.""",
   "Ferrari F40 exhaust", "CATALYTIC CONVERTERS: FROM 1990 (WIKIPEDIA) VS 1991 (DK ENGINEERING)")

ch("Where the money goes")
sc("""Let us sum up the costs as a list, using only sourced figures. Purchase: roughly two point eight to five point two million dollars for standard road cars in our sources. Annual fluids: about one thousand dollars. Belts: every three years. Fuel tanks: about every ten years, fifteen to twenty thousand euros per pair in the Italpassion list. A large preparation: about thirty-four thousand dollars on the Iacocca car.""",
   "Ferrari F40 costs", "PURCHASE · FLUIDS · BELTS · TANKS · PREPARATION")
sc("""Here is our arithmetic for a ten-year plan on the Italpassion figures, in euros. Annual overhaul at three to seven thousand, ten times, is thirty to seventy thousand. Three belt jobs at eight to ten thousand is twenty-four to thirty thousand. One pair of fuel tanks is fifteen to twenty thousand. The total is sixty-nine to one hundred twenty thousand euros over ten years.""",
   "Ferrari F40 ten-year cost", "10-YEAR PLAN: €69K–€120K (OUR ARITHMETIC FROM ITALPASSION'S ITEMS)")
sc("""Per year, by our arithmetic, that is roughly seven thousand to twelve thousand euros. Against a car worth two to four million euros, per the same article, that is between about two-tenths and six-tenths of a percent a year. Again, this excludes insurance, storage, gearbox work, tyres and any unexpected repair, because our sources do not give those figures.""",
   "Ferrari F40 yearly cost", "~€6.9K–€12K A YEAR, ~0.2%–0.6% OF VALUE (OUR ARITHMETIC)")

ch("What the cost does not buy")
sc("""One more point on what ownership does not include. Wikipedia describes a spartan car: no door handles, no glove box, no leather, no carpets, no door panels and no sound system. Classic Motorsports adds that it has no A B S. Owners pay seven figures for a car that, by the standards of its day, offered less equipment than a family sedan.""",
   "Ferrari F40 interior", "NO HANDLES · NO GLOVE BOX · NO CARPETS · NO SOUND SYSTEM · NO ABS")
sc("""What it does offer, per Wikipedia, is performance. A twin-turbocharged two point nine litre V eight with four hundred seventy-eight metric horsepower. A weight of one thousand, two hundred fifty-four kilograms in Europe. A rear-wheel-drive layout with a five-speed manual gearbox. The first independent test recorded zero to a hundred kilometres per hour in four point seven seconds.""",
   "Ferrari F40 performance", "478 PS · 1,254 KG · RWD · 5-SPEED · 0–100 KM/H IN 4.7 S")
sc("""And it offers the story: the last Ferrari approved by Enzo Ferrari, built for the fortieth anniversary of the company, thirteen months from the start of the project on the tenth of June, nineteen eighty-six to the unveiling on the twenty-first of July, nineteen eighty-seven. Each of those facts sits behind the price, and none of them depends on a service bill.""",
   "Maranello", "THE LAST FERRARI ENZO APPROVED · 13 MONTHS FROM START TO UNVEILING")
sc("""Racing versions are rarer still. Wikipedia says ten Competizione-specification cars were built, two L M and eight Competizione, with seven hundred horsepower. The G T E had six hundred twenty and seven were built, winning at Anderstorp in nineteen ninety-five and ninety-six. Nineteen racing cars in all. This explains why the Michelotto car in the Sotheby's list sits so far above the road cars.""",
   "Ferrari F40 racing", "10 COMPETIZIONE-SPEC · 7 GTE · 19 RACING CARS IN ALL (WIKIPEDIA)")

sc("""Which F forty would you buy, the ordinary car or the one with the famous owner? And would you drive it? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the F forty, compare it with the Porsche nine fifty-nine, and tell the story of the last car Enzo Ferrari approved. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video115", "What It Really Costs to Own a Ferrari F40", [
    "Wikipedia, Ferrari F40: https://en.wikipedia.org/wiki/Ferrari_F40",
    "Classic Motorsports, Ferrari F40: the truth about living with a legend: https://classicmotorsports.com/articles/ferrari-f40-how-you-spend-million/",
    "Sotheby's, The six most expensive Ferrari F40s: https://www.sothebys.com/en/articles/the-six-most-expensive-ferrari-f40s",
    "The Autopian, Lee Iacocca's Ferrari F40 preparation and sale",
    "Italpassion, Ferrari F40 running costs (May 2025)",
], "C")
