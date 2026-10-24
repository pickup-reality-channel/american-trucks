import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Most Lamborghinis are named after fighting bulls. The Miura, the Espada, the Diablo. The Countach is not. Its name is a word of astonishment, and the story of where it came from is only half documented. And the car that wears it was designed with a periscope, because the driver could not see out of the back. These are two things you may not know about the Lamborghini Countach.""",
   "Lamborghini Countach", "2 THINGS YOU DIDN'T KNOW ABOUT THE LAMBORGHINI COUNTACH")
sc("""We will take them one at a time: the name, and the periscope. Along the way we will also look at what the sources say about the prototype that was destroyed on purpose, the scissor doors, and the numbers. Every fact comes from a published source, listed in the description. Where sources disagree, we tell you. Where we do the maths, we say so.""",
   "Lamborghini Countach", "EVERY NUMBER IS SOURCED")

ch("Thing one: the name is not a bull")
sc("""Ferruccio Lamborghini named his cars after bulls. Wikipedia says the Miura was named after a family of Spanish fighting bulls, and that he visited their ranch near Seville in nineteen sixty-two. The list continues: Islero, Espada, Jarama, Urraco, Jalpa and Diablo. The page says the Countach broke that tradition completely.""",
   "Lamborghini Miura", "MIURA, ISLERO, ESPADA, JARAMA, URRACO, JALPA, DIABLO — BULL NAMES")
sc("""The name comes from a Piedmontese exclamation of astonishment, Wikipedia says. The page spells it contacc. The designer, Marcello Gandini, spells it countach, and says the word was first used as a joke by a worker, and then adopted. He calls it, in the page's quotation, the only true story behind the word. The name was coined in late nineteen seventy or nineteen seventy-one.""",
   "Marcello Gandini", "'CONTACC': A PIEDMONTESE EXCLAMATION OF ASTONISHMENT (WIKIPEDIA)")
sc("""Now the part that is not settled. Gandini says the word, as he spells it, literally means plague or contagion, but is used to express amazement. The Wikipedia article itself describes it only as an exclamation of astonishment. So two descriptions of the same word, in the same article, do not match exactly. We report both rather than choosing.""",
   "Lamborghini Countach", "GANDINI: 'LITERALLY' PLAGUE OR CONTAGION · ARTICLE: AN EXCLAMATION")
sc("""There is also the popular story that Nuccio Bertone saw the prototype and exclaimed the word. Wikipedia marks that story as needing a citation. In other words, the page does not support it. It is a good story and it may be true, but we have no source for it, so we do not tell it as fact. Gandini's version is the one the page quotes.""",
   "Nuccio Bertone", "THE BERTONE-EXCLAIMED STORY: 'CITATION NEEDED' (WIKIPEDIA)")
sc("""Why does this matter? Because retellings of the Countach story are full of confident claims. A name that sounds like a story attracts one. The honest version is short: the word is a Piedmontese expression of amazement, a worker's joke was adopted, it was coined around nineteen seventy or seventy-one, and that is what our sources can support.""",
   "Lamborghini Countach", "THE HONEST VERSION IS SHORT (OUR READING)")

ch("A car meant to replace the Miura")
sc("""Why was the car built at all? Wikipedia says Ferruccio Lamborghini wanted a successor to the Miura, which by nineteen seventy had lost ground to rivals such as the Ferrari Daytona. The chief engineer, Paolo Stanzani, started work in nineteen seventy under the project name L P one twelve. Test driver Bob Wallace, assistant engineer Massimo Parenti and Marcello Gandini of Bertone also worked on it.""",
   "Paolo Stanzani", "1970: PROJECT LP112 · STANZANI, WALLACE, PARENTI, GANDINI")
sc("""The first prototype, the L P five hundred, appeared at the Geneva Motor Show in nineteen seventy-one. The production L P four hundred followed in nineteen seventy-four. By our arithmetic, that is three years between the prototype and the car customers could buy. The prototype's bodywork came from Bertone, and its chassis from Marchesi, which also built the production chassis.""",
   "Geneva Motor Show", "LP500 PROTOTYPE: GENEVA 1971 · LP400 PRODUCTION: 1974 (3 YEARS LATER)")
