import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""Two Lamborghinis, from the same factory, by the same stylist, five years apart. One is a rounded, curvy car that hid its engine at its own launch. The other is a wedge that people put on their bedroom walls. They look nothing alike, and they sit on opposite sides of a design revolution. This is the real difference between the Lamborghini Countach and the Lamborghini Miura.""",
   "Lamborghini Countach and Miura", "COUNTACH VS MIURA: THE REAL DIFFERENCE")
sc("""Here is the twist. The Countach is the car everyone remembers, but on the figures we found, it was not dramatically heavier or lighter, faster or slower than the Miura at the top of its range. The big differences are in layout, in numbers built, and in what the cars sell for today. Let us go through them, and say where the sources disagree.""",
   "Lamborghini Countach and Miura", "THE BIG DIFFERENCES ARE NOT WHAT YOU THINK")
sc("""Every figure comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so, and we do not convert currencies, because our sources do not give exchange rates.""",
   "Lamborghini Countach and Miura", "EVERY NUMBER IS SOURCED")

ch("Two origin stories")
sc("""The Miura story, according to Wikipedia, begins in nineteen sixty-five. Three engineers, Giampaolo Dallara, Paolo Stanzani and Bob Wallace, developed the prototype in their spare time, largely at night. Ferruccio Lamborghini preferred grand tourers to race-derived cars, but after seeing the development car he approved continued work and gave the engineers a free hand, seeing a possible marketing tool.""",
   "Lamborghini Miura prototype", "MIURA: BUILT IN SPARE TIME, 1965 · FERRUCCIO SAW A MARKETING TOOL")
sc("""The Countach story starts five years later. Wikipedia says Lamborghini launched the project to succeed the Miura, which by nineteen seventy had lost ground to rivals such as the Ferrari Daytona. Paolo Stanzani, now chief engineer, began work under the project name L P one twelve, with Bob Wallace, Massimo Parenti and Marcello Gandini of Bertone. So some of the same people built both cars.""",
   "Lamborghini Countach LP112", "COUNTACH: 1970 · STANZANI, WALLACE, GANDINI — SOME OF THE SAME PEOPLE")
sc("""The Miura was shown first, at the Turin show in nineteen sixty-five as a rolling chassis, and then with a Bertone body at Geneva in nineteen sixty-six. Showgoers placed orders before there was a body, Wikipedia says. The Countach prototype appeared at Geneva in nineteen seventy-one. The production car debuted in nineteen seventy-four, when, the page says, fifty orders were placed at the Geneva show.""",
   "Geneva Motor Show", "MIURA: TURIN 1965 / GENEVA 1966 · COUNTACH: GENEVA 1971 PROTOTYPE, 1974 PRODUCTION")
sc("""By our arithmetic, the Miura went from spare-time prototype to a car on a stand in about one year, nineteen sixty-five to nineteen sixty-six. The Countach took from nineteen seventy to nineteen seventy-four to reach production, about four years. Wikipedia says the Countach prototype was crash-tested to destruction at MIRA in England on the twenty-first of March, nineteen seventy-four, for European type approval.""",
   "Lamborghini development", "MIURA ~1 YEAR TO THE SHOW · COUNTACH ~4 YEARS TO PRODUCTION (OUR ARITHMETIC)")

ch("The layout: sideways or lengthways")
sc("""The most important difference is hidden in the middle of the car. The Miura's three thousand, nine hundred twenty-nine cubic centimetre V twelve was mounted transversely, sideways, behind the driver, and the engine and gearbox shared one casting. Wikipedia calls it the first high-performance production road car with a rear mid-engine, rear-wheel-drive layout.""",
   "Lamborghini Miura engine", "MIURA: V12 MOUNTED SIDEWAYS · ENGINE AND GEARBOX IN ONE CASTING")
