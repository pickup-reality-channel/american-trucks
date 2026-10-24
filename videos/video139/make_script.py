import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""A Porsche nine eighteen Spyder cost eight hundred forty-five thousand dollars new. One sold in twenty twenty-six for nearly three million. And the people who publish its running costs disagree about almost everything: a replacement battery is quoted at fifty to eighty thousand dollars by one source, and eighty to one hundred fifty thousand by another. This is what it really costs to own a Porsche nine eighteen, and what nobody has actually published.""",
   "Porsche 918 Spyder", "WHAT IT REALLY COSTS TO OWN A PORSCHE 918")
sc("""We read Wikipedia, Porsche's own press material, two specialist guides, the recall reports, and the auction results. Here is the catch. Porsche publishes no price list for nine eighteen service, and the two guides we found are a magazine-style buyer's guide and a repair shop's marketing page. So every running-cost figure in this video is an estimate from someone, and we always say whose.""",
   "Porsche 918 Spyder", "SOURCES: WIKIPEDIA · PORSCHE · STUTTCARS · REPASI MOTORWERKS (A SHOP) · RECALL REPORTS · AUCTIONS · RUNNING COSTS = THIRD-PARTY ESTIMATES")

ch("The purchase price")
sc("""Start with the sticker. Wikipedia gives the base price as about eight hundred forty-five thousand dollars in the United States, or seven hundred eighty-one thousand euros. The Weissach package added eighty-four thousand dollars. By our arithmetic, a Weissach car started at nine hundred twenty-nine thousand dollars before any individual options.""",
   "Porsche 918 price", "BASE ~$845,000 / €781,000 · WEISSACH PACKAGE +$84,000 → ~$929,000 (WIKIPEDIA; OUR ARITHMETIC)")
sc("""Put that in context with the Census Bureau's median household income for twenty twenty-four, eighty-three thousand, seven hundred thirty dollars. By our arithmetic, the base price was ten point one years of median household income, and the Weissach starting price eleven point one years. These are gross incomes, before tax.""",
   "918 price vs median income", "$845,000 ≈ 10.1 YEARS · $929,000 ≈ 11.1 YEARS OF MEDIAN HOUSEHOLD INCOME ($83,730, CENSUS) (OUR ARITHMETIC)")
sc("""Against the average new vehicle, fifty thousand, eighty-nine dollars in August twenty twenty-six according to Kelley Blue Book, the base nine eighteen was sixteen point nine times as much. That is our arithmetic, and it compares a twenty fifteen list price with a twenty twenty-six average, so it is only a rough sense of scale.""",
   "918 price vs average new car", "$845,000 ÷ $50,089 ≈ 16.9× (KBB AUG 2026; OUR ARITHMETIC) · 2015 PRICE vs 2026 AVERAGE: ROUGH SCALE ONLY")
sc("""How many cars were there? Nine hundred eighteen, as the name says, with two hundred ninety-four for the United States according to Wikipedia. Production ran from September twenty thirteen to June twenty fifteen, and the car sold out in December twenty fourteen. Stuttcars says about two hundred thirty were Weissach cars. That figure comes from the guide itself, so we treat it as an estimate.""",
   "918 production", "918 UNITS · 294 US (WIKIPEDIA) · SOLD OUT DEC 2014 · ~230 WEISSACH (STUTTCARS, UNSOURCED ESTIMATE)")

ch("What it is worth now")
sc("""This is the part that changes the whole question. The duPont Registry says a standard nine eighteen sold for two million, nine hundred sixty thousand dollars in June twenty twenty-six. That car had four hundred twenty miles. By our arithmetic, that is three point five times the base price.""",
   "918 resale", "STANDARD 2015, 420 MI: $2,960,000 = 3.5× $845,000 BASE (DUPONT REGISTRY; OUR ARITHMETIC)")
