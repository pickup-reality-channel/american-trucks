import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""He did not come from racing. He did not come from a famous car family. He came from a farm town in northern Italy, he repaired military trucks, and he built tractors. Then, in nineteen sixty-three, he started a car company, and eleven years later his engineers launched the Lamborghini Countach. This is how a tractor maker ended up building one of the most famous supercars ever made.""",
   "Ferruccio Lamborghini", "HOW A TRACTOR MAKER ENDED UP BUILDING THE COUNTACH")
sc("""The usual version of this story has a single angry moment with Enzo Ferrari. The real record, according to our sources, is more complicated, and in places uncertain. We will tell it in order, say what is documented, and mark clearly what is legend. Every fact comes from a published source, listed in the description. Where we do the maths, we say so.""",
   "Ferruccio Lamborghini", "LEGEND VS RECORD")

ch("A farm boy who liked machines")
sc("""Wikipedia says Ferruccio Lamborghini was born on the twenty-eighth of April, nineteen sixteen, in Renazzo di Cento, in the Emilia-Romagna region of Italy. His parents, Antonio and Evelina, were wine growers. The page says he was drawn more to farm machinery than to farming, and that he studied at a technical institute near Bologna.""",
   "Renazzo di Cento", "BORN APRIL 28, 1916 · RENAZZO DI CENTO, EMILIA-ROMAGNA · PARENTS WERE WINE GROWERS")
sc("""What he studied is disputed. Wikipedia says the sources disagree: one says engineering without a degree, another industrial design, a third an industrial arts degree, and a fourth says he was drafted upon graduating in nineteen forty. We do not choose between them. The point is that even the basic facts of his education are not settled, which is a warning for everything that follows.""",
   "Technical institute near Bologna", "HIS STUDIES: ENGINEERING / INDUSTRIAL DESIGN / INDUSTRIAL ARTS — SOURCES DISAGREE")
sc("""In nineteen forty he was drafted into the Italian Royal Air Force. He served as a mechanic on the island of Rhodes, and became supervisor of the vehicle maintenance unit, Wikipedia says. After Italy's armistice in nineteen forty-three he stayed on the island, opened a small vehicle workshop with German permission, and was arrested as a collaborator when the British took Rhodes in nineteen forty-five.""",
   "Rhodes", "1940: AIR FORCE MECHANIC ON RHODES · 1945: ARRESTED WHEN THE BRITISH TOOK THE ISLAND")
sc("""He returned to Italy in nineteen forty-six. By our arithmetic, he was thirty years old, with six years of military service behind him and a skill that happened to be in demand: keeping machines running with whatever parts were available. That is our reading of the timeline. The sources say only that he went back and began to work with surplus vehicles.""",
   "Italy 1946", "RETURNED IN 1946, AGED ~30 (OUR ARITHMETIC)")
sc("""Wikipedia says he bought surplus military vehicles and converted them into agricultural machines. His first tractors, called the Carioca, around nineteen forty-seven, used engines from Morris trucks and a fuel atomiser that let them start on petrol and then run on cheaper diesel. The page gives nineteen forty-eight as the year he founded Lamborghini Trattori.""",
   "Lamborghini Carioca tractor", "CARIOCA TRACTOR c. 1947: MORRIS ENGINES + FUEL ATOMISER · LAMBORGHINI TRATTORI 1948")

ch("The money behind the dream")
sc("""The tractors made him rich enough to buy fast cars. Wikipedia lists Alfa Romeos, Lancias, a Mercedes-Benz three hundred S L, a Jaguar E-Type and two Maserati thirty-five hundred G Ts. It also says he bought several Ferrari two fifty G Ts, among them a short wheelbase Berlinetta and a two plus two. So he was a customer of the people he would later compete with.""",
   "Ferrari 250 GT", "HE OWNED ALFAS, LANCIAS, A 300 SL, AN E-TYPE, 2 MASERATIS AND SEVERAL FERRARI 250 GTs")
sc("""He built other businesses too. In nineteen fifty-nine, the page says, he opened an oil burner factory, Lamborghini Bruciatori, later called Lamborghini Calor, which moved into air conditioning. In nineteen sixty-nine he founded Lamborghini Oleodinamica, a hydraulics business. By our arithmetic, he was running tractors, heating and hydraulics before the car company was even four years old.""",
   "Lamborghini Calor", "1959: BURNERS / AIR CONDITIONING · 1969: HYDRAULICS · BEFORE THE CAR COMPANY WAS 4")
