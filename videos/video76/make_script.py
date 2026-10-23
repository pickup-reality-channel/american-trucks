import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""For sixty-six years, every Chevrolet Corvette had its engine in the front. Then, in July twenty nineteen, Chevrolet moved it behind the driver. It looked like a sudden revolution. It was not. The mid-engine Corvette was a dream that started in the nineteen fifties, survived secret prototypes, a rotary engine, an oil crisis, and the death of the man who wanted it most.""",
   "Chevrolet Corvette C8 Stingray", "THE INSANE STORY OF THE MID-ENGINE CORVETTE")
sc("""That man was Zora Arkus-Duntov, the engineer often called the father of the Corvette. He spent decades pushing for a mid-engine car, and he was told no again and again. When he reviewed a new front-engined Corvette in the nineteen nineties, he reportedly summed up his frustration in one short sentence. The engine is still in the front.""",
   "Zora Arkus-Duntov", "THE ENGINE IS STILL IN THE FRONT")
sc("""And here is the first twist. The father of America's sports car won his class at Le Mans twice driving a German car. A Porsche. That detail tells you a lot about where his ideas came from.""",
   "Porsche 550 Spyder Le Mans", "HE WON LE MANS IN A PORSCHE")
sc("""This is the story of how the Corvette finally got its engine behind the seats. Every date and number comes from a published source, listed in the description.""",
   "Corvette prototypes", "EVERY DATE IS SOURCED")

# ---------- 1. DUNTOV ----------
ch("The man behind the dream")
sc("""Wikipedia says Zachar Arkus was born in Brussels, Belgium, on Christmas Day, nineteen oh nine. He became an engineer and a racing driver. Driven, a New Zealand outlet, notes he also set a record at Pikes Peak, the famous hill climb in Colorado.""",
   "Brussels Belgium 1900s", "BORN IN BRUSSELS, 1909")
sc("""He raced at Le Mans four times, from nineteen fifty-two to nineteen fifty-five, according to Wikipedia. And in nineteen fifty-four and nineteen fifty-five, he won his class driving Porsche five fifty R S Spyders, small mid-engined race cars. So he knew first-hand how a car with its engine behind the driver behaves on a track.""",
   "Porsche 550 RS Spyder", "CLASS WINS: 1954 AND 1955")
sc("""Wikipedia says he joined Chevrolet on the first of May nineteen fifty-three, after seeing the Corvette concept at a show in New York. He was not the Corvette's creator. That credit goes to Harley Earl, GM's design chief. But Duntov became the engineer who turned it into a real sports car.""",
   "1953 Chevrolet Corvette", "JOINED CHEVROLET IN 1953")
sc("""And he did not wait long to make his views known. Wikipedia says that in December nineteen fifty-three, just months after joining, he wrote a memo called Thoughts Pertaining to Youth, Hot Rodders and Chevrolet. In it, he laid out his plans to use Chevrolet's V8 to win over performance fans. It was the start of the Corvette as a performance car.""",
   "1950s hot rod", "THE 1953 MEMO")
sc("""Remember, the first Corvette of nineteen fifty-three used a six-cylinder engine, not a V8. It looked like a sports car, but it was not very fast. Duntov's job was to give it the performance to match its looks. And from the start, he believed the engine should eventually move behind the driver.""",
   "1953 Corvette Blue Flame six", "THE FIRST CORVETTE HAD A SIX")
sc("""Driven reported that he became director of high-performance vehicles in nineteen fifty-four, introduced V8 power to the Corvette in nineteen fifty-five, and fuel injection in nineteen fifty-seven. And from the late nineteen fifties, he watched top-level racing move toward mid-engined cars. He wanted the Corvette to follow.""",
   "1957 Corvette fuel injection", "V8 IN 1955, FUEL INJECTION IN 1957")

# ---------- 2. THE BAN ----------
ch("The racing ban")
sc("""But there was a problem. Hagerty explained that in early nineteen fifty-seven, American carmakers agreed to stop direct racing involvement, after the nineteen fifty-five Le Mans disaster, which killed more than eighty spectators. GM's top executives kept a ban on hotter track models.""",
   "1955 Le Mans", "1957: THE RACING BAN")
