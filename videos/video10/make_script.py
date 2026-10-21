import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Thirteen thousand, five hundred pounds. That is the number Ford puts on the F-one-fifty, and it is true. But a Chevrolet Silverado without one option package tows about nine thousand pounds, four thousand less than its own maximum. The towing number on the brochure is a best-case number, and a very specific one. Here is what the max towing numbers really mean, truck by truck.""",
   "Ford F-150 towing trailer", "THE MAX TOWING NUMBER IS A BEST CASE")

# ---------- COLD OPEN ----------
sc("""Towing is the reason many people buy a truck. It is also the number that is the easiest to misread, because every company advertises its maximum, and the maximum depends on a very particular truck. The right engine, the right cab, the right axle, the right package. Change one thing, and the number drops. Sometimes by a few hundred pounds, and sometimes by thousands.""",
   "Chevrolet Silverado towing trailer", "MAX TOW = ONE VERY SPECIFIC TRUCK")
sc("""We used the Autoblog comparison of the twenty twenty-six Ram one thousand five hundred, Ford F-one-fifty and Chevrolet Silverado one thousand five hundred, the GM Authority report on the twenty twenty-seven Silverado, and the Autoblog and SlashGear lists of the cheapest trucks for the smaller ones. Every source is listed in the description. And where two sources disagree, we say so.""",
   "Ram 1500 pickup", "SOURCES: AUTOBLOG, GM AUTHORITY, SLASHGEAR")
sc("""There is a twist in every truck on this list. One truck has a diesel and still tows less than a gas rival. One truck loses more than three thousand pounds by changing the engine. One gets its high number only with the two-wheel drive version. And one small truck has two different ratings in two different reviews. Stay with me, because the last twist is about what you should check before you buy.""",
   "Ford F-250 Super Duty pickup", "FIVE TWISTS ON TOWING")

# ---------- 1. FORD F-150 ----------
sc("""Number one is the Ford F-one-fifty. According to Autoblog, the twenty twenty-six F-one-fifty can tow up to thirteen thousand, five hundred pounds. But to get that number, you need the three point five liter EcoBoost V six, the Tow Haul package, the Max Tow axle, a SuperCrew cab with a six and a half foot box, and four-wheel drive. Payload for that configuration is two thousand, four hundred forty pounds.""",
   "Ford F-150 pickup towing", "F-150: 13,500 LB, ONE CONFIGURATION")
sc("""Now the twist. Change the engine, and the number changes a lot. The five point oh liter V eight is rated at twelve thousand, nine hundred pounds. And the PowerBoost hybrid, the one that is selling in the tens of thousands, is rated at eleven thousand, two hundred. That is two thousand, three hundred pounds less than the maximum. So the best-selling hybrid full-size truck in America tows about seventeen percent less than the top version.""",
   "Ford F-150 PowerBoost hybrid pickup", "F-150 HYBRID: 11,200 LB")
sc("""And Autoblog adds a warning that applies to every truck here. A four-wheel drive F-one-fifty without the Max Tow axle drops below thirteen thousand, five hundred. The maximum is a best case. Passengers and cargo in the bed also reduce the usable towing and payload. So if you tow a heavy trailer with a family in the truck and gear in the bed, the number on the brochure is not the number you can use.""",
   "Ford F-150 Lariat pickup", "4X4 AND CARGO REDUCE THE NUMBER")

# ---------- 2. CHEVROLET SILVERADO ----------
sc("""Number two is the Chevrolet Silverado one thousand five hundred. The twenty twenty-six model is rated at thirteen thousand, three hundred pounds, according to Autoblog, and the configuration is the surprise. It is the three point oh liter Duramax turbo diesel, with the Max Trailering package, a Double Cab with the standard bed, and two-wheel drive. Payload for that truck is two thousand, two hundred sixty pounds. Notice that this diesel truck tows two hundred pounds less than the gas-powered Ford.""",
   "Chevrolet Silverado 1500 Duramax diesel", "SILVERADO: 13,300 LB, 2WD DIESEL")
sc("""The twist here is the package. Autoblog says that without the Max Trailering package, most Silverado configurations tow about nine thousand to nine thousand, seven hundred pounds. That is about three and a half to four and a half thousand pounds less than the maximum. The same truck, on the same lot, can have a difference of four thousand pounds, depending on one option box. If you do not check that box, you do not get that number.""",
   "Chevrolet Silverado 1500 pickup", "WITHOUT THE PACKAGE: ~9,000 LB")
sc("""And for twenty twenty-seven, the number goes up. GM Authority reported in September that the twenty twenty-seven Silverado one thousand five hundred is rated at thirteen thousand, seven hundred pounds, which it calls the segment towing champion. That is with the five point seven liter V eight, a Double Cab with two-wheel drive, and the Max Trailering package, and with a payload of two thousand, one hundred seventy pounds. The configuration is different from last year's, so the payload cannot be compared directly.""",
   "Chevrolet Silverado 1500 LT pickup", "2027 SILVERADO: 13,700 LB")