sc("""Then came the cars. Automobili Lamborghini was founded in nineteen sixty-three in Sant'Agata Bolognese, Wikipedia says. By our arithmetic, he was forty-seven. The page says he aimed to build a grand tourer with high performance, tractability, ride quality and good interiors. Note the words: not a race car, a refined road car. That matters for what happened next.""",
   "Sant'Agata Bolognese", "1963: AUTOMOBILI LAMBORGHINI · AIMED AT A REFINED GRAND TOURER · HE WAS 47 (OUR ARITHMETIC)")
sc("""The page notes that the first two cars carried alphanumeric names. The bull names started with the Miura. Wikipedia says he visited the ranch of the Miura family of fighting bulls near Seville in nineteen sixty-two, and the Miura was the fourth model he produced. Other bull names followed: Islero, Espada, Jarama, Urraco, Jalpa, Diablo. The Countach broke the pattern.""",
   "Lamborghini Miura", "BULL NAMES FROM THE MIURA (4TH MODEL) · ISLERO, ESPADA, JARAMA, URRACO, JALPA, DIABLO · NOT THE COUNTACH")

ch("The Ferrari story")
sc("""Now the legend. Wikipedia says Ferruccio Lamborghini complained that Ferrari's clutches were inferior and needed repeated rebuilds at Maranello. He raised the issue with Enzo Ferrari and was dismissed. In a nineteen ninety-one interview with Thoroughbred and Classic Cars, the page says, he recalled Ferrari telling him he could drive a tractor but never handle a Ferrari, which led him to build a perfect car.""",
   "Maranello", "1991 INTERVIEW: FERRARI SAID HE COULD 'DRIVE A TRACTOR' BUT NOT HANDLE A FERRARI")
sc("""He also said, according to the page, that Ferrari never spoke to him again. That is the whole of the documented story: a complaint about clutches, a dismissal, a remark recalled thirty years later. Wikipedia itself says the tale is as much the stuff of legend as of fact, and that his motives for entering the car business are unclear.""",
   "Ferruccio Lamborghini", "'FERRARI NEVER SPOKE TO ME AGAIN' · THE PAGE: 'AS MUCH LEGEND AS FACT'")
sc("""Wikipedia also cites an author, Sackey, who argues that economic motives were stronger than the insult. That is the sceptic's version: a businessman who already owned several Ferraris and saw a market. We do not know which version is right, and our sources do not say. The honest summary is that the tractor line is a good story that may be only part of the truth.""",
   "Ferruccio Lamborghini", "AN AUTHOR ARGUES ECONOMIC MOTIVES WERE STRONGER (WIKIPEDIA CITING SACKEY)")
sc("""There is a lesson in how the story has been used. A tractor maker beating Ferrari is a more satisfying tale than a rich industrialist spotting a gap. But the evidence we have shows both: he made tractors, he bought Ferraris, he built a refined grand tourer, and he later left the business. Whether pride or profit started it, the result was a car company.""",
   "Lamborghini factory", "BOTH THE LEGEND AND THE BUSINESS CASE FIT THE FACTS (OUR READING)")

ch("The Miura changes everything")
sc("""The Miura came next, and it was not his idea. Wikipedia says the engineers Giampaolo Dallara, Paolo Stanzani and Bob Wallace developed the prototype in their spare time, largely at night. Ferruccio preferred grand tourers to race-derived cars, but after seeing the development mule he approved and gave them a free hand, seeing the car as a possible marketing tool.""",
   "Lamborghini Miura", "THE MIURA WAS THE ENGINEERS' IDEA · HE APPROVED IT AS A POSSIBLE MARKETING TOOL")
sc("""So the car that made Lamborghini famous started as an unofficial night project by his own engineers. The rolling chassis appeared at the Turin show in nineteen sixty-five, and showgoers placed orders before there was a body. The Bertone body was finished days before the Geneva show of nineteen sixty-six. By our arithmetic, from prototype to show took about a year.""",
   "Turin Motor Show", "TURIN 1965: ORDERS BEFORE A BODY EXISTED · GENEVA 1966: BODY FINISHED DAYS BEFORE")
sc("""Wikipedia describes the show: the engineers had not checked whether the engine fitted the bay. They filled it with ballast and kept the bonnet locked, and sales head Ubaldo Sgarzi turned away journalists who wanted to look. The styling of Marcello Gandini and the mid-engine layout made it the star of the show. Whatever Ferruccio had planned, the Miura gave him a name.""",
   "Geneva Motor Show 1966", "BALLAST, A LOCKED BONNET AND ONE SALES HEAD TURNING JOURNALISTS AWAY")
