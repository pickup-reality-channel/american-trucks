import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The new Corvette ZR1 makes one thousand, sixty-four horsepower. It costs about as much as a well-equipped luxury S U V. And its name was once so rare that, in three years, only fifty-three buyers ticked the box. Here are two things you may not know about the Corvette ZR1: who really built the engine of the first one, and what that name has meant, generation by generation.""",
   "Chevrolet Corvette ZR1", "2 THINGS YOU DIDN'T KNOW ABOUT THE NEW CORVETTE ZR1")
sc("""One: the first ZR-1 engine was designed by Lotus and assembled by a company that mostly builds boat engines. Two: the ZR1 name started as a rare engine package, and each generation since has claimed to be the fastest Corvette of its day. We will follow the numbers across five decades, and say where our sources disagree.""",
   "Chevrolet Corvette ZR1", "THE ENGINE LOTUS DESIGNED · THE NAME THAT STARTED AS AN OPTION")
sc("""Every figure comes from a published source, listed in the description. Where sources disagree, we tell you. Where we do the maths ourselves, we say so. And where a number is a manufacturer's claim, rather than a measurement, we label it as one.""",
   "Chevrolet Corvette ZR1", "EVERY NUMBER IS SOURCED")

ch("Where the name came from")
sc("""The ZR1 name is older than most people think. Wikipedia says that in the nineteen seventy to nineteen seventy-two model years, ZR1 and ZR2 were special engine packages for the third-generation Corvette. The page gives a single production figure: only fifty-three of those packages were optioned across those three model years. That is the whole of the first chapter.""",
   "Chevrolet Corvette C3", "1970–72: ZR1 AND ZR2 WERE ENGINE PACKAGES · ONLY 53 OPTIONED")
sc("""By our arithmetic, fifty-three packages across three years is about eighteen a year. Compare that with the sixth-generation ZR1, which the same page treats as a full model, and the current car, where Wikipedia's production table lists one hundred eighty ZR1s for the twenty twenty-five model year. The name went from a rare option to a halo model.""",
   "Chevrolet Corvette ZR1", "53 PACKAGES IN 3 YEARS ≈ 18 A YEAR (OUR ARITHMETIC) · 180 ZR1s IN MY2025")
sc("""The name then disappeared for years. It came back in nineteen ninety on the fourth-generation Corvette, as the top-tier package, with a special engine designed in partnership with Lotus. Wikipedia says the goal was to create the world's fastest production car. That sentence is the whole point of the ZR1, and it has been the point ever since.""",
   "Chevrolet Corvette C4 ZR-1", "1990: THE ZR-1 RETURNS · GOAL: THE WORLD'S FASTEST PRODUCTION CAR")

ch("Thing one: an engine designed in Britain, built by a boat company")
sc("""Here is the first surprising fact. General Motors bought Group Lotus in nineteen eighty-six, Wikipedia says, and Lotus designed the C4 ZR-1's engine, called the L T five. It was a five point seven litre aluminium V eight with double overhead camshafts and thirty-two valves, and an eleven to one compression ratio. The standard Corvette engine of the time was a pushrod unit, and the contrast was large.""",
   "Lotus LT5 engine", "GM BOUGHT GROUP LOTUS IN 1986 · LOTUS DESIGNED THE LT5 · 5.7 L, DOHC, 32 VALVES")
sc("""It was rated at three hundred seventy-five horsepower and three hundred seventy pound-feet from nineteen ninety to ninety-two. After Lotus revised the heads, exhaust and valvetrain, the page says, it rose to four hundred five horsepower and three hundred eighty-five pound-feet for nineteen ninety-three to ninety-five. By our arithmetic, that is an increase of eight percent in power and about four percent in torque.""",
   "Chevrolet Corvette ZR-1 engine", "LT5: 375 HP / 370 LB-FT (1990–92) → 405 HP / 385 LB-FT (1993–95)")
sc("""Lotus also designed the air management system, which shuts off eight of the sixteen intake runners at part throttle, the page says, and upgraded the car's braking and steering. The engine used twelve quarts of oil, seven more than the standard engine. It was a different machine from the standard Corvette, in a car that looked, from the outside, much like one.""",
   "Chevrolet Corvette C4", "AIR MANAGEMENT SHUTS 8 OF 16 RUNNERS AT PART THROTTLE · 12 QUARTS OF OIL (7 MORE THAN STANDARD)")
