import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One truck company gained more than fifty-five thousand sales in a single year. Another lost almost fifty-three thousand. And the whole American pickup market barely moved. How can the total stay flat while the winners and losers change places? This is the real story of the truck brand war in twenty twenty-six.""",
   "Ram 1500 pickup truck", "TRUCK BRAND WAR 2026")

# ---------- COLD OPEN ----------
sc("""Every year, the pickup market looks like a calm lake from the air. Millions of trucks, the same famous names, the same top three. But underneath, the water is moving. Companies gain buyers in one corner and lose them in another, and the headline numbers hide it. To see it, you have to add the trucks up brand by brand, and compare the same nine months in two different years.""",
   "Ford F-150 pickup truck", "THE CALM LAKE HIDES THE CURRENT")
sc("""So that is what we did. We took the nine-month sales table that Pickup Truck Talk published for twenty twenty-six, with the same period of twenty twenty-five, and added up every pickup by company. Ford, General Motors, Stellantis, Toyota, Nissan, Honda and Hyundai. Please note that these totals are our own calculation from that table, and that they count the models in the table only, not the medium-duty trucks and not the startups.""",
   "Chevrolet Silverado 1500 pickup", "OUR CALCULATION FROM PUBLISHED SALES")
sc("""The result is a surprise. In the first nine months of twenty twenty-six, those trucks added up to about two million, three hundred twenty-four thousand. In the same months of twenty twenty-five, about two million, three hundred sixteen thousand. That is a change of three tenths of one percent. The market is flat. But inside that flat number, one company grew by eighteen percent, and another one shrank by almost seven.""",
   "Toyota Tacoma Ford F-150 Chevrolet Silverado pickups", "MARKET: +0.3%. COMPANIES: +18% TO -7%")
sc("""Stay with me, because there is a twist in every one of these stories. The biggest gain came from a truck brand that was supposed to be in trouble. The biggest loss came from the brand that has led America for decades. One company is celebrated for a truck that sold thirteen units. And one brand is quietly losing a third of its buyers. Every number comes from a published source, listed in the description.""",
   "Ford F-250 Super Duty pickup", "EVERY NUMBER IS SOURCED")

# ---------- 1. STELLANTIS / RAM ----------
sc("""Number one is Stellantis, the company behind Ram and Jeep, and it is the biggest winner in the table. Through nine months of twenty twenty-six, Ram pickups sold three hundred twenty-five thousand, three hundred forty-eight, up twenty-four percent. The Jeep Gladiator sold thirty thousand, nine hundred forty-four, down almost twenty percent. Put them together and Stellantis sold three hundred fifty-six thousand, two hundred ninety-two trucks, up about eighteen percent.""",
   "Ram 1500 Big Horn pickup", "STELLANTIS: +18.4%, +55,393 TRUCKS")
sc("""That is an extra fifty-five thousand, three hundred ninety-three trucks in a single year. And in our calculation, Stellantis went from about thirteen percent of these trucks to about fifteen percent. Two full points of the whole market, in one year, is a very large move. It happened in a year in which Ram canceled its electric truck, and delayed the replacement again. The truck that was not on sale did not hurt the trucks that were.""",
   "Ram 1500 pickup", "SHARE: 13.0% TO 15.3%")
sc("""Look inside the Ram number for the twist. The light-duty Ram, the one thousand five hundred, sold two hundred two thousand, one hundred forty-seven, up forty-one percent. In the third quarter alone, it jumped seventy-three percent, from forty-four thousand, three hundred forty-nine to seventy-six thousand, six hundred fifty. In this table, Ram is now the fastest-growing full-size truck brand in the country.""",
   "Ram 1500 Rebel pickup", "RAM LD: +41% IN 9 MONTHS")
sc("""A few things might explain it, and we want to be careful here, because the sources we checked do not give a single reason. What we can say is what the numbers show. Ram grew in the light-duty trucks and in the heavy-duty trucks, up three point four percent. It grew while Ford and General Motors were adjusting their electric plans. And it grew without a new electric truck. So the lesson is not that electric trucks hurt, but that the buyer showed up for the gas truck.""",
   "Ram 2500 Heavy Duty pickup", "RAM HD: +3.4%")

# ---------- 2. FORD ----------
sc("""Number two is Ford, and it is the biggest loser in the table, although it is still the biggest truck brand in the country. Adding the F-Series, the Lightning, the Ranger and the Maverick, Ford sold about seven hundred thirty-seven thousand trucks through nine months, down six point seven percent. That is a loss of fifty-two thousand, nine hundred forty-three trucks. The F-Series alone fell by forty thousand, eight hundred eight.""",
   "Ford F-150 XLT pickup", "FORD: -6.7%, -52,943 TRUCKS")
sc("""Here is the twist. The Lightning, which gets all the headlines, explains only part of it. It fell from twenty-three thousand and thirty-four to four thousand, seven hundred seventy, a drop of eighteen thousand, two hundred sixty-four. The rest of the fall came from the regular F-Series trucks. The F-Series, not counting the Lightning, went from five hundred ninety-seven thousand, five hundred forty-six to five hundred fifty-six thousand, seven hundred thirty-eight, down six point eight percent.""",
   "Ford F-150 Lightning pickup", "LIGHTNING: -18,264. F-SERIES: -40,808")
sc("""In our calculation, Ford went from about thirty-four percent of these trucks to about thirty-two percent. Still a giant, but a smaller one. And there is a quiet bright spot. The Ranger rose six point nine percent, to fifty-one thousand, six hundred thirty, and the Maverick rose two point three percent, to one hundred twenty-three thousand, six hundred eighty-one. The small trucks helped, and the big ones did not.""",
   "Ford Maverick pickup", "FORD SHARE: 34.1% TO 31.7%")
sc("""Ford's chief executive, Jim Farley, said in December that Ford would rather not spend billions more on large electric vehicles that have no path to profitability, and that hybrids have been more popular than the company ever expected. Ford took a nineteen point five billion dollar charge to change course. The sales table shows what changing course looks like in the short term. When you stop making a truck, its sales go away, and the company has to win them back somewhere else.""",
   "Ford Rouge Complex Dearborn factory", "FORD: $19.5 BILLION TO CHANGE COURSE")