sc("""A Weissach car in Riviera Blue, with one thousand, two hundred sixty-seven miles, sold at Broad Arrow on the twenty-fifth of April for four million, six hundred eighty thousand dollars. By our arithmetic, that is five times the nine hundred twenty-nine thousand dollar starting price, though the actual car was probably optioned above that, and the sources do not give its original sticker.""",
   "918 Weissach resale", "WEISSACH, 1,267 MI: $4,680,000 (BROAD ARROW, 25 APRIL 2026) ≈ 5.0× $929,000 STARTING PRICE (OUR ARITHMETIC) · ORIGINAL STICKER NOT GIVEN")
sc("""The record belongs to a one-of-one Pure Orange car, sold at Mecum Kissimmee in January twenty twenty-six for six million, fifty thousand dollars, according to the duPont Registry. Against the base price, our arithmetic says seven point two times. But it was a special order, so its original price was higher, and the comparison is only an upper bound.""",
   "918 record", "$6,050,000 · MECUM KISSIMMEE, JAN 2026 (DUPONT REGISTRY) ≈ 7.2× BASE PRICE (OUR ARITHMETIC) · SPECIAL ORDER: ORIGINAL PRICE HIGHER")
sc("""Now the median, which is less dramatic than the headlines. The duPont Registry puts the median for standard cars at two million, one hundred sixty-eight thousand, eight hundred thirty-six dollars across forty-eight price points. For Weissach cars, three million, thirty-two thousand, five hundred. By our arithmetic, that is two point six times and three point three times the starting prices.""",
   "918 median values", "MEDIAN STANDARD $2,168,836 (48 PRICE POINTS) ≈ 2.6× BASE · WEISSACH $3,032,500 ≈ 3.3× $929,000 (DUPONT; OUR ARITHMETIC)")
sc("""Stuttcars gives a price ladder by mileage, again as its own estimate. Under one thousand miles, two point two to two point five million dollars. One to five thousand miles, one point nine to two point two. Five to ten thousand, one point six to one point nine. Over ten thousand, one point five to one point seven. The ladder shows what mileage might cost an owner, and it also shows that the six-figure running costs we are about to see are small beside the value of the car.""",
   "918 value by mileage", "STUTTCARS ESTIMATES: <1,000 MI $2.2–2.5M · 1–5K $1.9–2.2M · 5–10K $1.6–1.9M · 10K+ $1.5–1.7M (GUIDE'S OWN FIGURES)")
sc("""Check that against the auction. The four hundred twenty-mile car at two point nine six million is above Stuttcars' top estimate for cars under a thousand miles, which is two point five million. So the guide's ladder is already behind the market, or the car was exceptional. Our sources do not say which.""",
   "Guide vs auction", "420-MILE CAR $2.96M vs GUIDE'S <1,000-MILE RANGE $2.2–2.5M (STUTTCARS; DUPONT) · WHICH IS RIGHT: NOT STATED")

ch("The mileage question")
sc("""The mileage on these cars is itself a cost. The June twenty twenty-six car had four hundred twenty miles after roughly eleven years. By our arithmetic, that is about thirty-eight miles a year. The Riviera Blue car, at one thousand, two hundred sixty-seven, is about one hundred fifteen miles a year. Those are rough, since the cars were not necessarily delivered in the same month.""",
   "918 mileage", "420 MI ÷ ~11 YEARS ≈ 38 MI/YEAR · 1,267 MI ÷ ~11 ≈ 115 MI/YEAR (OUR ARITHMETIC; DELIVERY DATES NOT GIVEN)")
sc("""Stuttcars recommends that the car be driven at least once a month. A shop that works on nine eighteens says the same kind of thing in a different way: its low-mileage owner budget assumes two to three thousand miles a year. We note that a car driven only thirty-eight miles a year is a car that is, in practice, being stored rather than used.""",
   "918 usage", "GUIDE: DRIVE AT LEAST MONTHLY (STUTTCARS) · SHOP'S 'LOW-MILEAGE' BUDGET = 2,000–3,000 MI/YEAR (REPASI) · 38 MI/YEAR = STORED, NOT USED (OUR OBSERVATION)")