sc("""The Miura, which the Countach was meant to replace, is a car with its own story. Wikipedia says the engineers Giampaolo Dallara, Paolo Stanzani and Bob Wallace built the Miura prototype in their spare time, largely at night, in nineteen sixty-five. Ferruccio Lamborghini approved it after seeing the development car, and gave the engineers a free hand.""",
   "Lamborghini Miura", "MIURA: BUILT IN SPARE TIME IN 1965 · FERRUCCIO GAVE A FREE HAND")
sc("""The Miura was the first high-performance production road car with a mid-engine, rear-wheel-drive layout, according to the page. Its three thousand, nine hundred twenty-nine cubic centimetre V twelve sat sideways behind the driver. The Countach kept the mid-engine idea, but turned the engine around. We will come back to that in the comparison video.""",
   "Lamborghini Miura", "MIURA: FIRST HIGH-PERFORMANCE MID-ENGINE RWD ROAD CAR (WIKIPEDIA)")

ch("Thing two: a periscope for the driver")
sc("""Now the second thing. The Countach prototype had a periscope. Wikipedia says that because rear visibility was poor, the prototype used a periscope supplied by Donnelly Mirrors. It had originally been developed for an E S V project, an experimental safety vehicle programme. The production L P four hundred kept it. Later models used conventional mirrors.""",
   "Lamborghini Countach LP400", "THE LP400 HAD A ROOF PERISCOPE FROM DONNELLY MIRRORS (WIKIPEDIA)")
sc("""That is where the name Periscopio comes from. The RM Sotheby's catalogue calls the first-series cars the L P four hundred Periscopio, and says about one hundred fifty were built, according to the Countach Register. By our arithmetic, that is about ninety-five percent of the one hundred fifty-seven L P four hundred cars Wikipedia lists. The two sources are close, not identical.""",
   "Countach LP400 Periscopio", "~150 PERISCOPIO (COUNTACH REGISTER) VS 157 LP400 (WIKIPEDIA) ≈ 95% (OUR ARITHMETIC)")
sc("""The page also describes another trick for reversing. Many drivers park by sitting on the wide sill with the door raised, and reversing while looking over the back of the car from outside. That is not a sales brochure. It is a practical workaround, and it appears in the encyclopaedia entry because owners actually do it.""",
   "Countach scissor doors", "REVERSING WHILE SITTING ON THE SILL (WIKIPEDIA)")
sc("""Rear visibility is the price of the shape. Wikipedia gives the dimensions of the production L P four hundred as four hundred fourteen centimetres long, one hundred eighty-nine wide and one hundred seven tall. By our arithmetic, it is eighty-two centimetres wider than it is tall. With the engine behind the driver, a low, wide car with a high rear deck is hard to see out of.""",
   "Lamborghini Countach", "LP400: 414 × 189 × 107 CM (WIKIPEDIA)")

ch("The doors that go up")
sc("""The scissor doors are the most famous feature of the Countach, yet they did not start here. Wikipedia says they first appeared on Marcello Gandini's nineteen sixty-eight Alfa Romeo Carabo concept. The doors hinge horizontally at the front, lift up and tilt forward, supported by gas struts. The Countach made the idea famous, but it was not the first car to show it.""",
   "Alfa Romeo Carabo", "SCISSOR DOORS FIRST SEEN ON GANDINI'S 1968 ALFA ROMEO CARABO")
sc("""There was a safety question. Wikipedia says engineers studied a removable kick-out windscreen and explosive bolts so that occupants could escape after a rollover. Neither idea was used on production cars. So the dramatic doors came without a documented emergency solution, a detail that is easy to forget when looking at a poster.""",
   "Lamborghini Countach", "KICK-OUT WINDSCREEN AND EXPLOSIVE BOLTS: STUDIED, NOT USED")
sc("""Wikipedia also says the Countach prototype was destroyed on purpose. The L P five hundred was crash-tested at MIRA in England on the twenty-first of March, nineteen seventy-four, to obtain European type approval. The show car that introduced the world to the Countach, in other words, was not preserved. It was used up so that the production car could be sold.""",
   "MIRA test facility", "THE LP500 PROTOTYPE WAS CRASH-TESTED AT MIRA ON MARCH 21, 1974 (WIKIPEDIA)")
sc("""The prototype was shown in nineteen seventy-one and crashed on the twenty-first of March, nineteen seventy-four, so by our arithmetic about three years passed between the two. The page does not give the exact date of the show, so this is approximate. The point stands: the car that made the name famous was destroyed in the process of making production possible.""",
   "Lamborghini Countach prototype", "ABOUT THREE YEARS FROM DEBUT TO DESTRUCTION (OUR APPROXIMATION)")

