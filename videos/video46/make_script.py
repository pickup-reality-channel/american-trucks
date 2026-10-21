import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""For more than twenty years, Americans could walk into almost any dealer and buy a small, simple, cheap pickup truck. Then, almost overnight, they vanished. Not because people stopped wanting them, but because of a rule most buyers have never heard of. And in twenty twenty-six, more than one hundred eighty thousand people put down deposits on a small pickup that costs under twenty-five thousand dollars. The compact truck is trying to come back.""",
   "Ford Ranger 1990s compact pickup", "THE SMALL TRUCK VANISHED. WHY?")
sc("""This is the rise and fall of the compact truck in America. How Japanese companies started it, how Detroit took it over, how rules in Washington quietly killed it, and how a few new trucks are bringing it back. There are twists in this story that explain why the truck you buy in twenty twenty-seven costs what it costs.""",
   "Chevrolet S-10 pickup", "RISE, FALL, AND COMEBACK")
sc("""Every number in this video comes from a published source, listed in the description. If we could not confirm a figure, we left it out. Let's go back to the nineteen seventies, when small trucks arrived from the other side of the Pacific.""",
   "Datsun pickup", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE RISE ----------
sc("""In the nineteen sixties and seventies, the American pickup was big. Ford, Chevy and Dodge built full-size trucks with big engines, and that was the market. Then Japanese companies arrived with something different. Small, light, fuel-efficient pickups from Datsun, which later became Nissan, and from Toyota. According to Hagerty, Toyota and Nissan practically invented the compact pickup in the nineteen seventies.""",
   "Datsun 620 pickup", "1. THE RISE: JAPAN ARRIVES")
sc("""The timing was perfect. In the nineteen seventies, oil crises sent fuel prices soaring, and Americans suddenly cared about miles per gallon. A small Japanese pickup was cheap to buy, cheap to run, and almost impossible to kill. Young buyers, farmers, surfers and small business owners bought them in huge numbers.""",
   "Toyota pickup 1970s", "THE OIL CRISIS OPENED THE DOOR")
sc("""These trucks also built a reputation that still matters today. Owners found that the little Japanese pickups kept running long after the odometer rolled past numbers that would kill other vehicles. That reputation for durability became the foundation of Toyota's truck business in America, and it is part of the reason the Tacoma is still so popular decades later.""",
   "Toyota pickup 1980s", "A REPUTATION THAT STILL SELLS")
sc("""But there was a problem for the Japanese brands: a twenty-five percent tariff on imported light trucks. It came from the chicken war of nineteen sixty-four, when President Lyndon Johnson retaliated against European tariffs on American chicken. According to The Daily Vroom, three of the four retaliatory tariffs were dropped within a few years. The truck tariff never was.""",
   "Toyota Hilux pickup", "THE 25% CHICKEN TAX")
sc("""Here is the twist. Detroit did not fight the small trucks at first. It joined them. Chevrolet sold a small pickup called the LUV, built by Isuzu. Ford sold the Courier, built by Mazda. To soften the tariff, some of these trucks were shipped as a cab and chassis, and the bed was added after they arrived. The first small trucks with American badges were actually Japanese.""",
   "Chevrolet LUV", "TWIST: DETROIT'S SMALL TRUCKS WERE JAPANESE")
sc("""And Subaru found the strangest loophole of all. Its small BRAT pickup came with two plastic seats bolted into the open bed. With seats, it could count as a passenger vehicle instead of a light truck. It sounds like a joke, but it is a real part of American truck history, and it shows how much a tax rule can shape the vehicles people drive.""",
   "Subaru BRAT", "SEATS IN THE BED")

# ---------- 2. DETROIT TAKES OVER ----------
sc("""Then Detroit built its own. In the early nineteen eighties, Chevrolet launched the S-ten, and Ford launched the Ranger. These were American-designed compact pickups, built in American plants. Dodge followed with the Dakota, a slightly larger truck that sat between compact and full-size. Suddenly, the small truck was not a foreign idea anymore. It was an American one.""",
   "Ford Ranger 1983", "2. DETROIT BUILDS ITS OWN")
