import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""In February two thousand three, a fire badly damaged the factory of a small Swedish carmaker, weeks before its big debut at the Geneva show. The company moved into a decommissioned fighter base, took over a jet hangar, and put the squadron's ghost on its cars. Here is the story of why Koenigsegg builds hypercars in a fighter-jet hangar, with every claim sourced.""",
   "Koenigsegg hangar", "WHY KOENIGSEGG BUILDS HYPERCARS IN A FIGHTER-JET HANGAR")
sc("""Our sources are Wikipedia's pages on Koenigsegg and on the Scania Wing, F ten, a SlashGear article about the ghost emblem, a Jalopnik factory tour, AOL's March twenty twenty-six report on the Gemera, and the RM Sotheby's catalogue for a Regera. Where they disagree, we show both. Our own arithmetic is labelled.""",
   "Sources", "SOURCES: WIKIPEDIA (KOENIGSEGG; SCANIA WING F 10) · SLASHGEAR · JALOPNIK TOUR · AOL (30 MAR 2026) · RM SOTHEBY'S · DISAGREEMENTS SHOWN · OUR ARITHMETIC LABELLED")

ch("A young founder")
sc("""The company was founded in nineteen ninety-four by Christian von Koenigsegg. Wikipedia says he was twenty-two and raised sixty million Swedish kronor from investors. It began in Olofström, and moved to Ängelholm in the early two-thousands. By our arithmetic, that is nine years from founding to the fire that changed its home.""",
   "Founded 1994", "WIKIPEDIA: FOUNDED 1994 · CHRISTIAN von KOENIGSEGG, AGE 22 · KR 60,000,000 FROM INVESTORS · OLOFSTRÖM → ÄNGELHOLM EARLY 2000s · 1994 → 2003 = 9 YEARS (OUR ARITHMETIC)")
sc("""The first production car was the CC8S, which Wikipedia dates to two thousand two. It was followed by the CCR in two thousand four, with fourteen built, the CCX in two thousand six, and the CCXR in two thousand seven. So the company in two thousand three was a small maker with one car on sale and a Geneva debut coming.""",
   "The early cars", "WIKIPEDIA: CC8S (2002) · CCR (2004, 14 BUILT) · CCX (2006) · CCXR (2007) · 2003 SITUATION = OUR SUMMARY OF THESE DATES")
sc("""By two thousand eight, Wikipedia reports, the staff numbered forty-five, and the company produced eighteen cars at an average price of about one million dollars. By our arithmetic, that is roughly eighteen million dollars of cars a year, built by forty-five people. It was a tiny operation compared with big carmakers, and it still is.""",
   "How small", "WIKIPEDIA: 2008 STAFF 45; 18 CARS AT AVERAGE ~$1 M · 18 × $1 M = ~$18 M (OUR ARITHMETIC) · COMPARISON WITH BIG CARMAKERS = GENERAL KNOWLEDGE, NO FIGURE IN OUR SOURCES")

ch("The fire")
sc("""Now the fire. Wikipedia says that on the twenty-second of February two thousand three, a fire badly damaged one of the company's facilities. SlashGear adds that it happened at the Margretetorp factory, a protected thatched heritage building, only weeks before the CC8S was due to debut at the Geneva motor show.""",
   "22 February 2003", "WIKIPEDIA: FIRE 22 FEB 2003 BADLY DAMAGED A FACILITY · SLASHGEAR: MARGRETETORP FACTORY, PROTECTED THATCHED HERITAGE BUILDING, WEEKS BEFORE THE CC8S GENEVA DEBUT")
sc("""Jalopnik's factory tour says the original factory burned on a weekend, and that staff managed to salvage cars and machinery. It does not give a date, a cause or an insurance figure, and neither do the other sources we found. So we know that a fire happened, when, and where, but not why or what it cost.""",
   "What was saved", "JALOPNIK TOUR (UNDATED): FACTORY BURNED ON A WEEKEND; STAFF SALVAGED CARS AND MACHINERY · CAUSE / COST / INSURANCE: NOT IN OUR SOURCES")