ch("Routine service")
sc("""Now the running costs. Two sources, two very different pictures. Stuttcars, the buyer's guide, says an annual service at an authorized Porsche dealer costs five to ten thousand dollars. It adds that twenty thousand dollars or more a year is a reasonable planning figure, and in its own FAQ it says ten thousand or more. The guide contradicts itself, so we show both.""",
   "918 annual service, guide", "STUTTCARS: ANNUAL SERVICE $5,000–10,000 · 'PLAN FOR $20,000+' · FAQ: $10,000+ (THE GUIDE'S OWN FIGURES; INTERNALLY INCONSISTENT)")
sc("""Repasi Motorwerks, a Porsche specialist in Connecticut, gives a much lower baseline: two thousand, eight hundred fifty to four thousand, four hundred dollars for an annual service. That includes oil and filter at eight hundred to twelve hundred, a multi-point inspection at one thousand to fifteen hundred, and a brake fluid flush at four to six hundred. This is the shop's own price estimate, published on a page that sells its services.""",
   "918 annual service, shop", "REPASI MOTORWERKS: ANNUAL $2,850–4,400 · OIL $800–1,200 · INSPECTION $1,000–1,500 · BRAKE FLUID $400–600 (SHOP ESTIMATE; MARKETING PAGE)")
sc("""Put the two side by side. The guide's five to ten thousand dollar range, against the shop's two thousand, eight hundred fifty to four thousand, four hundred. By our arithmetic, the guide's low end is about 1.8 times the shop's low end, and the guide's high end is about 2.3 times the shop's. Neither source says why they differ, and neither cites a Porsche price list.""",
   "Service estimate gap", "GUIDE $5,000–10,000 vs SHOP $2,850–4,400 → LOW END ×1.75 · HIGH END ×2.27 (OUR ARITHMETIC) · NEITHER CITES A PRICE LIST")
sc("""The shop also lists bigger services. At two years: spark plugs, air filter, and transmission fluid, totalling sixty-five hundred to ten thousand dollars. At four years: coolant, drive belt, brake fluid and a hybrid system exam, ten to sixteen thousand dollars. These are, again, its estimates.""",
   "918 interval services", "REPASI: 2-YEAR SERVICE $6,500–10,000 · 4-YEAR SERVICE $10,000–16,000 (SHOP ESTIMATES)")
sc("""What does that mean per mile? Repasi's budget for a low-mileage owner, two to three thousand miles a year, is seventy-two hundred to ten thousand, eight hundred dollars a year. By our arithmetic, if the owner drives three thousand miles, that is two dollars forty a mile at the low end, and if the owner drives two thousand, five dollars forty a mile at the high end.""",
   "918 service cost per mile", "$7,200 ÷ 3,000 MI = $2.40/MI · $10,800 ÷ 2,000 MI = $5.40/MI (REPASI BUDGET; OUR ARITHMETIC)")

ch("Tyres and brakes")
sc("""Tyres. Stuttcars gives five to seven thousand dollars for a full set of Michelin Pilot Sport Cup Twos. Repasi gives twenty-five hundred to four thousand dollars for a standard set, thirty-five hundred to fifty-five hundred for a high-performance set, and over six thousand for track compounds. The ranges overlap, but they are not describing the same set.""",
   "918 tyres", "GUIDE: PS CUP 2 SET $5,000–7,000 · SHOP: STANDARD $2,500–4,000 · HIGH-PERF $3,500–5,500 · TRACK $6,000+ (ESTIMATES)")