sc("""Why did Detroit finally build its own? Because the small truck market had become too big to ignore, and selling another company's truck meant sharing the profit. Building in America also avoided the import tariff completely. For Ford and GM, it was a chance to win back young buyers who had grown up driving Japanese pickups, and keep them for life.""",
   "Chevrolet S-10 1980s", "WHY DETROIT BUILT ITS OWN")
sc("""The Ranger became a legend. For many Americans, it was the first truck they ever owned. Simple, tough, affordable, and small enough to park anywhere. Parents bought them for teenagers. Companies bought them by the thousands for fleets. Mail carriers, utility workers and delivery drivers used them every day.""",
   "Ford Ranger pickup 1990s", "THE RANGER: AMERICA'S FIRST TRUCK")
sc("""The Chevy S-ten was just as popular, and it had a sporty side. In nineteen ninety-one, G M C built a high-performance version of its sister truck, the Syclone, with a turbocharged V six and all-wheel drive. According to V E H Q, fewer than three thousand were built, and it could reach sixty miles per hour in about four point three seconds. A small truck that could embarrass sports cars.""",
   "GMC Syclone", "GMC SYCLONE: 0-60 IN ~4.3 SEC")
sc("""The Dodge Dakota deserves a mention too. It was bigger than the Ranger and S-ten, and in some versions it offered a V eight, which none of the true compacts had. In a way, the Dakota predicted the future. It showed that buyers wanted something between a compact and a full-size truck. That middle ground is exactly where today's midsize trucks live.""",
   "Dodge Dakota", "THE DAKOTA PREDICTED THE FUTURE")
sc("""For a while, this was the golden age of small trucks. Ford, Chevy, GMC, Dodge, Toyota, Nissan, Mazda and Isuzu all sold compact pickups in America. A buyer could choose a basic work truck for very little money, or a sporty version with a V six. Competition kept prices low and quality improving.""",
   "Chevrolet S-10 Ford Ranger Toyota pickup", "THE GOLDEN AGE")
sc("""And here is a twist from that era. Some of the small trucks were secretly the same truck. Mazda's B-Series pickups sold in the United States were, in later years, based on the Ford Ranger. Isuzu's later small trucks were based on GM's. The companies that once built trucks for Detroit ended up selling Detroit trucks with their own badges. The relationship had flipped.""",
   "Mazda B-Series pickup", "TWIST: THE ROLES FLIPPED")

# ---------- 3. THE FALL ----------
sc("""Then came the fall. And it did not happen because of one bad truck. It happened slowly. First, small trucks started growing. Each new generation got a little bigger, a little heavier, and a little more expensive. Extended cabs became crew cabs. Four-cylinder engines gave way to V sixes. The compact truck was turning into a midsize truck.""",
   "Chevrolet Colorado 2004", "3. THE FALL BEGINS")
sc("""Why did they grow? Buyers asked for it, at least in part. They wanted more room for passengers, more power for towing, and more comfort for long drives. Each generation gave them a little more. But every step up in size also meant a step up in price, and the cheap, simple truck that started the segment slowly disappeared from the lineup.""",
   "Ford Ranger crew cab", "BUYERS ASKED FOR MORE")
sc("""Chevrolet replaced the S-ten with the larger Colorado in the mid two thousands. Dodge ended the Dakota after twenty eleven. And then came the biggest blow. According to Hagerty, after Ford killed off the Ranger in twenty twelve, the segment went into hibernation. America's most famous small truck was gone.""",
   "Ford Ranger 2011", "RANGER KILLED: 'HIBERNATION'")
sc("""Why did Ford kill a popular truck? Part of the answer is profit. A small truck sold for much less than a full-size F-one-fifty, but it did not cost that much less to build. Every buyer who chose a Ranger instead of an F-one-fifty was money left on the table. And with fuel economy improving in full-size trucks, the argument for a small truck got weaker.""",
   "Ford F-150 Ford Ranger", "WHY KILL A POPULAR TRUCK?")
