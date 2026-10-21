import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In January twenty twenty-six, a seventy-year-old Dodge work truck sold for eighty-eight thousand dollars. A Toyota pickup that people used to drive into the ground is now insured by four times as many collectors as in twenty seventeen. And in September twenty twenty-six, the very first Ford Bronco Raptor, which once sold for three hundred fifty thousand dollars, sold again for one hundred five thousand. Some trucks become collectibles. Some only pretend to.""",
   "Dodge Power Wagon", "TRUCKS THAT BECAME COLLECTIBLES")
sc("""These are five trucks that really became collectibles, with the numbers to prove it, and the warning signs of trucks that did not. If you own an old truck, or you are thinking of buying one as an investment, this video could save you, or make you, a lot of money. Stay to the end for the twist about the so-called instant collectible.""",
   "Toyota pickup 4x4 1980s", "REAL COLLECTIBLES VS FAKE ONES")
sc("""Every number in this video comes from a published source, listed in the description. If we could not confirm a figure, we left it out. Let's start with the oldest truck on the list, a truck that was built for war and became a legend.""",
   "Dodge Power Wagon 1950s", "EVERY NUMBER IS SOURCED")

# ---------- 1. POWER WAGON ----------
sc("""Number one is the Dodge Power Wagon. After World War Two, Dodge took what it learned building military trucks and sold a civilian four-wheel drive truck to farmers, ranchers and utility companies. It was tough, slow, simple and almost unstoppable. It was built to work in places where roads did not exist.""",
   "Dodge Power Wagon WDX", "1. DODGE POWER WAGON")
sc("""The Power Wagon was also one of the first civilian trucks in America sold with four-wheel drive from the factory as its main purpose. That was rare at the time. Most pickups were two-wheel drive, and buyers who needed more had to convert them. Dodge built the capability in from the start, and that made the truck famous among people who worked in hard places.""",
   "Dodge Power Wagon 4x4", "4WD FROM THE FACTORY")
sc("""For decades, the Power Wagon was exactly what it was designed to be: a tool. Many were worked until they fell apart. Many were left in fields. But the ones that survived are now some of the most valuable classic trucks in America. At Barrett-Jackson Scottsdale in January twenty twenty-six, a nineteen fifty-three Dodge Power Wagon sold for eighty-eight thousand dollars.""",
   "Dodge Power Wagon 1953", "1953 POWER WAGON: $88,000")
sc("""And here is the twist. That truck was rated by Classic dot com as original or highly original. That word matters more than anything else. A Power Wagon that still has its factory parts is a piece of history. One that has been heavily modified can still be a great truck, but it is a different kind of vehicle in the eyes of collectors.""",
   "Dodge Power Wagon original", "TWIST: 'ORIGINAL' IS THE MAGIC WORD")
sc("""Buying one today takes care. Many Power Wagons have been restored with parts from different years, and some have been converted with modern engines. For a collector, matching numbers, original sheet metal and documentation can change the value by tens of thousands of dollars. For a driver, a well-built restomod can be the better choice. The key is knowing which one you are paying for.""",
   "Dodge Power Wagon restored", "ORIGINAL VS RESTOMOD")
sc("""Why did the Power Wagon become a collectible? Because it has a story. It connects to World War Two, to the farms and ranches of the post-war years, and to a time when trucks were built to last. Collectors do not just buy metal. They buy stories. And the Power Wagon has one of the best in American truck history.""",
   "Dodge Power Wagon military", "COLLECTORS BUY STORIES")
sc("""And the name lives on. Ram still sells a Power Wagon version of its heavy-duty pickup, built for off-road work. When a modern company keeps reusing a name for decades, it keeps the original truck in the public eye. That helps the old trucks hold their value, because every new Power Wagon reminds buyers of where the name came from.""",
   "Ram 2500 Power Wagon", "THE NAME LIVES ON")

# ---------- 2. TOYOTA PICKUP ----------
sc("""Number two is a truck that most people never imagined as a collectible. The nineteen eighty-four to nineteen eighty-eight Toyota Pickup four by four, especially the S R five. For years, it was just a used truck. Cheap, tough, and famous for running forever. People drove them hard, lifted them, rusted them, and sold them for a few thousand dollars.""",
   "Toyota pickup 4x4 SR5", "2. TOYOTA PICKUP 4X4, 1984-88")
sc("""Then Hagerty named it a Bull Market pick, its list of vehicles expected to rise in value. According to Hagerty, a number two condition truck, meaning excellent, was valued at twenty-two thousand seven hundred dollars, and a number one, concours, at thirty-four thousand eight hundred. Hagerty wrote that, long considered just a used truck, it had finally achieved collector car status.""",
   "Toyota pickup 1985", "#2 VALUE: $22,700")
