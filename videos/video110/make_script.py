import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""One car is a graceful British roadster with a six-cylinder engine and a top speed of about a hundred sixteen miles per hour. The other is the same body with a Ford V eight and a top speed of a hundred sixty-four. One was sold in the hundreds. The other is among the most famous American cars ever made. This is the real difference between the Shelby Cobra and the A C Ace.""",
   "Shelby Cobra and AC Ace", "SHELBY COBRA VS AC ACE")
sc("""Here is the twist. The Cobra is an Ace. The chassis, the body and the factory are the same, and the Cobra's low nose was developed for an Ace. Yet in the sales we can find, the two cars sell in completely different price bands, by a factor of about ten. Let us go through the numbers, and the places where the sources disagree.""",
   "AC Ace", "THE COBRA IS AN ACE · A 10× PRICE GAP")
sc("""Every figure comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Shelby Cobra", "EVERY NUMBER IS SOURCED")

ch("The same car, twice")
sc("""Wikipedia says the A C Ace was designed by John Tojeiro and built by A C Cars at Thames Ditton, England. It was launched in nineteen fifty-three and produced until nineteen sixty-three, though other sources list the range as running to nineteen sixty-four. The Aceca hardtop coupé followed in nineteen fifty-four. It was a light, open two-seater with a steel ladder chassis.""",
   "AC Ace", "ACE: LAUNCHED 1953 · BUILT BY AC CARS, THAMES DITTON")
sc("""The Cobra page describes the chassis as a steel ladder with three-inch main rails. The Ace page gives engines in three groups. The A C two litre six, with eighty-five to a hundred two brake horsepower. The Bristol two litre six, from nineteen fifty-six, with a hundred five to a hundred twenty-eight. And the Ford Zephyr two point six, from nineteen sixty-one, with ninety to a hundred seventy depending on tune.""",
   "AC Ace chassis", "ACE ENGINES: AC 2.0 · BRISTOL 2.0 · ZEPHYR 2.6")
sc("""In nineteen sixty-one, the Ace page says, Carroll Shelby proposed fitting a Ford V eight to the Ace chassis. A C built a prototype, chassis C S X two thousand. Shelby's team installed the engine in the United States. The page considers it the first A C Cobra. And Ace production ended a year after the Cobra debuted, which tells you how quickly the new car took over.""",
   "Shelby Cobra prototype", "1961: SHELBY PROPOSES A FORD V8 FOR THE ACE")
sc("""So the two cars share a lot. Wikipedia's Cobra page says the Ace was built since nineteen fifty-three with a steel ladder chassis, and the Cobra was made on that foundation. The Cobra page also notes that the prototype was an Ace three point six. For the first cars, then, the difference was mainly in the engine bay.""",
   "AC Ace and Shelby Cobra", "FIRST COBRAS = ACE CHASSIS + FORD V8")

ch("Round one: engines and power")
sc("""Take the Ace's best engine, the Ruddspeed Zephyr. Wikipedia lists ninety to a hundred seventy brake horsepower, depending on tune. Only thirty-seven were made. The Bristol six had a hundred five to a hundred twenty-eight. The standard A C six had eighty-five to a hundred two. These are modest numbers by the standards of the Cobra that replaced the Ace.""",
   "AC Ace engine", "ACE: 85–170 BHP DEPENDING ON ENGINE")
sc("""The Cobra's first engine was the two hundred sixty cubic inch Ford V eight, which Wikipedia says is four point three litres. The next was the two hundred eighty-nine, four point seven litres. Then the four hundred twenty-seven, seven litres, rated at four hundred twenty-five horsepower, and four hundred eighty-five in S slash C tune. Du Pont Registry lists three hundred sixty for its spec list, a discrepancy.""",
   "Shelby Cobra 427 engine", "COBRA: 4.3 L → 4.7 L → 7.0 L")
sc("""By our own arithmetic, the Cobra's four hundred twenty-five horsepower is more than three times the Ace Bristol's top figure of a hundred twenty-eight, about three point three times. Against the best Ruddspeed Ace, at a hundred seventy, it is two and a half times. Even the lowest Cobra rating, three hundred sixty, is more than double the strongest Ace.""",
   "Engine comparison", "427 COBRA: 2.5× THE BEST ACE · 3.3× THE ACE BRISTOL (OUR ARITHMETIC)")
