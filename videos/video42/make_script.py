import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In twenty twenty-five, Ford sold eight hundred twenty-eight thousand, eight hundred thirty-two F-Series trucks in America. That is more than two thousand every single day. It was the forty-ninth year in a row as the country's best-selling truck. And yet, in the third quarter of twenty twenty-six, Ford lost a race it almost never loses. A fire, a sheet of aluminum, and one rival made it happen.""",
   "Ford F-150 pickup", "828,832 F-SERIES IN 2025")
sc("""This is the story of the Ford F-Series in five turning points. The moments that made it the best-selling vehicle in America for forty-four years, and the moments that almost broke it. Some of them you know. Some of them are strange. And the last one is happening right now, in twenty twenty-six.""",
   "Ford F-Series trucks lineup", "THE F-SERIES IN 5 TURNING POINTS")
sc("""Here is the scale. According to Ford, the F-Series has been America's best-selling truck since nineteen seventy-seven, and America's best-selling vehicle, of any kind, for forty-four years. If the F-Series were a company on its own, it would be one of the biggest in the country. It is not just a truck line. It is the engine that pays for almost everything else Ford does.""",
   "Ford F-150 dealership", "49 YEARS #1 TRUCK, 44 YEARS #1 VEHICLE")
sc("""Every number in this video comes from a published source, listed in the description. If we could not confirm a figure, we left it out. Stay until the end, because the final turning point changes what you should look for if you are buying a Ford truck in twenty twenty-seven. Let's go back to the beginning.""",
   "Ford F-1 pickup 1948", "EVERY NUMBER IS SOURCED")

# ---------- 1. 1948 ----------
sc("""Turning point number one. Nineteen forty-eight. World War Two is over, and America is building again. Ford had made pickup trucks before, but they were mostly versions of its cars. In nineteen forty-eight, Ford launched something new: a dedicated line of trucks, built on their own platform. Ford called them the Bonus Built trucks. The smallest was the F-one.""",
   "Ford F-1 pickup 1948", "1. 1948: THE F-1 IS BORN")
sc("""The F-Series started as a full family, from the light F-one pickup up to heavy trucks for commercial work. The idea was simple and powerful. One brand, one look, one dealer, for the farmer, the plumber, and the trucking company. It was the first time Ford treated trucks as their own business, instead of an afterthought to its cars.""",
   "Ford F-1 truck classic", "ONE FAMILY: F-1 UP TO HEAVY TRUCKS")
sc("""And here is the first twist. The F-one was not designed to be loved. It was designed to work. But the post-war years changed how Americans lived. People moved to the suburbs, built houses, and needed something to haul materials on weekends. The work truck slowly became a family vehicle. That shift, which started in the late forties, is the foundation of everything that came after.""",
   "Ford F-1 pickup restored", "TWIST: THE WORK TRUCK GOES HOME")
sc("""To understand why this mattered, think about how trucks were sold before. A truck was often just a car with a bed, built with whatever parts were available. The Bonus Built line changed that. It gave truck buyers their own engineering, their own cabs, and a reason to come back to Ford every time they needed a new one. Loyalty started here.""",
   "Ford F-1 pickup 1950", "LOYALTY STARTS HERE")
sc("""In nineteen fifty-three, for its second generation, Ford renamed the trucks. The F-one became the F-one hundred. The F-two became the F-two-fifty, and the F-three became the F-three-fifty. Those names are still on Ford trucks today, more than seventy years later. Few product names in American history have lasted that long.""",
   "Ford F-100 1953 pickup", "1953: F-1 BECOMES F-100")
sc("""The second generation also brought comfort that work trucks rarely had. A more modern cab, better visibility, and features that made long days easier. It was another small step in the same direction. Every new generation made the pickup a little more like a car inside, while keeping the toughness outside. That balance became Ford's playbook for the next seventy years.""",
   "Ford F-100 pickup interior", "TOUGH OUTSIDE, COMFORT INSIDE")
sc("""Those early F-one hundreds, from nineteen fifty-three to fifty-six, are now some of the most loved classic trucks in America. Restored examples are a common sight at auctions. But what made them important was not their style. It was that Ford had found a formula. Simple, tough, and available in a version for every job.""",
   "Ford F-100 1956 pickup", "A FORMULA THAT WORKED")