sc("""The Countach, the same page says, kept the mid-engine, rear-wheel-drive layout but changed the engine orientation. In contrast to the Miura's transverse engine, the Countach's was mounted longitudinally. The transmission sat between the two seats, with a driveshaft running from the transmission through the engine's oil sump to a differential at the rear.""",
   "Lamborghini Countach engine", "COUNTACH: ENGINE LENGTHWAYS · GEARBOX BETWEEN THE SEATS (WIKIPEDIA)")
sc("""Wikipedia says this layout had numerous advantages over the Miura's transverse engine, including better weight distribution near the centre of the car, a shorter wheelbase and easier maintenance access. Those are the page's words, not ours. We can add that the page also describes the Countach chassis as a full space frame of welded round-section steel tube.""",
   "Lamborghini Countach chassis", "COUNTACH: BETTER WEIGHT DISTRIBUTION, SHORTER WHEELBASE, EASIER ACCESS (WIKIPEDIA)")
sc("""The gearbox in the Countach is a five-speed manual with Porsche-type synchromesh, Wikipedia says. The Miura's is also a five-speed manual, with a four point oh eight three to one ratio listed. So on paper the transmissions have the same number of gears. What differs is where they are, and what that does to the rest of the car.""",
   "Lamborghini gearbox", "BOTH FIVE-SPEED MANUALS · DIFFERENT PLACEMENT")

ch("The engine: the same V twelve, mostly")
sc("""Both cars begin with a three thousand, nine hundred twenty-nine cubic centimetre V twelve. Wikipedia says the engine dates from nineteen sixty-three and was designed by Giotto Bizzarrini. In the Miura it appears in three states of tune. The P four hundred has three hundred fifty metric horsepower and three hundred fifty-five newton-metres. The P four hundred S has three hundred seventy and three hundred eighty-eight.""",
   "Lamborghini V12 engine", "MIURA P400: 350 PS / 355 NM · P400 S: 370 PS / 388 NM")
sc("""The P four hundred S V, the last Miura, has three hundred eighty-five metric horsepower at seven thousand, eight hundred fifty r p m and four hundred newton-metres at five thousand, seven hundred fifty, with different cams and four triple-barrel Weber carburettors. The Countach L P four hundred has three hundred seventy-five metric horsepower at eight thousand r p m and three hundred sixty-one newton-metres.""",
   "Lamborghini Miura SV", "MIURA SV: 385 PS / 400 NM · COUNTACH LP400: 375 PS / 361 NM")
sc("""Our arithmetic. The L P four hundred makes about two and a half percent less power than the Miura S V, three seventy-five against three eighty-five, and almost ten percent less torque, three sixty-one against four hundred. The first Countach, same displacement, was a little weaker than the last Miura. The reason is not in our sources, so we offer none.""",
   "Lamborghini engines", "COUNTACH LP400 vs MIURA SV: −2.6% POWER, −9.8% TORQUE (OUR ARITHMETIC)")
sc("""Later Countachs grew the engine. The L P five hundred S has four thousand, seven hundred fifty-four cubic centimetres and three hundred seventy-five metric horsepower. The five thousand Quattrovalvole has five thousand, one hundred sixty-seven cubic centimetres, four hundred fifty-five horsepower and five hundred newton-metres. By our arithmetic, that is about twenty-five percent more torque than the Miura S V and about eighteen percent more power.""",
   "Lamborghini Countach 5000 QV", "5000 QV: 455 PS / 500 NM · +18% POWER, +25% TORQUE VS MIURA SV (OUR ARITHMETIC)")

ch("Size and weight")
sc("""Now the size. Wikipedia gives the Miura at four thousand, three hundred sixty millimetres long, between one thousand, seven hundred sixty and one thousand, seven hundred eighty wide, and about one thousand, fifty-five to sixty tall, with a wheelbase of two thousand, five hundred. The Countach L P four hundred is four hundred fourteen centimetres long, one hundred eighty-nine wide and one hundred seven tall.""",
   "Lamborghini Countach and Miura size", "MIURA 4,360 × ~1,780 × ~1,057 MM · COUNTACH LP400 4,140 × 1,890 × 1,070 MM")