sc("""The sources also differ slightly in emphasis. Wikipedia calls it a fire that badly damaged a facility. SlashGear describes the loss of the heritage factory. Jalopnik says the original factory burned. We read these as the same event, but we cannot rule out that different buildings are being described. We flag that and move on.""",
   "Three descriptions", "WIKIPEDIA: 'A FACILITY' · SLASHGEAR: MARGRETETORP FACTORY · JALOPNIK: 'THE ORIGINAL FACTORY' → SAME EVENT = OUR READING; NOT CONFIRMED BY ANY SOURCE")
sc("""A fire weeks before a debut sounds fatal. But the sources say the Geneva show went ahead. SlashGear reports the company moved to a decommissioned air base, and the squadron's motto, The Show Must Go On, became part of the story. We could not find a source that says whether the CC8S was shown on schedule, so we do not claim it.""",
   "The show", "SLASHGEAR: COMPANY MOVED TO A DECOMMISSIONING AIR BASE; SQUADRON MOTTO 'THE SHOW MUST GO ON' · WHETHER THE CC8S APPEARED AT GENEVA ON SCHEDULE: NOT STATED IN OUR SOURCES")

ch("The air base")
sc("""The base was the Scania Wing, F ten, near Ängelholm. Wikipedia's page on the wing gives its history from nineteen forty to two thousand two. It says a decommissioning ceremony took place on the twentieth of December two thousand two, and that the wing was disbanded on the thirty-first of December. By our arithmetic, the base was disbanded only about seven weeks before the Koenigsegg fire.""",
   "The Scania Wing", "WIKIPEDIA (SCANIA WING, F 10): HISTORY 1940–2002 · DECOMMISSIONING CEREMONY 20 DEC 2002 · DISBANDED 31 DEC 2002 · 31 DEC 2002 → 22 FEB 2003 ≈ 7 WEEKS (OUR ARITHMETIC)")
sc("""That gap matters. From the thirty-first of December two thousand two to the twenty-second of February two thousand three is fifty-three days, by our arithmetic, just under eight weeks. The hangars had been empty for less than two months when the fire struck. Our sources do not say how the company found or leased the space, so we do not claim a deal.""",
   "Fifty-three days", "31 DEC 2002 → 22 FEB 2003 = 53 DAYS ≈ 7.6 WEEKS (OUR ARITHMETIC) · HOW THE SPACE WAS OBTAINED: NOT IN OUR SOURCES")
sc("""Wikipedia's article on the wing says that in two thousand three some buildings on the site were demolished, including the special Gripen hangar. It also says that Koenigsegg has factories and offices in former F ten buildings. So the site was being cleared in parts and reused in others, and the carmaker became one of the reusers.""",
   "What happened to the site", "WIKIPEDIA (SCANIA WING): 2003 — SOME BUILDINGS DEMOLISHED, INCLUDING THE SPECIAL GRIPEN HANGAR · KOENIGSEGG HAS FACTORIES AND OFFICES IN FORMER F 10 BUILDINGS")
sc("""The Koenigsegg page on Wikipedia gives the company side. After the fire, it says, the company took over an abandoned air field. In late two thousand three, one of two fighter-jet hangars and an office building became the factory. The page says the squadron's ghost symbol was adopted as a tribute. It does not give a floor area.""",
   "The company's account", "WIKIPEDIA (KOENIGSEGG): AFTER THE 2003 FIRE — ABANDONED AIR FIELD; LATE 2003 — ONE OF TWO FIGHTER-JET HANGARS + AN OFFICE BUILDING BECAME THE FACTORY · GHOST SYMBOL ADOPTED AS A TRIBUTE · FLOOR AREA: NOT STATED")
