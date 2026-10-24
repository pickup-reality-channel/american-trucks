import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""In twenty sixteen, Ferrari's chief executive Sergio Marchionne said that if Ferrari ever built an SUV, you would have to shoot him first. In September twenty twenty-two, Ferrari revealed the Purosangue, a four-door, four-seat car with a V twelve. Its chief executive asked people not to call it an SUV. This is the story of how the answer changed, and of what the sources do and do not say about why.""",
   "Ferrari Purosangue", "'YOU HAVE TO SHOOT ME FIRST' (2016) → PUROSANGUE (2022)")
sc("""We rely on Wikipedia, Autoevolution, Autocar, Autocar India, Drive dot com dot au, NBC, Bloomberg, Carscoops, Robb Report, Motor1 and Autohled. Several articles are undated, and some sources disagree on timing. Where they conflict, we show both. Where our sources are silent about a motive, we say so.""",
   "Ferrari history", "SOURCES: WIKIPEDIA · AUTOEVOLUTION · AUTOCAR · AUTOCAR INDIA · DRIVE.COM.AU · NBC · BLOOMBERG · CARSCOOPS · ROBB REPORT · MOTOR1 · AUTOHLED")

ch("The promise")
sc("""Start with the promise. Autoevolution recalls that in twenty sixteen Sergio Marchionne, then Ferrari's chief executive, was asked about an SUV. His answer, as the site quotes it, was that you would have to shoot him first. It is a blunt line, and it became the reference point for everything that followed.""",
   "Marchionne, 2016", "AUTOEVOLUTION: MARCHIONNE, 2016 — 'YOU HAVE TO SHOOT ME FIRST!'")
sc("""A later Ferrari executive, Enrico Galliera, gave the reasoning in plain words. As Autocar India reported, he said Ferrari was not producing an SUV, because an SUV is not a sports car. He also ruled out a four-door Ferrari at that time. And he said the GTC4Lusso was Ferrari's idea of an SUV.""",
   "Galliera's reasoning", "GALLIERA (AUTOCAR INDIA): 'WE ARE NOT PRODUCING AN SUV, BECAUSE AN SUV IS NOT A SPORTS CAR' · RULED OUT FOUR-DOOR · 'GTC4LUSSO IS OUR IDEA OF AN SUV'")
sc("""That last remark matters. The GTC4Lusso was a four-seat Ferrari shooting-brake with four-wheel drive. Wikipedia says the first test mule for the Purosangue was a GTC4Lusso body, spotted on the twenty-second of October twenty eighteen. So the car Ferrari held up as its answer to the SUV was also the car it used to test its first SUV.""",
   "GTC4Lusso", "WIKIPEDIA: PUROSANGUE TEST MULE BASED ON A GTC4LUSSO, SPOTTED 22 OCT 2018 · GTC4LUSSO = FERRARI'S 'IDEA OF AN SUV' (GALLIERA, AUTOCAR INDIA)")

ch("The first crack")
sc("""The first public crack came in July twenty seventeen. Autocar reported, in its piece of the fourth of August, that Marchionne had said an SUV would probably happen, but it would happen Ferrari style. The magazine stated the press conference was on the second of July. It also reported him saying that no decision had been made yet.""",
   "Marchionne, July 2017", "AUTOCAR, 4 AUG 2017 (PRESS CONFERENCE STATED AS 2 JULY 2017): 'WILL PROBABLY HAPPEN, BUT IT WILL HAPPEN FERRARI STYLE' · 'NO DECISION HAS BEEN MADE YET'")
sc("""In the same report, Autocar says an unnamed Ferrari spokesman insisted the company would not be launching an SUV. So within one news cycle, the chief executive said probably, and a spokesman said no. We cannot tell from our sources whether that was a communication problem or a deliberate signal.""",
   "Mixed messages", "AUTOCAR: UNNAMED SPOKESMAN SAID FERRARI 'WILL NOT BE LAUNCHING AN SUV' · SAME REPORT AS MARCHIONNE'S 'PROBABLY' · REASON FOR MIXED MESSAGE: NOT IN OUR SOURCES")