sc("""And the S slash C. Four hundred eighty-five horsepower is nearly four times the Bristol's figure, by our arithmetic. The same chassis family, the same company, a decade apart in the way the numbers read. That jump explains much of why the Cobra became famous and the Ace became a collector's classic.""",
   "Shelby Cobra 427 S/C", "S/C 485 HP ≈ 3.8× THE ACE BRISTOL (OUR ARITHMETIC)")

sc("""Here is a surprising piece of arithmetic, all ours. Per litre, the engines are closer than you would think. The Bristol two litre at a hundred twenty-eight horsepower makes about sixty-four horsepower per litre. The Ruddspeed two point six at a hundred seventy makes about sixty-five. The four hundred twenty-seven at four hundred twenty-five horsepower makes about sixty-one. The S slash C, at four eighty-five, makes about sixty-nine.""",
   "Engine output per litre", "PER LITRE: ACE 64–65 HP/L · COBRA 61–69 HP/L (OUR ARITHMETIC)")
sc("""So the Cobra was not made faster by a cleverer engine. It was made faster by a bigger one. The seven litre V eight has three and a half times the displacement of the Ace's two litre six, by our arithmetic. Output per litre is about the same. Cubic inches, as American hot rodders say, are the cheapest way to make power, and the Cobra proves it.""",
   "Shelby Cobra 427 engine", "7.0 L VS 2.0 L = 3.5× THE DISPLACEMENT (OUR ARITHMETIC)")
sc("""The same logic applies to the first Cobra, the two hundred sixty. At four point three litres, it has just over twice the displacement of the Bristol's two. Wikipedia lists the prototype engine as four point three litres, and another reference on the page as four point two. Road and Track's four point two second sprint to sixty came from an engine barely twice the Ace's size, in a car of similar weight.""",
   "Shelby Cobra 260", "FIRST COBRA: ~2.1× THE ACE'S DISPLACEMENT · 2.7× THE ACCELERATION")

ch("Round two: weight")
sc("""Weight is where the Ace page disagrees with itself. Its infobox gives a kerb weight of one thousand, nine hundred twenty pounds, eight hundred seventy-one kilograms. Its specification table gives seven hundred sixty-two to seven hundred eighty kilograms for the standard Ace, and seven hundred sixty-two to eight hundred ninety-four for the Bristol. These figures conflict, so we use the range.""",
   "AC Ace weight", "ACE WEIGHT: 762–894 KG (SOURCE CONFLICTS WITH ITSELF)")
sc("""The four hundred twenty-seven Cobra, per Du Pont Registry, weighs two thousand, three hundred fifty-five pounds, about one thousand, sixty-eight kilograms. By our arithmetic, that is about a hundred seventy-five to three hundred five kilograms more than the Ace, or roughly a fifth to two fifths heavier. The Cobra gained power much faster than it gained weight.""",
   "Shelby Cobra weight", "COBRA 427 ≈ 1,068 KG · 19–40% HEAVIER THAN AN ACE (OUR ARITHMETIC)")
sc("""Put them together as power to weight. A Bristol Ace at about a hundred twenty horsepower and an assumed eight hundred kilograms is roughly point one five horsepower per kilogram. The four hundred twenty-five horsepower Cobra at one thousand, sixty-eight kilograms is about point four. The Cobra has about two and a half times the power for its weight. The eight hundred kilogram figure is our own midpoint.""",
   "Power to weight", "ACE ~0.15 HP/KG · COBRA ~0.40 HP/KG (OUR ARITHMETIC, ASSUMED MIDPOINT)")

ch("Round three: speed")
sc("""Wikipedia lists the Ace's performance by engine. The A C six: about a hundred three miles per hour in a nineteen fifty-four Motor test, with zero to sixty in eleven point four seconds. The Bristol six: about a hundred sixteen, with zero to sixty in the nine-second range. The tuned Ruddspeed: about a hundred thirty, zero to sixty in eight point one seconds.""",
   "AC Ace road test", "ACE: 103 / 116 / 130 MPH · 0–60: 11.4 / ~9 / 8.1 S")