# ---------- 3. GENERAL MOTORS ----------
sc("""Number three is General Motors, the brand with the largest total, and a very small decline. Adding the Silverado, the Sierra, the Colorado, the Canyon, and the electric Silverado EV, Sierra EV and Hummer EV, GM sold about seven hundred eighty-seven thousand trucks through nine months, down one point eight percent. In our calculation, GM is now slightly ahead of Ford, with about thirty-four percent of the trucks, against about thirty-two for Ford.""",
   "Chevrolet Silverado 1500 pickup", "GM: -1.8%, NOW #1 IN OUR TABLE")
sc("""Look at what is inside that number, because it is a story of a company holding steady with one hand while losing with the other. The gas trucks did fine. The Silverado was down less than one percent. The Sierra was up three tenths of one percent. The Canyon was up twenty percent. But the three electric lines, the Silverado EV, the Sierra EV and the Hummer EV, fell from about twenty-eight thousand to about fifteen thousand.""",
   "GMC Sierra pickup", "GM EV TRUCKS: ~28,000 TO ~15,000")
sc("""That is the twist. General Motors lost less than most of its rivals, and the reason is the gas trucks carrying the weight of the electric ones. The heavy-duty Silverado fell thirteen percent, from one hundred fifty-three thousand, seven hundred fifty to one hundred thirty-three thousand, seven hundred sixty-nine. But the light-duty Silverado grew six point five percent. In a flat market, a company with a wide lineup can hide a bad corner.""",
   "Chevrolet Silverado HD pickup", "SILVERADO LD +6.5%, HD -13%")

# ---------- 4. TOYOTA ----------
sc("""Number four is Toyota, and its story is the quietest. Adding the Tundra and the Tacoma, Toyota sold three hundred twenty-four thousand, nine hundred fifty-five trucks, up three percent. In our calculation, its share rose from about thirteen point six percent to about fourteen percent. Nothing dramatic. But in a flat market, a company that gains a little every year is gaining at the expense of someone.""",
   "Toyota Tacoma pickup", "TOYOTA: +3.0%")
