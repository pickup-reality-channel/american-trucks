import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Pagani Zonda had a naturally aspirated engine with up to seven point three litres. The Pagani Utopia has a twin-turbocharged engine with less than six. One was made for twenty years, with about one hundred forty cars. The other plans two hundred twenty-nine cars in just a few years. And yet, by our own arithmetic, the newer car is the better one at the thing Pagani cares about most: power for every kilogram.""",
   "Pagani Zonda and Pagani Utopia", "PAGANI ZONDA VS UTOPIA")
sc("""So what really changed in twenty-three years of Pagani? Where did the company keep the same recipe, and where did it throw it away? We went through the published numbers, and the answers surprised us. Starting with the engine, and a detail that most comparisons skip.""",
   "Pagani Zonda", "WHAT REALLY CHANGED?")
sc("""Every number in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Pagani Utopia", "EVERY NUMBER IS SOURCED")

# ---------- 1. TWO CARS ----------
ch("Two cars, two eras")
sc("""Wikipedia says the Pagani Zonda made its debut at the Geneva Motor Show in nineteen ninety-nine. The Utopia was unveiled in Milan on the twelfth of September, twenty twenty-two. By our own arithmetic, that is twenty-three years and a few months between them, almost a quarter of a century.""",
   "Pagani Zonda Geneva 1999", "1999 VS 2022")
sc("""Inside Pagani, the cars have codes. Wikipedia says the Zonda is the C eight, the Huayra the C nine, and the Utopia the C ten. So the Utopia is only the third Pagani road car design in all those years. A company that has built so few models can compare them like members of one family.""",
   "Pagani models", "C8 · C9 · C10")
sc("""The Zonda has a famous name story. Wikipedia says it was planned as the Fangio F one, after the Formula One champion Juan Manuel Fangio. After Fangio died in nineteen ninety-five, it was renamed for the Zonda wind, a hot air current above Argentina. The Utopia, Top Gear says, takes its name from Sir Thomas More.""",
   "Juan Manuel Fangio", "FANGIO F1 → ZONDA · UTOPIA FROM THOMAS MORE")
sc("""Both cars were designed by the same man. Wikipedia lists Horacio Pagani as designer of the Utopia, and he is the founder of the company that made the Zonda. So, unlike most comparisons between old and new models, we are not comparing different design teams. We are comparing one designer with himself, twenty-three years apart.""",
   "Horacio Pagani", "SAME DESIGNER, 23 YEARS APART")

sc("""Time is the next surprise. Wikipedia says on Horacio Pagani's page that the first Zonda took seven years to complete. Wikipedia's Utopia page says the Utopia was developed over more than six years. So despite twenty-three years of technology, the time it takes a small company to make a new Pagani has barely changed. Some things cannot be hurried.""",
   "Pagani design studio", "ZONDA: 7 YEARS · UTOPIA: 6+ YEARS")
sc("""The Zonda also began with a crash. Wikipedia says that of the five Zondas with the six litre engine, one, chassis zero zero one, was used for crash testing and homologation, and another was a demonstrator. So of the first five cars Pagani ever built, one was destroyed in testing. The Utopia had eight prototypes to take that role.""",
   "Crash test", "ZONDA C12: 1 OF 5 CARS WAS CRASHED")
# ---------- 2. ENGINES ----------
ch("Round one: the engine")
sc("""Start with the engines. Wikipedia says the first Zonda, the C twelve, used a six litre Mercedes-Benz V twelve. The C twelve S used a seven thousand ten cubic centimetre engine tuned by Mercedes-AMG. Later cars, from the S seven point three, used a seven thousand two hundred ninety-one cubic centimetre engine built by Mercedes-AMG.""",
   "Pagani Zonda V12", "6.0 → 7.0 → 7.3 LITRES")