sc("""By our arithmetic, the Countach is two hundred twenty millimetres shorter than the Miura, and about one hundred ten millimetres wider than the S V. It is also slightly taller, by about ten to fifteen millimetres. A shorter, wider, taller car, with the engine turned around. That is what a shorter wheelbase and a longitudinal engine buy you, if the Wikipedia reasoning is right.""",
   "Lamborghini Countach and Miura", "COUNTACH: 220 MM SHORTER, ~110 MM WIDER, ~10–15 MM TALLER (OUR ARITHMETIC)")
sc("""Weight is harder, because the sources disagree. Wikipedia lists the Miura at one thousand, one hundred twenty-five kilograms dry for the P four hundred and one thousand, two hundred ninety-eight for the S and S V, with an infobox kerb weight of one thousand, two hundred ninety-two. The Countach L P four hundred is listed at one thousand, sixty-five dry and one thousand, three hundred point five kerb.""",
   "Lamborghini weight", "MIURA: 1,125 / 1,298 KG DRY · 1,292 KG KERB · COUNTACH LP400: 1,065 DRY / 1,300.5 KERB")
sc("""By our arithmetic, the kerb weights are almost identical: one thousand, three hundred point five against one thousand, two hundred ninety-two is a difference of eight and a half kilograms, about seven tenths of a percent. The dry weights differ by two hundred thirty-three kilograms, about eighteen percent. Those two comparisons cannot both be right, so we trust neither the dry weights nor the gap.""",
   "Lamborghini weight discrepancy", "KERB: ~0.7% APART · DRY: ~18% APART — THE SOURCES CONTRADICT (OUR ARITHMETIC)")
sc("""The Wikipedia Countach page itself points out one such problem: the five thousand Quattrovalvole's kerb weight, one thousand, four hundred eighty-eight kilograms, is lower than its listed dry weight, one thousand, four hundred ninety, which is impossible. So the weight data on both pages mixes definitions. We use them only as rough guides and say so.""",
   "Lamborghini Countach 5000 QV", "QV: KERB 1,488 KG < DRY 1,490 KG — IMPOSSIBLE · THE DATA MIX DEFINITIONS")

ch("Speed: claimed against measured")
sc("""Performance. Wikipedia lists measured top speeds for the Miura: two hundred seventy-five kilometres per hour for the P four hundred and two hundred seventy-eight for the P four hundred S. The S V is listed with a claimed three hundred, and no measured figure. Zero to sixty miles per hour was seven point oh seconds for the first car and six point seven for the S.""",
   "Lamborghini Miura performance", "MIURA MEASURED: P400 275 KM/H, 7.0 S · P400 S 278 KM/H, 6.7 S · SV CLAIMED 300 KM/H")
sc("""The Countach L P four hundred is listed at two hundred eighty-eight kilometres per hour measured, three hundred fifteen claimed, and zero to a hundred kilometres per hour in five point four seconds. By our arithmetic, the measured top speed is about ten kilometres per hour, or three and a half percent, above the Miura P four hundred S's measured figure.""",
   "Lamborghini Countach performance", "COUNTACH LP400 MEASURED 288 KM/H (CLAIMED 315) · +10 KM/H VS MIURA P400 S")
sc("""Acceleration is not quite like for like. Sixty miles per hour is about ninety-seven kilometres per hour, so a time to a hundred is slightly longer. Even so, five point four seconds to a hundred looks quicker than six point seven to sixty. By our arithmetic, that is at least about a second and a quarter faster, and it is for a car with a similar engine.""",
   "Lamborghini acceleration", "COUNTACH ≥ ~1.3 S QUICKER (ROUGH, DIFFERENT UNITS — OUR ARITHMETIC)")
sc("""The claimed speeds tell a different story. The Miura S V is claimed at three hundred; the Countach at three hundred fifteen, and the Walter Wolf special at three hundred fifteen or three hundred twenty-four. Claimed speeds in the sources are higher than measured ones in every case where we have both. For the Countach the gap is twenty-seven kilometres per hour, about nine percent.""",
   "Lamborghini claimed speeds", "COUNTACH: CLAIMED 315 VS MEASURED 288 (+9%, OUR ARITHMETIC)")
