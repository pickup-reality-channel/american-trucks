import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Two Japanese supercars, both aimed at the same racetrack, the Nürburgring. One has a naturally aspirated V ten that screams to nine thousand r p m. The other has a twin-turbo V six and all-wheel drive. One was built in five hundred copies. The other in about forty-eight thousand. And at the Nürburgring, the cheaper car's best version was faster. This is the real difference between the Lexus LFA and the Nissan GT-R.""",
   "Lexus LFA and Nissan GT-R", "LEXUS LFA VS NISSAN GT-R")
sc("""Here is the twist. The LFA cost three hundred seventy-five thousand dollars new. The GT-R's launch price was around seventy thousand. By our arithmetic, the LFA cost more than five times as much. Yet according to Wikipedia, the GT-R Nismo's claimed Nürburgring lap beat the LFA's, and its engines were built by hand, one craftsman at a time. Let us go through the numbers, and where the sources disagree.""",
   "Japanese supercars", "THE CHEAPER CAR WAS FASTER")
sc("""Every figure comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Lexus LFA and Nissan GT-R", "EVERY NUMBER IS SOURCED")

ch("Two cars, two philosophies")
sc("""The Nissan GT-R in its R thirty-five form was unveiled at the Tokyo Motor Show in two thousand seven, according to Wikipedia. Deliveries began on the sixth of December two thousand seven in Japan, on the seventh of July two thousand eight in North America, and in March two thousand nine in Europe. It was built at the Tochigi plant.""",
   "Nissan GT-R", "GT-R: TOKYO 2007 · DELIVERIES FROM DEC 2007")
sc("""The Lexus LFA was unveiled at the Tokyo Motor Show two years later, on the twenty-first of October two thousand nine, and production began on the fifteenth of December two thousand ten. Wikipedia says five hundred were built until December two thousand twelve. The GT-R, by contrast, ran until the twenty-sixth of August two thousand twenty-five, when the final unit left the Tochigi plant.""",
   "Lexus LFA", "LFA: 500 BUILT · GT-R: ~48,000 OVER 18 YEARS")
sc("""By our own arithmetic, the GT-R was made for about eighteen years and the LFA for two. Production of about forty-eight thousand against five hundred makes the GT-R ninety-six times more numerous. One was a car for the many who could afford a sports car. The other was a car for the few who could afford a showpiece.""",
   "Nissan GT-R and Lexus LFA", "GT-R ≈ 96× MORE NUMEROUS (OUR ARITHMETIC)")
sc("""The GT-R's chief engineer was Kazutoshi Mizuno, known as Mr. GT-R, who had also been chief engineer of the R thirty-four. Wikipedia says he initially rejected the project on the F M platform, then built a prototype on the P M platform in two thousand three. His targets included a three hundred kilometre per hour cabin where conversation was possible and a Nürburgring lap under eight minutes.""",
   "Kazutoshi Mizuno", "MR. GT-R: TARGET — NÜRBURGRING UNDER 8 MINUTES")

ch("Round one: the engines")
sc("""The LFA's engine is a four point eight litre V ten, co-developed with Yamaha, with four hundred twelve kilowatts, five hundred sixty metric horsepower at eight thousand seven hundred r p m, and four hundred eighty newton-metres at six thousand eight hundred. The redline is nine thousand r p m. It is naturally aspirated, as Wikipedia describes it.""",
   "Lexus LFA V10", "LFA: 4.8 L V10 · 560 PS · 480 NM · 9,000 RPM")
sc("""The GT-R's engine is the V R thirty-eight D E T T, a three point eight litre, sixty-degree, twin-turbocharged V six. Wikipedia lists the original rating as four hundred seventy-three horsepower at six thousand four hundred r p m and five hundred eighty-three newton-metres. The torque comes from three thousand two hundred to five thousand two hundred r p m, a broad plateau.""",
   "Nissan GT-R VR38DETT", "GT-R: 3.8 L TWIN-TURBO V6 · 473 HP · 583 NM")