sc("""Now the boat company. Wikipedia says Mercury Marine, through its MerCruiser division in Stillwater, Oklahoma, did most of the drilling and boring and the hand assembly of the L T fives, then shipped the engines to the Corvette plant in Bowling Green. So the ZR-1's heart was designed in Britain, assembled in Oklahoma by a marine engine builder, and fitted in Kentucky.""",
   "Mercury Marine Stillwater", "MERCURY MARINE (STILLWATER, OKLAHOMA) HAND-ASSEMBLED THE LT5 · FITTED AT BOWLING GREEN, KENTUCKY")
sc("""The page adds a detail that sounds like a joke but is documented. Mercury kept two L T fives for itself: one for the company president's ZR1, and one for a speedboat called the Wette Vette, tuned to four hundred twenty horsepower. We found no further source on that boat, so we repeat only what the page says, and do not elaborate.""",
   "Mercury Marine Wette Vette", "MERCURY KEPT TWO LT5s: ONE FOR THE PRESIDENT'S ZR1, ONE FOR A SPEEDBOAT TUNED TO 420 HP")
sc("""Why does that matter? Because the ZR1 name, from the start, was about borrowing engineering from outside the usual Corvette world. A British consultancy owned by GM, and a boat-engine factory in Oklahoma. Today the engine is a Chevrolet design, but the habit of reaching for a different approach, a flat-plane crank and twin turbos, continues. That connection is our reading, not a claim from the sources.""",
   "Chevrolet Corvette ZR1", "A TRADITION OF BORROWING DIFFERENT ENGINEERING (OUR READING)")

ch("The rest of the first ZR-1")
sc("""The rest of the car matched the engine. The page lists Bilstein F X three adaptive suspension, similar in concept to the Porsche nine fifty-nine's, with six damping settings in each of three modes. The tyres were Goodyear Eagle Gatorbacks, three fifteen over thirty-five Z R seventeen, on eleven-inch rear wheels. The ZR1 was wider, and about two hundred pounds heavier than a standard C four.""",
   "Chevrolet Corvette C4 ZR-1", "BILSTEIN ADAPTIVE SUSPENSION · P315/35ZR17 GOODYEAR GATORBACKS · +200 LB OVER A STANDARD C4")
sc("""It had a ZF six-speed manual gearbox with computer-aided gear selection, a three point four five to one final drive, and Bosch anti-lock brakes. The prototype's nickname, Wikipedia says, was King of the Hill. That is the ambition in three words: not a quick Corvette, but the car on top of the hill.""",
   "Chevrolet Corvette ZR-1", "ZF 6-SPEED · BOSCH ABS · PROTOTYPE NICKNAME: 'KING OF THE HILL'")
sc("""How fast was it? Wikipedia cites Road and Track at four point nine seconds to sixty miles per hour, a thirteen point four second quarter mile and a top speed of one hundred seventy-nine miles per hour. Car and Driver measured four point five seconds to sixty and a twelve point eight second quarter mile at one hundred eleven miles per hour. Two tests of the same year, two sets of numbers.""",
   "Chevrolet Corvette ZR-1 test", "R&T: 4.9 S, 13.4 S, 179 MPH · C&D: 4.5 S, 12.8 S AT 111 MPH")
sc("""The page also lists FIA-verified records set at Fort Stockton, Texas, on the first of March, nineteen ninety. The ZR-1 covered five thousand kilometres at one hundred seventy-five point seven one miles per hour and twenty-four hours at one hundred seventy-five point eight eight five, covering four thousand, two hundred twenty-one miles. By our arithmetic, that is an average of about one hundred seventy-six miles an hour for a whole day. The page adds that the Volkswagen W twelve concept later broke those records.""",
   "Fort Stockton", "MARCH 1, 1990: 24 HOURS AT 175.885 MPH · 4,221.256 MILES · FIA-VERIFIED · LATER BROKEN BY VW W12")
sc("""Production was small. Wikipedia lists six thousand, nine hundred thirty-nine ZR-1s built from nineteen ninety to nineteen ninety-five. By our arithmetic, that averages about one thousand, one hundred fifty-seven cars a year. The page does not give a ZR-1 price, or the premium over a base Corvette, which cost thirty-two thousand, four hundred seventy-nine dollars in nineteen ninety. So we cannot say how much more it cost.""",
   "Chevrolet Corvette ZR-1 production", "6,939 BUILT 1990–95 ≈ 1,157 A YEAR (OUR ARITHMETIC) · 1990 BASE CORVETTE $32,479")
