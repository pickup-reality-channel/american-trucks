import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Ford says it sells the best-selling truck in America, and it has for forty-nine years. General Motors says it is America's full-size pickup leader, for six years in a row. Both claims are true at the same time. And in the third quarter of twenty twenty-six, the brand that grew fastest was neither of them. It was Ram, up almost thirty-four percent, after admitting it made a huge mistake.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "BOTH CLAIM #1. RAM +33.7%")
sc("""This is the Chevy versus Ford versus Ram rivalry, explained. The oldest fight in the American car business. Who is really winning in twenty twenty-six, how each brand got here, the tricks they use with numbers, and the moments when one of them almost lost everything. By the end, you will know exactly how to use this rivalry to pay less for your next truck.""",
   "pickup trucks dealership lot", "THE TRUCK WAR, EXPLAINED")
sc("""Why should you care who wins? Because the fight between these three companies decides what trucks cost, what engines you can choose, and how big the discounts are at your local dealer. When one brand stumbles, the others pounce, and buyers who understand that can save thousands. The rivalry is not just a story. It is a tool.""",
   "Ram 1500 Chevrolet Silverado dealership", "THE RIVALRY IS A TOOL")
sc("""Every number in this video comes from a published source, and the sources are in the description. If a figure could not be confirmed, we left it out. Let's start with the numbers, because the numbers are where the fight gets interesting.""",
   "Chevrolet Silverado pickup", "EVERY NUMBER IS SOURCED")

# ---------- PART 1: THE NUMBERS ----------
sc("""Here is twenty twenty-five. According to Ford, it sold eight hundred twenty-eight thousand, eight hundred thirty-two F-Series trucks, up eight point three percent. That is the biggest single truck line in the country. On the Chevrolet side, according to sales figures compiled by Pedal Commander, the Silverado sold five hundred sixty-nine thousand and ninety-three. So Ford wins by more than a quarter of a million trucks. Case closed? Not even close.""",
   "Ford F-150 pickup", "2025: F-SERIES 828,832 / SILVERADO 569,093")
sc("""Here is the twist. General Motors also sells the GMC Sierra, which is built on the same platform as the Silverado. The Sierra sold three hundred forty-eight thousand, two hundred twenty-two in twenty twenty-five. Add the two together, and GM sold about nine hundred seventeen thousand full-size pickups. That is more than Ford. That is why GM calls itself the full-size pickup leader.""",
   "GMC Sierra pickup", "SILVERADO + SIERRA: ~917,000")
sc("""So who is right? Both of them. Ford counts one nameplate. GM counts one platform sold under two brands. And there is another detail that makes it even messier. The F-Series number includes heavy-duty Super Duty trucks, all the way up to the F-four-fifty. So every time you see a headline about who sells the most trucks, the real question is what exactly is being counted.""",
   "Ford Super Duty F-450", "WHAT IS BEING COUNTED?")
sc("""And GM's twenty twenty-five was special. According to D Business, GM said the Silverado and Sierra posted their best combined sales in twenty years. GM's head of North America, Duncan Aldred, said demand for its brands was strong at every price point. After years of being overshadowed by Ford's headline, GM had its strongest truck year in two decades.""",
   "Chevrolet Silverado 2025", "GM: BEST COMBINED YEAR IN 20 YEARS")
sc("""Here is how the marketing works in practice. Ford's ads talk about the best-selling truck. GM's ads talk about the full-size pickup leader. Each statement is carefully worded to be accurate. Neither is lying. They are just choosing different scoreboards. Once you know that, you can stop taking either headline as proof of which truck is better for you.""",
   "Ford F-150 Chevrolet Silverado advertising", "TWO SCOREBOARDS")
