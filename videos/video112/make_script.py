import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""He was told he had less than five years to live. So he quit racing, and built cars. Carroll Shelby had a heart defect from childhood, took nitroglycerin pills during races, and lived to eighty-nine. In between, he put an American engine in a British chassis, helped Ford win Le Mans, and had a heart transplant while working on the Dodge Viper. This is the story of the man who built the Shelby Cobra.""",
   "Carroll Shelby", "THE MAN WHO BUILT THE SHELBY COBRA")
sc("""Here is the twist. Before any of that, he was a chicken farmer whose farm went bankrupt. And the sources we read disagree on when he won Le Mans, on how he got the engine, and even on how many cars he made. We will tell his story as the sources do, and say where they conflict.""",
   "Carroll Shelby", "A BANKRUPT CHICKEN FARMER · SOURCES DISAGREE ON KEY DATES")
sc("""Every fact in this video comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Carroll Shelby", "EVERY FACT IS SOURCED")

ch("A sick boy in Texas")
sc("""Wikipedia says Carroll Shelby was born on the eleventh of January, nineteen twenty-three, in Leesburg, Texas. Texas Co-op Power adds that his father was a rural mail carrier, and that he graduated from Woodrow Wilson High School in Dallas. The page says he had heart valve leakage by age seven, and related complications for the rest of his life.""",
   "Leesburg, Texas", "BORN 11 JANUARY 1923 · LEESBURG, TEXAS")
sc("""Texas Co-op Power says he was diagnosed with a serious congenital heart defect at seven. That is the thread running through his whole life. A man who could not count on his heart spent his career at the limit of what machines and bodies can do. It is easy to call that irony. The sources simply record it.""",
   "Carroll Shelby", "HEART DEFECT DIAGNOSED AT AGE 7")
sc("""Wikipedia says he enlisted in the Army Air Corps on the eleventh of April, nineteen forty-one, and was commissioned a second lieutenant in December nineteen forty-two. Texas Co-op Power says he served as a flight instructor and test pilot near San Antonio. By our own arithmetic, he enlisted at eighteen. He was discharged after the war ended.""",
   "Army Air Corps", "ENLISTED 11 APRIL 1941 AT AGE 18 (OUR ARITHMETIC)")
sc("""After the war, he tried several trades. Wikipedia lists a dump truck business, work as an oil-well roughneck in nineteen forty-eight and forty-nine, and a poultry farm that went bankrupt in nineteen fifty-two. Texas Co-op Power says he ran the dump truck business, tried roughnecking, then raised chickens. Both sources agree on the order, and on where it ended.""",
   "Texas poultry farm", "DUMP TRUCKS · OIL RIGS · CHICKENS (BANKRUPT 1952)")

ch("From chicken farm to racetrack")
sc("""He began racing as an amateur in nineteen fifty-two, according to Wikipedia. In nineteen fifty-three he won eight or nine races. Texas Co-op Power says he left the chicken farm in striped bib overalls to race at Eagle Mountain near Fort Worth, and that the overalls became his signature attire. By nineteen fifty-six, the page says, he had won thirty races in a Ferrari.""",
   "Carroll Shelby racing 1950s", "1953: RACING IN BIB OVERALLS · 1956: 30 WINS IN A FERRARI")
sc("""Sports Illustrated named him driver of the year in nineteen fifty-six and nineteen fifty-seven, both sources say. His career had a stumble in Europe: Wikipedia lists eight Formula One entries in nineteen fifty-eight with no points and no podiums, driving a Maserati two fifty F for Scuderia Centro Sud. He was replaced at Le Mans by Stuart Lewis-Evans after falling ill with dysentery.""",
   "Maserati 250F", "1958 FORMULA ONE: 8 ENTRIES · NO POINTS")