sc("""The sources also disagree on when it debuted. The text says the ZR-1 appeared at the nineteen eighty-nine Geneva Motor Show and went on sale later that year, while the model-year table lists nineteen ninety as its introduction year. Both can be true: shown in nineteen eighty-nine, sold as a nineteen ninety model. We note the difference because it often confuses lists of Corvette dates.""",
   "Geneva Motor Show", "SHOWN AT GENEVA 1989 · SOLD AS A 1990 MODEL (WIKIPEDIA TEXT VS TABLE)")

ch("Thing two: each ZR1 was 'the fastest'")
sc("""Now the second fact. Every ZR1 since has been built to be the fastest Corvette of its time, and the numbers show how far that went. Wikipedia lists the sixth-generation ZR1, added for the two thousand nine model year, with a six point two litre supercharged L S nine V eight rated at six hundred thirty-eight horsepower and six hundred four pound-feet.""",
   "Chevrolet Corvette C6 ZR1", "C6 ZR1 (2009): 6.2 L SUPERCHARGED LS9 · 638 HP / 604 LB-FT")
sc("""Motor Trend, the page says, measured three point three seconds to sixty and an eleven point two second quarter mile at one hundred thirty point five miles per hour. The top speed of two hundred five miles per hour was what the car was engineered to reach, a design target, not a tested result. The internal project name was Blue Devil, reportedly after the chief executive's university, Duke.""",
   "Chevrolet Corvette C6 ZR1", "MOTOR TREND: 0–60 IN 3.3 S · 11.2 S AT 130.5 MPH · 205 MPH = DESIGN TARGET · CODENAME 'BLUE DEVIL'")
sc("""The seventh-generation ZR1, in the two thousand nineteen model year, raised the power to seven hundred fifty-five horsepower and seven hundred fifteen pound-feet from a supercharged six point two litre L T five. Wikipedia gives its top speed as two hundred fourteen point eight eight miles per hour with the low rear wing, though a cited source is titled two hundred twelve miles per hour official.""",
   "Chevrolet Corvette C7 ZR1", "C7 ZR1 (2019): 755 HP / 715 LB-FT · 214.88 MPH (TEXT) VS '212 MPH OFFICIAL' (CITED TITLE)")
sc("""Production of the C7 ZR1 in two thousand nineteen was two thousand, four hundred forty-one coupes and five hundred twelve convertibles, two thousand, nine hundred fifty-three in all. By our arithmetic, that is about eight and a half percent of the nineteen model year's thirty-four thousand, eight hundred twenty-two Corvettes, which matches the page.""",
   "Chevrolet Corvette C7 ZR1 production", "2019: 2,441 COUPES + 512 CONVERTIBLES = 2,953 ≈ 8.5% OF 34,822 CORVETTES")
sc("""Now the current car. Wikipedia says the C8 ZR1 has a five point five litre twin-turbocharged flat-plane crank V eight, the L T seven, rated at one thousand, sixty-four horsepower at seven thousand r p m and eight hundred twenty-eight pound-feet at six thousand. The page calls it the most powerful V eight Chevrolet has built. It is rear-wheel drive, with an eight-speed dual-clutch gearbox.""",
   "Chevrolet Corvette C8 ZR1 engine", "C8 ZR1: 5.5 L TWIN-TURBO FLAT-PLANE V8 · 1,064 HP · 828 LB-FT · 8-SPEED DCT · RWD")
sc("""Wikipedia says Chevrolet claims zero to sixty in two point five seconds, or two point three with the ZTK package, and a quarter mile of nine point seven seconds, or nine point six with ZTK at one hundred fifty-two miles per hour. Car and Driver, reported by The Drive, measured two point two seconds to sixty and nine point five at one hundred forty-nine miles per hour.""",
   "Chevrolet Corvette C8 ZR1 acceleration", "CLAIMED 2.5 S / 2.3 S (ZTK) · C&D MEASURED 2.2 S AND 9.5 S AT 149 MPH")