sc("""And here is the twist inside Toyota. All of the growth came from the Tacoma, up five point one percent, to two hundred fourteen thousand, eight hundred seventy-five. The Tundra, the full-size truck, was down eight tenths of a percent, to one hundred ten thousand and eighty. Toyota is winning in the middle of the market and holding in the big one, and the company does not have to invent anything new to do it.""",
   "Toyota Tundra pickup", "TACOMA +5.1%, TUNDRA -0.8%")

# ---------- 5. NISSAN ----------
sc("""Number five is Nissan, and it is the strangest company on the list. Adding the Titan and the Frontier, Nissan sold sixty-six thousand, five hundred twenty-six trucks through nine months, up thirty-four percent. That is the highest growth rate of any company in the table. And it happened in a year in which the Titan sold thirteen trucks.""",
   "Nissan Frontier pickup", "NISSAN: +34%")
sc("""Yes, thirteen. A year earlier, the Titan sold two thousand and twenty-four. Nissan ended the full-size truck after the twenty twenty-four model year, as Motor Authority reported, and the numbers are now just the last trucks leaving the lots. But the Frontier more than made up for it. It rose from forty-seven thousand, six hundred thirty to sixty-six thousand, five hundred thirteen. A company can grow by ending a truck, if the truck it keeps is the right one.""",
   "Nissan Titan pickup", "TITAN: 2,024 TO 13")

# ---------- 6. HONDA AND HYUNDAI ----------
sc("""Number six is the pair at the bottom of the table, Honda and Hyundai, and they tell opposite stories. The Honda Ridgeline sold thirty-seven thousand and twenty-eight through nine months, down just one percent. A very small drop, and a very stable share of about one point six percent. Honda has one truck, and a small, steady group of buyers.""",
   "Honda Ridgeline pickup", "HONDA RIDGELINE: -1.0%")
sc("""The Hyundai Santa Cruz is the weakest number in the whole table. It sold fourteen thousand, eight hundred eleven trucks through nine months, down twenty-eight percent from twenty thousand, six hundred thirty-three. In our calculation, its share fell from about nine tenths of a percent to about six tenths. Automotive News and The Autopian reported, through unnamed sources, that the Santa Cruz is being phased out. Hyundai declined to confirm that.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: -28.2%")


# ---------- THE THIRD QUARTER TWIST ----------
sc("""Now we need to talk about the third quarter, because it changes the picture. Everything so far used nine months. But the most recent three months, July through September, look different. Ford's F-Series, not counting the Lightning, sold two hundred three thousand, four hundred eighteen trucks, up two point nine percent from the same quarter a year earlier. In that quarter, the biggest brand in the country was growing.""",
   "Ford F-150 pickup", "Q3: F-SERIES UP 2.9%")
sc("""And Ford was not alone. The Chevrolet Silverado grew four point nine percent in the quarter, to one hundred forty-four thousand, four hundred ninety-nine. The Ford Ranger grew fourteen point eight percent. The Maverick grew twenty point four percent. The Canyon grew almost eighteen. But the Toyota Tacoma slipped three and a half percent, the GMC Sierra slipped six tenths of a percent, and the Gladiator fell more than nine.""",
   "Chevrolet Silverado pickup", "Q3: SILVERADO +4.9%, MAVERICK +20.4%")
sc("""The Ram trucks, meanwhile, rose almost thirty-four percent in the quarter, from eighty-eight thousand and sixty-six to one hundred seventeen thousand, seven hundred fifty-seven. The Nissan Frontier rose thirty-seven and a half. And the Santa Cruz fell almost twenty-five percent. So the winners stayed the winners, and the biggest loser of the year, Ford, started to recover. A nine-month table tells you the direction, and the latest quarter tells you where the road bends.""",
   "Ram 1500 pickup truck", "Q3: RAM +33.7%, SANTA CRUZ -24.7%")
sc("""This is why we always read two windows at the same time. If you only read the nine months, you might believe Ford is in free fall. If you only read the third quarter, you might believe nothing happened at all. Both are true, and neither is the full story. A company can be losing for the year and recovering at the end of it. And a buyer who understands that can ask a better question at the dealership.""",
   "Ford F-150 Lightning pickup", "TWO WINDOWS, ONE TRUTH")
