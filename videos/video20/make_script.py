import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""The twenty twenty-seven Chevrolet Colorado has an engine that changed, and Chevrolet has not said how. The order guide shows a new engine code. The power figures have not been updated. The price of the twenty twenty-six model went up in the last weeks of its production, and the new model year started production on October nineteenth. So what do we really know about the new Colorado? Less than you would think, and more than the headlines say.""",
   "Chevrolet Colorado ZR2 pickup", "2027 COLORADO: WHAT CHANGED?")
sc("""The Chevrolet Colorado is the second best selling midsize truck in America, behind the Toyota Tacoma. It has a small engine with big numbers, a crew cab only lineup, and a loyal group of off-road buyers. This year it is selling a little less than last year, and the new model year brings quiet changes. In this video we go through each change, and we also separate what is confirmed from what is still a question.""",
   "Chevrolet Colorado Trail Boss pickup", "SECOND-BEST MIDSIZE SELLER")
sc("""Our sources. Pickup Truck Talk, from August fourth, which read the twenty twenty-seven order guide published by GM-Trucks dot com. GM Authority, from October sixteenth, for the price increases. And the sales table we have used all week, from Pickup Truck Talk, for the numbers. Chevrolet has not published an official price list for twenty twenty-seven in these sources.""",
   "Chevrolet Colorado Z71 pickup", "SOURCES: PTT ORDER GUIDE, GM AUTHORITY")
sc("""Four twists. An engine that changed with no explanation. A price increase at the very end of a model year. A list of colors where three leave and three arrive, with strange restrictions. And a connectivity change that matters more than it looks. Let us begin with the engine.""",
   "Chevrolet Colorado pickup truck", "FOUR TWISTS")

# ENGINE
sc("""Part one, the engine. The Colorado uses a two point seven liter TurboMax turbocharged four cylinder with an eight speed automatic. The power is three hundred ten horsepower and four hundred thirty pound-feet of torque. For twenty twenty-seven, the engine is listed as unchanged, according to Pickup Truck Talk. But there is one thing in the order guide.""",
   "Chevrolet Colorado TurboMax engine", "2.7L TURBO: 310 HP, 430 LB-FT")
sc("""The regular production option code changes from L three B to L four B. In plain language, General Motors has given the engine a new code. The article says it does not know what changed inside. It writes that the order guide confirms something changed, and that now we need Chevrolet to explain exactly what it was. And it says Chevrolet has not announced revised output figures.""",
   "Chevrolet Colorado engine bay", "ENGINE CODE: L3B BECOMES L4B")
sc("""Why does a code change matter? Because manufacturers do not usually change an engine code without a reason. It could be an emissions update, a supplier change, a durability fix, or a tuning adjustment. We do not know which. And we will not guess. What we know is that the published horsepower, torque, payload, weight and dimensions did not change. So for a buyer, the honest answer is, wait for Chevrolet's explanation before you assume anything.""",
   "Chevrolet Colorado ZR2 off road", "WE DO NOT KNOW WHAT CHANGED")

# SPECS
sc("""Towing and payload are the same as before. The Colorado can tow up to seven thousand, seven hundred pounds when properly configured. Payload is up to about seventeen hundred pounds on a properly configured four wheel drive truck. The fuel tank holds twenty-one point four gallons. And the ZR2 has ten point seven inches of ground clearance. These come from Pickup Truck Talk and refer to the maximum, not to every trim.""",
   "Chevrolet Colorado towing trailer", "TOW 7,700 LB. PAYLOAD ABOUT 1,700 LB.")
sc("""The lineup is also unchanged. Five trims, all crew cab, all with the short bed. The Work Truck and the LT come in rear wheel drive. The Trail Boss, the Z71 and the ZR2 come in four wheel drive. There is no extended cab and no long bed. That is a difference from the Tacoma, the Ranger and the Frontier, which offer more body choices. Chevrolet chose to simplify, and the order guide confirms it stays that way.""",
   "Chevrolet Colorado crew cab", "5 TRIMS. ALL CREW CAB. ALL SHORT BED.")

