import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One old Ford pickup jumped thirty-two percent in value in just three months this year. A Chevy truck that sold as a used work truck for a few thousand dollars is now worth more than sixty thousand. And a Ford Bronco, the most famous classic four by four in America, just lost twelve percent. The classic truck market is moving fast in twenty twenty-six, and not in the direction most people think.""",
   "Ford F-150 1980s pickup classic", "+32% IN 3 MONTHS")
sc("""So which classic American pickups are actually worth buying right now, before twenty twenty-seven? Not the ones that already peaked. The ones the data says are still climbing. We looked at the numbers from Hagerty, the largest classic vehicle insurer in America, and from the biggest auctions of the year. Five trucks stood out, and one of them is probably sitting in a barn near you.""",
   "Chevrolet C10 pickup classic", "5 CLASSIC TRUCKS STILL CLIMBING")
sc("""Here is the scale of the market. At Barrett-Jackson in Scottsdale, Arizona, in January twenty twenty-six, more than two thousand vehicles crossed the block. The average sale was about one hundred one thousand dollars. The median was sixty thousand five hundred. That is the money now flowing into old metal. But trucks follow their own rules, and the rules changed this year.""",
   "Barrett-Jackson auction Scottsdale", "SCOTTSDALE 2026: AVG $101,298")
sc("""Stay to the end, because the fifth truck is the one most people overlook, and the last section is the checklist we use before buying any old pickup. Every number in this video comes from a published source, listed in the description. If a figure could not be confirmed, we left it out. Let's start with the truck that surprised everyone this summer.""",
   "Ford pickup truck classic restored", "EVERY NUMBER IS SOURCED")

# ---------- 1. BULLNOSE FORD ----------
sc("""Number one is the nineteen eighty to nineteen eighty-six Ford F-Series. Truck people call it the Bullnose, because of the rounded hood and the shape of the grille. For decades it was just an old work truck. You saw them on farms, behind gas stations, and parked in driveways with a for sale sign that nobody called about.""",
   "1985 Ford F-150 pickup", "1. FORD F-SERIES 1980-1986")
sc("""Then came the second quarter of twenty twenty-six. According to Hagerty, as reported by Ford Authority in August, the nineteen eighty to eighty-six F-Series rose thirty-two percent in value in a single quarter. That made it one of the largest gainers among all collectible vehicles in the country. Not among trucks. Among everything.""",
   "Ford F-250 1980s pickup", "Q2 2026: +32% VALUE")
sc("""And here is the twist. The jump was not driven by the trucks you would expect. Hagerty said the increase was largely driven by heavy-duty models catching up to the lighter duty models. In other words, the F-two-fifty and F-three-fifty, the trucks that did real work, are finally being valued like the F-one-fifty. For years, a buyer could get a heavy-duty Bullnose for less. That gap is now closing.""",
   "Ford F-350 classic pickup", "TWIST: HEAVY-DUTY CATCHING UP")
sc("""Hagerty also said there has been a notable uptick in activity being led by the F-Series. That matters, because activity comes before price. More people asking for insurance quotes and valuations usually means more buyers are getting ready to spend. The Bullnose is no longer a secret.""",
   "Ford F-150 pickup 1980s red", "MORE BUYERS ARE LOOKING")
sc("""Now the second twist. At the same time, the first-generation Ford Bronco, the classic sixties and seventies four by four that dominated auctions for years, lost twelve percent of its value in the same quarter. And the earliest F-Series pickups have softened too. Money is not leaving old Fords. It is moving from the famous ones to the overlooked ones.""",
   "Ford Bronco first generation classic", "BRONCO: -12% SAME QUARTER")
sc("""Here is some context. The F-Series has been the best-selling truck line in America for decades, so millions of these trucks were built. That is usually bad news for collector value. Common trucks stay cheap. But common also means survivors are everywhere, and most were used hard and thrown away. Clean, rust-free, unmodified examples are much rarer than the production numbers suggest.""",
   "Ford F-150 1986 pickup blue", "MILLIONS BUILT, FEW SURVIVED CLEAN")