sc("""The Zonda F, in two thousand five, used a seven point three litre Mercedes-AMG M two ninety-seven V twelve. Wikipedia lists six hundred two metric horsepower at six thousand one hundred fifty r p m, and seven hundred sixty newton-metres of torque. None of these Zonda engines is turbocharged. They were big, naturally aspirated V twelves.""",
   "Pagani Zonda F", "ZONDA F: 7.3 L · 602 PS")
sc("""The Utopia is different. Wikipedia says it has a five point nine eight litre Mercedes-AMG M one fifty-eight twin-turbocharged V twelve. That is about eighteen percent smaller than the seven thousand two hundred ninety-one cubic centimetre engine, by our own arithmetic. Smaller, but with turbochargers, and more powerful.""",
   "Pagani Utopia V12", "UTOPIA: 5.98 L TWIN-TURBO")
sc("""How much more powerful? Wikipedia lists eight hundred sixty-four metric horsepower for the Utopia, and eleven hundred newton-metres of torque. Compared with the Zonda F's six hundred two, that is about forty-four percent more power. And compared with the first Zonda C twelve, at four hundred eight or four hundred fifty, it is roughly double.""",
   "Pagani Utopia engine", "864 PS VS 602 PS: +44%")
sc("""The Wikipedia page on the Zonda gives two figures for the C twelve's power, four hundred eight or four hundred fifty metric horsepower, and two ranges for its torque. We do not know which is right, so we give both. Against the higher figure the Utopia has about one point nine times more power. Against the lower, about two point one.""",
   "Pagani Zonda C12", "C12: 408 OR 450 PS (SOURCES DIFFER)")
sc("""And the torque? The Zonda F had seven hundred sixty newton-metres, the Utopia eleven hundred. By our arithmetic, that is about forty-five percent more. Wikipedia also says the Utopia's torque is available between two thousand eight hundred and five thousand nine hundred r p m. Turbos fill the low end that a big naturally aspirated engine needs revs to reach.""",
   "Pagani Utopia turbo", "1,100 NM VS 760 NM")
sc("""Top Gear says the Utopia's engine is built specially for Pagani. Attic Capital's interview summary says the Huayra's engine was made only for Pagani too. And the Zonda, in the same source, began when Mercedes agreed to supply a V twelve in nineteen ninety-four. Pagani has always built its cars around an engine that Mercedes-AMG shaped for it.""",
   "Mercedes-AMG engine", "A MERCEDES-AMG V12, ALWAYS")

sc("""Between the two sits the Huayra. Wikipedia says it was revealed in twenty eleven with a six litre twin-turbo Mercedes-AMG V twelve, seven hundred forty metric horsepower and one thousand newton-metres. A hundred were built, each costing one million pounds before options. The Utopia, by our arithmetic, adds about seventeen percent power to that.""",
   "Pagani Huayra", "THE HUAYRA IN BETWEEN: 740 PS · 100 CARS")
sc("""The Huayra B C, named after Benny Caiola, Horacio Pagani's friend and the first Pagani customer, made seven hundred sixty-four metric horsepower and weighed one thousand two hundred eighteen kilograms, according to Wikipedia. Thirty were built. By our arithmetic, that is about point six three. The Utopia, at point six eight, is already close to that special edition.""",
   "Pagani Huayra BC", "HUAYRA BC: 764 PS · 1,218 KG")
# ---------- 3. WEIGHT ----------
ch("Round two: weight, the twist")
sc("""Now the twist. Wikipedia lists dry weights for the Zonda. The C twelve weighed one thousand two hundred fifty kilograms. The S and the roadster, one thousand two hundred eighty. The Cinque, Cinque Roadster and Tricolore, one thousand two hundred ten. The R and the Revolución, one thousand seventy. The Utopia weighs one thousand two hundred eighty.""",
   "Pagani Zonda Cinque", "ZONDA: 1,070–1,280 KG · UTOPIA: 1,280 KG")