sc("""According to Hagerty, boomers still own forty-three percent of these trucks. And a nearly equal third of insurance quotes come from boomers, Gen X and millennials. That is unusual. Most collectibles are dominated by one generation. The Toyota pickup appeals to almost everyone, which is one reason its future looks strong.""",
   "Toyota pickup SR5 1986", "LOVED BY EVERY GENERATION")
sc("""Here is the twist. Hagerty said the number of these trucks on its insurance policies had quadrupled since twenty seventeen. And collectors under forty more than doubled their ownership share since twenty nineteen, from seven percent to sixteen percent. Young collectors are not buying old Ferraris. They are buying the Toyota truck they saw in movies and on the street when they were kids.""",
   "Toyota pickup 4x4 red", "POLICIES: 4X SINCE 2017")
sc("""Why does that matter for buyers? Because demand from younger collectors tends to last longer. They will be in the market for decades. The Toyota pickup's mechanical simplicity also helps. It is easy to fix, parts are available, and it can be driven, not just stored. Collectibles that can be used tend to keep a wider buyer pool.""",
   "Toyota Hilux 1980s", "YOUNG COLLECTORS STAY LONGER")
sc("""And there is an irony here. Toyota's newer pickups also have a reputation for holding value, which is one reason the Tacoma is so popular. According to Pedal Commander, it sold two hundred seventy-four thousand, six hundred thirty-eight units in twenty twenty-five. The reputation the old truck built is still selling new ones forty years later.""",
   "Toyota Tacoma", "THE OLD TRUCK SELLS THE NEW ONE")

# ---------- 3. BULLNOSE ----------
sc("""Number three is a truck that is becoming a collectible right now, in twenty twenty-six. The nineteen eighty to nineteen eighty-six Ford F-Series, nicknamed the Bullnose. According to Hagerty, as reported by Ford Authority in August twenty twenty-six, it rose thirty-two percent in value in the second quarter of twenty twenty-six. That made it one of the biggest gainers among all collectible vehicles.""",
   "Ford F-150 1985", "3. BULLNOSE FORD: +32% IN Q2 2026")
sc("""Here is the twist. Hagerty said the jump was largely driven by heavy-duty models catching up to the lighter duty models. The F-two-fifty and F-three-fifty work trucks, once worth less, are now being valued like the F-one-fifty. And Hagerty noted a notable uptick in activity being led by the F-Series. More people are looking, which usually comes before prices rise further.""",
   "Ford F-250 1980s", "HEAVY-DUTY CATCHING UP")
sc("""At the same time, the first-generation Ford Bronco, a famous collectible, shed twelve percent of its value in the same quarter, according to the same report. And the earliest F-Series pickups had softened. So the money is moving. Collectors are leaving some famous names and moving into trucks that were overlooked. That is how a truck becomes a collectible: when the market discovers it.""",
   "Ford Bronco first generation", "BRONCO: -12% SAME QUARTER")
sc("""Here is what that means for anyone who owns one. If you have a Bullnose F-Series sitting in a barn or behind a house, do not sell it as scrap without checking its value first. Look at the cab, the frame and the paperwork. A truck that seems worthless to you may be exactly what a collector is looking for right now.""",
   "Ford F-Series barn find", "CHECK BEFORE YOU SCRAP IT")
sc("""The Bullnose has something many collectibles do not: huge production numbers. The F-Series has been America's best-selling truck since nineteen seventy-seven, according to Ford. Millions were built. But most were worked to death. Clean, rust-free, original examples are much rarer than the production numbers suggest, and that is where the value is.""",
   "Ford F-150 1980s blue", "MILLIONS BUILT, FEW CLEAN")

# ---------- 4. SVT LIGHTNING ----------
sc("""So what is the best way to buy a Bullnose before prices rise further? Look for heavy-duty trucks with simple specifications and solid frames, since Hagerty says those are catching up fastest. Avoid trucks with major rust in the cab corners and floors, because repairs can cost more than the truck. And buy with documentation whenever possible.""",
   "Ford F-250 1980s pickup", "HOW TO BUY A BULLNOSE")
sc("""Number four is a truck that was designed to be special from the start. The Ford S V T Lightning. Ford's Special Vehicle Team built it from nineteen ninety-three to ninety-five, and again from ninety-nine to two thousand four, with a supercharged V eight in the second generation. A factory performance truck, in limited numbers.""",
   "Ford SVT Lightning", "4. FORD SVT LIGHTNING")
