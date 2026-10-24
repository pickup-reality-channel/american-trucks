import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""Two Italian SUVs, two completely different engines. The Lamborghini Urus has a four litre twin-turbo V eight. The Ferrari Purosangue has a six point five litre V twelve with no turbochargers, that revs to eight thousand two hundred fifty. One has more torque, and the other has more power. One costs, by our own arithmetic, about one hundred seventy thousand dollars less. And Ferrari insists that its car is not an SUV at all. This is the real difference between them.""",
   "Lamborghini Urus and Ferrari Purosangue", "LAMBORGHINI URUS VS FERRARI PUROSANGUE")
sc("""Here is the twist. The cheaper car has more torque, and gets it four thousand r p m earlier. The more expensive car is quicker to two hundred kilometres per hour, by more than two seconds. And Ferrari will build fewer Purosangue each year than Lamborghini builds Urus, by design. Let us go through the numbers, and the places where the sources disagree.""",
   "Ferrari Purosangue", "THE CHEAPER CAR HAS MORE TORQUE")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Lamborghini Urus", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE CARS ----------
ch("Two answers to the same question")
sc("""Wikipedia says the Lamborghini Urus was unveiled on the fourth of December, twenty seventeen, with deliveries beginning in early twenty eighteen. The Ferrari Purosangue was unveiled on the thirteenth of September, twenty twenty-two, for the twenty twenty-three model year. By our arithmetic, Ferrari arrived four years and nine months after Lamborghini.""",
   "Lamborghini Urus and Ferrari Purosangue", "URUS: DEC 2017 · PUROSANGUE: SEPT 2022")
sc("""The Purosangue's development was long. Wikipedia says it began in twenty seventeen, codenamed F one seventy-five. Then-CEO Sergio Marchionne had hinted at it, and Ferrari confirmed it in September twenty eighteen. The first test-mule pictures appeared on the twenty-second of October twenty eighteen, with a prototype based on the GTC4Lusso.""",
   "Ferrari Purosangue prototype", "CODENAME F175 · CONFIRMED SEPTEMBER 2018")
sc("""The name comes from the horse breed, Wikipedia says. And there is a legal story. Ferrari tried to trademark Purosangue in twenty twenty, but a group called the Purosangue Foundation blocked it, and Ferrari sued over the naming rights. The case went to court on the fifth of March, twenty twenty-one.""",
   "Purosangue horse", "THE NAME CAUSED A LAWSUIT")
sc("""Ferrari has denied building an SUV, the page says, and calls the car an F U V, a Ferrari Utility Vehicle. Wikipedia describes it as a mid-size luxury crossover SUV with five doors, a fastback shape, and rear coach doors that open forward from a fixed B-pillar. Lamborghini, by contrast, has called the Urus an SUV from the start.""",
   "Ferrari Purosangue rear doors", "FERRARI CALLS IT AN \"FUV\"")
sc("""The Urus's name comes from the urus, the ancestor of modern cattle, the wild ox, according to Wikipedia. So one car is named after a thoroughbred horse, and the other after a wild bull. That fits the two companies' symbols, a prancing horse and a charging bull, even if the names were not chosen as a matched pair.""",
   "Ferrari and Lamborghini badges", "HORSE VS BULL")

# ---------- 2. ENGINES ----------
ch("Round one: the engines")
sc("""Start with the Purosangue. Wikipedia lists a six point five litre F one forty V twelve, six thousand four hundred ninety-six cubic centimetres, with seven hundred twenty-five metric horsepower at seven thousand seven hundred fifty r p m, and seven hundred sixteen newton-metres at six thousand two hundred fifty. The redline is eight thousand two hundred fifty. Motor1 describes it as naturally aspirated.""",
   "Ferrari V12 engine", "6.5 L V12 · 725 PS @ 7,750 RPM")
sc("""Now the Urus. Wikipedia lists a four litre twin-turbo V eight with six hundred fifty metric horsepower at six thousand r p m, and eight hundred fifty newton-metres from two thousand two hundred fifty to four thousand five hundred r p m. It is a reworked version of an Audi engine, assembled at a Volkswagen plant in Hungary.""",
   "Lamborghini Urus engine", "4.0 L TWIN-TURBO V8 · 650 PS")
