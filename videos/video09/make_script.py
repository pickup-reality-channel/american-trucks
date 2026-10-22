import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""You can still buy a new pickup truck for less than thirty thousand dollars in America. But there is a catch, and it is the reason most buyers never find that price. One of these trucks is being phased out, according to reports. One has the best resale value of any truck we checked. And one of the cheapest trucks in America might not be built yet. Here are the cheapest new trucks, and which one is worth buying.""",
   "Ford Maverick pickup truck", "THE CHEAPEST NEW TRUCKS")

# ---------- COLD OPEN ----------
sc("""The average new full-size pickup sold for sixty-seven thousand, four hundred forty-six dollars in August, according to Kelley Blue Book. That is more than the cheapest truck on this list costs twice over. So if you are looking for a first truck, a work truck, or just a truck that does not eat your budget, the real market is somewhere else. It is in the small trucks and the midsize trucks, with starting prices between about twenty-five and thirty-five thousand dollars.""",
   "Ford F-150 pickup truck", "FULL-SIZE AVERAGE: $67,446")
sc("""For the prices, we used the Autoblog list of the ten cheapest trucks, published in June of twenty twenty-six. We cross-checked it with SlashGear, from May. Where the two disagree, we say so. For the sales, we used the nine-month table from Pickup Truck Talk. For resale value, we used iSeeCars. A starting price is the price of the cheapest trim, and it usually does not include the destination fee. Every source is listed in the description.""",
   "Ford Ranger pickup", "SOURCES: AUTOBLOG, SLASHGEAR, ISEECARS")
sc("""So here are seven trucks that are, or soon might be, under thirty-five thousand dollars. And in each of them, there is a twist. One is the cheapest and the best seller, at once. One is called the last of its kind. One is cheaper than all of them, and has no screen. And one is the best truck to resell, but not the cheapest to buy. Stay with me, because the last twist changes the math.""",
   "Toyota Tacoma pickup", "SEVEN TRUCKS. SEVEN TWISTS.")

# ---------- 1. SLATE ----------
sc("""Number one is the truck that does not exist yet, the Slate. On June twenty-fourth, twenty twenty-six, Slate Auto announced a starting price of twenty-four thousand, nine hundred fifty dollars, and opened preorders the same day. That is the lowest price on this list, and it is lower than the Ford Maverick by three thousand, one hundred ninety-five dollars. The price does not include taxes, registration, or destination fees.""",
   "Slate Auto electric truck", "SLATE: FROM $24,950")
sc("""And here is the twist. It is an electric truck, and Slate originally pitched it at under twenty thousand dollars. But that assumed the seven thousand, five hundred dollar federal tax credit, which no longer exists. According to Electrek, it has a sixty-five kilowatt-hour battery, one hundred eighty-one horsepower, and an estimated range of two hundred five miles. It has no infotainment screen. First deliveries are expected by the end of twenty twenty-six. It is a promise, not a truck you can drive today.""",
   "Slate Auto truck", "NO SCREEN. 205 MILES. NOT DELIVERED YET.")

# ---------- 2. FORD MAVERICK ----------
sc("""Number two is the Ford Maverick, and it is the cheapest truck you can actually buy. Autoblog lists it at twenty-eight thousand, one hundred forty-five dollars, with a two point five liter hybrid engine and one hundred ninety-one horsepower. Autoblog lists forty-two miles per gallon in the city. SlashGear lists it at twenty-seven thousand, two hundred twenty-nine dollars, so the sources differ by about nine hundred dollars.""",
   "Ford Maverick pickup", "MAVERICK: FROM $28,145")
sc("""The twist is that the cheapest truck is also a very popular one. Ford sold one hundred twenty-three thousand, six hundred eighty-one Mavericks through nine months of twenty twenty-six, and seventy-four thousand, three hundred of them were hybrids. That is more than any midsize truck except the Tacoma. After five years, iSeeCars shows it keeps sixty-eight point two percent of its value. A cheap truck that holds value is rare.""",
   "Ford Maverick Hybrid pickup", "MAVERICK: 123,681 SOLD, 68.2% RESALE")

# ---------- 3. HYUNDAI SANTA CRUZ ----------
sc("""Number three is the Hyundai Santa Cruz, and the price is attractive. Autoblog lists the SE at twenty-nine thousand, seven hundred fifty dollars, with a one hundred ninety-one horsepower four-cylinder, and up to five thousand pounds of towing with the turbo engine. It has a lockable trunk in the bed. But Autoblog also notes that twenty twenty-six will be the last model year.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: FROM $29,750")
sc("""That fits with the sales. The Santa Cruz sold fourteen thousand, eight hundred eleven trucks through nine months, down twenty-eight percent. Automotive News and The Autopian reported through unnamed sources that it is being phased out, and Hyundai declined to confirm. So here is the twist. It is the second cheapest truck on the list, and the one most likely to be discontinued. A truck with no future can be a bargain, if you plan to keep it, and a trap, if you plan to sell it.""",
   "Hyundai Santa Cruz pickup truck", "LAST MODEL YEAR: 2026")