sc("""So the measured result beat the claim, by about a tenth, according to The Drive. The same page notes that the car was a stock one on factory Michelin Pilot Sport Cup two R tyres, and that the test details, such as the number of runs, were not given. We take it as a strong data point, not an official record. Wikipedia lists a top speed of two hundred thirty-three miles per hour, tested by GM's president, Mark Reuss.""",
   "Chevrolet Corvette C8 ZR1 test", "TOP SPEED 233 MPH (TESTED BY GM PRESIDENT MARK REUSS, PER WIKIPEDIA)")

ch("Five generations in one table")
sc("""Let us line the generations up, from our sources. Power: three seventy-five, four oh five, six thirty-eight, seven fifty-five, one thousand, sixty-four. By our arithmetic, the C8 ZR1 makes about two point eight times the power of the original C4 ZR-1, and about forty-one percent more than the C7 ZR1. The jump from the C7 to the C8 is bigger in percentage terms than the jump from C6 to C7, which was about eighteen percent.""",
   "Corvette ZR1 power", "375 → 405 → 638 → 755 → 1,064 HP · C8 ≈ 2.8× THE C4 (OUR ARITHMETIC)")
sc("""Zero to sixty. Car and Driver measured four point five for the first ZR-1, Motor Trend three point three for the C6, and Car and Driver two point two for the C8. Quarter mile: twelve point eight, eleven point two, nine point five. Different magazines, different decades, so we do not claim the comparison is exact. But the direction, and the size of the change, are plain.""",
   "Corvette ZR1 acceleration", "0–60: 4.5 → 3.3 → 2.2 S · QUARTER: 12.8 → 11.2 → 9.5 S (DIFFERENT TESTERS)")
sc("""Top speed. Road and Track recorded one hundred seventy-nine for the C4, the C6 was engineered for two hundred five, the C7 is listed at two hundred fourteen point nine or two hundred twelve, and the C8 at two hundred thirty-three. By our arithmetic, the C8 is about thirty percent faster than the first ZR-1, at least on these numbers. They mix measured, claimed and target figures, so we state that clearly.""",
   "Corvette ZR1 top speed", "179 (C4, MEASURED) · 205 (C6, TARGET) · 212–215 (C7) · 233 (C8, TESTED BY GM) MPH")
sc("""Weight did not fall. The first ZR-1 was about two hundred pounds heavier than a standard C4. The C6 ZR1 had a curb weight of three thousand, three hundred fifty pounds, the C7 three thousand, five hundred sixty, and the C8 three thousand, eight hundred thirty-one on Wikipedia's infobox, though the text gives a dry weight of three thousand, six hundred seventy. The cars got heavier as they got faster.""",
   "Corvette ZR1 weight", "C6 3,350 LB · C7 3,560 LB · C8 3,831 LB CURB (INFOBOX) / 3,670 LB DRY (TEXT)")
sc("""By our arithmetic, the C8 ZR1's infobox weight is about fourteen percent above the C6's, while its power is about sixty-seven percent higher. That is why the power-to-weight ratio improved so much. It is a reminder that raw horsepower is not the whole story; the engineers also had to make the extra power usable, with downforce, tyres and cooling.""",
   "Corvette ZR1 power to weight", "C8 vs C6: +14% WEIGHT, +67% POWER (OUR ARITHMETIC)")

ch("What changed in the C8")
sc("""The biggest change is the layout. Wikipedia says the C8 is GM's first rear mid-engine sports car since the Pontiac Fiero, and the first mid-engine Corvette. The coupe debuted on the eighteenth of July, twenty nineteen at the Kennedy Space Center. Development began around twenty sixteen, and the car was originally planned for the twenty eighteen model year before slipping to twenty nineteen and twenty twenty.""",
   "Chevrolet Corvette C8", "FIRST MID-ENGINE CORVETTE · DEBUT JULY 18, 2019 · KENNEDY SPACE CENTER")
sc("""Production began on the third of February, twenty twenty, after delays caused by the twenty nineteen G M strike, the page says. The twenty twenty base price was under sixty thousand dollars, and the twenty twenty-five base price was sixty-nine thousand, nine hundred ninety-five dollars for the coupe. The ZR1 arrived in spring twenty twenty-five, as the top of a range that includes the Z06, the E-Ray and the ZR1X.""",
   "Chevrolet Corvette C8 production", "PRODUCTION BEGAN FEB 3, 2020 · 2025 BASE COUPE $69,995 · ZR1 ARRIVED SPRING 2025")
