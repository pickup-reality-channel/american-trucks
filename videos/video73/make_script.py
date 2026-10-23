import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Chevrolet Corvette Z06 has the most powerful naturally aspirated V8 ever put in a production car, according to Chevrolet. Six hundred seventy horsepower, no turbos, no superchargers, and a redline of eight thousand six hundred r p m. But two facts about this car are almost never mentioned. One involves a wrecked Ferrari. The other is hidden inside every single engine.""",
   "Chevrolet Corvette Z06 C8", "2 THINGS YOU DIDN'T KNOW ABOUT THE Z06")
sc("""Here is the hint. To build this American engine, General Motors bought a crashed Italian supercar and took it apart. And when you open up a Z06 engine, you will find dozens of small symbols that have nothing to do with making power. Both stories are true, and both are documented.""",
   "Ferrari 458 Italia", "A CRASHED FERRARI?")
sc("""Along the way, you will see the race car this engine came from, the Le Mans win that ended an era, the Z06's lap of the Nürburgring, the recall that stopped sales in twenty twenty-five, and what happened to the people who paid huge markups. Every number is from a published source, listed in the description.""",
   "Corvette C8.R Le Mans", "EVERY NUMBER IS SOURCED")
sc("""And there is a twist at the end about price. The car that dealers once sold for far above sticker was later sitting on lots by the thousands. But first, the engine.""",
   "Chevrolet Corvette Z06 dealership", "THE PRICE TWIST")

# ---------- 1. THE CAR ----------
ch("The engine")
sc("""The Z06 was unveiled on the twenty-sixth of October twenty twenty-one, according to Wikipedia, and went into production in twenty twenty-two as a twenty twenty-three model. It is based on the eighth-generation Corvette, the C8, the first Corvette with its engine behind the driver.""",
   "Chevrolet Corvette Z06 reveal", "REVEALED OCT 26, 2021")
sc("""That move was huge. The Associated Press reported in July twenty nineteen that Corvettes had used front-mounted engines for sixty-six years. Chief engineer Tadge Juechter explained the change simply. He said they were reaching the performance limitations of a front-engine car. The Z06 is the car that takes full advantage of that new layout.""",
   "Corvette C8 Stingray mid engine", "66 YEARS OF FRONT ENGINES")
sc("""With the engine behind the seats, more weight sits over the rear wheels, which helps traction when accelerating out of corners. That is why the Z06 can put six hundred seventy horsepower through only its rear tires and still reach sixty miles per hour in under three seconds. The layout made this engine possible.""",
   "Corvette Z06 rear three quarter", "WEIGHT OVER THE REAR WHEELS")
sc("""Its engine is called the L T six. The Drive reported the details. A five point five liter V8 with two overhead camshafts per bank, making six hundred seventy horsepower at eight thousand four hundred r p m, and four hundred sixty pound-feet of torque at six thousand three hundred. The redline is eight thousand six hundred.""",
   "Corvette LT6 engine", "5.5L LT6: 670 HP, 8,600 RPM")
sc("""That is twenty horsepower more than the previous Z06, which used a supercharged six point two liter V8. Chevrolet's new engine makes more power with less displacement and without forced induction. Hagerty described it as the most powerful naturally aspirated production V8 ever.""",
   "Corvette C7 Z06", "MORE POWER, NO SUPERCHARGER")
sc("""The Drive listed forged aluminum pistons, forged titanium connecting rods, a six-stage dry-sump oil system, and twin eighty-seven millimeter throttle bodies. Zero to sixty miles per hour takes a claimed two point six seconds. This is a long way from the pushrod V8s that powered Corvettes for decades.""",
   "Corvette Z06 engine bay", "0-60 IN 2.6 SECONDS")
sc("""And the most important part is the crankshaft. The L T six uses a flat-plane crank. In a typical American V8, the crankshaft throws are set at ninety degrees to each other, which gives that deep, rumbling sound. In a flat-plane crank, they are set at one hundred eighty degrees, flat, like in many Ferrari V8s.""",
   "flat plane crankshaft", "THE FLAT-PLANE CRANK")