sc("""But here is the bigger twist, the rule almost nobody knows. According to Hagerty, the federal fuel economy standards were revised in two thousand eight, with a formula based on a vehicle's footprint, the area between its four wheels. Bigger vehicles get easier targets. Hagerty says the footprint rule effectively discourages carmakers from building body-on-frame trucks in smaller sizes.""",
   "pickup trucks highway", "TWIST: THE FOOTPRINT RULE")
sc("""Here is how it worked in simple terms. Under the footprint formula, each vehicle gets a fuel economy target based on its size. A small truck is expected to get much better mileage than a big truck. If a carmaker builds a small truck that is only slightly more efficient than its big truck, the small truck can actually make its numbers look worse. That is an upside-down incentive.""",
   "pickup truck fuel economy", "AN UPSIDE-DOWN INCENTIVE")
sc("""Think about what that means. A rule designed to improve fuel economy made it harder to build the most fuel-efficient kind of truck. A small truck had to meet a tougher target than a big one. For carmakers, the easy answer was to make trucks bigger, or to stop making small ones. Many did both.""",
   "full size pickup trucks parking lot", "A RULE THAT KILLED SMALL TRUCKS")
sc("""And light trucks took over America. According to Hagerty, sales of light trucks, which include pickups and S U Vs, swelled to three-quarters of the U S light vehicle market. The small, simple pickup that once filled driveways across the country was replaced by bigger trucks and crossovers. Meanwhile, the twenty-five percent tariff kept small pickups built in places like Thailand out of America.""",
   "pickup trucks SUVs traffic", "LIGHT TRUCKS: 3/4 OF THE MARKET")

# ---------- 4. BIGGER 'SMALL' TRUCKS ----------
sc("""Here is how big today's small trucks really are. Ford brought the Ranger back to America in twenty nineteen, but as a midsize truck. According to Hagerty, old compact trucks were nearly a foot shorter, about eight inches narrower, and roughly a thousand pounds lighter than today's so-called small pickups. The trucks we call midsize today are close to the size of full-size trucks from decades ago.""",
   "Ford Ranger 2019", "4. TODAY'S 'SMALL' TRUCKS AREN'T SMALL")
sc("""This size creep happened to almost every vehicle. Cars got bigger, S U Vs got bigger, and trucks got bigger. Safety rules added weight, buyers wanted more space, and the footprint rule rewarded larger vehicles. The result is that a buyer today who wants the size of a nineteen eighty-five Ranger has very few options. Almost nothing new is built in that size anymore.""",
   "Ford Ranger 1985 Ford Ranger 2023", "SIZE CREEP")
sc("""And the midsize market is booming. According to Ford, the Ranger sold seventy thousand, nine hundred sixty units in twenty twenty-five, up fifty-three point six percent. According to Pedal Commander, the Toyota Tacoma sold two hundred seventy-four thousand, six hundred thirty-eight in twenty twenty-five, up more than forty-two percent. The demand for smaller trucks never disappeared. It just had nothing to buy.""",
   "Toyota Tacoma", "TACOMA +42%, RANGER +53.6%")
sc("""But midsize trucks are not cheap anymore. Many well-equipped versions cost as much as a full-size truck did a few years ago. The original promise of the compact pickup, a simple truck for little money, was still missing from the market. Until one company decided to try something nobody else would.""",
   "Chevrolet Colorado 2023", "MIDSIZE, BUT NOT CHEAP")

# ---------- 5. THE COMEBACK ----------
sc("""The comeback started in twenty twenty-one. Ford launched the Maverick, a small pickup built on a car-like platform, with a standard hybrid engine. Hyundai launched the Santa Cruz. According to Hagerty, the two together sold over fifty thousand units in the first six months of twenty twenty-two. A once-sleepy corner of the market had woken up.""",
   "Ford Maverick", "5. THE COMEBACK BEGINS")
sc("""Why did Ford take the risk? Because the company saw buyers leaving trucks for crossovers, and buyers holding on to old Rangers because nothing new fit their needs. The Maverick was built to catch both groups. And it launched with a starting price under twenty thousand dollars before destination, which made it one of the cheapest new vehicles of any kind in America.""",
   "Ford Maverick XL", "WHY FORD TOOK THE RISK")