sc("""The press also began to guess at the shape. Analyst Max Warburton, as quoted in the articles we read, expected a Ferrari utility vehicle, which he called an FUV, priced around two hundred fifty thousand pounds, built at two to three thousand a year, with hidden rear doors. We use this only as a prediction. What actually arrived differed in price and in volume.""",
   "The FUV prediction", "ANALYST MAX WARBURTON (AS QUOTED): 'FUV', ~£250,000, 2,000–3,000/YEAR, HIDDEN REAR DOORS · A PREDICTION, NOT FERRARI'S PLAN")
sc("""By our arithmetic, a prediction of two to three thousand a year compares with Ferrari's own cap. Robb Report says the Purosangue is limited to twenty percent of output. Ferrari delivered thirteen thousand, six hundred forty cars in twenty twenty-five, according to Autohled, so twenty percent is at most twenty-seven twenty-eight. That is just inside the analyst's range.""",
   "Prediction vs cap", "WARBURTON 2,000–3,000/YEAR vs 20% × 13,640 (2025 DELIVERIES, AUTOHLED) = 2,728 MAX (OUR ARITHMETIC) · CAP FROM ROBB REPORT")

ch("The change of tone")
sc("""Then the tone shifted at the top. In articles from Drive dot com dot au and NBC, Marchionne spoke at a press event at the New York Stock Exchange. The reports say he told the audience Ferrari was dead serious about a new vehicle, which would be the only four-door Ferrari, in limited numbers. Both articles are undated in the copies we read, so we cannot place the event precisely.""",
   "The NYSE press event", "DRIVE.COM.AU / NBC: MARCHIONNE AT A NYSE PRESS EVENT — 'WE'RE DEAD SERIOUS ABOUT THIS' · ONLY FOUR-DOOR FERRARI · LIMITED NUMBERS · ARTICLES UNDATED IN OUR COPIES")
sc("""Bloomberg, as relayed in those reports, said it would take about thirty months to settle production details. He also drew a distinction between exclusivity and scarcity. Ferrari would keep numbers low, he suggested, so that the cars stayed desirable. That distinction explains the later twenty percent cap, but our sources do not link the two directly.""",
   "Exclusivity and scarcity", "BLOOMBERG (VIA ARTICLES): ~30 MONTHS TO SETTLE PRODUCTION DETAILS · MARCHIONNE: EXCLUSIVITY vs SCARCITY · LINK TO THE LATER 20% CAP: NOT STATED IN OUR SOURCES")
sc("""Wikipedia gives a date for the confirmation. It says the project was confirmed in September twenty eighteen, after Marchionne's hints, and that the car was code-named F one seven five. It also says development began in twenty seventeen. So by Wikipedia's account, the work was under way at the very time the company was telling reporters that no decision had been made.""",
   "Wikipedia's timeline", "WIKIPEDIA: CODE F175 · DEVELOPMENT BEGAN 2017 · CONFIRMED SEPT 2018 AFTER MARCHIONNE'S HINTS · NYSE ARTICLES UNDATED → CONFLICT ON CONFIRMATION DATE NOT RESOLVABLE")
sc("""We should be careful with that inference. A company can begin studies without a final decision. Wikipedia says development started in twenty seventeen, and Autocar quotes no decision in August twenty seventeen. Both can be true. What our sources do not tell us is when the decision was actually made, or by whom.""",
   "Careful with the inference", "DEVELOPMENT 2017 (WIKIPEDIA) AND 'NO DECISION YET' AUG 2017 (AUTOCAR) CAN BOTH BE TRUE · DATE AND AUTHOR OF THE DECISION: NOT IN OUR SOURCES")

ch("Why did it change?")
sc("""So why did the answer change? Reporters gave a market reason. In the articles we read, they noted that Bentley's Bentayga was rapidly becoming its top seller, that Aston Martin had shown its DBX concept in twenty fifteen, and that Lamborghini and Rolls-Royce were developing utility vehicles. They also noted that light trucks were about two thirds of American sales.""",
   "The market context", "ARTICLES (DRIVE.COM.AU / NBC): BENTAYGA BECOMING BENTLEY'S TOP SELLER · ASTON DBX CONCEPT 2015 · LAMBORGHINI + ROLLS-ROYCE DEVELOPING UTILITY VEHICLES · LIGHT TRUCKS ≈ 2/3 OF US SALES")
