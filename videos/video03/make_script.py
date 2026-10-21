import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""A small Nissan pickup grew forty percent in one year, while one of the most famous Jeeps lost a fifth of its sales. And the average full-size truck now costs sixty-seven thousand, four hundred forty-six dollars. Something strange is happening to the American pickup, and it is happening in the middle of the lineup. Here is the real story of the midsize truck comeback.""",
   "Nissan Frontier pickup", "MIDSIZE TRUCKS: WHO IS WINNING?")

# ---------- COLD OPEN ----------
sc("""For years, the story of the American pickup was simple. Trucks got bigger, trucks got fancier, and trucks got more expensive. According to Kelley Blue Book data reported by Cox Automotive, the average full-size pickup sold for sixty-seven thousand, four hundred forty-six dollars in August of twenty twenty-six. That is up two point one percent from a year earlier. And in March, the same figure was sixty-five thousand, nine hundred sixty-four dollars.""",
   "Ford F-150 pickup truck", "FULL-SIZE AVERAGE: $67,446")
sc("""At that price, a lot of buyers do the same thing. They look at the truck on the lot, look at the monthly payment, and keep walking. And right next to that giant truck, there is a smaller one, built on a smaller frame, that does most of the same jobs for a lot less. The question is whether those smaller trucks are really winning, or whether it is just a story that sounds good.""",
   "Toyota Tacoma pickup truck", "ARE SMALLER TRUCKS REALLY WINNING?")
sc("""We checked the numbers, and the answer has a twist. Yes, midsize trucks are growing faster than full-size trucks. But not every midsize truck is winning, and some of them are collapsing. One of them nearly doubled the sales of Toyota's full-size Tundra. One lost a third of its sales in a quarter. And one has rumors around it that nobody has confirmed. Stay with me, because every number comes from a published source, listed in the description.""",
   "Toyota Tundra pickup", "EVERY NUMBER IS SOURCED")
sc("""Here is the number that sets the scale. Through the first nine months of twenty twenty-six, according to Pickup Truck Talk, the seven midsize trucks sold five hundred seven thousand, three hundred ninety-eight in total, up five point four percent. The five full-size trucks we checked, from Ford, Chevrolet, Ram, GMC and Toyota, sold one million, six hundred fifty-eight thousand, one hundred eighty-eight, up one point two percent. So midsize is growing faster. But it is still a third of the size.""",
   "Ford Ranger pickup", "MIDSIZE +5.4% VS FULL-SIZE +1.2%")

# ---------- 1. TOYOTA TACOMA ----------
sc("""Number one is the Toyota Tacoma, and it is not close. Through the first nine months of twenty twenty-six, Toyota sold two hundred fourteen thousand, eight hundred seventy-five Tacomas, up five point one percent. The next best midsize truck, the Chevrolet Colorado, sold seventy-two thousand, eight hundred sixty-three. That means the Tacoma sold almost three times as many as its closest rival. The Fast Lane Truck wrote that no competitor is even remotely close.""",
   "Toyota Tacoma TRD pickup", "TACOMA: 214,875 IN 9 MONTHS")
sc("""Here is the first twist. The Tacoma sold nearly twice as many trucks as Toyota's own full-size pickup. The Tundra sold one hundred ten thousand and eighty in the same period. So the smaller truck is the real star of the Toyota truck business. But the story is not perfect. The Tacoma grew nearly sixteen percent in the first half of the year, and then slipped three and a half percent in the third quarter, to seventy-one thousand and twenty-seven.""",
   "Toyota Tundra pickup", "TACOMA VS TUNDRA: ALMOST 2 TO 1")

# ---------- 2. NISSAN FRONTIER ----------
sc("""Number two is the Nissan Frontier, and it is the biggest surprise in the segment. Through nine months, Nissan sold sixty-six thousand, five hundred thirteen Frontiers. A year earlier it was forty-seven thousand, six hundred thirty. That is a jump of almost forty percent. In the third quarter alone, sales rose thirty-seven and a half percent, to twenty-three thousand, four hundred twelve.""",
   "Nissan Frontier Pro-4X", "FRONTIER: UP 39.6% IN 9 MONTHS")
sc("""So what changed? The Fast Lane Truck credited Nissan's naturally aspirated V six engine, and said buyers seem to be listening. That is worth thinking about. In an age of turbochargers and hybrids and screens, the story behind one of the fastest-growing trucks in America is a simple engine that does not try to be clever. And this is the same Nissan that gave up on its full-size Titan, which sold just thirteen trucks in nine months.""",
   "Nissan Frontier pickup truck", "THE SECRET: A SIMPLE V6")

