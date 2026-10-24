import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""A supercharged five point two litre V eight with eight hundred fifteen horsepower, or a four litre flat-six that revs to nine thousand and makes about five hundred. One is a Mustang with a rear gearbox and an active wing. The other is a nine eleven with a name that comes from a racing category. They both aim at the same thing: the fastest lap you can buy. This is the real difference between the Ford Mustang GTD and the Porsche nine eleven G T three.""",
   "Ford Mustang GTD and Porsche 911 GT3", "MUSTANG GTD VS PORSCHE 911 GT3: THE REAL DIFFERENCE")
sc("""Here is the twist. The Mustang has about sixty percent more power, costs about forty percent more, and has a lap time that, on the figures we found, is slower than the Porsche's by more than two seconds. And then the Mustang gets a new version, and the story changes. We will go through the numbers, and say where our sources disagree.""",
   "Mustang GTD vs 911 GT3", "MORE POWER, MORE MONEY, A SLOWER LAP — UNTIL IT ISN'T")
sc("""Every figure comes from a published source, listed in the description. Where sources disagree, we tell you. Where we do the maths ourselves, we say so. And where a figure is a manufacturer's claim, we label it a claim.""",
   "Mustang GTD vs 911 GT3", "EVERY NUMBER IS SOURCED")

ch("Two kinds of engine")
sc("""The Mustang GTD's engine is a five point two litre supercharged Predator V eight, five thousand, one hundred sixty-three cubic centimetres, rated at eight hundred fifteen horsepower at seven thousand, four hundred r p m and six hundred sixty-four pound-feet at four thousand, eight hundred, according to Wikipedia. Design News calls it an eight hundred horsepower engine, a difference of under two percent.""",
   "Ford Mustang GTD engine", "GTD: 5.2 L SUPERCHARGED V8 · 815 HP AT 7,400 RPM · 664 LB-FT")
sc("""The nine eleven G T three's engine is a four litre naturally aspirated flat-six. Wikipedia lists the nine ninety-two G T three at five hundred ten metric horsepower, which it converts to five hundred three horsepower, with four hundred seventy newton-metres, or three hundred forty-seven pound-feet, and a nine thousand r p m redline. It is the opposite of the Mustang's idea: small, high-revving, no turbo, no supercharger.""",
   "Porsche 911 GT3 engine", "GT3 (992.1): 4.0 L NA FLAT-SIX · 510 PS / 503 HP · 347 LB-FT · 9,000 RPM REDLINE")
sc("""By our arithmetic, the GTD has about sixty-two percent more power than the G T three, eight hundred fifteen against five hundred three, and about ninety-one percent more torque, six hundred sixty-four against three hundred forty-seven. Per litre, the Mustang makes about one hundred fifty-eight horsepower, the Porsche about one hundred twenty-six. The supercharger does the work that revs do for the Porsche.""",
   "Engine comparison", "GTD +62% POWER, +91% TORQUE · 158 vs 126 HP PER LITRE (OUR ARITHMETIC)")
sc("""Rev limits tell the story. Wikipedia lists the Mustang's peak power at seven thousand, four hundred r p m. The Porsche's redline is nine thousand, which by our arithmetic is sixteen hundred r p m, or about twenty-two percent, higher. A redline and a power peak are different things, so this is only a rough guide, but it shows that the Porsche's engine is built to spin, and the Mustang's to push.""",
   "Engine revs", "GTD POWER PEAK 7,400 RPM · GT3 REDLINE 9,000 RPM (+22%, DIFFERENT MEASURES — OUR ARITHMETIC)")
sc("""The Porsche's engine has a long heritage, Wikipedia says. The first nine ninety-six G T three, in nineteen ninety-nine, was a homologation model with a three point six litre engine rated at three hundred sixty metric horsepower, based on the Mezger racing engine used in the nine sixty-two and the nine eleven G T one. Porsche sold one thousand, eight hundred sixty-eight of them.""",
   "Porsche 996 GT3", "1999 996 GT3: 3.6 L · 360 PS · 1,868 SOLD · MEZGER ENGINE (962, 911 GT1)")

