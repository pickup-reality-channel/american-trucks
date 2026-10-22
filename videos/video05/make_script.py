import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Tariffs added thirty billion dollars in costs to the car industry in one year. A Chevrolet Silverado LT now costs twelve point six percent more than it did two years ago. But a Toyota Tacoma costs less than one percent more. And the biggest price jump on your next truck might not be the truck at all. Here is what tariffs really did to truck prices, model by model.""",
   "Chevrolet Silverado 1500 pickup", "TARIFFS VS TRUCK PRICES")

# ---------- COLD OPEN ----------
sc("""When tariffs on cars arrived, the warning was loud and simple. Trucks will cost thousands more. Some of the early estimates were frightening. But a year later, the real picture is more interesting, and more useful, because it depends on which truck you look at, which costs you count, and who ends up paying. The headline number is not the whole story. The model-by-model numbers are.""",
   "Ford F-150 pickup truck", "THE WARNING VS THE REAL NUMBERS")
sc("""So we collected the published data. For the industry-wide picture, we used the Cox Automotive release reported by CBT News in March of twenty twenty-six. For the truck-by-truck prices, we used the analysis by TFL Car, which compared the landed cost of the most popular trims in twenty twenty-four with twenty twenty-six. Landed cost means the sticker price plus the destination fee. Every source is listed in the description.""",
   "Ram 1500 Big Horn pickup", "EVERY NUMBER IS SOURCED")
sc("""There is a twist in every one of these stories. One truck got a price increase that was bigger than almost any other vehicle in the study. One truck got cheaper after you adjust for inflation. One fee went up forty percent, and it has nothing to do with the truck itself. And the data says that the tariffs are only part of what happened. Stay with me, because the last twist changes how you should shop.""",
   "Toyota Tacoma pickup", "SIX TWISTS ON ONE LIST")

# ---------- THE BIG PICTURE FIRST ----------
sc("""First, the industry numbers. According to Cox Automotive, as reported by CBT News, tariffs added an estimated thirty billion dollars in costs over the year since they were imposed. The average suggested retail price rose ten point four percent. Imported vehicles were estimated to cost between five thousand dollars and eight thousand, nine hundred dollars more per vehicle. Domestic vehicles rose by sixteen hundred to two thousand dollars, because of tariffs on materials like steel and aluminum.""",
   "Ford F-150 Chevrolet Silverado pickups dealership lot", "TARIFFS: $30 BILLION IN A YEAR")
sc("""Now the part most people miss. Those costs did not all land on the buyer. Cox estimated that consumers paid five point nine percent more on average over thirty-seven weeks for model year twenty twenty-five and twenty twenty-six vehicles. Dealers absorbed the other four and a half percent. So of every ten dollars of price pressure, about six reached the buyer and about four were absorbed by someone else.""",
   "Chevrolet Silverado dealership", "BUYERS: +5.9%. DEALERS: +4.5%")
sc("""And here is a number that matters for trucks in particular. Domestic production rose four point nine percent in the period, and reached fifty-four point four percent of new vehicles sold. Most full-size pickups are built in North America, and the domestic tariff cost, of sixteen hundred to two thousand dollars, is much smaller than the import cost. That might be the first clue about why the truck numbers look so different from the car numbers.""",
   "Ford F-150 factory assembly line", "54.4% OF NEW VEHICLES BUILT IN THE US")

# ---------- 1. CHEVROLET SILVERADO ----------
sc("""Number one is the Chevrolet Silverado one thousand five hundred, and it is the biggest price increase on the list. TFL Car compared the LT trim, in twenty twenty-four and twenty twenty-six. In twenty twenty-four, the landed cost was forty-nine thousand, nine hundred ninety-five dollars. In twenty twenty-six, it was fifty-six thousand, two hundred ninety dollars. That is an increase of twelve point six percent, or six thousand, two hundred ninety-five dollars.""",
   "Chevrolet Silverado 1500 LT pickup", "SILVERADO LT: $49,995 TO $56,290")
sc("""After you adjust for inflation, the increase shrinks to five point two percent. But that is still the biggest real increase among all the pickups in the study. And here is the twist. The Silverado is built in North America, and the tariff cost on domestic vehicles was estimated at sixteen hundred to two thousand dollars. The price rose by more than three times that. So the tariff cannot explain the whole increase, and the data suggests that something else is also going on.""",
   "Chevrolet Silverado pickup truck", "ADJUSTED FOR INFLATION: +5.2%")

# ---------- 2. GMC SIERRA ----------
sc("""Number two is the GMC Sierra one thousand five hundred, which is the Silverado's twin. The SLE trim cost fifty-one thousand and ninety-five dollars in twenty twenty-four, and fifty-seven thousand, one hundred ninety dollars in twenty twenty-six. An increase of eleven point nine percent. After inflation, four point six percent. Almost exactly the same story as the Silverado, which is what you would expect from two trucks built by the same company on the same platform.""",
   "GMC Sierra 1500 SLE pickup", "SIERRA SLE: $51,095 TO $57,190")