sc("""Note what that is. It is the reporters' context, not Ferrari's stated motive. Our sources contain no Ferrari document that says it built the Purosangue to follow rivals. What Ferrari said publicly was that it wanted a car with space for four, usable in daily life, that was still a Ferrari. Even that comes through press coverage, not a primary text.""",
   "Context is not motive", "MARKET CONTEXT = REPORTERS' FRAMING · FERRARI'S STATED MOTIVE: NOT FOUND IN A PRIMARY DOCUMENT IN OUR SOURCES")
sc("""The Rolls-Royce story offers a parallel. Wikipedia says Rolls-Royce's chief Torsten Müller-Ötvös said in twenty fifteen that the Cullinan would be revealed in twenty eighteen and on sale in twenty nineteen. Rolls named it in February twenty eighteen and showed it that May. Wikipedia adds that demand exceeded supply in twenty nineteen. It was a luxury brand moving first.""",
   "The Rolls-Royce parallel", "WIKIPEDIA (CULLINAN): 2015 ANNOUNCEMENT OF 2018 REVEAL · NAME CONFIRMED 13 FEB 2018 · UNVEILED MAY 2018 · 2019 DEMAND EXCEEDED SUPPLY")
sc("""Rolls-Royce is not a sports-car maker, which is the objection Galliera made about Ferrari. But Wikipedia calls the Cullinan the second best-selling Rolls-Royce ever. We have no sources comparing the sales effects, and we do not claim Ferrari followed Rolls. We only note that a luxury rival had already shown buyers would pay for a tall, four-door car.""",
   "What the parallel shows", "WIKIPEDIA: CULLINAN = 2ND BEST-SELLING ROLLS-ROYCE EVER · NO SOURCE CLAIMS FERRARI FOLLOWED ROLLS · LAUNCH PRICE ≈ $325,000")

ch("The reveal")
sc("""Now the reveal. Wikipedia says leaks surfaced in February twenty twenty-two, and Ferrari presented the Purosangue on the thirteenth of September twenty twenty-two, as a twenty twenty-three model. It shares the Roma's platform, according to Wikipedia. So the car is more than five years from the first hints to the unveiling, counting from July twenty seventeen.""",
   "The unveiling", "WIKIPEDIA: LEAKS FEB 2022 · REVEALED 13 SEPT 2022 AS MY2023 · SHARES ROMA PLATFORM · JULY 2017 → SEPT 2022 ≈ 5 YEARS 2 MONTHS (OUR ARITHMETIC)")
sc("""There is a pattern in that sentence. In twenty sixteen the promise was no SUV. In twenty twenty-two the delivery was a car Ferrari asked us not to call an SUV. The name Purosangue is Ferrari's own. We can describe this as a change of category on paper, with the underlying idea, a tall four-door car, kept.""",
   "A change of words", "2016: 'SHOOT ME FIRST' · 2022: 'PLEASE DON'T CALL IT AN SUV' · DESCRIPTION OF THE CAR: 4 DOORS, 4 SEATS (WIKIPEDIA)")
sc("""What did Ferrari put in it? Wikipedia lists a six point five litre naturally aspirated V twelve, seven hundred fifteen horsepower at seventy-seven fifty rpm, and five hundred twenty-eight pound-feet. There is an eight-speed dual-clutch gearbox and all-wheel drive. Ferrari claims zero to a hundred kilometres per hour in three point three seconds, and a top speed above three hundred ten.""",
   "What is in it", "WIKIPEDIA: 6.5 L F140 IA V12 · 715 HP @ 7,750 · 528 LB-FT @ 6,250 · 8-SPEED DCT (MAGNA) · AWD · 0–100 KM/H 3.3 S (FERRARI CLAIM) · TOP SPEED >310 KM/H")
sc("""Motor1's review adds details. It reports Multimatic dampers, no anti-roll bars, a weight distribution of forty-nine to fifty-one, and sixteen point seven cubic feet of cargo space. The reviewer estimated zero to sixty in three point two seconds. These are the features Ferrari could point to when it said the car was not a typical SUV.""",
   "Motor1's details", "MOTOR1 (SILVESTRO, 2 JULY 2024): MULTIMATIC TASV DAMPERS · NO SWAY BARS · 49/51 WEIGHT DISTRIBUTION · 16.7 CU FT CARGO · 0–60 3.2 S (ESTIMATED)")