# ---------- 2. 1975-1977 ----------
sc("""Turning point number two. The truck that became the most famous name in the line was born almost by accident. In nineteen seventy-five, Ford introduced the F-one-fifty. It sat between the F-one hundred and the F-two-fifty. A half-ton truck with a little more capability.""",
   "Ford F-150 1970s pickup", "2. 1975: THE F-150 ARRIVES")
sc("""Here is the twist. The F-one-fifty is widely reported to have been created partly because of emissions rules in the seventies. Trucks above a certain weight rating faced different requirements. A truck with a slightly higher rating could fit into a different class. So the most famous pickup name in America may have started as a clever answer to a regulation.""",
   "Ford F-150 1977 pickup", "TWIST: BORN FROM A REGULATION")
sc("""Whatever the exact reason, the timing was perfect. The seventies were the decade when pickups stopped being just for farms. Fuel crises pushed many buyers toward smaller cars, but at the same time, a growing number of Americans discovered that a truck could be a daily driver, a weekend toy, and a work tool all at once. The F-one-fifty was ready for them.""",
   "Ford F-150 1979 pickup", "THE RIGHT TRUCK AT THE RIGHT TIME")
sc("""Two years later, in nineteen seventy-seven, the F-Series became the best-selling truck in America. It has held that title every year since. Forty-nine years in a row, according to Ford. Think about everything that has changed since nineteen seventy-seven. Oil crises, recessions, new rivals from Japan, electric trucks. Through all of it, the F-Series stayed on top.""",
   "Ford F-Series 1977 pickup", "1977: #1 TRUCK. NEVER LOST IT")
sc("""And a few years later, the F-Series became the best-selling vehicle of any kind in America, ahead of every car. According to Ford, it has now held that title for forty-four years. The pickup truck, once a tool for farms and job sites, was now the most popular vehicle in the country.""",
   "Ford F-150 1980s pickup", "#1 VEHICLE: 44 YEARS")
sc("""In nineteen eighty, the seventh generation arrived, the trucks fans call the Bullnose. Today, they are one of the hottest classics in the market. According to Hagerty, as reported by Ford Authority, the nineteen eighty to eighty-six F-Series rose thirty-two percent in value in the second quarter of twenty twenty-six alone. The trucks that won the sales crown are now winning at auction.""",
   "Ford F-150 1985 pickup", "1980-86 BULLNOSE: +32% IN Q2 2026")
sc("""Here is a twist that surprises many people. Being number one for so long creates its own momentum. Fleet buyers, like utility companies and contractors, often buy the same truck again so their parts and training stay the same. Families buy what their parents drove. Dealers stock what sells. Once the F-Series took the lead, every one of those habits helped it keep the lead.""",
   "Ford F-Series fleet trucks", "TWIST: WINNING CREATES WINNING")
sc("""Why did the F-Series keep winning in those years? A big reason was choice. Regular cab, extended cab, long bed, short bed, two-wheel drive, four-wheel drive, six cylinder, V eight. A buyer could build almost exactly the truck they wanted. Rivals had good trucks too, but few could match the range of the F-Series lineup.""",
   "Ford F-250 pickup 1980s", "THE SECRET: CHOICE")

# ---------- 3. 1997-1999 ----------
sc("""Turning point number three. The biggest risk Ford ever took with its best-seller. For the nineteen ninety-seven model year, Ford launched a completely redesigned F-one-fifty. It was round, smooth, and aerodynamic, and it looked nothing like the boxy truck before it. Many loyal buyers hated it at first.""",
   "Ford F-150 1997 pickup", "3. 1997: THE BIG GAMBLE")
sc("""Think about how big that risk was. The F-Series was already the best-selling vehicle in America. Most companies protect a best-seller and change it slowly. Ford threw out the old shape completely. If buyers had rejected it, Ford would have lost its most important product. Inside the company, it was a bet on where the market was going, not where it had been.""",
   "Ford F-150 1998 pickup", "RISKING THE BEST-SELLER")
sc("""The redesign was aimed at a new kind of buyer. Not just the contractor, but the family that wanted a comfortable truck to drive every day. It rode more like a car and had a more refined interior. It was a bet that the future of the pickup was personal use, not just work.""",
   "Ford F-150 tenth generation", "BUILT FOR FAMILIES, NOT JUST WORK")