sc("""Now the third quarter of twenty twenty-six. According to autoevolution, Ford delivered two hundred three thousand, seven hundred seven F-Series trucks, down one point nine percent. The Silverado delivered eighty-six thousand, five hundred ninety, down two point five percent. Silverado and Sierra together reached two hundred thirty-three thousand, two hundred twenty-nine. Again, Ford wins the nameplate fight, and GM wins the platform fight.""",
   "Chevrolet Silverado GMC Sierra", "Q3 2026: GM 233,229 / FORD 203,707")
sc("""But the real story of that quarter was Ram. Its combined light-duty and heavy-duty trucks reached one hundred seventeen thousand, seven hundred fifty-seven. That is up thirty-three point seven percent from a year earlier. While Ford and Chevy were slightly down, Ram was growing by a third. To understand why, we have to go back to a decision Ram now openly calls a mistake.""",
   "Ram 1500 pickup", "RAM Q3 2026: 117,757, +33.7%")

# ---------- PART 2: HISTORY ----------
sc("""First, a quick history, because this rivalry is older than most people realize. After World War Two, both Chevrolet and Ford launched new truck lines. Chevrolet introduced its Advance Design trucks in nineteen forty-seven. Ford followed with the F-Series in nineteen forty-eight. From that moment, the two brands have fought over the same buyers for almost eighty years.""",
   "Chevrolet Advance Design pickup", "1947 VS 1948: THE FIGHT BEGINS")
sc("""For decades, the fight was about small differences. Engines, styling, and loyalty passed down from parents to children. Then, in nineteen seventy-seven, Ford took the title of best-selling truck in America, and it has never given it back. For GM, that headline became a permanent target. Much of the advertising war since then has been about one brand trying to take a crown, and the other refusing to let go.""",
   "Ford F-150 1977 Chevrolet C10", "1977: FORD TAKES THE CROWN")
sc("""There is a twist hidden in that crown. Ford's title has always been about the F-Series as one nameplate. GM spread its trucks across two brands, Chevrolet and GMC, which split its total in half on paper. In other words, part of the reason Ford has been number one for nearly fifty years is the way the trophy is defined. That does not take away from Ford's success. But it explains why GM never stopped fighting.""",
   "GMC pickup classic Chevrolet pickup", "TWIST: HOW THE TROPHY IS DEFINED")
sc("""Dodge, the ancestor of Ram, was a distant third for most of that time. Its trucks were tough, but they lacked the image and the dealer reach of Ford and Chevy. That changed in nineteen ninety-four, when Dodge launched a Ram pickup with a bold, big-rig style grille. It looked like a small semi truck. Some people hated it. Many more loved it. For the first time in years, Dodge had a truck people talked about.""",
   "Dodge Ram 1994 pickup", "1994: THE BIG-RIG RAM")
sc("""Dodge also had a secret weapon in its heavy-duty trucks: the Cummins diesel engine. It gave Dodge a reputation for towing and durability that its light-duty trucks never had. And then came another twist. In twenty ten, Chrysler split Ram off from Dodge as its own brand. A truck name became a company. The third player in the rivalry finally had its own identity.""",
   "Ram 2500 Cummins diesel", "2010: RAM BECOMES ITS OWN BRAND")
sc("""Ram used that identity to do something different. Instead of only competing on toughness, it competed on comfort. Ram pushed coil-spring rear suspension in its half-ton truck and later air suspension, plus large touchscreens and luxury interiors. The idea was simple. Many truck buyers drive their trucks every day with their families, so make the truck ride and feel like a luxury car.""",
   "Ram 1500 Limited interior", "RAM'S BET: COMFORT")
sc("""The bet paid off in a way nobody expected. In twenty nineteen, according to The Drive, Ram sold six hundred thirty-three thousand, six hundred ninety-four pickups, up eighteen percent. The Silverado sold five hundred seventy-five thousand, six hundred. For the first time in history, Ram had pushed Chevy out of second place for a full year. The underdog had bitten back.""",
   "Ram 1500 2019 pickup", "2019: RAM 633,694 BEATS SILVERADO")