# ---------- 3. FORD MAVERICK ----------
sc("""Number three is the Ford Maverick, the compact pickup that most people did not expect to matter. Through nine months of twenty twenty-six, Ford sold one hundred twenty-three thousand, six hundred eighty-one Mavericks, up two point three percent. That is more than any midsize truck except the Tacoma, and about twenty-two percent as many as the entire F-Series. According to Pickup Truck Talk, the Maverick still significantly outsells every other compact pickup.""",
   "Ford Maverick pickup", "MAVERICK: 123,681 IN 9 MONTHS")
sc("""The twist is in the rhythm of the year. In the first half, Maverick sales were down five percent, at eighty-one thousand, seven hundred eleven. Then in the third quarter, they jumped twenty point four percent, to forty-one thousand, nine hundred seventy. The only other compact pickup on sale, the Hyundai Santa Cruz, sold fourteen thousand, eight hundred eleven through nine months, down twenty-eight percent. A compact truck can be a hit. This one just happens to be the only one.""",
   "Ford Maverick Lariat", "SANTA CRUZ: DOWN 28.2%")

# ---------- 4. CHEVROLET COLORADO AND GMC CANYON ----------
sc("""Number four is a pair that should be twins. The Chevrolet Colorado and the GMC Canyon are the same truck with different badges. And they went in opposite directions. Through nine months, the Colorado sold seventy-two thousand, eight hundred sixty-three, down five point eight percent. The Canyon sold thirty-three thousand, five hundred forty-five, up twenty point three percent.""",
   "Chevrolet Colorado ZR2", "COLORADO -5.8%, CANYON +20.3%")
sc("""That is one of the strangest splits in the whole market. Same company, same factory, same basic truck, and a gap of more than twenty-six points between the two. The Fast Lane Truck said the Canyon continues to perform well, with a quarterly gain of nearly twenty-two percent in the second quarter. Meanwhile the Colorado sold three percent less in that same quarter. The lesson is that the badge and the price tier matter almost as much as the truck.""",
   "GMC Canyon pickup", "SAME TRUCK. OPPOSITE RESULTS.")

# ---------- 5. FORD RANGER ----------
sc("""Number five is the Ford Ranger, and it is a truck of two moods. Through nine months of twenty twenty-six, Ford sold fifty-one thousand, six hundred thirty Rangers, up six point nine percent. But the quarters look like a roller coaster. Ranger sales slipped nearly ten percent in the second quarter, to sixteen thousand, two hundred ninety-four. Then in the third quarter they jumped fourteen point eight percent, to seventeen thousand, five hundred sixty-one.""",
   "Ford Ranger Raptor", "RANGER: UP 6.9% IN 9 MONTHS")
sc("""Look at that and you can see the real shape of the midsize market. It is not a steady climb. It moves with prices, with incentives, and with what Ford, Toyota and Nissan are doing on the lot that quarter. Cox Automotive's Erin Keating said the continued strong growth of subcompact SUVs highlights how important affordability remains in today's market. And a midsize truck is, for many buyers, the affordable truck.""",
   "Ford Ranger pickup truck", "AFFORDABILITY DRIVES THE MARKET")

# ---------- 6. JEEP GLADIATOR ----------
sc("""Number six is the Jeep Gladiator, and it is the one in trouble. Through nine months, Jeep sold thirty thousand, nine hundred forty-four Gladiators, down nineteen point seven percent. In the second quarter alone, sales fell almost thirty-three percent, from thirteen thousand, three hundred forty-three to eight thousand, nine hundred forty-six. Every other midsize truck on this list is doing better than that.""",
   "Jeep Gladiator pickup", "GLADIATOR: DOWN 19.7%")
sc("""Now the careful part. Pickup Truck Talk wrote in March that rumors claim the Gladiator is living on borrowed time. But the article calls that unconfirmed, and no official announcement has been made. It also says that Ram's midsize pickup, expected to be built in Toledo, is likely to share the plant with the Gladiator. That is speculation, and we are labeling it as speculation. What is confirmed is the sales drop, and that is not a rumor.""",
   "Jeep Gladiator Rubicon", "RUMORS UNCONFIRMED. SALES DROP IS REAL.")

# ---------- 7. HONDA RIDGELINE ----------
sc("""Number seven is the Honda Ridgeline, the truck that never really picked a fight. Through nine months, Honda sold thirty-seven thousand and twenty-eight Ridgelines, down one percent. That is almost flat. The Ridgeline has a loyal base and a small share, and it has stayed there, quarter after quarter. In the third quarter, it rose three point three percent, to thirteen thousand, five hundred thirty-eight.""",
   "Honda Ridgeline pickup", "RIDGELINE: 37,028, DOWN 1%")
