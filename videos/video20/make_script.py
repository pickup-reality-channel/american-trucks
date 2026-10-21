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

# BUYERS
sc("""So who should buy a Colorado? Someone who wants a midsize truck with strong power, a high tow rating and a good off-road package. The Trail Boss and the ZR2 are the favorites. And who should wait? Anyone who needs to know what the new engine code means, and anyone who wants a published price. Chevrolet opened the order books for the twenty twenty-seven Colorado, but the sources give no on-sale date.""",
   "Chevrolet Colorado Trail Boss", "BUY: OFF-ROAD, POWER. WAIT: PRICE, ENGINE.")
sc("""If you are comparing, remember what we saw in the sales numbers. The Tacoma sells far more than the Colorado, and the Frontier is growing fast. And the Canyon is the same truck as the Colorado with a different look. So the choice is partly about the dealer and the deal, not only the truck. Get quotes on both the Colorado and the Canyon, and compare the same trim, with the same options, on the same day.""",
   "Toyota Tacoma and Chevrolet Colorado", "COMPARE COLORADO, CANYON, TACOMA, FRONTIER")
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
json.dump({"id": "video20", "length_scale": 2.0,
  "title": "2027 Chevy Colorado: The Engine Changed and Chevrolet Won't Say How", "scenes": S}, open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