sc("""What made the difference? The twenty nineteen Ram fifteen hundred was a new generation, launched with a high-quality interior, a big touchscreen, and a smooth ride. Many reviewers praised it as one of the most comfortable trucks in its class. At the same time, the new Silverado had a mixed reception, especially for its interior. Buyers noticed, and they voted with their wallets.""",
   "Ram 1500 2019 interior", "INTERIOR WON THE ROUND")
sc("""GM's answer, again, was to count both brands. Silverado plus Sierra in twenty nineteen added up to more than Ram. But the message had landed. The truck market was no longer a two-way fight between Ford and Chevy. It was a three-way war, and the smallest of the three had shown it could win a round.""",
   "Chevrolet Silverado GMC Sierra Ram", "A THREE-WAY WAR")

# ---------- PART 3: THE BIG FIGHTS ----------
sc("""Now some of the biggest moments of the fight. In twenty fifteen, Ford built the body of the F-one-fifty out of aluminum, to cut weight. Chevrolet saw an opening. It ran ads comparing its steel truck beds to Ford's aluminum beds, showing heavy loads dropped into both. The message was simple: steel is tougher. Ford pushed back and kept selling. The aluminum F-one-fifty stayed the best-selling truck.""",
   "Ford F-150 aluminum 2015", "2015: STEEL VS ALUMINUM")
sc("""The twist is that both sides were partly right. Aluminum saved weight and did not rust. Steel was cheaper to repair in some cases. Ten years later, the debate had a new chapter. In September twenty twenty-five, a fire at the Novelis aluminum plant in New York disrupted Ford's supply. According to Automotive Logistics, Ford's chief financial officer confirmed a production loss of about one hundred thousand vehicles across twenty twenty-five.""",
   "Novelis aluminum plant", "2025: THE ALUMINUM FIRE")
sc("""What did this teach the industry? That a rival's weakness can become your marketing. It also taught Ford something the hard way. Using one special material makes a truck dependent on a small number of suppliers. Steel trucks have more suppliers to choose from. In a crisis, that difference matters.""",
   "Ford F-150 assembly line", "A WEAKNESS BECOMES AN AD")
sc("""Then came the electric fight. Ford launched the F-one-fifty Lightning. GM launched the Silverado E V and the GMC Sierra E V. Ram promised the Ram fifteen hundred R E V. For a few years, all three brands said the future of the pickup was electric, and each one wanted to win it.""",
   "Chevrolet Silverado EV", "THE ELECTRIC RACE")
sc("""None of them won. In September twenty twenty-five, Ram cancelled its all-electric R E V before a single customer received one. In December twenty twenty-five, according to Fox Business, Ford took a nineteen point five billion dollar charge and ended production of the all-electric Lightning. GM's electric trucks continued, but in small numbers. The electric race ended with all three brands quietly walking back to the starting line.""",
   "Ford F-150 Lightning", "THE RACE NOBODY WON")

# ---------- PART 4: THE HEMI ----------
sc("""Why did all three fail at the same time? Price, towing, and timing. Electric trucks cost more to build. Towing a heavy trailer can cut their range sharply. And when the federal tax credit for electric vehicles ended in twenty twenty-five, the price gap got wider. The rivalry pushed all three companies to rush into a market that their own buyers were not ready for.""",
   "Ford F-150 Lightning towing", "WHY ALL THREE FAILED")
sc("""And that brings us to Ram's big mistake. For the twenty twenty-five model year, Ram dropped its famous five point seven liter Hemi V eight from the Ram fifteen hundred. The plan was to move buyers to a new twin-turbo six-cylinder engine. On paper, the new engine was more powerful and more efficient.""",
   "Ram 1500 Hemi V8", "RAM DROPS THE HEMI")