sc("""Duntov did not give up. Motor Authority reported that he worked around the ban with experimental cars, and by quietly giving performance parts to race teams. In nineteen sixty-three, he created the Z06 option package, which Hagerty said was code-named Zora's Option six and listed as a normal production option to avoid alarming management.""",
   "1963 Corvette Z06", "ZORA'S OPTION 6")
sc("""Only one hundred ninety-nine Z06s were built that first year, Motor Authority said, and the first ones went straight to race teams. Duntov was clearly willing to bend the rules to make the Corvette faster. And his biggest idea was still waiting, moving the engine.""",
   "1963 Corvette Sting Ray racing", "199 BUILT")
sc("""Why did he care so much about the engine's position? It comes down to physics. With the engine in the front, most of the weight sits over the front wheels, away from the rear wheels that drive the car. With the engine in the middle, the weight sits closer to the center, and more of it presses on the driven rear wheels. That helps traction, braking balance, and how quickly the car can change direction.""",
   "mid engine layout diagram", "WHY MID-ENGINE?")

# ---------- 3. CERV I AND II ----------
ch("The research cars")
sc("""In nineteen sixty, Duntov built the C E R V one, the Chevrolet Engineering Research Vehicle. Driven described it as a single-seat, Indy-style open-wheeler with the engine behind the driver. It was not a road car. It was a rolling laboratory.""",
   "Chevrolet CERV I", "1960: CERV I")
sc("""And it had a real impact. CorvSport reported that the C E R V one tested the independent rear suspension that later appeared on the famous nineteen sixty-three Split-Window Corvette. So even a mid-engined research car made the front-engined Corvette better.""",
   "1963 Corvette split window", "IT IMPROVED THE 1963 CORVETTE")
sc("""Then came the C E R V two, in nineteen sixty-four. Driven said it was a mid-engined, all-wheel-drive sports car that would have worn a Corvette badge, built to compete with the Ford G T forty in endurance racing. Duntov hoped private teams could race it, since factory racing was banned.""",
   "Chevrolet CERV II", "1964: CERV II vs FORD GT40")
sc("""Here is the twist. Ford went to Le Mans with the G T forty and beat Ferrari. Chevrolet's mid-engined answer, the C E R V two, never raced as planned. Driven put it simply. It didn't happen. While Ford made history with a mid-engined car, Chevrolet's stayed in the workshop.""",
   "Ford GT40 Le Mans", "IT DIDN'T HAPPEN")
sc("""And Ford's success made the point painfully clear. In nineteen sixty-six, Ford's mid-engined G T forty finished first, second, and third at Le Mans, ending Ferrari's run of victories there. The car that Chevrolet's C E R V two was meant to fight became one of the most famous race cars in history. The mid-engine layout was now the proven formula.""",
   "Ford GT40 1966 Le Mans finish", "1966: FORD 1-2-3 AT LE MANS")

# ---------- 4. THE PROTOTYPES ----------
ch("The prototypes")
sc("""The prototypes kept coming. CorvSport described the X P eight nineteen, a rear-engined prototype inspired by the Chevrolet Corvair, with a body designed by Larry Shinoda. It had too much weight at the back, and CorvSport called it a failure.""",
   "Chevrolet XP-819", "XP-819: TOO MUCH WEIGHT AT THE BACK")
sc("""Then came the Astro two, a race-inspired mid-engine prototype with a big V8 mounted across the car. And in nineteen sixty-nine, CorvSport said, engineers built two X P eight eighty-two prototypes, with a three hundred fifty cubic inch small-block V8 mounted transversely behind the seats.""",
   "Chevrolet Astro II", "1969: XP-882")
sc("""And then the story turned strange. John DeLorean, Chevrolet's general manager at the time, cancelled the X P eight eighty-two, calling it too impractical and costly, CorvSport reported. Then he learned that Ford planned to sell the De Tomaso Pantera, an Italian mid-engined sports car, through its Lincoln-Mercury dealers.""",
   "De Tomaso Pantera", "FORD'S PANTERA")