sc("""The GT-R's power grew over the years. Two thousand nine: four hundred eighty-five metric horsepower and five hundred eighty-eight newton-metres. Two thousand twelve: five hundred fifty metric horsepower and six hundred twenty-eight. Twenty seventeen: five hundred seventy metric horsepower and six hundred thirty-three. The Nismo version, from two thousand thirteen, has six hundred metric horsepower and six hundred fifty-two newton-metres.""",
   "Nissan GT-R engine", "GT-R POWER: 485 → 550 → 570 PS · NISMO 600 PS")
sc("""Compare the mature figures. A twenty seventeen GT-R at five hundred seventy metric horsepower makes about two percent more than the LFA's five hundred sixty, by our arithmetic. And its torque, six hundred thirty-three newton-metres, is about thirty-two percent more than the LFA's four hundred eighty. The torque comes from turbochargers. The LFA's character comes from revs.""",
   "Engine comparison", "GT-R 2017: +2% POWER · +32% TORQUE (OUR ARITHMETIC)")
sc("""Per litre, the figures flip. The LFA makes about one hundred seventeen metric horsepower per litre. The twenty seventeen GT-R makes about one hundred fifty, by our arithmetic. Turbochargers let a smaller engine produce more. The LFA chose displacement and revs. The GT-R chose boost. Nobody says one is better. They are different answers to the same question.""",
   "Turbocharged engine", "LFA 117 PS/L · GT-R 150 PS/L (OUR ARITHMETIC)")
sc("""There is a cost to the LFA's approach. Its torque peaks high, and its power peaks only three hundred r p m below the redline. The GT-R's strong torque from three thousand two hundred r p m means that it pulls from lower revs. On paper, the GT-R is easier to drive quickly. The LFA is more demanding, and by all accounts, more theatrical.""",
   "Engine rev counter", "THE LFA WANTS REVS · THE GT-R PULLS FROM 3,200 RPM")

ch("Round two: the engine builders")
sc("""Both engines were built with unusual care. Wikipedia says GT-R engines were hand-built by nine Takumi craftsmen over the production run. Each engine took about six hours and three hundred components, and the builder's name was badged on the engine. About thirteen engines were built per day in a single shift.""",
   "Nissan Takumi engine builder", "GT-R ENGINES: HAND-BUILT · 6 HOURS EACH · BUILDER'S NAME")
sc("""By our arithmetic, thirteen engines a day at six hours each is seventy-eight hours of work per day, spread among the craftsmen. For the LFA, Wikipedia gives production of twenty cars a month. So the GT-R plant built about thirteen engines in a day, and the LFA plant built twenty complete cars in a month. The difference of scale is enormous.""",
   "Engine assembly", "13 ENGINES A DAY VS 20 CARS A MONTH (OUR ARITHMETIC)")
sc("""Both firms treated the engine as the product. Lexus co-developed its V ten with Yamaha and had it tuned for sound, with two octaves channelled into the cabin. Nissan put a name on each GT-R engine. In different ways, each company tried to make buyers feel that a person, not only a machine, had built the car.""",
   "Engine plate", "TWO WAYS TO MAKE A MACHINE FEEL HUMAN (OUR READING)")

ch("Round three: weight and speed")
sc("""Weight. The LFA is listed by Wikipedia at either one thousand, five hundred eighty or one thousand, four hundred eighty kilograms, depending on the table. The GT-R was one thousand, seven hundred forty kilograms in two thousand seven to two thousand nine, rising to one thousand, seven hundred eighty-five kilograms from two thousand sixteen. The Nismo was one thousand, seven hundred fifty after the two thousand nineteen update.""",
   "Nissan GT-R weight", "LFA 1,480–1,580 KG · GT-R 1,740–1,785 KG")
sc("""By our arithmetic, the GT-R weighs between about two hundred and three hundred kilograms more than the LFA, using the lower LFA figure. That is the cost of all-wheel drive and a heavier steel body, compared with the LFA's carbon structure. The page does not state those reasons, so they are our reading. But the carbon body was a defining feature of the LFA.""",
   "Lexus LFA carbon fibre", "GT-R ~160–300 KG HEAVIER (OUR ARITHMETIC)")