sc("""There is an extra twist for the Countach. The later L P four hundred S is listed at only two hundred fifty-four kilometres per hour measured, with a claimed two hundred seventy-nine point six. Wikipedia says the optional rear wing improved high-speed stability but cost at least sixteen kilometres per hour. The most famous-looking Countach was, on paper, slower than the Miura.""",
   "Lamborghini Countach LP400 S", "LP400 S: 254 KM/H MEASURED — SLOWER THAN THE MIURA P400 S (278)")

ch("Looks and the cabin")
sc("""Both cars were styled by Marcello Gandini at Bertone, according to the sources. The Miura, Wikipedia says, was the highlight of the Geneva show in nineteen sixty-six, thanks to Gandini's styling and the mid-engine design. The Countach was a break. The Miura was curved; the Countach, in the photographs, is a wedge. The page does not use those words, so this is our description.""",
   "Marcello Gandini", "BOTH STYLED BY GANDINI AT BERTONE · MIURA CURVED, COUNTACH A WEDGE (OUR DESCRIPTION)")
sc("""The most obvious difference is the doors. The Countach has scissor doors, which hinge at the front and lift up. Wikipedia says they first appeared on Gandini's nineteen sixty-eight Alfa Romeo Carabo concept, so the idea was already two years old when the Miura was in showrooms. The Miura has conventional doors. The Countach also had a periscope for rear visibility, which the Miura did not need.""",
   "Alfa Romeo Carabo", "SCISSOR DOORS: FIRST ON THE 1968 CARABO · COUNTACH ONLY")
sc("""Inside, the Countach had a low seating position, a prominent transmission tunnel and wide door sills, which Wikipedia says gave it a race-car cockpit feel. The prototype had deeply recessed bucket seats. For the Miura, our sources do not describe the cabin in the same detail, though the S added power windows and optional air conditioning at eight hundred dollars.""",
   "Lamborghini Countach interior", "COUNTACH: RACE-CAR COCKPIT FEEL · MIURA S: POWER WINDOWS, A/C $800 EXTRA")
sc("""On the Countach, Wikipedia says drivers often reverse by sitting on the wide sill and looking over the back of the car. The Miura's visibility is not discussed in our sources, so we cannot compare. We can say that the Countach's poor rear view was serious enough to need a periscope, and that the periscope was dropped on later cars in favour of ordinary mirrors.""",
   "Countach periscope", "COUNTACH VISIBILITY NEEDED A PERISCOPE · LATER CARS USED MIRRORS")

ch("How many were built")
sc("""Production. Wikipedia lists the Miura at two hundred seventy-five P four hundreds, three hundred thirty-eight P four hundred Ss and one hundred fifty S Vs. By our arithmetic, that is seven hundred sixty-three cars. The Countach total on its page is one thousand, nine hundred eighty-three, including the prototype, or one thousand, nine hundred eighty-two production cars.""",
   "Lamborghini production", "MIURA: 275 + 338 + 150 = 763 · COUNTACH: 1,983 INCLUDING THE PROTOTYPE")
sc("""By our arithmetic, the Countach was built in about two and a half times the number of the Miura, one thousand, nine hundred eighty-three over seven hundred sixty-three, which is about two point six. And it ran for sixteen years, nineteen seventy-four to nineteen ninety, against roughly seven for the Miura. The rarity of the Miura is not about scarcity at launch, but about what survived.""",
   "Lamborghini production", "COUNTACH ≈ 2.6× MORE CARS THAN THE MIURA, OVER 16 YEARS VS ~7 (OUR ARITHMETIC)")
sc("""Compare the first series cars. The Miura S V, the last Miura, is one of only one hundred fifty built, according to RM Sotheby's. The first-series Countach L P four hundred Periscopio is one of about one hundred fifty, according to the Countach Register, though Wikipedia lists one hundred fifty-seven L P four hundreds. At the top of each range, the numbers are close to equal.""",
   "Lamborghini SV and Periscopio", "MIURA SV: 150 BUILT · COUNTACH LP400 PERISCOPIO: ~150 (COUNTACH REGISTER) / 157 (WIKIPEDIA)")