sc("""Do the arithmetic. The Purosangue has about eleven and a half percent more power, seven hundred twenty-five against six hundred fifty. But the Urus has about nineteen percent more torque, eight hundred fifty against seven hundred sixteen. The V twelve is stronger at the top, and the V eight is stronger in the middle.""",
   "Engine comparison", "POWER: +11.5% FERRARI · TORQUE: +19% LAMBORGHINI")
sc("""And where the torque arrives matters. The Urus has its peak torque from two thousand two hundred fifty r p m. The Purosangue peaks at six thousand two hundred fifty. By our arithmetic, the Ferrari needs four thousand more r p m to reach its torque peak. That is why the two cars feel so different, according to the logic of the numbers.""",
   "Engine rpm", "TORQUE PEAK: 2,250 RPM VS 6,250 RPM")
sc("""Per litre, the numbers flip. The Purosangue makes about one hundred twelve metric horsepower per litre, by our arithmetic. The Urus makes about one hundred sixty-three, since it has turbochargers. Turbocharging lets a smaller engine produce more. Ferrari chose size and revs. Lamborghini chose boost.""",
   "Turbocharger", "112 PS/L VS 163 PS/L")
sc("""The Purosangue's gearbox is an eight-speed dual-clutch from Magna, Wikipedia says. The Urus has an eight-speed automatic, according to CARFAX's listing of the hybrid. Both use all-wheel drive. The Purosangue is a front mid-engine car, built on a platform shared with the Ferrari Roma coupé. The Urus uses the Volkswagen Group's M L B Evo platform.""",
   "Ferrari Roma platform", "FERRARI: ROMA PLATFORM · LAMBORGHINI: VW GROUP PLATFORM")
sc("""That platform difference is interesting. Ferrari built its first four-door model on a platform from its own sports car. Lamborghini built its SUV on a platform shared with a Porsche, a Bentley, an Audi and a Volkswagen. Winkelmann has said it has a common platform, but our engineers did a fantastic job creating a car which is a real Lamborghini.""",
   "Stephan Winkelmann", "\"A REAL LAMBORGHINI\"")

# ---------- 3. PERFORMANCE ----------
ch("Round two: speed and weight")
sc("""Wikipedia lists Ferrari's claims for the Purosangue: zero to a hundred in three point three seconds, zero to two hundred in ten point six, and a top speed of over three hundred ten kilometres per hour. For the Urus, it lists three point six, twelve point eight, and about three hundred five or three hundred six.""",
   "Ferrari Purosangue acceleration", "0–100: 3.3 VS 3.6 S · 0–200: 10.6 VS 12.8 S")
sc("""By our own arithmetic, the Purosangue is about eight percent quicker to a hundred, and about seventeen percent quicker to two hundred. The top speed gap is small, about one point three percent. So Ferrari's advantage grows with speed. At lower speeds the two cars are close, and the V twelve pulls away as the r p m climb.""",
   "Ferrari Purosangue", "FERRARI'S EDGE GROWS WITH SPEED")
sc("""The Urus Performante narrows the gap. Wikipedia claims three point three to a hundred, the same as the Purosangue, with six hundred sixty-six metric horsepower, and a weight forty-seven kilograms lower than other versions. And the Urus S E, the plug-in, reaches a hundred in three point four with seven hundred ninety-nine horsepower, and a top speed of three hundred twelve.""",
   "Lamborghini Urus Performante", "PERFORMANTE: 3.3 S · SE: 799 HP, 312 KM/H")
sc("""So the newest Urus beats the Purosangue on power by more than eleven percent, by our arithmetic, and on top speed by two kilometres per hour. The Ferrari's advantage over the base Urus does not hold up against the hybrid. But the S E also weighs about three hundred kilograms more than the Urus S, because of its twenty-five point nine kilowatt-hour battery.""",
   "Lamborghini Urus SE", "URUS SE: +11.7% POWER OVER THE PUROSANGUE")