sc("""Size gives the other side. Wikipedia lists the car at forty-nine seventy-three millimetres long, twenty twenty-eight wide and fifteen eighty-nine high, with a kerb weight of twenty-one seventy kilograms. By our arithmetic, that is about four thousand seven hundred eighty-four pounds, heavier than a typical sports coupe. Our sources do not compare it with a specific one.""",
   "Size and weight", "WIKIPEDIA: L 4,973 / W 2,028 / H 1,589 / WB 3,018 MM · 2,170 KG = 4,784 LB (OUR CONVERSION) · NO COUPE COMPARISON IN OUR SOURCES")

ch("The numbers after")
sc("""Demand was strong. Robb Report reports Ferrari closed the order book about two and a half months after the debut, with a wait of roughly two years. Carscoops, on the fifth of May twenty twenty-three, quoted Vigna saying Ferrari was caught by a positive surprise. That tells us the company did not claim to have predicted the level of demand.""",
   "The order book", "ROBB REPORT: BOOK CLOSED ~2.5 MONTHS AFTER DEBUT, ~2-YEAR WAIT · CARSCOOPS, 5 MAY 2023: VIGNA — 'CAUGHT BY A POSITIVE SURPRISE'")
sc("""Motor1's third-quarter twenty twenty-three coverage said order books covered all of twenty twenty-five, and that Vigna said the combustion engine still had a lot to do. Ferrari also said the Purosangue would be at most twenty percent of output. By our arithmetic, that is up to two thousand seven hundred twenty-eight of its thirteen thousand, six hundred forty cars in twenty twenty-five.""",
   "Cap and calendar", "MOTOR1 Q3 2023: ORDER BOOKS COVER ALL OF 2025 · VIGNA: 'ICE STILL HAS A LOT TO DO' · 20% × 13,640 = 2,728 (OUR ARITHMETIC; AUTOHLED)")
sc("""Prices rose with the model years. AOL listed the twenty twenty-four car at three hundred ninety-eight thousand, three hundred fifty dollars including destination. Motor1 listed the twenty twenty-five at four hundred twenty-three thousand, six hundred eighty-six. By our arithmetic, that is a rise of twenty-five thousand, three hundred thirty-six, or six point four percent, across two model years.""",
   "Price rises", "2024: $398,350 (AOL) → 2025: $423,686 (MOTOR1) = +$25,336 = +6.4% (OUR ARITHMETIC; BOTH INCLUDE DESTINATION PER SOURCES — NOT CHECKED FOR 2025)")
sc("""The second-hand story is mixed. Autoevolution reported a twenty twenty-three car with 7,574 miles failing to reach its reserve on Bring a Trailer, with a top bid of four hundred forty-three thousand, five hundred dollars against an original five hundred fifteen thousand, six hundred fifty-five. The one bid is a single car, not a trend.""",
   "Used market", "AUTOEVOLUTION, 8 JULY 2026: 2023 CAR, 7,574 MI, TOP BID $443,500 (BELOW RESERVE) vs $515,655 ORIGINAL (−14%, OUR ARITHMETIC) · ONE CAR, NOT A TREND")
sc("""Awards followed. Wikipedia says the Purosangue won the Compasso d'Oro in twenty twenty-four. The Italian design prize is not a sales number, and it says little about whether the promise was kept. We mention it because it shows Italian institutions treating the car as design, not as a controversy.""",
   "An award", "WIKIPEDIA: COMPASSO D'ORO 2024 · AN AWARD, NOT A SALES OR PROMISE METRIC · INSTITUTIONAL VIEW: NOT IN OUR SOURCES BEYOND THE AWARD")

ch("Legal side note")
sc("""There is one odd footnote. Wikipedia says a court ruled on the fifth of March twenty twenty-one in a trademark dispute with the Purosangue Foundation, a body unrelated to the car. We do not have the ruling's text or its result in our notes beyond that date. It shows that the name was contested before the car was shown.""",
   "A trademark footnote", "WIKIPEDIA: COURT, 5 MARCH 2021, TRADEMARK DISPUTE WITH THE PUROSANGUE FOUNDATION · RESULT AND TEXT: NOT IN OUR SOURCES")