ch("The numbers")
sc("""Now the figures, from the Wikipedia table. The L P four hundred has a three thousand, nine hundred twenty-nine cubic centimetre V twelve rated at three hundred seventy-five metric horsepower at eight thousand r p m, and three hundred sixty-one newton-metres. Dry weight is one thousand, sixty-five kilograms. Zero to a hundred in five point four seconds. One hundred fifty-seven were built.""",
   "Lamborghini Countach LP400", "LP400: 3.9 L V12 · 375 PS · 361 NM · 1,065 KG DRY · 0–100 IN 5.4 S · 157 BUILT")
sc("""Top speed is where things get interesting. The table gives two hundred eighty-eight kilometres per hour measured, with three hundred fifteen claimed. By our arithmetic, the claim is nine percent above the measurement, or twenty-seven kilometres per hour. Wikipedia also lists a Walter Wolf special at three hundred fifteen or three hundred twenty-four claimed. Claims and measurements are different things.""",
   "Lamborghini Countach", "LP400 TOP SPEED: 288 KM/H MEASURED VS 315 CLAIMED (+9%, OUR ARITHMETIC)")
sc("""The L P four hundred S followed. Wikipedia lists three hundred forty-nine or three hundred fifty metric horsepower, depending on whether you read the table or the text, with two hundred fifty-four kilometres per hour measured and two hundred seventy-nine point six claimed. Two hundred thirty-seven were built, in three series of fifty, one hundred five and eighty-two. It was slower than the car it replaced.""",
   "Lamborghini Countach LP400 S", "LP400 S: 349/350 PS · 254 KM/H MEASURED · 237 BUILT (50 + 105 + 82)")
sc("""Our arithmetic: fifty plus one hundred five plus eighty-two is two hundred thirty-seven, which matches the page. The S measured about thirty-four kilometres per hour slower than the L P four hundred, about twelve percent. The page explains part of this: the optional rear wing improved high-speed stability, but cut top speed by at least sixteen kilometres per hour.""",
   "Countach rear wing", "LP400 S ≈ 12% SLOWER THAN LP400 · WING COST AT LEAST 16 KM/H (OUR ARITHMETIC + WIKIPEDIA)")
sc("""Then the engine grew. The L P five hundred S has a four thousand, seven hundred fifty-four cubic centimetre V twelve, the page says, with three hundred seventy-five metric horsepower and two hundred ninety-three kilometres per hour. Three hundred twenty-one were built. The five thousand Quattrovalvole has five thousand, one hundred sixty-seven cubic centimetres and four hundred fifty-five metric horsepower, and six hundred ten were built.""",
   "Lamborghini Countach 5000 QV", "LP500 S: 4.75 L · 375 PS · 321 BUILT · 5000 QV: 5.17 L · 455 PS · 610 BUILT")
sc("""The last version was the twenty-fifth Anniversary, restyled by Horacio Pagani, with six hundred fifty-seven built and a listed top speed of two hundred ninety-eight kilometres per hour. Add them up, by our arithmetic: one, plus one fifty-seven, plus two thirty-seven, plus three twenty-one, plus six ten, plus six fifty-seven. The total is one thousand, nine hundred eighty-three, which matches the page.""",
   "Countach 25th Anniversary", "TOTAL 1,983 (INCLUDING THE PROTOTYPE) · 25TH ANNIVERSARY: 657 BUILT")
sc("""Notice the shape of that production curve. Wikipedia says substantially more than half the cars were built in the final five years. By our arithmetic, the Quattrovalvole and the anniversary car together account for one thousand, two hundred sixty-seven cars, about sixty-four percent of the total. The car became more popular as it aged.""",
   "Lamborghini Countach production", "5000 QV + 25TH ANNIVERSARY = 1,267 CARS ≈ 64% (OUR ARITHMETIC)")

ch("The sixteen-year question")
sc("""How long was the Countach made? Wikipedia says nineteen seventy-four to nineteen ninety, which is sixteen years. But the same article also refers to a nineteen-year lifespan, which, by our reading, counts from the nineteen seventy-one prototype. Two numbers for one car, because it depends on whether you start the clock at the show or at the showroom.""",
   "Lamborghini Countach", "16 YEARS (1974–1990) OR 19 YEARS (FROM THE 1971 PROTOTYPE)")