sc("""Brakes are where the numbers jump. Repasi lists front rotors at twelve to sixteen thousand dollars and rear rotors at ten to fourteen thousand. Add front pads at eighteen hundred to twenty-five hundred and rear pads at fifteen hundred to twenty-two hundred. By our arithmetic, a full set of rotors and pads comes to about twenty-five thousand to thirty-five thousand dollars on the shop's own list.""",
   "918 brakes, shop", "REPASI: ROTORS FRONT $12–16K + REAR $10–14K · PADS FRONT $1.8–2.5K + REAR $1.5–2.2K → ~$25,300–34,700 (OUR ARITHMETIC)")
sc("""Stuttcars gives a different set of numbers. Brake pads and rotors, if needed, fifteen to thirty thousand dollars in its costs section. In its FAQ, twenty-five to forty thousand for the carbon-ceramic rotors and pads. And in the brake section, over forty thousand for rotors alone, with pads and labour on top, for a total above fifty thousand. The guide gives three numbers for the same job.""",
   "918 brakes, guide", "STUTTCARS: $15–30K (COSTS) · $25–40K (FAQ, PCCB) · $50K+ (BRAKE SECTION) · THREE FIGURES FOR ONE JOB")
sc("""Whichever list you believe, a brake job on a nine eighteen is the price of a new family car or more. By our arithmetic, even the shop's lowest total is about half the average new vehicle price of fifty thousand, eighty-nine dollars, and the guide's highest figure is more than that average. Neither source says how often a brake job is needed, which depends on how the car is driven.""",
   "918 brakes vs average car", "$25,300 ≈ 0.5× · $50,000+ ≈ 1.0×+ THE $50,089 AVERAGE NEW VEHICLE (KBB; OUR ARITHMETIC) · FREQUENCY NOT GIVEN")

ch("The battery")
sc("""The battery is the number that frightens buyers. Wikipedia and Porsche describe a six point eight kilowatt-hour lithium-ion pack, about seven in Porsche's wording, with three hundred twelve cells, and a seven-year battery warranty. By our arithmetic, a car delivered in twenty fifteen would have been out of that warranty by twenty twenty-two. Whether it counts from delivery or registration, our sources do not say.""",
   "918 battery warranty", "6.8 kWh · 312 CELLS · 7-YEAR BATTERY WARRANTY (WIKIPEDIA; PORSCHE) · 2015 + 7 = 2022 (OUR ARITHMETIC) · START DATE OF WARRANTY NOT STATED")
sc("""What does a replacement cost? Stuttcars says fifty to eighty thousand dollars, attributing the top figure to unnamed experts. Repasi says complete replacement is eighty to one hundred fifty thousand. Only the ends touch. The shop adds module replacement at fifteen to thirty thousand, and battery conditioning, which it recommends every six to eight years, at twenty-five hundred to five thousand.""",
   "918 battery cost", "GUIDE: REPLACEMENT $50–80K · SHOP: COMPLETE $80–150K · MODULES $15–30K · CONDITIONING $2.5–5K (ESTIMATES; ONLY ENDPOINTS OVERLAP)")
sc("""Porsche has not published a price for the pack in anything we found. The only invoice we have seen is for a different car: a Motorious article on a LaFerrari says it had a new high-voltage battery and a service invoice of more than two hundred thousand euros. So the nine eighteen figures stay as estimates. By our arithmetic, the shop's top figure of one hundred fifty thousand dollars is about eighteen percent of the car's original base price.""",
   "No published battery price", "NO PORSCHE PRICE FOUND · LAFERRARI: NEW HV BATTERY + INVOICE >€200,000 (MOTORIOUS) · $150,000 ÷ $845,000 = 17.8% (OUR ARITHMETIC)")
sc("""There is also the electric range. The EPA rating for the nine eighteen is twelve miles on electricity alone, while Porsche's own claim was over thirty kilometres. By our arithmetic, twelve miles is about nineteen kilometres. The difference between claim and rating is a reminder that the hybrid system's real-world performance is not exactly what the brochure says.""",
   "918 electric range", "EPA EV RANGE 12 MI (~19 KM) vs PORSCHE CLAIM >30 KM (WIKIPEDIA; PORSCHE) · 12 MI × 1.609 = 19.3 KM (OUR ARITHMETIC)")