sc("""And here is the twist. To keep its heavy-duty customers happy, Ford split the line. Starting with the nineteen ninety-nine model year, the bigger F-two-fifty and F-three-fifty became the Super Duty, a separate, tougher truck. That decision created two businesses inside one name. And it worked. According to Ford, Super Duty had its best sales year since two thousand four in twenty twenty-five.""",
   "Ford Super Duty F-250", "TWIST: THE SUPER DUTY SPLIT")
sc("""The nineties also brought a factory hot rod, the S V T Lightning, built from nineteen ninety-three to ninety-five and again from ninety-nine to two thousand four. According to Ford Authority, a second-generation Lightning in good condition went from about twenty thousand dollars in twenty sixteen to forty-eight thousand seven hundred by twenty twenty-four. Remember that name. Lightning. It will come back in a very different form.""",
   "Ford SVT Lightning", "SVT LIGHTNING: $20K TO $48,700")
sc("""Here is why the Super Duty split still matters to buyers today. Because the two trucks were separated, Ford could make the F-one-fifty lighter and more comfortable, while making the Super Duty heavier and stronger. Each truck could be good at its own job, instead of one truck trying to do everything. Rivals eventually followed the same approach.""",
   "Ford F-350 Super Duty", "EACH TRUCK GOOD AT ITS OWN JOB")
sc("""In two thousand eleven, another quiet revolution happened. Ford put a twin-turbo V six, the EcoBoost, into the F-one-fifty. Many truck buyers swore they would never buy a pickup without a V eight. Then they drove it. The EcoBoost became one of the most popular engines in the lineup, and it changed what Americans expected from a truck engine.""",
   "Ford F-150 EcoBoost", "2011: THE V6 THAT WON")

# ---------- 4. 2015 ALUMINUM ----------
sc("""Turning point number four. Twenty fifteen. Ford did something no other mass-market truck maker had dared to do. It built the body of the F-one-fifty out of aluminum instead of steel. The truck lost a lot of weight, which helped fuel economy, towing and payload. Competitors mocked it. Some ads even questioned whether aluminum was tough enough for a real truck.""",
   "Ford F-150 thirteenth generation", "4. 2015: THE ALUMINUM BODY")
sc("""Ford's argument was simple. Aluminum is the material used in airplanes and many military vehicles. It does not rust like steel. And a lighter truck can carry and tow more for the same engine. Critics argued that repairs would cost more and that insurers would charge more. For a while, both sides had a point.""",
   "Ford F-150 2015 pickup", "AIRPLANE METAL VS STEEL")
sc("""The switch was enormous. Ford had to retool its factories, train body shops, and convince loyal buyers. For a while, sales slowed as plants changed over. But the bet paid off. The aluminum F-one-fifty kept the sales crown, and the material became part of the truck's identity.""",
   "Ford Dearborn Truck Plant", "RETOOL EVERYTHING")
sc("""Now here is the twist, and it is happening right now. Using aluminum made the F-Series depend on a small number of aluminum suppliers. On September sixteenth, twenty twenty-five, a fire broke out at the Novelis aluminum plant in Oswego, New York. On November twentieth, a second significant fire hit the same plant. That plant supplies a large share of the aluminum sheet for Ford trucks.""",
   "Novelis Oswego aluminum plant", "SEPT 16, 2025: FIRE AT NOVELIS")
sc("""The damage was real. According to Automotive Logistics, Ford's chief financial officer Sherry House confirmed a production loss of about one hundred thousand vehicles across twenty twenty-five. On the February twenty twenty-six earnings call, chief executive Jim Farley referred to a two billion dollar headwind from the Novelis fires. Novelis said it expected to restart the hot mill late in the second quarter of twenty twenty-six.""",
   "Ford F-150 assembly plant", "~100,000 VEHICLES LOST")
sc("""For buyers, the effect was visible on dealer lots. Ford Authority reported in October twenty twenty-five that F-one-fifty production at the Dearborn assembly plant was cut sharply while aluminum supply was limited. Fewer trucks being built usually means fewer discounts, and buyers who wanted a specific configuration sometimes had to wait or pay more.""",
   "Ford Dearborn Truck Plant F-150", "FEWER TRUCKS, FEWER DISCOUNTS")