sc("""So after twenty-three years, the Utopia weighs the same as the Zonda S. That is remarkable. The Utopia has stricter safety rules, modern electronics and more comfort to carry. Yet it is not heavier than a two thousand car, and it is only thirty kilograms heavier than the nineteen ninety-nine C twelve.""",
   "Pagani Utopia", "SAME WEIGHT AS THE ZONDA S")
sc("""Now divide power by weight. The Zonda S seven point three had five hundred fifty-five metric horsepower and one thousand two hundred eighty kilograms, about point four three metric horsepower per kilogram, by our own arithmetic. The Utopia has eight hundred sixty-four and the same weight, about point six eight. That is more than fifty percent better.""",
   "Pagani power to weight", "0.43 VS 0.68 PS/KG (OUR ARITHMETIC)")
sc("""Even the special editions lose. The Zonda Cinque has six hundred seventy-eight metric horsepower and one thousand two hundred ten kilograms. By our arithmetic, that is about point five six. The Utopia is roughly twenty percent better than a Cinque, which was one of the most extreme Zondas ever sold, with only five built.""",
   "Pagani Zonda Cinque", "UTOPIA BEATS THE CINQUE BY ~20%")
sc("""And the HP Barchetta, the last Zonda, had eight hundred metric horsepower and weighed one thousand two hundred fifty kilograms. By our arithmetic, about point six four. The Utopia is still ahead, by around five percent. But the gap between them is much narrower. Pagani's last Zonda was already very close to its newest car.""",
   "Pagani Zonda HP Barchetta", "HP BARCHETTA: 0.64 PS/KG")
sc("""There is one car that the Utopia does not beat on weight. The Zonda R and the Revolución weigh just one thousand seventy kilograms, according to Wikipedia, because they are track cars. The sources do not give their power in the same way, so we make no ratio. But the lightest Zonda is more than two hundred kilograms lighter than the Utopia.""",
   "Pagani Zonda R", "TRACK-ONLY ZONDA R: 1,070 KG")

sc("""Several Zondas show how far the company pushed the idea. Wikipedia lists the one-off series with a seven hundred sixty metric horsepower engine, the Revolución, introduced at the Goodwood Festival of Speed in twenty twelve, and the Zonda Revo Barchetta, a one-off combining the Revolución body kit with the Barchetta's open top. Each is a custom job, not a catalogue car.""",
   "Pagani Zonda Revolución", "ONE-OFFS: REVOLUCIÓN · REVO BARCHETTA")
sc("""Against the seven hundred sixty horsepower one-offs, the Utopia's eight hundred sixty-four is about fourteen percent more, by our arithmetic. So the new standard car has more power than the most powerful normal Zonda, and only the final HP Barchetta, at eight hundred, came close. The newest Pagani starts where the last Zonda ended.""",
   "Pagani Zonda 760", "UTOPIA IS +14% OVER THE 760 PS ONE-OFFS")
# ---------- 4. SPEED ----------
ch("Round three: speed and records")
sc("""Now speed. This is where the sources are tricky, because the Utopia has no published performance numbers that we could find. Wikipedia lists none, and Top Gear's launch article gives no acceleration time or top speed. So for the Utopia, we only have the engine and the weight. For the Zonda, we have a lot more.""",
   "Pagani Utopia", "UTOPIA: NO OFFICIAL SPEED FIGURES FOUND")
sc("""Wikipedia says the Zonda C twelve S reached a hundred kilometres per hour in three point seven seconds, with a top speed of three hundred thirty-five kilometres per hour. The Zonda F reached three hundred forty-five. The Cinque, according to the same page, went from zero to a hundred in three point four seconds.""",
   "Pagani Zonda F", "ZONDA CINQUE: 0–100 IN 3.4 SECONDS")
sc("""The Cinque also had enormous downforce. Wikipedia says it produced seven hundred fifty kilograms of downforce at three hundred fifty-five kilometres per hour. That is a lot of load pressing the car into the road. It tells you the Cinque was built to be driven fast, and not only to be admired in a collection.""",
   "Pagani Zonda Cinque aero", "750 KG OF DOWNFORCE AT 355 KM/H")