sc("""For the Cobra, EVO reports that Road and Track timed the very first car, with the two hundred sixty engine, at four point two seconds to sixty and a hundred fifty-three miles per hour in nineteen sixty-two. Wikipedia lists a hundred sixty-four for the standard four hundred twenty-seven, and a hundred eighty-five for the S slash C. Du Pont Registry lists zero to sixty in three point four.""",
   "Shelby Cobra road test", "COBRA 260: 4.2 S, 153 MPH · 427: 164 MPH · S/C: 185 MPH")
sc("""By our arithmetic, the very first Cobra, with the smallest engine, was already more than twice as quick to sixty as the plain Ace, four point two seconds against eleven point four, and about twice as quick as the Bristol, which took around nine. At the top end it was a hundred fifty-three against a hundred sixteen, thirty-two percent faster.""",
   "Shelby Cobra and AC Ace", "FIRST COBRA: 4.2 S VS 11.4 S (ACE) AND ~9 S (BRISTOL)")
sc("""And the 427 S slash C, at a hundred eighty-five miles per hour, is about fifty-nine percent faster than the Bristol Ace's top speed of a hundred sixteen, by our arithmetic. Add the fact that the Cobra weighs a fifth to two fifths more. Whatever the exact figures, the pattern is the same. The engine transformed the car.""",
   "Shelby Cobra 427 S/C", "S/C TOP SPEED ≈ +59% OVER THE ACE BRISTOL (OUR ARITHMETIC)")

ch("Round four: production")
sc("""The Ace was made in small numbers. Wikipedia says about two hundred twenty A C-engined Aces and four hundred sixty-six Ace Bristols were built, plus thirty-seven of the Ruddspeed cars. By our arithmetic, two hundred twenty plus four hundred sixty-six plus thirty-seven is seven hundred twenty-three, though the page does not state a combined total, so treat it as an estimate.""",
   "AC Ace production", "~220 AC-ENGINED · 466 BRISTOL · 37 RUDDSPEED")
sc("""For the Cobra, Du Pont Registry says Shelby American built nine hundred ninety-eight Cobras, with six hundred fifty-five small-block leaf-spring cars delivered. Wikipedia lists a hundred twenty-six Mark One cars, about five hundred twenty-eight Mark Two cars, and fifty-six four hundred twenty-sevens. The sources do not add up neatly, as the Wikipedia page itself admits.""",
   "Shelby Cobra production", "COBRA: 998 BUILT (DU PONT) · 126 + ~528 + 56 (WIKIPEDIA)")
sc("""By our arithmetic, Wikipedia's three figures sum to seven hundred ten, which is quite far from Du Pont's nine hundred ninety-eight. We do not know whether the difference is in the counting or in what is counted. What we can say is that both cars were built in the hundreds, not thousands, and that Shelby's output was not many times the Ace's.""",
   "Cobra and Ace production", "126 + 528 + 56 = 710 VS 998: THE SOURCES DON'T AGREE")

ch("Round four and a half: how the car changed underneath")
sc("""Look under the skin. Wikipedia says the Ace and early Cobra shared a steel ladder chassis with three-inch main rails and leaf springs. The big change came with the Mark Three, whose chassis used four-inch tubes and coil springs all round, designed with Ford in Detroit. In other words, the Cobra needed a new foundation once the engine reached seven litres.""",
   "Shelby Cobra chassis", "ACE/EARLY COBRA: 3-INCH LADDER · MK III: 4-INCH TUBES, COIL SPRINGS")
sc("""The Mark Two, redesigned by Alan Turner, brought rack-and-pinion steering. The rack came from the M G B and the column from the Volkswagen Beetle, Wikipedia says. By our reading, that is the Cobra's character in one detail: world-class engine, borrowed parts, built fast. About five hundred twenty-eight were built from nineteen sixty-three to the summer of nineteen sixty-five.""",
   "Shelby Cobra Mk II", "MK II STEERING: MGB RACK + VW BEETLE COLUMN")