sc("""Then Le Mans. Wikipedia says Shelby won the twenty-four hours in nineteen fifty-nine with Roy Salvadori in an Aston Martin D B R one. He later called it, the page says, probably the greatest thrill I ever got out of racing. Texas Co-op Power, however, says he won with Salvadori in nineteen fifty-eight. The sources disagree by a year.""",
   "Le Mans 1959 Aston Martin", "LE MANS WIN: 1959 (WIKIPEDIA) VS 1958 (TEXAS CO-OP POWER)")
sc("""We use nineteen fifty-nine, since Wikipedia gives the specific car, an Aston Martin D B R one, and since it also mentions the nineteen fifty-eight season separately, when he drove a Maserati in Formula One. We flag the discrepancy because the Le Mans win is central to his legend. A viewer who looks it up should check a primary record of the race.""",
   "Aston Martin DBR1", "WE USE 1959 · CHECK A PRIMARY RACE RECORD")
sc("""Wikipedia says he won the S C C A and U S A C road racing sports car championship in nineteen sixty. Texas Co-op Power says he won three U.S. sports car championships in all. In nineteen sixty he was also racing with a secret, the pills. In a two hundred mile race, the magazine says, he took nitroglycerin under his tongue and finished third.""",
   "Carroll Shelby 1960", "1960: CHAMPION — AND RACING ON NITROGLYCERIN")
sc("""Texas Co-op Power quotes him: if I hadn't slowed down each time I popped one of those pills, I might have won. That same year, the page says, he was told he had less than five years to live and quit driving. Wikipedia says he retired in October nineteen sixty for health reasons, and opened a high-performance driving school in nineteen sixty-one with Pete Brock.""",
   "Carroll Shelby", "\"IF I HADN'T SLOWED DOWN EACH TIME I POPPED ONE OF THOSE PILLS...\"")
sc("""By our arithmetic, five years from nineteen sixty would have been nineteen sixty-five. Carroll Shelby died in two thousand twelve. So the prediction was out by forty-seven years. We do not know who made it or how precisely it was put, and the source does not say. But the contrast is the point: a man told he had little time did more with it than most.""",
   "Carroll Shelby", "A 5-YEAR PREDICTION · 52 YEARS LATER HE DIED (OUR ARITHMETIC)")

sc("""Wikipedia gives more detail on his early racing. In nineteen fifty-four, it says, he raced a D B R three at Sebring, where it broke an axle, and drove an Aston Martin at Le Mans that did not finish. In nineteen fifty-three he won eight or nine races, the page says, and in nineteen fifty-six he won thirty with a Ferrari. His record is a mixture of great seasons and failures.""",
   "Sebring racing", "1954: AN AXLE BREAKS AT SEBRING · A DNF AT LE MANS")
sc("""By our arithmetic, his racing career as an amateur and professional ran from nineteen fifty-two to October nineteen sixty, which is about eight years. In those eight years, he went from bankrupt farmer to Sports Illustrated's driver of the year, and then to retired invalid. It is a short career by the standards of most racing drivers, and it was shortened by his heart.""",
   "Carroll Shelby", "RACING CAREER: 1952–1960 ≈ 8 YEARS (OUR ARITHMETIC)")
sc("""Let us line up his age at the key moments, all our arithmetic from the sourced dates. Eighteen when he enlisted. Twenty-nine when his poultry farm failed. Thirty-six at Le Mans, if the win was in nineteen fifty-nine. Thirty-seven when he retired. Thirty-nine at the first Cobra. Forty-three at the Ford one-two-three at Le Mans in nineteen sixty-six.""",
   "Timeline", "AGE 18 · 29 · 36 · 37 · 39 · 43 (OUR ARITHMETIC)")
sc("""Look at that sequence. His greatest success as a builder came after the end of his career as a driver, and after a doctor told him he had little time. Texas Co-op Power says he quit driving and turned to designing cars. The sources never claim that his illness caused his success, and we do not either. We only note the order of events.""",
   "Carroll Shelby", "THE BUILDER'S CAREER BEGAN WHERE THE DRIVER'S ENDED")