sc("""A flat-plane crank is lighter, and it lets the engine rev higher and faster. Autoblog reported that the L T six's forged steel crank is thirty-three percent lighter than the one in the regular Stingray's engine. It also changes the sound into a high-pitched scream, closer to a European race car than a muscle car. And that is where our first secret begins.""",
   "Corvette Z06 exhaust", "33% LIGHTER CRANK")

# ---------- 2. SECRET ONE ----------
ch("Secret 1: the wrecked Ferrari")
sc("""Secret number one. To learn how to build a flat-plane V8, General Motors bought a Ferrari. Not a new one. Autoblog reported that GM bought a wrecked Ferrari four fifty-eight Italia from Europe, for about twenty-five thousand dollars, and tore it down to study its flat-plane crank.""",
   "Ferrari 458 Italia", "SECRET 1: GM BOUGHT A WRECKED FERRARI")
sc("""Think about that. The engineers behind America's sports car, the car that has competed against Ferrari and Porsche for decades, went shopping for a crashed Italian supercar and took its engine apart piece by piece. Twenty-five thousand dollars is a tiny amount in a car development budget, and it bought something valuable, a close look at how Ferrari had solved the problem.""",
   "Ferrari 458 engine", "$25,000 FOR A CRASHED 458")
sc("""The Ferrari four fifty-eight was a good choice. It used a high-revving, naturally aspirated V8 with a flat-plane crank, one of the last of its kind before Ferrari moved to turbocharging with the four eighty-eight. It was exactly the type of engine Chevrolet wanted to understand.""",
   "Ferrari 458 Italia rear", "THE LAST FERRARI OF ITS KIND")
sc("""This is not unusual in the car industry. Carmakers routinely buy and dismantle rivals' cars to study them. It is called benchmarking, or teardown. But it is rare to hear a story this specific, a crashed Ferrari helping to shape an American V8.""",
   "car engineering workshop", "IT'S CALLED BENCHMARKING")
sc("""Here is the twist. The L T six did not end up as a copy of a Ferrari engine. Autoblog said its cylinder block, heads, valvetrain, and fuel system are shared with the Corvette C8 dot R race car. The Drive reported that a version of the engine had been in testing since twenty nineteen, when it was first used in that race car. The Ferrari teardown was research. The final engine was born on the race track.""",
   "Corvette C8.R race car", "BORN ON THE RACE TRACK")
sc("""And Chevrolet kept one link with its past. Autoblog said Chevrolet still calls the L T six a Small Block, even though it is a clean-sheet engine with four camshafts. The Drive explained the only real connection. The block keeps the classic four point four inch bore spacing of the traditional small-block Chevy. The rest is new.""",
   "Chevrolet small block V8", "STILL CALLED A SMALL BLOCK")

# ---------- 3. SECRET TWO ----------
ch("Secret 2: hand-built, with hidden rockets")
sc("""Secret number two. Every Z06 engine is built by hand, by one person. Autoblog reported that a single technician assembles each engine at Chevrolet's Performance Build Center in Bowling Green, Kentucky, a job that takes about three hours. And when the engine is finished, the technician signs a plaque that goes on it.""",
   "Corvette engine plaque", "SECRET 2: ONE PERSON, ONE ENGINE")
sc("""Bowling Green is a fitting place for it. Every C8 Corvette is built at GM's Bowling Green Assembly plant in Kentucky, where production of the C8 officially began on the third of February twenty twenty, according to Wikipedia. The engine builders work in the same city, so each Z06 engine and the car around it come from the same small corner of Kentucky.""",
   "Bowling Green Kentucky Corvette", "BOWLING GREEN, KENTUCKY")
sc("""That is the kind of tradition people associate with Mercedes A M G or with Italian supercars. Here, it is part of a Chevrolet that starts at around one hundred twenty thousand dollars. Autoblog said each engine then gets a twenty-minute full-load test on a dynamometer before it goes into a car.""",
   "Bowling Green Corvette plant", "SIGNED AND DYNO TESTED")