sc("""Suddenly, DeLorean changed his mind. CorvSport said he reversed the cancellation and ordered the X P eight eighty-two prepared for the nineteen seventy New York Auto Show. A rival's announcement had brought the mid-engine Corvette back from the dead.""",
   "Chevrolet XP-882 auto show", "BACK FROM THE DEAD")
sc("""CorvSport said Ford planned to offer the Pantera in America from late nineteen seventy-one. The idea of an Italian mid-engined car in Ford showrooms, while Chevrolet had nothing like it, was apparently too much for GM. Competition, not engineering, decided the fate of the prototype.""",
   "De Tomaso Pantera 1971", "COMPETITION DECIDED IT")

# ---------- 5. THE ROTARY ----------
ch("The rotary Corvette")
sc("""Then came one of the wildest ideas in Corvette history. In nineteen seventy-two, the X P eight ninety-five was built on the X P eight eighty-two chassis with an aluminum alloy body. CorvSport said it was nicknamed the Reynolds Aluminum Car, and Driven said it was authorized by John DeLorean.""",
   "Chevrolet XP-895", "1972: THE ALUMINUM CAR")
sc("""And GM considered rotary power. CorvSport reported that early plans included a four hundred twenty horsepower four-rotor engine, made by joining two Vega two-rotor engines together. A Wankel rotary engine has no pistons in the usual sense. It uses spinning triangular rotors, and it is very compact, which made it attractive for a mid-engined car.""",
   "four rotor Wankel engine", "A 420 HP FOUR-ROTOR ENGINE")
sc("""Here is the twist. The rotary program was scrapped during the energy crisis of the early nineteen seventies, CorvSport said. Rotary engines were known for poor fuel economy. In a world of fuel shortages, a thirsty four-rotor engine was the wrong idea at the wrong time.""",
   "1973 oil crisis gas line", "KILLED BY THE OIL CRISIS")
sc("""And DeLorean himself left Chevrolet in nineteen seventy-three, CorvSport said, to start his own company. His own car, the DMC twelve, would later become famous with its stainless steel body and gullwing doors. One of the mid-engine Corvette's biggest supporters was gone.""",
   "DeLorean DMC-12", "DELOREAN LEAVES")

# ---------- 6. THE AEROVETTE ----------
ch("So close: the Aerovette")
sc("""The car did not die. CorvSport said that by nineteen seventy-six it had a four hundred cubic inch Chevrolet V8 and double-folding gullwing doors, and the name Aerovette was later applied to all its versions. And this time, it came very close to production.""",
   "Chevrolet Aerovette", "THE AEROVETTE")
sc("""CorvSport reported that the Aerovette was approved for production starting in nineteen eighty, with a three hundred fifty V8 and an expected price of fifteen thousand to eighteen thousand dollars. A mid-engine Corvette was finally on the plan.""",
   "Chevrolet Aerovette gullwing", "APPROVED FOR 1980")
sc("""Imagine what that would have meant. A mid-engined American sports car with gullwing doors, in showrooms at the start of the nineteen eighties, at a price many middle-class buyers could stretch to. It would have arrived years before most people had ever seen a mid-engined car on an American street.""",
   "Chevrolet Aerovette rear", "WHAT MIGHT HAVE BEEN")
sc("""Then the twist. By then, its supporters had left. CorvSport said Duntov, design chief Bill Mitchell, and GM president Ed Cole had all retired. Wikipedia says Duntov retired in nineteen seventy-five, and Dave McLellan became the Corvette's chief engineer.""",
   "Bill Mitchell GM design", "THE SUPPORTERS RETIRE")
sc("""McLellan cancelled it. CorvSport said he argued that a front-engined car would be cheaper to build and more powerful, and he pointed to weak American sales of imported mid- and rear-engined cars, compared with front-engined cars like the Datsun two forty Z. The Aerovette was dead, and the Corvette stayed front-engined for four more generations.""",
   "Datsun 240Z", "CANCELLED")