sc("""The Maverick became a phenomenon. According to Ford, it sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, up eighteen point two percent. And here is the twist: the Maverick is not a traditional truck at all. It is built like a crossover, not on a separate frame. That may be exactly why it can be small and still pass the rules that killed the old compacts.""",
   "Ford Maverick hybrid", "2025: 155,051 MAVERICKS")
sc("""There is a detail that matters for the future. For the twenty twenty-seven model year, according to Ford Authority, the base Maverick X L becomes hybrid only. The small truck that brought back the segment is now leaning fully into efficiency. That is a big contrast with the nineteen eighties, when small trucks were cheap because they were simple, not because they were high-tech.""",
   "Ford Maverick hybrid", "2027 MAVERICK XL: HYBRID ONLY")
sc("""Not every comeback truck survived. According to The Autopian in January twenty twenty-six, Hyundai sold twenty-five thousand, four hundred ninety-nine Santa Cruzes in twenty twenty-five, and the Maverick outsold it six to one. Automotive News reported that Hyundai plans to end Santa Cruz production early. The small truck market is back, but it is not forgiving.""",
   "Hyundai Santa Cruz", "SANTA CRUZ: OUTSOLD 6 TO 1")
sc("""And the Maverick got more expensive. According to The Truth About Cars in August twenty twenty-six, the current Maverick starts at about thirty thousand dollars. That leaves an opening at the very bottom of the market, for a truly cheap, basic truck. And that is exactly where a startup from Indiana is aiming.""",
   "Ford Maverick Lariat", "MAVERICK NOW ~$30,000")
sc("""The startup is Slate Auto, backed in part by Jeff Bezos's family office. According to The Next Web, in June twenty twenty-six, Slate opened preorders for a small, two-seat electric pickup that will start at twenty-four thousand nine hundred fifty dollars. More than one hundred eighty thousand existing reservations were converted into three hundred dollar nonrefundable deposits.""",
   "electric pickup truck small", "SLATE: $24,950, 180,000+ DEPOSITS")
sc("""And the Slate is built like the old compact trucks: simple. According to The Next Web, it has crank windows, no built-in connectivity, optional speakers, and composite body panels wrapped in vinyl instead of paint. It has one hundred eighty-one horsepower, rear-wheel drive only, a two hundred five mile range, two thousand pounds of towing and one thousand five hundred fifty pounds of payload. It is the Model T idea, rebuilt for twenty twenty-six.""",
   "pickup truck simple interior", "CRANK WINDOWS, VINYL WRAP")
sc("""Here is the twist, and the caution. Slate is building in a former printing plant in Warsaw, Indiana, with a target of one hundred fifty thousand vehicles a year and deliveries expected in the fourth quarter of twenty twenty-six. But according to The Next Web, Slate still needs federal vehicle validation and certification before it can legally deliver trucks, and it had not disclosed its status. A deposit is not a truck in your driveway.""",
   "factory Indiana", "TWIST: STILL NEEDS CERTIFICATION")
sc("""And there is a lesson from the electric truck market. The Tesla Cybertruck had huge interest, and yet, according to Cox Automotive estimates reported by InsideEVs, Americans bought about twenty thousand two hundred in twenty twenty-five, while Tesla says it can build over one hundred twenty-five thousand a year. Reservations are a signal of interest, not a guarantee of sales.""",
   "Tesla Cybertruck", "RESERVATIONS ARE NOT SALES")

# ---------- PATTERN ----------
sc("""And Slate is not the only company watching this space. Hyundai says a new midsize body-on-frame truck is due in the U S market before twenty thirty, according to The Autopian. And other brands have hinted at small or affordable trucks for America. The bottom of the truck market, empty for more than a decade, is suddenly getting crowded with promises.""",
   "Hyundai Santa Cruz", "A CROWDED BOTTOM OF THE MARKET")
sc("""So what is the full story? The compact truck rose because it was cheap and efficient when America needed both. It fell because trucks grew, profits pushed buyers toward bigger models, and rules made small body-on-frame trucks harder to build. And it is coming back because millions of buyers never stopped wanting a simple, affordable pickup.""",
   "Ford Ranger Chevrolet S-10 Ford Maverick", "WHY IT ROSE, FELL, AND RETURNED")