sc("""Buyers did not care about paper. Many loyal Ram customers wanted a V eight, and they said so. In June twenty twenty-five, Ram reversed course and announced the Hemi was coming back. According to Carscoops, Stellantis said the brand received over ten thousand orders in the first twenty-four hours after the announcement.""",
   "Ram 1500 pickup red", "10,000+ ORDERS IN 24 HOURS")
sc("""And here is the part almost no company ever says out loud. Ram's chief executive, Tim Kuniskis, admitted the company screwed up when it dropped the Hemi. He said some customers felt Ram had abandoned something important, and the company feared losing them to Ford and General Motors. The returning Hemi made three hundred ninety-five horsepower and four hundred ten pound-feet of torque, as a one thousand two hundred dollar option on most versions.""",
   "Ram 1500 Hemi engine", "CEO: WE SCREWED UP")
sc("""A year later, the result showed up in the sales numbers. In the third quarter of twenty twenty-six, Ram's trucks were up thirty-three point seven percent. The Ram fifteen hundred alone reached seventy-six thousand, six hundred fifty. The lesson for all three brands was clear. In this rivalry, the fastest way to lose buyers is to take away something they love. The fastest way to win them back is to admit it.""",
   "Ram 1500 pickup", "THE COMEBACK")

# ---------- PART 5: WHAT EACH BRAND DOES BEST ----------
sc("""Ram's story also shows a deeper truth about this rivalry. The three companies watch each other constantly. When Ram dropped the V eight, Ford and GM kept theirs, and their dealers were happy to welcome Ram's unhappy customers. When Ram brought it back, it was trying to close that door. Every move in this rivalry is made with the other two in mind.""",
   "Chevrolet Silverado Ford F-150", "EVERY MOVE WATCHES THE OTHERS")
sc("""So in twenty twenty-six, what does each brand actually do best? Ford's strength is choice and scale. The F-Series covers everything from the F-one-fifty to the heavy Super Duty, and Ford leads in hybrids. According to Ford, it sold eighty-four thousand, nine hundred thirty-four F-one-fifty hybrids in twenty twenty-five, up fifteen percent. No rival sells a full-size hybrid pickup in those numbers.""",
   "Ford F-150 hybrid", "FORD: CHOICE AND HYBRIDS")
sc("""General Motors' strength is its two-brand strategy. A buyer who wants a working truck can go to Chevrolet. A buyer who wants something more upscale can go to GMC, with Denali trims that compete with luxury cars. Same platform, different image, different prices. That is how GM wins the combined numbers year after year.""",
   "GMC Sierra Denali", "GM: TWO BRANDS, ONE PLATFORM")
sc("""Ram's strength is ride quality and interiors, and now, once again, the Hemi. Ram has built its reputation on making a truck that feels comfortable on long drives. And by listening to buyers about the V eight, it showed it can move faster than its bigger rivals. Ram is still third, but it is the brand with the most momentum in twenty twenty-six.""",
   "Ram 1500 Laramie", "RAM: COMFORT AND MOMENTUM")
sc("""And here is the twist that the three brands rarely mention. The fastest growth in the pickup market is not happening in full-size trucks at all. According to Pedal Commander, the midsize Toyota Tacoma sold two hundred seventy-four thousand, six hundred thirty-eight in twenty twenty-five, up more than forty-two percent. And Ford's small Maverick sold over one hundred fifty-five thousand. Many buyers are leaving the big three-way war for something smaller.""",
   "Toyota Tacoma Ford Maverick", "TACOMA +42%: THE REAL GROWTH")
sc("""Toyota is the outsider in this fight. Its full-size Tundra sold one hundred ten thousand and eighty through September twenty twenty-six, according to autoevolution, down slightly. That is a fraction of what the Detroit three sell. In full-size trucks, the American brands still own the market. In midsize trucks, the story is very different.""",
   "Toyota Tundra", "TUNDRA: 110,080 THROUGH SEPT 2026")