# ---------- 3. RAM 1500 ----------
sc("""Number three is the Ram one thousand five hundred. Autoblog lists the twenty twenty-six Ram at eleven thousand, six hundred ten pounds, with the three point oh liter Hurricane twin-turbo inline six, and rear-wheel drive. The payload is two thousand, three hundred sixty pounds. That is about two thousand pounds below the Ford and about seventeen hundred below the Chevrolet.""",
   "Ram 1500 Hurricane pickup", "RAM 1500: 11,610 LB")
sc("""The twist is the engines. The five point seven liter Hemi is rated at eleven thousand, three hundred twenty pounds, only a few hundred pounds below the Hurricane. But the three point six liter Pentastar V six drops to eight thousand, one hundred thirty. That is three thousand, four hundred eighty pounds less than the best Ram. A buyer who picks the base engine to save money might be buying a truck that tows what a midsize truck tows.""",
   "Ram 1500 Big Horn pickup", "PENTASTAR V6: 8,130 LB")

# ---------- 4. THE MIDSIZE TRUCKS ----------
sc("""Number four is the midsize trucks, and the numbers are much lower. Autoblog lists the Toyota Tacoma at up to six thousand, five hundred pounds with the i-Force engine. SlashGear lists the Chevrolet Colorado at up to seven thousand, seven hundred pounds with its three hundred ten horsepower engine. And SlashGear lists the Nissan Frontier at up to seven thousand, one hundred fifty pounds.""",
   "Toyota Tacoma towing trailer", "TACOMA 6,500. COLORADO 7,700. FRONTIER 7,150.")
sc("""Here is the twist. The Colorado, the cheapest of the three on the sticker at thirty-two thousand, four hundred dollars, tows the most. And the Tacoma, the best seller, with two hundred fourteen thousand, eight hundred seventy-five sold through nine months, tows the least of the three. That is a good reminder. The most popular truck is not the one with the best numbers, and the numbers are not why buyers pick it.""",
   "Chevrolet Colorado pickup", "COLORADO TOWS 1,200 LB MORE THAN TACOMA")

# ---------- 5. COMPACT TRUCKS ----------
sc("""Number five is the compact trucks, and here the sources disagree. Autoblog lists the Hyundai Santa Cruz at five thousand pounds with the turbo engine. SlashGear lists it at up to three thousand, five hundred pounds. That is a gap of fifteen hundred pounds between two reputable outlets, and it is probably the difference between the base engine and the turbo. We cannot tell from the articles, so we will not guess.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: 3,500 OR 5,000 LB?")
sc("""And the Ford Maverick has its own surprise. Autoblog lists a payload of fifteen hundred pounds. SlashGear lists a maximum hauling capacity of two thousand pounds, with the same payload of fifteen hundred. So the little hybrid truck, the cheapest you can actually buy, can carry fifteen hundred pounds in the bed. That is more than some buyers expect from a truck that starts at twenty-eight thousand, one hundred forty-five dollars.""",
   "Ford Maverick pickup", "MAVERICK: 1,500 LB PAYLOAD")

# ---------- THE CONCLUSION ----------
sc("""So what do we learn? First, the maximum is a very specific truck. For the Ford, it is the V six, the Max Tow axle, the four-door cab and the four-wheel drive. For the Chevrolet, it is the diesel, the package, the standard bed and two-wheel drive. For the Ram, it is the Hurricane with rear-wheel drive. These are not the trucks that most buyers take home, and the difference can be thousands of pounds.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "THE MAX IS A SPECIFIC TRUCK")
sc("""Second, payload and towing compete. Autoblog says that passengers and cargo reduce the usable towing and payload. So a truck that can tow thirteen thousand pounds on paper, with two people and no gear, may tow less in real life with a family and a full bed. The two numbers share the same truck. The more you put in the bed and the cabin, the less you can pull behind it.""",
   "Chevrolet Silverado pickup towing", "PAYLOAD AND TOWING SHARE THE TRUCK")
sc("""Third, the engine you choose matters more than the badge. Across the three big half-ton trucks, the gap between the best and the weakest engine we have numbers for is two thousand, three hundred pounds for the Ford, and three thousand, four hundred eighty for the Ram. That is a bigger gap than the one between the three brands. When you compare trucks for towing, compare engines, not brands.""",
   "Ram 1500 pickup", "ENGINE GAP > BRAND GAP")


