import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""A pickup that cost two hundred eighty-one dollars. A truck that was legally turned into a car by bolting two seats into its bed. A trade war over chicken that still decides which trucks you can buy in twenty twenty-six. And a small hybrid pickup that Ford sold more than one hundred fifty-five thousand times last year. These are the pickups that changed America, and most people only know half the story.""",
   "Ford Model T pickup", "5 PICKUPS THAT CHANGED AMERICA")
sc("""Each one of these trucks changed something bigger than the truck market. How Americans work, where they live, what they pay, and even the laws of the country. And every one of them still shapes the truck you will buy in twenty twenty-seven. Some of the twists in this story are so strange they sound made up. They are not. Every one of them is documented.""",
   "Ford Maverick pickup", "EVERY ONE STILL SHAPES 2027")
sc("""Every number in this video comes from a published source, listed in the description. If we could not confirm a figure, we left it out. Let's go back almost exactly one hundred years, to the truck that started it all.""",
   "Ford Model T 1925", "EVERY NUMBER IS SOURCED")

# ---------- 1. MODEL T PICKUP ----------
sc("""Number one is the nineteen twenty-five Ford Model T Runabout with a pickup body. According to The Henry Ford museum, Ford introduced its light-duty Model T runabout pickup in April nineteen twenty-five. It came with a factory-installed steel pickup bed. And it was priced at two hundred eighty-one dollars.""",
   "1925 Ford Model T pickup", "1. 1925 MODEL T PICKUP: $281")
sc("""Before this, if you wanted a pickup, you usually bought a car or a chassis and had a bed built by someone else. Farmers cut the back off their cars. Small companies sold conversion kits. Ford's idea was simple: build the truck at the factory, sell it at the dealer, and make it cheap enough for anyone who worked with their hands.""",
   "Ford Model T truck", "BEFORE: CUT THE BACK OFF YOUR CAR")
sc("""It worked. According to The Henry Ford, the company sold nearly thirty-three thousand eight hundred units in that first year. For a brand-new kind of vehicle, that was a huge number. Farmers, delivery workers and small business owners suddenly had a tool that could carry goods to town and back in a single day.""",
   "Ford Model T pickup farm", "~33,800 IN YEAR ONE")
sc("""And here is the twist. The Model T pickup was not designed as a lifestyle vehicle at all. It was a tool. But it planted an idea in the American mind that has never gone away: that a working person can own a vehicle that does real work and still drive it to church on Sunday. Every pickup sold today, from a work truck to a ninety-thousand-dollar luxury model, comes from that idea.""",
   "Ford Model T Runabout", "TWIST: A TOOL BECOMES AN IDENTITY")
sc("""The Model T pickup also changed where Americans could live. A farmer with a truck could live farther from town and still sell crops. A builder could carry tools to jobs across the county. Small towns grew around roads instead of railroads. The pickup became part of how rural America worked, long before it became a symbol on television.""",
   "Ford Model T truck rural", "IT CHANGED WHERE PEOPLE LIVED")
sc("""Think about the price. Two hundred eighty-one dollars in nineteen twenty-five. Today, the average new full-size pickup costs many times what the average worker earns in a month. The Model T pickup was affordable by design. That idea, the cheap, simple truck for everyone, is exactly what disappeared over the next hundred years. And it is exactly what the last truck on this list tried to bring back.""",
   "Ford Model T pickup restored", "AFFORDABLE BY DESIGN")

# ---------- 2. RANCHERO / EL CAMINO ----------
sc("""Number two is a truck that was not really a truck. In nineteen fifty-seven, Ford launched the Ranchero. It was a car, with the front of a Ford sedan, and a pickup bed where the back seat and trunk would be. Two years later, Chevrolet answered with the El Camino. A new kind of vehicle was born: the car-based pickup.""",
   "Ford Ranchero 1957", "2. FORD RANCHERO, 1957")
sc("""Why did it matter? Because it was the first time an American carmaker openly sold a pickup as a lifestyle choice. The Ranchero and El Camino rode like cars, looked like cars, and came with car engines, including big V eights. They were for people who wanted the image and the usefulness of a truck, without the rough ride.""",
   "Chevrolet El Camino 1959", "1959: CHEVY ANSWERS WITH THE EL CAMINO")
sc("""The El Camino became a legend. Chevrolet offered it with muscle car engines in the late sixties and early seventies, and today the high-performance versions are prized classics. The Ranchero ended in nineteen seventy-nine. The El Camino lasted until nineteen eighty-seven. And then, for decades, the idea disappeared from America.""",
   "Chevrolet El Camino SS", "EL CAMINO: GONE AFTER 1987")