sc("""Put the dates in a line. July twenty seventeen, a chief executive says it will probably happen Ferrari style. September twenty eighteen, Wikipedia says the project is confirmed. March twenty twenty-one, a court deals with the name. September twenty twenty-two, the reveal. Seventeenth of September twenty twenty-two, the request not to say SUV. Then an order book that closes in under three months.""",
   "Timeline", "JULY 2017 'PROBABLY HAPPEN' · SEPT 2018 CONFIRMED (WIKIPEDIA) · MAR 2021 TRADEMARK COURT · 13 SEPT 2022 REVEAL · 17 SEPT 2022 'PLEASE DON'T CALL IT AN SUV' · ORDER BOOK CLOSED ~2.5 MONTHS LATER")
sc("""One more number for scale. Marchionne said in twenty sixteen to shoot him first, and, as our notes record, he died about two years after that interview, before the car was shown. So the man who made the promise never saw it broken. Whether he would have approved of the final car is something none of our sources claim to know.""",
   "Marchionne did not see it", "MARCHIONNE DIED ABOUT 2 YEARS AFTER THE 2016 INTERVIEW (OUR NOTES) · CAR SHOWN SEPT 2022 · HIS VIEW OF THE FINAL CAR: NOT IN OUR SOURCES")

ch("Was the promise broken?")
sc("""So was the promise broken? It depends on what he promised. If it meant never a tall four-door Ferrari with four seats and a V twelve, then yes, by Wikipedia's description, it was broken. If it meant never a conventional SUV from a sports-car brand, Ferrari argues no, and says so in its choice of words. Both readings are defensible from our sources.""",
   "Two readings", "READING 1: NO TALL FOUR-DOOR FERRARI → BROKEN (WIKIPEDIA SPECS) · READING 2: NO CONVENTIONAL SUV → FERRARI'S ARGUMENT, 'PLEASE DON'T CALL IT AN SUV' (VIGNA)")
sc("""There is also what the executives said as they moved. Galliera said an SUV is not a sports car. Marchionne said it would be Ferrari style. Vigna said it is a Ferrari. Each statement defines the product by the brand, not by its shape. That is a consistent argument, even if it is not a satisfying answer for people who took the first promise literally.""",
   "A consistent argument", "GALLIERA (AUTOCAR INDIA) · MARCHIONNE (AUTOCAR 2017) · VIGNA (BLOOMBERG 2022): EACH DEFINES THE PRODUCT BY THE BRAND · OUR SUMMARY, NOT A FERRARI STATEMENT")
sc("""Look at the fuel numbers, too, since Ferrari's identity is partly about engines. The EPA rates the Purosangue at eleven miles per gallon in the city, fifteen on the highway, and twelve combined, according to Wikipedia. The Cullinan rates twelve, nineteen and fourteen, according to Autoblog for the twenty twenty-six model. Neither is economical, which is not the argument either car makes.""",
   "Fuel economy", "EPA 11/15/12 MPG PUROSANGUE (WIKIPEDIA) · CULLINAN 2026 12/19/14 MPG (AUTOBLOG)")
sc("""Vigna also told Motor1 that the combustion engine still had a lot to do. The Purosangue is a V twelve. Our sources do not say whether Ferrari has announced any electric model in this class, and we do not speculate. What they do show is that the promise was changed at the level of the product, while the engine tradition was kept.""",
   "The engine tradition", "MOTOR1 Q3 2023: VIGNA — ICE 'STILL HAS A LOT TO DO' · PUROSANGUE = V12 (WIKIPEDIA) · ELECTRIC MODELS IN THIS CLASS: NOT IN OUR SOURCES")


ch("Purosangue and Cullinan on paper")
sc("""Since the Rolls-Royce Cullinan is the car most often placed next to the Purosangue, compare them on paper. By Wikipedia's figures, the Ferrari makes seven hundred fifteen horsepower and the Cullinan five hundred sixty-three. By our arithmetic, the Ferrari has twenty-seven percent more power. The Cullinan has more torque, six hundred twenty-seven pound-feet against five hundred twenty-eight.""",
   "Power and torque", "WIKIPEDIA: FERRARI 715 HP / 528 LB-FT · CULLINAN 563 HP / 627 LB-FT · FERRARI +27.0% POWER, CULLINAN +18.8% TORQUE (OUR ARITHMETIC)")