sc("""Weight next. Wikipedia lists the Purosangue's kerb weight at two thousand, one hundred seventy kilograms. Motor1 gives two thousand and thirty-three kilograms, but that is a dry figure. The Urus is listed at under two thousand, two hundred kilograms by the manufacturer, according to Wikipedia. The two are essentially the same weight.""",
   "Ferrari Purosangue weight", "2,170 KG KERB · 2,033 KG DRY · URUS <2,200 KG")
sc("""Power-to-weight, by our own arithmetic, is about point three three metric horsepower per kilogram for the Purosangue, and at least point three for the Urus, since its weight is an upper limit. That puts the Ferrari at least ten percent ahead. The difference comes from its extra horsepower, since weight is nearly equal.""",
   "Power to weight", "FERRARI ≥10% BETTER POWER-TO-WEIGHT")
sc("""Dimensions are less discussed. Wikipedia lists the Purosangue at four thousand, nine hundred seventy-three millimetres long, two thousand, twenty-eight wide, and one thousand, five hundred eighty-nine tall, with a wheelbase of three thousand and eighteen. These are big numbers for a car with a V twelve. The sources we read do not give the same measurements for the Urus.""",
   "Ferrari Purosangue dimensions", "4,973 MM LONG · 3,018 MM WHEELBASE")

# ---------- 4. FUEL ----------
ch("Round three: fuel and tax")
sc("""Fuel is not a strength. Wikipedia lists the Purosangue's E P A fuel economy at eleven miles per gallon in the city, fifteen on the highway, and twelve combined. Motor1 notes the price excludes the gas-guzzler tax, which could be four thousand, five hundred to seven thousand, seven hundred dollars, depending on the rating, unless the car is classified as an SUV.""",
   "Fuel pump", "FERRARI: 11/15 MPG · GAS-GUZZLER TAX ESTIMATE")
sc("""For the Urus, CARFAX gives numbers for the plug-in only: forty-eight miles per gallon equivalent combined with a thirty-five mile electric range, and twenty miles per gallon combined with the engine alone. We found no E P A figure for the non-hybrid Urus in our sources, so we make no comparison. The comparison that matters is the S E, which can run on electricity.""",
   "Lamborghini Urus SE charging", "URUS SE: 20 MPG ON PETROL · 35-MILE EV RANGE")
sc("""So the Purosangue's twelve miles per gallon compares with the Urus S E's twenty miles per gallon on petrol alone, by our arithmetic, about two-thirds more distance for each gallon. But a non-hybrid Urus would be different. This is why we do not draw a conclusion. We only note that one of the two cars is available as a plug-in, and the other is not.""",
   "Lamborghini Urus plug-in", "ONLY THE LAMBORGHINI HAS A PLUG-IN")

# ---------- 5. PRICE ----------
ch("Round four: price")
sc("""Now money. Motor1 reported that the two thousand twenty-four Ferrari Purosangue costs three hundred ninety-three thousand, three hundred fifty dollars, plus a five thousand dollar destination charge, about three hundred ninety-eight thousand, three hundred fifty. It said that was roughly one hundred seventy thousand dollars more than a standard Urus.""",
   "Ferrari Purosangue price", "$393,350 + $5,000 DESTINATION")
sc("""By our own arithmetic, one hundred seventy thousand below three hundred ninety-three thousand puts the Urus near two hundred twenty-three thousand. That would make the Purosangue about seventy-six percent more expensive. The Premier Auto Miami page, a rental company's marketing, estimates the twenty twenty-five Urus at around two hundred forty-one thousand, eight hundred dollars.""",
   "Lamborghini Urus price", "URUS: ~$223K–$242K · PUROSANGUE: $393K")
sc("""Using that higher estimate, the gap is about one hundred fifty-one thousand dollars, or sixty-three percent. Either way, the Purosangue costs between sixty and seventy-five percent more, by our arithmetic. Motor1 also says the Ferrari costs over forty thousand dollars more than a base Rolls-Royce Cullinan, and much more than an Aston Martin D B X or a Bentley Bentayga Speed.""",
   "Rolls-Royce Cullinan", "FERRARI: +60% TO +75% OVER THE URUS")