# PRICE
sc("""Part two, the price. GM Authority reported on October sixteenth that three twenty twenty-six trims went up in October. The Trail Boss rose one hundred dollars, to forty-two thousand, five hundred ninety-five. The Z71 rose two hundred, to forty-six thousand, six hundred ninety-five. And the ZR2 rose two hundred dollars, to fifty-two thousand, seven hundred ninety-five. Those prices include a destination charge of two thousand, ninety-five dollars.""",
   "Chevrolet Colorado ZR2 price", "OCT 2026: TRAIL BOSS +$100, Z71 +$200, ZR2 +$200")
sc("""The unchanged trims are the Work Truck, which starts at thirty-four thousand, four hundred ninety-five dollars in two wheel drive and thirty-seven thousand, seven hundred ninety-five in four wheel drive, and the LT, at thirty-eight thousand, ninety-five and forty-one thousand, three hundred ninety-five. The ZR2 Bison is listed at sixty-four thousand, four hundred ninety-five. The article says the increases came as the twenty twenty-six model neared the end of its run, with the last twenty twenty-six trucks built on October sixteenth.""",
   "Chevrolet Colorado Work Truck", "WT FROM $34,495. ZR2 BISON $64,495.")
sc("""The twist is the timing. The increases are small, and the article gives no official reason. We should not invent one. But they happened while the model was ending, and the twenty twenty-seven truck, which starts production on October nineteenth, has no published price yet. So the best advice is to treat these prices as the floor. And to treat any twenty twenty-seven price as unknown until Chevrolet publishes it.""",
   "Chevrolet Colorado dealership", "2027 PRICE: NOT PUBLISHED")

# COLORS
sc("""Part three, the colors, which sound small, but have strange rules. Three colors leave. Snowdrift Metallic, Reef Blue Metallic and Sunrise Orange. Three arrive. Serpent Metallic, Storm Gray Metallic and Nitron Blue. Still available are White Sands, Summit White, Black, Radiant Red Tintcoat and Sterling Gray Metallic. If you liked the orange, this is the last chance on a new truck.""",
   "Chevrolet Colorado orange pickup", "OUT: ORANGE. IN: NITRON BLUE.")
sc("""And now the restrictions, which are the twist. Storm Gray Metallic and Nitron Blue cannot be paired with the ZR2's Jet Black or Artemis interior. Serpent Metallic cannot be ordered with the Z71's Adrenaline Red interior. So a buyer cannot simply choose any color and any interior. The configurator will block some combinations. If you have a favorite, check it before you commit to an order.""",
   "Chevrolet Colorado ZR2 interior", "SOME COLOR-INTERIOR COMBOS BLOCKED")
sc("""The wheels change too. The LT trim gets new seventeen inch wheels, and there is an available eighteen inch Gloss Black machined face wheel. The old seventeen inch Argent Metallic wheel option is dropped. Small things, yes, but they are the kind of changes that matter to people who are choosing between a Colorado and a Canyon at the dealership.""",
   "Chevrolet Colorado wheels", "NEW 17-INCH LT WHEEL, 18-INCH BLACK")

# TECH
sc("""Part four, technology, and the quiet change is connectivity. A five G Wi-Fi hotspot replaces the previous four G LTE system. For a work truck, or for someone who camps and works from the bed of a truck, that is a real upgrade. Remember, though, that the hotspot normally needs a data plan, and the sources we used do not say what it costs.""",
   "Chevrolet Colorado camping", "5G HOTSPOT REPLACES 4G LTE")
sc("""Convenience Package Three is optional on the Z71 and available on the ZR2. Depending on the configuration, it includes ventilated front seats, driver seat memory, a heated steering wheel, wireless phone charging and extra interior storage. There is also a Universal Home Remote, which operates compatible garage doors and gates. And a new Jet Black interior, with Artemis cloth and Evotex upholstery, is offered on the ZR2.""",
   "Chevrolet Colorado cabin", "NEW: VENTED SEATS, HOME REMOTE")