ch("Layout and transmission")
sc("""The layouts are opposites. The Mustang GTD has its engine at the front and an eight-speed dual-clutch transaxle at the rear, with a carbon-fibre driveshaft, according to Kelley Blue Book and Wikipedia. The nine eleven has its engine in the rear, Wikipedia says. One car moves weight rearward by putting a gearbox at the back; the other has its engine there already.""",
   "Mustang GTD and 911 layouts", "GTD: FRONT ENGINE, REAR TRANSAXLE · 911: REAR ENGINE")
sc("""The Porsche is available with a seven-speed P D K dual-clutch or a six-speed manual, Wikipedia says. The Mustang GTD offers only the eight-speed dual-clutch transaxle in our sources. So the Mustang's automatic has one more gear than the Porsche's, eight against seven. And the Porsche alone offers a manual, which many enthusiasts value.""",
   "Porsche PDK and manual", "GT3: 7-SPEED PDK OR 6-SPEED MANUAL · GTD: 8-SPEED DUAL-CLUTCH TRANSAXLE ONLY IN OUR SOURCES")
sc("""The Porsche's wheelbase is two thousand, four hundred fifty millimetres, according to Wikipedia's nine ninety-two page. The GTD's wheelbase is not given in our sources, so we cannot compare. The Mustang family is much larger: Wikipedia lists the ordinary Mustang at one hundred eighty-nine point four inches long and seventy-five point four wide. The nine eleven is a smaller car.""",
   "Porsche 911 wheelbase", "911 WHEELBASE 2,450 MM (96.5 IN) · MUSTANG 189.4 × 75.4 IN · GTD DIMENSIONS NOT IN OUR SOURCES")

ch("Weight and speed")
sc("""Weight is where the Porsche shows its hand. Wikipedia lists the nine ninety-two G T three at one thousand, four hundred thirty-five kilograms with P D K, and one thousand, four hundred eighteen with the manual. The G T three R S is one thousand, four hundred fifty. The facelifted G T three is heavier, at one thousand, four hundred seventy-nine, and the Touring one thousand, four hundred sixty-one. The GTD's weight is not in our sources.""",
   "Porsche 911 GT3 weight", "GT3: 1,435 KG (PDK) / 1,418 (MANUAL) · RS 1,450 · 992.2 GT3 1,479 · GTD: NOT IN OUR SOURCES")
sc("""So we cannot compute a power-to-weight ratio for the Mustang. For the Porsche, by our arithmetic, five hundred three horsepower over one thousand, four hundred thirty-five kilograms is about three hundred fifty horsepower per tonne. The sources say the GTD has a carbon-fibre body, but not how much it weighs, so it would be a guess to say the Mustang is heavier or lighter.""",
   "Porsche 911 GT3 power to weight", "GT3 ≈ 350 HP/TONNE (OUR ARITHMETIC) · GTD WEIGHT UNKNOWN")
sc("""Acceleration. Wikipedia lists the Porsche at three point four seconds to a hundred kilometres per hour with P D K, and three point nine with the manual. The G T three R S is three point two in the text, and three point oh in a table, which the page does not reconcile. Edmunds measured three point four seconds to sixty miles per hour in its test of a P D K car. The Mustang's acceleration is not in our sources.""",
   "Porsche 911 GT3 acceleration", "GT3: 3.4 S (PDK) / 3.9 S (MANUAL) · EDMUNDS 0–60 3.4 S · GTD: NOT IN OUR SOURCES")
sc("""Top speed. Wikipedia lists the Mustang GTD at two hundred two miles per hour, three hundred twenty-five kilometres per hour. For the Porsche nine ninety-two G T three, its table gives three hundred eighteen for the P D K and three hundred twenty for the manual, while its text says one hundred ninety-three miles per hour, about three hundred eleven. The facelifted car is listed at three hundred eleven.""",
   "Top speed comparison", "GTD 202 MPH (325 KM/H) · GT3 318/320 KM/H (TABLE) vs 193 MPH (TEXT) · 992.2: 311 KM/H")