sc("""According to Ford Authority in February twenty twenty-six, the average value of a number two condition second-generation Lightning went from around twenty thousand dollars in twenty sixteen to forty-eight thousand seven hundred by twenty twenty-four. The first generation went from around fifteen thousand to forty-two thousand four hundred. Both more than doubled in about eight years.""",
   "Ford SVT Lightning red", "$20K TO $48,700")
sc("""The Lightning shows another rule of truck collectibles. Limited factory performance models from a big brand tend to do well, because they combine rarity with a famous name. The buyer gets something special, but parts and service knowledge are still available through the brand's huge network. That combination is hard to beat.""",
   "Ford SVT Lightning 2004", "RARE + FAMOUS NAME")
sc("""Here is the twist about who is buying. According to Ford Authority, millennials make up forty percent of the first-generation Lightning market and thirty-five percent of the second-generation market. Gen Z is second, at eight and seven percent. The Lightning is a millennial collectible, bought by people who grew up with it in magazines and video games.""",
   "Ford SVT Lightning black", "MILLENNIALS: 40% OF BUYERS")
sc("""And there is a second twist. Ford reused the Lightning name for its electric F-one-fifty, and then, according to Fox Business, ended production of that electric Lightning in December twenty twenty-five, after a nineteen point five billion dollar charge. The gas Lightning from the nineties is now worth more than double what it was a decade ago, while its electric namesake is already discontinued.""",
   "Ford F-150 Lightning electric", "THE NAME'S TWO FATES")

# ---------- 5. RAM SRT-10 ----------
sc("""Number five is the Dodge Ram S R T ten, from two thousand four to two thousand six. A light-duty Ram pickup with an eight point three liter V ten making five hundred horsepower, according to Hagerty. It was absurd, thirsty and fast, and it lasted only three model years.""",
   "Dodge Ram SRT-10", "5. DODGE RAM SRT-10")
sc("""According to Hagerty in twenty twenty-one, number two condition values had risen forty-six percent in a year, to fifty-four thousand two hundred dollars for regular cabs, and eleven percent to thirty-one thousand seven hundred for Quad Cabs. Over five years, regular cabs were up one hundred seventeen percent. Hagerty also reported sales like sixty-eight thousand two hundred dollars for a two hundred forty-five mile example at Mecum.""",
   "Dodge Ram SRT-10 pickup", "REGULAR CAB: +117% IN 5 YEARS")
sc("""According to Hagerty, Gen Xers and millennials made up sixty percent of S R T ten collectors and sixty-six percent of insurance quotes. Once again, the buyers are the people who were young when the truck was new. In almost every case on this list, the collector market follows the age of the people who first dreamed about the truck.""",
   "Dodge Ram SRT-10 black", "GEN X + MILLENNIALS: 60%")
sc("""Here is the twist. The regular cab with the manual transmission is worth far more than the Quad Cab with the automatic. The rarer, more raw version wins. That is a pattern across collectible trucks. The version that was hardest to live with as a daily vehicle often becomes the most valuable, because fewer were bought and fewer survived.""",
   "Dodge Ram SRT-10 regular cab", "THE RAW VERSION WINS")

# ---------- THE FAKE COLLECTIBLE ----------
# ---------- MENTIONS ----------
sc("""Before the big twist, three honorable mentions, trucks that are on their way. The first is the nineteen ninety to ninety-three Chevrolet four fifty-four S S. According to Hagerty figures cited by V E H Q, an excellent nineteen ninety-one example went from about twenty-three thousand seven hundred dollars in twenty nineteen to about sixty thousand four hundred in early twenty twenty-six. And it was named to Hagerty's twenty twenty-six Bull Market list.""",
   "Chevrolet 454 SS", "MENTION: CHEVY 454 SS")
sc("""The second is the nineteen ninety-one G M C Syclone, the small turbocharged, all-wheel drive pickup. According to V E H Q, fewer than three thousand were built. Its average value was about thirty thousand nine hundred dollars in July twenty twenty-four, according to Hagerty figures, but one sold for one hundred thirty thousand dollars in May twenty twenty-five. The best examples are already serious collectibles.""",
   "GMC Syclone", "MENTION: GMC SYCLONE, $130K TOP")
sc("""The third is the Dodge Li'l Red Express, from nineteen seventy-eight and seventy-nine. Only seven thousand three hundred sixteen were built, and the nineteen seventy-eight version could reach one hundred miles per hour faster than a Corvette. Yet according to a report published in twenty twenty-six, you can still buy one for less than thirty thousand dollars. A collectible with history, still at an entry price.""",
   "Dodge Lil Red Express", "MENTION: LI'L RED EXPRESS, UNDER $30K")
