import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The sticker price of a Koenigsegg Gemera starts at one point seven million dollars. That is the number everyone repeats. It is not the cost of owning one. In this video we separate what our sources actually document from what is guesswork, and we label our own arithmetic. Some of the numbers you want do not exist in public, and we say so.""",
   "Koenigsegg ownership", "WHAT IT REALLY COSTS TO OWN A KOENIGSEGG")
sc("""Our sources are Motor1, InsideHook, a March twenty twenty-six report on AOL, Wikipedia's Koenigsegg, Gemera and Regera pages, the RM Sotheby's catalogue for a twenty twenty Regera, a Jalopnik factory tour, the U.S. Energy Information Administration and the Census Bureau. One cost website, Automonitor, gives estimates with no stated sources, so we flag every number from it.""",
   "Sources", "SOURCES: MOTOR1 · INSIDEHOOK · AOL · WIKIPEDIA · RM SOTHEBY'S · JALOPNIK · EIA · CENSUS BUREAU · AUTOMONITOR (UNSOURCED ESTIMATES, FLAGGED)")

ch("The price on the paper")
sc("""Start with the base price. Motor1 reported in April twenty twenty that Christian von Koenigsegg told Top Gear the U.S.-spec Gemera starts at one point seven million dollars. InsideHook, in July twenty twenty-four, repeats that figure from Auto Express. Wikipedia's Gemera page itself gives no price, so this comes from press reports, not an official list.""",
   "Base price", "MOTOR1 (13 APR 2020): U.S.-SPEC GEMERA FROM $1.7 M (von KOENIGSEGG TO TOP GEAR) · INSIDEHOOK (29 JULY 2024): $1.7 M (AUTO EXPRESS) · WIKIPEDIA GEMERA PAGE: NO PRICE · OFFICIAL LIST: NOT IN OUR SOURCES")
sc("""Next, the engine choice. InsideHook reports a rumoured additional four hundred thousand dollars for the V8, and its author adds that the total of two point one million is his own calculation. Since the three-cylinder car was dropped, Wikipedia says, in July twenty twenty-four, the V8 is now the only engine. Whether the premium applies to every new order is not stated.""",
   "V8 premium", "INSIDEHOOK: V8 RUMOURED +$400,000 → ~$2.1 M (AUTHOR'S SUM) · WIKIPEDIA: I3 DROPPED JULY 2024 · WHETHER THE PREMIUM IS INCLUDED IN CURRENT ORDERS: NOT IN OUR SOURCES")
sc("""By our arithmetic, four hundred thousand on one point seven million is twenty-three and a half percent. If that rumour holds, a Gemera with the V8 starts at about two point one million. We stress the word rumour. We have no Koenigsegg price list and no dealer confirming this number, so treat two point one as a plausible estimate, not a quote.""",
   "The sum", "$400,000 ÷ $1,700,000 = 23.5% · $1.7 M + $0.4 M = $2.1 M (OUR ARITHMETIC; RUMOURED PREMIUM) · NO PRICE LIST OR DEALER CONFIRMATION IN OUR SOURCES")
sc("""Then comes taxes and fees, which no source we found quantifies for a Koenigsegg. Sales tax depends on the state. In our sources, no buyer discloses a final invoice. So we cannot honestly add a line for tax. What we can do is show what the rate would mean: each one percent of two point one million dollars is twenty-one thousand dollars, by our arithmetic.""",
   "Tax", "TAX / REGISTRATION / DELIVERY FEES: NOT IN OUR SOURCES · 1% × $2.1 M = $21,000 (OUR ARITHMETIC, FOR SCALE ONLY; NOT A PREDICTION)")

ch("The options that double down")
sc("""Options are where Koenigsegg budgets can grow. The RM Sotheby's catalogue for a twenty twenty Regera lists about five hundred one thousand dollars in options on one car. That includes a one hundred seventy thousand dollar clear carbon finish, wheels at fifty-seven thousand dollars, and a dark carbon finish with gold dust at sixty-two thousand.""",
   "Options on a Regera", "RM SOTHEBY'S MONTEREY 2024, LOT 240 (2020 REGERA): OPTIONS ≈ $501,330 · CLEAR CARBON $170,000 · TRESEX AIRCORE WHEELS $57,000 · DARK CARBON WITH GOLD DUST $62,000")