sc("""The Miura's engine, Wikipedia says, was a three thousand, nine hundred twenty-nine cubic centimetre V twelve, mounted sideways behind the driver, with the engine and gearbox sharing one casting. The page calls it the first high-performance production road car with a rear mid-engine, rear-wheel-drive layout. The V twelve itself dates from nineteen sixty-three and was designed by Giotto Bizzarrini.""",
   "Lamborghini V12", "MIURA: V12 SIDEWAYS BEHIND THE DRIVER · FIRST HIGH-PERFORMANCE MID-ENGINE ROAD CAR · ENGINE DESIGNED 1963 BY BIZZARRINI")

ch("Trouble at the tractor factory")
sc("""Just as the cars took off, the tractors ran into trouble. Wikipedia says Lamborghini Trattori struggled in nineteen seventy-one and seventy-two after its South African importer cancelled orders and a Bolivian military government cancelled a large shipment. Those are the two causes the page names. It does not give the sizes of the orders, so we cannot put numbers on the loss.""",
   "Lamborghini tractors", "1971–72: SOUTH AFRICAN IMPORTER CANCELLED ORDERS · BOLIVIAN GOVERNMENT CANCELLED A LARGE SHIPMENT")
sc("""In nineteen seventy-two, the page says, he sold his entire tractor holding to SAME. Many retellings give nineteen seventy-three for that sale. The Wikipedia page we used says nineteen seventy-two, so we use that, and note the difference. The company that gave him his fortune, and his name, was no longer his.""",
   "SAME tractors", "TRACTOR HOLDING SOLD TO SAME IN 1972 (WIKIPEDIA) — OTHER ACCOUNTS SAY 1973")
sc("""Also in nineteen seventy-two, he sold fifty-one percent of Automobili Lamborghini to the Swiss businessman Georges-Henri Rossetti for six hundred thousand dollars. By our arithmetic, that values the whole company at about one point two million dollars. The car business that would later produce the Countach was, for him, a fraction of what the tractor business had been worth.""",
   "Georges-Henri Rossetti", "1972: 51% OF AUTOMOBILI LAMBORGHINI SOLD FOR $600,000 → IMPLIED ~$1.2M (OUR ARITHMETIC)")
sc("""In nineteen seventy-four, Wikipedia says, disillusioned, he sold his remaining forty-nine percent to René Leimer, a friend of Rossetti. The page gives no price for that second sale. By our arithmetic, he had owned the car company for eleven years, from nineteen sixty-three to nineteen seventy-four, and the tractor company for about twenty-four, from nineteen forty-eight to nineteen seventy-two.""",
   "René Leimer", "1974: REMAINING 49% SOLD TO RENÉ LEIMER · CAR COMPANY OWNED 11 YEARS, TRACTORS ~24 (OUR ARITHMETIC)")

ch("The Countach project")
sc("""Meanwhile, the next car was being built. Wikipedia says that, by nineteen seventy, the Miura had lost ground to rivals such as the Ferrari Daytona. Ferruccio Lamborghini launched a project to replace it. Chief engineer Paolo Stanzani started work in nineteen seventy under the name L P one twelve, with test driver Bob Wallace, assistant engineer Massimo Parenti and Marcello Gandini of Bertone.""",
   "Paolo Stanzani", "1970: PROJECT LP112 TO REPLACE THE MIURA · STANZANI, WALLACE, PARENTI, GANDINI")
sc("""The prototype, the L P five hundred, was shown at the Geneva show in nineteen seventy-one. The production L P four hundred debuted in nineteen seventy-four, about three years later. That is the same year the page says he sold his remaining shares. By our reading of the dates, the car he commissioned reached customers as he walked away.""",
   "Geneva Motor Show 1971", "LP500: GENEVA 1971 · LP400: 1974 — THE YEAR HE SOLD HIS LAST SHARES")
sc("""The sources do not tell us how involved he was in the Countach's design, so we cannot say how much of it was his. They say he launched the project. They say the engineers and the stylist built it. They do not quote him on the finished car. We avoid attributing views to him that the record does not contain.""",
   "Lamborghini Countach", "HE LAUNCHED THE PROJECT · THE SOURCES DO NOT QUOTE HIM ON THE FINISHED CAR")