sc("""Acceleration. The LFA's official zero to sixty miles per hour is three point six seconds, without launch control, according to Wikipedia. The GT-R page lists zero to ninety-seven kilometres per hour at three point two seconds for the first cars, and two point seven seconds for the two thousand twelve to two thousand sixteen cars. That includes a note that one figure comes from an unreliable source.""",
   "Nissan GT-R launch", "0–97 KM/H: LFA 3.6 S · GT-R 3.2 S → 2.7 S")
sc("""By our arithmetic, the later GT-R is quicker to sixty by about twenty-five percent. By our reading, all-wheel drive and launch control give it traction that the LFA's layout cannot match from a standstill. We note that the two pages list different test conditions, so the comparison is indicative, not exact. But the direction is clear.""",
   "Nissan GT-R", "2012–2016 GT-R ~25% QUICKER TO 60 (OUR ARITHMETIC)")
sc("""Top speed is where the LFA is competitive. Wikipedia lists three hundred twenty-five or three hundred twenty-six kilometres per hour for the LFA. The GT-R page we used does not give a top speed, so we cannot compare. We can say that the LFA's roughly three hundred twenty-five is a high number for a car of that period.""",
   "Lexus LFA", "LFA TOP SPEED ~325 KM/H · GT-R: NOT LISTED IN OUR SOURCE")

ch("Round four: the Nürburgring")
sc("""Both cars were built with this track in mind. Wikipedia lists the LFA's Nürburgring Package time of seven minutes, fourteen point six four seconds, confirmed in September two thousand eleven. An earlier test lap, in June two thousand eleven, was seven twenty-two point eight five. The package has five hundred seventy-one metric horsepower, and sixty-four were built.""",
   "Lexus LFA Nürburgring", "LFA N-PACKAGE: 7:14.64 (SEPT 2011)")
sc("""The GT-R's lap times improved steadily. Seven thirty-eight point five four in September two thousand seven, in damp conditions. Seven thirty-two in April two thousand eight. Seven twenty-nine point zero three in May two thousand nine. Seven twenty-six point seven in the two thousand ten model year. Seven twenty-four point two two in September two thousand ten, damp, on the facelifted car.""",
   "Nissan GT-R Nürburgring", "GT-R: 7:38.54 (2007) → 7:24.22 (2010)")
sc("""Then the later cars. Nissan claimed seven eighteen point six for the two thousand thirteen model year, with seven nineteen point one measured in October two thousand twelve. And the Nismo, driven by Michael Krumm in two thousand thirteen, did seven oh eight point six seven nine, which Nissan claimed as the mass-production record. These are manufacturer claims, as the page makes clear.""",
   "Nissan GT-R Nismo", "GT-R NISMO 2013: 7:08.679 (NISSAN'S CLAIM)")
sc("""By our own arithmetic, the standard two thousand thirteen GT-R, at seven eighteen point six, was about four seconds slower than the LFA's seven fourteen point six four. But the Nismo, at seven oh eight point six seven nine, was about six seconds faster. A road-going GT-R beat the LFA's package time, and the GT-R was a car priced in the low hundred thousands.""",
   "Nürburgring Nordschleife", "BASE GT-R 4 S SLOWER · NISMO 6 S FASTER (OUR ARITHMETIC)")
sc("""A caution about lap times. They depend on weather, tyres, driver, and the date the lap was set. The pages show some laps run in damp conditions and some claimed by manufacturers. So we do not say which car is faster in general. We say what the sources list, and that the GT-R, with its two thousand thirteen Nismo, held the record Nissan claimed.""",
   "Racing circuit", "LAP TIMES: WEATHER, TYRES, DRIVER, DATE")