sc("""Wikipedia mentions upgrades of seven hundred ten thousand two hundred dollars on another Regera sold at auction. By our arithmetic, that is thirty-seven percent of the car's nineteen hundred thousand dollar citation price. The Gemera has its own option list, including a Ghost package, but its prices are not in our sources.""",
   "Upgrades", "WIKIPEDIA (REGERA): UPGRADES $710,200 ON ONE AUCTIONED CAR · $710,200 ÷ $1.9 M = 37.4% (OUR ARITHMETIC; CITATION-TITLE PRICE) · GEMERA OPTION PRICES / GHOST PACKAGE COST: NOT IN OUR SOURCES")
sc("""If the Gemera's options follow the Regera pattern, a buyer could add a third or more to the base price. By our arithmetic, five hundred one thousand dollars on one point seven million is twenty-nine and a half percent. That is a thought experiment, not a forecast. It assumes similar option pricing on a different car, which our sources do not show.""",
   "If it followed", "$501,330 ÷ $1.7 M = 29.5% · $1.7 M + $0.50 M = $2.2 M (OUR ARITHMETIC; ASSUMES REGERA-STYLE OPTIONS — NOT SHOWN IN SOURCES FOR THE GEMERA)")

ch("Fuel: what the numbers allow")
sc("""Fuel. The Gemera's V8 runs on E85, Wikipedia says, and has a total range of fourteen hundred sixty-three kilometres, which is nine hundred nine miles. Our sources give no tank size and no consumption figure, so we cannot compute miles per gallon honestly. What we can do is show the pump price for context.""",
   "Fuel", "WIKIPEDIA: V8 ON E85 · TOTAL RANGE 1,463 KM (909 MI) · TANK SIZE / MPG: NOT IN OUR SOURCES → NO CONSUMPTION FIGURE COMPUTED")
sc("""The U.S. Energy Information Administration reported regular gasoline at four dollars twenty-eight cents a gallon for the week of the nineteenth of October twenty twenty-six. That is regular, not E85, and E85 prices are not in our sources. Automonitor estimates fuel for a Jesko at three to six thousand dollars a year at twelve to twenty miles per gallon, but gives no sources.""",
   "Pump price", "EIA: REGULAR GASOLINE $4.284/GAL, WEEK OF 19 OCT 2026 · E85 PRICE: NOT IN OUR SOURCES · AUTOMONITOR (JESKO, UNSOURCED ESTIMATE): FUEL $3,000–6,000/YR AT 12–20 MPG")
sc("""By our arithmetic, at four dollars twenty-eight a gallon, a three thousand dollar fuel bill buys seven hundred gallons, and six thousand buys fourteen hundred. At the estimate's fifteen miles per gallon midpoint, that is roughly ten thousand to twenty-one thousand miles. Real owners drive these cars far less, but our sources give no mileage data.""",
   "Gallons", "$3,000 ÷ $4.284 = 700 GAL · $6,000 ÷ $4.284 = 1,401 GAL · × 15 MPG = 10,500–21,000 MI (OUR ARITHMETIC; 15 MPG = OUR MIDPOINT OF AUTOMONITOR'S RANGE; AUTOMONITOR UNSOURCED)")
sc("""There is one more relevant data point. The auctioned Regera had fifteen hundred twelve miles after four years. By our arithmetic, that is about three hundred seventy-eight miles a year, so at four dollars twenty-eight a gallon and fifteen miles per gallon, fuel would be about one hundred eight dollars a year. That is an illustration from one car, not a typical owner.""",
   "A garage queen", "RM SOTHEBY'S: 1,512 MILES · 4 YEARS · 378 MI/YR · 378 ÷ 15 MPG × $4.284 = $108/YR (OUR ARITHMETIC; 15 MPG ASSUMED; ONE CAR ONLY)")

