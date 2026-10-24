import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In twenty seventeen, Lamborghini sold three thousand, eight hundred fifteen cars. Two years later, it sold eight thousand, two hundred five. More than half of them were one single model, and it was an SUV. The company that built the Miura and the Countach had bet its future on a family car with five seats. This is why Lamborghini bet everything on the Urus, and whether the bet paid off.""",
   "Lamborghini Urus", "WHY LAMBORGHINI BET EVERYTHING ON AN SUV")
sc("""Here is the twist. This was not the first time. Lamborghini had built an SUV in nineteen eighty-six, a military-style truck with a Countach engine, and it was cancelled after only three hundred one were built. The Urus is the second attempt. And the second attempt changed the company completely.""",
   "Lamborghini LM002", "IT WAS THE SECOND TIME")
sc("""Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. Let us start with a company that has gone bankrupt before.""",
   "Lamborghini Urus", "EVERY FACT IS SOURCED")

# ---------- 1. A COMPANY THAT NEARLY DISAPPEARED ----------
ch("A company with a fragile history")
sc("""Wikipedia says Ferruccio Lamborghini, who already made tractors, founded Lamborghini Automobili in Sant'Agata Bolognese on the seventh of May, nineteen sixty-three. The first series-produced car, the three fifty G T, followed in nineteen sixty-six, the same year as the Miura. It was a quick rise for a company that began as a tractor maker's hobby.""",
   "Ferruccio Lamborghini", "FOUNDED 7 MAY 1963")
sc("""But the story was not smooth. Wikipedia says that in nineteen seventy-two Ferruccio sold a majority stake to Georges-Henri Rossetti, sold the rest to René Leimer, and fully retired in nineteen seventy-four. In nineteen seventy-eight the company went bankrupt, and the Mimran brothers took over through receivership.""",
   "Lamborghini 1970s", "1978: BANKRUPTCY")
sc("""The ownership table is a list of changes. Patrick Mimran from nineteen eighty-four to nineteen eighty-seven. Chrysler Corporation from nineteen eighty-seven to nineteen ninety-four. MegaTech for a year. V'Power and Mycom Setdco from nineteen ninety-five to nineteen ninety-eight. And Audi, part of the Volkswagen Group, since nineteen ninety-eight. By our count, the table shows eight ownership periods in sixty-two years.""",
   "Lamborghini owners", "6 OWNERS IN ~35 YEARS")
sc("""The 2005 numbers show how small the company was. An article in Yahoo Autos says that in two thousand five, the year Stephan Winkelmann was appointed president and chief executive, the brand sold sixteen hundred cars. Remember that number. Twenty years later, Wikipedia lists deliveries of ten thousand, seven hundred forty-seven.""",
   "Stephan Winkelmann", "2005: 1,600 CARS SOLD")

# ---------- 2. THE FIRST ATTEMPT ----------
ch("The first attempt: the LM002")
sc("""Now the first SUV. Wikipedia says the LM002, short for Lamborghini Militaire, was an off-road vehicle unveiled at the nineteen eighty-six Brussels Auto Show. It was, the page says, an unusual departure for a company then mainly known for high-performance, hand-built sports cars. Nicknamed the Rambo-Lambo, it was built from nineteen eighty-six to nineteen ninety-three.""",
   "Lamborghini LM002", "1986: THE \"RAMBO-LAMBO\"")
sc("""It had the Countach's five point two litre V twelve in the front. Wikipedia lists a curb weight of two thousand seven hundred kilograms, a five-speed manual gearbox, a tubular steel frame with riveted aluminium panels, and a hundred sixty-nine litre fuel tank. It rode on custom run-flat Pirelli Scorpion tyres, with separate tread designs for mixed use and for sand.""",
   "Lamborghini LM002 off-road", "COUNTACH V12 · 2,700 KG · 169-LITRE TANK")