sc("""The ZR1 sits above the Z06, which has a five point five litre naturally aspirated flat-plane V eight with six hundred seventy horsepower at eight thousand, four hundred r p m. By our arithmetic, the ZR1 makes about fifty-nine percent more power than the Z06, from the same displacement, using two turbochargers. Wikipedia lists a Nürburgring time of six fifty point seven six three for the ZR1, against seven eleven point eight two six for the Z06.""",
   "Chevrolet Corvette Z06 and ZR1", "Z06: 670 HP NA · ZR1: 1,064 HP TWIN-TURBO (+59%) · NÜRBURGRING 6:50.763 vs 7:11.826")
sc("""And above the ZR1 is the ZR1X, a hybrid with the same twin-turbo V eight plus an upgraded E-Ray electric motor on the front axle, for a combined one thousand, two hundred fifty horsepower and all-wheel drive. Wikipedia lists a Nürburgring time of six forty-nine point two seven five, and says it was later second to the Ford Mustang GTD Competition at six forty point eight, in April twenty twenty-six.""",
   "Chevrolet Corvette ZR1X", "ZR1X: 1,250 HP HYBRID AWD · NÜRBURGRING 6:49.275 · MUSTANG GTD COMPETITION 6:40.8 (APR 2026)")

ch("What it costs, and what it cost")
sc("""Prices show the same pattern. Wikipedia lists the C8 ZR1 at one hundred seventy-three thousand, three hundred dollars for the 1LZ coupe and one hundred eighty-four thousand, three hundred for the 3LZ coupe. Convertibles are one hundred eighty-four thousand, nine hundred ninety-five and one hundred ninety-six thousand, one hundred ninety-five. Other sources give one hundred seventy-four thousand, nine hundred ninety-five, including destination.""",
   "Chevrolet Corvette ZR1 price", "C8 ZR1: $173,300 (1LZ) · $184,300 (3LZ) · CONVERTIBLES $184,995 / $196,195 (WIKIPEDIA)")
sc("""Car and Driver, quoted by AOL, lists the previous ZR1, from two thousand nineteen, at one hundred nineteen thousand, nine hundred ninety-five dollars to start. By our arithmetic, the new car's one hundred seventy-four thousand, nine hundred ninety-five is about forty-six percent higher in nominal dollars. The same article lists the twenty twenty-five Z06 at one hundred sixteen thousand, nine hundred ninety-five.""",
   "Chevrolet Corvette C7 ZR1 price", "C7 ZR1 (2019): $119,995 → C8 ZR1: $174,995 = +46% NOMINAL (OUR ARITHMETIC)")
sc("""Compare that with the base car. Wikipedia lists the twenty twenty-five Corvette at sixty-nine thousand, nine hundred ninety-five dollars for the coupe. By our arithmetic, the cheapest ZR1, at one hundred seventy-three thousand, three hundred, costs about two and a half times the base car. The first ZR-1's premium over the base Corvette is not in our sources, so we cannot compare the multiples across generations.""",
   "Chevrolet Corvette C8", "ZR1 $173,300 ÷ BASE $69,995 ≈ 2.5× (OUR ARITHMETIC)")
sc("""Price is not the whole story, and our sources show prices vary widely. GM Authority reported dealer markups for the twenty twenty-five ZR1, including a listing at a Monterey, California, dealership with a window sticker of two hundred six thousand, eighty dollars and a one hundred thousand dollar markup, and a Midwest buyer who said the highest markup he saw was one hundred fifty thousand over sticker. Those are reports from a social media post and a forum.""",
   "Chevrolet dealership", "REPORTED MARKUPS: $50K–$150K OVER STICKER (GM AUTHORITY, FROM SOCIAL MEDIA AND REDDIT — UNVERIFIED)")
sc("""In December, GM Authority wrote that not all dealers were marking up. It listed a two thousand twenty-six ZR1 3LZ coupe in El Paso at one hundred ninety-nine thousand, eighty-five dollars, and a Michigan dealer advertising a 3LZ at two hundred twenty-five thousand, nine hundred fifteen with no added markup. It also said some dealers were listing new ZR1s at three hundred twenty to three hundred forty thousand dollars.""",
   "GM Authority", "DEC 2025: SOME DEALERS AT STICKER ($199,085 EL PASO) · OTHERS AT $320K–$340K")