ch("Service and upkeep")
sc("""Service is the one cost where we have a real receipt. The RM Sotheby's catalogue for the Regera says the third-year service and updates, in spring twenty twenty-four, cost nearly nineteen thousand dollars, and included a technician flown in from Sweden. It is a Regera, not a Gemera, and it covers updates as well as routine work.""",
   "A real service bill", "RM SOTHEBY'S (REGERA LOT 240): THIRD-YEAR SERVICE + UPDATES, SPRING 2024, 'NEARLY $19,000', TECHNICIAN FLOWN FROM SWEDEN · GEMERA SERVICE COSTS: NOT IN OUR SOURCES")
sc("""By our arithmetic, nineteen thousand dollars is one point one percent of the Gemera's one point seven million base price. Spread over a year, that is about fifteen hundred eighty-three dollars a month. But that was the third-year visit, with updates, so a normal year may be less, or more. Our sources do not give a schedule.""",
   "Per month", "$19,000 ÷ $1.7 M = 1.1% · $19,000 ÷ 12 = $1,583/MONTH (OUR ARITHMETIC; SINGLE REGERA BILL, INCLUDES UPDATES; SCHEDULE NOT IN OUR SOURCES)")
sc("""Automonitor estimates dealer maintenance of five to eight thousand dollars a year for a Jesko, and a major service of three to eight thousand. It gives no source. Its own page is inconsistent in places, so we treat it as a rough guess. Notice that the Regera receipt of nineteen thousand sits well above the top of that range.""",
   "A website's guess", "AUTOMONITOR (JESKO, UNSOURCED): DEALER MAINTENANCE $5,000–8,000/YR · MAJOR SERVICE $3,000–8,000 · PAGE INTERNALLY INCONSISTENT · $19,000 REGERA BILL IS 2.4× THE TOP OF THE $8,000 RANGE (OUR ARITHMETIC)")
sc("""Tyres and brakes are in the same Automonitor list: tyres at twelve hundred to twenty-four hundred dollars and more per set, and carbon-ceramic brakes at twelve to twenty-five thousand dollars a set. Wikipedia names the Gemera's Michelin tyres and gives its wheel sizes, but not their price. So the guess is the only figure, and we flag it as one.""",
   "Tyres and brakes", "AUTOMONITOR (JESKO, UNSOURCED): TYRES $1,200–2,400+ PER SET · CARBON-CERAMIC BRAKES $12,000–25,000 PER SET · WIKIPEDIA (GEMERA): MICHELIN PILOT SPORT 4S / CUP 2R, 21 IN FRONT, 22 IN REAR — NO PRICES")

ch("Insurance, storage, depreciation")
sc("""Insurance. Automonitor estimates fourteen to twenty thousand dollars a year for a Jesko, again with no source. Our other sources do not mention insurance at all. Insurance for a car like this depends on the owner, the garage and the policy, so a single number is a weak guide. We include it only to show the possible order of magnitude.""",
   "Insurance", "AUTOMONITOR (JESKO, UNSOURCED): INSURANCE $14,000–20,000/YR · OTHER SOURCES: SILENT ON INSURANCE · GEMERA INSURANCE: NOT IN OUR SOURCES")
sc("""Storage. Automonitor puts storage at two hundred to six hundred dollars a month. By our arithmetic, that is twenty-four hundred to seventy-two hundred dollars a year. Jalopnik's factory tour mentions that Koenigsegg itself stores a number of cars, and that storage holds a full ten percent of total production, but gives no price.""",
   "Storage", "AUTOMONITOR (UNSOURCED): STORAGE $200–600/MONTH → $2,400–7,200/YR (OUR ARITHMETIC) · JALOPNIK TOUR: STORAGE HOLDS 'A FULL TEN PERCENT OF THE TOTAL KOENIGSEGG PRODUCTION' · STORAGE PRICE: NOT STATED")