sc("""Why does this matter for a buyer? Because the Bullnose is still mechanically simple. Parts are widely available, the frames are tough, and many came with the straight six or a small block V eight. The lesson is that the best time to buy a rising classic is when it starts moving, not after everyone is already talking about it. And as of this summer, it started moving.""",
   "Ford F-150 1984 pickup", "SIMPLE, TOUGH, STILL AFFORDABLE")

# ---------- 2. CHEVY C/K 1967-1972 ----------
sc("""Number two is the nineteen sixty-seven to nineteen seventy-two Chevrolet C and K pickup. Many people call it the most beautiful pickup General Motors ever built. The long body line, the clean sides, the simple dashboard. It is the truck you see on posters, in movies, and at almost every car show in America.""",
   "Chevrolet C10 1967 pickup", "2. CHEVY C/K 1967-1972")
sc("""It is also proof of how far a truck can climb. At Barrett-Jackson in twenty twenty-five, a custom nineteen sixty-seven C ten sold for two hundred three thousand five hundred dollars. That is not a typical truck, it is a full custom build. But it shows how much money serious buyers are now willing to put into this generation.""",
   "Chevrolet C10 1967 custom", "CUSTOM 1967 C10: $203,500")
sc("""Here is the twist that saves you money. Not all of these trucks are valued the same. In a Hagerty analysis, valuation expert James Hewitt found that two-wheel drive versions were worth about fifteen percent less than the four by four K models, and a Stepside was worth about six percent less than a Fleetside. If you want the look and not the auction headline, a two-wheel drive Stepside is the way in.""",
   "Chevrolet C10 Stepside pickup", "2WD: ~15% LESS THAN 4X4")
sc("""And here is the trap. Because these trucks are so popular, many have been modified, re-engined, or rebuilt from parts. Auction sites label those as custom. A custom truck can be wonderful to drive, but it is valued differently from an original. In January twenty twenty-six at Scottsdale, for example, a custom nineteen fifty-seven Chevy thirty-one hundred sold for forty-four thousand dollars, while restored originals of the same family often bring more.""",
   "Chevrolet 3100 pickup 1957", "ORIGINAL VS CUSTOM: KNOW WHICH")
sc("""There is one more reason this generation keeps its value. Almost every part, from the grille to the full cab, is now reproduced by aftermarket companies. That means a rusty truck can be saved, and a good one is easy to keep on the road. It also means a buyer must be careful, because a truck can look perfect and still be mostly new parts.""",
   "Chevrolet C10 pickup restoration", "EVERY PART IS REPRODUCED")
sc("""So what do you check on a sixty-seven to seventy-two Chevy? First, the cab corners and the floor, where rust hides. Second, the paperwork. A truck sold as original should come with documents. Third, the engine. A modern crate engine is great for daily driving, but it changes what the truck is worth to a collector.""",
   "Chevrolet K10 pickup 1970", "CHECK: RUST, PAPERS, ENGINE")

# ---------- 3. 454 SS ----------
sc("""Number three is a truck that was mocked when it was new. The nineteen ninety to nineteen ninety-three Chevrolet four fifty-four S S. It had a seven point four liter V eight, a regular cab, a short bed, and it was painted almost entirely black. According to The Truth About Cars, it got about eight miles per gallon. Critics called it a muscle car in the wrong body.""",
   "Chevrolet 454 SS pickup", "3. CHEVY 454 SS 1990-1993")
sc("""Production was small. General Motors built about seventeen thousand of them, and most were made in the first model year. After that, sales fell off quickly. For years, a used four fifty-four S S was just a thirsty old truck. People bought them cheap, drove them hard, and many were modified or wrecked.""",
   "Chevrolet C1500 454 SS", "ONLY ~17,000 BUILT")
sc("""Then the market woke up. According to Hagerty's valuation tools, as cited by V E H Q, a nineteen ninety-one four fifty-four S S in excellent condition was worth about twenty-three thousand seven hundred dollars in twenty nineteen. By early twenty twenty-six, the same truck was valued at about sixty thousand four hundred. That is more than two and a half times in seven years.""",
   "Chevrolet 454 SS truck black", "1991: $23,700 TO $60,400")