sc("""By our arithmetic, the Porsche's table speed of three hundred eighteen kilometres per hour is about two percent below the Mustang's three hundred twenty-five, while its text figure is about four percent below. The G T three R S is listed at only two hundred ninety-six, because it trades top speed for downforce. A road car's top speed is a smaller part of its story than the headline suggests.""",
   "Top speed", "GT3 ≈ 2–4% BELOW THE GTD · GT3 RS 296 KM/H (DOWNFORCE FIRST) (OUR ARITHMETIC)")

ch("The Nürburgring")
sc("""The lap everyone quotes is the Nordschleife. AutoGuide reports that the GTD set a certified six fifty-seven point six eight on the seventh of August, twenty twenty-four, driven by Dirk Müller, with a roll cage, competition seat and harness added. Wikipedia gives six fifty-seven point six eight five. That made it, Ford says, the fastest American production car, and the fifth-fastest production sports car on official records.""",
   "Nürburgring Nordschleife", "GTD: 6:57.68 (AUG 7, 2024) · DIRK MÜLLER · 'FIFTH-FASTEST PRODUCTION SPORTS CAR' (FORD CLAIM)")
sc("""The Porsche's times, from Wikipedia's nine eleven G T three page: six fifty-five point three four for the nine ninety-two G T three, set by Lars Kern on the fifteenth of September, twenty twenty, and six forty-four point eight four eight for the G T three R S, set by Jörg Bergmeister on the fifth of October, twenty twenty-two. The page calls the R S the fastest lap by a naturally aspirated production car as of December twenty twenty-four.""",
   "Porsche 911 GT3 RS", "GT3: 6:55.34 (LARS KERN, SEPT 15, 2020) · GT3 RS: 6:44.848 (JÖRG BERGMEISTER, OCT 5, 2022)")
sc("""By our arithmetic, the G T three was two point three four five seconds, or about half a percent, quicker than the GTD. The G T three R S was twelve point eight three seven seconds quicker, about three percent. The AutoGuide article lists two nine eleven G T threes with Manthey kits and a G T three R S among the cars faster than the Mustang, which fits.""",
   "Nürburgring comparison", "GT3 2.3 S (0.6%) QUICKER · GT3 RS 12.8 S (3.1%) QUICKER (OUR ARITHMETIC)")
sc("""Now a disagreement between two Wikipedia pages. The Mustang page says the nine eleven G T three R S record is six forty-nine point three two eight. The nine eleven G T three page gives six forty-four point eight four eight for the same car. By our arithmetic, that is a difference of four and a half seconds. We cannot tell which is right, so we show both, and we use the G T three page for the R S, since it names the driver and date.""",
   "Wikipedia discrepancy", "GT3 RS: 6:49.328 (MUSTANG PAGE) vs 6:44.848 (GT3 PAGE) — 4.48 S APART (OUR ARITHMETIC)")
sc("""Then the GTD Competition. Wikipedia says a pre-production Mustang GTD Competition lapped in six forty point eight three five on the seventeenth of April, twenty twenty-six, with magnesium wheels, a power increase that is not specified, dive planes, wheel aero discs and a modified wing. By our arithmetic, that is about four seconds quicker than the G T three R S's six forty-four point eight four eight.""",
   "Ford Mustang GTD Competition", "GTD COMPETITION 6:40.835 (APR 17, 2026) ≈ 4.0 S QUICKER THAN THE GT3 RS 6:44.848 (OUR ARITHMETIC)")
sc("""A caution about that comparison. The GTD Competition is a pre-production car with undisclosed changes. The G T three R S is a production car from twenty twenty-two. And our sources do not give a lap time for the new nine ninety-two point two G T three, so we do not know how today's Porsche compares. The records are a moving target, as the Corvette ZR1 showed in July twenty twenty-five.""",
   "Nürburgring records", "PRE-PRODUCTION vs PRODUCTION · NO 992.2 LAP TIME IN OUR SOURCES")