sc("""On the track, the Zonda has real records. Wikipedia's Pagani page says that on the thirtieth of June, twenty ten, a Zonda R completed the Nürburgring Nordschleife in six minutes forty-seven seconds, a production-car record that beat the Ferrari five ninety-nine X X. A Zonda F Clubsport, driven by Marc Basseng, did seven twenty-four point seven.""",
   "Nürburgring Nordschleife", "ZONDA R: 6:47 AT THE NÜRBURGRING (2010)")
sc("""Top Gear's test track also features. Wikipedia says a Zonda Roadster F Clubsport lapped it in one minute seventeen point eight, beating the Bugatti Veyron on the lap. But it lost a quarter-mile drag race to the Veyron by nearly two and a half seconds. So the Zonda was a car for corners, not for straight lines.""",
   "Top Gear test track", "BEAT THE VEYRON ON A LAP, LOST THE DRAG RACE")
sc("""The Zonda even went to Le Mans. Wikipedia says the Zonda G R, a racing version developed by Carsport Zonda, weighed one thousand one hundred kilograms, and retired from the two thousand three twenty-four hours of Le Mans after ten laps because of a gearbox failure. A short race, but a Zonda made it to the starting grid.""",
   "Le Mans 24 Hours", "ZONDA GR AT LE MANS 2003")
sc("""So the honest summary on speed is this. The Zonda has a proud record book. The Utopia, as of our sources, has none. It may be faster than any Zonda, as the power-to-weight figures suggest. It may not be. But nobody has published the numbers, and we will not guess.""",
   "Pagani Utopia vs Zonda", "THE UTOPIA'S RECORD BOOK IS STILL BLANK")

sc("""The Zonda ended in a particular way. Wikipedia says the HP Barchetta was unveiled at the two thousand seventeen Pebble Beach Concours d'Elegance, with eight hundred metric horsepower and eight hundred fifty newton-metres, and marks the end of Zonda production. Three were built, and Horacio Pagani kept one himself.""",
   "Pebble Beach Concours", "2017: THE LAST ZONDA")
sc("""By our arithmetic, five years passed between the HP Barchetta in twenty seventeen and the Utopia in twenty twenty-two. In that time Pagani did not switch to hybrids, as other makers did. It built another Mercedes-AMG V twelve with twin turbochargers, and a gearbox choice that includes a clutch pedal. It kept going the way it always had.""",
   "Pagani Utopia", "5 YEARS LATER: ANOTHER V12")
# ---------- 5. GEARBOX ----------
ch("Round four: the gearbox")
sc("""Now the part where the new car goes backwards. Wikipedia says the Zonda Cinque used a six-speed automated manual, with shifts in under one hundred milliseconds. The Utopia uses a seven-speed Xtrac gearbox, offered as a pure manual or an automated manual. In an era of faster gearboxes, Pagani added a true clutch pedal.""",
   "Pagani manual gearbox", "A TRUE MANUAL RETURNS")
sc("""Supercar Blondie says Pagani added the manual because it was especially important, as it is what customers demanded. Top Gear says there is no dual-clutch system at all. So here is a car with seven forward gears, a clutch pedal and a stick. Technology moved forward in twenty-three years, and Pagani's customers asked for the opposite.""",
   "Pagani Utopia gear lever", "CUSTOMERS DEMANDED IT")

# ---------- 6. RARITY ----------
ch("Round five: rarity")
sc("""Production numbers are another contrast. Wikipedia says that as of twenty nineteen, one hundred forty Zondas had been built, including development cars. Within that, the C twelve had five cars with the six litre engine, the Zonda F was limited to twenty-five, the Roadster F to twenty-five, and forty roadsters used the S engine.""",
   "Pagani Zonda production", "140 ZONDAS IN TOTAL")