sc("""And the twist: Hagerty still thinks it has room to grow. In December twenty twenty-five, the four fifty-four S S was named on Hagerty's twenty twenty-six Bull Market list, its annual selection of eleven vehicles expected to rise in value. A truck that was once a punchline is now officially on the watch list of the biggest name in collector insurance.""",
   "Chevrolet 454 SS pickup red", "HAGERTY 2026 BULL MARKET LIST")
sc("""Why is it climbing? The people who were teenagers when it came out are now in their forties and fifties, with money to spend. That is the same pattern that drove muscle car prices up a generation ago. When a buyer sees a four fifty-four S S, they are not seeing a truck. They are seeing the poster on their bedroom wall.""",
   "Chevrolet C/K 1990 pickup", "NOSTALGIA DRIVES PRICES")
sc("""The catch is condition. A low-mile, original four fifty-four S S is now a collector item. A worn one with a swapped engine is not. Before you pay collector money, check the build code, the original engine, and the interior trim. And be honest with yourself. At eight miles per gallon, this is a weekend truck, not a commuter.""",
   "Chevrolet 454 SS black truck", "CHECK THE BUILD CODE")

# ---------- 4. SVT LIGHTNING ----------
sc("""Number four is Ford's answer to the four fifty-four S S, and it ended up even more valuable. The Ford S V T Lightning. Ford built it in two generations, from nineteen ninety-three to nineteen ninety-five, and from nineteen ninety-nine to two thousand four. A factory hot rod pickup, built by Ford's Special Vehicle Team.""",
   "Ford SVT Lightning pickup", "4. FORD SVT LIGHTNING")
sc("""The second generation came with a supercharged V eight. According to Ford Authority, in February twenty twenty-six, the average value of a number two condition second-generation Lightning went from around twenty thousand dollars in twenty sixteen to forty-eight thousand seven hundred dollars by twenty twenty-four. More than double in eight years.""",
   "Ford F-150 SVT Lightning 2003", "2ND GEN: $20K TO $48,700")
sc("""The first generation climbed too, from around fifteen thousand dollars to forty-two thousand four hundred over the same period. And there are roughly half as many first-generation trucks as second-generation ones, which is why the clean ones are getting hard to find. According to V E H Q, one first-generation Lightning with only one hundred fifty miles sold at auction for seventy-five thousand dollars.""",
   "Ford SVT Lightning 1994", "1ST GEN: $15K TO $42,400")
sc("""Now here is the twist, and it tells you who is buying. According to the same Ford Authority report, millennials are the largest group in this market. They make up forty percent of the first-generation Lightning market and thirty-five percent of the second-generation market. Gen Z is second. The people driving these prices up are not retirees. They are the kids who grew up playing racing video games with this truck in them.""",
   "Ford SVT Lightning red pickup", "MILLENNIALS: 40% OF BUYERS")
sc("""And there is a second twist. The name Lightning came back as an electric truck in twenty twenty-two, and in December twenty twenty-five Ford ended production of that electric F-one-fifty Lightning after a nineteen point five billion dollar charge on its electric strategy. So the gas-powered Lightning from the nineties is a classic, and the electric Lightning from this decade is already discontinued.""",
   "Ford F-150 Lightning electric", "THE NEW LIGHTNING: ALREADY ENDED")
sc("""What do you check on an S V T Lightning? Mileage and originality matter more here than on almost any truck. Many were modified for more boost. A stock truck with records is the one that holds value. And be careful with the word clean. Ask for photos of the frame, the supercharger, and the paperwork before you travel to see one.""",
   "Ford SVT Lightning engine supercharger", "STOCK + RECORDS = VALUE")

# ---------- 5. TASK FORCE / EARLY TRUCKS ----------
sc("""Number five is the one most people overlook, and it is the oldest on the list. The nineteen fifty-five to nineteen fifty-nine Chevrolet Task Force trucks, the thirty-one hundred, and their cousins from GMC. These were the first Chevy pickups with a factory V eight, wraparound windshields, and styling borrowed from the cars of the fifties.""",
   "Chevrolet 3100 Task Force pickup", "5. CHEVY TASK FORCE 1955-1959")