sc("""One small mismatch. Wikipedia says the company took one of two fighter-jet hangars. The Scania Wing page, as we read it, mentions the special Gripen hangar being demolished, but does not say which of the hangars Koenigsegg occupies. So we cannot say whether the demolished hangar and the one Koenigsegg uses are related. Our sources are silent on it.""",
   "Which hangar?", "WIKIPEDIA (KOENIGSEGG): 'ONE OF TWO' HANGARS · WIKIPEDIA (SCANIA WING): GRIPEN HANGAR DEMOLISHED 2003 · RELATIONSHIP BETWEEN THE TWO: NOT STATED IN OUR SOURCES")

ch("The ghost")
sc("""Now the ghost. SlashGear says the squadron based there, the Johan Röd squadron, was formed in November nineteen forty and nicknamed the Ghost Squadron. When Koenigsegg moved in, the pilots asked for the ghost emblem to appear on the cars. The squadron's motto, according to the article, was The Show Must Go On.""",
   "The Ghost Squadron", "SLASHGEAR: JOHAN RÖD SQUADRON FORMED NOV 1940, NICKNAMED 'GHOST SQUADRON' · PILOTS ASKED FOR THE GHOST EMBLEM ON THE CARS · MOTTO 'THE SHOW MUST GO ON'")
sc("""Where is the ghost on the car? SlashGear says it is on the rear hood. Jalopnik's tour says it is on the rear window. Both are sources we trust for the story, and both cannot be exactly right for the same car. Cars from different years may differ, and we have no photograph in our sources, so we show the disagreement.""",
   "Where is it?", "SLASHGEAR: GHOST ON THE REAR HOOD · JALOPNIK: GHOST ON THE REAR WINDOW → DISAGREEMENT; DIFFERENT MODELS / YEARS POSSIBLE; NO IMAGE IN OUR SOURCES TO SETTLE IT")
sc("""Wikipedia's Gemera page lists an optional Ghost package, and the Koenigsegg page says the ghost symbol was adopted as a tribute. Whether the Ghost package takes its name from the squadron is not stated in our sources. It would be natural to assume so, but we mark that as our inference, not a documented fact.""",
   "Ghost package", "WIKIPEDIA (GEMERA): OPTIONAL GHOST PACKAGE, CONTENTS NOT DESCRIBED · WIKIPEDIA (KOENIGSEGG): GHOST SYMBOL ADOPTED AS A TRIBUTE · LINK BETWEEN THE PACKAGE NAME AND THE SQUADRON: OUR INFERENCE, NOT IN SOURCES")

ch("Inside the factory")
sc("""What is inside? Jalopnik's tour, which is undated and appears to date from the Agera or One:1 era, says all the carbon work and wheels are made in-house. It says storage holds a full ten percent of the total Koenigsegg production, plus one Lamborghini Gallardo. And it says the detailer spends fifty hours on each car.""",
   "The tour", "JALOPNIK TOUR (UNDATED): CARBON WORK AND WHEELS MADE IN-HOUSE · STORAGE HOLDS 'A FULL TEN PERCENT OF THE TOTAL KOENIGSEGG PRODUCTION' PLUS ONE GALLARDO · DETAILER ~50 HOURS PER CAR")
sc("""By our arithmetic, fifty hours of detailing is more than a full working week at forty hours, plus ten hours. On a hypothetical run of eighteen cars a year, the number Wikipedia gives for two thousand eight, that would be nine hundred hours of detailing. Those two facts come from different years, so this is only an illustration of scale.""",
   "Detailing hours", "50 HR PER CAR · 18 CARS × 50 = 900 HR (OUR ARITHMETIC; COMBINES JALOPNIK'S UNDATED FIGURE WITH WIKIPEDIA'S 2008 OUTPUT — ILLUSTRATIVE ONLY)")