sc("""The name was another departure. Wikipedia says it comes from a Piedmontese exclamation of astonishment. Marcello Gandini says the word was first used as a joke by a worker and then adopted, and he calls this the only true story behind it. The popular tale of Nuccio Bertone exclaiming the word on seeing the prototype is marked on the page as needing a citation.""",
   "Lamborghini Countach name", "COUNTACH = PIEDMONTESE EXCLAMATION · BERTONE STORY: 'CITATION NEEDED'")
sc("""The page is clear that the name broke the tradition of bull names that began with the Miura. So the car that arrived as he was leaving also departed from the naming habit of his own company. We should be careful: our sources do not say whether he approved the name. That detail is missing.""",
   "Lamborghini bull emblem", "THE COUNTACH BROKE THE BULL TRADITION · WHETHER HE APPROVED THE NAME IS NOT IN OUR SOURCES")

ch("What he did next")
sc("""After selling, Ferruccio Lamborghini retired. Wikipedia says that in nineteen seventy-four he moved to a roughly seven hundred forty acre estate called La Fiorita, on Lake Trasimeno in Castiglione del Lago, in Umbria, where he made wine and hunted. Many retellings place the winery in Tuscany, but the page we used says Umbria, so we use Umbria.""",
   "Lake Trasimeno", "1974: RETIRED TO LA FIORITA, ~740 ACRES, LAKE TRASIMENO, UMBRIA — WINE AND HUNTING")
sc("""He died of a heart attack at Silvestrini Hospital in Perugia on the twentieth of February, nineteen ninety-three, aged seventy-six, and is buried in Renazzo, the page says. By our arithmetic, he lived about nineteen years after leaving the car business, and the Countach stayed in production for sixteen of them, until nineteen ninety.""",
   "Perugia", "DIED FEB 20, 1993, AGED 76 · ~19 YEARS OF RETIREMENT (OUR ARITHMETIC)")
sc("""His family carries on in other ways. Wikipedia says his son Tonino, born in nineteen forty-seven, runs a clothing line and the Museo Lamborghini, and his daughter Patrizia, born when he was fifty-eight, runs the family winery in Umbria. His first wife, Clelia Monti, died in childbirth in nineteen forty-seven, and he met Annita Borgatti in nineteen forty-eight, who helped run his businesses for over thirty years.""",
   "Museo Lamborghini", "TONINO: CLOTHING AND MUSEO LAMBORGHINI · PATRIZIA: FAMILY WINERY IN UMBRIA")

ch("What the Countach became")
sc("""The Countach outlived his involvement by sixteen years. Wikipedia says it was produced from nineteen seventy-four to nineteen ninety, in six variants, and that one thousand, nine hundred eighty-three cars were built, including the prototype. Substantially more than half were built in the last five years. The car that was launched as he left sold best after the company had changed hands.""",
   "Lamborghini Countach production", "1974–1990 · 1,983 CARS (INCLUDING THE PROTOTYPE) · MORE THAN HALF IN THE LAST FIVE YEARS")
sc("""Wikipedia gives the breakdown: one hundred fifty-seven L P four hundreds, two hundred thirty-seven L P four hundred Ss, three hundred twenty-one L P five hundred Ss, six hundred ten Quattrovalvoles and six hundred fifty-seven twenty-fifth Anniversary cars. By our arithmetic, the final two variants account for one thousand, two hundred sixty-seven cars, about sixty-four percent of the total.""",
   "Lamborghini Countach 25th Anniversary", "LP400 157 · LP400 S 237 · LP500 S 321 · QV 610 · 25TH 657 (WIKIPEDIA)")
sc("""The American market mattered. The page says the United States was Lamborghini's largest market, though the Countach was not built to U S standards, so owners paid to modify cars in the grey-market era, from nineteen seventy-six to nineteen eighty-eight. The first U S-specification factory car arrived in nineteen eighty-five. A Countach also paced the Monaco Grand Prix from nineteen eighty to nineteen eighty-three.""",
   "Lamborghini Countach in America", "GREY MARKET 1976–88 · FIRST US-SPEC CAR 1985 · MONACO GP SAFETY CAR 1980–83")
sc("""Today, the early cars are valuable. RM Sotheby's sold Rod Stewart's L P four hundred Periscopio for eight hundred eighty-five thousand dollars in twenty twenty-six, and Hagerty shows one million dollars for a good nineteen seventy-five car. A Miura S V sold in Paris for three million, seven hundred seventeen thousand, five hundred euros. The company he sold in nineteen seventy-two was worth about one point two million dollars, by our arithmetic.""",
   "Lamborghini auction", "COUNTACH PERISCOPIO $885K · HAGERTY LP400 $1M · MIURA SV €3,717,500 · COMPANY IN 1972 ~$1.2M (IMPLIED)")