sc("""The body changed as well. EVO notes that the prototype kept its early A C shell, and that later Cobras had wider bodywork to fit larger tyres. The Ace page adds that the Cobra's lower bonnet and smaller grille were developed for the Ace two point six, though Shelby is often credited with them. So the Cobra's shape is more Ace than legend admits.""",
   "AC Ace and Shelby Cobra bodies", "WIDER BODYWORK FOR BIGGER TYRES · NOSE FROM THE ACE 2.6")
sc("""Costs mattered too. The Cobra page says the inboard brakes moved outboard to cut cost, and the fuel filler moved from the fender to the boot. Shelby's cars were sold at a price, and the changes show a product being engineered for production. The Ace had been a hand-built British sports car. The Cobra became a hybrid of British hand-building and American practicality.""",
   "Shelby Cobra brakes", "COST CUTS: OUTBOARD BRAKES, BOOT FUEL FILLER")

ch("What happened to the two cars")
sc("""The Ace page says production ended in nineteen sixty-three, a year after the Cobra debuted. A C itself continued with Cobras. Wikipedia says A C built the coil-spring roadster with a two hundred eighty-nine until late nineteen sixty-nine, and the A C four twenty-eight Frua, built on a stretched four twenty-seven chassis, until nineteen seventy-three.""",
   "AC Cars", "ACE ENDED 1963 · AC COBRA ROADSTER UNTIL 1969 · 428 FRUA UNTIL 1973")
sc("""For Shelby, the Cobra story ended sooner. Wikipedia says Ford and Shelby ended imports from England in nineteen sixty-seven and calls the Cobra a financial failure. So the car that gave the American muscle era its icon was not a profitable product. The sources do not give the loss, so we will not guess one. The page says only that it failed financially.""",
   "Shelby American", "1967: FORD AND SHELBY END IMPORTS · \"A FINANCIAL FAILURE\"")
sc("""In nineteen eighty-six, the page says, Autokraft bought A C and built the Mark Four with a four point nine five litre, three hundred two cubic inch V eight. Ford joined as a partner in nineteen eighty-seven. The Mark Four had two hundred fifty horsepower and weighed two thousand, six hundred twenty pounds. So the A C name had its second life on the Cobra, not on the Ace.""",
   "AC Cobra Mk IV", "1986: AUTOKRAFT BUYS AC · MK IV FROM 1987")

ch("Two markets, a decade apart")
sc("""A sum on the Ace Bristol sales. A nineteen fifty-nine car sold for a hundred sixteen thousand, five hundred sixty-two dollars in December two thousand three, and a nineteen fifty-six car for two hundred twenty-three thousand, one hundred twenty-four in September twenty eleven. By our arithmetic, the later price is about ninety-one percent higher. Hagerty's note on the first sale says the price was distorted by the weak dollar.""",
   "AC Ace Bristol", "ACE BRISTOL: +91% BETWEEN TWO DIFFERENT CARS, 2003 → 2011 (OUR ARITHMETIC)")
sc("""A caution: those are two different cars in different conditions, so we cannot call it a trend. The same applies to the Cobra. A nineteen sixty-five four hundred twenty-seven S slash C sold for four hundred fifty-one thousand dollars in two thousand one, and a nineteen sixty-six four hundred twenty-seven for one point zero five million in twenty twenty-two. Different cars again. We note them, we do not draw a line.""",
   "Classic car auction", "DIFFERENT CARS, DIFFERENT YEARS: NOT A TREND")
sc("""What we can say is that both cars have appreciated over their histories, and that the Cobra's price is in a different band. For the Ace, the top sales we found are in the low hundreds of thousands. For the Cobra, the bottom of the original range is about a million, according to Du Pont Registry, and the Hagerty guide is higher. Whatever else changes, that gap is large.""",
   "Classic car prices", "ACE: LOW HUNDREDS OF THOUSANDS · COBRA: ~$1M AND UP")