sc("""But it is not a disaster for resale. iSeeCars shows the Santa Cruz keeping sixty-five point one percent of its value after five years, only about three points below the Maverick. So the market has not punished it yet. That could change. A warranty normally stays valid on a discontinued model, but parts and service attention can fade over time. If you buy one, get the warranty terms in writing.""",
   "Hyundai Santa Cruz", "SANTA CRUZ RESALE: 65.1%")

# ---------- 4. TOYOTA TACOMA ----------
sc("""Number four is the Toyota Tacoma, and it is the one that costs more than it looks. Autoblog lists the SR XtraCab at thirty-two thousand, one hundred forty-five dollars, with a two point four liter turbo four-cylinder and up to six thousand, five hundred pounds of towing. SlashGear lists thirty-two thousand, four hundred forty-five. Either way, it is the cheapest midsize truck from Toyota, and the best-selling truck on this list.""",
   "Toyota Tacoma SR pickup", "TACOMA: FROM $32,145")
sc("""Here is the twist. TFL Car measured the landed cost of the popular SR5 trim, which includes the destination fee. In twenty twenty-six, it was thirty-nine thousand, four hundred fifty dollars, up only seven tenths of a percent from twenty twenty-four. That is seven thousand, three hundred five dollars above the starting price of the cheapest version. The headline price and the price most buyers pay are not the same number.""",
   "Toyota Tacoma SR5 pickup", "SR5 LANDED COST: $39,450")
sc("""But there is a reason many buyers pay it. The Tacoma sold two hundred fourteen thousand, eight hundred seventy-five through nine months, almost three times its closest midsize rival. And iSeeCars shows it keeping eighty and a half percent of its value after five years, which is the best resale of any truck on the list. A Tacoma that costs more to buy is also a Tacoma that returns more when you sell.""",
   "Toyota Tacoma TRD pickup", "TACOMA RESALE: 80.5%")

# ---------- 5. CHEVROLET COLORADO ----------
sc("""Number five is the Chevrolet Colorado. Autoblog lists the work truck trim at thirty-two thousand, four hundred dollars, with a two point seven liter turbo four-cylinder making two hundred thirty-seven horsepower. SlashGear lists the same price, and says the Colorado can tow up to seven thousand, seven hundred pounds with its three hundred ten horsepower engine. That is more towing than the Tacoma, at almost the same price.""",
   "Chevrolet Colorado WT pickup", "COLORADO: FROM $32,400")
sc("""The twist is the split inside General Motors. The Colorado sold seventy-two thousand, eight hundred sixty-three trucks through nine months, down five point eight percent. But its twin, the GMC Canyon, rose twenty percent, even though Autoblog lists the Canyon at thirty-eight thousand, nine hundred dollars, more than six thousand dollars above the Colorado. In the third quarter, the Colorado grew two point four percent. So the cheaper twin is the one losing buyers, for the year.""",
   "GMC Canyon pickup", "CANYON: $38,900, UP 20%")