ch("Aerodynamics")
sc("""Both cars use aerodynamics as much as engines. The Mustang has a dual-element rear wing with an active flap that flattens in drag-reduction mode, plus a front underwing with two flaps that open to reduce front downforce, Design News says. It also lowers by forty millimetres at the front and thirty at the rear in track mode. No downforce figures are given.""",
   "Ford Mustang GTD aerodynamics", "GTD: ACTIVE REAR FLAP · FRONT FLAPS · TRACK MODE −40 / −30 MM · NO DOWNFORCE FIGURES")
sc("""For the Porsche, Wikipedia gives a figure. The nine ninety-two G T three R S produces eight hundred sixty kilograms of downforce at two hundred eighty-five kilometres per hour, with an active rear wing that can be opened manually from the steering wheel. By our arithmetic, eight hundred sixty kilograms is about one thousand, eight hundred ninety-six pounds. The Mustang's figure is not published in our sources.""",
   "Porsche 911 GT3 RS downforce", "GT3 RS: 860 KG (≈ 1,896 LB) DOWNFORCE AT 285 KM/H · ACTIVE WING (OUR CONVERSION)")
sc("""The ordinary G T three has a rear wing, too, and the Touring version replaces the wing with an automatically deployable spoiler, Wikipedia says. The Touring is offered with a six-speed manual or P D K. For buyers who want the engine and the chassis without the visual drama, it is a quiet alternative. The Mustang has no quiet alternative: the GTD is meant to look like what it is.""",
   "Porsche 911 GT3 Touring", "GT3 TOURING: NO FIXED WING · AUTO SPOILER · 6-SPEED MANUAL OR PDK")

ch("Meet the rest of the field")
sc("""AutoGuide puts the GTD in a wider field. The Mercedes-AMG G T Black Series, from twenty twenty, lapped the Nordschleife in six forty-eight point oh four, nine seconds quicker than the GTD, and is the front-engined leader. The previous American record was the Dodge Viper ACR's seven oh one point oh three in twenty seventeen. By our arithmetic, the GTD was three point three four seconds quicker than the Viper.""",
   "Mercedes-AMG GT Black Series", "AMG GT BLACK SERIES 6:48.04 (+9.6 S QUICKER THAN GTD) · VIPER ACR 7:01.03 (GTD 3.3 S QUICKER) (OUR ARITHMETIC)")
sc("""The Corvette ZR1 and ZR1X, at six fifty point seven six three and six forty-nine point two seven five, beat the GTD's original time in July twenty twenty-five, Wikipedia says. By our arithmetic, the ZR1 was about six point nine seconds, or one point seven percent, quicker. The Corvette costs far less: GM lists one hundred seventy-four thousand, nine hundred ninety-five dollars with destination. The Mustang's answer was the Competition.""",
   "Corvette ZR1 Nürburgring", "ZR1 6:50.763 · ≈ 6.9 S (1.7%) QUICKER THAN THE ORIGINAL GTD · $174,995 (OUR ARITHMETIC)")
sc("""So the Mustang GTD's original lap put it between the Viper and the Corvette in American terms, and behind the Porsche and the Mercedes in global ones. Ford's claim, per AutoGuide, was that it was the fastest American production car at the time, and the fifth-fastest production sports car on official records. Both of those claims were true on the date they were made, and neither lasted.""",
   "Ford Mustang GTD claim", "THE CLAIMS WERE TRUE WHEN MADE (AUG–DEC 2024) AND OVERTAKEN WITHIN A YEAR")

ch("The Porsche's line-up")
sc("""The Porsche side is a family too. Wikipedia says the nine ninety-two was introduced in Los Angeles on the twenty-seventh of November, twenty eighteen, and the point two update launched on the twenty-eighth of May, twenty twenty-four. The point two G T three was revealed on the eighteenth of October, twenty twenty-four, alongside a G T three Touring. Its engine is unchanged at five hundred ten metric horsepower.""",
   "Porsche 911 992.2 GT3", "992 INTRODUCED NOV 27, 2018 · 992.2 UPDATE MAY 28, 2024 · 992.2 GT3 AND TOURING REVEALED OCT 18, 2024")