# ---------- THE NUMBERS SIDE BY SIDE ----------
sc("""Let's put the numbers side by side, so you can see the whole picture. The best Ford, thirteen thousand, five hundred. The best Chevrolet, thirteen thousand, three hundred. The best Ram, eleven thousand, six hundred ten. Then the middle of the range. The Ford V eight, twelve thousand, nine hundred, and the Ram Hemi, eleven thousand, three hundred twenty. And then the low end. The Ford hybrid, eleven thousand, two hundred, the Silverado without the package, about nine thousand, and the Ram Pentastar, eight thousand, one hundred thirty.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "FROM 13,500 DOWN TO 8,130 LB")
sc("""Look at the spread. The highest number in that list is thirteen thousand, five hundred, and the lowest is eight thousand, one hundred thirty. That is a gap of five thousand, three hundred seventy pounds, and all of those trucks are called half-ton pickups, from the three biggest brands. If a friend says a half-ton truck can tow thirteen thousand pounds, the honest answer is that some of them can, and some of them cannot.""",
   "Ram 1500 Big Horn pickup", "SAME CLASS, 5,370 LB APART")
sc("""Now compare the full-size trucks with the midsize ones. The Colorado at seven thousand, seven hundred pounds is about five thousand, eight hundred pounds below the best Ford. The Tacoma, at six thousand, five hundred, is seven thousand pounds below. But the Colorado is within about five hundred pounds of the Ram with the Pentastar engine, at eight thousand, one hundred thirty. A basic full-size truck and a strong midsize truck are closer than their sizes suggest.""",
   "Chevrolet Colorado ZR2 pickup", "COLORADO 7,700 VS RAM V6 8,130")
sc("""This is useful for a buyer who is choosing between a base full-size truck and a midsize truck with a stronger engine. The base full-size truck may have a bigger bed, and a bigger cabin. But if the goal is only towing, the midsize truck might do the same work, for a lower price. The Colorado starts at thirty-two thousand, four hundred dollars, and the Silverado at thirty-six thousand, nine hundred, according to Autoblog. That is a difference of four thousand, five hundred dollars.""",
   "Chevrolet Silverado Work Truck", "COLORADO $32,400. SILVERADO $36,900.")
sc("""And here is the opposite case. A buyer who tows a heavy trailer, close to ten thousand pounds, should not buy a base half-ton and hope. They should look at the engine and the package, because that is where the numbers change. The Silverado, for example, goes from about nine thousand to thirteen thousand, three hundred with the package and the diesel. Spending more on the right configuration can be the cheapest way to stay inside the limit.""",
   "Chevrolet Silverado 1500 Duramax pickup", "THE RIGHT CONFIGURATION")

# ---------- THE REAL-WORLD CHECKLIST ----------
sc("""Here is how to use these numbers in practice. Autoblog's advice is simple, and it is worth repeating. Check the door sticker on your specific truck, and know your trailer's weight. Do not use the brochure number for your truck, use the sticker for your truck. And do not use the trailer's advertised weight, use what it weighs when it is loaded. These three checks take ten minutes, and they prevent the most common mistake.""",
   "Ford F-150 pickup", "CHECK THE DOOR STICKER")
sc("""Then think about the margin. A trailer that is close to the limit of a truck is hard on the truck, on the brakes, and on the driver. Buying a truck with some extra capacity is cheaper than replacing a transmission, and much cheaper than an accident. We cannot give you a safe percentage, because the sources we used do not, and it depends on the trailer, the road and the driver. But we can say this. Never buy a truck for a number that you will use at its limit, every weekend.""",
   "Chevrolet Silverado 1500 pickup", "KEEP A MARGIN")
sc("""One more point, because it connects with the price. The Silverado's Max Trailering package is an option, and the truck without it tows about four thousand pounds less. That option costs money, and the sources we used do not list its price. So ask the dealer. A buyer who needs to tow nine thousand pounds, and buys the version that tows nine thousand, has no margin. A buyer who spends more on the package may have much more.""",
   "Chevrolet Silverado LT pickup", "THE PACKAGE IS AN OPTION")
sc("""Finally, remember the new trucks. The Ram one thousand five hundred REV, the range-extended truck coming in twenty twenty-seven, has no published towing capacity yet, according to TruckDaily. The Lightning will return as an extended-range truck, but Ford has not announced when it will go on sale. And the Slate truck has no towing figure in the sources we found. If towing is your reason for buying, do not buy a truck that has no number yet.""",
   "Ram 1500 pickup truck", "NEW TRUCKS: NO TOWING NUMBERS YET")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a truck for towing in twenty twenty-seven? First, the engine, cab, drive and package, not only the model. Second, the door sticker of the exact truck you are buying. Third, the loaded weight of your trailer. And fourth, the payload, because the tongue of the trailer and the people in the truck count against it. If one of those four is wrong, the brochure number does not apply to you.""",
   "Ford F-150 pickup", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Thirteen thousand, five hundred pounds": "Intro", "Number one": "1. Ford F-150", "Number two": "2. Chevrolet Silverado 1500",
      "Number three": "3. Ram 1500", "Number four": "4. Midsize trucks", "Number five": "5. Compact trucks",
      "So what do we learn": "What the numbers mean", "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video10", "length_scale": 2.0,
  "title": "The Truth About Max Towing Numbers (What the Brochure Does Not Say)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