# ---------- 6. FORD RANGER ----------
sc("""Number six is the Ford Ranger. Autoblog lists the XL at thirty-three thousand, three hundred fifty dollars, with a two point three liter turbocharged EcoBoost engine making two hundred seventy horsepower, and a ten-speed automatic. Ford sold fifty-one thousand, six hundred thirty Rangers through nine months, up six point nine percent. And iSeeCars shows it keeping sixty-eight point eight percent of its value, second only to the Tacoma among the midsize trucks.""",
   "Ford Ranger XL pickup", "RANGER: FROM $33,350")
sc("""The twist is the roller coaster. The Ranger fell nearly ten percent in the second quarter, then rose almost fifteen percent in the third. And it sits between two very different Ford trucks, the Maverick below it and the F-one-fifty above it. The Ranger is cheaper than the F-one-fifty XL regular cab at thirty-seven thousand, two hundred ninety dollars, by three thousand, nine hundred forty. For some buyers, that gap decides everything.""",
   "Ford Ranger pickup truck", "RANGER VS F-150: $3,940 GAP")

# ---------- 7. NISSAN FRONTIER ----------
sc("""Number seven is the Nissan Frontier, and here the two sources we used look like they disagree, but they are really talking about two different trucks. SlashGear lists thirty-two thousand, one hundred fifty dollars, and Autoblog's list shows thirty-five thousand, one hundred fifty. According to Autoblog's later report on the twenty twenty-seven Frontier, the first is the King Cab with two-wheel drive, and the second is the same King Cab with four-wheel drive.""",
   "Nissan Frontier pickup", "FRONTIER: $32,150 (4X2). $35,150 (4X4).")
sc("""For twenty twenty-seven, Nissan prices the cheapest Frontier, the S King Cab two-wheel drive, at thirty-two thousand, four hundred ninety dollars, up three hundred forty dollars. It has a three point eight liter V six, three hundred ten horsepower, and tows up to seven thousand, one hundred fifty pounds. The Frontier sold sixty-six thousand, five hundred thirteen trucks through nine months, up nearly forty percent. That is the fastest growth on this list.""",
   "Nissan Frontier Pro-4X pickup", "2027 FRONTIER: FROM $32,490")
sc("""But here is the twist. iSeeCars shows the Frontier keeping sixty-three point four percent of its value after five years, the lowest of the five midsize trucks on the list. A truck that is popular and cheap is not always a truck that keeps its price. And a two-wheel drive King Cab is a very basic truck. The price you see is for the version with the fewest options.""",
   "Nissan Frontier S King Cab pickup", "FRONTIER: FAST SALES, LOWEST RESALE")

# ---------- THE FIVE-YEAR COST ----------
sc("""Now let's do the math that most buyers skip, and it will change the ranking. We take each starting price from Autoblog, and apply the iSeeCars five-year resale value. This is an estimate, using the cheapest trim, and not a quote. But it shows what each truck costs you in lost value after five years. Start with the Ford Maverick. At twenty-eight thousand, one hundred forty-five dollars, and sixty-eight point two percent resale, it would be worth about nineteen thousand, one hundred ninety-five dollars. A loss of eight thousand, nine hundred fifty.""",
   "Ford Maverick pickup", "MAVERICK: LOSES ~$8,950")
sc("""The Hyundai Santa Cruz, at twenty-nine thousand, seven hundred fifty and sixty-five point one percent, would be worth about nineteen thousand, three hundred sixty-seven. A loss of ten thousand, three hundred eighty-three. The Ford Ranger, at thirty-three thousand, three hundred fifty and sixty-eight point eight percent, would be worth about twenty-two thousand, nine hundred forty-five. A loss of ten thousand, four hundred five. And the Nissan Frontier, at thirty-two thousand, one hundred fifty and sixty-three point four percent, would be worth about twenty thousand, three hundred eighty-three. A loss of eleven thousand, seven hundred sixty-seven.""",
   "Nissan Frontier pickup", "FRONTIER: LOSES ~$11,767")