ch("Insurance and storage")
sc("""Insurance. Stuttcars quotes fifteen to thirty thousand dollars or more, and says it asked brokers on Long Island. It does not say whether that is per year, though the context suggests so. Repasi says eight to twenty-five thousand dollars annually. Neither is an insurer's quote, and both depend on the owner, the state, and the agreed value of the car.""",
   "918 insurance", "GUIDE: $15,000–30,000+ (LONG ISLAND BROKERS; PERIOD NOT STATED) · SHOP: $8,000–25,000 A YEAR · NEITHER IS AN INSURER'S QUOTE")
sc("""Storage. Repasi says climate-controlled storage costs four hundred to two thousand dollars a month. By our arithmetic, that is four thousand, eight hundred to twenty-four thousand dollars a year. For a car that is driven thirty-eight miles a year, storage may be a large part of the bill, but only for owners who pay for it rather than keep the car at home.""",
   "918 storage", "REPASI: $400–2,000/MONTH → $4,800–24,000/YEAR (OUR ARITHMETIC) · ONLY FOR OWNERS WHO PAY FOR STORAGE")

ch("Recalls")
sc("""The recalls are a different kind of cost, because the manufacturer pays. In May twenty fifteen, Autoblog reported a global precautionary recall: a carbon-fibre component could damage the radiator fan's wiring harness. It covered two hundred twenty-three cars in the United States, those built through the end of April twenty fifteen. The fix was free and took about half a day.""",
   "918 recall 2015", "MAY 2015 RECALL: CARBON PART CAN DAMAGE FAN WIRING HARNESS · 223 US CARS BUILT THROUGH APRIL 2015 · FREE, ~HALF A DAY (AUTOBLOG)")
sc("""By our arithmetic, two hundred twenty-three of the two hundred ninety-four United States cars is seventy-six percent. So three out of four cars on American roads needed that visit. The article does not give a global figure, and it does not say how many of the cars were found to have damaged harnesses.""",
   "918 recall share", "223 ÷ 294 = 75.9% OF US CARS (OUR ARITHMETIC) · GLOBAL FIGURE AND NUMBER ACTUALLY DAMAGED: NOT GIVEN")
sc("""A later recall, NHTSA campaign sixteen V eight eight five, covered three hundred six vehicles, built between the sixth of November twenty thirteen and the twenty-seventh of July twenty fifteen. The front lower control arms may crack at the ball joint. Dealers replaced them free of charge. Motor1, which reported it, does not give a repair cost.""",
   "918 recall control arms", "NHTSA 16V885: 306 VEHICLES, BUILT 6 NOV 2013 – 27 JUL 2015 · FRONT LOWER CONTROL ARMS MAY CRACK AT BALL JOINT · FREE (MOTOR1) · NO REPAIR COST GIVEN")
sc("""Stuttcars also mentions a twenty-sixteen recall for coolant pipe bonding, repaired under warranty, with no dollar figure. We keep it separate, because we could not verify it in a primary source. The point is the same in every case: recalls cost the owner nothing, but they show that the car needed attention in the first years.""",
   "918 other recalls", "STUTTCARS: 2016 COOLANT PIPE BONDING, REPAIRED UNDER WARRANTY (NO PRIMARY SOURCE FOUND; NO COST GIVEN) · ABOUT 6 RECALLS IN ALL (WIKIPEDIA)")