sc("""The tour does not state the facility's size, its staff count or its production rate. We looked. Those figures are not in the Jalopnik piece, and the SlashGear article does not give them either. Wikipedia gives staff numbers: just under eight hundred at the end of twenty twenty-three. So any statement of the factory area would be our invention, and we will not make one.""",
   "What the tour omits", "JALOPNIK TOUR: FACILITY SIZE, STAFF COUNT, PRODUCTION RATE — NOT STATED · WIKIPEDIA: JUST UNDER 800 STAFF AT END-2023 · FACTORY AREA: NOT IN OUR SOURCES")

ch("From hangar to a bigger factory")
sc("""The hangar story does not end there. Wikipedia says that in July twenty twenty-three a new factory opened, doubling the company's capacity. By our arithmetic, that is twenty years after the move into the base. The page does not say whether production left the hangar or whether both sites are used together, so we cannot say.""",
   "A new factory", "WIKIPEDIA: NEW FACTORY OPENED JULY 2023, DOUBLING CAPACITY · LATE 2003 → JULY 2023 ≈ 20 YEARS (OUR ARITHMETIC) · WHETHER THE HANGAR IS STILL USED: NOT STATED")
sc("""Staffing tells the growth story. Forty-five people in two thousand eight, just under eight hundred at the end of twenty twenty-three, by Wikipedia's count. By our arithmetic, that is a seventeen-fold increase in fifteen years. Wikipedia's introduction also mentions about eight hundred fifty staff, without a date, so we use the dated figure.""",
   "Growth", "WIKIPEDIA: 45 (2008) → JUST UNDER 800 (END-2023) · INTRODUCTION: ~850 (UNDATED) · 800 ÷ 45 ≈ 17.8× (OUR ARITHMETIC)")
sc("""The 2023 factory opening came just as the company launched its new models. Wikipedia lists the Jesko, the Gemera and the CC850 in the twenty twenty-six line-up. The CC850 won a Top Gear innovation award in twenty twenty-three for its ESS shift system. AOL reports the Gemera is being built alongside the CC850, with Sadair's Spear to follow.""",
   "Building today", "WIKIPEDIA: 2026 LINE-UP — JESKO, GEMERA, CC850 · CC850 TOP GEAR INNOVATION AWARD 2023 (ESS SHIFT SYSTEM) · AOL (30 MAR 2026): GEMERA BUILT ALONGSIDE CC850; SADAIR'S SPEAR TO JOIN")

ch("Survival")
sc("""The company's money story is also one of near misses. Wikipedia says Koenigsegg signed a letter of intent in June two thousand nine to buy Saab, backed by six hundred million dollars from the European Investment Bank, and withdrew in November. A Chinese company, BAIC, took a minority stake that year.""",
   "The Saab bid", "WIKIPEDIA: SAAB LETTER OF INTENT JUNE 2009 ($600 M FROM THE EUROPEAN INVESTMENT BANK), WITHDRAWN NOV 2009 · BAIC MINORITY STAKE 2009")
sc("""In January twenty nineteen, twenty percent of the company was sold to NEVS for one hundred seventy-one million dollars, and the company bought that stake back in twenty twenty-one, according to Wikipedia. By our arithmetic, the price implies eight hundred fifty-five million dollars for the whole, assuming the numbers are exact. The page does not state a valuation.""",
   "NEVS", "WIKIPEDIA: 20% SOLD TO NEVS FOR $171 M (JAN 2019); STAKE BOUGHT BACK 2021 · $171 M ÷ 0.20 = $855 M (OUR ARITHMETIC; ROUNDED INPUTS) · VALUATION: NOT STATED")
sc("""Records helped the company's profile. Wikipedia lists the CCR at three hundred eighty-seven point eight six six kilometres per hour at Nardò in two thousand five, and the Agera RS at four hundred forty-seven point one nine average and four hundred fifty-seven point nine four instrumented at Pahrump in two thousand seventeen. The Jesko Attack lapped Laguna Seca in one twenty-four eighty-six in August twenty twenty-four.""",
   "Records", "WIKIPEDIA: CCR 387.866 KM/H (28 FEB 2005, NARDÒ) · AGERA RS 447.19 AVG / 457.94 INSTRUMENTED (4 NOV 2017, PAHRUMP) · JESKO ATTACK LAGUNA SECA 1:24.86 (18 AUG 2024)")