ch("Why the ZR1 is rare")
sc("""The production tables show how few there are. Wikipedia lists one hundred eighty ZR1s for the twenty twenty-five model year, against eight thousand, eight hundred sixty-two Z06s and three thousand, one hundred fifty-three E-Rays. By our arithmetic, that means there were about forty-nine Z06s for every ZR1 built in that model year. The ZR1 arrived in spring, so the first year was short.""",
   "Chevrolet Corvette production", "MY2025: 180 ZR1 · 8,862 Z06 · 3,153 E-RAY → ~49 Z06 PER ZR1 (OUR ARITHMETIC)")
sc("""A caution on that table. In several years the total column on the page appears to equal the Stingray column alone, so we do not use the totals. We use only the model-specific figures, and we flag that the table as copied contains an inconsistency. If you know an official production number for the ZR1, a G M press release for instance, tell us in the comments.""",
   "Wikipedia production table", "THE TABLE'S TOTAL COLUMN IS UNRELIABLE · WE USE ONLY MODEL-SPECIFIC FIGURES")
sc("""One more fact on rarity: the page says ZR1 production and ordering began in spring twenty twenty-five, and the ZR1X came for the twenty twenty-six model year. By our arithmetic, a car launched in spring has only half a model year to build up, so one hundred eighty should not be taken as a yearly rate. Treat it as the length of the first, short run.""",
   "Chevrolet Corvette ZR1X", "ZR1 ORDERING SPRING 2025 · ZR1X IN MY2026 · 180 = A PARTIAL FIRST YEAR")

ch("The honest limits")
sc("""Now what our sources do not say. The Wikipedia page for the C8 does not give the ZR1's aerodynamic figures, brake sizes or tyre sizes. The C4 page does not give a ZR-1 price. The C6 page does not give a Nürburgring time. And the C8's price is quoted differently by different sources, which we will cover in the other videos of this series, so we do not repeat it here.""",
   "Chevrolet Corvette ZR1", "WHAT OUR SOURCES DO NOT SAY: AERO · BRAKES · TYRE SIZES · EARLY PRICES")
sc("""Also remember that some of these are claims, and some are measurements. The ZR1's two point five seconds is Chevrolet's claim, two point two is Car and Driver's measurement, and two hundred thirty-three miles per hour is a test run by the company's own president. The Fort Stockton records are FIA-verified, which is a different standard. We tried to label each, so you can weigh them.""",
   "Chevrolet Corvette ZR1", "CLAIM VS MEASUREMENT VS VERIFIED RECORD")

ch("Recap")
sc("""So, two things you may not have known. First, the original ZR-1's engine was designed by Lotus, which GM owned, and hand-assembled by Mercury Marine, the boat engine builder in Oklahoma, with one engine kept for a speedboat. Second, the ZR1 name started as an option taken by fifty-three buyers in three years, and each generation since has tried to be the fastest Corvette ever built.""",
   "Chevrolet Corvette ZR1", "1. LOTUS DESIGN + MERCURY MARINE ASSEMBLY · 2. FROM 53 PACKAGES TO A 1,064 HP HALO CAR")
sc("""Which ZR1 would you have chosen, the nineteen ninety King of the Hill or the current one? Tell us in the comments, with a source if you have one. In the other videos of this series, we compare the ZR1 with the Ferrari two ninety-six G T B, ask whether a normal person can afford one, and tell the story of America's fastest Corvette. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Chevrolet Corvette ZR1", "SUBSCRIBE: PICKUP REALITY")

save("video121", "2 Things You Didn't Know About the New Corvette ZR1", [
    "Wikipedia, Chevrolet Corvette (C8): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C8)",
    "Wikipedia, Chevrolet Corvette ZR1: https://en.wikipedia.org/wiki/Chevrolet_Corvette_ZR1",
    "Wikipedia, Chevrolet Corvette (C4): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C4)",
    "Wikipedia, Chevrolet Corvette (C6): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C6)",
    "Wikipedia, Chevrolet Corvette (C7): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C7)",
    "The Drive, A stock 2025 Corvette ZR1 has already beaten Chevy's official 0-60 time: https://www.thedrive.com/news/a-stock-2025-corvette-zr1-has-already-beaten-chevys-official-0-to-60-time.md",
], "A")