sc("""Options are extra on both. Motor1 says there are plenty of options for the Ferrari. Marque Cars says optioned Purosangues often exceed four hundred fifty thousand dollars. For the Urus, Premier Auto Miami says a fully optioned S E can reach well over three hundred thousand to three hundred forty thousand. Both estimates are from non-manufacturer pages.""",
   "Ferrari Purosangue options", "OPTIONED: FERRARI $450K+ · URUS SE $300–340K")

# ---------- 6. PRODUCTION ----------
ch("Round five: how many get built")
sc("""This is where the philosophies differ most. Motor1 says Ferrari caps Purosangue production at twenty percent of the company's annual capacity, to keep it exclusive. Marque Cars estimates that means about two thousand, seven hundred to two thousand, eight hundred cars per year. It is an estimate, and Ferrari has not said so.""",
   "Ferrari factory Maranello", "CAPPED AT 20% OF OUTPUT (~2,700–2,800 A YEAR)")
sc("""The Urus has no such cap. Wikipedia lists seven thousand, two hundred sixty-five built in twenty twenty-five, six thousand, six hundred eighty-one in twenty twenty-four, and a total of forty-three thousand, two hundred fifty-four by our arithmetic since twenty seventeen. By our arithmetic, the Urus is built in about two and a half times the quantity of the Purosangue's estimated cap.""",
   "Lamborghini Urus production", "URUS 7,265 IN 2025 VS PUROSANGUE CAP ~2,750")
sc("""And the Urus is the core of its company. Carscoops reported that it was sixty-one percent of Lamborghini's sales in twenty nineteen. Ferrari, by contrast, has set a cap so that its SUV does not take over. That is the real strategic difference: Lamborghini built an SUV to grow, and Ferrari built one to complement.""",
   "Lamborghini and Ferrari strategy", "URUS = 61% OF LAMBORGHINI · PUROSANGUE ≤ 20% OF FERRARI")
sc("""Demand was huge on the Ferrari side too. InsideHook reported in May twenty twenty-three that CEO Benedetto Vigna said the order book already extended into twenty twenty-five, and that Ferrari decided to reopen orders for the Purosangue, which had been suspended due to an initial unprecedented demand. New orders then had an earliest delivery of twenty twenty-six.""",
   "Benedetto Vigna", "ORDER BOOK INTO 2025 · NEW ORDERS: 2026")
sc("""Motor1 adds that Vigna said order books filled four times quicker than originally estimated. In the first quarter of twenty twenty-three, InsideHook reports, Ferrari shipments rose nine point seven percent and profits twenty-seven percent. The article credits the outlook for the SUV for the bigger takeaway. A cap does not stop a car from changing a company.""",
   "Ferrari earnings", "Q1 2023: SHIPMENTS +9.7% · PROFITS +27%")

# ---------- 7. RESALE ----------
ch("Round six: what they are worth used")
sc("""Marque Cars wrote in September twenty twenty-six that optioned Purosangues routinely clear four hundred fifty thousand dollars used, and well-specified ones land above five hundred thousand. It says early delivery-mile cars sold above sticker while the order book was closed, but that premium compressed. The page marks its figures as directional.""",
   "Ferrari Purosangue used", "USED: $450K–$500K+ (DIRECTIONAL)")
sc("""For the Urus, VinAssessment lists median dealer asking prices by model year. Twenty twenty-three, two hundred fifty-three thousand, one hundred twelve dollars. Twenty twenty-four, two hundred seventy-nine thousand, five hundred sixty-seven. Twenty twenty-five, two hundred ninety-five thousand, three hundred sixty-six. These are asking prices, not sale prices, and they include the plug-in in later years.""",
   "Lamborghini Urus used", "URUS ASKING: $253K (2023) → $295K (2025)")
sc("""The Marque guide says one more important thing: the active suspension on the Purosangue is newer, more complex, and the component you most want documented. It recommends a franchised dealer inspection and complete documentation. That is the kind of detail that matters when you buy a used car at this price, and it applies to the Urus as well.""",
   "Ferrari Purosangue suspension", "ACTIVE SUSPENSION: GET IT DOCUMENTED")