sc("""The Countach also had far more variants. L P four hundred, L P four hundred S, L P five hundred S, five thousand Quattrovalvole and twenty-fifth Anniversary, plus Wolf specials, turbo cars and one-offs. The Miura had three main versions, plus the Jota, which Bob Wallace built in nineteen seventy, and six factory S V slash J cars. One car had many forms; the other had a few.""",
   "Lamborghini variants", "COUNTACH: 5 MAIN VARIANTS + SPECIALS · MIURA: 3 MAIN VARIANTS + JOTA / SV-J")

ch("The Jota and the specials")
sc("""The Miura Jota is the legend inside the legend. Wikipedia says Bob Wallace built it in nineteen seventy as a racing test car to FIA Appendix J rules. Aluminium and plastic cut roughly three hundred sixty kilograms, the page says, and the compression ratio rose to eleven point five to one, with dry-sump lubrication and between four hundred eighteen and four hundred forty horsepower at eight thousand, eight hundred r p m.""",
   "Lamborghini Miura Jota", "JOTA (1970): ~360 KG LIGHTER · 418–440 BHP AT 8,800 RPM · BOB WALLACE")
sc("""The original Jota burned in a crash in April nineteen seventy-one, the page says. The Countach prototype was destroyed in a crash test on purpose, in nineteen seventy-four. Both of the first cars of their type are gone. The page lists six factory S V slash J cars, plus a seventh built between nineteen eighty-three and nineteen eighty-seven for Jean Claude Mimran.""",
   "Lamborghini Jota", "JOTA BURNED APRIL 1971 · LP500 CRASH-TESTED MARCH 1974 · 6 FACTORY SV/J CARS")
sc("""The Countach had its own special: the Walter Wolf car. Dallara built chassis one one two zero one four eight with the five litre engine from the L P five hundred prototype, rated at four hundred fifty-three metric horsepower, with a rear wing that cut at least sixteen kilometres per hour. Wikipedia says two more Wolf specials followed. Three cars in total, against seven for the Miura slash J.""",
   "Walter Wolf Countach", "COUNTACH WOLF SPECIALS: 3 CARS · MIURA SV/J: 7 CARS (6 + 1)")

ch("Price new and price now")
sc("""Now money. Wikipedia says the Miura P four hundred launched at twenty thousand dollars, about one hundred ninety-eight thousand, four hundred sixty-two dollars in twenty twenty-five money, according to the page's own conversion. The Countach's launch price is not given in the article we used, so we cannot compare list prices. That is a gap, and we state it plainly.""",
   "Lamborghini Miura price", "MIURA P400 LAUNCH: US$20,000 (~$198,462 IN 2025 DOLLARS, PER WIKIPEDIA) · COUNTACH: NOT IN OUR SOURCE")
sc("""Today. RM Sotheby's Paris sold Miura S V chassis four eight four zero for three million, seven hundred seventeen thousand, five hundred euros in twenty twenty-six. It had sold at the same house in February twenty twenty-one for two million, four hundred twenty-three thousand, seven hundred fifty euros, The Jalopy reports. By our arithmetic, that is a rise of about fifty-three percent in nominal euros in about five years.""",
   "Lamborghini Miura SV", "MIURA SV CHASSIS 4840: €2,423,750 (2021) → €3,717,500 (2026) = +53% (OUR ARITHMETIC)")
sc("""In September twenty twenty, Gooding sold a metallic gold Miura S V Speciale, with extras like the Jota's, for three point two million pounds including premium, against an estimate of one point six to two million. The earlier price context: Nicolas Cage bought the Shah of Iran's S V slash J in nineteen ninety-seven for four hundred ninety thousand dollars, then a record, and an S V slash J later sold for over one point nine million.""",
   "Lamborghini Miura SV Speciale", "GOODING 2020: £3.207M · 1997 SV/J: $490,000 (NICOLAS CAGE) · LATER SV/J: OVER $1.9M")