ch("Round five: racing")
sc("""Both cars raced. Wikipedia says A C Aces raced at Le Mans in nineteen fifty-seven and fifty-eight. The class win it describes came in nineteen fifty-nine, when Ted Whiteaway and John Turner's Ace Bristol took the two litre G T class and finished seventh overall. That is a very respectable result for a small, light British sports car against much larger cars.""",
   "AC Ace Le Mans", "1959: ACE BRISTOL WINS ITS CLASS · 7TH OVERALL")
sc("""The Cobra's record is bigger. Carroll Shelby's page says the Daytona Coupe won three G T class wins in nineteen sixty-four, including Le Mans and Goodwood, plus the S C C A U S G T Championship. In nineteen sixty-five, the Cobra won the International Championship for G T Manufacturers. And Wikipedia notes that the four hundred twenty-seven was not homologated for that season.""",
   "Shelby Daytona Coupe", "COBRA: CLASS WINS 1964 · GT MANUFACTURERS' TITLE 1965")
sc("""So the Ace won a class at Le Mans in nineteen fifty-nine, and the Cobra won classes and a championship five and six years later. The difference was again the engine. A larger V eight could be developed and reliably run, and the Daytona Coupe was rated at three hundred eighty-five horsepower, according to Wikipedia. The chassis was the same family, but the results were not.""",
   "Racing Cobra", "SAME CHASSIS FAMILY · A VERY DIFFERENT RESULT SHEET")

ch("Round six: price and value")
sc("""Du Pont Registry says the Cobra four hundred twenty-seven's release price was seven thousand, five hundred dollars. The Ace's original price is not given in the sources we used. So we cannot compare new prices. What we can compare are values today, from sales reported by Hagerty and others, and these show a big gap.""",
   "Shelby Cobra 427", "NEW PRICE: COBRA 427 $7,500 · ACE: NOT IN OUR SOURCES")
sc("""Hagerty's past-sales database lists a nineteen fifty-nine Ace Bristol sold at Coys in London in December two thousand three for a hundred sixteen thousand, five hundred sixty-two dollars. A nineteen fifty-six Ace Bristol sold at Bonhams in September twenty eleven for two hundred twenty-three thousand, one hundred twenty-four dollars. Hagerty called the second price high for a standard Bristol-engined Ace.""",
   "AC Ace Bristol auction", "ACE BRISTOL: $116,562 (2003) · $223,124 (2011)")
sc("""For the Cobra, Hagerty lists a nineteen sixty-five four hundred twenty-seven S slash C sold in August two thousand one by R M Auctions for four hundred fifty-one thousand dollars. A Hagerty price guide dated April twenty twenty-five lists a number three good condition S slash C at two point two five million. Du Pont Registry says a nineteen sixty-six four hundred twenty-seven sold for one point zero five million at Amelia Island in twenty twenty-two.""",
   "Shelby Cobra auction", "COBRA 427: $451K (2001) · $1.05M (2022) · GUIDE $2.25M (2025)")
sc("""By our arithmetic, the Cobra's two point two five million guide value is about ten times the Ace Bristol's two hundred twenty-three thousand sale. Against the two thousand three Ace sale, it is nearly twenty times. These dates differ by fourteen to twenty-two years, so the comparison is rough, but the order of magnitude is clear.""",
   "Shelby Cobra and AC Ace values", "COBRA ≈ 10–19× THE ACE BRISTOL (OUR ARITHMETIC, DIFFERENT DATES)")
sc("""The Cobra's price has its own ceiling and floor. Du Pont Registry says original four hundred twenty-seven Cobras start at over a million dollars, and the two hundred eighty-nine is just under a million. It adds that A C Cobra prices have stayed under seven figures partly because of the continuation cars. So the original, the continuation and the replica form three separate markets.""",
   "Shelby Cobra market", "ORIGINAL · CONTINUATION · REPLICA: THREE MARKETS")
sc("""And one more number. The prototype, chassis C S X two thousand, sold for thirteen point seven five million dollars at R M Sotheby's in August two thousand sixteen, according to EVO. That is a unique car with a unique story, not a typical Cobra. But it shows what the right chassis number can mean, and nothing like it has happened to an Ace.""",
   "Shelby Cobra CSX2000", "THE PROTOTYPE: $13.75 MILLION (2016)")