sc("""Its origins were military. Wikipedia says the Cheetah prototype of nineteen seventy-seven was Lamborghini's first military vehicle, built in the hope of selling to oil exploration companies, and used a rear-mounted Chrysler V eight. The LM001 followed, then a new chassis that moved the Countach V twelve to the front, which became the LM002.""",
   "Lamborghini Cheetah", "FROM THE CHEETAH TO THE LM002")
sc("""Civilian models had a luxury package, Wikipedia says: full leather, tinted power windows, air conditioning and a roof-console premium stereo. The last sixty were the LM American, sold only in the United States, first shown at the nineteen ninety-two Detroit Auto Show. A truck for the sand with a leather interior.""",
   "Lamborghini LM002 interior", "LAST 60: THE LM/AMERICAN")
sc("""How many were built? Wikipedia says three hundred one in total. By our own arithmetic, that is about forty-three a year over seven years. The page says that when the end was announced in nineteen ninety-one, Lamborghini claimed about eight hundred orders, but the complicated manufacturing process made them discontinue the car, so it could focus on more profitable models.""",
   "Lamborghini LM002 production", "301 BUILT · ~800 ORDERS CLAIMED")
sc("""So the first SUV failed, not because nobody wanted it, but because it was too hard to build. That lesson matters. Wikipedia lists the Urus as the LM002's spiritual successor. And the Urus would be built a very different way: on the Volkswagen Group's platform, with parts shared with other brands, so it could be built in large numbers.""",
   "Lamborghini Urus and LM002", "THE LESSON: MAKE IT EASY TO BUILD")

sc("""The LM002 had a colourful life. Wikipedia says a Turin coachbuilder, Salvatore Diomante, built a one-off estate version for the Sultan of Brunei, and that Uday Hussein owned one, which U.S. forces blew up in two thousand four in a car-bomb test. It appeared in films including No Holds Barred, Toys and Fast and Furious. It was a car people remembered, even if few were built.""",
   "Lamborghini LM002 owners", "SULTAN OF BRUNEI · FILM STAR")
sc("""The LM002 also went racing, in a way. Wikipedia says the LM002 Evoluzione of nineteen eighty-eight was tuned to six hundred metric horsepower for the Paris-Dakar, but funding ran out before it could officially enter. Sandro Munari drove the white car in the Rallye des Pharaons in Egypt and in Greece. A company that could not afford its own rally programme was already dreaming big.""",
   "Lamborghini LM002 Evoluzione", "EVOLUZIONE: 600 PS, NO FUNDS FOR DAKAR")
# ---------- 3. THE IDEA ----------
ch("The idea returns: Beijing, 2012")
sc("""Wikipedia says the Urus concept was unveiled at the Beijing Auto Show on the twenty-third of April, twenty twelve. It had a five point two litre V ten from the Gallardo, rated at six hundred metric horsepower, and all-wheel drive. It was also shown at Pebble Beach that year. Designer Filippo Perini is credited with the concept.""",
   "Lamborghini Urus concept 2012", "23 APRIL 2012: BEIJING")
sc("""Stephan Winkelmann described the decision in the Yahoo Autos article. We decided to do an SUV soon after that, he said, but it took years to get there. By our arithmetic, the production Urus was shown on the fourth of December, twenty seventeen, five years and eight months after the concept. That is long, even by car industry standards.""",
   "Stephan Winkelmann", "\"IT TOOK YEARS TO GET THERE\"")
sc("""The production car changed a lot. Wikipedia says its exterior and powertrain differed substantially from the concept, and that Mitja Borkert designed the production version. The V ten was replaced by a four litre twin-turbo V eight, based on an Audi engine and assembled at a Volkswagen plant in Hungary. The car sits on the Volkswagen Group's M L B Evo platform.""",
   "Lamborghini Urus production", "V10 CONCEPT → TWIN-TURBO V8")