sc("""That pairing is useful, because it tells you what is a company decision and what is a truck decision. When two trucks from the same company move together, it is likely a company decision about price. When two trucks from different companies move very differently, it points to something else. And that is exactly what happens when we look at the next truck on the list, the Ford F-one-fifty.""",
   "GMC Sierra pickup truck", "SAME COMPANY, SAME MOVE")

# ---------- 3. FORD F-150 ----------
sc("""Number three is the Ford F-one-fifty XLT, and it is a much smaller story. The XLT cost forty-nine thousand, six hundred fifteen dollars in twenty twenty-four and fifty-two thousand, five hundred ninety dollars in twenty twenty-six. An increase of six percent. And after inflation, it is down nine tenths of one percent. In real terms, the best-selling truck in America got very slightly cheaper in two years.""",
   "Ford F-150 XLT pickup", "F-150 XLT: $49,615 TO $52,590")
sc("""Look at the gap with the Silverado. The Silverado LT rose six thousand, two hundred ninety-five dollars. The F-one-fifty XLT rose two thousand, nine hundred seventy-five. The trims are not identical, so this is not a perfect comparison, and TFL Car says so. But it is a useful one, because the two trucks are the closest rivals in America. Same buyers, same price band, very different paths. The difference is a company decision, not a tariff decision.""",
   "Ford F-150 pickup truck", "FORD +$2,975. CHEVROLET +$6,295.")

# ---------- 4. RAM 1500 ----------
sc("""Number four is the Ram one thousand five hundred Big Horn. It cost forty-six thousand, five hundred seventy-nine dollars in twenty twenty-four, and forty-nine thousand, five hundred forty-one in twenty twenty-six. An increase of six point four percent, or two thousand, nine hundred sixty-two dollars. Adjusted for inflation, it is down six tenths of one percent. Almost the same shape as the Ford.""",
   "Ram 1500 Big Horn pickup", "RAM BIG HORN: $46,579 TO $49,541")
sc("""This is where the twist begins. The Ram is the cheapest of the big three trucks in this study, and in the same period its sales jumped twenty-four percent through nine months, according to Pickup Truck Talk. We are not saying the price caused the sales growth, because the sources do not say that. But the two facts sit side by side. The truck whose real price barely moved was the truck that grew the most.""",
   "Ram 1500 pickup truck", "RAM: PRICE STABLE, SALES +24%")

# ---------- 5. TOYOTA TACOMA ----------
sc("""Number five is the Toyota Tacoma SR5, and it is the lowest price increase on the whole list. In twenty twenty-four, it cost thirty-nine thousand, one hundred ninety dollars. In twenty twenty-six, thirty-nine thousand, four hundred fifty. An increase of seven tenths of one percent, or two hundred sixty dollars. And after you adjust for inflation, the Tacoma is five point nine percent cheaper than it was two years ago.""",
   "Toyota Tacoma SR5 pickup", "TACOMA SR5: +0.7%")