sc("""But the strangest detail is hidden inside. Autoblog reported that the engine project had an internal code name, Gemini, after the NASA space program of the nineteen sixties. And the engineers hid fifty-four small rocket symbols throughout each engine. Fifty-four rockets, in places most owners will never see.""",
   "NASA Gemini rocket launch", "54 HIDDEN ROCKETS")
sc("""Why Gemini? Autoblog connects the code name to NASA's Gemini program. Here is an interesting link. In the nineteen sixties, many American astronauts famously drove Corvettes. So naming a Corvette race engine after a NASA program fits a long relationship between the car and the space age.""",
   "astronauts Corvette 1960s", "THE GEMINI CODE NAME")
sc("""And here is the twist. Those engine builders are building a race-derived engine at a rate of a few hours each, for a car sold in tens of thousands. Wikipedia lists more than fifty-three thousand Corvettes of all types produced for the twenty twenty-three model year. Not all were Z06s, but it shows the scale at which Chevrolet was building something close to a hand-made race engine.""",
   "Corvette production line", "HAND-BUILT AT SCALE")
sc("""There is even a break-in rule for new owners. Autoblog said the engine has a five-hundred-mile break-in period, with limited torque in first and second gear. Chevrolet wants each hand-built engine to settle in before it is pushed to its eight thousand six hundred r p m redline.""",
   "Corvette Z06 tachometer", "500-MILE BREAK-IN")

# ---------- 4. MORE ENGINEERING ----------
ch("Built for the track")
sc("""The engine also had to survive the track. Autoblog reported that the Z06's total cooling capacity is fifty percent higher than a Stingray with the Z fifty-one package, with five radiators. A removable front panel can make the grille opening seventy-five percent larger for track days.""",
   "Corvette Z06 front grille", "FIVE RADIATORS")
sc("""Even the air conditioning was designed for the track. Autoblog said it is built to cool the cabin with an outside temperature of one hundred degrees Fahrenheit, at full speed. And the valvetrain, with titanium intake valves and sodium-filled exhaust valves, is designed never to need adjustment over the engine's life, according to GM.""",
   "Corvette Z06 interior", "TRACK-RATED AIR CONDITIONING")
sc("""The body is wider too. The Drive said the Z06 is three point six inches wider than the regular Stingray, so it can fit rear tires three hundred forty-five millimeters wide. With the optional Z zero seven package, it gets carbon fiber aerodynamic parts, carbon-ceramic brakes, and carbon fiber wheels that save forty-one pounds.""",
   "Corvette Z06 Z07 package", "Z07: CARBON EVERYTHING")
sc("""The exhaust was engineered carefully too. Autoblog reported that valves in the center pipes can be tuned in two-degree steps, through three presets called Tour, Sport, and Track. The new design cuts back pressure by twenty-one percent compared with the previous Z06, and the muffler is twenty pounds lighter than the one on the Stingray.""",
   "Corvette Z06 exhaust tips", "TOUR, SPORT, TRACK")
sc("""Hagerty reported that the Z zero seven package helps the car make seven hundred thirty-four pounds of downforce at one hundred eighty-six miles per hour, compared with three hundred sixty-five pounds for the standard car. Chevrolet claims the Z zero seven can reach one point two two g of lateral grip.""",
   "Corvette Z06 rear wing", "734 LB OF DOWNFORCE")
sc("""And unlike many track cars, the Z06 comes with a folding roof option. The Drive reported that it is offered as a coupe and as a convertible, and that Chevrolet says both share the same suspension tuning. So a buyer can choose a hand-built, eight thousand six hundred r p m engine with the sky above, which few rivals at this price can offer.""",
   "Corvette Z06 convertible", "COUPE OR CONVERTIBLE")

# ---------- 5. THE RACE CAR ----------
ch("The race car")
sc("""Now, the race car. The C eight dot R was the car that first used a version of this engine. And in June twenty twenty-three, Racer reported, the number thirty-three Corvette C eight dot R won the G T E Am class at the twenty-four hours of Le Mans, driven by Ben Keating, Nico Varrone, and Nicky Catsburg.""",
   "Corvette C8.R Le Mans 2023", "LE MANS 2023: CLASS WIN")