sc("""After retirement, Wikipedia says he opened a high-performance driving school in nineteen sixty-one with Pete Brock. EVO adds that the first Cobra, C S X two thousand, was used at a driving school for a time, and then in promotional and historic events, and stayed in the Shelby family for decades. The school was a way to make a living from his name and skill while he could not race.""",
   "Driving school", "1961: DRIVING SCHOOL WITH PETE BROCK")

ch("The Cobra")
sc("""In nineteen sixty-one, the Cobra page says, Ford gave Shelby two new small-block V eights in September, and one went to A C in England. The A C Ace page says Shelby proposed fitting a Ford V eight to the Ace chassis. AC completed the prototype in January nineteen sixty-two, and it was air-freighted to Shelby in Los Angeles on the second of February.""",
   "AC Ace chassis", "SEPT 1961: FORD ENGINES · FEB 1962: PROTOTYPE ARRIVES")
sc("""Shelby's team installed the engine and transmission in under eight hours at Dean Moon's shop in Santa Fe Springs, California. Jalopnik says the prototype was tested on an improvised road course between oil derricks, and that its durability convinced them the idea was sound. Shelby built it on a small budget, then got funding from Ford for the first group of Cobras.""",
   "Dean Moon's shop", "INSTALLED IN UNDER EIGHT HOURS · FUNDED BY FORD AFTER")
sc("""Texas Co-op Power says that in nineteen sixty-two, in Southern California, he put an American Ford V eight into a British A C Cars chassis, creating the first Cobra. Carroll Shelby's Wikipedia page says production began in March nineteen sixty-two, with seventy-five cars sold by the end of that year, and a hundred built by April nineteen sixty-three.""",
   "Shelby Cobra 1962", "MARCH 1962: PRODUCTION BEGINS · 75 SOLD BY YEAR END")
sc("""Shelby founded Shelby American in nineteen sixty-two, Wikipedia says, to manufacture and market performance vehicles. In an age when most carmakers were large corporations, this was a small firm making fast cars from a combination of British and American parts. By our reading, Shelby's genius was not engineering from scratch. It was combining the right pieces and selling them with a story.""",
   "Shelby American", "1962: SHELBY AMERICAN FOUNDED")
sc("""The racing began right away. Wikipedia says the Daytona Coupe won three G T class wins in nineteen sixty-four, including Le Mans and Goodwood, plus the S C C A U S G T Championship. In nineteen sixty-five, the Cobra won the International Championship for G T Manufacturers. These are the wins that made the car's reputation, and they came within three years of the prototype's arrival.""",
   "Shelby Daytona Coupe", "1964: CLASS WINS · 1965: GT MANUFACTURERS' CHAMPIONSHIP")
sc("""Not everything was smooth. Wikipedia says Ford and Shelby ended Cobra imports from England in nineteen sixty-seven, and calls the Cobra a financial failure. The car that made his name did not make his firm rich. That fact is worth remembering when you see what Cobras sell for now. The money went to owners and auction houses, decades later.""",
   "Shelby Cobra", "1967: IMPORTS END · \"A FINANCIAL FAILURE\"")

ch("Ford, Le Mans and Mustang")
sc("""After the Cobra, Ford. Wikipedia says Shelby developed the Ford G T forty Mark Two, which gave Ford a one-two-three finish at Le Mans in nineteen sixty-six and the constructors' title. Texas Co-op Power credits his Ford G T forty with Le Mans wins in nineteen sixty-six and sixty-seven. Wikipedia says the G T forty won Le Mans in nineteen sixty-six, sixty-seven, sixty-eight and sixty-nine.""",
   "Ford GT40 Le Mans 1966", "FORD GT40: LE MANS 1966, 67, 68, 69")