sc("""Here is how close it came, and how cheap it would have been. Fifteen to eighteen thousand dollars in nineteen eighty money. Today, a Corvette Z R one costs about one hundred eighty-two thousand dollars, GM Authority reported. The mid-engine Corvette eventually arrived, but in a very different price world.""",
   "Chevrolet Aerovette show", "$15,000-$18,000 IN 1980")

# ---------- 7. THE LONG WAIT ----------
ch("The long wait")
sc("""The dream returned once more in nineteen ninety. The C E R V three, Driven said, paid homage to Duntov's earlier concepts. It looked production-ready, with all-wheel drive, four-wheel steering, and active suspension. But, as Driven put it, it still wasn't the right time.""",
   "Chevrolet CERV III", "1990: CERV III")
sc("""Why did it fail again? The reasons were never simple. A mid-engine car is more expensive to engineer and build. It needs a new chassis, new cooling, and a new gearbox. And for decades, the front-engined Corvette was selling well and making money. There was always a reason to wait one more generation.""",
   "Corvette C4 1990", "ALWAYS ONE MORE GENERATION")
sc("""Meanwhile, front-engined Corvettes kept getting better. The C four, the C five, the C six, and the C seven. Some had enormous power. Hagerty reported that the C seven Z06 of twenty fifteen had a supercharged six hundred fifty horsepower V8. But the engine was still in the front.""",
   "Corvette C7 Z06", "650 HP, ENGINE IN THE FRONT")
sc("""Duntov never saw his dream come true. Wikipedia says that during a review of the C five Corvette in the mid nineteen nineties, he reportedly said, the engine is still in the front. He died on the twenty-first of April nineteen ninety-six, at the age of eighty-six. His ashes are entombed at the National Corvette Museum in Bowling Green, Kentucky.""",
   "National Corvette Museum", "DUNTOV DIES, 1996")
sc("""Here is the twist. Bowling Green is also where every Corvette is built. So the man who fought for a mid-engine Corvette rests in the same city where, more than twenty years after his death, the first mid-engine Corvettes would roll off the line.""",
   "Bowling Green Corvette plant", "HE RESTS WHERE THEY ARE BUILT")

# ---------- 8. THE C8 ----------
ch("Finally: the C8")
sc("""On the eighteenth of July twenty nineteen, Chevrolet finally revealed the mid-engine Corvette, the C eight. The Associated Press reported that the reveal took place in a World War Two dirigible hangar in Orange County, California, and that Corvettes had used front-mounted engines for sixty-six years.""",
   "Corvette C8 reveal 2019", "JULY 18, 2019: THE C8")
sc("""Chief engineer Tadge Juechter told the Associated Press why. We were reaching the performance limitations of a front-engine car, he said. And people spending a lot of money want it to be the best performer all around. The same argument Duntov had made sixty years earlier.""",
   "Corvette C8 Stingray side", "THE PERFORMANCE LIMIT")
sc("""The numbers were remarkable. The AP reported a new six point two liter V8 with four hundred ninety-five horsepower, zero to sixty in under three seconds with the performance package, and a starting price under sixty thousand dollars. A mid-engined car with supercar acceleration, for the price of a well-equipped pickup truck.""",
   "Corvette C8 Stingray", "UNDER $60,000")
sc("""The AP also listed some surprises. The C eight can run on four cylinders to save fuel, it has a front trunk big enough for an airline-size carry-on, and the rear storage can hold two sets of golf clubs. It was also built in right-hand drive for international markets for the first time. A mid-engine car that was still practical, exactly the kind of compromise Duntov's critics said was impossible.""",
   "Corvette C8 frunk", "PRACTICAL AND MID-ENGINED")
sc("""Business was part of the reason too. The AP reported that Corvette sales through June twenty nineteen were just under ten thousand cars, not huge numbers, and that GM hoped the new design would attract younger buyers who had never considered a Corvette. The mid-engine layout was a bet on the car's future, not just its performance.""",
   "Corvette C8 young buyers", "A BET ON THE FUTURE")