sc("""Winkelmann addressed the shared platform directly. In the article he says it has a common platform, but our engineers did a fantastic job creating a car which is a real Lamborghini. The page lists the Audi Q7, Bentley Bentayga, Porsche Cayenne and Volkswagen Touareg as platform relatives. Sharing is how the Urus could be built at all.""",
   "Lamborghini Urus platform", "\"A REAL LAMBORGHINI\"")
sc("""The target was clear. Wikipedia says deliveries began in early twenty eighteen, with a target of about three thousand five hundred units a year. It also says that the company aimed to double its sales volume by twenty nineteen after adding the Urus. In 2017, Lamborghini delivered three thousand, eight hundred fifteen cars. Doubling that is seven thousand, six hundred thirty.""",
   "Lamborghini Urus launch", "TARGET: ~3,500 URUS A YEAR · DOUBLE THE VOLUME")

sc("""The name has its own story. Wikipedia says Urus is the ancestor of modern domestic cattle, also called the aurochs, and that the Latin word urus meant wild ox from the Gallic Wars onward. Lamborghini had trademarked the name earlier, and blogs in two thousand eight expected it for what became the Estoque. The bull is the brand's symbol, and the wild ox is an older bull.""",
   "Aurochs", "URUS = THE WILD OX")
sc("""The finished car was fast. Wikipedia lists six hundred fifty metric horsepower at six thousand r p m and eight hundred fifty newton-metres from two thousand two hundred fifty to four thousand five hundred, zero to a hundred in three point six seconds, zero to two hundred in twelve point eight, and a top speed of about three hundred five kilometres per hour. The page says it weighs under two thousand two hundred kilograms, thanks to carbon fibre.""",
   "Lamborghini Urus", "650 PS · 0–100 IN 3.6 S · ~305 KM/H")
sc("""The engine borrowed from the group, but with changes. Wikipedia says it was uprated by a hundred metric horsepower and eighty newton-metres over the Porsche Cayenne Turbo. The Urus Performante, later, made six hundred sixty-six metric horsepower, was forty-seven kilograms lighter and claimed three point three seconds to a hundred. A race version, the S T-X, was said to be twenty-five percent lighter than the street car.""",
   "Lamborghini Urus Performante", "PERFORMANTE: 666 PS, −47 KG")
sc("""In the Urus's first year, 2018, Wikipedia lists a total of five thousand, seven hundred fifty deliveries for Lamborghini, against three thousand, eight hundred fifteen the year before. By our arithmetic, that is a jump of about fifty-one percent. And the Urus itself accounted for two thousand, five hundred sixty-five of the cars built in that first year, according to the production table.""",
   "Lamborghini 2018", "2018: +51% DELIVERIES")
# ---------- 4. THE RESULT ----------
ch("What happened: the numbers")
sc("""Did it work? Wikipedia lists Lamborghini deliveries of three thousand, eight hundred fifteen in twenty seventeen, five thousand, seven hundred fifty in twenty eighteen, and eight thousand, two hundred five in twenty nineteen. By our own arithmetic, the volume more than doubled in two years, up by about one hundred fifteen percent. The target of doubling was beaten.""",
   "Lamborghini deliveries", "2017: 3,815 → 2019: 8,205 (+115%)")
sc("""Carscoops reported that the Urus contributed four thousand, nine hundred sixty-two cars in twenty nineteen, a whopping sixty-one percent of total sales, with total volume up forty-three percent on the previous year. CEO Stefano Domenicali said that the year two thousand nineteen was the most successful in the company's history.""",
   "Lamborghini 2019 sales", "2019: URUS = 61% OF ALL SALES")
sc("""The sources count the Urus slightly differently. Wikipedia's Urus table lists five thousand, two hundred thirty-three for twenty nineteen, which is probably production, against four thousand, nine hundred sixty-two in Carscoops, which is deliveries. A difference of two hundred seventy-one cars. We use each as the source gives it, and do not mix them.""",
   "Lamborghini Urus 2019", "PRODUCTION VS DELIVERIES: 5,233 VS 4,962")