sc("""Here is why the long production matters. The Countach started as a Bertone show car, passed through the Wolf special era, a series of engine growths, a grey-market period in the United States and a Pagani facelift. It was effectively several cars with one name. Treating it as a single model, as many lists do, hides how much changed under the same silhouette.""",
   "Lamborghini Countach", "SEVERAL CARS WITH ONE NAME (OUR READING)")
sc("""The page also notes that the V twelve itself dates from nineteen sixty-three, and was designed by Giotto Bizzarrini. By our arithmetic, the engine in the last Countach, built in nineteen ninety, was twenty-seven years old in design. That is not a flaw; the engine grew from three point nine to five point two litres. It is a reminder that the car's shape was new, but its heart was not.""",
   "Lamborghini V12", "V12 DESIGNED 1963 BY GIOTTO BIZZARRINI · 27 YEARS OLD IN 1990 (OUR ARITHMETIC)")

ch("The American connection")
sc("""The United States was Lamborghini's largest market, Wikipedia says, yet the Countach was not built to U S or Canadian standards. Owners paid to modify cars during the grey-market era, which the page dates from nineteen seventy-six to nineteen eighty-eight. The first U S-specification factory model was the nineteen eighty-five five thousand Quattrovalvole, with larger bumpers and Bosch K-Jetronic fuel injection.""",
   "Lamborghini Countach in America", "GREY MARKET 1976–1988 · FIRST US-SPEC MODEL: 1985 5000 QV")
sc("""A Countach was also used as the Monaco Grand Prix safety car from nineteen eighty to nineteen eighty-three, the page says. And cars older than twenty-five years are exempt from U S federal design, safety and emissions rules. For a car that was never officially sold in the United States for its first decade, that exemption is an important part of its American story.""",
   "Monaco Grand Prix", "MONACO GP SAFETY CAR 1980–83 · 25-YEAR-OLD CARS EXEMPT FROM US RULES")
sc("""The Cannonball Run is mentioned too, but only as using a nineteen seventy-nine U S-model L P four hundred S. The page says the upper front spoiler on that car is unique to grey-market cars. That is all it says. The film associations that fans remember are not documented in our sources, so we leave them out.""",
   "Lamborghini Countach LP400 S", "CANNONBALL RUN: ONLY A 1979 US-MODEL LP400 S IS MENTIONED")

ch("The cars that were never built")
sc("""Wikipedia lists several Countach projects that went no further. The L one fifty, from nineteen eighty-four to nineteen eighty-seven, was an update that Patrick Mimran rejected on cost grounds. The Q V X, in nineteen eighty-five, was a Group C racing car using a five point seven litre Countach-derived engine, not built by the factory. And a one-off, the Evoluzione, was destroyed in crash testing.""",
   "Lamborghini Countach Evoluzione", "UNBUILT: L150 (1984–87) · QVX GROUP C CAR (1985) · EVOLUZIONE DESTROYED")
sc("""The Evoluzione has disputed numbers. The text says about five hundred metric horsepower, a top speed of about three hundred twenty kilometres per hour and three hundred ninety-seven kilograms lighter than the Quattrovalvole. The table says four hundred fifty-five horsepower, three hundred thirty, and one thousand, fifty kilograms. We cannot reconcile them, so we say so.""",
   "Lamborghini Countach Evoluzione", "EVOLUZIONE: ~500 PS / 320 KM/H (TEXT) VS 455 PS / 330 KM/H (TABLE)")
sc("""And there were turbo Countachs. Max Bobnar, Lamborghini's Swiss distributor, commissioned two between nineteen eighty and nineteen eighty-two. The L P five hundred S Turbo, shown at Geneva in nineteen eighty-four, weighed one thousand, five hundred fifteen kilograms, with a claimed seven hundred fifty-nine metric horsepower in the text and seven hundred forty-six in the table, and a claimed top speed of three hundred thirty-five.""",
   "Max Bobnar", "LP500 S TURBO (1984): 1,515 KG · 759 PS (TEXT) / 746 PS (TABLE) · 335 KM/H CLAIMED")