sc("""For the Countach, RM Sotheby's Arizona sold a nineteen seventy-seven L P four hundred Periscopio for eight hundred eighty-five thousand dollars in twenty twenty-six. Hagerty's April twenty twenty-five page shows one million dollars for a nineteen seventy-five L P four hundred in good condition. A twenty-fifth Anniversary sold for four hundred seventy-eight thousand in twenty twenty-four, and a low-mileage Quattrovalvole for five hundred ninety-nine thousand, five hundred.""",
   "Lamborghini Countach prices", "COUNTACH: LP400 PERISCOPIO $885K · HAGERTY LP400 $1M · 25TH $478K · QV $599.5K")
sc("""Comparisons across currencies are unsafe, and the cars are different ages and conditions, so we do not compute a ratio. What the sources do show is that the best Miura S V results are in the millions, in euros and pounds, while the Countach results we found range from the high four hundreds of thousands to about a million dollars. The Miura, the earlier and rarer car, commands more.""",
   "Lamborghini auctions", "BEST MIURA SV RESULTS: MILLIONS · COUNTACH RESULTS WE FOUND: $478K–$1M (NO RATIO: CURRENCIES DIFFER)")

ch("Living with them")
sc("""What is it like to own one? Our sources give service data for the Countach. RM Sotheby's, describing a nineteen eighty-nine twenty-fifth Anniversary car sold in Arizona in twenty twenty-four, says invoices since two thousand one total over sixty-eight thousand dollars. Work included an engine-out service, a transmission overhaul with a Kevlar clutch kit, and a December twenty twenty-three visit costing over sixteen thousand dollars.""",
   "Lamborghini Countach service", "25TH ANNIVERSARY: $68K+ OF INVOICES SINCE 2001 · DEC 2023 VISIT $16K+")
sc("""For the Miura, our sources give history rather than costs. RM Sotheby's says the S V it sold in Paris was converted in the nineteen seventies to look like the Jota, then restored back to its original June nineteen seventy-one specification in twenty sixteen. Mythic Motors performed a major service in April twenty twenty-four. The catalogue gives no invoice totals, so we cannot compare service costs.""",
   "Lamborghini Miura SV", "MIURA SV 4840: JOTA-STYLE CONVERSION 1972–77 · RESTORED TO ORIGINAL 2016 · SERVICE APRIL 2024 (NO COSTS GIVEN)")
sc("""There is a useful point about the layout. Wikipedia says the Countach's longitudinal engine made maintenance access easier than the Miura's transverse layout. The Miura's engine and gearbox share one casting, so work on one affects the other. Our sources do not quantify the saving, so this remains the page's claim, not a measured fact. We mention it because owners care.""",
   "Lamborghini maintenance", "COUNTACH SAID TO BE EASIER TO WORK ON (WIKIPEDIA) — NOT QUANTIFIED")
sc("""One more fact on survival. The Countach was never built to U S or Canadian standards at first, and Wikipedia says that, in a market that was Lamborghini's largest, owners paid to modify grey-market cars between nineteen seventy-six and nineteen eighty-eight. The first U S-specification car came in nineteen eighty-five. So many Countachs were converted, which is a factor when buyers look for originality.""",
   "Lamborghini Countach grey market", "GREY MARKET 1976–1988 · FIRST US-SPEC MODEL 1985")

ch("The legacy")
sc("""Both names came back. Wikipedia says Lamborghini unveiled the Aventador Miura Homage in twenty sixteen to mark the Miura's fiftieth anniversary, and its Ad Personam division built fifty units. The Countach name returned in twenty twenty-one on the Countach L P I eight hundred dash four, which the page says has a naturally aspirated six point five litre V twelve and a forty-eight volt electric motor, and is based on the Sián.""",
   "Lamborghini Aventador Miura Homage", "MIURA HOMAGE 2016: 50 UNITS · COUNTACH LPI 800-4 (2021): 6.5 L V12 + 48 V MOTOR")