sc("""Weight differs sharply. Wikipedia lists the Ferrari at twenty-one seventy kilograms and the Cullinan at twenty-six sixty. By our arithmetic, the Ferrari is four hundred ninety kilograms lighter, or eighteen point four percent. Autoblog puts the Cullinan at about sixty-one seventy-three pounds, close to Wikipedia's figure. Weight is one measurable way the Ferrari differs from the typical luxury utility vehicle.""",
   "Weight", "WIKIPEDIA: 2,170 KG vs 2,660 KG → 490 KG = 18.4% LIGHTER (OUR ARITHMETIC) · AUTOBLOG: CULLINAN ~6,173 LB")
sc("""Size follows the same pattern. The Ferrari is forty-nine seventy-three millimetres long and fifteen eighty-nine high. The Cullinan is fifty-three forty-one long and eighteen thirty-five high. By our arithmetic, the Ferrari is six point nine percent shorter and thirteen point four percent lower. It is a little wider, at twenty twenty-eight millimetres against two thousand.""",
   "Size", "WIKIPEDIA: FERRARI 4,973 L / 2,028 W / 1,589 H · CULLINAN 5,341 / 2,000 / 1,835 → −6.9% LENGTH, −13.4% HEIGHT, +28 MM WIDTH (OUR ARITHMETIC)")
sc("""The wheelbase is three thousand eighteen millimetres for the Ferrari and thirty-two ninety-five for the Cullinan. By our arithmetic, the Ferrari's is eight point four percent shorter. Cargo space is where the Rolls pulls ahead. Cars dot com lists twenty-one cubic feet for the Cullinan, and Motor1 lists sixteen point seven for the Ferrari. Different sources measure differently, so treat that as indicative.""",
   "Wheelbase and cargo", "WHEELBASE 3,018 vs 3,295 MM = −8.4% (OUR ARITHMETIC; WIKIPEDIA) · CARGO: CULLINAN 21 CU FT (CARS.COM) vs FERRARI 16.7 (MOTOR1) → +25.7% (OUR ARITHMETIC; SOURCES MAY MEASURE DIFFERENTLY)")
sc("""Rolls-Royce built its Cullinan to sit tall and comfortable. Ferrari built a car that, by Motor1's description, uses adaptive dampers and no anti-roll bars. We are not rating which is better. The point for this story is that Ferrari's engineering choices match its argument that the car is a Ferrari first, and a tall four-door second.""",
   "Two philosophies", "MOTOR1: MULTIMATIC TASV DAMPERS, NO SWAY BARS · CULLINAN: TALLER, HEAVIER, LONGER (WIKIPEDIA) · 'BETTER' NOT RATED")
sc("""The price history differs too. Wikipedia gives the Cullinan's launch price as about three hundred twenty-five thousand dollars. Autoblog lists the twenty twenty-six model at four hundred thirty-two thousand, three hundred fifty. By our arithmetic, that is thirty-three percent higher. The Purosangue's price rose six point three percent from the AOL twenty twenty-four figure to Cars dot com's twenty twenty-six figure.""",
   "Price over time", "CULLINAN: ~$325,000 LAUNCH (WIKIPEDIA) → $432,350 FOR 2026 (AUTOBLOG) = +33.0% · PUROSANGUE $398,350 (2024 AOL) → $423,636 (2026 CARS.COM) = +6.3% (OUR ARITHMETIC; DIFFERENT YEARS AND SOURCES)")
sc("""Demographics are a final point. The Drive reported in July twenty twenty-five that the average Rolls-Royce buyer is forty-two. We found no equivalent figure for the Purosangue's buyers. So we cannot say whether the Ferrari is reaching the same people as the Cullinan. Both brands, in our sources, say demand was strong.""",
   "Who buys", "THE DRIVE (JERRY PEREZ, 10 JULY 2025): AVERAGE ROLLS-ROYCE BUYER IS 42 · PUROSANGUE BUYER AGE: NOT IN OUR SOURCES")

ch("The same story by the calendar")
sc("""Lay the timeline on a calendar. By our arithmetic, from the 2016 shoot-me-first interview to the thirteenth of September twenty twenty-two reveal is about six years. From Wikipedia's September twenty eighteen confirmation to the reveal is four years. And from the order book opening to closing, on Robb Report's account, is about two and a half months.""",
   "Years and months", "2016 → 13 SEPT 2022 ≈ 6 YEARS · SEPT 2018 → SEPT 2022 = 4 YEARS · ORDER BOOK ~2.5 MONTHS ≈ 75 DAYS (OUR ARITHMETIC; WIKIPEDIA, ROBB REPORT)")