sc("""There is one more piece of the puzzle: price. For many young buyers, a new full-size pickup is out of reach. A small truck is often the only way into truck ownership. That is why the compact truck matters far beyond its sales numbers. It is the entry door. When it disappeared, many people simply stopped buying trucks, or bought used ones instead.""",
   "used pickup trucks for sale", "THE ENTRY DOOR")
sc("""And here is the final twist. The new small trucks do not look like the old ones underneath. The Maverick is built like a crossover. The Slate is electric. The old compact pickup did not come back the way it left. It came back in the only shapes that today's rules and costs allow.""",
   "Ford Maverick pickup", "IT CAME BACK IN A NEW SHAPE")

sc("""There is one more chapter in the small truck story: the used market. Because new small trucks disappeared for years, clean used Rangers, S-tens and old Toyota pickups became valuable. According to Hagerty, the nineteen eighty-four to eighty-eight Toyota Pickup four by four even became a Bull Market pick, with the number of these trucks on Hagerty policies quadrupling since twenty seventeen.""",
   "Toyota pickup 1980s", "OLD SMALL TRUCKS GOT VALUABLE")
sc("""That tells you how strong the demand for small trucks really is. When buyers cannot find a new one, they pay more for an old one. And it explains why the Maverick sold so quickly when it arrived. The demand had been building for a decade, with nowhere to go.""",
   "Ford Ranger 1990s", "DEMAND WITH NOWHERE TO GO")
sc("""There is also a lesson about regulations. Rules written for good reasons, like better fuel economy, can have side effects nobody planned. The footprint rule did not set out to kill small trucks, but it changed the math for every carmaker. Whenever you see a big change in what is for sale, it is worth asking what rule might be behind it.""",
   "pickup trucks traffic", "RULES HAVE SIDE EFFECTS")
sc("""And the future may bring new rules again. Fuel economy and emissions standards change with each administration, and tariffs on imported vehicles and parts shifted in twenty twenty-five and twenty twenty-six. Each change can make small trucks easier or harder to build and sell in America. The next chapter of this story will be written partly in Washington.""",
   "US Capitol building", "THE NEXT CHAPTER: WASHINGTON")
sc("""For buyers, the takeaway is simple. The small truck you can buy today is shaped by decisions made long before you walked into the dealer. Knowing that history helps you understand why prices and choices look the way they do, and helps you spot a real bargain when one appears.""",
   "Ford Maverick dealership", "HISTORY EXPLAINS THE PRICE")

# ---------- CLOSE ----------
sc("""So if you want a smaller truck in twenty twenty-seven, here is what to check. First, measure your real needs. If you rarely tow more than a few thousand pounds, a small or midsize truck may do everything you need for much less money. Second, compare bed size and payload, not just the price. A short bed might not fit your gear.""",
   "Ford Maverick bed", "CHECKS 1 AND 2: NEEDS, BED")
sc("""Third, compare the running costs. A hybrid like the Maverick can save a lot on fuel, especially in town. Fourth, if you are considering a new startup truck, read the fine print on deposits and delivery dates, and wait for real reviews. And fifth, check resale. Small trucks have historically held their value well, but a discontinued model can lose it fast.""",
   "pickup trucks dealership", "CHECKS 3, 4 AND 5")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the numbers to compare, the questions to ask, and the warning signs to watch for. The link is in the description and in the pinned comment. Subscribe for the next video, about six muscle trucks nobody remembers. And tell us in the comments: what was your first small truck? Thanks for watching.""",
   "Ford Ranger pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"For more than twenty years": "Intro", "In the nineteen sixties and seventies": "1. The rise: small trucks from Japan",
      "Then Detroit built its own": "2. Detroit takes over", "Then came the fall": "3. The fall and the footprint rule",
      "Here is how big today": "4. Today's small trucks are not small", "The comeback started": "5. The comeback: Maverick, Santa Cruz, Slate",
      "So if you want a smaller truck": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video46", "length_scale": 1.45,
  "title": "The Rise and Fall of the Small Truck in America (And the Rule That Killed It)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