ch("The car the engineers built")
sc("""What kind of car did his engineers actually build? Wikipedia says the Countach chassis was a full space frame of welded round-section steel tubing. The chassis for both the prototype and the production L P four hundred was built by Marchesi, and the prototype body by Bertone. The five-speed gearbox had Porsche-type synchromesh. So the parts came from several suppliers, assembled by a small team.""",
   "Lamborghini Countach chassis", "SPACE FRAME OF WELDED STEEL TUBE · CHASSIS BY MARCHESI · BODY BY BERTONE · 5-SPEED WITH PORSCHE-TYPE SYNCHROMESH")
sc("""The engine was turned around from the Miura's. In contrast to the Miura's transverse engine, the page says, the Countach's was longitudinal, with the transmission between the two seats and a driveshaft that ran through the engine's oil sump to the rear differential. The page lists better weight distribution, a shorter wheelbase and easier maintenance access as the advantages of that layout.""",
   "Lamborghini Countach layout", "LONGITUDINAL ENGINE · GEARBOX BETWEEN THE SEATS · SHORTER WHEELBASE (WIKIPEDIA)")
sc("""The doors lifted up. Wikipedia says scissor doors first appeared on Marcello Gandini's nineteen sixty-eight Alfa Romeo Carabo concept, and that the Countach made them famous. Engineers studied a kick-out windscreen and explosive bolts for escaping a rollover, but neither was used. And because rear visibility was so poor, the prototype and the L P four hundred had a periscope supplied by Donnelly Mirrors.""",
   "Lamborghini Countach doors", "SCISSOR DOORS · PERISCOPE FROM DONNELLY MIRRORS · KICK-OUT WINDSCREEN STUDIED, NOT USED")
sc("""The prototype did not survive. The L P five hundred was crash-tested at the British test centre MIRA on the twenty-first of March, nineteen seventy-four, to win European type approval, and was destroyed. By our arithmetic, that was three years after its debut. At the same time, as far as the dates show, the man who had launched the project was selling his last shares in the company.""",
   "MIRA crash test", "LP500 CRASH-TESTED AND DESTROYED, MARCH 21, 1974")
sc("""The first production figures were modest. Wikipedia says one hundred fifty-seven L P four hundreds were built, and that fifty orders were placed at the nineteen seventy-four Geneva show. The RM Sotheby's catalogue for a Periscopio says about one hundred fifty first-series cars were built, according to the Countach Register. By our arithmetic, fifty orders at Geneva were about a third of the first series.""",
   "Geneva Motor Show 1974", "50 ORDERS AT GENEVA 1974 ≈ 1/3 OF ~150 PERISCOPIO CARS (OUR ARITHMETIC)")

ch("The people who kept building it")
sc("""After Ferruccio, the car carried on under others. Wikipedia lists a Swiss distributor, Max Bobnar, who commissioned two turbocharged Countachs between nineteen eighty and nineteen eighty-two. One was shown at Geneva in nineteen eighty-four with a claimed seven hundred fifty-nine metric horsepower in the text and seven hundred forty-six in the table. Those were not factory products, but they show the car's appeal to outside buyers.""",
   "Max Bobnar", "BOBNAR TURBO COUNTACHS 1980–82 · LP500 S TURBO AT GENEVA 1984 · 759 / 746 PS (WIKIPEDIA)")
sc("""In nineteen eighty-five the factory built the five thousand Quattrovalvole, with five thousand, one hundred sixty-seven cubic centimetres and four hundred fifty-five metric horsepower, and later the twenty-fifth Anniversary, which marked twenty-five years of the marque, restyled by Horacio Pagani. The page says it was possibly the fastest variant. None of these carried his hand. They were the work of the men and companies who came after him.""",
   "Horacio Pagani", "5000 QV (5.17 L, 455 PS) · 25TH ANNIVERSARY RESTYLED BY HORACIO PAGANI")
sc("""A few ideas never reached the road. Wikipedia lists the L one fifty, an update from nineteen eighty-four to nineteen eighty-seven that Patrick Mimran rejected for cost reasons, and the Q V X, a Group C racing car that was not built by the factory. In twenty twenty-one the Countach name returned on the L P I eight hundred dash four, a six point five litre V twelve with a forty-eight volt electric motor.""",
   "Lamborghini Countach LPI 800-4", "L150 REJECTED FOR COST · QVX GROUP C CAR · 2021 LPI 800-4: 6.5 L V12 + 48 V MOTOR")