sc("""So the truck with the best sales growth in the midsize segment, the Tacoma, is also the truck whose real price fell the most. That does not prove that one caused the other. But it fits the pattern in the sales data. Toyota sold two hundred fourteen thousand, eight hundred seventy-five Tacomas through nine months, up five percent. It is a reminder that tariffs do not hit every company the same way, and that a company can choose how much of a cost to pass on.""",
   "Toyota Tacoma TRD pickup", "REAL PRICE: DOWN 5.9%")

# ---------- 6. DESTINATION FEES ----------
sc("""Number six is the fee that most buyers never think about, the destination charge. According to the CBT News report, the destination fee on most full-size General Motors and Ford trucks and SUVs is two thousand, seven hundred ninety-five dollars for twenty twenty-six. And General Motors raised the Chevrolet Silverado destination fee by forty percent in one year. Forty percent. For delivering a truck from a factory to a dealer.""",
   "Chevrolet Silverado delivery transport truck", "DESTINATION FEE: $2,795")
sc("""CBT News estimated that this single increase would generate seven hundred forty-eight point eight million dollars in additional revenue from the Silverado and the Sierra, based on sales volume. That is the article's estimate, and we want to label it as an estimate. But it shows the scale. A fee that is invisible to most buyers, because it is added at the end of the price, can be worth hundreds of millions of dollars to a company.""",
   "Chevrolet Silverado pickup trucks", "SILVERADO FEE: +40% IN ONE YEAR")
sc("""And TFL Car found the same pattern across the half-ton trucks. Destination fees on every half-ton pickup in the study rose about forty percent over three years. TFL suggests that this may be one way the big three carmakers pass tariff-related costs to the buyer. But it also says inflation could explain some of it. So the honest summary is this. The fee went up a lot, the reason is not fully proven, and you should always look at it before you sign.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "HALF-TONS: FEES UP ~40%")

# ---------- THE CONCLUSION ----------
sc("""So what is the final twist? TFL Car looked at the top ten best-selling vehicles, and found that the average price rose seven point two percent from twenty twenty-four to twenty twenty-six, before adjusting for inflation. After inflation, it rose two tenths of one percent. Their conclusion was that the price increases consumers see mostly reflect inflation, not tariffs alone. That is a more careful answer than the headlines gave, and it is worth taking seriously.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "AVERAGE: +7.2%. AFTER INFLATION: +0.2%")
sc("""But we should be careful not to overstate it either. The same analysis covers only popular trims, not base trims or fully loaded ones. It calls itself dramatically simplified, and it does not separate out raw material costs, trade deals, financing costs or where the truck was assembled. And Cox Automotive's industry data tells a different part of the story, with thirty billion dollars in tariff costs and imported vehicles costing thousands more. Both can be true at once.""",
   "Chevrolet Silverado 1500 pickup truck", "LIMITS: POPULAR TRIMS ONLY")
sc("""Now the averages. According to Kelley Blue Book, the average full-size pickup sold for sixty-five thousand, nine hundred sixty-four dollars in March of twenty twenty-six, up two point eight percent. By August it was sixty-seven thousand, four hundred forty-six dollars, up two point one percent from a year earlier. Those are transaction prices, which include what buyers actually paid, with options. They are much higher than the trims in the TFL study, because buyers tend to choose more expensive versions.""",
   "Ford F-150 Lariat pickup", "FULL-SIZE AVERAGE: $67,446 IN AUGUST")
sc("""One more thing that matters. Cox Automotive reported that incentives were six point five percent of the average price in August, down from seven point two percent a year earlier. So discounts got smaller while prices rose a little. That is the real squeeze on a buyer. It is not one big jump. It is several small changes, a higher sticker, a higher destination fee, and a smaller discount, all moving in the same direction.""",
   "Chevrolet Silverado pickup dealership", "INCENTIVES: 7.2% TO 6.5%")
