import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The ten best-selling pickup trucks in America sold more than two million, one hundred eighty-seven thousand units in nine months. One of them is up forty percent. One is down thirteen percent in its heavy-duty version. And number two is closing in on number one faster than anyone expected. This is the real ranking of the best-selling trucks of twenty twenty-six, and what the ranking hides.""",
   "Ford F-150 pickup truck", "TOP 10 TRUCKS OF 2026")

# ---------- COLD OPEN ----------
sc("""Every year, the same question gets asked. Which truck is really number one? And every year, the answer is the same, with one small change. But this year, the change is bigger than usual. We took the nine-month sales table that Pickup Truck Talk published for twenty twenty-six, covering January through September, and ranked the ten best-selling trucks. Then we looked for the twist in each one.""",
   "Chevrolet Silverado 1500 pickup", "JAN-SEP 2026 SALES TABLE")
sc("""Before the countdown, one number sets the scale. The ten trucks on this list add up to two million, one hundred eighty-seven thousand, seven hundred fifty. The top three alone, the Ford F-Series, the Chevrolet Silverado and the Ram, are fifty-nine percent of that. So the market is concentrated at the top. But the ranking is not frozen, and the changes happen in the middle. Every number comes from a published source, listed in the description.""",
   "Ram 1500 pickup truck", "TOP 3 = 59% OF THE TOP 10")
sc("""A note on method. We count each model line as one truck, including its light-duty and heavy-duty versions. The Ford F-Series is shown without the electric Lightning, as the table does, and where Ford's own number differs, we say so. We rank by sales through September, not by the last quarter. And we leave out the electric trucks and the medium-duty trucks, which sell in much smaller numbers and have their own videos. Let's start at the bottom.""",
   "Ford F-250 Super Duty pickup", "METHOD: JAN-SEP 2026, U.S. SALES")

# ---------- 10. FORD RANGER ----------
sc("""Number ten is the Ford Ranger. Through nine months of twenty twenty-six, Ford sold fifty-one thousand, six hundred thirty Rangers, up six point nine percent from forty-eight thousand, two hundred seventy-eight a year earlier. It is the smallest number on the list. But look at the quarters. Sales fell nearly ten percent in the second quarter, to sixteen thousand, two hundred ninety-four, and then jumped almost fifteen percent in the third, to seventeen thousand, five hundred sixty-one.""",
   "Ford Ranger pickup", "10. RANGER: 51,630")
sc("""That is the twist. The truck at the bottom of the ranking is a truck with a roller coaster year. It is up for nine months, down in one quarter, and up in the next. If you only read one quarter, you would draw the wrong conclusion twice. The Ranger tells you why a nine-month table is more honest than a headline about one quarter, and why a small number is not the same as a weak truck.""",
   "Ford Ranger Raptor pickup", "Q2 -9.8%. Q3 +14.8%.")

# ---------- 9. NISSAN FRONTIER ----------
sc("""Number nine is the Nissan Frontier, and it is the fastest-growing truck on the list. Nissan sold sixty-six thousand, five hundred thirteen Frontiers through nine months, up thirty-nine point six percent from forty-seven thousand, six hundred thirty. In the third quarter, it sold twenty-three thousand, four hundred twelve, up thirty-seven and a half percent. No other truck in this ranking comes close to that rate of growth.""",
   "Nissan Frontier pickup", "9. FRONTIER: 66,513 (+39.6%)")
sc("""The twist is who this truck belongs to. Nissan is the same company that ended its full-size Titan after the twenty twenty-four model year, and the Titan sold just thirteen trucks in the same nine months. The company lost a full-size truck and gained a midsize one. The Fast Lane Truck credited the Frontier's naturally aspirated V six engine, and said buyers seem to be listening. A simple engine, in a simple truck, is selling.""",
   "Nissan Frontier Pro-4X pickup", "TITAN: 13 TRUCKS. FRONTIER: UP 40%.")

# ---------- 8. CHEVROLET COLORADO ----------
sc("""Number eight is the Chevrolet Colorado. Through nine months, Chevrolet sold seventy-two thousand, eight hundred sixty-three, down five point eight percent from seventy-seven thousand, three hundred ninety. It is the only midsize truck from a Detroit company in the top ten besides the Ranger, and it is the second best seller in its segment, behind the Tacoma by a wide margin.""",
   "Chevrolet Colorado ZR2 pickup", "8. COLORADO: 72,863 (-5.8%)")