ch("What to know before you buy either")
sc("""A word for anyone who dreams of owning one. For the Ace, the Hagerty entries describe cars with right-hand drive, Bristol engines of about a hundred twenty horsepower, wire wheels and side exhausts, in conditions from very good to exceptionally clean original. The condition and history, the commentary says, drove the price. A long ownership by two owners from new was cited for the higher result.""",
   "AC Ace Bristol", "ACE: HISTORY AND ORIGINALITY DROVE THE PRICE (HAGERTY)")
sc("""For the Cobra, the question before price is authenticity. Original, continuation, or replica. Wikipedia describes continuation series numbered four thousand to nine thousand, a nineteen ninety-three controversy about duplicate titles, and mostly fibreglass bodies on the later cars. A buyer needs the chassis number and its documentation checked by someone who knows the history. The sources agree on nothing else as strongly.""",
   "Shelby Cobra chassis plate", "COBRA: CHECK THE CHASSIS NUMBER AND ITS PAPERWORK")
sc("""For both cars, we found no reliable figures for running costs, insurance or repairs. Anyone quoting a precise number for them has a source we did not find. The honest summary is that both are rare, old, hand-finished cars. Their prices, as we showed, are in very different ranges, and their maintenance needs are different too, though we cannot put numbers on that.""",
   "Classic car garage", "RUNNING COSTS: NO RELIABLE FIGURES IN OUR SOURCES")

ch("The verdict")
sc("""So, which wins? On power, the Cobra, by a factor of two and a half to three. On weight, the Ace, by a fifth to two fifths. On speed, the Cobra, by roughly half again. On racing, the Cobra, with a championship against a class win. On production, about the same order. On price today, the Cobra, by a factor of ten or more.""",
   "Shelby Cobra and AC Ace", "SCORECARD")
sc("""The real difference is the engine. The Ace is a delicate, beautiful British car whose power came from a six. The Cobra is the same car with the biggest Ford V eight that would fit. That is not a criticism of the Ace. It is the simplest explanation of why one is a classic and the other is an icon.""",
   "Shelby Cobra and AC Ace", "ONE ENGINE SWAP CHANGED EVERYTHING")
sc("""One caution. We have not driven either car. The Ace page's weights conflict, the Cobra's power ratings differ between sources, and the production numbers do not add up. We told you where, and where the arithmetic is ours. If you have a verified detail, tell us in the comments, with where it comes from.""",
   "Shelby Cobra and AC Ace", "SOURCES DISAGREE ON WEIGHT, POWER AND COUNTS")
sc("""Which would you rather own, the Ace or the Cobra? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Cobra, work out what a real one costs today, and tell the story of the man who built it. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video110", "Shelby Cobra vs AC Ace: The Real Difference", [
    "Wikipedia, AC Cobra: https://en.wikipedia.org/wiki/Shelby_Cobra",
    "Wikipedia, AC Ace: https://en.wikipedia.org/wiki/AC_Ace",
    "Wikipedia, Carroll Shelby: https://en.wikipedia.org/wiki/Carroll_Shelby",
    "Du Pont Registry, Shelby 427 Cobra price, specs, photos and review: https://news.dupontregistry.com/blogs/specs/shelby-427-cobra-price-specs-photos-and-review",
    "EVO, First-ever Shelby Cobra sells for record $13.75 million (22 Aug 2016): https://evo.co.uk/news/17955/first-ever-shelby-cobra-sells-for-record-1375-million",
    "Hagerty, 1965 Shelby Cobra 427 S/C (CSX3040): https://hagerty.com/valuation-tools/past-sales/1965-shelby-cobra/CSX3040/f33aeb97-e529-47a0-8f48-6136a6b53fde",
    "Hagerty, 1959 AC Ace Bristol (BEX1117): https://www.hagerty.com/valuation-tools/past-sales/1959-ac-ace/BEX1117/1941242a-4d75-4ac0-bb77-074a95444bf2",
    "Hagerty, 1956 AC Ace Bristol (BE172): https://www.hagerty.com/valuation-tools/past-sales/1956-ac-ace/BE172/572ff6cd-fdbd-4ac0-9fb2-66be383447e4",
], "B")