# SALES
sc("""Now the numbers that tell you where the Colorado stands. Through nine months of twenty twenty-six, it sold seventy-two thousand, eight hundred sixty-three trucks, down five point eight percent. In the third quarter, it fell about three percent. That makes it the second best selling midsize truck. But the Tacoma sells far more, and the Frontier is growing fast. So the Colorado is a solid truck that is slowly losing ground.""",
   "Chevrolet Colorado pickup", "2026 YTD: 72,863, DOWN 5.8%")
sc("""And remember, the Colorado and the GMC Canyon are the same truck with different badges. The Canyon is growing while the Colorado slips, so part of the Colorado's decline may be buyers moving to the sibling. Adding the Silverado, the Sierra, the Colorado, the Canyon and the electric trucks, General Motors sold about seven hundred eighty-seven thousand trucks through nine months, down one point eight percent.""",
   "GMC Canyon pickup", "GM TRUCKS: ABOUT 787,000. DOWN 1.8%")

sc("""Let us look at the price ladder, because it shows how the lineup is built. The Work Truck starts at thirty-four thousand, four hundred ninety-five dollars in two wheel drive. The LT in two wheel drive is thirty-eight thousand, ninety-five. The Trail Boss is forty-two thousand, five hundred ninety-five, the Z71 is forty-six thousand, six hundred ninety-five, and the ZR2 is fifty-two thousand, seven hundred ninety-five. And the ZR2 Bison is sixty-four thousand, four hundred ninety-five. From bottom to top, that is a difference of thirty thousand dollars.""",
   "Chevrolet Colorado ZR2 Bison", "FROM $34,495 TO $64,495")
sc("""Notice what you get for the extra money. From the Work Truck to the LT, about three thousand six hundred dollars buys a more comfortable cabin. From the LT four wheel drive to the Trail Boss, the price rises about one thousand two hundred dollars, and the truck gains an off-road character. These are our own calculations from the listed prices, not Chevrolet's. The point is that the Colorado has a clear ladder, and most buyers will find a step that fits.""",
   "Chevrolet Colorado LT pickup", "OUR MATH FROM THE LISTED PRICES")
sc("""The destination charge deserves a word. All the prices we quoted include a destination charge of two thousand, ninety-five dollars. That means the truck's own price is lower than it looks, and the number on the window sticker is higher than an advertisement that leaves it out. When you compare quotes from different dealers, always ask for the out-the-door price, which includes taxes and fees. It is the only number that lets you compare two offers honestly.""",
   "Chevrolet Colorado window sticker", "ASK FOR THE OUT-THE-DOOR PRICE")
sc("""Think also about the engine question in practical terms. A new engine code could mean nothing for the owner, or it could mean a small change in emissions or durability. While we wait for Chevrolet, the safest move for a buyer who wants an early build is to ask the dealer for written confirmation of the warranty, and to read the coverage terms. The GM powertrain warranty details are not in the sources we used, so check them on the manufacturer's site.""",
   "Chevrolet Colorado engine warranty", "ASK FOR THE WARRANTY IN WRITING")
sc("""And remember the buying calendar. The last twenty twenty-six trucks were built on October sixteenth, and the twenty twenty-seven trucks begin on October nineteenth. That means the first weeks of the new model year will have very few trucks on dealer lots, and orders will take time. A buyer in a hurry should look at a leftover twenty twenty-six, and a buyer who wants the new truck should place an order and be patient.""",
   "Chevrolet Colorado factory", "2026 ENDS OCT 16. 2027 STARTS OCT 19.")
sc("""Last, think about how you will use the truck. The Colorado is crew cab only, with a short bed, and it tows up to seven thousand, seven hundred pounds. If you need a long bed, an extended cab, or a diesel, look at other trucks. If you want a strong turbo engine and a good off-road package in a single body style, the Colorado makes it simple. The lack of choice is a feature for buyers who dislike spending hours on a configurator.""",
   "Chevrolet Colorado Z71 trail", "ONE BODY STYLE. FEWER CHOICES.")