sc("""The page says the point two car's options include the Weissach package, which originally came from the G T three R S, and a Clubsport package offered free of charge. It lists torque at four hundred fifty newton-metres, top speed at three hundred eleven kilometres per hour for the G T three and three hundred thirteen for the Touring. The sources do not give a Nürburgring time for the point two car.""",
   "Porsche 911 GT3 992.2 options", "992.2 OPTIONS: WEISSACH PACKAGE · FREE CLUBSPORT PACKAGE · 311 / 313 KM/H · NO LAP TIME")
sc("""The G T three R S is the more extreme version. Wikipedia lists five hundred twenty-five metric horsepower at eight thousand, five hundred r p m, four hundred sixty-five newton-metres, one thousand, four hundred fifty kilograms and a top speed of two hundred ninety-six kilometres per hour. Its zero to a hundred is three point oh in a table and three point two in the text, which the page does not reconcile.""",
   "Porsche 911 GT3 RS", "GT3 RS: 525 PS AT 8,500 RPM · 465 NM · 1,450 KG · 296 KM/H · 0–100 3.0 S (TABLE) / 3.2 S (TEXT)")
sc("""By our arithmetic, the R S makes about three percent more power than the G T three, five twenty-five against five ten, yet it is twelve point eight seconds quicker at the Nürburgring. The difference is aerodynamics: eight hundred sixty kilograms of downforce at two hundred eighty-five kilometres per hour, against a plain G T three. Downforce, not power, is what separates the two.""",
   "Porsche 911 GT3 RS", "RS: +3% POWER BUT −12.8 S AT THE NÜRBURGRING · THE DIFFERENCE IS DOWNFORCE (OUR ARITHMETIC AND READING)")

ch("The Mustang's line-up")
sc("""The Mustang side is a family as well. Wikipedia lists the EcoBoost, the GT, the Dark Horse, the GTD, and the Dark Horse S C unveiled on the fifteenth of January, twenty twenty-six, with seven hundred ninety-five horsepower from the same supercharged five point two litre engine as the GTD. By our arithmetic, the S C gives away only two and a half percent in power. It is the nearest thing to a GTD engine in a normal Mustang.""",
   "Ford Mustang Dark Horse SC", "DARK HORSE SC (JAN 15, 2026): 795 HP / 660 LB-FT vs GTD 815 / 664 (−2.5% POWER)")
sc("""And the racing cars. Wikipedia lists a G T three, a G T four built by Multimatic with the five litre Coyote engine, a track-only Dark Horse R and a NASCAR Next Gen Dark Horse body. The G T four debuted at the Michelin Pilot Challenge at Daytona in twenty twenty-four, and KohR Motorsports and Luca Mars won the twenty twenty-four I M S A GSX titles. That is the Mustang's racing family.""",
   "Ford Mustang racing family", "GT3 · GT4 (2024, KOHR / LUCA MARS WON GSX TITLES) · DARK HORSE R · NASCAR NEXT GEN")
sc("""The point of listing the families is that each company has built a range around one car. For Porsche, the G T three sits above the Carrera range. For Ford, the GTD sits above the Dark Horse. The difference is the price of the step: from the Dark Horse S C's engine, the GTD adds a rear gearbox, a carbon body, active aero and Multimatic's dampers, and the price rises accordingly.""",
   "Mustang and 911 line-ups", "EACH COMPANY BUILT A RANGE AROUND A HALO MODEL (OUR READING)")