sc("""It was Corvette's ninth class win at Le Mans, and it came in the final race of the G T E category at the circuit, Racer reported. So the race car that gave the Z06 its engine finished its era with a victory at the most famous endurance race in the world.""",
   "Le Mans 24 hours", "NINTH WIN, FINAL GTE RACE")
sc("""And the link goes back to the beginning. Hagerty quoted Corvette executive chief engineer Tadge Juechter saying that racing was the reason the Z06 was developed in nineteen sixty-three. The very first Z06 was a racing package, created by Zora Arkus-Duntov, often called the father of the Corvette.""",
   "1963 Corvette Sting Ray", "THE FIRST Z06: 1963")
sc("""Hagerty said the nineteen sixty-three Z06 package included a three hundred sixty horsepower, three hundred twenty-seven cubic inch V8, a limited-slip differential, heavy-duty suspension, and a thirty-six gallon fuel tank. Only one hundred ninety-nine were built that first year, and Motor Authority said the first cars went straight to race teams.""",
   "1963 Corvette Z06 race", "ONLY 199 BUILT")
sc("""Why was it so secretive? Hagerty explained that in early nineteen fifty-seven, American carmakers agreed to stop direct racing involvement, after the nineteen fifty-five Le Mans disaster that killed more than eighty spectators. So Duntov listed his racing equipment as a regular production option, code-named Zora's Option six, to avoid alarming GM management.""",
   "1955 Le Mans", "ZORA'S OPTION 6")
sc("""Hagerty said the package cost about one thousand eight hundred eighteen dollars on a coupe at launch. After problems with the special wheels and the big tank, those parts were deleted, and the price dropped to about one thousand two hundred ninety-four dollars. A small, strange beginning for a famous name.""",
   "1963 Corvette split window", "$1,818.45 IN 1963")
sc("""Then the name disappeared for almost forty years. It returned in two thousand one on the C five Corvette. Hagerty said that car used the L S six V8, with three hundred eighty-five horsepower at launch, later four hundred five, and it came only as a fixed-roof hardtop with a six-speed manual.""",
   "Corvette C5 Z06", "2001: THE NAME RETURNS")
sc("""The C six Z06 of twenty oh six went bigger, with a seven liter, four hundred twenty-seven cubic inch V8 making five hundred five horsepower, and an aluminum frame thirty percent lighter than steel, Hagerty reported. Then the C seven Z06 of twenty fifteen used a supercharged six point two liter V8 with six hundred fifty horsepower.""",
   "Corvette C6 Z06", "505 HP, THEN 650 HP")
sc("""So the C eight Z06 broke the pattern. After two decades of bigger engines and then a supercharger, Chevrolet went to a smaller, high-revving engine with no supercharger at all. And it still made more power than any Z06 before it.""",
   "Corvette C8 Z06", "SMALLER ENGINE, MORE POWER")

# ---------- 6. THE NUMBERS ON TRACK ----------
ch("The Nürburgring")
sc("""So how fast is it? In twenty twenty-five, Chevrolet took the Z06 to the Nürburgring Nordschleife in Germany. Top Gear reported a lap time of seven minutes eleven point eight two six seconds, driven by Aaron Link.""",
   "Nürburgring Nordschleife", "NÜRBURGRING: 7:11.826")
sc("""On the same trip, the more powerful twin-turbo Corvette Z R one lapped in six minutes fifty point seven six three seconds, and the hybrid Z R one X in six minutes forty-nine point two seven five seconds, Top Gear said. At that moment, those were the fastest laps ever by American cars.""",
   "Corvette ZR1", "ZR1X: 6:49.275")
sc("""For comparison, Motor1 reported that the Porsche nine eleven G T three R S, the Z06's most famous rival, lapped the Nordschleife in six minutes forty-nine point three two eight seconds. That car is a lot more expensive, as we explain in the comparison video of this series.""",
   "Porsche 911 GT3 RS", "GT3 RS: 6:49.328")