sc("""The special editions were far smaller. Wikipedia lists five Cinque coupés and five Cinque roadsters, three Tricolores and three HP Barchettas. By our arithmetic, those last four editions together make only sixteen cars. Every one of them is rarer than the rarest Utopia, since Pagani plans ninety-nine coupés.""",
   "Pagani Zonda Tricolore", "CINQUE 5+5 · TRICOLORE 3 · BARCHETTA 3")
sc("""The Utopia changes the scale. Wikipedia says Pagani plans ninety-nine coupés, excluding the eight prototypes, and a hundred thirty roadsters. By our arithmetic that is two hundred twenty-nine cars, about sixty-four percent more than the entire Zonda production. And Wikipedia says all ninety-nine coupés were assigned to customers.""",
   "Pagani Utopia production", "229 UTOPIAS VS 140 ZONDAS")
sc("""So the Zonda is rarer in total, but the Utopia is more of a mass-produced car, if you can use those words about Pagani. The company has grown. Pagani's release says the Utopia coupé and roadster were developed jointly, unlike the Zonda and Huayra roadsters, which came later.""",
   "Pagani factory", "A BIGGER COMPANY NOW")

sc("""Customers shaped many Zondas. Wikipedia says the Cinque was developed at the request of a Hong Kong dealer, with deliveries set for June two thousand nine. The Tricolore was a tribute to the Frecce Tricolori, the Italian air force's aerobatic team, on its fiftieth anniversary. Both are tiny editions, five and three cars, created for particular people or ideas.""",
   "Pagani Zonda Tricolore", "THE CINQUE WAS BUILT FOR A DEALER'S REQUEST")
# ---------- 7. PRICE ----------
ch("Round six: price")
sc("""Now money. Wikipedia says the Zonda Tricolore was priced at one point two million pounds. The Utopia starts at two point one nine million dollars according to Wikipedia, and at two million, one hundred seventy thousand euros according to Supercar Blondie. Different currencies and different years, so be careful, but the direction is clear.""",
   "Pagani Zonda Tricolore", "TRICOLORE: £1.2M · UTOPIA: €2.17M")
sc("""The Utopia roadster is more expensive. Wikipedia says the base price is three point four million dollars, or three point one million euros. And Pagani's own release says the roadster starts at three point one million euros, excluding local taxes. So the open car costs, by our arithmetic, about forty-three percent more than the closed one in euros.""",
   "Pagani Utopia Roadster", "ROADSTER: +43% OVER THE COUPÉ")
sc("""The Zonda has also set auction records. The Gulf News reported that a Zonda Riviera, a car with seven hundred sixty horsepower and the seven point three litre engine, sold for five point five million dollars at a Silverstone Auctions sale in Riyadh in twenty nineteen. Wikipedia's Pagani page says two of the three HP Barchettas cost fifteen million dollars each.""",
   "Pagani Zonda Riviera", "ZONDA RIVIERA: $5.5M AT AUCTION")
sc("""So the old Zonda is no cheap alternative. A well-chosen Zonda can cost more than a new Utopia. The sources give one auction and one claim about Barchettas, not a market study. But they show that Pagani cars are collected like art, and the older cars have had time to be priced as such.""",
   "Pagani Zonda collection", "THE OLD CAR CAN COST MORE")

sc("""Put the Utopia's chassis next to the older cars. Top Gear says it has a carbo-titanium monocoque with tubular alloy steel subframes, forged aluminium double wishbones, helical springs and active dampers. Brakes are carbon ceramic, with six-piston calipers at the front and four at the rear. Wheels are twenty-one inch at the front and twenty-two at the rear.""",
   "Pagani Utopia chassis", "CARBON CERAMIC BRAKES · 21/22-INCH WHEELS")