# BUYERS
sc("""So who should buy a Colorado? Someone who wants a midsize truck with strong power, a high tow rating and a good off-road package. The Trail Boss and the ZR2 are the favorites. And who should wait? Anyone who needs to know what the new engine code means, and anyone who wants a published price. Chevrolet opened the order books for the twenty twenty-seven Colorado, but the sources give no on-sale date.""",
   "Chevrolet Colorado Trail Boss", "BUY: OFF-ROAD, POWER. WAIT: PRICE, ENGINE.")
sc("""If you are comparing, remember what we saw in the sales numbers. The Tacoma sells far more than the Colorado, and the Frontier is growing fast. And the Canyon is the same truck as the Colorado with a different look. So the choice is partly about the dealer and the deal, not only the truck. Get quotes on both the Colorado and the Canyon, and compare the same trim, with the same options, on the same day.""",
   "Toyota Tacoma and Chevrolet Colorado", "COMPARE COLORADO, CANYON, TACOMA, FRONTIER")
# NEWSCENES
sc("""Let us explain the engine code change in terms of what a buyer can do. You cannot read the inside of an engine, but you can read paperwork. Ask the dealer for the build date of the exact truck and ask which engine code appears on its order. Compare it with the code on a twenty twenty-six truck. If the code is different, you at least know you are looking at the changed version. That does not tell you what changed, but it tells you which truck you are buying.""",
   "Chevrolet Colorado engine", "CHECK THE CODE ON THE ORDER")
sc("""Now compare two prices that we already stated. The Trail Boss is forty-two thousand, five hundred ninety-five dollars, and the Z71 is forty-six thousand, six hundred ninety-five. The ZR2 is fifty-two thousand, seven hundred ninety-five. Each step brings more off-road equipment, but each step also costs a few thousand dollars. Ask yourself how often you will actually leave the pavement. If the answer is rarely, a lower trim may serve you for less money.""",
   "Chevrolet Colorado Trail Boss pickup", "HOW OFTEN DO YOU LEAVE THE PAVEMENT?")
sc("""A common mistake is to buy the top trim for a feature you will not use. The ZR2 has ten point seven inches of ground clearance, which matters on rough trails and matters little on a commute. The Bison, at sixty-four thousand, four hundred ninety-five dollars, is built for serious off-road use. If your driving is mostly highway and town, paying for that capability is like buying a boat for a pond. Be honest about your weekends.""",
   "Chevrolet Colorado ZR2 Bison", "DO NOT PAY FOR TRAILS YOU WILL NOT DRIVE")
sc("""How should you read the towing figure? Seven thousand, seven hundred pounds is the maximum when the truck is properly configured. That means the right trim, the right drive and the right equipment. A Colorado you find on a lot may tow less. So before you buy for a specific trailer, find the number on the door sticker of that exact truck. Then compare it with the weight of your trailer, with the load already inside it. Leave a margin.""",
   "Chevrolet Colorado towing", "MAXIMUM TOW IS NOT EVERY TRUCK")
sc("""Payload is the number people forget. Up to about seventeen hundred pounds sounds like a lot, until you add passengers, a toolbox, a tonneau cover and a tongue weight from a trailer. Payload is what the truck can carry in the cab and in the bed together. If you use the truck for work, add up what you carry on an ordinary day. And again, read the sticker of the truck you are buying, not the maximum in a brochure.""",
   "Chevrolet Colorado bed cargo", "PAYLOAD COUNTS PEOPLE TOO")
sc("""Let us talk about the Canyon, since it is the same truck with a different badge. The Canyon is growing while the Colorado slips. That tells us the two trucks compete with each other for the same buyer. For you, that is useful. Ask both dealers for a quote on the same trim, with the same options, on the same day. Because the trucks match, any difference in price is a difference in the deal, and not in the truck.""",
   "GMC Canyon pickup", "SAME TRUCK, TWO DEALS: GET BOTH QUOTES")