sc("""And now the twist that changes the ranking. The Toyota Tacoma, at thirty-two thousand, one hundred forty-five dollars and eighty and a half percent resale, would be worth about twenty-five thousand, eight hundred seventy-seven. A loss of only six thousand, two hundred sixty-eight dollars. The truck that costs the most to buy, among these, is the one that loses the least. Over five years, the Tacoma costs about two thousand, seven hundred dollars less in lost value than the Maverick, even though it costs four thousand dollars more upfront.""",
   "Toyota Tacoma pickup truck", "TACOMA: LOSES ONLY ~$6,268")
sc("""Let's be careful with that. It is a simple estimate. It ignores fuel, insurance, repairs, financing, and the fact that the Maverick Hybrid uses much less fuel, with forty-two miles per gallon in the city according to Autoblog. Those costs can easily outweigh a difference of two thousand dollars. So the Tacoma is not automatically the winner. But it shows that the cheapest sticker and the cheapest truck to own are two different things.""",
   "Ford Maverick Hybrid pickup", "STICKER PRICE VS REAL COST")
sc("""Think about what that means when you shop. A salesperson will often talk about the monthly payment. A smart buyer thinks about the difference between what they pay at the start, and what they can sell the truck for at the end. That difference is the real cost of the truck, before fuel and repairs. A truck that costs six thousand dollars to own over five years in lost value is a better deal than one that costs thirteen thousand, even if its sticker is higher.""",
   "Toyota Tacoma TRD Off-Road pickup", "THE REAL COST: START MINUS END")
sc("""One last point about buying the cheapest truck. The cheapest trim is usually a work truck, with a basic interior and few options. That is fine for many buyers, and it is the reason the price is low. But if you plan to add options later, the price will rise quickly, as the Tacoma's landed price of thirty-nine thousand, four hundred fifty dollars shows. So decide which options you need before you shop, and compare trucks with the same options, not the same badge.""",
   "Chevrolet Colorado pickup", "COMPARE THE SAME OPTIONS")

# ---------- THE VERDICT ----------
sc("""So which one is worth buying? It depends on what you value. For the lowest price you can actually buy, it is the Maverick. For the best resale and the best sales record, it is the Tacoma, at a higher price. For the most towing for the money, it is the Colorado. For a simple V six, it is the Frontier. And for something that is not here yet, it is the Slate. There is no single winner, only a trade between price today and value later.""",
   "Ford Maverick Toyota Tacoma pickups", "NO SINGLE WINNER")
sc("""Let's use one more number to explain the trade. The gap between the Maverick at twenty-eight thousand, one hundred forty-five and the Frontier two-wheel drive at thirty-two thousand, one hundred fifty is four thousand, five dollars. And the gap in five-year resale is about five points, sixty-eight point two against sixty-three point four. On a thirty-thousand-dollar truck, five points is fifteen hundred dollars. So the cheaper truck is also the one that keeps more.""",
   "Ford Maverick pickup truck", "CHEAPER AND KEEPS MORE VALUE")
sc("""That is the final twist. In the truck market, the cheap truck and the smart truck are not always the same. But in this list, the cheapest truck you can buy today is also one of the better ones at keeping its value. That is unusual, and it is part of the reason the Maverick has become so popular, with its hybrid selling in the tens of thousands. A low price can be a strength, if the truck holds up.""",
   "Ford Maverick Lariat pickup", "CHEAP AND SMART, FOR ONCE")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a cheap truck in twenty twenty-seven? First, ask for the full price, with the destination fee and every other charge, because the starting price is only the first number. Second, check whether the model is still being built, like the Santa Cruz. Third, compare the resale value, because a cheaper truck that loses more may cost more over five years. And fourth, match the truck to your real needs, like towing and bed size.""",
   "Ford F-150 pickup", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"You can still buy a new pickup": "Intro", "Number one": "1. Slate", "Number two": "2. Ford Maverick",
      "Number three": "3. Hyundai Santa Cruz", "Number four": "4. Toyota Tacoma", "Number five": "5. Chevrolet Colorado",
      "Number six": "6. Ford Ranger", "Number seven": "7. Nissan Frontier", "So which one is worth buying": "The verdict",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video09", "length_scale": 1.88,
  "title": "7 Cheapest New Trucks You Can Buy in 2027 (Which One Is Worth It)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