sc("""Add the three yearly guesses together: dealer maintenance, insurance and storage. By our arithmetic, using Automonitor's low ends, that is five thousand plus fourteen thousand plus twenty-four hundred, or twenty-one thousand four hundred dollars a year. Using the high ends, it is eight thousand plus twenty thousand plus seventy-two hundred, or thirty-five thousand two hundred dollars.""",
   "Yearly total", "LOW: $5,000 + $14,000 + $2,400 = $21,400 · HIGH: $8,000 + $20,000 + $7,200 = $35,200 (OUR ARITHMETIC; ALL FIGURES FROM AUTOMONITOR'S UNSOURCED JESKO ESTIMATES; EXCLUDES FUEL, TYRES, BRAKES)")
sc("""Against a two point one million dollar V8 Gemera, that is one to one point seven percent a year, by our arithmetic. Against Census Bureau data, the median household income in twenty twenty-four was eighty-three thousand seven hundred thirty dollars. So even the low yearly estimate is about a quarter of a median household's gross income.""",
   "In perspective", "$21,400 ÷ $2.1 M = 1.0% · $35,200 ÷ $2.1 M = 1.7% · $21,400 ÷ $83,730 = 25.6% (OUR ARITHMETIC) · CENSUS: MEDIAN HOUSEHOLD INCOME 2024 $83,730")
sc("""Depreciation is where Automonitor says these cars behave differently, retaining sixty-five to eighty-five percent of value over five years. Again, no source. The best evidence we have is the Regera auction: an estimate of two point seven five to three point two five million dollars, against a citation price of one point nine, and the car did not sell.""",
   "Depreciation?", "AUTOMONITOR (UNSOURCED): RETAINS 65–85% OVER 5 YEARS · RM SOTHEBY'S 2024: REGERA ESTIMATE $2.75–3.25 M, NOT SOLD · WIKIPEDIA CITATION TITLE: REGERA $1.9 M")
sc("""By our arithmetic, the auction estimate was forty-five to seventy-one percent above the citation price. But the estimate is not a result. The car did not sell, so the market never confirmed it. Those cars are rare. A seller can set a high estimate, and a buyer can decline. A no-sale tells us the price was not met, not what was.""",
   "Estimate, not result", "$2.75 M ÷ $1.9 M = +44.7% · $3.25 M ÷ $1.9 M = +71.1% (OUR ARITHMETIC) · RESULT: NOT SOLD · FINAL MARKET PRICE: NOT IN OUR SOURCES")

ch("Putting the price in human terms")
sc("""Now scale. Kelley Blue Book put the average new vehicle in August twenty twenty-six at fifty thousand and eighty-nine dollars. By our arithmetic, one point seven million dollars is about thirty-four average new vehicles. A two point one million dollar V8 Gemera is about forty-two. That is a comparison of prices, not of value.""",
   "Average new cars", "KBB: AVERAGE NEW VEHICLE, AUG 2026 $50,089 · $1.7 M ÷ $50,089 = 33.9 · $2.1 M ÷ $50,089 = 41.9 (OUR ARITHMETIC)")
sc("""Against the median household income of eighty-three thousand seven hundred thirty dollars, one point seven million is about twenty and a third years of gross household income, by our arithmetic. Two point one million is about twenty-five years. Census income is before tax, and we use a median, so this only gives a sense of scale.""",
   "Years of income", "$1.7 M ÷ $83,730 = 20.3 YR · $2.1 M ÷ $83,730 = 25.1 YR (OUR ARITHMETIC; CENSUS 2024 MEDIAN HOUSEHOLD INCOME, GROSS)")
sc("""Per month, the Census income is about sixty-nine hundred seventy-eight dollars. By our arithmetic, the Gemera's yearly upkeep guess of twenty-one thousand four hundred dollars is three point one months of gross income, and the high guess of thirty-five thousand two hundred is five months. Again, a scale comparison, not a household budget.""",
   "Months of income", "$83,730 ÷ 12 = $6,978/MONTH · $21,400 ÷ $6,978 = 3.1 MONTHS · $35,200 ÷ $6,978 = 5.0 MONTHS (OUR ARITHMETIC)")