sc("""And the tariffs themselves have no end date. According to CBT News, the tariffs were imposed under Section two thirty-two of the Trade Expansion Act of nineteen sixty-two, and they do not include a sunset clause. Changing them would need administrative action or legal intervention. So if you are waiting for prices to drop because tariffs will disappear, the published reporting does not give you a date to wait for.""",
   "United States Capitol building Washington", "NO SUNSET CLAUSE ON THE TARIFFS")


# ---------- RECAP AND DOLLARS ----------
sc("""Let's line the five trucks up, in dollars, so you can see the whole picture at once. The Silverado LT rose six thousand, two hundred ninety-five dollars. The Sierra SLE rose six thousand, ninety-five. The F-one-fifty XLT rose two thousand, nine hundred seventy-five. The Ram Big Horn rose two thousand, nine hundred sixty-two. And the Tacoma SR5 rose two hundred sixty. Same two years, same tariffs, and a spread of more than six thousand dollars between the highest and the lowest.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 Toyota Tacoma pickups", "SPREAD: $260 TO $6,295")
sc("""That spread is the most important number in this video. If tariffs were the only reason prices rose, all of these trucks would move in a similar way, because they all face a similar system of costs. But they do not. The spread tells you that each company made its own choices about how much to charge, how much to absorb, and how much to add through fees. The tariff is the same. The decision is different.""",
   "Chevrolet Silverado Ford F-150 pickups", "SAME TARIFFS. DIFFERENT DECISIONS.")
sc("""There is a second lesson in the dealer number. Cox said dealers absorbed four and a half percent of the cost pressure. That means that at the dealership, there is real money that someone has already agreed to give up. And it means that a buyer who asks for a better price is not asking for something impossible. The cost is already being shared. The only question is who shares it with you.""",
   "Chevrolet Silverado dealership lot", "DEALERS ABSORBED 4.5%")
sc("""And here is what you should not conclude from these numbers. You should not conclude that tariffs did nothing, because the industry data says they added thirty billion dollars in costs. You should not conclude that a Silverado is a bad truck, because price and quality are different questions. And you should not conclude that the Tacoma will stay cheap, because a price in twenty twenty-six does not promise a price in twenty twenty-seven. Prices can change again, in either direction.""",
   "Toyota Tacoma pickup truck", "WHAT NOT TO CONCLUDE")
sc("""So here are the questions to bring to a dealer, in plain words. What is the full price, with every fee, before taxes? What is the destination charge, and is it the same as last year? Which incentives apply to this exact truck, and when do they end? And what would the price be at another dealer, for the same trim? Four questions, and any honest dealer can answer them in a minute.""",
   "Ford F-150 pickup truck dealership", "FOUR QUESTIONS FOR THE DEALER")
sc("""Finally, think about the five year picture. A truck that costs more to buy can still cost less to own if it holds its value better, uses less fuel, or needs fewer repairs. We will cover that in a future video, with numbers. For now, the lesson is that the sticker price is the first number in a long list, and the truck that looks expensive today is not always the one that costs you the most.""",
   "Toyota Tundra pickup truck", "STICKER PRICE IS ONLY THE START")

# ---------- CLOSE ----------
# ---------- EXTRA: BUYER VALUE ----------
sc("""Let's slow down and turn the biggest number into something you can use. A twelve point six percent increase sounds abstract. But for the Silverado LT it means six thousand, two hundred ninety-five dollars more, on a truck that cost forty-nine thousand, nine hundred ninety-five dollars two years earlier. If you finance a truck, that extra money does not just sit on the sticker. It becomes a bigger loan, and a bigger loan means a bigger payment every month for as long as you keep the truck.""",
   "Chevrolet Silverado 1500 LT pickup", "WHAT +$6,295 MEANS FOR YOU")