sc("""The two sources describe his role slightly differently. Wikipedia says he developed the Mark Two and finalised the Mark Four, which won at Sebring in nineteen sixty-seven. The magazine credits the car to him broadly. The long list of G T forty wins was a Ford programme with many people, and Shelby's part was large. We should not give him credit for all of it.""",
   "Ford GT40", "SHELBY'S PART WAS LARGE — BUT IT WAS A FORD PROGRAMME")
sc("""There was a loss. Wikipedia says Ken Miles died in a crash in August nineteen sixty-six, after which Shelby finalised the Mark Four. Miles, the same driver who raced the big-engined Cobra and called it The Turd. The page records the fact briefly. It is a reminder that this was a dangerous business, and that the people in it paid for the wins.""",
   "Ken Miles", "AUGUST 1966: KEN MILES DIES IN A CRASH")
sc("""On the road, the Shelby G T three fifty, from nineteen sixty-five, and the G T five hundred, from nineteen sixty-seven, were produced with Ford, and Shelby built them through nineteen sixty-eight, according to Wikipedia. Texas Co-op Power says he helped Ford's chairman, Lee Iacocca, develop the Mustang racers: the G T three fifty, the G T forty, the G T five hundred and the G T five hundred K R, for king of the road.""",
   "Shelby GT350 Mustang", "GT350 (1965) · GT500 (1967) · GT500KR \"KING OF THE ROAD\"")

sc("""Shelby used his own cars. EVO says a nineteen sixty-five Shelby four twenty-seven Cobra, chassis C S X three one seven eight, sold in the same two thousand sixteen auction as the prototype, was used regularly by Shelby. And Wikipedia says the Super Snake, a nineteen sixty-six conversion with twin Paxton superchargers, was later used by him personally. He seems to have driven what he built.""",
   "Shelby Cobra 427", "SHELBY DROVE HIS OWN CARS: CSX 3178 AND THE SUPER SNAKE")
sc("""The Super Snake sold for five million dollars at Barrett-Jackson in January two thousand seven, the Cobra page says. That is a car he drove, converted to a purpose he cared about: more power. By our arithmetic, five million dollars is about six hundred sixty-seven times the seven thousand, five hundred dollar price of a new four hundred twenty-seven, though the Super Snake was never a showroom car.""",
   "Shelby Cobra Super Snake", "$5M ÷ $7,500 ≈ 667× (OUR ARITHMETIC)")
sc("""There was a human cost to the racing programme. Wikipedia says Ken Miles died in nineteen sixty-six. The same page records that Miles raced a Ford powered Mark Two at Sebring and called it The Turd, and that at Nassau a six point four litre Cobra led after one lap but retired with brake problems. These details show how experimental Shelby's cars were, and how dangerous the work was.""",
   "Ken Miles", "EXPERIMENTAL CARS · A DANGEROUS JOB")

ch("Chrysler, the Viper and a new heart")
sc("""Later he worked with Dodge and Chrysler, Wikipedia says, including on the Dodge Viper. Texas Co-op Power says he helped create the Dodge Charger and the Dodge Viper with Iacocca at Chrysler. We looked at the Viper in another video of this series, so the name may be familiar. Shelby's role is described in both sources as that of an adviser and a promoter.""",
   "Dodge Viper", "LATER: DODGE AND CHRYSLER, INCLUDING THE VIPER")
sc("""Here is the personal side. Both sources say he had a heart transplant in nineteen ninety. Texas Co-op Power adds that he was working on the Viper at the time. In nineteen ninety-one he established the Carroll Shelby Foundation, and the page says it helps children with heart disease. Wikipedia names it the Carroll Shelby Children's Foundation.""",
   "Carroll Shelby Foundation", "1990: HEART TRANSPLANT · 1991: FOUNDATION")