ch("Round four and a half: power to weight")
sc("""Power to weight shows how the two cars reach their speed. Wikipedia lists the LFA at two point six seven kilograms per horsepower. For the GT-R, Mizuno's target was under four kilograms per horsepower. By our own arithmetic, the twenty seventeen car, at one thousand, seven hundred eighty-five kilograms and five hundred sixty-two horsepower, comes to about three point one eight.""",
   "Power to weight", "LFA 2.67 KG/HP · GT-R 2017 ≈ 3.18 KG/HP (OUR ARITHMETIC)")
sc("""So the GT-R beat its own target of four kilograms per horsepower by a wide margin, but remained about nineteen percent heavier per unit of power than the LFA. The LFA wins on that measure. And yet, as the lap times show, the GT-R's drive system and engine torque make up the difference on a circuit. Numbers on a spec sheet are only part of a story.""",
   "Nissan GT-R", "GT-R ~19% HEAVIER PER HP — YET QUICK ON A LAP (OUR ARITHMETIC)")
sc("""Mizuno's other target was a cabin where conversation remained possible at three hundred kilometres per hour. The LFA's design was the opposite: Wikipedia says two octaves of engine sound are channelled into the cabin on purpose. One car was made to be calm at speed, the other to be thrilling. That difference of intention is perhaps the clearest contrast of all.""",
   "Lexus LFA and Nissan GT-R cabins", "GT-R: A CALM CABIN AT 300 · LFA: SOUND CHANNELLED IN")

ch("Racing and heritage")
sc("""The LFA also raced. Wikipedia says the number fifteen car in the two thousand nine Nürburgring twenty-four hours finished with a driveshaft failure and a fire. In twenty ten, the number fifty car won its class, S P eight, finishing eighteenth overall after one hundred forty-two laps. It was a showpiece with a competition record.""",
   "Nürburgring 24 Hours", "LFA 2010: CLASS WIN AT THE NÜRBURGRING 24H")
sc("""The GT-R, by the page, descends from a line that includes the R thirty-four, whose chief engineer was the same Mizuno. The name is known worldwide, and the R thirty-five carried it for eighteen years. Nissan ended North American sales in October two thousand twenty-four, according to Wikipedia, and the last car left the Tochigi plant in August two thousand twenty-five.""",
   "Nissan GT-R production end", "NORTH AMERICAN SALES ENDED OCT 2024 · LAST CAR AUG 2025")
sc("""By our arithmetic, the North American sales ended about ten months before the last car was built. One possible reading is that cars for other markets were still being built, though the page does not say so. The LFA's final car, in contrast, was sold in June two thousand twenty-three, more than ten years after the end of its production, an Australian dealer's display car.""",
   "Nissan GT-R final car", "GT-R: SALES END PRECEDE LAST CAR · LFA: LAST SALE 10+ YEARS LATE")

ch("Two details that define each car")
sc("""For the LFA, one detail defines it. Wikipedia says the engine revs from idle to redline in point six seconds, which required a digital tachometer. A mechanical needle could not keep up. It is the kind of fact that only appears when engineers build around an engine rather than fit an engine into a design.""",
   "Lexus LFA digital tachometer", "LFA: IDLE TO REDLINE IN 0.6 S · DIGITAL TACHOMETER")
sc("""For the GT-R, the defining detail is the person. Each engine carries a badge with the builder's name. Wikipedia says nine Takumi craftsmen built the engines over the production run, and each engine took about six hours and three hundred components. A mass-produced car with a signed engine is an unusual idea, and Nissan made it central to the car's identity.""",
   "Nissan GT-R engine badge", "GT-R: A BADGE WITH THE BUILDER'S NAME")
sc("""And for materials, the contrast is stark. The LFA's body is sixty-five percent carbon fibre reinforced plastic by mass, woven on a laser-monitored loom, according to Wikipedia. The manufacturer says the carbon saves a hundred kilograms compared with aluminium. The GT-R's weight figures are far higher, which is consistent with a steel and aluminium body, though the page we used does not say so.""",
   "Lexus LFA carbon fibre", "LFA: 65% CARBON FIBRE · GT-R WEIGHS 160–300 KG MORE")