sc("""It was not perfect. The AP noted that the new car was slightly heavier and slightly less aerodynamic than the front-engined model it replaced, partly because of the large air intakes on its sides. A mid-engined car needs to feed air to an engine behind the driver, and those intakes became the C eight's signature look.""",
   "Corvette C8 side air intake", "HEAVIER, BUT FASTER")
sc("""And Duntov was not forgotten. Wikipedia says there were rumors that a high-performance C eight might be called Zora, and that a camouflaged prototype was spotted with stickers resembling his profile. Engineers seemed to know exactly whose dream they were finishing.""",
   "Corvette C8 prototype camouflage", "THE ZORA RUMORS")

# ---------- 9. THE BUMPY START ----------
ch("A bumpy start")
sc("""But even now, the story had one more obstacle. GM Authority reported that C eight production was originally planned to start in December twenty nineteen, but was delayed by the United Auto Workers strike against General Motors, which included a walkout at the Bowling Green plant. Wikipedia says production officially began on the third of February twenty twenty.""",
   "Bowling Green Assembly", "DELAYED BY A STRIKE")
sc("""And the very first production C eight was special. The Peak reported that Rick Hendrick, the NASCAR team owner and Corvette enthusiast, bought it at the Barrett-Jackson auction in Scottsdale, Arizona, for about three million dollars. The money above the car's normal price went to the Detroit Children's Fund.""",
   "Barrett-Jackson auction", "FIRST C8: $3 MILLION")
sc("""The car was a hit. Wikipedia says the C eight was named twenty twenty MotorTrend Car of the Year, and lists about twenty thousand three hundred C eights built for twenty twenty, despite the strike and the pandemic. For the twenty twenty-three model year, production rose to about fifty-three thousand eight hundred.""",
   "Corvette C8 MotorTrend", "2020 CAR OF THE YEAR")
sc("""Production stayed strong. Wikipedia lists about twenty-six thousand two hundred C eights for twenty twenty-one, about twenty-five thousand eight hundred for twenty twenty-two, the peak of about fifty-three thousand eight hundred for twenty twenty-three, and about forty-two thousand nine hundred for twenty twenty-four. With about twenty-five thousand eight hundred more for twenty twenty-five, that adds up to almost one hundred ninety-five thousand mid-engine Corvettes in six model years, by our own arithmetic. Duntov's impossible car had become a mass-production reality.""",
   "Corvette C8 assembly line", "~195,000 MID-ENGINE CORVETTES")

# ---------- 10. THE FAMILY ----------
ch("The family Duntov never saw")
sc("""Then the mid-engine layout made new Corvettes possible. The Z06, unveiled on the twenty-sixth of October twenty twenty-one, with its five point five liter flat-plane crank V8 making six hundred seventy horsepower. The E Ray, unveiled in January twenty twenty-three, the first hybrid, all-wheel-drive Corvette, with six hundred fifty-five horsepower, according to Wikipedia.""",
   "Corvette E-Ray", "Z06 AND E-RAY")
sc("""Then the Z R one, revealed in July twenty twenty-four with a twin-turbo V8 making one thousand sixty-four horsepower, and the hybrid Z R one X with one thousand two hundred fifty, Wikipedia said. Top Gear reported that the Z R one X lapped the Nürburgring in six minutes forty-nine point two seven five seconds in twenty twenty-five, at the time the fastest lap ever by an American car.""",
   "Corvette ZR1X", "1,250 HP ZR1X")
sc("""Think about that. The C E R V two of nineteen sixty-four was a mid-engined, all-wheel-drive Corvette concept built to fight the best in the world. Sixty years later, the Z R one X is a mid-engined, all-wheel-drive Corvette that set an American record at the Nürburgring. Duntov's idea was right. It just needed half a century.""",
   "Chevrolet CERV II and ZR1X", "DUNTOV WAS RIGHT")
sc("""And the competition did not stop. In April twenty twenty-six, Corvette Blogger reported that Ford answered with the G T Mark four, a track-only, non-street-legal car, which lapped the Nordschleife in about six minutes sixteen seconds, while the Corvette Z R one X still held the American production car record. Ford and Chevrolet, rivals since the days of the G T forty and the C E R V two, are still fighting over the same German racetrack.""",
   "Ford GT Mk IV", "FORD STRIKES BACK")