sc("""What does that mean at the dealership? It means that a brand that lost ground and is now recovering might be willing to negotiate to keep the recovery going. And a brand that is growing quickly might have fewer reasons to discount. We cannot promise which one you will find. But we can tell you that Cox Automotive measured incentives at six point five percent of the average price in August, down from seven point two percent a year earlier.""",
   "Ford F-150 XLT pickup", "INCENTIVES: 7.2% TO 6.5%")
sc("""A final point about what a table like this can and cannot tell you. It counts trucks sold in the United States, by company. It does not count the quality of the truck, or how happy the owners are, or how much each one cost to build. A truck can sell well because it is good, because it is cheap, because the company discounted it, or because a fleet bought thousands at once. Sales tell you what buyers did. They do not tell you why.""",
   "Chevrolet Silverado 1500 pickup", "SALES SHOW WHAT, NOT WHY")
sc("""That is why we pair every sales number with a check you can do yourself. Look up the reliability record of the exact model year. Read the owner reviews. Compare the price of the same trim at two dealers. And look at the warranty. A sales number can tell you which truck is popular, but only you can decide which truck is right for the work you do and the money you have.""",
   "Toyota Tacoma pickup", "SALES NUMBERS ARE ONLY A START")

# ---------- THE BIG PICTURE ----------
sc("""So let's put the whole race in one picture. Stellantis gained about two points of share. Nissan gained about eight tenths of a point. Toyota gained about four tenths. Honda stayed the same. Hyundai lost three tenths. General Motors lost seven tenths. And Ford lost two and a half points, the biggest loss in the table, almost two and a half points. These are our calculations from published sales, rounded, and they show who is taking buyers from whom.""",
   "Ram Ford Chevrolet pickup trucks", "SHARE CHANGE: RAM +2.3, FORD -2.4")
sc("""Now here is the final twist. Total trucks in the table grew by about eight thousand in nine months. But Stellantis alone grew by more than fifty-five thousand, and Ford alone shrank by almost fifty-three thousand. So the market did not grow, and the winners took the trucks from the losers. In a market this big and this stable, a buyer is rarely new. A buyer is almost always a buyer taken from somebody else.""",
   "Ford F-150 and Ram 1500 pickups side by side", "WINNERS TAKE FROM LOSERS")
sc("""Why does that matter to you? Because the brand that is gaining has a reason to make a deal, and the brand that is losing has a reason to make a deal too, just for different reasons. And the truck you cross-shop is probably the one that went the other way. If you are looking at a Ford, check what Ram is offering. If you are looking at a Ram, check what Ford and General Motors are offering. Competition is the most useful tool a buyer has.""",
   "Chevrolet Silverado Ford F-150 pickups", "COMPETITION IS YOUR BEST TOOL")

# ---------- CLOSE ----------
sc("""So what should you check before you buy in twenty twenty-seven? First, look at the sales trend of the exact model, not only the brand. A brand can be growing while one of its trucks is falling. Second, find out whether the truck is still being built, and for how long. Third, compare the full cost, with the price, the financing, and the resale value, because a truck that sells well is generally easier to sell later.""",
   "Ford F-150 pickup", "CHECK 1, 2 AND 3")
sc("""Fourth, ask for the incentives. The Cox Automotive report for August showed incentives at six point five percent of the average price, down from seven point two percent a year earlier, so you may have to ask for them. And fifth, remember that a flat market means every sale is a fight. You are not the one who needs to be convinced. The brand is.""",
   "Chevrolet Silverado 1500", "CHECK 4 AND 5")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we just walked through. The link is in the description and in the pinned comment. If you want to see how tariffs changed truck prices, subscribe, because that is coming next. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One truck company gained": "Intro", "Number one": "1. Stellantis (Ram and Jeep)", "Number two": "2. Ford",
      "Number three": "3. General Motors", "Number four": "4. Toyota", "Number five": "5. Nissan",
      "Number six": "6. Honda and Hyundai", "So let's put the whole race": "The big picture",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video04", "length_scale": 1.66,
  "title": "6 Truck Brands Winning and Losing the Sales War Right Now", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