# ---------- 8. DESIGN ----------
ch("Round seven: design and recognition")
sc("""Wikipedia says the Purosangue won the Compasso d'Oro industrial design award in twenty twenty-four. It was designed by the Ferrari Styling Centre under Flavio Manzoni. The Urus was designed by Mitja Borkert, and the concept by Filippo Perini. Both designs divide opinion, but only one has won a design prize, according to our sources.""",
   "Ferrari Purosangue design", "COMPASSO D'ORO 2024")
sc("""The two cars also differ in how they are seen. The Ferrari has a fastback shape and rear coach doors, which make it look unlike any other SUV. The Lamborghini looks like an SUV with a Lamborghini face. Winkelmann says nobody who drives an Urus ever doubts that it is a real Lamborghini. Ferrari says its car is not an SUV at all.""",
   "Ferrari Purosangue and Lamborghini Urus", "TWO WAYS TO LOOK DIFFERENT")

# ---------- 8b. EXTRA ----------
ch("Round eight: reliability and recalls")
sc("""Reliability is harder to compare, because we found no recall list for the Purosangue in our sources. For the Urus, Wikipedia lists two recalls. In November twenty twenty, two thousand, eight hundred thirty-one cars were recalled over a fuel line problem. In May twenty twenty-four, two thousand, one hundred thirty-three cars were recalled over rivets in the hood latch.""",
   "Lamborghini Urus recall", "URUS RECALLS: 2,831 (2020) · 2,133 (2024)")
sc("""Those numbers need context. By our own arithmetic, two thousand, eight hundred thirty-one is a small fraction of the roughly twelve thousand, three hundred Urus built by the end of twenty nineteen and twenty twenty, using Wikipedia's production figures of one hundred twenty-one, two thousand five hundred sixty-five, five thousand, two hundred thirty-three and four thousand, three hundred sixty-four. A recall is not a verdict. It only tells you a problem was found and fixed.""",
   "Lamborghini factory", "A RECALL IS NOT A VERDICT")
sc("""The Purosangue is simply newer. It has been on sale only since twenty twenty-three, so there is far less history to read. Marque Cars says the active suspension is the part to document, and that no written rule about buying two cars exists. That last point is interesting, because Ferrari is known for steering its best allocations to loyal customers, but the guide says no formal rule was published.""",
   "Ferrari Purosangue", "NEWER CAR · LESS HISTORY")

ch("Round nine: how fast the Urus changed Lamborghini")
sc("""To see why the Urus matters, look at Lamborghini's deliveries. Wikipedia and company figures list three thousand, eight hundred fifteen cars in twenty seventeen, the year before the Urus. Then five thousand, seven hundred fifty in twenty eighteen, and eight thousand, two hundred five in twenty nineteen. Ten thousand, seven hundred forty-seven in twenty twenty-five.""",
   "Lamborghini deliveries", "DELIVERIES: 3,815 (2017) → 10,747 (2025)")
sc("""By our arithmetic, that is a rise of about one hundred eighty-two percent in eight years. And in twenty twenty-four, the company reported revenue of three point one zero billion euros and operating income of eight hundred thirty-five million. Winkelmann has said the company sold only sixteen hundred cars in two thousand five. The Urus did not do that alone, but it is the biggest change.""",
   "Stephan Winkelmann", "2024: €3.10B REVENUE · €835M OPERATING INCOME")
sc("""The Urus reached ten thousand units in July twenty twenty, according to Wikipedia, and twenty thousand by twenty twenty-two, the fastest any Lamborghini has reached that mark. Remember the original target of about three thousand, five hundred a year. By our arithmetic, in twenty twenty-five Lamborghini built more than double that target. The SUV beat its plan comfortably.""",
   "Lamborghini Urus production", "10,000TH UNIT: JULY 2020 · 20,000 BY 2022")
sc("""Ferrari's case is different, and we should be fair to it. The Purosangue is not the foundation of the company, it is an addition, and the cap keeps it that way. Whether the cap is exactly twenty percent is the company's own statement as reported by Motor1. The yearly number is an outside estimate. What is clear is the intent.""",
   "Ferrari Purosangue", "FERRARI'S INTENT: AN ADDITION, NOT THE FOUNDATION")