sc("""In nineteen ninety-six he received a kidney, according to Wikipedia. Texas Co-op Power says it came from his son Michael, making him one of the oldest survivors of two transplants. By our own arithmetic, he was seventy-three years old at the kidney transplant, and sixty-seven at the heart transplant. A man told in nineteen sixty that he had five years left did both.""",
   "Hospital", "HEART AT 67 · KIDNEY AT 73 (OUR ARITHMETIC)")
sc("""In two thousand three, Wikipedia says, he became technical adviser to the Ford G T project. And the two thousand five Ford G T five hundred was the first official Shelby-Ford Mustang collaboration since nineteen seventy-one. By our arithmetic, that is thirty-four years between the two. His name was still on the cars, long after his racing days.""",
   "Ford GT500", "2003: FORD GT ADVISER · 2005: GT500 FIRST SINCE 1971")

ch("The less glorious parts")
sc("""A fair biography includes what went wrong. Wikipedia says he was married seven times. It also records controversies. The completion Cobras were allegedly built from leftover parts, and Shelby allegedly skipped blocks of V I N numbers to satisfy homologation, before the cars were relabelled continuation Cobras. The page uses the word allegedly, and so do we.""",
   "Carroll Shelby", "SEVEN MARRIAGES · ALLEGATIONS ABOUT COMPLETION COBRAS")
sc("""The Cobra page adds that in nineteen ninety-three the Los Angeles Times reported that Shelby had obtained forty-three duplicate titles for Cobras not in A C's records. Shelby said the chassis were built by McCluskey in nineteen ninety-one and ninety-two, and claimed a rival was behind the report. We cannot settle it. We report that the report existed, and that he disputed it.""",
   "Los Angeles Times 1993", "1993 REPORT: 43 DUPLICATE TITLES · SHELBY DISPUTED IT")
sc("""In two thousand seven, Wikipedia says, he ended a licensing deal with Unique Performance after customers complained about undelivered cars. The company was raided and went bankrupt. In two thousand eight, Denice Halicki won a case against Shelby over selling Eleanor-branded cars. These are legal outcomes recorded on a public page. We add no gloss to them.""",
   "Courtroom", "2007: LICENSING DEAL ENDED · 2008: HALICKI CASE LOST")
sc("""He also lent his name to many things. Wikipedia lists chili kits, a nineteen sixty-seven deodorant, a Donzi boat and Saab wheels. Texas Co-op Power says he owned a ranch near Terlingua, helped launch the world chili cook-off in nineteen sixty-eight, created a chili mix, and in nineteen seventy-five helped start the Chili's restaurant chain. It is an odd range for a racing driver.""",
   "Carroll Shelby chili", "CHILI · DEODORANT · A BOAT · SAAB WHEELS")

ch("Shelby by the numbers")
sc("""A few numbers, from the sources. Born in nineteen twenty-three, died in twenty twelve, which by our arithmetic is eighty-nine years. Married seven times. Two transplants. Thirty race wins in a Ferrari in a single season. Seventy-five Cobras sold in the first year, a hundred by April nineteen sixty-three. Nine hundred ninety-eight Cobras built in all, according to Du Pont Registry.""",
   "Carroll Shelby", "89 YEARS · 7 MARRIAGES · 2 TRANSPLANTS · 998 COBRAS")
sc("""And the numbers that came later. The first Cobra sold for thirteen point seven five million dollars. The Super Snake for five million. A good condition four hundred twenty-seven S slash C is valued at two point two five million by Hagerty's April twenty twenty-five guide. These are what the market assigns to the things he made. They are not what the things earned him in his lifetime.""",
   "Shelby Cobra", "$13.75M · $5M · $2.25M: THE MARKET'S VERDICT")
sc("""We said at the start that the Cobra was a financial failure, according to Wikipedia. We should be fair to Shelby: his Ford programmes, his Mustang work and his licensing earned money that our sources do not quantify. We do not know how rich he was at any point, and we will not guess. What we know is what he did, and what the cars are worth now.""",
   "Carroll Shelby", "WE DON'T KNOW HOW RICH HE WAS (NOT IN OUR SOURCES)")