sc("""Why are they on a buy list? Because the market for fifties trucks has been quiet while the attention went to newer models. At Barrett-Jackson Scottsdale in January twenty twenty-six, a custom nineteen fifty-seven thirty-one hundred Stepside sold for forty-four thousand dollars, well below the sixty thousand five hundred dollar median of the auction.""",
   "1957 Chevrolet 3100 pickup", "1957 3100: $44,000 IN 2026")
sc("""And here is the twist. Classic.com listed seventy-one Chevrolet thirty-one hundred pickups from nineteen fifty-five to nineteen fifty-nine for sale at the same time. That is a lot of supply. When there are many trucks on the market, the buyer has the power. You can walk away, compare, and negotiate. That is rare in the classic truck world right now.""",
   "Chevrolet Apache pickup 1959", "71 FOR SALE: BUYER HAS POWER")
sc("""Design is part of the appeal. The Task Force trucks had a wraparound windshield, a wide grille, and in nineteen fifty-five, the luxurious Cameo Carrier, with smooth fiberglass bed sides. It was a pickup made to look like a car. Today, those design details are exactly what collectors pay for, and they photograph beautifully, which matters more than ever in the age of social media.""",
   "Chevrolet Cameo Carrier", "1955 CAMEO: A TRUCK LIKE A CAR")
sc("""There is a catch, and it is age. A truck from the fifties needs more work than one from the eighties. Brakes, wiring, and steering were designed for a different world. Many owners add modern brakes and power steering for safety. That is smart, but every change moves the truck further from original, so decide early what you want: a driver or an investment.""",
   "Chevrolet 3100 pickup restored", "DRIVER OR INVESTMENT?")


# ---------- HONORABLE MENTIONS ----------
sc("""Before we get to who is really buying these trucks, three honorable mentions, because each one has a twist of its own. The first is the GMC Syclone, from nineteen ninety-one. A small pickup with a turbocharged V six and all-wheel drive. According to V E H Q, only two thousand nine hundred ninety-eight were built, which makes it far rarer than the four fifty-four S S.""",
   "GMC Syclone", "MENTION: GMC SYCLONE, 2,998 BUILT")
sc("""Its values tell a strange story. According to Hagerty figures cited by V E H Q, a Syclone was valued at about twenty-seven thousand three hundred dollars in January twenty twenty-three, and about thirty thousand nine hundred in July twenty twenty-four. Steady, not explosive. But in May twenty twenty-five, one sold at auction for one hundred thirty thousand dollars. The average is calm. The best examples are not.""",
   "GMC Syclone pickup red", "SYCLONE: $30,900 AVG, $130K TOP")
sc("""That gap is the lesson. For rare trucks, the average value tells you very little. A perfect, low-mile example can sell for four times the average, while a tired one struggles to find a buyer. If you are buying as an investment, buy the best one you can afford, not the cheapest one you can find.""",
   "GMC Syclone truck", "BUY THE BEST, NOT THE CHEAPEST")
sc("""The second honorable mention is the nineteen sixty-five to nineteen seventy-one Dodge D-Series pickup. In a Hagerty comparison, it was valued slightly above both the Chevy and the Ford of the same era. The most valuable version was the nineteen sixty-five D one hundred Sweptline Custom Sports Special with a four twenty-six cubic inch V eight, worth forty-nine thousand five hundred dollars in excellent condition.""",
   "Dodge D100 Sweptline pickup", "MENTION: DODGE D-SERIES")
sc("""Here is the twist with the old Dodge. Far fewer were built than Fords and Chevys, so parts are harder to find, and restoration costs more. Rarity helps the value, but it hurts the owner. Before you buy, find out where the trim, glass and body parts will come from.""",
   "Dodge D200 pickup classic", "RARE = HARDER TO RESTORE")
sc("""The third honorable mention is not a pickup, but it is built on one. The nineteen eighty-one to nineteen ninety-three Dodge Ramcharger, a full-size S U V on the Dodge truck chassis. It was also named on Hagerty's twenty twenty-six Bull Market list. It shows how the market is moving toward eighties and nineties trucks and truck-based S U Vs.""",
   "Dodge Ramcharger", "MENTION: DODGE RAMCHARGER")