sc("""Rolls-Royce's timeline was shorter. Wikipedia says the Cullinan was announced in twenty fifteen for a twenty eighteen reveal, launched at Jackson Hole in the autumn of twenty eighteen, and updated as a Series Two in August twenty twenty-four. So from public announcement to launch was about three years, and a mid-life update about six years later.""",
   "Cullinan calendar", "WIKIPEDIA: 2015 ANNOUNCEMENT → MAY 2018 UNVEILING → AUTUMN 2018 LAUNCH (JACKSON HOLE) → SERIES II ANNOUNCED AUG 2024 · ~3 YEARS ANNOUNCEMENT-TO-LAUNCH (OUR ARITHMETIC)")
sc("""Ferrari's revenue gives context. Autohled's headline says Ferrari averaged five hundred twenty-four thousand euros in revenue for every car in twenty twenty-five. By our arithmetic, with thirteen thousand, six hundred forty deliveries, that is about seven billion euros. The figure includes more than car sales, so it is only a rough indicator of the scale Ferrari protects with its limited numbers.""",
   "Ferrari's scale", "AUTOHLED: ~€524,000 REVENUE PER CAR, 2025 · × 13,640 = ~€7.15 BILLION (OUR ARITHMETIC; REVENUE MAY INCLUDE NON-CAR ITEMS; BREAKDOWN NOT IN OUR NOTES)")
sc("""The twenty percent cap, again, is Ferrari's way of keeping its rule on numbers while adding a model. Robb Report says the cap applies to the Purosangue's share of output. Our sources do not say how Ferrari would respond if demand grew past it. Marchionne's distinction between exclusivity and scarcity is the only published reasoning we found.""",
   "The cap as policy", "ROBB REPORT: 20% CAP · MARCHIONNE: EXCLUSIVITY vs SCARCITY (ARTICLES) · FERRARI'S RESPONSE TO DEMAND ABOVE CAP: NOT IN OUR SOURCES")


ch("Options and special editions")
sc("""Both brands also sell personalisation. Motor1's review car was priced at five hundred six thousand, three hundred five dollars as tested, against a base of four hundred twenty-three thousand, six hundred eighty-six. By our arithmetic, that is nineteen and a half percent of extras. The Drive's Cullinan was four hundred five thousand base and five hundred seventy-two thousand, five hundred fifty as tested.""",
   "Options on both", "MOTOR1: PUROSANGUE $506,305 AS TESTED vs $423,686 BASE = +19.5% · THE DRIVE: CULLINAN $572,550 vs $405,000 = +41.4% (OUR ARITHMETIC; DIFFERENT YEARS)")
sc("""Special editions follow. Wikipedia says the Cullinan Blue Shadow was limited to sixty-two cars. Autoblog lists a Cullinan Yachting in four units and a Cyril Kongo Black Badge in five, for twenty twenty-seven. Ferrari's equivalent in our sources is the Tailor Made programme, with one car priced at eight hundred eighty-four thousand, six hundred forty-six dollars.""",
   "Limited editions", "WIKIPEDIA: CULLINAN BLUE SHADOW LIMITED TO 62 · AUTOBLOG 2027: CULLINAN YACHTING 4 UNITS, CYRIL KONGO BLACK BADGE 5 · YAHOO / MODERN CAR COLLECTOR: TAILOR MADE PUROSANGUE MSRP $884,646")
sc("""By our arithmetic, a limited Cullinan of four or five cars is a tiny fraction of the Purosangue's potential twenty-seven hundred a year. That contrast is the heart of Ferrari's argument about numbers. A model can be rare because it is built in a handful, or because a cap holds it below demand. Our sources show both strategies.""",
   "Two ways to be rare", "4–5 UNITS vs UP TO 2,728/YEAR → 0.15%–0.18% OF THE FERRARI CAP (OUR ARITHMETIC) · STRATEGIES: LIMITED RUN (ROLLS) vs CAP ON SHARE OF OUTPUT (FERRARI)")