ch("Price")
sc("""Prices. Motor One reports that the GTD officially starts at three hundred twenty-seven thousand, nine hundred sixty dollars including fees and tax, from a base price of three hundred eighteen thousand, seven hundred sixty. The Porsche nine ninety-two point two G T three, according to supercars dot net, has a base M S R P of two hundred twenty-four thousand, four hundred ninety-five dollars. Edmunds lists two hundred twenty-two thousand, five hundred without destination.""",
   "Ford Mustang GTD and Porsche 911 GT3 price", "GTD BASE $318,760 · GT3 $224,495 (SUPERCARS.NET) / $222,500 (EDMUNDS, EX. DESTINATION)")
sc("""By our arithmetic, the GTD's base price is about forty-two percent above the G T three's two hundred twenty-four thousand, four hundred ninety-five. Per horsepower, the Mustang costs about three hundred ninety-one dollars and the Porsche about four hundred forty-six. So the Mustang is cheaper per unit of power, though the Porsche, with its naturally aspirated engine, is selling something else.""",
   "Price per horsepower", "GTD +42% PRICE · ~$391/HP vs GT3 ~$446/HP (OUR ARITHMETIC)")
sc("""The Porsche's price has risen. Supercars dot net says the nine ninety-two point one G T three launched in twenty twenty-one at one hundred sixty-one thousand, nine hundred dollars, and that the point two car is about thirty-nine percent more. By our arithmetic, two twenty-four ninety-five over one sixty-one nine hundred is one point three eight seven, so the rise is about thirty-nine percent. The same article calls it a hard sell, at best.""",
   "Porsche 911 GT3 price rise", "992.1 GT3 (2021): $161,900 → 992.2: $224,495 = +39% (SUPERCARS.NET; OUR ARITHMETIC AGREES)")
sc("""The same article says the point two car has less torque and more weight than the point one car, without the Weissach package. Wikipedia agrees on the figures: torque down from four hundred seventy to four hundred fifty newton-metres, weight up from one thousand, four hundred thirty-five to one thousand, four hundred seventy-nine. By our arithmetic, that is about four percent less torque and three percent more weight.""",
   "Porsche 911 GT3 992.2", "992.2: TORQUE −4% · WEIGHT +3% vs 992.1 (WIKIPEDIA; OUR ARITHMETIC)")
sc("""Fuel economy and tax. Edmunds lists fifteen miles per gallon combined for the automatic Porsche. Motor One lists twelve combined for the Mustang, with a three thousand, seven hundred dollar gas-guzzler tax. The Edmunds page does not mention a Porsche tax. Both cars are, by any standard, thirsty; the Porsche is a little less so on these numbers.""",
   "Fuel economy", "GT3: 15 MPG COMBINED (EDMUNDS) · GTD: 12 MPG + $3,700 TAX (MOTOR1)")
sc("""And the ratings. Edmunds' own score for the twenty twenty-five G T three is six point nine out of ten, though its meta description says seven point five. We note the discrepancy without choosing a number. Our sources contain no equivalent rating for the Mustang GTD, and we do not give one. A rating is an opinion, and we are comparing figures.""",
   "Edmunds rating", "EDMUNDS 2025 GT3: 6.9/10 (PAGE) vs 7.5/10 (META DESCRIPTION) · NO GTD RATING IN OUR SOURCES")

ch("Racing roots")
sc("""Both names point to racing. The Porsche nine eleven G T three descends from the nine ninety-six homologation car of nineteen ninety-nine. Wikipedia lists a G T three Cup at two hundred twenty-five thousand euros and a nine ninety-one point two G T three R at four hundred fifty-nine thousand euros, excluding taxes. The Porsche sells racing cars as well as road cars, from the same family.""",
   "Porsche 911 GT3 Cup", "GT3 CUP €225,000 · 991.2 GT3 R €459,000 (EX. TAXES) (WIKIPEDIA)")
sc("""The Mustang GTD is the road car behind a racing programme. Wikipedia says the Mustang G T three, built by Ford and Multimatic, raced in I M S A and the World Endurance Championship, and returned to Le Mans for the first time since nineteen ninety-seven. Torque Café quotes Jim Farley saying that to go to Le Mans you need a road car. The GTD is that road car, and the Dark Horse is the homologation model.""",
   "Ford Mustang GT3", "MUSTANG GT3: IMSA + WEC · LE MANS RETURN AFTER 27 YEARS · 'YOU NEED A ROAD CAR' — FARLEY (TORQUE CAFÉ)")