ch("The cost of waiting")
sc("""There is also a cost that does not show up in a ledger: time. Wikipedia says the Gemera was unveiled in March twenty twenty and originally scheduled for production in twenty twenty-two. AOL reports production starting in March twenty twenty-six. By our arithmetic, that is six years after the reveal, and about four after the original date.""",
   "The wait", "WIKIPEDIA: UNVEILED 3 MARCH 2020; ORIGINALLY SCHEDULED FOR 2022 · AOL (30 MAR 2026): PRODUCTION STARTING · 6 YEARS FROM REVEAL; ~4 FROM ORIGINAL DATE (OUR ARITHMETIC)")
sc("""Motor1 reported in April twenty twenty that a McLaren dealer in Charlotte was listing a Gemera build slot with VIN zero zero one. The listing price was not given. That suggests buyers were paying for places in the queue years ahead of delivery, but our sources do not say how much anyone paid or whether the sale completed.""",
   "Queue slots", "MOTOR1 (13 APR 2020): McLAREN CHARLOTTE BUILD SLOT, VIN 001, GRAY WITH ORANGE INTERIOR · PRICE AND OUTCOME: NOT IN OUR SOURCES")
sc("""If a buyer paid the base price in deposits and installments years ahead, the money was tied up for years. We have no source on Koenigsegg's payment schedule, so we cannot calculate the cost of that. For scale only: at five percent a year, one million dollars would earn fifty thousand dollars a year, by our arithmetic.""",
   "Opportunity cost", "PAYMENT SCHEDULE / DEPOSIT SIZE: NOT IN OUR SOURCES · $1 M × 5% = $50,000/YR (OUR ARITHMETIC, ILLUSTRATIVE RATE; NOT A CLAIM ABOUT ANY BUYER)")

ch("Depreciation, run through the numbers")
sc("""Let us test Automonitor's claim that these cars keep sixty-five to eighty-five percent of their value over five years. It is unsourced, so this is a what-if, not a finding. Start with a two point one million dollar V8 Gemera. By our arithmetic, keeping eighty-five percent leaves one million seven hundred eighty-five thousand, a loss of three hundred fifteen thousand dollars.""",
   "Best case", "WHAT-IF ONLY: AUTOMONITOR'S UNSOURCED 85% RETENTION · $2.1 M × 0.85 = $1,785,000 · LOSS $315,000 (OUR ARITHMETIC)")
sc("""At sixty-five percent, the same car would be worth one million three hundred sixty-five thousand dollars, a loss of seven hundred thirty-five thousand. Spread over five years, by our arithmetic, that is sixty-three thousand to one hundred forty-seven thousand dollars a year, which is three to seven times the yearly upkeep guess at the low end.""",
   "Worse case", "$2.1 M × 0.65 = $1,365,000 · LOSS $735,000 · ÷ 5 = $63,000–147,000/YR vs UPKEEP $21,400 → 2.9× TO 6.9× (OUR ARITHMETIC; WHAT-IF ONLY)")
sc("""That reshuffles the cost list. In this what-if, the largest yearly cost is not service, insurance or storage. It is the value that quietly leaves the car. But a rare, limited car can also hold or gain value, and our sources show no resale result for the Gemera, so we cannot say which side of the range is realistic.""",
   "The biggest line", "WHAT-IF: DEPRECIATION $63,000–147,000/YR > UPKEEP $21,400–35,200/YR (OUR ARITHMETIC) · REAL GEMERA RESALE DATA: NOT IN OUR SOURCES")
sc("""There is a data point for a sister model. The auctioned Regera had an estimate above its original price, and it did not sell. That is the opposite of a classic depreciation story, but a single no-sale proves little. Wikipedia also says the Regera sold out in June twenty seventeen, which shows demand, though not what resale prices later looked like.""",
   "A sister model", "RM SOTHEBY'S: ESTIMATE $2.75–3.25 M vs CITATION PRICE $1.9 M; NOT SOLD · WIKIPEDIA: REGERA SOLD OUT 13 JUNE 2017 · REGERA RESALE PRICES BEYOND THIS LOT: NOT IN OUR SOURCES")