ch("What the sources leave unsaid")
sc("""Now we should be honest about what we cannot tell you. The sources we found do not say what Ferruccio Lamborghini thought of the Countach, whether he saw it as a success, or why exactly he sold in nineteen seventy-four beyond calling him disillusioned. They do not give the price of the second sale. They do not say how the Rossetti and Leimer years went.""",
   "Ferruccio Lamborghini", "NOT IN OUR SOURCES: HIS VIEW OF THE COUNTACH · THE PRICE OF THE 1974 SALE")
sc("""They also differ on small things. The date of the tractor sale to SAME, nineteen seventy-two on the page we used and nineteen seventy-three in many retellings. The location of his winery, Umbria on the page and Tuscany elsewhere. The nature of his studies. And the origin of the Countach name. If a video tells you these things with total confidence, be sceptical, including of ours.""",
   "Ferruccio Lamborghini", "SAME SALE: 1972 VS 1973 · WINERY: UMBRIA VS TUSCANY · STUDIES · THE NAME")
sc("""One more point of caution. The Ferrari clutch story is recalled from an interview thirty years after the event, the page notes. By our arithmetic, nineteen ninety-one minus the early nineteen sixties is roughly thirty years. Memory changes, and a good story improves with each telling. That does not make it false. It means it is a memory, not a document.""",
   "Thoroughbred & Classic Cars interview", "A 1991 INTERVIEW RECALLING EVENTS ~30 YEARS EARLIER (OUR ARITHMETIC)")
sc("""And the larger legend has a similar structure. A man is dismissed, so he builds a better car, and then the car becomes an icon. It is neat. The sources suggest a messier reality: an industrialist with money, a team of engineers who built a prototype at night, a tractor firm hit by cancelled orders, and a car company he sold within eleven years. Both stories can be told. Only one fits all the documents.""",
   "Ferruccio Lamborghini", "THE NEAT STORY VS THE DOCUMENTED ONE (OUR READING)")

ch("The honest version")
sc("""So how did a tractor maker end up building the Countach? He earned a fortune with converted military vehicles and tractors. He bought fast cars. He founded a car company in nineteen sixty-three, perhaps because of an insult from Enzo Ferrari, perhaps because he saw a market. His engineers built the Miura in their spare time. And when it lost ground, he launched a successor.""",
   "Ferruccio Lamborghini", "TRACTORS → FAST CARS → A CAR COMPANY → THE MIURA → THE COUNTACH PROJECT")
sc("""Then trouble in the tractor business forced him to sell, first his tractors, then his shares in the car company. The Countach reached production in the year he left. He spent his last nineteen years making wine in Umbria. The record leaves much unsaid: his motives, his role in the design, his reaction to the finished car. We have tried not to fill those gaps with stories.""",
   "Ferruccio Lamborghini", "HE SOLD UP, THE COUNTACH REACHED PRODUCTION, HE MADE WINE (WIKIPEDIA)")
sc("""What would you have done in his place, kept the car company or sold? Tell us in the comments, and if you have a published source on the Countach name or on his role, share it. In the other videos of this series we reveal two things you may not know about the Countach, compare it with the Miura, and work out what a classic Lamborghini really costs. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video120", "How a Tractor Maker Ended Up Building the Countach", [
    "Wikipedia, Ferruccio Lamborghini: https://en.wikipedia.org/wiki/Ferruccio_Lamborghini",
    "Wikipedia, Lamborghini Countach: https://en.wikipedia.org/wiki/Lamborghini_Countach",
    "Wikipedia, Lamborghini Miura: https://en.wikipedia.org/wiki/Lamborghini_Miura",
    "RM Sotheby's, 1977 Lamborghini Countach LP400 Periscopio (Arizona 2026): https://rmsothebys.com/auctions/az26/lots/r0060-1977-lamborghini-countach-lp400-periscopio-by-bertone",
    "RM Sotheby's, 1971 Lamborghini Miura SV (Paris 2026, lot 150): https://rmsothebys.com/auctions/pa26/lots/r0090-1971-lamborghini-miura-sv",
    "Hagerty valuation tools, 1975 Lamborghini Countach LP400: https://hagerty.com/apps/valuationtools/1975-lamborghini-countach-lp400",
], "D")