sc("""Think about the five G hotspot honestly. It sounds like a large upgrade, and for some people it is. But it normally needs a data plan, and the sources do not say what that costs. If you already have a phone plan with hotspot data, you may not need it. If you work remotely from the truck, it might be worth paying for. Either way, ask the dealer how long any trial lasts, and write down the answer.""",
   "Chevrolet Colorado hotspot", "DO YOU NEED A SECOND DATA PLAN?")
sc("""One more caution about colors and interiors. If you want Storm Gray Metallic, Nitron Blue or Serpent Metallic, the restrictions we described can block some pairings. A salesperson may promise a combination that the order system will not accept. Before you put down a deposit, ask to see the configuration confirmed on the order screen. A deposit is easier to give than to get back, so settle the color first.""",
   "Chevrolet Colorado new colors", "CONFIRM THE COMBINATION BEFORE A DEPOSIT")
sc("""And a last view of the whole picture. The Colorado is a strong, simple lineup with real choices on price and off-road equipment, and with two open questions. What did the engine change, and what will the twenty twenty-seven price be? If those questions matter to you, wait. If they do not, you can still make a smart purchase by comparing out-the-door prices, checking the sticker and getting the warranty terms in writing. Prepared buyers rarely overpay.""",
   "Chevrolet Colorado ZR2 pickup", "TWO OPEN QUESTIONS, THEN DECIDE")

sc("""Let us go through a sample plan for a careful buyer. Step one, decide whether you need the off-road trims or whether a Work Truck or LT will do. Step two, ask two dealers for the out-the-door price on the same trim, one for the Colorado and one for the Canyon. Step three, ask for the warranty terms in writing. Step four, read the door sticker for towing and payload. Step five, confirm the color and interior on the order screen. Five steps, and none of them cost anything.""",
   "Chevrolet Colorado pickup", "A FIVE-STEP PLAN FOR BUYERS")
sc("""Finally, a word about patience. The first weeks of a new model year are when information is thinnest. Prices may not be published, the engine change may be unexplained, and trucks are scarce. A buyer who waits a little gets more facts, and a buyer who cannot wait gets a leftover twenty twenty-six truck, which we know a little better. Either choice is sensible. What is not sensible is paying for a new truck while guessing about what changed inside it.""",
   "Chevrolet Colorado Z71 pickup", "PATIENCE BEATS GUESSING")
sc("""And if you remember only one idea from this video, let it be this one. Every number we quoted is a starting point, not an answer. Prices are before taxes and fees. Towing is a maximum. Payload depends on the sticker. The engine code is a question. When you walk into a dealership, bring these questions with you, and the answers will tell you far more than any advertisement. Good buyers ask, and then they check.""",
   "Chevrolet Colorado Trail Boss pickup", "EVERY NUMBER IS A STARTING POINT")

sc("""So what should you check before you buy a twenty twenty-seven Colorado? First, the official price. Second, the explanation for the engine code change. Third, whether your color and interior can be combined. And fourth, the exact towing and payload on the door sticker of the truck you are buying. The Twenty Twenty-Seven Truck Buyer's Guide has this checklist. The link is in the description and in the pinned comment.""",
   "Chevrolet Colorado pickup", "CHECK 1, 2, 3 AND 4")
sc("""If you want to see the Toyota Tacoma against the Colorado, subscribe, because that comparison is coming. Thanks for watching.""",
   "Toyota Tacoma pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The twenty twenty-seven Chevrolet Colorado has": "Intro", "Part one": "1. The mystery engine code",
      "Towing and payload": "Towing, payload, lineup", "Part two": "2. The price", "Part three": "3. Colors and wheels",
      "Part four": "4. Technology", "Now the numbers": "Sales", "So who should": "Who should buy it",
      "So what should you check": "What to check before you buy"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video20", "length_scale": 1.55,
  "title": "2027 Chevy Colorado: The Engine Changed and Chevrolet Won't Say How", "scenes": S}, open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