# ---------- PART 6: LOYALTY ----------
sc("""This matters for the three-way war. Every buyer who chooses a midsize Tacoma or a small Maverick is a buyer who did not choose a full-size truck. Ford is in a good position, because it sells both. GM sells the midsize Colorado and Canyon. Ram, for now, has no midsize pickup in America. That gap could matter more in the next few years than any fight over horsepower.""",
   "Chevrolet Colorado GMC Canyon", "RAM HAS NO MIDSIZE TRUCK")
sc("""Why is this rivalry so emotional? Because truck buyers are some of the most loyal customers in the car business. Many buyers stay with one brand for life, often the same brand their parents drove. You see it in bumper stickers, in family arguments, and in parking lots full of one brand at a single job site. For the companies, that loyalty is worth billions.""",
   "pickup trucks parking lot", "LOYALTY IS WORTH BILLIONS")
sc("""And that loyalty is exactly why the Hemi story mattered so much. When Ram took away the V eight, it was not just removing an engine. It was breaking a promise to its most loyal buyers. When it brought it back, it repaired that promise. The same thing happened to Ford in a different way, when electric trucks did not match what its traditional buyers wanted.""",
   "Ram 1500 Ford F-150", "BREAKING A PROMISE")
sc("""But loyalty is changing. Younger buyers compare online before they ever walk into a dealership. They read reviews, watch videos, and look at reliability data. A brand can no longer count on a family tradition. The Hemi comeback and the Ram surge of twenty nineteen both show that buyers will switch when a rival offers something better.""",
   "pickup truck buyers dealership", "LOYALTY IS CHANGING")
sc("""Here is the final twist, and it is the one that helps you. The fiercer the rivalry, the better it is for buyers. When three companies are fighting over the same customer, they compete with incentives, financing deals, and features. In a quarter when Ram is growing by a third and Ford and Chevy are slightly down, someone is under pressure to win buyers back. Pressure means deals.""",
   "truck dealership sale", "RIVALRY = DEALS")

# ---------- CLOSE ----------
sc("""So here is how to use the rivalry when you buy a truck in twenty twenty-seven. First, never shop just one brand. Get a written price on comparable trucks from Ford, Chevy or GMC, and Ram. Dealers know buyers are loyal, and they price for it. Showing that you are willing to switch is one of the strongest moves you have.""",
   "Ford Chevrolet Ram trucks", "CHECK 1: SHOP ALL THREE")
sc("""Second, compare the same thing. Match the cab, the bed length, the engine and the trim. A cheaper truck with a smaller engine or a basic trim is not a better deal. Third, look at which brand is losing ground right now. A brand with falling sales is often the one with the biggest incentives. Fourth, check whether a midsize truck can do everything you need, for less money.""",
   "pickup truck comparison", "CHECKS 2, 3 AND 4")
sc("""And fifth, count the full cost, not just the monthly payment. Fuel, insurance, and what the truck will be worth in five years can change which deal is really the best. Loyalty is fine. But loyalty without a comparison is how buyers leave thousands of dollars on the table.""",
   "pickup truck dealer", "CHECK 5: THE FULL COST")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the numbers to compare and the questions to ask every dealer. The link is in the description and in the pinned comment. Subscribe for the next video, where we look at five pickups that changed America. And tell us in the comments: Ford, Chevy, or Ram? Thanks for watching.""",
   "Ford F-150 Chevrolet Silverado", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Ford says it sells": "Intro", "Here is twenty twenty-five": "1. Who is really number one",
      "First, a quick history": "2. How the rivalry started", "Now some of the biggest moments": "3. Aluminum, fires and the EV race",
      "And that brings us to Ram": "4. Ram's Hemi mistake", "So in twenty twenty-six, what does": "5. What each brand does best",
      "Why is this rivalry": "6. Loyalty and what it costs you", "So here is how to use": "How to use the rivalry when you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video43", "length_scale": 1.45,
  "title": "Chevy vs Ford vs Ram: Who Is Really Winning the Truck War in 2026?", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