sc("""Here is the twist. The idea did not die. It just took a different form. When Ford launched the small Maverick pickup in twenty twenty-one, built on a car-like platform, and Hyundai launched the Santa Cruz, many reviewers compared them to the Ranchero and El Camino. A comfortable, car-based truck for people who mostly drive on paved roads. The fifties idea came back sixty-five years later.""",
   "Hyundai Santa Cruz", "TWIST: THE IDEA CAME BACK")
sc("""There is another twist in the Ranchero story. Ford launched the Ranchero first, but the El Camino became the more famous name. Being first is not the same as winning. Chevrolet watched, waited, and then offered more power and more style. That pattern repeats again and again in the truck business, and it is still happening today with small pickups.""",
   "Chevrolet El Camino 1970", "FIRST IS NOT THE SAME AS WINNING")
sc("""And the Ranchero changed something deeper. It proved that many people who buy a pickup do not need a heavy-duty work truck. They want a bed for weekend projects, sports gear and home improvement trips. That insight is behind almost every pickup sold today. The modern pickup is as much a family car as a work tool, and the Ranchero was the first to say so out loud.""",
   "Ford Ranchero", "THE TRUCK AS A FAMILY CAR")

# ---------- 3. CHICKEN TAX ----------
sc("""Number three is not one truck, but a law that changed every truck. And it started with chicken. According to The Daily Vroom, in nineteen sixty-two, European farmers objected to cheap American chicken, with West Germany leading the push back. Europe put tariffs on American chicken. In nineteen sixty-four, President Lyndon Johnson responded with retaliatory tariffs on four European imports. One of them was light trucks.""",
   "Volkswagen Type 2 pickup", "3. 1964: THE CHICKEN TAX")
sc("""The rate was twenty-five percent. At the time, one of the targets was the Volkswagen pickup, based on the famous V W bus. Three of the four retaliatory tariffs were dropped within a few years. The tax on light trucks never was. As The Daily Vroom wrote in April twenty twenty-six, sixty-one years later, it is still sitting there.""",
   "Volkswagen Transporter pickup", "25% TARIFF, STILL IN 2026")
sc("""Think about how unusual that is. A trade dispute about poultry, between governments in the nineteen sixties, created a permanent rule for American pickup trucks. Most people who buy a truck today have never heard of it. Yet it quietly affects which brands sell trucks here, where they are built, and how much they cost.""",
   "pickup trucks import port", "A POULTRY FIGHT, A PERMANENT RULE")
sc("""Here is where it gets strange. In the nineteen seventies, small Japanese pickups became popular in America. To avoid the twenty-five percent tax, some companies shipped them without the bed, as a cab and chassis, which faced a lower rate. The beds were added after the trucks arrived. Chevrolet sold a small truck called the LUV, built by Isuzu. Ford sold the Courier, built by Mazda.""",
   "Chevrolet LUV pickup", "THE CAB-CHASSIS LOOPHOLE")
sc("""And then came the craziest twist of all. Subaru sold a small car-based pickup called the BRAT. To avoid being classified as a light truck, it came with two plastic seats bolted into the open bed, facing backwards. With seats, the BRAT counted as a passenger vehicle, not a truck. Two seats in the back turned a pickup into a car, at least for the tax man.""",
   "Subaru BRAT", "SUBARU BRAT: SEATS IN THE BED")
sc("""The loophole did not last forever. Rules were tightened, and over time Japanese companies began building pickups in North America instead. Today, Toyota builds its Tacoma and Tundra in North American plants, and Nissan builds the Frontier in the United States. In a way, the chicken tax pushed foreign truck makers to build factories in America.""",
   "Toyota Tundra factory", "THE TAX BROUGHT FACTORIES")