ch("The cost per mile of a car you barely drive")
sc("""Here is an uncomfortable calculation. The auctioned Regera covered about three hundred seventy-eight miles a year. If its owner paid the low upkeep guess of twenty-one thousand four hundred dollars, by our arithmetic that is about fifty-seven dollars per mile, before any depreciation. That mixes one car's mileage with a website's guess, so it is purely illustrative.""",
   "Cost per mile", "$21,400 ÷ 378 MI = $56.6/MI (OUR ARITHMETIC; COMBINES RM SOTHEBY'S MILEAGE WITH AUTOMONITOR'S UNSOURCED UPKEEP ESTIMATE — ILLUSTRATIVE ONLY)")
sc("""Even at the high upkeep guess, thirty-five thousand two hundred, the figure rises to about ninety-three dollars a mile. Add the what-if depreciation of sixty-three thousand and the cost per mile goes past two hundred dollars. For comparison, our sources give no figure for a typical car, so we offer none. The point is how low mileage amplifies fixed costs.""",
   "More per mile", "$35,200 ÷ 378 = $93.1/MI · ($21,400 + $63,000) ÷ 378 = $223/MI (OUR ARITHMETIC; WHAT-IF, NOT A MEASURED COST)")
sc("""Of course, owners may drive more than the Regera at auction. The Gemera is a four-seat grand tourer with a total range of nine hundred nine miles, which suggests it was designed to be driven. Our sources give no owner mileage data, so we cannot tell whether Gemera owners drive more. If you do, the cost per mile drops quickly.""",
   "If you drive it", "WIKIPEDIA: GEMERA TOTAL RANGE 909 MI · 'DESIGNED TO BE DRIVEN' = OUR INFERENCE FROM THE GRAND-TOURER LAYOUT · GEMERA OWNER MILEAGE: NOT IN OUR SOURCES")
sc("""For scale, at five thousand miles a year, the low upkeep guess works out to about four dollars twenty-eight a mile, by our arithmetic. That is a coincidence with the gasoline price per gallon, nothing more. At ten thousand miles it is two dollars fourteen. Fixed costs fall as use rises, but the fuel and tyre costs rise with it.""",
   "More miles", "$21,400 ÷ 5,000 = $4.28/MI · $21,400 ÷ 10,000 = $2.14/MI (OUR ARITHMETIC; ILLUSTRATIVE MILEAGES; EXCLUDES FUEL AND TYRES)")

ch("A closer look at the price history")
sc("""The same company sold cars at a very different price level not long ago. Wikipedia says that in two thousand eight Koenigsegg produced eighteen cars at an average price of about one million dollars each. By our arithmetic, the Gemera's base price of one point seven million is seventy percent above that average, without adjusting for inflation.""",
   "Then", "WIKIPEDIA: 2008 — 18 CARS, AVERAGE ~$1 M · $1.7 M ÷ $1 M = +70% (OUR ARITHMETIC; NOT INFLATION-ADJUSTED — INFLATION FIGURES NOT IN OUR SOURCES)")
sc("""The Regera, in between, has a citation price of one point nine million dollars on Wikipedia, and one point five million pounds. So the Gemera's base is below the Regera's quoted figure, but the Gemera seats four and the Regera two. By our arithmetic, one point seven million over four seats is four hundred twenty-five thousand dollars a seat, against nine hundred fifty thousand for the Regera.""",
   "Per seat", "WIKIPEDIA CITATION TITLES: REGERA $1.9 M / £1.5 M · $1.7 M ÷ 4 = $425,000/SEAT · $1.9 M ÷ 2 = $950,000/SEAT (OUR ARITHMETIC; BASE PRICES, FUN FRAMING ONLY)")
sc("""And the horsepower per dollar. Twenty-three hundred horsepower for two point one million is about nine hundred thirteen dollars per horsepower, by our arithmetic. The Regera, at fifteen hundred for one point nine million, is about twelve hundred sixty-seven. On that measure, the Gemera is the cheaper way to buy horsepower, if both sets of claims hold.""",
   "Per horsepower", "$2.1 M ÷ 2,300 = $913/HP; $1.7 M ÷ 2,300 = $739/HP · $1.9 M ÷ 1,500 = $1,267/HP (OUR ARITHMETIC; CLAIMED POWER, MIXED SOURCES)")