sc("""The United States was the biggest market in twenty nineteen, with two thousand, three hundred seventy-four deliveries, according to Carscoops. Then came mainland China with Hong Kong and Macau at seven hundred seventy, the United Kingdom at six hundred fifty-eight, Japan at six hundred forty-one and Germany at five hundred sixty-two.""",
   "Lamborghini US market", "US: 2,374 · CHINA: 770 · UK: 658")
sc("""Wikipedia lists Urus numbers for each year: one hundred twenty-one in twenty seventeen, two thousand, five hundred sixty-five in twenty eighteen, then four thousand, three hundred sixty-four in twenty twenty, five thousand, two hundred forty in twenty twenty-one, five thousand, seven hundred eighty-five in twenty twenty-two, and six thousand in twenty twenty-three.""",
   "Lamborghini Urus sales chart", "URUS: 2,565 → 5,233 → 4,364 → 5,240 → 5,785")
sc("""Then six thousand, six hundred eighty-one in twenty twenty-four, and seven thousand, two hundred sixty-five in twenty twenty-five. By our own arithmetic, the nine years add up to forty-three thousand, two hundred fifty-four. And Wikipedia says the ten thousandth Urus was announced in July twenty twenty, and twenty thousand by twenty twenty-two, the fastest for any Lamborghini.""",
   "Lamborghini Urus 10,000th", "10,000TH IN JULY 2020 · 20,000 BY 2022")
sc("""Look at the whole company in twenty twenty-five. Wikipedia lists deliveries of ten thousand, seven hundred forty-seven. By our own arithmetic, seven thousand, two hundred sixty-five Urus would be about sixty-eight percent of that. This mixes production with deliveries, so treat it as a rough indication. The Yahoo article says the Urus accounts for significantly more than half of annual sales.""",
   "Lamborghini 2025", "URUS ≈ 2/3 OF THE COMPANY (ROUGH)")

sc("""After the first record year, the company kept growing. Wikipedia lists deliveries of seven thousand, four hundred thirty in twenty twenty, eight thousand, four hundred five in twenty twenty-one, nine thousand, two hundred thirty-three in twenty twenty-two, and ten thousand, one hundred twelve in twenty twenty-three. Then ten thousand, six hundred eighty-seven, and ten thousand, seven hundred forty-seven.""",
   "Lamborghini deliveries 2020-2025", "2020: 7,430 → 2025: 10,747")
sc("""By our own arithmetic, deliveries in twenty twenty-five were about thirty-one percent above twenty nineteen, and about one hundred eighty-two percent above twenty seventeen, the year before the Urus. In twenty twenty, deliveries dipped about nine percent from twenty nineteen, then recovered. The shape of the curve is up.""",
   "Lamborghini sales chart", "2025 VS 2017: +182%")
sc("""The Yahoo article quotes Winkelmann on whether the SUV is a real Lamborghini. Nobody who drives an Urus ever doubts this, he says. It is, of course, the opinion of the man who made the decision. But his claim comes with eight hundred thirty-five million euros of operating income and a sixty-eight percent share of sales, by our rough arithmetic. That is a strong case.""",
   "Stephan Winkelmann", "\"NOBODY WHO DRIVES AN URUS EVER DOUBTS THIS\"")
sc("""Wikipedia gives one more number about the company's size. In December twenty twenty, Lamborghini had one thousand, seven hundred seventy-nine employees. By our arithmetic, with seven thousand, four hundred thirty deliveries that year, that is about four cars per employee. It remained a small company, with a very large product in its range.""",
   "Lamborghini employees", "1,779 EMPLOYEES (DEC 2020)")