ch("The timeline in one place")
sc("""Let us line up the dates, all from our sources. Nineteen forty: the squadron is formed. Nineteen ninety-four: Koenigsegg is founded. Two thousand two: the base is decommissioned and disbanded in December. February two thousand three: the fire. Late two thousand three: a hangar and an office building become the factory. July twenty twenty-three: a new factory opens.""",
   "Timeline", "SLASHGEAR + WIKIPEDIA: 1940 SQUADRON FORMED (NOV) · 1994 FOUNDING · 20/31 DEC 2002 DECOMMISSIONING / DISBANDING · 22 FEB 2003 FIRE · LATE 2003 HANGAR BECOMES FACTORY · JULY 2023 NEW FACTORY")
sc("""By our arithmetic, the squadron's life ran from November nineteen forty to December two thousand two, which is about sixty-two years. Koenigsegg's own life, from nineteen ninety-four to this year, is about thirty-two. The carmaker has therefore been in the former fighter base for roughly twenty-three of its thirty-two years, if the move is dated to late two thousand three.""",
   "Years", "NOV 1940 → DEC 2002 ≈ 62 YEARS · 1994 → 2026 = 32 YEARS · LATE 2003 → 2026 ≈ 23 YEARS (OUR ARITHMETIC; 2026 = THE CURRENT YEAR) · SQUADRON AND WING ARE NOT THE SAME THING — SEE SOURCES")
sc("""One caution about that first date. SlashGear dates the squadron's formation to November nineteen forty, while Wikipedia's page on the wing gives a history from nineteen forty. These fit together, but the squadron and the wing are not the same unit, and we do not claim that the ghost nickname covered the whole base for the whole period.""",
   "Squadron vs wing", "SLASHGEAR: JOHAN RÖD SQUADRON FORMED NOV 1940 · WIKIPEDIA (SCANIA WING): HISTORY 1940–2002 · SQUADRON vs WING: DIFFERENT UNITS — NICKNAME SCOPE NOT STATED")
sc("""How many cars were built in those early years? Our sources give two data points: fourteen CCRs, and eighteen cars in two thousand eight. By our arithmetic, that is a combined 32 cars across two data points, from a company that was then still in its first decade of production.""",
   "Tiny volumes", "WIKIPEDIA: CCR — 14 BUILT · 2008 — 18 CARS · 14 + 18 = 32 (OUR ARITHMETIC; DIFFERENT YEARS AND MODELS, NOT A TOTAL OUTPUT)")

ch("Cars that came out of the hangar")
sc("""Which cars were built there? Wikipedia's model list gives dates, not factory locations. It lists the CCR in two thousand four, the CCX in two thousand six, the CCXR in two thousand seven, the Trevita with three planned and two finished, the Agera ending in July twenty eighteen, the Regera from twenty fifteen, and the Jesko, Gemera and CC850. Which were built in the hangar is not stated.""",
   "Models", "WIKIPEDIA MODEL LIST: CCR 2004 · CCX 2006 · CCXR 2007 · TREVITA (3 PLANNED, 2 FINISHED) · AGERA (ENDED JULY 2018) · REGERA 2015 · JESKO · GEMERA · CC850 · WHICH WERE BUILT IN THE HANGAR: NOT STATED")
sc("""The Regera is the best documented. Wikipedia says eighty or eighty-five were built between March twenty sixteen and twenty twenty-two, with the page giving both figures. The RM Sotheby's catalogue says eighty-five. By our arithmetic, that is a production run of six years, or about fourteen cars a year if we take eighty-five.""",
   "Regera run", "WIKIPEDIA: REGERA 80 (INFOBOX) / 85 (TEXT) BUILT, MARCH 2016–2022 · RM SOTHEBY'S: 85 · 85 ÷ 6 ≈ 14 CARS/YEAR (OUR ARITHMETIC; ASSUMES 6 FULL YEARS)")