sc("""Price per horsepower is the last sum, all our arithmetic. The LFA at three hundred seventy-five thousand dollars and five hundred fifty-three horsepower is about six hundred seventy-eight dollars per horsepower. The twenty seventeen GT-R at about seventy thousand to one hundred twenty thousand dollars and five hundred sixty-two horsepower is roughly one hundred twenty-five to two hundred thirteen. The LFA costs three to five times more per horsepower.""",
   "Price per horsepower", "LFA ~$678/HP · GT-R ~$125–$213/HP (OUR ARITHMETIC)")

ch("What a buyer got")
sc("""Imagine two buyers in two thousand eleven. One spent three hundred seventy-five thousand dollars on an LFA, and Wikipedia says that in North America many cars were first sold through a two-year lease, one hundred fifty in all. The other spent less than one hundred thousand dollars on a GT-R. Each got a car that could lap the Nürburgring in about seven and a half minutes or less.""",
   "Two buyers", "$375K LFA vs < $100K GT-R · SIMILAR LAP TIMES")
sc("""That makes the LFA the more extreme purchase and the GT-R the more rational one. Rational is not a criticism. The GT-R's price rose from about seventy thousand to one hundred twenty-three thousand over fifteen years, according to Car and Driver, and it still cost less than a third of the LFA's original price. By our arithmetic, one hundred twenty-three over three seventy-five is about thirty-three percent.""",
   "Nissan GT-R", "2024 GT-R PREMIUM ≈ 33% OF LFA'S ORIGINAL PRICE")
sc("""There is something else a buyer got with the LFA. A car that, by the numbers in our other video, would later sell for more than double its original price. Nobody could know that in two thousand eleven. We mention it because it is the most striking difference in how the two cars have aged, and because it says nothing about which one is the better car.""",
   "Lexus LFA", "THE LFA AGED INTO A COLLECTIBLE · NO ONE KNEW IN 2011")
sc("""And for a sense of scale, remember that the GT-R was ninety-six times more numerous. If you wanted to see one, you could. If you wanted to see an LFA, you needed luck. In that sense the two cars represent two ways of earning respect: by being everywhere, and by being almost nowhere. Both worked, in different ways.""",
   "Nissan GT-R and Lexus LFA", "EVERYWHERE VS ALMOST NOWHERE (OUR READING)")

ch("Round five: price")
sc("""Price is where the two cars could not be further apart. Wikipedia lists the LFA's base price at three hundred seventy-five thousand dollars. For the GT-R, Jalopnik reported a launch price of sixty-nine thousand, eight hundred fifty dollars for the two thousand nine model, on sale on the seventh of July two thousand eight. Car and Driver gives seventy thousand, eight hundred fifty. The sources disagree by a thousand dollars.""",
   "Nissan GT-R price", "GT-R 2009: $69,850 (JALOPNIK) VS $70,850 (CAR AND DRIVER)")
sc("""By our arithmetic, three hundred seventy-five thousand divided by seventy thousand is about five point four. The LFA cost more than five times as much as the GT-R. Car and Driver says the two thousand twenty-four GT-R Premium cost one hundred twenty-two thousand, eight hundred eighty-five dollars, the T-spec one hundred forty-two thousand, eight hundred eighty-five, and the Nismo two hundred twenty-two thousand, eight hundred eighty-five.""",
   "Nissan GT-R 2024", "2024 GT-R: $122,885 · T-SPEC $142,885 · NISMO $222,885")
sc("""Even the most expensive two thousand twenty-four GT-R, the Nismo at about two hundred twenty-three thousand, cost about sixty percent of the LFA's original price, by our arithmetic. Car and Driver also notes the original two thousand nine GT-R, adjusted for inflation, would be about one hundred one thousand, eight hundred twenty-five. So the GT-R's price rose well beyond inflation.""",
   "Nissan GT-R Nismo", "2024 NISMO ≈ 60% OF LFA STICKER (OUR ARITHMETIC)")