ch("Parts and body")
sc("""Parts. Stuttcars gives a list of estimates, and again they are the guide's own. Carbon body panels, ten to twenty thousand dollars each. A rear carbon bumper, over fifteen thousand. A headlight assembly, eight to twelve thousand per unit. The Weissach exhaust system, fifteen to twenty-five thousand. Nothing here comes from Porsche, and the guide does not cite a source.""",
   "918 parts", "STUTTCARS ESTIMATES: CARBON PANEL $10–20K · REAR BUMPER $15K+ · HEADLIGHT $8–12K EACH · WEISSACH EXHAUST $15–25K (NO SOURCE CITED)")
sc("""Even so, the headlight number is worth a moment. By our arithmetic, a pair at eight to twelve thousand each is sixteen to twenty-four thousand dollars, which is a third to a half of the average new vehicle price. Whether a collision repair actually costs that much depends on the insurer, the shop, and parts supply, none of which our sources describe.""",
   "918 headlights", "2 × $8–12K = $16–24K ≈ 0.32–0.48× $50,089 AVERAGE NEW VEHICLE (OUR ARITHMETIC) · REAL REPAIR COST DEPENDS ON INSURER/SHOP/PARTS (NOT IN SOURCES)")

ch("Fuel and energy")
sc("""Fuel. The EPA rated the nine eighteen at twenty-two miles per gallon on petrol alone, and fifty kilowatt-hours per one hundred miles on electricity. Porsche's European figure was three litres per one hundred kilometres, with seventy-nine grams of CO two per kilometre. We did not find a published real-world fuel bill, and we will not guess one.""",
   "918 fuel", "EPA 22 MPG (GAS ONLY) · 50 kWh/100 MI (ELECTRIC) · NEDC 3 L/100 KM, 79 g/KM CO₂ (WIKIPEDIA) · NO REAL-WORLD FUEL BILL FOUND")
sc("""By our arithmetic, at two thousand to three thousand miles a year and twenty-two miles per gallon on petrol, the car would burn about ninety-one to one hundred thirty-six gallons a year. We do not attach a price, because our sources do not give a fuel price for the period. The point is that fuel is small compared to everything else on this list.""",
   "918 annual fuel volume", "2,000–3,000 MI ÷ 22 MPG ≈ 91–136 GALLONS/YEAR, GAS ONLY (OUR ARITHMETIC) · NO FUEL PRICE USED")

ch("Putting it together")
sc("""Time to add it up, with every assumption stated. The guide's version: annual service of five to ten thousand dollars plus insurance of fifteen to thirty thousand. By our arithmetic, that is twenty to forty thousand dollars a year, before tyres, brakes, storage and the battery.""",
   "918 yearly total, guide", "STUTTCARS: SERVICE $5–10K + INSURANCE $15–30K = $20,000–40,000/YEAR (OUR ARITHMETIC) · EXCLUDES TYRES, BRAKES, STORAGE, BATTERY")
sc("""The shop's version for a low-mileage owner: its own budget of seventy-two hundred to ten thousand, eight hundred, plus insurance at eight to twenty-five thousand, plus storage at four thousand, eight hundred to twenty-four thousand. By our arithmetic, twenty thousand to fifty-nine thousand, eight hundred dollars a year. An active owner, at thirteen to twenty-two thousand, comes to about twenty-five thousand, eight hundred to seventy-one thousand.""",
   "918 yearly total, shop", "SHOP BUDGET $7.2–10.8K + INSURANCE $8–25K + STORAGE $4.8–24K = $20,000–59,800/YEAR · ACTIVE OWNER $13–22K → $25,800–71,000 (OUR ARITHMETIC)")
sc("""Notice that both sets of sources, built independently, give a low end of about twenty thousand dollars a year. That is our arithmetic and a coincidence of two estimates, not a confirmed figure. The high end is far less certain, and depends on whether the owner pays for storage and how much the car is driven.""",
   "918 yearly total comparison", "BOTH LOW ENDS ≈ $20,000/YEAR (OUR ARITHMETIC; ESTIMATES, NOT CONFIRMED) · HIGH END: $40,000 (GUIDE) TO $71,000 (SHOP, ACTIVE OWNER)")