sc("""There is one more kind of number: years. From the prototype's arrival in February nineteen sixty-two to the Ford G T forty's Le Mans win in nineteen sixty-six is about four years, by our arithmetic. In that time Shelby went from installing one engine in an English car to supporting a manufacturers' championship and a one-two-three. It is a fast rise by any measure.""",
   "Ford GT40 Le Mans", "FEB 1962 → 1966: ABOUT 4 YEARS (OUR ARITHMETIC)")

ch("The end, and the legacy")
sc("""Carroll Shelby died on the tenth of May, twenty twelve, in Dallas, aged eighty-nine, Wikipedia says. Texas Co-op Power adds that he died at Baylor Hospital, shortly before the twenty thirteen Shelby G T five hundred debuted. His last wife, Wikipedia notes, was in the process of divorcing him at the time. The page is blunt about that, and so are we.""",
   "Carroll Shelby", "DIED 10 MAY 2012 · DALLAS · AGE 89")
sc("""In twenty nineteen, Ford v Ferrari depicted him, played by Matt Damon, and the film won an Oscar, Wikipedia records. By our arithmetic, the film appeared seven years after his death. It brought his name to people who had never seen a Cobra. The page does not say what happened to Cobra prices, so we do not claim anything about that.""",
   "Ford v Ferrari", "2019: PLAYED BY MATT DAMON IN FORD V FERRARI")
sc("""What is his legacy? A car that looks as good as it did in nineteen sixty-two, a prototype that sold for thirteen point seven five million dollars in two thousand sixteen, and a reputation for turning a bad hand into a story. The sources also record disputes and failures, and a fair account has to include them. Both parts are true.""",
   "Shelby Cobra CSX2000", "CSX 2000 SOLD FOR $13.75M IN 2016 (EVO)")
sc("""Look at the dates once more. Born in nineteen twenty-three. A bankrupt farm in nineteen fifty-two. Le Mans in nineteen fifty-nine. Retired in nineteen sixty. The first Cobra in nineteen sixty-two. Le Mans for Ford in nineteen sixty-six. A new heart in nineteen ninety. A death in twenty twelve. By our arithmetic, the Cobra came when he was thirty-nine, after he thought his career was over.""",
   "Carroll Shelby", "THE FIRST COBRA CAME AT AGE 39 (OUR ARITHMETIC)")
sc("""A last caution. We have not met anyone who knew Carroll Shelby, and we are not biographers. We have read Wikipedia and a magazine profile, and we have flagged where they disagree: the year of the Le Mans win, and the details of the Ford programme. If you know a primary source, tell us in the comments, so we can get it right.""",
   "Carroll Shelby", "SOURCES DISAGREE ON THE LE MANS YEAR")
sc("""Which part of his story stayed with you most, the pills, the eight hours, or the new heart? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Cobra, compare it with the A C Ace, and work out what a real one costs today. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video112", "The Man Who Built the Shelby Cobra", [
    "Wikipedia, Carroll Shelby: https://en.wikipedia.org/wiki/Carroll_Shelby",
    "Texas Co-op Power, From Chicken Farmer to Snake Charmer: https://texascooppower.com/from-chicken-farmer-to-snake-charmer/",
    "Wikipedia, AC Cobra: https://en.wikipedia.org/wiki/Shelby_Cobra",
    "Wikipedia, AC Ace: https://en.wikipedia.org/wiki/AC_Ace",
    "Jalopnik, The very first Shelby Cobra just sold for a staggering record $13.75 million (21 Aug 2016): https://www.jalopnik.com/the-very-first-shelby-cobra-just-sold-for-a-staggering-1785559850/",
    "EVO, First-ever Shelby Cobra sells for record $13.75 million (22 Aug 2016): https://evo.co.uk/news/17955/first-ever-shelby-cobra-sells-for-record-1375-million",
], "D")