sc("""So the Z06 is not the fastest Corvette around the Nürburgring. The twin-turbo Z R one and the hybrid Z R one X are both much quicker. But the Z06 is the one that keeps the old recipe of a naturally aspirated engine and rear-wheel drive. For many enthusiasts, that makes it the purest Corvette of the C eight family.""",
   "Corvette Z06 track", "THE PUREST C8")
sc("""It also sits in a clear spot in the price list. GM Authority reported twenty twenty-six prices of about seventy-two thousand dollars for the Stingray, one hundred eleven thousand for the hybrid E Ray, about one hundred twenty thousand for the Z06, and about one hundred eighty-two thousand for the Z R one, all including destination.""",
   "Corvette lineup", "Z06: ~$119,695 IN 2026")

# ---------- 7. THE RECALL ----------
ch("The recall")
sc("""Not everything went smoothly. In August twenty twenty-five, Auto123 reported a recall of about twenty-five thousand Corvettes, including Z06 models from twenty twenty-three to twenty twenty-five, and Z R one models. Sales were suspended.""",
   "Corvette Z06 recall", "RECALL: ~25,000 CARS")
sc("""The issue was fuel. According to the report, fuel could spill during refueling and reach the left radiator, creating a risk of fire. At the time, no remedy was available yet, and GM was reportedly considering a shield to divert spilled fuel away from possible ignition sources.""",
   "Corvette Z06 fuel filler", "FUEL SPILL RISK")
sc("""It is a reminder that high-performance packaging is hard. A mid-engined car puts a lot of hot, complex hardware close together. The Z06 has five radiators, a high-revving V8, and a fuel tank, all in a tight space. Getting everything right takes time.""",
   "Corvette Z06 side intake", "TIGHT PACKAGING")

# ---------- 8. THE PRICE TWIST ----------
ch("The price twist")
sc("""Now the price twist. When the Z06 arrived, demand was enormous. Hagerty said the twenty twenty-three model year sold out, with a base price of about one hundred nine thousand dollars including the gas guzzler tax. CarScoops reported that some dealers asked tens of thousands of dollars over sticker.""",
   "Corvette Z06 window sticker", "2023: SOLD OUT")
sc("""Then the market turned. In August twenty twenty-five, Motorious reported, GM's own inventory tracker showed about one thousand seven hundred Z06s sitting at American dealerships, and some were discounted by as much as twelve thousand dollars.""",
   "Corvette dealership lot", "2025: 1,700 UNSOLD")
sc("""Used prices dropped too. CarScoops reported a Z06 coupe with an original sticker of about one hundred forty-six thousand dollars and two thousand one hundred miles that sold on Bring a Trailer for one hundred eighteen thousand. Another, a twenty twenty-five Z06 convertible with the Z zero seven package and a sticker of about one hundred seventy thousand, sold for one hundred thirty-seven thousand five hundred.""",
   "Corvette Z06 auction", "$170K STICKER, $137.5K SALE")
sc("""So the car that people once paid huge premiums for became one of the better deals in the performance world, at least on the used market. The engine is the same hand-built, race-derived L T six. Only the hype changed.""",
   "Corvette Z06 Torch Red", "SAME ENGINE, LESS HYPE")
sc("""Why did the market cool so fast? Production is part of the answer. Wikipedia lists about fifty-three thousand Corvettes built for the twenty twenty-three model year and about forty-three thousand for twenty twenty-four, across all versions. When a car is built in those numbers, it is no longer rare, and the premium for getting one first disappears.""",
   "Corvette Bowling Green assembly", "53,785 BUILT IN 2023")

# ---------- 9. RECAP ----------
ch("The two things, again")
sc("""So let's recap the two things most people don't know about the Corvette Z06. Number one, to understand flat-plane V8s, GM bought a wrecked Ferrari four fifty-eight Italia from Europe for about twenty-five thousand dollars and tore it down. The final engine, though, came from the C eight dot R race car.""",
   "Ferrari 458 and Corvette Z06", "1. THE WRECKED FERRARI")