sc("""Here is the twist. In the third quarter, the Colorado sold twenty-five thousand, one hundred seventy, up two point four percent. So the truck that lost ground for the year was growing again in the latest quarter. And its twin, the GMC Canyon, rose twenty percent for the nine months, to thirty-three thousand, five hundred forty-five. Same truck, same factory, opposite directions. The Colorado is a reminder that two badges can tell two different stories.""",
   "GMC Canyon pickup", "Q3: COLORADO +2.4%")

# ---------- 7. TOYOTA TUNDRA ----------
sc("""Number seven is the Toyota Tundra. Toyota sold one hundred ten thousand and eighty Tundras through nine months, down eight tenths of a percent from one hundred ten thousand, nine hundred forty-five. It is the only full-size truck from a Japanese company still being built, and it is the smallest of the five full-size trucks in this ranking. But the number is very stable, quarter after quarter.""",
   "Toyota Tundra pickup", "7. TUNDRA: 110,080 (-0.8%)")
sc("""The twist is who beats it. The Tundra is Toyota's full-size flagship, and it sold fewer trucks than the Toyota Tacoma, the midsize one, by a margin of almost two to one. And the Ford Maverick, a compact truck, outsold it too, with one hundred twenty-three thousand, six hundred eighty-one. A full-size truck can be a very good truck and still not be the best-seller of its own family.""",
   "Toyota Tacoma pickup", "TUNDRA: BEATEN BY ITS OWN TACOMA")

# ---------- 6. FORD MAVERICK ----------
sc("""Number six is the Ford Maverick, the compact pickup that now outsells every midsize truck except the Tacoma. Ford sold one hundred twenty-three thousand, six hundred eighty-one Mavericks through nine months, up two point three percent. In the third quarter alone it sold forty-one thousand, nine hundred seventy, up twenty point four percent. And the Maverick Hybrid was seventy-four thousand, three hundred of those trucks, a record for the model.""",
   "Ford Maverick pickup", "6. MAVERICK: 123,681")
sc("""The twist is the hybrid. About sixty percent of every Maverick sold through the third quarter was a hybrid, and in the third quarter alone, about two thirds. The smallest truck from Ford is selling the most advanced powertrain. And it outsold the entire Hyundai Santa Cruz many times over. The Santa Cruz sold fourteen thousand, eight hundred eleven in the same period. A small truck can win, when it is the right small truck.""",
   "Ford Maverick Hybrid pickup", "MAVERICK HYBRID: 74,300")

# ---------- 5. TOYOTA TACOMA ----------
sc("""Number five is the Toyota Tacoma, the best-selling midsize truck in America by a very large margin. Toyota sold two hundred fourteen thousand, eight hundred seventy-five Tacomas through nine months, up five point one percent from two hundred four thousand, four hundred sixty-four. The next midsize truck, the Chevrolet Colorado, sold seventy-two thousand, eight hundred sixty-three. The Tacoma sold almost three times as many.""",
   "Toyota Tacoma pickup", "5. TACOMA: 214,875 (+5.1%)")
sc("""And here is the twist. The Tacoma is number five on this list, right behind four full-size trucks, and it is the only truck in the top five that is not full-size. The Tacoma grew nearly sixteen percent in the first half, to one hundred forty-three thousand, eight hundred forty-eight, and then slipped three and a half percent in the third quarter, to seventy-one thousand and twenty-seven.""",
   "Toyota Tacoma TRD pickup", "H1 +15.8%. Q3 -3.5%.")

# ---------- 4. GMC SIERRA ----------
sc("""Number four is the GMC Sierra. Through nine months, GMC sold two hundred fifty-two thousand, six hundred thirty-nine Sierras, up three tenths of a percent from two hundred fifty-one thousand, eight hundred forty-five. Almost perfectly flat. In the third quarter, it sold eighty-four thousand, nine hundred twenty-nine, down six tenths of a percent. If you want a truck with a steady, predictable record, this is it.""",
   "GMC Sierra pickup truck", "4. SIERRA: 252,639 (+0.3%)")
sc("""The twist is hidden inside the number. The light-duty Sierra rose four point four percent, to one hundred seventy-four thousand, three hundred ninety-three. The heavy-duty Sierra fell seven point seven percent, to seventy-eight thousand, two hundred forty-six. A flat total hides a split. The everyday truck is growing, and the work truck is shrinking. That is a pattern we will see again, in the next two trucks.""",
   "GMC Sierra HD pickup", "LD +4.4%. HD -7.7%.")