# ---------- 5. THE MONEY ----------
ch("What it did to the company")
sc("""The money followed. Wikipedia says that in twenty twenty-four, Lamborghini reported revenue of three point one billion euros and an operating income of eight hundred thirty-five million. By our own arithmetic, that is an operating margin of nearly twenty-seven percent. For a carmaker, that is a high figure. The Yahoo article calls the Urus a huge profit driver for the Volkswagen Group.""",
   "Lamborghini finances", "2024: €3.10B REVENUE · €835M OPERATING INCOME")
sc("""To put that in context, Wikipedia also lists a net income of ten point one million euros for twenty fourteen. Net income and operating income are different measures, so we cannot compare them directly. But the scale of the change, from ten million to hundreds of millions, shows why Volkswagen was happy to approve the SUV.""",
   "Lamborghini 2014", "2014 NET INCOME: €10.1M")
sc("""The Urus also changed the factory. Wikipedia says the Sant'Agata Bolognese site grew from eighty thousand to one hundred sixty thousand square metres when the Urus launched. By our arithmetic, that is exactly double. A company that built a few thousand sports cars now needed a second set of buildings for one SUV.""",
   "Sant'Agata Bolognese factory", "FACTORY AREA: 80,000 → 160,000 M²")
sc("""Winkelmann has been at the helm of Lamborghini for fifteen of the past twenty years, according to the Yahoo Autos article, which says that he transformed the company beyond recognition. In his own words, they see themselves as brave, unexpected and authentic. By our arithmetic, sixteen hundred cars in two thousand five to ten thousand seven hundred forty-seven in twenty twenty-five is about a 6.7 times increase.""",
   "Stephan Winkelmann Lamborghini", "1,600 → 10,747 IN 20 YEARS (6.7×)")

# ---------- 6. THE RISKS ----------
ch("The risks of the bet")
sc("""A bet this big has risks. The Yahoo article makes a pointed remark about other brands: performance brands with similar heritage such as Maserati and Lotus have struggled to maintain an identity. It does not say that of Lamborghini, but it shows the danger of chasing volume. A brand can sell more cars and lose what made it special.""",
   "Lamborghini brand identity", "THE DANGER OF VOLUME")
sc("""The Urus also had quality problems. Wikipedia says that in November twenty twenty, the N H T S A recalled two thousand, eight hundred thirty-one Urus, from the twenty nineteen and twenty twenty model years, over a fuel-line connector that was a fire risk. Wikipedia adds that Porsche had identified the issue in twenty nineteen.""",
   "Lamborghini Urus recall", "NOV 2020: 2,831 CARS RECALLED")
sc("""In May twenty twenty-four, Wikipedia says, two thousand, one hundred thirty-three Urus from the twenty twenty-three and twenty twenty-four model years were recalled because the hood latch striker rivets could fail, allowing the hood to detach above ninety-four miles per hour. A high-volume car brings high-volume problems.""",
   "Lamborghini Urus hood", "MAY 2024: 2,133 CARS RECALLED")
sc("""There is also the strategic risk of dependence. By our arithmetic, if the Urus is roughly two thirds of the company, then a bad year for SUVs would be a bad year for Lamborghini. The twenty twenty numbers show a small version of that: Urus production fell from five thousand, two hundred thirty-three to four thousand, three hundred sixty-four.""",
   "Lamborghini Urus 2020", "2020: URUS DOWN 17%")

sc("""Winkelmann's other big decision was about hybrids. Wikipedia says the Asterion L P I nine ten dash four, a hybrid concept from twenty fourteen, was the company's first, with a claimed combined output of nine hundred seven horsepower. So the company that started with a V twelve at the front of a truck is now defined by plug-ins, and the SUV came right in the middle of that story.""",
   "Lamborghini Asterion", "2014: ASTERION HYBRID CONCEPT, 907 HP")
sc("""Let us step back and count what changed, by our own arithmetic. Thirteen years separate the Beijing concept in twenty twelve and the twenty twenty-five figures. In those years, the company moved from a V ten concept to a plug-in V eight, from fifteen hundred cars to more than ten thousand, and from a single small factory to a site twice its size.""",
   "Lamborghini timeline", "CONCEPT 2012 → 10,747 CARS IN 2025")