sc("""The Nismo Special Edition, Wikipedia says, was limited to three hundred units worldwide. The page also mentions the N-Attack Package used for the record lap, with engine control, suspension and aero upgrades. So even the GT-R had rare versions. But none was as rare as the LFA, with its total of five hundred cars of any kind.""",
   "Nissan GT-R Nismo Special Edition", "NISMO SPECIAL EDITION: 300 WORLDWIDE")

ch("Round six: what they are worth now")
sc("""Used values tell a story. Motor Authority reported in July two thousand twenty-one that a two thousand twelve Lexus LFA with seventy-two miles sold for eight hundred eight thousand dollars on Bring a Trailer. Supercar Blondie reported eight hundred forty-five thousand for another in April two thousand twenty-two. These are single sales, not a market index, as we say in another video of this series.""",
   "Lexus LFA auction", "LFA AUCTIONS: $808,000 (2021) · $845,000 (2022)")
sc("""For the GT-R, the sources we used give new prices but not used prices, so we do not compare them. What we can say is that the LFA sold at more than double its original price, by our arithmetic, a markup of about one hundred fifteen to one hundred twenty-five percent. The GT-R, produced in vastly greater numbers, is not in the same position.""",
   "Lexus LFA", "LFA SOLD AT 2.15–2.25× STICKER (OUR ARITHMETIC)")

ch("The verdict")
sc("""So how do they compare? On sound and character, the LFA, by every description in the sources. On torque, the GT-R, by about thirty percent. On acceleration to sixty, the later GT-R. On the Nürburgring, the LFA's package against the base GT-R, a close contest, with the Nismo ahead. On price, the GT-R, by a factor of five. On rarity, the LFA by a factor of ninety-six.""",
   "Lexus LFA and Nissan GT-R", "SCORECARD")
sc("""The real difference is the idea. Lexus built a showpiece for its twentieth anniversary, with a naturally aspirated V ten, a loom-woven carbon body and a digital tachometer. Nissan built a performance car for many buyers, with a twin-turbo V six, all-wheel drive and hand-built engines. Both reached the Nürburgring, and both succeeded in their own terms.""",
   "Lexus LFA and Nissan GT-R", "A SHOWPIECE VS A PERFORMANCE CAR FOR MANY (OUR READING)")
sc("""One caution. We have not driven either car. Every figure comes from published sources, some of which disagree, and some comparisons are our own arithmetic. We do not claim which is better to drive. The Wikipedia pages even disagree with themselves, on the LFA's weight and the GT-R's early acceleration. We have told you where.""",
   "Lexus LFA and Nissan GT-R", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you choose, the LFA or the GT-R? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the LFA, explain why it is worth more now than new, and tell the story behind it. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video106", "Lexus LFA vs Nissan GT-R: The Difference Nobody Explains", [
    "Wikipedia, Lexus LFA: https://en.wikipedia.org/wiki/Lexus_LFA",
    "Wikipedia, Nissan GT-R: https://en.wikipedia.org/wiki/Nissan_GT-R",
    "Car and Driver (via Yahoo Autos), 2024 Nissan GT-R costs $122,885 (16 May 2023): https://autos.yahoo.com/2024-nissan-gt-r-costs-161200041.html",
    "Jalopnik, 2009 Nissan GT-R priced at $69,850, on sale July 7: https://jalopnik.com/2009-nissan-gt-r-priced-at-69-850-on-sale-july-7-397345",
    "Motor Authority, Pearl Yellow 2012 Lexus LFA with 72 miles sells for $808,000 on Bring a Trailer (7 July 2021): https://www.motorauthority.com/news/1132702_pearl-yellow-2012-lexus-lfa-with-72-miles-sells-for-808-000-on-bring-a-trailer",
    "Supercar Blondie, Super rare Lexus LFA sells for massive $845k at auction (25 April 2022): https://supercarblondie.com/cars/lexus-lfa-850-miles-sells-845k/",
], "B")