sc("""Other tributes are smaller. Wikipedia mentions a recreation of the Jota called Millechiodi built on a P four hundred S. LEGO released a Countach five thousand Quattrovalvole set in June twenty twenty-four. A Countach was the Monaco Grand Prix safety car from nineteen eighty to nineteen eighty-three, and a Miura appears in the opening sequence of the nineteen sixty-nine film The Italian Job.""",
   "Lamborghini legacy", "MILLECHIODI JOTA RECREATION · LEGO COUNTACH (JUNE 2024) · MONACO GP SAFETY CAR 1980–83 · THE ITALIAN JOB (1969)")
sc("""One last piece of arithmetic. From the Miura's Geneva debut in nineteen sixty-six to the last Countach in nineteen ninety is twenty-four years. Over those twenty-four years Lamborghini built, by our arithmetic, seven hundred sixty-three Miuras and about one thousand, nine hundred eighty-two production Countachs, almost two thousand, seven hundred fifty cars in all, according to Wikipedia's tables.""",
   "Lamborghini", "1966–1990: 763 MIURAS + ~1,982 COUNTACHS ≈ 2,745 CARS (OUR ARITHMETIC)")

ch("Which was the better car?")
sc("""So, which one? On layout, the Countach, according to the page's own reasoning: better weight distribution, a shorter wheelbase, easier access. On measured top speed and acceleration, the Countach, by a little. On engine tune, the Miura S V, until the Quattrovalvole arrived. On numbers built, the Countach by a factor of two and a half. On auction price, the Miura. On fame, the Countach.""",
   "Lamborghini Countach and Miura", "SCORECARD")
sc("""The real difference is the idea. The Miura invented the layout and made it a road car; the Countach rearranged it and gave it a shape nobody had seen. One was a surprise, finished days before a show with ballast under the bonnet. The other was a deliberate successor, four years in the making. Both were designed, in part, by the same stylist. That is our reading, based on the facts above.""",
   "Lamborghini Countach and Miura", "THE MIURA INVENTED IT · THE COUNTACH REARRANGED IT (OUR READING)")
sc("""A caution. We have not driven either car, the weight figures contradict each other, the Countach launch price is not in our source, and the prices are in different currencies. We have tried to say so each time. If you have a verified figure from a primary source, tell us in the comments.""",
   "Lamborghini Countach and Miura", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you rather have in your garage, the Miura or the Countach? Tell us in the comments. In the other videos of this series, we reveal two things you may not know about the Countach, work out what it really costs to own a classic Lamborghini, and tell how a tractor maker ended up building the Countach. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video118", "Countach vs Miura: The Real Difference", [
    "Wikipedia, Lamborghini Countach: https://en.wikipedia.org/wiki/Lamborghini_Countach",
    "Wikipedia, Lamborghini Miura: https://en.wikipedia.org/wiki/Lamborghini_Miura",
    "RM Sotheby's, 1971 Lamborghini Miura SV (Paris 2026, lot 150): https://rmsothebys.com/auctions/pa26/lots/r0090-1971-lamborghini-miura-sv",
    "RM Sotheby's, 1977 Lamborghini Countach LP400 Periscopio (Arizona 2026): https://rmsothebys.com/auctions/az26/lots/r0060-1977-lamborghini-countach-lp400-periscopio-by-bertone",
    "Goodwood, This ultimate Miura SV Speciale just sold for £3.2 million: https://www.goodwood.com/grr/road/news/this-ultimate-miura-sv-speciale-just-sold-for-3.2-million",
    "The Jalopy, Record prices for Lamborghini Miura SV and Countach LP 400 Periscopo at RM Sotheby's Paris: https://thejalopy.com/record-prices-lamborghini-miura-sv-countach-lp-400-sotheby/",
    "Hagerty valuation tools, 1975 Lamborghini Countach LP400: https://hagerty.com/apps/valuationtools/1975-lamborghini-countach-lp400",
], "B")