sc("""Now compare two figures from the same list. The Silverado went up twelve point six percent before inflation, and five point two percent after inflation. The difference between those two numbers is what everything cost in general over two years. So if a salesperson says prices are up because of the economy, part of that is true. But only five point two points of the Silverado increase are left after you take the general rise out. Always ask which of the two numbers you are being shown.""",
   "Chevrolet Silverado pickup truck", "BEFORE AND AFTER INFLATION")
sc("""A common mistake is to compare the monthly payment between two trucks and stop there. A payment can look the same because the loan is longer, or because the down payment is bigger. The number that does not hide anything is the out-the-door price. That is the price with the destination charge, every dealer fee and the taxes, all in one line. Ask for it in writing, for each truck you are considering, and compare those lines instead of the monthly payment.""",
   "Ford F-150 pickup dealership", "ASK FOR THE OUT-THE-DOOR PRICE")
sc("""There is a second mistake, and it is comparing the wrong trims. The Tacoma SR5 at thirty-nine thousand, four hundred fifty dollars and the Silverado LT at fifty-six thousand, two hundred ninety dollars are not rivals. One is a midsize truck and the other is a full-size truck. If you are cross-shopping, put the Tacoma next to a midsize truck and the Silverado next to the F-one-fifty and the Ram. The study itself warns that its trims are not identical, and you should treat your own comparison the same way.""",
   "Toyota Tacoma SR5 pickup", "COMPARE SAME-SIZE TRUCKS")
sc("""So who does each result suit? If you want a full-size truck and care about price paid, the F-one-fifty XLT and the Ram Big Horn both rose about six percent, and both went slightly down after inflation. If you only need a smaller truck, the Tacoma SR5 moved by just two hundred sixty dollars. And if you are set on a Silverado or a Sierra, the numbers say you should negotiate harder, because those two rose the most and the dealers absorbed part of the cost in the industry data.""",
   "Ram 1500 Big Horn pickup", "WHO SHOULD BUY WHAT")
sc("""And who should wait? If your current truck is running well and your only reason to buy is fear of the next price rise, the numbers do not force you. The tariffs have no sunset clause, so waiting for them to vanish is not a plan either. What you can do is compare the same trim on the same day at more than one dealer, write the prices down, and let the difference between them decide. A calm buyer with three quotes has more power than a rushed buyer with none.""",
   "Chevrolet Silverado dealership lot", "SAME TRIM, SAME DAY, THREE QUOTES")

sc("""So what should you check before you buy a truck in twenty twenty-seven? First, compare the exact trim, not the model. A fifty-six thousand dollar Silverado and a fifty-two thousand dollar F-one-fifty are different trucks with different options. Second, ask for the destination fee in writing, and compare it between brands. It can be two thousand, seven hundred ninety-five dollars, and it is added after the price you were quoted.""",
   "Ford F-150 pickup", "CHECK 1 AND 2: TRIM AND FEES")
sc("""Third, look at the price after inflation, not only the sticker, if you are comparing a truck to the one you bought years ago. Fourth, ask about incentives, because they are smaller than a year ago. And fifth, do not assume that the brand with the biggest price increase has the worst truck. Price is a company decision. Quality is a different question, and you can only answer it by checking the exact model.""",
   "Chevrolet Silverado 1500", "CHECK 3, 4 AND 5")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we just walked through. The link is in the description and in the pinned comment. If you want to know what it really costs to own a new truck for five years, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Tariffs added thirty billion": "Intro", "First, the industry numbers": "The industry numbers", "Number one": "1. Chevrolet Silverado",
      "Number two": "2. GMC Sierra", "Number three": "3. Ford F-150", "Number four": "4. Ram 1500",
      "Number five": "5. Toyota Tacoma", "Number six": "6. The destination fee", "So what is the final twist": "The verdict",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video05", "length_scale": 1.55,
  "title": "What Tariffs Really Did to Truck Prices (Model by Model)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