sc("""And the race car came full circle too. In June twenty twenty-three, Racer reported, the mid-engined Corvette C eight dot R won its class at Le Mans, Corvette's ninth class win there, in the final race of the G T E category. Duntov won his class at Le Mans in a mid-engined Porsche. Almost seventy years later, a mid-engined Corvette did the same.""",
   "Corvette C8.R Le Mans 2023", "LE MANS, FULL CIRCLE")
sc("""So here is the insane story behind the mid-engine Corvette. A Belgian-born engineer who won Le Mans in a Porsche. A racing ban. Research cars and rotary engines. A rival's Italian sports car that saved a prototype. An oil crisis, a cancelled production plan, and one short, famous complaint. And finally, sixty-six years after the first Corvette, the engine moved behind the seats.""",
   "Corvette C8 and Aerovette", "THE STORY IN ONE MINUTE")
sc("""Do you think Chevrolet waited too long, or was the timing finally right? Tell us in the comments. In the other videos of this series, we reveal two things you didn't know about the Corvette Z06, compare it with the Porsche nine eleven G T three R S, and work out what it really costs to own one.""",
   "Corvette Z06", "DID CHEVY WAIT TOO LONG?")
sc("""And if your next vehicle is a pickup instead of a Corvette, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Corvette C8 sunset", "SUBSCRIBE: PICKUP REALITY")

save("video76", "The Insane Story Behind the Mid-Engine Corvette", [
    "Wikipedia, Zora Arkus-Duntov: https://en.wikipedia.org/wiki/Zora_Arkus-Duntov",
    "Driven (NZ), The 'Father of the Corvette' always wanted a middle child (June 2022): https://www.drivencarguide.co.nz/news/the-good-oil-father-of-the-corvette-always-wanted-a-middle-child",
    "CorvSport, Mid-engine Corvette prototypes: XP-882: https://www.corvsport.com/mid-engine-corvette-prototypes-xp-882/",
    "Hagerty, How the Corvette Z06 went from '60s racing package to modern monster: https://hagerty.com/media/?p=257365",
    "Motor Authority, The 2023 Corvette Z06 exists because of Zora Arkus-Duntov: https://www.motorauthority.com/news/1136291_the-2023-chevrolet-corvette-z06-exists-because-of-zora-arkus-duntov",
    "AP via WFYI, Corvette goes mid-engine for first time to raise performance (July 2019): https://www.wfyi.org/news/articles/corvette-goes-mid-engine-for-first-time-to-raise-performance",
    "Wikipedia, Chevrolet Corvette (C8): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C8)",
    "GM Authority, C8 Corvette production now officially underway (Feb 2020): https://gmauthority.com/blog/2020/02/c8-corvette-production-now-officially-underway/",
    "The Peak, First production C8 Corvette auctioned for $3 million (Jan 2020): https://www.thepeakmagazine.com.sg/lifestyle/chevy-c8-corvette",
    "GM Authority, 2026 Corvette pricing uncovered: https://gmauthority.com/blog/2025/06/2026-corvette-pricing-uncovered/",
    "Racer, Corvette Racing takes final GTE victory at Le Mans (June 2023): https://racer.com/2023/06/11/corvette-racing-fights-through-to-take-final-gte-victory-at-le-mans/",
    "Wikipedia, Ford GT40: https://en.wikipedia.org/wiki/Ford_GT40",
    "Corvette Blogger, Ford needed a non-production race car to beat the ZR1X Nürburgring record (Apr 2026): https://www.corvetteblogger.com/2026/04/04/video-ford-needed-a-non-production-race-car-to-beat-the-corvette-zr1xs-record-at-the-nurburgring/",
    "Top Gear, Corvette ZR1X fastest American car around the Nürburgring (Aug 2025): https://www.topgear.com/car-news/usa/chevrolet-corvette-zr1x-fastest-american-car-ever-around-nurburgring",
], "D")