# ---------- 8. DESIGN ----------
ch("Round seven: design")
sc("""The two cars look different on purpose. Top Gear says the Utopia lacks the big wings, splitters and vents typical of Pagani. Pagani says each car begins with an aesthetic shock, and calls the Utopia's lines flowing and curvaceous. The Zonda, in the Attic Capital interview, was seen as futuristic and provocative in nineteen ninety-nine.""",
   "Pagani Utopia and Zonda design", "PROVOCATIVE THEN, RESTRAINED NOW")
sc("""The interior has changed as well. Supercar Blondie says the Utopia's instrumentation is analogue, aside from one small screen for the driver. Top Gear says the structure is a carbo-titanium monocoque. Pagani's release says one car holds over forty composite formulas. The Zonda was already famous for carbon fibre. The Utopia takes the idea much further.""",
   "Pagani Utopia cockpit", "40+ COMPOSITE FORMULAS")
sc("""Both cars keep a few traditions. The Utopia has butterfly doors, according to Wikipedia, and Supercar Blondie says four central exhaust tips are a Pagani hallmark. In other words, the Utopia may look quieter than a Zonda, but a Pagani owner would recognise it as the same family from behind.""",
   "Pagani exhaust tips", "BUTTERFLY DOORS · FOUR CENTRAL EXHAUSTS")

# ---------- 9. VERDICT ----------
ch("The verdict")
sc("""So here is the scorecard. Engine: the Utopia, with forty-four percent more power than a Zonda F. Weight: a tie with the Zonda S, but behind the track Zondas. Power-to-weight: the Utopia, by fifty percent over the S. Records: the Zonda, so far. Rarity per edition: the Zonda. Gearbox: a draw, depending on your taste.""",
   "Pagani Zonda vs Utopia", "SCORECARD")
sc("""But the numbers do not tell the whole story. Many Pagani buyers do not choose between the two on a spreadsheet. They choose the Zonda for its history, its naturally aspirated sound, and its place in the story of the hypercar. They choose the Utopia for the new manual gearbox and the latest work of the same designer.""",
   "Pagani owners", "THE ZONDA FOR HISTORY, THE UTOPIA FOR NOW")
sc("""We also want to be fair about the limits. We have no independent test of the Utopia, no lap time, and no published acceleration. So this comparison is of specifications and the company's own statements. When real figures appear, the verdict may change. Our scorecard is a map of the numbers we could verify.""",
   "Pagani Utopia", "A COMPARISON OF PUBLISHED NUMBERS")
sc("""Which would you choose, the Zonda or the Utopia? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Utopia, work out what it really costs to own a Pagani, and tell the story of Horacio Pagani, the man behind both cars.""",
   "Pagani Zonda and Utopia", "ZONDA OR UTOPIA?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more comparisons between the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video90", "Pagani Zonda vs Utopia: The Difference Nobody Explains", [
    "Wikipedia, Pagani Zonda: https://en.wikipedia.org/wiki/Pagani_Zonda",
    "Wikipedia, Pagani Utopia: https://en.wikipedia.org/wiki/Pagani_Utopia",
    "Wikipedia, Pagani (company): https://en.wikipedia.org/wiki/Pagani_(company)",
    "Top Gear, This is the brand new Pagani Utopia: https://www.topgear.com/car-news/first-look/brand-new-pagani-utopia-v12-engined-throwback",
    "Supercar Blondie, The Pagani Utopia is here: https://supercarblondie.com/pagani-utopia-c10-v12-manual-supercar-revealed/",
    "Pagani Automobili press release, Pagani Utopia Roadster: https://www.pagani.com/press/utopia-roadster/",
    "Gulf News, Pagani Zonda Riviera sold for $5.5 million at Riyadh Season car auction: https://gulfnews.com/amp/auto/news/pagani-zonda-riviera-sold-for-55-million-at-riyadh-season-car-auction-1.1574581887664",
    "Attic Capital, Horacio Pagani and the Zonda: https://atticcapital.com/horacio-pagani-zonda/",
], "B")