sc("""There is a twist even here. The Ridgeline sold more than the Gladiator and more than the Canyon in the first nine months, and the Gladiator was once the exciting one. The calm truck outsold the exciting truck. It is a good reminder that in the truck business, excitement does not always turn into sales, and boring can pay.""",
   "Honda Ridgeline RTL-E", "BORING CAN SELL")

# ---------- THE BIG PICTURE ----------
sc("""Now let's pull back and see the whole picture, because the pattern is clearer from a distance. Of the seven midsize trucks, the picture is not one of a boom. It is a split. Four of them grew, and three of them shrank. The ones that grew were the Tacoma, the Frontier, the Canyon and the Ranger. The ones that shrank were the Colorado, the Gladiator and the Ridgeline. And among the compact trucks, the Maverick grew while the Santa Cruz fell.""",
   "Toyota Tacoma Nissan Frontier pickups", "MIDSIZE: 4 GREW, 3 SHRANK")
sc("""And here is the final twist. All seven midsize trucks put together sold five hundred seven thousand, three hundred ninety-eight in nine months. The F-Series alone, without counting the Lightning, sold five hundred fifty-six thousand, seven hundred thirty-eight. So the entire midsize segment, with all of its brands and all of its headlines, is still smaller than one single full-size truck line.""",
   "Ford F-150 pickup truck", "ALL MIDSIZE < F-SERIES ALONE")
sc("""Why does the midsize truck get so much attention then? Because it is where the change is visible. Prices went up in the full-size segment, the electric trucks stumbled, and buyers who wanted a truck without the full-size price started to look at the lower shelf. According to Kelley Blue Book, the average new vehicle in the United States sold for fifty thousand and eighty-nine dollars in August. A midsize truck can still sit under that number for the right trim.""",
   "Toyota Tacoma pickup", "AVERAGE NEW VEHICLE: $50,089")


# ---------- THE FULL-SIZE SIDE ----------
sc("""To understand the midsize story, you have to look at the other side of the lot, because the full-size trucks are not standing still either. Through the first nine months of twenty twenty-six, Ram pickups sold three hundred twenty-five thousand, three hundred forty-eight, up twenty-four percent. The Chevrolet Silverado sold four hundred thirteen thousand, three hundred eighty-three, down less than one percent. The GMC Sierra sold two hundred fifty-two thousand, six hundred thirty-nine, almost flat.""",
   "Ram 1500 pickup truck", "RAM: +24% IN 9 MONTHS")
sc("""The Ford F-Series, without the electric Lightning, sold five hundred fifty-six thousand, seven hundred thirty-eight, down six point eight percent. That is a fall of more than forty thousand trucks in a single year. And yet it still sold far more than the Ram or the Sierra. When the biggest truck line in America loses forty thousand sales, it is a headline. When the Frontier gains nearly nineteen thousand sales, it is also a headline. Both are real.""",
   "Ford F-150 XLT pickup", "F-SERIES: DOWN 6.8%, STILL #1")
sc("""There is a detail inside the numbers that matters. The Silverado light-duty trucks, the one thousand five hundred models, grew six point five percent. But the heavy-duty Silverado fell thirteen percent, from one hundred fifty-three thousand, seven hundred fifty to one hundred thirty-three thousand, seven hundred sixty-nine. And the Ram light-duty trucks grew forty-one percent, while Ram heavy-duty grew three point four. The market is not moving as one block. It is moving in small pieces.""",
   "Chevrolet Silverado 1500 pickup", "SILVERADO LD +6.5%, HD -13%")
sc("""So a buyer who says trucks are getting more expensive is right, and a buyer who says trucks are getting more affordable is also right, depending on which truck you look at. The full-size average sits above sixty-seven thousand dollars. And the small trucks that sell in huge numbers, like the Maverick, sit much lower on the price scale. It is a market split into tiers, and each tier is following its own logic.""",
   "Ford Maverick pickup", "A MARKET SPLIT IN TIERS")
sc("""Now think about what the carmakers are watching. Nissan watched the Titan sell thirteen trucks in nine months, and it watched the Frontier jump forty percent. Hyundai is watching the Santa Cruz fall twenty-eight percent. Jeep is watching the Gladiator fall twenty percent. Every company has the same table in front of it, and every company is making the same decision. Put the money where the buyers are going.""",
   "Nissan Frontier pickup truck", "THE TABLE EVERY CARMAKER SEES")