sc("""Rolls-Royce also offers a Black Badge Cullinan. Wikipedia lists six hundred metric horsepower and six hundred sixty-four pound-feet. Autoblog lists its twenty twenty-seven price at five hundred four thousand, nine hundred fifty. By our arithmetic, that is sixty-nine thousand dollars above the standard twenty twenty-seven Cullinan. Ferrari's route to more performance, in this period, was not a separate trim in our sources.""",
   "Black Badge", "WIKIPEDIA: BLACK BADGE 600 PS / 664 LB-FT · AUTOBLOG 2027: $504,950 vs $435,950 = +$69,000 (OUR ARITHMETIC) · FERRARI PUROSANGUE TRIM LEVELS: NOT IN OUR SOURCES")

ch("What our sources do not say")
sc("""What is missing. The date of the actual decision to build the car. A Ferrari document stating the motive. The exact date of the New York press event. The result of the trademark case. How many Purosangues have been built so far. Without these, the story of why Ferrari broke its promise stays as reporters' context, plus the executives' own words.""",
   "Ferrari Purosangue", "NOT IN OUR SOURCES: DATE OF THE DECISION · FERRARI MOTIVE DOCUMENT · NYSE EVENT DATE · TRADEMARK RESULT · TOTAL PUROSANGUE PRODUCTION")
sc("""A claim we did not use: an article said around fifteen thousand Purosangues had been made. It does not give a source, and it does not match the cap of twenty percent of output. We leave it out. If you have a production figure from Ferrari, share it in the comments and we will update the description.""",
   "A claim we left out", "AUTOEVOLUTION ARTICLE: '~15,000 UNITS' — NO SOURCE GIVEN, NOT USED · CAP 20% OF ~13,640/YEAR (OUR ARITHMETIC: ≤ 2,728/YEAR) · PRODUCTION TOTAL: NOT IN OUR SOURCES")
sc("""Which do you think it is: a broken promise, or a smart change of words? Tell us in the comments. In the other videos of this series, we show two things you did not know about the Purosangue, compare it with the Cullinan, and ask whether a normal person can afford it. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ferrari Purosangue", "SUBSCRIBE: PICKUP REALITY")

save("video148", "Why Ferrari Swore It Would Never Build an SUV", [
    "Wikipedia, Ferrari Purosangue: https://en.wikipedia.org/wiki/Ferrari_Purosangue",
    "Wikipedia, Rolls-Royce Cullinan: https://en.wikipedia.org/wiki/Rolls-Royce_Cullinan",
    "Autoevolution, Marchionne 2016 interview coverage (you have to shoot me first)",
    "Autocar, 4 Aug 2017, Ferrari boss Sergio Marchionne on a Ferrari SUV",
    "Autocar India, Ferrari executives on an SUV (Galliera quote)",
    "Drive.com.au and NBC, Marchionne at the New York Stock Exchange press event (undated copies)",
    "Bloomberg via Autoevolution, 17 Sept 2022, Vigna on the word SUV",
    "Carscoops, 5 May 2023, Vigna: caught by a positive surprise",
    "Robb Report, Ferrari stops taking Purosangue orders because of high demand: https://robbreport.com/motors/cars/ferrari-temporarily-closes-purosangue-order-book-1234778214/",
    "Motor1, Ferrari says if you order a car today you won't get it until 2026: https://www.motor1.com/news/694830/ferrari-new-orders-fulfilled-2026/",
    "Motor1 (Brian Silvestro), Ferrari Purosangue review: https://www.motor1.com/reviews/725148/2025-ferrari-purosangue-review/",
    "AOL, 2024 Ferrari Purosangue will start at an eye-watering $398,350: https://www.aol.com/2024-ferrari-purosangue-start-eye-143900131.html",
    "autoevolution (Sergiu Tudose), used Ferrari Purosangue on Bring a Trailer: https://www.autoevolution.com/news/maserati-dealer-tries-to-sell-used-ferrari-purosangue-and-fails-they-can-forget-about-msrp-272537.html",
    "Autohled, Ferrari averaged 524 thousand euros in revenue for every car: https://www.autohled.cz/en/magazin/ferrari-utrzilo-v-prumeru-524-tisic-eur-za-kazde-auto-rekordni-rok-2025-ukazuje-silu-exkluzivity/9983",
    "Autoblog, 2026 Rolls-Royce Cullinan specs and fuel economy",
], "D")