ch("The tractor maker")
sc("""Who was the man behind the name on the nose? Wikipedia says Ferruccio Lamborghini was born on the twenty-eighth of April, nineteen sixteen in Renazzo di Cento, to a family of wine growers. He was drawn more to farm machinery than to farming. He was drafted into the Italian air force in nineteen forty and served as a mechanic on the island of Rhodes.""",
   "Ferruccio Lamborghini", "BORN APRIL 28, 1916 · AIR FORCE MECHANIC ON RHODES FROM 1940")
sc("""After the war he returned to Italy in nineteen forty-six. The page says he bought surplus military vehicles and converted them into agricultural machines. His first tractors, around nineteen forty-seven, used engines from Morris trucks and a fuel atomiser that let them start on petrol and run on cheaper diesel. He founded Lamborghini Trattori in nineteen forty-eight.""",
   "Lamborghini tractor", "SURPLUS VEHICLES → TRACTORS · LAMBORGHINI TRATTORI 1948 (WIKIPEDIA)")
sc("""The tractor money paid for the dream. Wikipedia says his income let him buy fast cars, among them Alfa Romeos, Lancias, a Mercedes three hundred S L, a Jaguar E-Type, two Maserati thirty-five hundred G Ts and several Ferrari two fifty G Ts. He opened Automobili Lamborghini in nineteen sixty-three at Sant'Agata Bolognese. A heating business followed in nineteen fifty-nine and a hydraulics firm in nineteen sixty-nine.""",
   "Ferruccio Lamborghini's cars", "AUTOMOBILI LAMBORGHINI FOUNDED 1963 AT SANT'AGATA BOLOGNESE")
sc("""The famous story says he started making cars after Enzo Ferrari insulted him about a clutch. Wikipedia describes that tale as being as much the stuff of legend as of fact. In a nineteen ninety-one interview, the page says, he recalled being told he could drive a tractor but never handle a Ferrari. The page also says his motives are unclear, and notes an author who argues economic motives were stronger.""",
   "Enzo Ferrari and Ferruccio Lamborghini", "THE FERRARI CLUTCH STORY: 'AS MUCH LEGEND AS FACT' (WIKIPEDIA)")
sc("""We tell you that not to spoil a good story, but because the story is the first thing people repeat about the Countach's maker. The sources support the clutch complaint and the quotation from the nineteen ninety-one interview. They do not settle why he really entered the car business. So the safest version is that both the legend and the economics may be part of it.""",
   "Lamborghini Trattori", "THE SOURCES DO NOT SETTLE WHY HE ENTERED THE CAR BUSINESS")

ch("The Wolf special")
sc("""One more Countach story is better documented. Wikipedia says Walter Wolf bought an L P four hundred in nineteen seventy-five. The page says Dallara built a special version of chassis one one two zero one four eight with the five litre engine from the L P five hundred prototype, rated at four hundred fifty-three metric horsepower at seven thousand, nine hundred r p m.""",
   "Walter Wolf Countach", "WOLF SPECIAL (1975): 5.0 L ENGINE · 453 PS AT 7,900 RPM")
sc("""It had a rear wing, which the page calls a precursor of the optional wing on the L P four hundred S. Its claimed top speed was three hundred fifteen or three hundred twenty-four kilometres per hour, depending on the source. The wing improved stability but cost at least sixteen kilometres per hour. Two more Wolf specials were built, one shown at Geneva in nineteen seventy-eight.""",
   "Countach rear wing", "WOLF SPECIAL: CLAIMED 315 OR 324 KM/H · 3 CARS BUILT")
sc("""There is a small contradiction on that page. The Geneva car, chassis one one two one two one zero, is called the very first L P four hundred S, but its number falls in the second series, after chassis one one two one one zero zero. We cannot resolve it. We flag it, because it shows how even a well-documented car has loose ends.""",
   "Geneva Motor Show 1978", "CHASSIS 1121210: 'VERY FIRST' LP400 S, YET IN THE SECOND SERIES (WIKIPEDIA)")

ch("What these cars sell for")
sc("""Now what the early cars sell for. RM Sotheby's Arizona sale of twenty twenty-six offered a nineteen seventy-seven L P four hundred Periscopio, chassis one one two zero two six two. It sold for eight hundred eighty-five thousand dollars. The page does not say whether that includes the buyer's premium. It was built right-hand drive for Australia and bought new by the singer Rod Stewart.""",
   "Countach LP400 Periscopio", "RM SOTHEBY'S ARIZONA 2026: LP400 PERISCOPIO $885,000 (ROD STEWART'S CAR)")