sc("""Total volume gives the last perspective. Three hundred Gemeras at the one point seven million base is five hundred ten million dollars, by our arithmetic. The Regera's eighty-five cars at one point nine would be about one hundred sixty-two million. These are base-price totals only, with no options, and assume every car sells at those prices.""",
   "Totals", "300 × $1.7 M = $510 M · 85 × $1.9 M = $161.5 M (OUR ARITHMETIC; BASE PRICES, EXCLUDES OPTIONS, ASSUMES ALL AT LIST)")

ch("Questions buyers would ask")
sc("""Could you finance one? Our sources say nothing about loans, leases or payment plans for a Koenigsegg, so we cannot give a monthly payment. For scale only, by our arithmetic, a one point seven million dollar price spread over ten years with no interest would be about fourteen thousand one hundred sixty-seven dollars a month. Real financing would cost more, and we have no rate.""",
   "Financing", "FINANCING TERMS: NOT IN OUR SOURCES · $1.7 M ÷ 120 = $14,167/MONTH (OUR ARITHMETIC; ZERO INTEREST, ILLUSTRATIVE ONLY)")
sc("""Could you resell it quickly? The RM Sotheby's catalogue adds a clue. It notes that California rules require such a Regera to be sold to a dealer or an out-of-state resident. That is a note about one auction, not a general law that we can verify, but it hints that the buyer pool and the paperwork can limit how easily a car like this changes hands.""",
   "Reselling", "RM SOTHEBY'S (REGERA LOT): CALIFORNIA REQUIRES SALE TO A DEALER OR OUT-OF-STATE RESIDENT · GENERAL LEGAL POSITION: NOT VERIFIED IN OUR SOURCES")
sc("""Could you service it anywhere? The Regera's service visit included a technician flown in from Sweden, according to the catalogue. Wikipedia says Koenigsegg's factory is in Ängelholm, Sweden, after its early days in Olofström. If you live far from Sweden, that suggests travel costs, but our sources do not itemise them.""",
   "Where to service it", "RM SOTHEBY'S: TECHNICIAN FLOWN IN FROM SWEDEN · WIKIPEDIA: FACTORY IN ÄNGELHOLM (EARLY 2000s ONWARD; NEW FACTORY JULY 2023) · TRAVEL COSTS: NOT IN OUR SOURCES")
sc("""Could you get parts? Our sources do not say. Jalopnik's factory tour does say that all carbon work and wheels are made in-house at Koenigsegg, which might matter for repairs, since there is one supplier. But that tour is undated and about an earlier era, so we use it only as a pointer, not a finding about today's parts supply.""",
   "Parts", "JALOPNIK TOUR (UNDATED, AGERA/ONE:1 ERA): CARBON WORK AND WHEELS MADE IN-HOUSE · 'ONE SUPPLIER' = OUR INFERENCE · CURRENT PARTS AVAILABILITY / PRICES: NOT IN OUR SOURCES")
sc("""Could you modify it? The catalogue's option list shows how much of the price is personalisation: clear carbon, wheels, a gold-dust carbon finish. Wikipedia lists a Ghost package for the Gemera. What these options cost on the Gemera is not in our sources, which is why our scenario borrows the Regera's figure, and why we call it a scenario.""",
   "Personalisation", "RM SOTHEBY'S REGERA OPTIONS ≈ $501,330 · WIKIPEDIA (GEMERA): OPTIONAL GHOST PACKAGE · GEMERA OPTION PRICES: NOT IN OUR SOURCES")