sc("""So the decision that helped the F-one-fifty win in twenty fifteen became its weak point ten years later. One supplier, one city, one fire. Ford said it planned to add fifty to sixty thousand units of production in twenty twenty-six to make up for the loss. It shows how a single part of a supply chain can shake the best-selling vehicle in America.""",
   "Ford F-150 aluminum truck", "ONE SUPPLIER, ONE FIRE")

# ---------- 5. 2021-2026 ----------
sc("""Turning point number five. The electric bet, and the U-turn. In twenty twenty-one, Ford launched the fourteenth-generation F-one-fifty, including a hybrid called PowerBoost. Then came the big one. The F-one-fifty Lightning, a fully electric pickup, using the name of the nineties hot rod. Orders poured in, and for a while it looked like the future had arrived.""",
   "Ford F-150 Lightning", "5. THE ELECTRIC BET")
sc("""It did not last. According to Fox Business, on December sixteenth, twenty twenty-five, Ford announced a nineteen point five billion dollar charge as it changed its electric vehicle strategy, and ended production of the all-electric Lightning. In the third quarter of twenty twenty-six, according to autoevolution, Ford sold just two hundred eighty-nine Lightnings, compared with ten thousand and five a year earlier.""",
   "Ford F-150 Lightning pickup", "Q3: 10,005 TO 289")
sc("""What went wrong? Price was a big part of it. Electric trucks cost more to build, and when the federal tax credit for electric vehicles ended in twenty twenty-five, the gap got wider. Towing range was another. A heavy trailer could cut the range of an electric pickup dramatically, and many truck buyers tow. The Lightning was a great truck for some people, just not enough of them.""",
   "Ford F-150 Lightning towing trailer", "WHY THE LIGHTNING STRUGGLED")
sc("""But here is the twist. While the electric truck faded, the hybrid exploded. According to Ford, it sold eighty-four thousand, nine hundred thirty-four F-one-fifty hybrids in twenty twenty-five, up fifteen percent. The small Maverick hybrid sold eighty-one thousand and thirty-four. In total, Ford sold two hundred twenty-eight thousand hybrid vehicles in twenty twenty-five. The future arrived, just not in the form Ford expected.""",
   "Ford F-150 hybrid PowerBoost", "F-150 HYBRID: 84,934 IN 2025")
sc("""This tells you something important about truck buyers. They are willing to change, but slowly. A hybrid feels familiar. It fills up at a gas station, tows like a normal truck, and still saves fuel in town. Ford's own numbers show that American truck buyers chose the step that felt safest, not the leap.""",
   "Ford F-150 PowerBoost hybrid", "BUYERS CHOSE THE SAFE STEP")
sc("""And the Lightning name is not dead. Ford has said it plans to bring it back as an extended-range electric truck, with a gas engine that charges the battery. So the name has now lived three lives. A supercharged hot rod, a battery-electric truck, and soon, a hybrid of both ideas.""",
   "Ford F-150 Lightning Platinum", "LIGHTNING: THREE LIVES")

# ---------- 2026 RACE ----------
sc("""Now back to the race we mentioned at the start. In the third quarter of twenty twenty-six, according to autoevolution, Ford delivered two hundred three thousand, seven hundred seven F-Series trucks, down one point nine percent. Still the best-selling single truck line. But Chevrolet and GMC together delivered two hundred thirty-three thousand, two hundred twenty-nine Silverado and Sierra pickups.""",
   "Chevrolet Silverado GMC Sierra", "Q3 2026: GM 233,229 VS FORD 203,707")
sc("""That is the twist that has followed the F-Series for decades. Ford counts one brand. General Motors sells the same basic truck under two brands, Chevrolet and GMC. Count them separately, and Ford wins. Count them together, and in some quarters, GM wins. Both sides have used the numbers that suit them. As a buyer, it simply means the competition is closer than the ads suggest.""",
   "Chevrolet Silverado pickup", "TWO BRANDS VS ONE")
sc("""There is one more detail. The F-Series number includes the Super Duty heavy-duty trucks, while some rival figures are split between light and heavy-duty models. So comparing truck sales is never as simple as reading one headline. When you see a claim about who is number one, always ask which trucks are being counted.""",
   "Ford Super Duty Chevrolet Silverado HD", "ASK WHICH TRUCKS ARE COUNTED")