sc("""There is a naming overlap worth noting. The Porsche road car is a G T three, named for a racing class. The Mustang's race car is also a G T three. So the same category name appears on a Mustang racing car and a Porsche road car, while the Mustang road car is called a GTD. By our reading, the names show which racing world each company is borrowing from.""",
   "GT3 racing class", "PORSCHE ROAD CAR = 'GT3' · MUSTANG RACE CAR = 'GT3' · MUSTANG ROAD CAR = 'GTD' (OUR READING)")

ch("The verdict")
sc("""So, which wins? On power and torque, the Mustang. On price per horsepower, the Mustang. On top speed, the Mustang, slightly. On weight and acceleration, our sources only have the Porsche's numbers. On the original lap, the Porsche, by two point three seconds, and the R S by nearly thirteen. On the Competition lap, the Mustang. On a manual gearbox and engine character, the Porsche.""",
   "Mustang GTD vs Porsche 911 GT3", "SCORECARD")
sc("""The real difference is the approach. Ford used a supercharged V eight, a rear gearbox and active aerodynamics to build a track weapon that is also street-legal. Porsche used a naturally aspirated flat-six that revs to nine thousand and an established chassis. One adds technology to find speed; the other refines a formula it has built since nineteen ninety-nine. That is our reading of the figures.""",
   "Mustang GTD vs Porsche 911 GT3", "TECHNOLOGY vs REFINEMENT (OUR READING)")
sc("""A caution. We have not driven either car. The GTD's weight and acceleration are not in our sources, the records come from different dates, and the two Wikipedia pages disagree on a Porsche lap time. Some comparisons are our own arithmetic, labelled each time. If you have a verified figure, put it in the comments with where it comes from.""",
   "Mustang GTD vs Porsche 911 GT3", "NUMBERS, NOT A DRIVING VERDICT")
sc("""Which would you rather have, the Mustang or the Porsche? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Mustang GTD, work out what it really costs to own one, and tell why Ford built a Mustang to beat Porsche. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford Mustang GTD", "SUBSCRIBE: PICKUP REALITY")

save("video126", "Mustang GTD vs Porsche 911 GT3: The Real Difference", [
    "Wikipedia, Ford Mustang GTD: https://en.wikipedia.org/wiki/Ford_Mustang_GTD",
    "Wikipedia, Porsche 911 GT3: https://en.wikipedia.org/wiki/Porsche_911_GT3",
    "Wikipedia, Porsche 911 (992): https://en.wikipedia.org/wiki/Porsche_911_(992)",
    "Kelley Blue Book, Ford drops details on GTD, the uber Mustang: https://www.kbb.com/car-news/ford-drops-details-on-gtd-the-uber-mustang",
    "Design News, Engineering the Maximum Mustang GTD: https://www.designnews.com/automotive-engineering/engineering-the-maximum-mustang-gtd",
    "AutoGuide, Ford Mustang GTD joins Nürburgring's sub-seven-minute club: https://www.autoguide.com/auto/manufacturers/ford/ford-mustang-gtd-joins-nrburgring-s-sub-seven-minute-club-44615074",
    "Motor1, The Ford Mustang GTD is even more expensive than we thought: https://www.motor1.com/news/762588/ford-mustang-gtd-price-window-sticker/",
    "Supercars.net, Is the latest Porsche 992.2 GT3 worth the price?: https://www.supercars.net/blog/?p=891516",
    "Edmunds, 2025 Porsche 911 GT3: https://www.edmunds.com/porsche/911/2025/gt3",
    "Torque Café, Why Ford built a race car for the road: https://archive.torquecafe.com/why-ford-built-a-race-car-for-the-road/",
], "B")