ch("The sticker, rebuilt")
sc("""Let us rebuild the cost with everything labelled. Base price one point seven million, from Motor1. V8 premium four hundred thousand, rumoured by InsideHook. Options, unknown for the Gemera, but five hundred one thousand on one Regera. Yearly upkeep, twenty-one to thirty-five thousand, from an unsourced website. Service bill, nineteen thousand, from one Regera.""",
   "Recap", "RECAP: BASE $1.7 M (MOTOR1) · V8 +$0.4 M (RUMOUR, INSIDEHOOK) · OPTIONS UNKNOWN (REGERA ≈ $501,330) · UPKEEP $21,400–35,200/YR (AUTOMONITOR, UNSOURCED, OUR SUM) · SERVICE $19,000 (ONE REGERA BILL)")
sc("""By our arithmetic, add the base, the V8 rumour and a Regera-style options figure, and the purchase reaches about two point six million dollars. Then five years of the unsourced upkeep estimate adds about one hundred seven thousand to one hundred seventy-six thousand. The total is a scenario, not a quote, and it excludes tax, fuel, tyres and depreciation.""",
   "Scenario", "$1.7 M + $0.4 M + $0.50 M = $2.6 M · 5 × $21,400 = $107,000; 5 × $35,200 = $176,000 (OUR ARITHMETIC; SCENARIO ONLY — EXCLUDES TAX, FUEL, TYRES, DEPRECIATION)")
sc("""By our arithmetic again, five years of upkeep is only four to seven percent of the purchase price in that scenario. The money is in the purchase itself. If these cars hold their value, as Automonitor claims, the real cost may be mostly the capital tied up. If they do not, depreciation dwarfs everything else. Our sources cannot settle which.""",
   "Where the money is", "$107,000 ÷ $2.6 M = 4.1% · $176,000 ÷ $2.6 M = 6.8% (OUR ARITHMETIC) · DEPRECIATION: NOT SETTLED BY OUR SOURCES (AUTOMONITOR UNSOURCED; REGERA NO-SALE)")

ch("What the sources do not say")
sc("""What is missing. An official Gemera price list. The cost of the Gemera's options, and the Ghost package. A real owner's service bill for a Gemera. An insured value. A sale result for a Gemera. And E85 pump prices. If you own or service one of these cars, and can share a document, tell us in the comments and we will update.""",
   "Koenigsegg ownership", "NOT IN OUR SOURCES: OFFICIAL PRICE LIST · GEMERA OPTION PRICES · OWNER SERVICE BILLS · INSURANCE · RESALE RESULTS · E85 PRICES · TAX / FEES")
sc("""So what does it really cost to own a Koenigsegg? On documented numbers: one point seven million to start, a rumoured two point one with the V8, a nineteen thousand dollar service on a Regera, and an auction estimate that did not sell. Everything else here is an estimate. Subscribe to Pickup Reality for the other Koenigsegg stories this week.""",
   "Koenigsegg ownership", "SUBSCRIBE: PICKUP REALITY")

save("video159", "What It Really Costs to Own a Koenigsegg", [
    "Motor1, Koenigsegg Gemera build slot already available at McLaren dealer, 13 Apr 2020: https://www.motor1.com/news/409351/koenigsegg-gemera-build-slot-sale/",
    "InsideHook (Tobias Carroll), V8 Koenigsegg supercar buyers pay an extra $400,000, 29 Jul 2024: https://www.insidehook.com/autos/v8-koenigsegg-supercar-buyers-extra-400000/amp",
    "AOL (Car and Driver), The Koenigsegg Gemera is finally starting production, 30 Mar 2026: https://www.aol.com/articles/koenigsegg-gemera-finally-starting-production-210300723.html",
    "Wikipedia, Koenigsegg Gemera: https://en.wikipedia.org/wiki/Koenigsegg_Gemera",
    "Wikipedia, Koenigsegg Regera: https://en.wikipedia.org/wiki/Koenigsegg_Regera",
    "RM Sotheby's, 2020 Koenigsegg Regera, Monterey 2024, lot 240",
    "Jalopnik, Koenigsegg factory tour",
    "U.S. Energy Information Administration, weekly retail gasoline prices, week of 2026-10-19",
    "U.S. Census Bureau, median household income 2024",
    "Kelley Blue Book, average new vehicle transaction price, August 2026",
    "Automonitor.io, Koenigsegg Jesko ownership cost estimates (unsourced estimates)",
], "C")