sc("""There is also the matter of the model year. A truck bought in the last months of a model year, when the lot is full, is often a better deal than the same truck in spring. Incentives tell the story. Cox Automotive reported that incentives were six point five percent of the average transaction price in August, down from seven point two percent in August of twenty twenty-five. Discounts are getting smaller, and a smaller discount means the buyer has to negotiate harder.""",
   "Toyota Tundra pickup", "INCENTIVES: 6.5% OF PRICE IN AUGUST")
sc("""One last thing about the Tundra, because it explains the Tacoma's power. The Tundra sold one hundred ten thousand and eighty trucks in nine months, down less than one percent. It is a solid truck, and a loyal one. But the Tacoma is the truck Toyota can sell to a first-time buyer, a family, a worker, and an off-road fan, all at once. A truck that fits many lives sells more than a truck built for one.""",
   "Toyota Tundra pickup truck", "TACOMA FITS MANY LIVES")


# ---------- WHICH BUYER ARE YOU ----------
sc("""So which truck fits which buyer? Let's use only what the numbers can support. If you want the choice that the most people have already made, the Tacoma sold two hundred fourteen thousand, eight hundred seventy-five in nine months, which means parts, service, and resale demand are likely to be easy to find. A truck with a big sales base is easier to sell later, because there are more buyers looking for exactly that truck.""",
   "Toyota Tacoma pickup truck", "BUYER 1: THE POPULAR CHOICE")
sc("""If your budget is tight, the Maverick is the truck that the market has clearly voted for among compact pickups, with one hundred twenty-three thousand, six hundred eighty-one sold. It is smaller, so check that its bed and its towing capacity fit your jobs. Do not assume. Look up the exact number for the exact configuration, because the same model can tow very different loads depending on the engine and the package.""",
   "Ford Maverick pickup truck", "BUYER 2: THE TIGHT BUDGET")
sc("""If you want something different from the crowd, the Frontier is the surprise, up nearly forty percent, and the Canyon is the sibling that is growing while the Colorado slips. Growth is not a guarantee of quality, but it does tell you that other buyers are choosing these trucks right now, and dealers tend to keep trucks that sell well in stock. That can mean more choice of trims and colors.""",
   "GMC Canyon pickup truck", "BUYER 3: SOMETHING DIFFERENT")
sc("""And if you love the Gladiator, you should not panic. A sales drop and a rumor are not an announcement. But before buying, ask the dealer directly about the future of the model, and ask about the warranty coverage in writing. A warranty normally stays valid on a model that has been discontinued, but a clear answer before you sign is always better than a surprise afterward.""",
   "Jeep Gladiator pickup", "BUYER 4: THE GLADIATOR FAN")
sc("""One more point about reading numbers like these. A quarter can lie. The Ranger fell almost ten percent in one quarter and rose almost fifteen in the next. The Maverick fell five percent in the first half and rose twenty percent in the third quarter. So when you read a headline about a truck that is booming or collapsing, check the full nine months, not only the last three. The longer window tells you the real direction.""",
   "Ford Ranger pickup", "A QUARTER CAN LIE")

# ---------- CLOSE ----------
sc("""So what does this mean if you are buying a truck in twenty twenty-seven? First, a midsize truck is not automatically cheaper in total cost. Compare the exact trim, the options, and the financing, not the segment. Second, look at the sales trend of the exact model. A truck with falling sales, like the Gladiator, can mean fewer incentives to negotiate with and a risk for resale value, or sometimes a better deal, so check both.""",
   "Ford Ranger pickup truck", "CHECK 1 AND 2: TRIM AND TREND")
sc("""Third, look at what you actually tow and haul. A midsize truck is enough for many weekend jobs, but not for every trailer. Check the towing capacity of the exact configuration before you decide. Fourth, ask the dealer about incentives. The Cox report shows incentives at six point five percent of the average price in August, down from seven point two percent a year earlier, so discounts are smaller than they were.""",
   "Chevrolet Colorado pickup", "CHECK 3 AND 4: TOWING AND INCENTIVES")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to see which trucks keep their value the longest, subscribe, because that is coming soon. Thanks for watching.""",
   "Toyota Tacoma pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"A small Nissan pickup": "Intro", "Number one": "1. Toyota Tacoma", "Number two": "2. Nissan Frontier",
      "Number three": "3. Ford Maverick", "Number four": "4. Chevrolet Colorado and GMC Canyon",
      "Number five": "5. Ford Ranger", "Number six": "6. Jeep Gladiator", "Number seven": "7. Honda Ridgeline",
      "Now let's pull back": "The big picture", "So what does this mean": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video03", "length_scale": 1.45,
  "title": "7 Midsize Trucks Fighting for Buyers in 2027 (Who Is Really Winning)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