# ---------- 3. RAM ----------
sc("""Number three is the Ram, and it is the biggest story of the year. Ram sold three hundred twenty-five thousand, three hundred forty-eight pickups through nine months, up twenty-four percent from two hundred sixty-two thousand, three hundred eighty-six. That is an extra sixty-two thousand, nine hundred sixty-two trucks. In the third quarter alone, Ram sold one hundred seventeen thousand, seven hundred fifty-seven, up thirty-three point seven percent.""",
   "Ram 1500 pickup truck", "3. RAM: 325,348 (+24%)")
sc("""Look inside the number for the twist. The light-duty Ram sold two hundred two thousand, one hundred forty-seven, up forty-one percent. In the third quarter, the light-duty Ram jumped seventy-three percent, from forty-four thousand, three hundred forty-nine to seventy-six thousand, six hundred fifty. The heavy-duty Ram, meanwhile, rose only three point four percent. The growth is in the everyday truck. And it happened in a year in which Ram canceled its electric truck.""",
   "Ram 1500 Rebel pickup", "RAM LD: +41%")

# ---------- 2. SILVERADO ----------
sc("""Number two is the Chevrolet Silverado. Chevrolet sold four hundred thirteen thousand, three hundred eighty-three Silverados through nine months, down seven tenths of a percent from four hundred sixteen thousand, two hundred ninety. In the third quarter, it sold one hundred forty-four thousand, four hundred ninety-nine, up four point nine percent.""",
   "Chevrolet Silverado 1500 pickup", "2. SILVERADO: 413,383 (-0.7%)")
sc("""And now the twist. The light-duty Silverado grew six point five percent, to two hundred seventy-nine thousand, six hundred fourteen. The heavy-duty Silverado fell thirteen percent, from one hundred fifty-three thousand, seven hundred fifty to one hundred thirty-three thousand, seven hundred sixty-nine. The same split as the Sierra, only bigger. And the gap between the Silverado and the Ram, which was one hundred fifty-three thousand, nine hundred four trucks a year ago, is now eighty-eight thousand and thirty-five.""",
   "Chevrolet Silverado HD pickup", "GAP TO RAM: 153,904 TO 88,035")

# ---------- 1. FORD F-SERIES ----------
sc("""Number one, as always, is the Ford F-Series. Without the Lightning, Ford sold five hundred fifty-six thousand, seven hundred thirty-eight through nine months, down six point eight percent from five hundred ninety-seven thousand, five hundred forty-six. Ford's own release, which includes the Lightning, shows five hundred sixty-one thousand, five hundred eight. Either way, it is about a quarter of everything on this list, and ten times the Ranger.""",
   "Ford F-150 XLT pickup", "1. F-SERIES: 556,738 (-6.8%)")
sc("""Here is the twist. The F-Series lost forty thousand, eight hundred eight trucks in a year. That is a very large number. And it is still number one by one hundred forty-three thousand trucks over the Silverado. In the third quarter, it recovered, selling two hundred three thousand, four hundred eighteen, up two point nine percent, and in September, Ford sold sixty-seven thousand, four hundred forty-eight, up two point four percent. The king is wounded, but it is still the king.""",
   "Ford F-150 pickup truck", "Q3: +2.9%. SEPT: 67,448.")