sc("""Now compare that to what the car did. The standard car sold for two million, nine hundred sixty thousand, against a base price of eight hundred forty-five thousand. By our arithmetic, that is a gain of two million, one hundred fifteen thousand dollars. Spread over eleven years, about one hundred ninety-two thousand a year, which is several times the twenty to sixty thousand running cost.""",
   "918 gain vs running cost", "$2,960,000 − $845,000 = $2,115,000 · ÷ 11 YEARS ≈ $192,000/YEAR vs $20–60K RUNNING COST (OUR ARITHMETIC) · GAINS ARE UNREALISED UNTIL SOLD")
sc("""That comparison needs three warnings. The gain is on paper until the car is sold. It ignores the cost of money tied up in the purchase, which our sources do not discuss. And the original buyers got their cars only if Porsche chose them, so most people could never have paid the list price at all. We are describing what the numbers say, not advising anyone to buy.""",
   "Warnings on the gain", "PAPER GAIN ONLY · IGNORES COST OF CAPITAL (NOT IN SOURCES) · LIST-PRICE ACCESS WAS NOT OPEN TO ALL (WIKIPEDIA: SOLD OUT BEFORE END OF PRODUCTION) · NOT FINANCIAL ADVICE")
sc("""The duPont Registry's index adds a growth rate: about ten percent a year for standard cars and about six percent for Weissach cars. By our arithmetic, ten percent of the two million, one hundred sixty-eight thousand median is about two hundred seventeen thousand a year. That is a statistic about the index, not a forecast of what any car will do.""",
   "918 index growth", "DUPONT INDEX: ~10%/YEAR STANDARD · ~6%/YEAR WEISSACH · 10% × $2,168,836 ≈ $216,900 (OUR ARITHMETIC) · INDEX STATISTIC, NOT A FORECAST")


sc("""Per day, then. By our arithmetic, twenty thousand dollars a year is fifty-four dollars eighty a day, and fifty-nine thousand, eight hundred is one hundred sixty-four dollars a day. That is every day, including the days when the car does not move. It is the same arithmetic as before, applied to the shop and guide estimates, and it is not a measured cost.""",
   "918 cost per day", "$20,000 ÷ 365 ≈ $54.80/DAY · $59,800 ÷ 365 ≈ $163.84/DAY (OUR ARITHMETIC FROM THIRD-PARTY ESTIMATES)")
sc("""Now the worst case on the shop's own list: a complete battery at one hundred fifty thousand dollars, plus a full set of brake rotors and pads at about thirty-four thousand, seven hundred. By our arithmetic, that is one hundred eighty-four thousand, seven hundred dollars, or six point two percent of the two point nine six million dollar auction price. Two jobs, both at the top of the shop's range.""",
   "918 worst-case repairs", "$150,000 + ~$34,700 = ~$184,700 = 6.2% OF $2,960,000 (REPASI TOP FIGURES; OUR ARITHMETIC) · BOTH AT TOP OF RANGE")
sc("""How does the battery compare with routine service? Using the shop's own numbers, a complete battery at eighty thousand dollars equals eighteen years of its baseline annual service at four thousand, four hundred dollars. At one hundred fifty thousand and the lowest baseline of two thousand, eight hundred fifty, it is fifty-three years. Those are our ratios, not Repasi's.""",
   "Battery vs routine service", "$80,000 ÷ $4,400 ≈ 18.2 YEARS · $150,000 ÷ $2,850 ≈ 52.6 YEARS OF BASELINE ANNUAL SERVICE (REPASI FIGURES; OUR ARITHMETIC)")