sc("""The Agera RS set speed records, according to Wikipedia: four hundred forty-seven point one nine kilometres per hour on average in November twenty seventeen. The Agera ended in July twenty eighteen. Wikipedia also records the Agera RS at zero to four hundred to zero in thirty-three point two nine seconds, the same month. Those are performance claims, not statements about the factory.""",
   "The Agera RS", "WIKIPEDIA: AGERA RS 447.19 KM/H AVG (4 NOV 2017) · 0–400–0 33.29 S (NOV 2017) · AGERA ENDED JULY 2018")
sc("""The Regera then took the zero to four hundred to zero record, with thirty-one point four nine seconds in September twenty nineteen and twenty-eight point eight one in June twenty twenty-three. By our arithmetic, the Regera beat the Agera RS's thirty-three point two nine by one point eight seconds in two thousand nineteen, and by four point four eight in two thousand twenty-three.""",
   "Records trade hands", "WIKIPEDIA: REGERA 31.49 S (23 SEP 2019) AND 28.81 S (16 JUN 2023) vs AGERA RS 33.29 S · 33.29 − 31.49 = 1.80 S; 33.29 − 28.81 = 4.48 S (OUR ARITHMETIC)")

ch("The people")
sc("""A few numbers about the people. Wikipedia says the company had forty-five staff in two thousand eight and just under eight hundred at the end of twenty twenty-three. It does not break down how many work in the hangar, and Jalopnik's tour does not give a headcount. So we know the company's total, not the hangar's.""",
   "Staff", "WIKIPEDIA: 45 (2008); JUST UNDER 800 (END-2023) · HEADCOUNT IN THE HANGAR: NOT IN OUR SOURCES")
sc("""Jalopnik says the detailer spends fifty hours on a car. By our arithmetic, at forty hours a week, that is one and a quarter weeks of work per car for one person. The tour does not say how many detailers there are or how they are paid. It also does not say whether that figure still applies to the Gemera.""",
   "Fifty hours", "50 HR ÷ 40 HR/WEEK = 1.25 WEEKS (OUR ARITHMETIC) · NUMBER OF DETAILERS / APPLIES TO GEMERA: NOT IN OUR SOURCES")
sc("""The founder appears in the sources mostly through quotes about products. InsideHook quotes him saying there were so few customers left asking for a three-cylinder Gemera, and that the company persuaded the holdouts to take the V8. That is a glimpse of how the company talks to its customers, though it says nothing about the hangar.""",
   "The founder", "INSIDEHOOK (29 JULY 2024): von KOENIGSEGG — 'THERE WERE SO FEW LEFT THAT ASKED FOR A THREE-CYLINDER' · COMPANY PERSUADED HOLDOUTS TO CHOOSE THE V8 · HANGAR COMMENTS: NONE IN THIS SOURCE")

ch("Today")
sc("""Today the hangar's tenant makes a four-seat grand tourer. AOL reports on the thirtieth of March twenty twenty-six that the Gemera is in production after six years, limited to three hundred, with all of them spoken for. By our arithmetic, that is three hundred cars from a company that once built eighteen a year, which would take sixteen years at the two thousand eight rate.""",
   "Gemera", "AOL (30 MAR 2026): GEMERA IN PRODUCTION; LIMITED TO 300; ALL SPOKEN FOR · 300 ÷ 18 = 16.7 YEARS AT 2008 RATE (OUR ARITHMETIC; RATES HAVE CHANGED — NEW FACTORY DOUBLED CAPACITY IN 2023)")
sc("""The new factory doubled capacity, Wikipedia says, so the output is higher now. How much higher is not stated. Neither is the Gemera's build rate. We can say that the company has grown from a hangar and an office building to a plant that, in Wikipedia's words, doubled its capacity in July twenty twenty-three, and that is the extent of the numbers.""",
   "Capacity", "WIKIPEDIA: JULY 2023 NEW FACTORY DOUBLED CAPACITY · CURRENT OUTPUT / GEMERA BUILD RATE: NOT IN OUR SOURCES")