sc("""And there is a third player moving fast. In the same quarter, Ram's combined light and heavy-duty trucks rose thirty-three point seven percent, to one hundred seventeen thousand, seven hundred fifty-seven, according to autoevolution. Ram brought back its Hemi V eight, and buyers responded. The full-size truck war in twenty twenty-six is a three-way fight again.""",
   "Ram 1500 pickup", "RAM: +33.7% IN Q3 2026")
sc("""Meanwhile, Ford's smaller trucks are growing. According to Ford, the Maverick sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, up eighteen percent, and the Ranger sold seventy thousand, nine hundred sixty, up fifty-three point six percent. The F-Series is still the king, but Ford's future growth may come from the trucks below it.""",
   "Ford Maverick pickup", "MAVERICK 155,051 / RANGER 70,960")

# ---------- LESSONS ----------
sc("""So what do these five turning points have in common? Every time, Ford took a risk that people said would fail. A dedicated truck line in nineteen forty-eight. A new name in nineteen seventy-five. A round, soft design in ninety-seven. An aluminum body in twenty fifteen. An electric truck in twenty twenty-two. Four of those bets won. One did not, and Ford changed course within a few years.""",
   "Ford F-Series history trucks", "5 RISKS, 4 WINS")
sc("""And notice the pattern in the bet that failed. The electric Lightning was the only turning point where Ford moved faster than its buyers. Every successful change, from the F-one-fifty name to the aluminum body to the hybrid, moved the truck forward while keeping what buyers already trusted. When Ford asked buyers to change too much, too quickly, they said no.""",
   "Ford F-150 Lightning Ford F-150", "THE ONE BET THAT MOVED TOO FAST")
sc("""And here is the last twist. The F-Series did not stay on top because it was always the best truck. In many years, critics preferred a rival. It stayed on top because it offered the widest range, the biggest dealer network, and a name buyers trusted. That trust is worth more than any single feature.""",
   "Ford F-150 dealership lot", "TRUST BEATS FEATURES")

sc("""One more detail shows how deep the F-Series runs in American life. Many fleets, from utility companies to city governments, standardize on one truck so that parts, training and repairs stay simple. Once a fleet chooses the F-Series, it often keeps buying it for decades. That fleet loyalty is a quiet engine behind the forty-nine year streak, and it rarely shows up in the headlines.""",
   "Ford F-150 fleet trucks", "FLEETS KEEP THE STREAK ALIVE")

# ---------- CLOSE ----------
sc("""So what does this history mean if you are buying a Ford truck in twenty twenty-seven? First, check the powertrain trend. The hybrid F-one-fifty is selling strongly, while the electric Lightning has ended. A truck with growing demand is usually easier to resell and to service.""",
   "Ford F-150 hybrid", "CHECK 1: THE POWERTRAIN TREND")
sc("""Second, check production and supply. After the Novelis fires, some trims and configurations were harder to find. If the exact truck you want is scarce, dealers have less reason to discount it. Being flexible on color or trim can save real money.""",
   "Ford F-150 dealer inventory", "CHECK 2: SUPPLY")
sc("""Third, compare the full lineup, not just the F-one-fifty. A Maverick or Ranger may do everything you need for much less. Fourth, compare across brands. With Ram and GM pushing hard in twenty twenty-six, competition is fierce, and that gives buyers leverage. And fifth, look at the total cost: fuel, insurance, and what the truck will be worth in five years.""",
   "Ford Ranger Ford Maverick", "CHECKS 3, 4 AND 5")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the numbers to compare, the questions to ask a dealer, and the warning signs to watch for. The link is in the description and in the pinned comment. Subscribe for the next video, where we break down the Chevy versus Ford versus Ram rivalry. Thanks for watching.""",
   "Ford F-150 pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In twenty twenty-five, Ford sold": "Intro", "Turning point number one": "1. 1948: the F-1 is born",
      "Turning point number two": "2. 1975-1977: the F-150 and the sales crown",
      "Turning point number three": "3. 1997-1999: the big gamble and Super Duty",
      "Turning point number four": "4. 2015: the aluminum body (and the 2025 fires)",
      "Turning point number five": "5. The electric bet and the U-turn",
      "Now back to the race": "The 2026 truck war", "So what does this history mean": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video42", "length_scale": 1.45,
  "title": "The Ford F-Series in 5 Turning Points (And the Fire That Shook It in 2026)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