ch("Round ten: the cost of ownership")
sc("""Ownership cost is hard to compare, because neither company publishes it. The one source we found for the Urus is Premier Auto Miami, a rental firm, which estimates insurance at five thousand to ten thousand dollars or more a year, and notes the car needs high-octane fuel. These are estimates from a commercial page. We found no comparable source for the Purosangue, so we will not guess.""",
   "Insurance and fuel costs", "URUS INSURANCE EST.: $5,000–$10,000+ A YEAR")
sc("""What we can say is that the Purosangue's published fuel economy is eleven in the city and fifteen on the highway, and that Motor1 flags a possible gas-guzzler tax of four thousand, five hundred to seven thousand, seven hundred dollars. For a car that costs close to four hundred thousand, those are small numbers. They are the kind of extras that matter less to the buyer than the purchase price.""",
   "Gas pump", "GAS-GUZZLER TAX EST.: $4,500–$7,700")

# ---------- 9. VERDICT ----------
ch("The verdict")
sc("""So who wins? On power, the Purosangue, by eleven and a half percent, until you compare it with the Urus S E. On torque, the Urus, by nineteen percent. On acceleration to two hundred, the Purosangue. On weight, a tie. On price, the Urus, by sixty to seventy-five percent. On rarity, the Purosangue. On fuel use, the plug-in Urus.""",
   "Lamborghini Urus vs Ferrari Purosangue", "SCORECARD")
sc("""The real difference is philosophy. Ferrari used a big, high-revving V twelve and a cap on numbers, and called the car something else. Lamborghini used a turbo V eight, a group platform, and sold as many as it could. Both approaches have worked. Both companies are richer for them, according to the sources we read.""",
   "Lamborghini Urus and Ferrari Purosangue", "FERRARI CAPPED IT · LAMBORGHINI BET ON IT")
sc("""One final caution. We have not driven either car. Every figure here comes from manufacturers' claims or published guides, and some, like the Urus price, are our own calculation. We do not claim which is better to drive. We claim only what the numbers show, which is that each car is ahead of the other in some ways.""",
   "Italian SUVs", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you choose, the Urus or the Purosangue? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Urus, work out what it really costs to own one, and tell why Lamborghini bet everything on an SUV.""",
   "Lamborghini Urus and Ferrari Purosangue", "URUS OR PUROSANGUE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more comparisons between the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video98", "Lamborghini Urus vs Ferrari Purosangue: The Difference Nobody Explains", [
    "Wikipedia, Lamborghini Urus: https://en.wikipedia.org/wiki/Lamborghini_Urus",
    "Wikipedia, Ferrari Purosangue: https://en.wikipedia.org/wiki/Ferrari_Purosangue",
    "Motor1, 2024 Ferrari Purosangue is predictably expensive: https://www.motor1.com/news/652734/2024-ferrari-purosangue-suv-price/",
    "InsideHook, Ferrari Purosangue SUV bet has paid off: https://www.insidehook.com/autos/ferrari-purosangue-suv-bet-paid",
    "Marque Cars, Buying a Ferrari Purosangue: https://marquecars.com/journal/ferrari-purosangue-buying-guide",
    "CARFAX, 2026 Lamborghini Urus: https://www.carfax.com/Research-Lamborghini-Urus_w9540",
    "Premier Auto Miami, How much is a Lamborghini Urus: https://www.premierautomiami.com/how-much-is-a-lamborghini-urus/",
    "VinAssessment, Lamborghini Urus prices by year: https://vinassessment.com/prices/lamborghini/urus",
    "Carscoops, Lamborghini sold nearly 5,000 Urus SUVs last year (January 2020): https://www.carscoops.com/2020/01/lamborghini-sales-soar-43-percent-in-2019-thanks-to-urus-suv/",
    "Yahoo Autos, We're not selling mobility: how Stephan Winkelmann transformed Lamborghini: https://autos.yahoo.com/people-and-culture/articles/were-not-selling-mobility-stephan-083648052.html",
], "B")