sc("""Prices rose with the ambition. Wikipedia gives an average price of about one million dollars in two thousand eight. Motor1 reports the Gemera starting at one point seven million in twenty twenty. By our arithmetic, that is seventy percent higher, without adjusting for inflation, which our sources do not provide. The fire, the base and the ghost are the origin story of that climb.""",
   "Prices", "WIKIPEDIA: 2008 AVERAGE ~$1 M · MOTOR1 (13 APR 2020): GEMERA FROM $1.7 M · +70% (OUR ARITHMETIC; NOT INFLATION-ADJUSTED) · 'ORIGIN STORY OF THAT CLIMB' = OUR FRAMING")

ch("Three versions of the same story")
sc("""There are three tellers of this story in our sources, and each stresses something different. Wikipedia gives the dates and the bare facts. SlashGear tells the tale of the heritage building, the squadron and its motto. Jalopnik walks through the shop floor. Reading them together gives a fuller picture, and also shows where each leaves gaps.""",
   "Three tellers", "WIKIPEDIA: DATES AND FACTS · SLASHGEAR: HERITAGE BUILDING, SQUADRON, MOTTO · JALOPNIK: SHOP-FLOOR DETAILS (UNDATED) · COMPARISON = OUR SYNTHESIS")
sc("""Where they agree: a fire damaged or destroyed the original factory, and the company moved to the former air base, adopting the ghost. Where they differ: the position of the ghost on the car, the level of detail about the buildings, and whether the hangar is described as one of two. None of them gives the cost of the fire or the move.""",
   "Agreement", "AGREE: FIRE → MOVE TO FORMER AIR BASE → GHOST EMBLEM · DIFFER: GHOST POSITION (REAR HOOD vs REAR WINDOW); BUILDING DETAIL · COST OF FIRE / MOVE: NOT IN ANY OF OUR SOURCES")
sc("""The dating of the sources matters. The Wikipedia pages are current encyclopedia entries, with dated entries through twenty twenty-four and a twenty twenty-six mention of the lineup. SlashGear's article is not dated in our copy. Jalopnik's tour is undated and refers to cars from the Agera era. So the freshest facts about the factory come from Wikipedia and AOL.""",
   "How fresh", "WIKIPEDIA: ENTRIES THROUGH 2024; 2026 LINE-UP · SLASHGEAR: UNDATED IN OUR COPY · JALOPNIK: UNDATED, AGERA/ONE:1 ERA · AOL: 30 MAR 2026")
sc("""One practical point for anyone planning a visit. None of our sources says whether the factory offers public tours. The Jalopnik piece describes a tour, but that appears to be a press visit, and we do not know the conditions. If you want to visit, check Koenigsegg's own website. We have not verified any current visiting policy.""",
   "Visiting", "JALOPNIK: DESCRIBES A TOUR (PRESS VISIT, CONDITIONS NOT STATED) · PUBLIC TOUR POLICY: NOT IN OUR SOURCES · KOENIGSEGG WEBSITE: NOT CHECKED")
sc("""By our arithmetic, the whole arc spans sixty-three years from the squadron's founding in November nineteen forty to the carmaker's move in late two thousand three. Eighty-six years separate the squadron's founding from this year. In that time, the same site has gone from jet fighters to carbon-fibre hypercars, which is why the story keeps being retold.""",
   "A long arc", "NOV 1940 → LATE 2003 ≈ 63 YEARS · 1940 → 2026 = 86 YEARS (OUR ARITHMETIC) · 'KEEPS BEING RETOLD' = OUR OBSERVATION; THREE OF OUR SOURCES TELL IT")