sc("""And the Weissach premium, which Stuttcars puts at two hundred fifty thousand dollars or more. The duPont medians give a way to check it. By our arithmetic, three million, thirty-two thousand, five hundred minus two million, one hundred sixty-eight thousand, eight hundred thirty-six is eight hundred sixty-three thousand, six hundred sixty-four dollars. So on the medians, the premium is more than three times the guide's figure.""",
   "Weissach premium check", "$3,032,500 − $2,168,836 = $863,664 vs GUIDE '$250K+' → ~3.5× (DUPONT; STUTTCARS; OUR ARITHMETIC)")

ch("What our sources do not say")
sc("""What is missing. Porsche publishes no service price list for the nine eighteen. No insurer's quote. No owner's actual annual bill. No price for the battery pack from Porsche. The two cost sources contradict each other and, in the guide's case, itself. No figure for how often the brakes need replacing, or whether the pack really ages out at a given mileage.""",
   "Porsche 918 Spyder", "NOT PUBLISHED: PORSCHE SERVICE PRICES · INSURER QUOTES · OWNER BILLS · OFFICIAL BATTERY PRICE · BRAKE REPLACEMENT INTERVALS · BATTERY AGEING DATA")
sc("""So the honest answer to what it really costs to own a Porsche nine eighteen is a range. Our arithmetic from the two outside sources says about twenty thousand dollars a year at the low end, and up to roughly seventy thousand for an active owner who pays for storage, before a battery or brake job. The car's value, meanwhile, has risen far more than that.""",
   "Porsche 918 Spyder", "ESTIMATE: ~$20,000/YEAR LOW END · UP TO ~$71,000 ACTIVE OWNER + STORAGE · BATTERY/BRAKES EXTRA (OUR ARITHMETIC FROM THIRD-PARTY ESTIMATES)")
sc("""If you own a nine eighteen, or know someone who does, and can share a real invoice or a published source, tell us in the comments, and we will update the description. What is the highest bill you have heard of for a hypercar? In the other videos of this series, we reveal two things you did not know about the nine eighteen, compare it with the LaFerrari, and tell the story of the Holy Trinity. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Porsche 918 Spyder", "SUBSCRIBE: PICKUP REALITY")

save("video139", "The Real Cost of Owning a Porsche 918", [
    "Wikipedia, Porsche 918 Spyder: https://en.wikipedia.org/wiki/Porsche_918_Spyder",
    "Porsche press release (company source), Porsche 918 Spyder: the technology, via 911uk: https://911uk.com/porsche/official-press-release-porsche-918-spyder-the-technology.58965/latest",
    "Stuttcars, Porsche 918 Buyer's Guide: https://www.stuttcars.com/porsche-buyers-guides/porsche-918-buyers-guide/",
    "Repasi Motorwerks, 918 Spyder Annual Maintenance Cost (a repair shop's own page): https://repasimotorwerks.com/blog/918-spyder-annual-maintenance-cost",
    "Autoblog, Porsche 918 Spyder recalled over bad wiring harness: https://www.autoblog.com/2015/05/22/porsche-918-spyder-recall/",
    "Motor1, Porsche 918 recalled for cracked suspension: https://www.motor1.com/news/132292/porsche-918-recalled-again/",
    "duPont REGISTRY, Market spotlight: Porsche 918 Spyder: https://news.dupontregistry.com/blogs/features/market-spotlight-porsche-918-spyder",
    "Broad Arrow Auctions, Porsche 918 Spyder Weissach tops Broad Arrow's $20 million Air|Water auction: https://www.broadarrowauctions.com/news/Porsche-918-Spyder-Weissach-Tops-Broad-Arrows-20-Million-AirWater-Auction",
    "Motorious, Delivery-mileage 2015 Ferrari LaFerrari heads to Broad Arrow's Zürich auction: https://www.motorious.com/articles/all/delivery-mileage-2015-ferrari-laferrari-heads-to-broad-arrows-zurich-auction/",
    "Kelley Blue Book, average new vehicle price: https://www.kbb.com/",
    "U.S. Census Bureau, Income in the United States: 2024: https://www.census.gov/library/publications/2025/demo/p60-286.html",
], "C")