# ---------- RANK CHANGES ----------
sc("""Now let's look at the same list a year ago, because the ranking tells another story when you compare. In the first nine months of twenty twenty-five, the order of the top seven was exactly the same. Ford, Chevrolet, Ram, GMC, Toyota Tacoma, Ford Maverick and Toyota Tundra. The top of the table did not change places. The only changes happened in the numbers, and at the very bottom.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "TOP 7: SAME ORDER AS 2025")
sc("""At the bottom, there is a swap. A year ago, the Ford Ranger sold forty-eight thousand, two hundred seventy-eight, and the Nissan Frontier sold forty-seven thousand, six hundred thirty. The Ranger was ahead. This year the Frontier sold sixty-six thousand, five hundred thirteen, and the Ranger fifty-one thousand, six hundred thirty. The Frontier overtook the Ranger, with a lead of almost fifteen thousand trucks. That is the only rank change in the entire list.""",
   "Nissan Frontier Ford Ranger pickups", "FRONTIER PASSES RANGER")
sc("""And there is a third change that the ranking cannot show, because the order stayed the same. The gap between the Ram and the GMC Sierra. A year ago, the Ram sold two hundred sixty-two thousand, three hundred eighty-six, and the Sierra two hundred fifty-one thousand, eight hundred forty-five, a gap of ten thousand, five hundred forty-one trucks. This year the gap is seventy-two thousand, seven hundred nine. Same positions, very different distance.""",
   "Ram 1500 GMC Sierra pickups", "RAM VS SIERRA: GAP 10,541 TO 72,709")
sc("""That is the lesson of any ranking. A list tells you who is ahead, but not how fast they are moving, and not how far apart they are. Two trucks can hold the same position for years while one of them is quietly pulling away. When you read a ranking of the best-selling trucks, look for the gaps, because the gaps are where the news is.""",
   "Ford F-150 Chevrolet Silverado pickups", "READ THE GAPS, NOT THE RANKS")
sc("""So how should a buyer use a ranking like this? Not as a shopping list. Use it as a check. If a truck is in the top five, it means service, parts and resale demand are likely to be easy to find, because a lot of trucks are on the road. If a truck is falling in the ranking, ask why, and ask the dealer whether the model is going to be updated. And if a truck is rising fast, check whether the price is rising with it.""",
   "Toyota Tacoma pickup truck", "HOW TO USE A RANKING")
sc("""There is a simple way to do that. Take the truck you like, and look up three numbers. The sales for the first nine months of this year, the sales for the same months last year, and the change in the latest quarter. If all three point the same way, you have a clear signal. If they point in different directions, like the Ranger, you have a truck in motion, and you should ask more questions before you sign.""",
   "Ford Ranger pickup truck", "THREE NUMBERS TO CHECK")

# ---------- WHAT THE RANKING HIDES ----------
sc("""So what does the ranking hide? Three things. First, it hides the split between light-duty and heavy-duty. Both Chevrolet and GMC grew the everyday truck and lost the work truck, and Ram did the opposite in volume, growing the everyday truck fast and the work truck slowly. Second, it hides the quarters. Nine months tell the direction, and the third quarter shows the turn. And third, it hides the small numbers.""",
   "Ford F-250 Chevrolet Silverado HD Ram 2500 pickups", "WHAT THE RANKING HIDES")
sc("""Because just below this list are trucks that matter. The Honda Ridgeline sold thirty-seven thousand and twenty-eight, down one percent. The Jeep Gladiator sold thirty thousand, nine hundred forty-four, down nearly twenty percent. And the Hyundai Santa Cruz sold fourteen thousand, eight hundred eleven, down twenty-eight percent. These are not in the top ten, but their numbers show where the market is going cold.""",
   "Honda Ridgeline pickup", "BELOW THE LIST: RIDGELINE, GLADIATOR")
sc("""There is one more twist, and it is about the price. According to Kelley Blue Book, the average full-size pickup sold for sixty-seven thousand, four hundred forty-six dollars in August, up two point one percent. So the trucks on this ranking are selling in huge numbers, at prices that are higher than ever. The pickup is not a cheap product in twenty twenty-six. It is a very expensive product that Americans keep buying.""",
   "Ford F-150 Lariat pickup", "AVERAGE FULL-SIZE PRICE: $67,446")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a truck in twenty twenty-seven? First, look at the sales of the exact version, not the model. A heavy-duty truck and a light-duty truck from the same brand can move in opposite directions. Second, look at the latest quarter, not only the year. And third, remember that the best-selling truck is not automatically the best truck for you. Popularity helps resale and service. It does not choose your trailer.""",
   "Ford F-150 pickup", "CHECK 1, 2 AND 3")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which trucks are the most reliable, according to the data, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The ten best-selling pickup": "Intro", "Number ten": "10. Ford Ranger", "Number nine": "9. Nissan Frontier",
      "Number eight": "8. Chevrolet Colorado", "Number seven": "7. Toyota Tundra", "Number six": "6. Ford Maverick",
      "Number five": "5. Toyota Tacoma", "Number four": "4. GMC Sierra", "Number three": "3. Ram",
      "Number two": "2. Chevrolet Silverado", "Number one": "1. Ford F-Series", "So what does the ranking hide": "What the ranking hides",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video07", "length_scale": 1.85,
  "title": "The 10 Best-Selling Trucks of 2026 (And What the Ranking Hides)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