sc("""The same pattern appears in the LM002 and the Urus. Both were SUVs. Both used the best engine the company could get. But one was built by hand on a tubular steel frame, and the other on a shared group platform. One sold three hundred one cars in seven years. The other sold more than seven thousand in a single year, in twenty twenty-five.""",
   "Lamborghini LM002 and Urus", "301 CARS IN 7 YEARS VS 7,265 IN ONE YEAR")
# ---------- 7. THE FUTURE ----------
ch("The bet continues")
sc("""Lamborghini has kept going. Wikipedia lists the Urus SE, a plug-in hybrid with a four litre V eight making six hundred twenty horsepower, plus an electric motor of one hundred eighty-nine, for a combined seven hundred ninety-nine horsepower and nine hundred fifty newton-metres. It describes it as the fastest production SUV in the world at launch, with a top speed of three hundred twelve kilometres per hour.""",
   "Lamborghini Urus SE", "URUS SE: 799 HP PLUG-IN HYBRID")
sc("""The Urus SE weighs about three hundred kilograms more than the Urus S because of its twenty-five point nine kilowatt-hour battery, according to Wikipedia. Even so, it reaches a hundred kilometres per hour in three point four seconds. The SUV that started as a bet has become a platform for the company's electrification plans.""",
   "Lamborghini Urus SE battery", "25.9 KWH BATTERY · +300 KG")
sc("""The wider range is changing too. Wikipedia lists the Revuelto, a V twelve hybrid with one thousand and one horsepower, and the Temerario, a mid-engine plug-in hybrid unveiled on the sixteenth of August, twenty twenty-four. In twenty twenty-one, Winkelmann said all models would be hybrid by two thousand twenty-four. The Urus was where the strategy began.""",
   "Lamborghini Revuelto", "REVUELTO · TEMERARIO · ALL HYBRID")
sc("""So was the bet worth it? On the numbers, yes. Deliveries went from three thousand eight hundred fifteen to ten thousand seven hundred forty-seven. The Urus became the best-selling Lamborghini ever. The company expanded its factory, and its operating income reached eight hundred thirty-five million euros. The sources we read describe the SUV as the engine of that growth.""",
   "Lamborghini Urus", "ON THE NUMBERS, THE BET PAID OFF")
sc("""But a bet is not only about the numbers. A reasonable person can still ask whether a Lamborghini should be a family car. The sources show that sales soared and that the company stayed profitable. They cannot tell you whether the brand lost something intangible. That part is a judgement, and it belongs to you.""",
   "Lamborghini Urus family", "NUMBERS CAN'T JUDGE THE BRAND")
sc("""Do you think Lamborghini was right to build the Urus? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Urus, compare it with the Ferrari Purosangue, and work out what it really costs to own one.""",
   "Lamborghini Urus", "WAS LAMBORGHINI RIGHT?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video100", "Why Lamborghini Bet Everything on an SUV", [
    "Wikipedia, Lamborghini: https://en.wikipedia.org/wiki/Lamborghini",
    "Wikipedia, Lamborghini Urus: https://en.wikipedia.org/wiki/Lamborghini_Urus",
    "Wikipedia, Lamborghini LM002: https://en.wikipedia.org/wiki/Lamborghini_LM002",
    "Carscoops, Lamborghini sold nearly 5,000 Urus SUVs last year (January 2020): https://www.carscoops.com/2020/01/lamborghini-sales-soar-43-percent-in-2019-thanks-to-urus-suv/",
    "Yahoo Autos, We're not selling mobility: how Stephan Winkelmann transformed Lamborghini: https://autos.yahoo.com/people-and-culture/articles/were-not-selling-mobility-stephan-083648052.html",
], "D")