sc("""Why does a sixty-year-old chicken fight matter to you? Because the chicken tax is one of the reasons the American pickup market is dominated by trucks built in North America. For decades, importing a pickup from Europe or Asia meant paying an extra twenty-five percent. That protected Detroit's most profitable vehicles, and it shaped which trucks Americans could buy.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "WHY DETROIT OWNS THE TRUCK MARKET")
sc("""And here is the last twist. Many popular trucks from other countries, like the Toyota Hilux, have never been sold new in America. And even if you try to import an old one under the twenty-five year rule, The Daily Vroom points out that the age exemption and the tariff are completely separate things. In its example, a nineteen ninety-four Hilux faced a three thousand nine hundred dollar tariff line, inside about eight thousand dollars in import fees.""",
   "Toyota Hilux", "HILUX IMPORT: $3,900 TARIFF LINE")
sc("""So when people ask why small, cheap pickups disappeared from America, the chicken tax is part of the answer. And in twenty twenty-five and twenty twenty-six, new tariffs on imported vehicles and parts added another layer on top of it. The chicken war of nineteen sixty-four is still deciding what is parked in American driveways today.""",
   "pickup trucks dealer lot", "A CHICKEN WAR STILL DECIDES")

# ---------- 4. 1994 DODGE RAM ----------
sc("""Number four is the truck that changed how pickups look. The nineteen ninety-four Dodge Ram. Before it, most American pickups had flat, boxy faces. Dodge, a distant third in truck sales, took a huge risk. The new Ram had a tall hood and a big, crosshair grille that made it look like a small semi truck.""",
   "Dodge Ram 1994 pickup", "4. THE 1994 DODGE RAM")
sc("""The design divided people. Some thought it was too much. But it gave Dodge something it had not had in years: attention. The Ram became a hit, and the big-rig look spread across the industry. Look at almost any full-size pickup sold today, with its tall hood and massive grille, and you are looking at the influence of the nineteen ninety-four Ram.""",
   "Dodge Ram 1500 1990s", "THE BIG-RIG LOOK SPREAD")
sc("""Here is the twist. That design change came with a side effect that people are still debating. As pickups got taller and their front ends got bigger, critics, including safety researchers, raised concerns about visibility in front of the truck and about the risk to pedestrians. The look that sold millions of trucks also started a safety debate that continues in twenty twenty-six.""",
   "Ram 1500 front grille", "TWIST: THE SAFETY DEBATE")
sc("""There is a lesson here about risk. Dodge was in third place, so it had less to lose. Ford and Chevy were protecting huge sales, so they changed carefully. The company with the least to lose took the biggest swing, and it worked. In the truck business, the underdog often has the freedom to try what the leader cannot.""",
   "Dodge Ram pickup classic", "THE UNDERDOG TOOK THE SWING")
sc("""The Ram also launched an identity. In twenty ten, Chrysler made Ram its own brand, separate from Dodge. And in twenty nineteen, according to The Drive, Ram sold six hundred thirty-three thousand, six hundred ninety-four pickups and outsold the Chevrolet Silverado for the first time in history. The bet on a bold face in nineteen ninety-four eventually helped turn a third-place truck into a brand of its own.""",
   "Ram 1500 2019", "2019: RAM BEATS SILVERADO")
sc("""And the Ram story still shapes buyers' choices in twenty twenty-six. After dropping its Hemi V eight for one model year, Ram brought it back in June twenty twenty-five. According to Carscoops, the brand received over ten thousand orders in the first twenty-four hours. Ram's chief executive, Tim Kuniskis, admitted the company screwed up when it dropped the Hemi. The brand built on bold choices learned what happens when it takes one away.""",
   "Ram 1500 Hemi", "HEMI BACK: 10,000 ORDERS IN 24H")

# ---------- 5. FORD MAVERICK ----------
sc("""Number five is the newest truck on the list, and the one that may change the most. The Ford Maverick. Ford launched it for the twenty twenty-two model year as a small, car-based pickup, with a hybrid engine as standard, and a starting price under twenty thousand dollars before destination. At a time when pickups were getting bigger and more expensive every year, Ford went the other way.""",
   "Ford Maverick hybrid", "5. FORD MAVERICK")
sc("""Buyers rushed in. According to Ford, the Maverick sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, up eighteen point two percent, with a record thirty-four thousand one hundred forty-seven in the fourth quarter alone. The Maverick hybrid by itself sold eighty-one thousand and thirty-four. A small, efficient pickup turned out to be exactly what a huge number of Americans wanted.""",
   "Ford Maverick pickup blue", "2025: 155,051 MAVERICKS")
sc("""And here is who was buying. Many Maverick buyers were not traditional truck owners. They were people coming from small cars and crossovers who wanted a bed for weekend projects without the size and price of a full-size truck. Just like the Model T pickup and the Ranchero, the Maverick reached people the truck market had forgotten.""",
   "Ford Maverick Lariat", "NEW BUYERS, NOT TRUCK OWNERS")
sc("""There is another twist in how Ford designed it. The Maverick was built on a platform shared with Ford crossovers, which kept costs down. It has a four and a half foot bed, smaller than a full-size truck, but Ford designed it with slots and tie-downs so owners could build their own storage. It was a pickup made for people who like to customize, at a price that left money for the projects.""",
   "Ford Maverick bed", "BUILT TO BE CUSTOMIZED")
sc("""Now the twist. The cheap truck did not stay cheap. According to The Truth About Cars in August twenty twenty-six, the current Maverick starts at about thirty thousand dollars. That is a long way from the under twenty thousand dollar launch price. Tariffs, inflation and added features all pushed it up. The truck that was supposed to bring back affordable pickups has become a thirty thousand dollar vehicle.""",
   "Ford Maverick Tremor", "TWIST: $20K TRUCK NOW ~$30K")
sc("""But Ford is betting harder on the hybrid. According to Ford Authority, for the twenty twenty-seven model year, the base Maverick X L becomes hybrid only, and the turbo engine is dropped from the X L and Lariat trims. Some upper trims got big price cuts. The Lobo, for example, starts at thirty-two thousand one hundred fifty-five dollars, down three thousand seven hundred seventy-five from twenty twenty-six.""",
   "Ford Maverick Lobo", "2027: XL GOES HYBRID-ONLY")
sc("""The hybrid matters for running costs, too. A buyer who drives mostly in town sees the biggest benefit, because hybrids recover energy when braking. For many Maverick owners, fuel costs are far lower than with a full-size truck. That is the kind of saving that does not show up on the window sticker, but shows up every week at the gas station.""",
   "Ford Maverick hybrid fuel", "THE SAVING YOU SEE WEEKLY")
sc("""So what did the Maverick change? It proved, with real sales, that the small, affordable pickup still has a huge market in America. Other companies are now chasing that idea, including startups promising simple, low-cost trucks. The Maverick reopened a door that the industry had closed for decades.""",
   "Ford Maverick pickup", "IT REOPENED A DOOR")

# ---------- HONORABLE MENTION ----------
sc("""Before we wrap up, an honorable mention that changed the conversation, even if it did not change the market the way it promised. The Tesla Cybertruck. When it was revealed in twenty nineteen, it looked like nothing else on the road, with flat stainless steel panels and a shape like a wedge. It made more people talk about pickups than any truck in years.""",
   "Tesla Cybertruck", "MENTION: TESLA CYBERTRUCK")
sc("""But talk did not turn into the sales that many expected. Its sales fell in twenty twenty-five, as InsideEVs reported. The twist is that the Cybertruck still changed something: it showed that a pickup could be a cultural object, debated online, photographed everywhere, and talked about by people who would never buy one. Whether that is a success depends on who you ask.""",
   "Tesla Cybertruck stainless steel", "TALK VS SALES")

# ---------- PATTERN ----------
sc("""And there are more trucks that could have made this list. The first Chevrolet and Ford trucks after World War Two, which turned pickups into everyday vehicles. The first crew cabs, which made the pickup a family car. The first factory diesel pickups, which changed towing. But the five we picked each changed not just trucks, but who buys them and why.""",
   "Chevrolet pickup 1950s Ford F-1", "THE ONES THAT ALMOST MADE IT")
sc("""So what do these five have in common? Each one changed who a pickup was for. The Model T pickup made trucks affordable for working families. The Ranchero made them a lifestyle choice. The chicken tax decided who could sell them. The Ram changed how they look, and the Maverick brought back the small, efficient truck.""",
   "pickup trucks history", "EACH ONE CHANGED WHO TRUCKS ARE FOR")
sc("""And here is the final twist. The biggest changes in pickup history did not come from making trucks bigger or more powerful. They came from reaching people who were not being served. The cheapest truck in nineteen twenty-five. The car-like truck in nineteen fifty-seven. The small hybrid truck in twenty twenty-two. The next truck to change America will probably do the same.""",
   "Ford Maverick Ford Model T", "THE NEXT ONE WILL DO THE SAME")

# ---------- CLOSE ----------
sc("""So what does this mean if you are buying a truck in twenty twenty-seven? First, buy for your real needs. Many people who buy a full-size truck rarely tow or haul heavy loads. If that is you, a smaller truck like the Maverick may save you thousands, just like it did for the buyers who made it a hit.""",
   "Ford Maverick Ford F-150", "CHECK 1: YOUR REAL NEEDS")
sc("""Second, check where the truck is built, because tariffs, including the old chicken tax and the new ones, affect prices. Third, compare trims carefully, because price cuts on some trims and increases on others, like the twenty twenty-seven Maverick changes, can flip which version is the best deal. Fourth, look at the powertrain trend. Hybrids are growing, and that can help resale value.""",
   "pickup truck window sticker", "CHECKS 2, 3 AND 4")
sc("""And fifth, count the full cost: fuel, insurance, maintenance and value after five years. A truck is a big purchase, and the cheapest sticker is not always the cheapest truck to own.""",
   "pickup truck dealership", "CHECK 5: THE FULL COST")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the numbers to compare and the questions to ask every dealer. The link is in the description and in the pinned comment. Subscribe for the next video, about trucks that were complete flops, and why. Thanks for watching.""",
   "Ford Ranchero Chevrolet El Camino", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"A pickup that cost": "Intro", "Number one": "1. 1925 Ford Model T pickup", "Number two": "2. Ford Ranchero and Chevy El Camino",
      "Number three": "3. The Chicken Tax", "Number four": "4. 1994 Dodge Ram", "Number five": "5. Ford Maverick",
      "Before we wrap up": "Honorable mention: Tesla Cybertruck", "So what does this mean": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video44", "length_scale": 1.45,
  "title": "5 Pickups That Changed America (One Started With a War Over Chicken)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