sc("""Notice the pattern in these mentions. The four fifty-four S S has already taken off. The Syclone has taken off for the best examples. The Li'l Red Express has not yet. If you are looking for the next one, look for trucks with a great story and limited production, whose prices have not moved yet. That is where early buyers find value.""",
   "classic pickup trucks", "FIND THE ONE THAT HASN'T MOVED")
sc("""Now the twist we promised, the so-called instant collectible. In April twenty twenty-two, the first production Ford Bronco Raptor, chassis number zero zero zero one, sold at a Barrett-Jackson charity auction for three hundred fifty thousand dollars. The money went to the National Forest Foundation and Outward Bound. It was a new S U V with an original price of sixty-eight thousand five hundred dollars before options.""",
   "Ford Bronco Raptor", "BRONCO RAPTOR #0001: $350,000")
sc("""In September twenty twenty-six, according to autoevolution, the same vehicle sold again on Bring a Trailer, with just ninety-nine miles, for one hundred five thousand dollars. That is less than a third of its charity price. A charity auction is not a market price. People pay extra because the money goes to a good cause, not because the vehicle is worth that much.""",
   "Ford Bronco Raptor orange", "2026 RESALE: $105,000")
sc("""This is the most important lesson in this video. A vehicle does not become a collectible because a company calls it limited, or because a first example sold for a headline price. It becomes a collectible over years, when demand from real buyers grows faster than the supply of good examples. The Power Wagon, the Toyota and the Lightning all took decades.""",
   "classic trucks auction", "COLLECTIBLES TAKE DECADES")
sc("""And sometimes values fall. The first-generation Bronco, one of the most celebrated collectibles of the last decade, lost twelve percent in a single quarter of twenty twenty-six. Even real collectibles go through cycles. Anyone who buys at the top of a wave can wait years to get their money back.""",
   "Ford Bronco classic", "EVEN REAL COLLECTIBLES FALL")

# ---------- PATTERN ----------
sc("""There is a lesson for new truck buyers too. When a dealer tells you a new truck is a future collectible, be careful. Many limited editions are built in large numbers, and most new vehicles lose value in their first years. The Bronco Raptor number zero zero zero one is the extreme case, but the rule applies to every special edition sticker.""",
   "new truck dealership special edition", "BEWARE 'FUTURE COLLECTIBLE'")
sc("""So what turns a truck into a collectible? Five things. A story, like the Power Wagon's link to the war. Nostalgia, like the Toyota and the Lightning for people who grew up with them. Survivors, because most examples were used up. Simplicity, so they can be kept running. And a buyer group that is growing, not shrinking.""",
   "classic pickup trucks show", "WHAT MAKES A COLLECTIBLE")
sc("""And the twist in that list is that none of these trucks were expensive when new. They were work trucks, cheap trucks, or oddball performance trucks. The collectibles of the future are probably sitting in driveways right now, being used every day, and their owners have no idea.""",
   "pickup truck driveway", "THE NEXT ONE IS IN A DRIVEWAY")

# ---------- CLOSE ----------
sc("""So if you want to buy a collectible truck in twenty twenty-seven, here is what to check. First, originality. Original engine, paint, interior and documents can be worth more than any upgrade. Second, the trend. Look at values over three to five years, not one auction. Third, who is buying. A truck loved by younger collectors usually has a longer future.""",
   "classic truck inspection", "CHECKS 1, 2 AND 3")
sc("""Fourth, ignore charity and first-of prices. They are not the market. And fifth, count the full cost: storage, insurance, maintenance and the time it takes to sell. A collectible truck is a passion first and an investment second. Buy the one you will enjoy owning, even if its value never moves.""",
   "classic truck garage", "CHECKS 4 AND 5")
sc("""One last practical tip. Get a valuation from an independent source before you buy or insure a collectible truck, and keep every receipt. A documented history is one of the easiest ways to add value to any old truck. When it is time to sell, buyers pay more for a truck they can trust.""",
   "classic truck documents", "KEEP EVERY RECEIPT")
sc("""We put the full checklist, for new, used and classic trucks, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, where we answer one of the biggest money questions: lease or buy a truck in twenty twenty-seven. Thanks for watching.""",
   "Dodge Power Wagon", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In January twenty twenty-six, a seventy": "Intro", "Number one": "1. Dodge Power Wagon", "Number two": "2. Toyota Pickup 4x4 (1984-88)",
      "Number three": "3. Ford F-Series 1980-86 (Bullnose)", "Number four": "4. Ford SVT Lightning", "Number five": "5. Dodge Ram SRT-10",
      "Before the big twist": "Honorable mentions", "Now the twist we promised": "The instant collectible that crashed", "So what turns a truck": "What makes a collectible",
      "So if you want to buy": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video50", "length_scale": 1.5,
  "title": "5 Trucks That Became Collectibles (And One That Lost $245,000)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