# ---------- BONUS TWIST ----------
sc("""Now, one more twist that matters for anyone buying in twenty twenty-seven. In twenty twenty-six, according to Hagerty data reported by The Autopian in May, Gen Z made up about ten percent of collector insurance quotes. Boomers were still the biggest group, at about thirty-four percent, followed by Gen X at thirty-one percent and millennials at twenty percent.""",
   "classic car show pickups", "WHO BUYS CLASSICS IN 2026")
sc("""But Gen Z's favorite collector vehicles this year were not trucks at all. Their top pick was a tiny Japanese sports car, the Honda Beat. So the long-term demand for classic American trucks depends on millennials and Gen X, the two groups who grew up with them. That is why trucks from the eighties and nineties are rising, while some trucks from the fifties are flat.""",
   "Honda Beat", "GEN Z PICKED A HONDA BEAT")
sc("""The pattern is simple. Prices follow nostalgia. People buy the truck they wanted when they were young, once they can afford it. Today, that means the Bullnose Ford, the four fifty-four S S and the S V T Lightning. In ten years, it may mean trucks from the two thousands. If you want to stay ahead, look at what today's thirty-five-year-olds dreamed about as teenagers.""",
   "Ford F-150 SVT Lightning Chevrolet 454 SS", "PRICES FOLLOW NOSTALGIA")

sc("""One more honest point before the checklist. A classic truck is not a savings account. Values can fall, like the early Bronco did this year. Insurance, storage and repairs cost money every month. The buyers who do best are the ones who would be happy owning the truck even if its value stayed flat. If the truck rises, that is a bonus.""",
   "classic pickup truck show", "NOT A SAVINGS ACCOUNT")
sc("""And there is a timing question. Classic prices usually move in waves. A truck jumps when a new group of buyers discovers it, and then it often levels off. The Bullnose Ford is in that jump right now. The four fifty-four S S and the Lightning have already doubled. The fifties Chevy is waiting. Knowing where a truck sits in that wave is the difference between buying early and buying the top.""",
   "Ford F-150 1980s Chevrolet pickup", "WHERE IS EACH TRUCK IN THE WAVE?")

# ---------- CLOSE ----------
sc("""So here is what to check before you buy any classic pickup in twenty twenty-seven. First, check the trend. Use a valuation tool and look at the last three years, not just today's price. A truck rising thirty-two percent in a quarter, like the Bullnose, is a different buy from one that is flat or falling, like the early Bronco.""",
   "Ford F-Series classic pickups", "CHECK 1: THE TREND")
sc("""Second, know whether it is original or custom. That one word can change the value by tens of thousands of dollars. Third, look underneath. Frames, cab corners, floors and bed supports tell you more than shiny paint. Fourth, check the documents: title, build sheet, and service records. A truck with a story you can prove is worth more than one with a story you have to believe.""",
   "pickup truck frame restoration", "CHECK 2, 3 AND 4")
sc("""And fifth, count the full cost. Insurance, storage, parts, and the repairs every old truck eventually needs. A cheap truck that needs everything is often the most expensive truck you will ever buy. If you budget for the work before you buy, you will enjoy the truck instead of fighting it.""",
   "classic pickup truck garage", "CHECK 5: THE FULL COST")
sc("""We put the full checklist, for new and used trucks, into the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a seller, and the warning signs we talked about today. The link is in the description and in the pinned comment. Subscribe for the next video, where we go through the history of the Ford F-Series in five turning points. Thanks for watching.""",
   "Ford F-100 classic pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One old Ford pickup": "Intro", "Number one": "1. Ford F-Series 1980-1986 (Bullnose)",
      "Number two": "2. Chevrolet C/K 1967-1972", "Number three": "3. Chevrolet 454 SS",
      "Number four": "4. Ford SVT Lightning", "Number five": "5. Chevrolet Task Force 1955-1959",
      "Before we get to who": "Honorable mentions", "Now, one more twist": "Who is really buying classic trucks",
      "So here is what to check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video41", "length_scale": 1.45,
  "title": "5 Classic American Pickups Worth Buying Now (Before 2027 Prices Jump)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