sc("""The lesson, if there is one, is that companies are shaped by what happens to them as much as by what they plan. A fire forced a move. A closing base provided the space. A squadron gave a symbol. None of that was in a business plan we can see. What the company did next, build faster and stranger cars, is documented, and we have shown the numbers.""",
   "The lesson", "'SHAPED BY WHAT HAPPENS TO THEM' = OUR EDITORIAL READING · BUSINESS PLAN: NOT IN OUR SOURCES · LATER CARS: WIKIPEDIA MODEL LIST")

ch("Why a hangar?")
sc("""So why a fighter-jet hangar? The sources give a chain of events, not a stated strategy. A fire destroyed the old factory. A nearby base had just closed. The company moved in. Nowhere in our sources does Christian von Koenigsegg say the hangar was a deliberate choice, and none of them gives a rent or purchase price. The answer is circumstance.""",
   "The honest answer", "CHAIN OF EVENTS FROM WIKIPEDIA + SLASHGEAR · FOUNDER'S OWN STATEMENT ON THE CHOICE: NOT IN OUR SOURCES · RENT / PURCHASE PRICE: NOT IN OUR SOURCES · 'CIRCUMSTANCE' = OUR READING")
sc("""There are practical reasons a hangar could suit a carmaker, such as large open floors and a doorway wide enough for aircraft. That is our inference, not a documented reason, and none of our sources list the hangar's dimensions. We mention it only because a reader will wonder, and we want to be clear about which parts are fact and which are guesses.""",
   "A guess", "'LARGE OPEN FLOORS, WIDE DOORS' = OUR INFERENCE · HANGAR DIMENSIONS: NOT IN OUR SOURCES")
sc("""The tribute side, though, is documented. Wikipedia says the ghost symbol was adopted as a tribute to the squadron, and SlashGear says the pilots themselves asked for it. That is a human detail in a story of fire, closures and finance: a group of airmen losing their base, and a carmaker keeping their emblem alive.""",
   "The tribute", "WIKIPEDIA: GHOST SYMBOL ADOPTED AS A TRIBUTE · SLASHGEAR: PILOTS ASKED FOR THE EMBLEM · 'LOSING THEIR BASE' = OUR PARAPHRASE OF THE F 10 CLOSURE (WIKIPEDIA: DISBANDED 31 DEC 2002)")

ch("What the sources do not say")
sc("""What is missing. The cause of the fire. The size of the hangar. What the lease or purchase cost. Whether the CC8S reached Geneva on time. Whether the original hangar is still used after the twenty twenty-three factory. And the founder's own account of why he chose the base. If you have a primary source for any of these, put it in the comments.""",
   "Koenigsegg hangar", "NOT IN OUR SOURCES: CAUSE OF FIRE · HANGAR SIZE · LEASE/PURCHASE COST · CC8S GENEVA TIMING · CURRENT USE OF THE HANGAR · FOUNDER'S REASONING")
sc("""So a fire, a closed air base and a ghost squadron produced one of the world's more unusual car factories. We can document the dates, the buildings and the emblem, but not the founder's reasoning. In the other videos this week we look at the Gemera, compare it with the Regera, and count the cost of ownership. Subscribe to Pickup Reality.""",
   "Koenigsegg hangar", "SUBSCRIBE: PICKUP REALITY")

save("video160", "Why Koenigsegg Builds Hypercars in a Fighter-Jet Hangar", [
    "Wikipedia, Koenigsegg: https://en.wikipedia.org/wiki/Koenigsegg_Automotive",
    "Wikipedia, Scania Wing (F 10): https://en.wikipedia.org/wiki/Scania_Wing",
    "SlashGear, the story of the Koenigsegg ghost emblem",
    "Jalopnik, Koenigsegg factory tour",
    "Wikipedia, Koenigsegg Gemera: https://en.wikipedia.org/wiki/Koenigsegg_Gemera",
    "AOL (Car and Driver), The Koenigsegg Gemera is finally starting production, 30 Mar 2026: https://www.aol.com/articles/koenigsegg-gemera-finally-starting-production-210300723.html",
], "D")