sc("""The same chassis had sold before. The Jalopy reports that it made seven hundred seventy-five thousand euros at RM Sotheby's Paris in February twenty twenty-one, after failing to reach its reserve at Artcurial's Retromobile sale in twenty twenty, where the estimate was eight hundred thousand to one point two million euros. We do not convert currencies, so we cannot say how much it rose.""",
   "Rod Stewart's Countach", "SAME CAR: €775,000 (PARIS, FEB 2021) · NO SALE AT RETROMOBILE 2020")
sc("""Hagerty's valuation page, from April twenty twenty-five, shows one million dollars for a nineteen seventy-five L P four hundred in good condition with average specification. It does not list the other condition levels. Together with the auction result, that suggests the early cars trade around the high six figures to a million. That is our reading of two data points, not an index.""",
   "Hagerty valuation", "HAGERTY (APR 2025): 1975 LP400 'GOOD' = $1,000,000")
sc("""RM Sotheby's also sold a nineteen eighty-nine twenty-fifth Anniversary car in Arizona in twenty twenty-four for four hundred seventy-eight thousand dollars. It had 15,430 kilometres and had been with one owner since nineteen ninety-nine. The page says invoices since two thousand one total over sixty-eight thousand dollars. By our arithmetic, that is about fourteen percent of the sale price spent on service over roughly twenty-three years.""",
   "Countach 25th Anniversary", "25TH ANNIVERSARY SOLD $478,000 · SERVICE INVOICES SINCE 2001 > $68,000 (≈14%)")

ch("The Miura it replaced")
sc("""Back to the car the Countach replaced. Wikipedia says the Miura rolling chassis appeared at the nineteen sixty-five Turin show and showgoers placed orders before there was a body. Bertone finished the body just days before the nineteen sixty-six Geneva Motor Show. The engineers had not checked whether the engine fitted the engine bay properly.""",
   "Lamborghini Miura at Geneva", "MIURA: ORDERS TAKEN AT TURIN 1965 BEFORE THERE WAS A BODY")
sc("""So the page says they filled it with ballast and kept the bonnet locked at Geneva. Sales head Ubaldo Sgarzi turned away journalists who wanted to see the engine. Marcello Gandini's styling and the mid-engine layout made the Miura the highlight of the show. The Countach would be designed by the same stylist, five years later.""",
   "Ubaldo Sgarzi", "MIURA AT GENEVA 1966: BALLAST UNDER A LOCKED BONNET")

ch("Recap")
sc("""So, two things you may not have known. First, the name is not a bull. It is a Piedmontese exclamation of astonishment, a worker's joke that was adopted, and the story about Bertone exclaiming it is unsupported in our source. Second, the original production car had a periscope, because the driver could not see out of the back, and the prototype was crash-tested to destruction.""",
   "Lamborghini Countach", "1. THE NAME IS AN EXCLAMATION, NOT A BULL · 2. THE PERISCOPE")
sc("""The numbers add up to a car that changed constantly. One thousand, nine hundred eighty-three units, six variants, a sixteen-year production run, and measured top speeds well below the claimed ones. Where the sources disagreed, we said so. If you know a figure we missed, put it in the comments with the source.""",
   "Lamborghini Countach", "1,983 UNITS · 16 YEARS · CLAIMED SPEEDS ABOVE MEASURED")
sc("""Which would you have wanted, the Periscopio or the Quattrovalvole? Tell us in the comments. In the other videos of this series, we compare the Countach with the Miura, work out what it really costs to own a classic Lamborghini, and tell how a tractor maker ended up building the Countach. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video117", "2 Things You Didn't Know About the Lamborghini Countach", [
    "Wikipedia, Lamborghini Countach: https://en.wikipedia.org/wiki/Lamborghini_Countach",
    "Wikipedia, Lamborghini Miura: https://en.wikipedia.org/wiki/Lamborghini_Miura",
    "Wikipedia, Ferruccio Lamborghini: https://en.wikipedia.org/wiki/Ferruccio_Lamborghini",
    "RM Sotheby's, 1977 Lamborghini Countach LP400 Periscopio by Bertone (Arizona 2026, lot 141): https://rmsothebys.com/auctions/az26/lots/r0060-1977-lamborghini-countach-lp400-periscopio-by-bertone",
], "A")