sc("""Number two, each L T six engine is assembled by a single technician in Bowling Green, Kentucky, in about three hours, signed with a plaque, and hides fifty-four small rocket symbols, a tribute to the Gemini code name. A race engine, built by hand, with a sense of humor.""",
   "Corvette LT6 engine plaque", "2. ONE BUILDER, 54 ROCKETS")
sc("""In the other videos of this series, we compare the Z06 with the Porsche nine eleven G T three R S, we work out what it really costs to own one, and we tell the insane story behind the mid-engine Corvette, a dream that took more than sixty years. Tell us in the comments which secret surprised you more.""",
   "Porsche 911 GT3 RS and Corvette Z06", "3 MORE ANGLES")
sc("""If you are shopping for a truck instead of a supercar, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Corvette Z06 sunset", "SUBSCRIBE: PICKUP REALITY")

save("video73", "2 Things You Didn't Know About the Corvette Z06", [
    "The Drive, 2023 Chevy Corvette Z06: 670 hp from a naturally aspirated flat-plane V8 (Oct 2021): https://www.thedrive.com/news/42882/2023-chevy-corvette-z06-670-hp-from-a-naturally-aspirated-flat-plane-v8",
    "Autoblog, 2023 Chevy Corvette Z06: the 9 coolest things (Feb 2022): https://www.autoblog.com/2022/02/18/2023-chevy-corvette-z06-coolest-9-things/",
    "Hagerty, 2023 Corvette Z06 arrives with world's most powerful naturally aspirated V-8: https://www.hagerty.com/media/?p=179871",
    "Hagerty, How the Corvette Z06 went from '60s racing package to modern monster: https://hagerty.com/media/?p=257365",
    "Motor Authority, The 2023 Corvette Z06 exists because of Zora Arkus-Duntov: https://www.motorauthority.com/news/1136291_the-2023-chevrolet-corvette-z06-exists-because-of-zora-arkus-duntov",
    "AP via WFYI, Corvette goes mid-engine for first time to raise performance (July 2019): https://www.wfyi.org/news/articles/corvette-goes-mid-engine-for-first-time-to-raise-performance",
    "GM Authority, 2026 Corvette pricing uncovered (June 2025): https://gmauthority.com/blog/2025/06/2026-corvette-pricing-uncovered/",
    "Wikipedia, Chevrolet Corvette (C8): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C8)",
    "Racer, Corvette Racing takes final GTE victory at Le Mans (June 2023): https://racer.com/2023/06/11/corvette-racing-fights-through-to-take-final-gte-victory-at-le-mans/",
    "Top Gear, Corvette ZR1X fastest American car ever around the Nürburgring (Aug 2025): https://www.topgear.com/car-news/usa/chevrolet-corvette-zr1x-fastest-american-car-ever-around-nurburgring",
    "Motor1, 2023 Porsche 911 GT3 RS laps the Nürburgring in 6:49.328: https://www.motor1.com/news/616069/porsche-911-gt3-rs-nurburgring-lap-record/",
    "Auto123, Corvette Z06 and ZR1 recall (Aug 2025): https://www.auto123.com/en/news/chevrolet-corvette-recall-z06-zr1/73126",
    "Motorious, Dealers offer deep discounts as over 1,700 Corvette Z06s sit unsold (Aug 2025): https://www.motorious.com/articles/news/dealers-offer-deep-discounts-as-over-1-700-chevrolet-corvette-z06s-sit-unsold",
    "CarScoops, Corvette Z06 prices crashing on the used market (Aug 2025): https://www.carscoops.com/2025/08/corvette-z06-prices-crashing-used-market-losses/",
    "CarScoops, Corvette Z06 flippers learn what happens when the hype fades (Oct 2025): https://www.carscoops.com/2025/10/corvette-z06-flippers-are-learning-the-hard-way-what-happens-when-the-hype-fades/",
], "A")
