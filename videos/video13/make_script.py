import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Tesla planned to build two hundred fifty thousand Cybertrucks a year. In the best quarter of twenty twenty-six, the best estimate says it sold about eight thousand. That is thirteen percent of the plan, and the real number may be lower. The most famous truck in America has a numbers problem, and some of the numbers are stranger than you think. Here are seven of them, with the sources.""",
   "Tesla Cybertruck", "THE CYBERTRUCK NUMBERS PROBLEM")

# ---------- COLD OPEN ----------
sc("""When the Cybertruck was unveiled, it looked like nothing else on the road. Stainless steel, sharp angles, a promise of a truck that could do everything. And a demand that seemed enormous. But Tesla does not report Cybertruck sales separately. It groups them under a line called other models. So everything we know about the numbers comes from estimates, registrations, and a few carefully chosen statements.""",
   "Tesla Cybertruck stainless steel", "TESLA DOES NOT REPORT CYBERTRUCK SALES")
sc("""That is the first thing to say, and we will keep saying it. Almost every number in this video is an estimate. We will tell you who made it, and what it covers. We used Electrek, InsideEVs, Cox Automotive data, S and P Global Mobility registrations as reported by Electrek, and Pickup Truck Talk. And where the estimates disagree, we show both. Every source is listed in the description.""",
   "Tesla Cybertruck pickup", "ALMOST EVERY NUMBER IS AN ESTIMATE")
sc("""There is a twist in each of the seven numbers. One of them is about trucks that were registered, but not sold to customers in the usual way. One is about a price that went up. One is about a plan that is twice the installed capacity. And one is about a category that Tesla itself no longer fills. Stay with me, because the last number is the one that matters for you.""",
   "Tesla Cybertruck front", "SEVEN NUMBERS. SEVEN TWISTS.")

# ---------- NUMBER 1 ----------
sc("""Number one is two hundred fifty thousand, the planned volume. According to Electrek, Tesla's planned Cybertruck volume is two hundred fifty thousand a year. The twist is that Tesla's latest shareholder letter lists more than one hundred twenty-five thousand units of installed capacity, which is half of the plan. So the factory, as it stands, is not built for the number in the plan. And Pickup Truck Talk wrote that Musk once mentioned a target of half a million a year.""",
   "Tesla Gigafactory Texas", "PLAN: 250,000. CAPACITY: 125,000+")

# ---------- NUMBER 2 ----------
sc("""Number two is thirty-nine thousand, the first full year. According to InsideEVs, citing Cox Automotive, Tesla sold about thirty-nine thousand Cybertrucks in the United States in twenty twenty-four. That is the biggest year the truck has had. And it is about sixteen percent of the plan, in the year when the truck was new and the waiting list was at its fullest.""",
   "Tesla Cybertruck pickup truck", "2024: ~39,000 (COX)")

# ---------- NUMBER 3 ----------
sc("""Number three is twenty thousand, the second year. InsideEVs, citing Cox, put the twenty twenty-five total at about twenty thousand, two hundred. That is a fall of about forty-eight percent. Electrek estimated about twenty-one thousand, five hundred, and GM Authority wrote that industry estimates were closer to twenty-five thousand. The estimates differ, but they all point to the same shape. The second year was much smaller than the first.""",
   "Tesla Cybertruck", "2025: ~20,200 TO ~25,000")
sc("""And here is the twist inside the year. Cox counted five thousand, three hundred eighty-five Cybertrucks in the third quarter of twenty twenty-five, and four thousand, one hundred forty in the fourth. But S and P Global Mobility counted seven thousand and seventy-one Cybertruck registrations in the fourth quarter, and one thousand, three hundred thirty-nine of them went to SpaceX and Musk's other companies. Registrations and sales are not the same, and some of the trucks went to the company's own family.""",
   "Tesla Cybertruck SpaceX", "Q4 2025: 1,339 REGISTERED TO MUSK COMPANIES")

# ---------- NUMBER 4 ----------
sc("""Number four is thirty-five hundred, the first quarter of twenty twenty-six. Cox Automotive data, posted by Sawyer Merritt, shows the Cybertruck at three thousand, five hundred nineteen, down forty-five percent from a year earlier. It was still the best-selling electric pickup that quarter, ahead of the Lightning at two thousand and sixty, the Rivian R1T at sixteen hundred fifty-eight, and the Silverado EV at fourteen hundred and six.""",
   "Tesla Cybertruck pickup", "Q1 2026: 3,519 (-45%)")
sc("""The twist is the second quarter. Cox counted three thousand, seven hundred forty-four, which is only slightly higher. And again the Cybertruck led the electric pickups, ahead of the Lightning at two thousand, four hundred twenty-one, the Silverado EV at two thousand, two hundred sixty-six, and the Rivian at twelve hundred nineteen. So the truck that is called a failure by some is still the leader of its own category. Its category is just very small.""",
   "Tesla Cybertruck truck", "Q2 2026: 3,744, STILL #1 AMONG EV TRUCKS")

# ---------- NUMBER 5 ----------
sc("""Number five is seventy-four thousand, nine hundred ninety, the price. According to Electrek, a cheaper dual-motor Cybertruck began reaching customers in late June of twenty twenty-six, and Tesla raised its price by five thousand dollars in August. It now starts at seventy-four thousand, nine hundred ninety dollars. And back in September of twenty twenty-five, Tesla had dropped the cheapest trim.""",
   "Tesla Cybertruck dual motor", "PRICE: $74,990 AFTER +$5,000")
sc("""The twist is what the price tells you. A company that has too many trucks and not enough buyers usually cuts prices. Tesla raised this one. That could mean demand improved, it could mean costs rose, or it could mean the company wants a higher profit on each truck. The articles we read do not say which. What we can say is that the Cybertruck at seventy-five thousand dollars costs more than the average full-size pickup, which sold for sixty-seven thousand, four hundred forty-six dollars in August.""",
   "Tesla Cybertruck", "AVERAGE FULL-SIZE: $67,446")

# ---------- NUMBER 6 ----------
sc("""Number six is eight thousand, two hundred ninety-five, the other models line. Tesla reported that its other models deliveries in the third quarter of twenty twenty-six were eight thousand, two hundred ninety-five, down forty-eight percent from fifteen thousand, nine hundred thirty-three a year earlier. Electrek says that is the lowest since the second quarter of twenty twenty-one. And production was seven thousand and four, down forty percent.""",
   "Tesla Cybertruck Model S", "OTHER MODELS: 8,295 (-48%)")
sc("""That line includes the Cybertruck, the Semi, and the last Model S and Model X cars. The Model S and X production ended in April twenty twenty-six, with about six hundred cars left in inventory. Electrek estimates the Cybertruck made up seven to eight thousand of the third quarter, a pace of about thirty thousand a year. That is thirteen percent of the plan. But Pickup Truck Talk's estimate is lower, about thirty-seven hundred.""",
   "Tesla Cybertruck pickup", "CYBERTRUCK Q3: 7,000-8,000 (ELECTREK)")
sc("""Why do the two estimates differ so much? Electrek estimates deliveries using Tesla's global other models total as a ceiling. Pickup Truck Talk's article calls its number a low-confidence estimate, based on the second quarter's run rate. Cox counts only the United States. We do not know which is closer to the truth, and Tesla does not tell. So we show both, and we say that the real number is somewhere between about thirty-seven hundred and eight thousand.""",
   "Tesla Cybertruck front", "TWO ESTIMATES: ~3,700 AND 7,000-8,000")

# ---------- NUMBER 7 ----------
sc("""Number seven is several thousand, the unsold trucks. In a July lawsuit against its casting supplier, Tesla said it had several thousand Cybertrucks already committed to customers. That is one of the very few official statements about the Cybertruck, and it is a vague one. Several thousand could be three thousand or nine. It does not tell us how many trucks are in inventory, or how many orders there are.""",
   "Tesla Cybertruck delivery", "TESLA: 'SEVERAL THOUSAND COMMITTED'")
sc("""And the twist is what that means for a buyer. A truck with few sales and a company that does not publish the numbers is harder to judge. You do not know how big the market for used ones will be, or how many dealers can service it. We cannot give you a prediction, because none of the sources do. What we can say is that this is a different situation from a Silverado, with hundreds of thousands sold, or a Maverick, with over a hundred thousand.""",
   "Tesla Cybertruck pickup truck", "A TRUCK WITH FEW SALES AND NO DATA")


# ---------- TIMELINE AND PERCENT OF PLAN ----------
sc("""Let's put the whole story on one timeline, using the percent of the plan. In twenty twenty-four, about thirty-nine thousand, which is about sixteen percent of two hundred fifty thousand. In twenty twenty-five, about twenty thousand, two hundred, which is about eight percent. In the first quarter of twenty twenty-six, three thousand, five hundred nineteen, which is about one and a half percent of a year of the plan, and if it continued all year, about fourteen thousand.""",
   "Tesla Cybertruck pickup", "PERCENT OF PLAN: 16% TO 8%")
sc("""And in the third quarter, using Electrek's estimate of seven to eight thousand, the pace is about thirty thousand a year, or about twelve to thirteen percent. So the shape is a fall from the first year to the second, a very low first half of twenty twenty-six, and a possible rebound in the third quarter. Whether that rebound is real depends on which estimate you trust, and Tesla will not settle it.""",
   "Tesla Cybertruck", "Q3 2026: ~13% OF PLAN AT THE HIGH END")
sc("""Now compare the Cybertruck with the trucks it was supposed to rival. The Ford F-Series sold five hundred fifty-six thousand, seven hundred thirty-eight through nine months of twenty twenty-six. The Chevrolet Silverado sold four hundred thirteen thousand, three hundred eighty-three. Even the Nissan Frontier, a midsize truck, sold sixty-six thousand, five hundred thirteen. The Cybertruck sold about eleven thousand in nine months on Pickup Truck Talk's estimate, or about fifteen thousand if you add Electrek's third quarter to Cox's first two. Either way, that is less than the Nissan Frontier sold in the third quarter alone, which was twenty-three thousand, four hundred twelve.""",
   "Ford F-150 pickup truck", "FRONTIER: 66,513. CYBERTRUCK: ~11,000.")
sc("""That comparison is not fair in one way, and it is important to say so. The Cybertruck is a very different product, with a price near seventy-five thousand dollars, and it was never going to sell like a Maverick. A truck at that price competes with a small group of buyers. But the plan was two hundred fifty thousand a year, which is the size of a mainstream truck, not a niche one. That is where the gap comes from, and it is a gap between a plan and a market, not between a truck and a truck.""",
   "Tesla Cybertruck", "A NICHE PRICE, A MAINSTREAM PLAN")
sc("""There is also a point about the electric truck rivals that is easy to forget. In the second quarter of twenty twenty-six, the Cybertruck sold more than the Lightning, the Silverado EV and the Rivian R one T. And the Lightning, which Ford stopped building, still sold two thousand, four hundred twenty-one. So demand for electric trucks exists, in the low thousands per truck per quarter. The question for every company is whether that is enough to build a truck for.""",
   "Rivian R1T pickup", "EV TRUCK DEMAND: LOW THOUSANDS PER QUARTER")
sc("""What would change the picture? We do not know, and the sources do not say. Cheaper versions might bring in new buyers, as Tesla tried with the dual-motor truck in June. Gas prices might push buyers toward electric, as Electrek noted for the second half of the year. And the end of the federal tax credit has already removed one source of demand. Those are the forces, and the numbers in the next three quarters will show which one wins.""",
   "Tesla Cybertruck dual motor pickup", "WHAT COULD CHANGE THE NUMBERS")
sc("""For a buyer, the honest summary is this. The Cybertruck is a real truck, with real owners and real sales. It is also a truck from a company that does not report how many it sells, in a market that is shrinking, at a price that rose. If you love the design and you are comfortable with those facts, that is your choice. If you want the lowest risk, a truck with a long record, hundreds of thousands of owners and published numbers is a safer path.""",
   "Tesla Cybertruck stainless steel", "THE HONEST SUMMARY")
sc("""One last point. Reports like this one change every quarter. By the time you watch this video, new numbers may have come out. Check the latest quarter from Cox Automotive, and from Tesla's own delivery report. And remember that an estimate is an estimate, even when it appears in many places. The best habit is to look for the source, and to ask who has the data and who does not.""",
   "Tesla Cybertruck pickup", "ALWAYS CHECK THE SOURCE")

# ---------- THE BIGGER PICTURE ----------
sc("""So what is the Cybertruck problem? It is not that the truck failed to sell at all. Tesla sold tens of thousands in its best year, and it leads the electric pickups every quarter in the data we found. The problem is the gap between the plan and the sales. Two hundred fifty thousand a year was the plan, and about twenty thousand to thirty thousand a year is the reality, depending on whose estimate you use.""",
   "Tesla Cybertruck stainless steel pickup", "THE GAP: 250,000 VS ~20,000-30,000")
sc("""And the problem is the wider electric truck market. The Silverado EV fell forty-three percent through nine months. The Lightning fell seventy-nine. The Hummer EV fell sixty-two. The Cybertruck is not alone, and it is not even the worst. Its number is a symptom of a market that was planned for a subsidy, and that lost the federal tax credit. The truck that looks the most different is in the same trouble as the ones that look like everything else.""",
   "Tesla Cybertruck Ford F-150 Lightning", "SAME MARKET. SAME TROUBLE.")

# ---------- BUYER GUIDE: HOW TO USE THESE NUMBERS ----------
sc("""Before the checklist, let's turn the biggest numbers into something a buyer can use. Three different things have been mixed together in the headlines. A plan is what a company hopes to sell, and for the Cybertruck that was two hundred fifty thousand a year. Capacity is what a factory is able to build, and the shareholder letter lists more than one hundred twenty-five thousand. Sales are what customers actually paid for. When you read a claim about any truck, ask which of the three it is, because mixing them up is the easiest way to end up confused.""",
   "Tesla Cybertruck pickup truck", "PLAN, CAPACITY AND SALES ARE NOT THE SAME")
sc("""Next, registrations and sales. A registration is a record that a truck is on the road under somebody's name. A sale is a customer choosing to buy it. We saw that S and P Global Mobility counted seven thousand and seventy-one registrations in the fourth quarter, while Cox counted four thousand, one hundred forty sales, and one thousand, three hundred thirty-nine of the registrations went to SpaceX and Musk's other companies. The lesson is simple. Compare numbers only when they come from the same source, and always ask who the buyer was.""",
   "Tesla Cybertruck SpaceX", "REGISTRATIONS ARE NOT SALES")
sc("""Now think about the range between the two estimates, about thirty-seven hundred on one side and seven to eight thousand on the other. A buyer should read a wide range like that as a message. It says that nobody outside Tesla really knows. The lower figure is described as a low-confidence estimate, and the higher one uses Tesla's global total as a ceiling. Do not pick the number that supports what you already believe. Hold both in your head, and let the uncertainty be part of your decision.""",
   "Tesla Cybertruck front", "A WIDE RANGE MEANS NOBODY OUTSIDE TESLA KNOWS")
sc("""Then there is the price. The truck now starts at seventy-four thousand, nine hundred ninety dollars after a five thousand dollar increase, and the average full-size pickup sold for sixty-seven thousand, four hundred forty-six. A starting price is not what you pay. Ask for the out-the-door price in writing, with every fee and every option on the exact truck. Ask what day the quote is good for, because this price has moved in both directions in a short time. And if you compare it with another truck, compare the same kind of trim on the same day.""",
   "Tesla Cybertruck dual motor", "ASK FOR THE OUT-THE-DOOR PRICE IN WRITING")
sc("""Here is how to verify the truck itself. Take the vehicle identification number, the VIN, and run it through the official recall lookup before you pay. Ask for the service records, and ask for the warranty terms in writing, not in conversation. Then find out where the nearest service center is, and how long the wait is for an appointment. With a truck that has few sales and little published data, these checks matter more, because there are fewer owners who have already found the problems for you.""",
   "Tesla Cybertruck stainless steel", "CHECK THE VIN, THE RECALLS AND THE SERVICE")
sc("""Who is this truck for, and who should wait? It suits a buyer who loves the design, who has the budget for a price near seventy-five thousand dollars, and who is comfortable owning something unusual from a company that does not report its numbers. It may not suit a buyer who needs a proven record, who wants easy resale, or who depends on a nearby service network. If that second description sounds like you, waiting for the next quarter's numbers costs very little, and it may tell you a lot.""",
   "Tesla Cybertruck pickup", "WHO IT SUITS, AND WHO SHOULD WAIT")
sc("""Finally, the mistakes we see most often. Buying because of a headline, either the one that says the truck failed or the one that says it leads. Forgetting that leading a small category is not the same as a large market. Paying the starting price without reading the fees. Skipping the recall check because the truck is new. And assuming that a company's confidence is the same as a company's data. A calm buyer with a written quote and a checked VIN is better protected than any prediction, ours included.""",
   "Tesla Cybertruck", "COMMON BUYER MISTAKES")

sc("""To put all of this together, imagine you are standing in a showroom, or reading an online listing. Here is a short routine that works for any low-volume truck. First, write down the out-the-door price, and compare it with the average full-size pickup at sixty-seven thousand, four hundred forty-six dollars, so you know what the premium is. Second, ask for the warranty and service terms in writing. Third, run the VIN. Fourth, ask yourself which numbers you trust, and who published them. If you can answer all four calmly, you are ready to decide. If you cannot, the truck will still be there next month.""",
   "Tesla Cybertruck pickup", "A FOUR-STEP SHOWROOM ROUTINE")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a Cybertruck, or any low-volume truck, in twenty twenty-seven? First, the real price, with every fee, since the starting price has changed in both directions. Second, the warranty and the service network near you. Third, the resale value, which the sources we found do not give. And fourth, the company's honesty about its numbers. A company that tells you how many it sells is easier to trust.""",
   "Tesla Cybertruck", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Tesla planned to build": "Intro", "Number one": "1. 250,000: the plan", "Number two": "2. 39,000: the first full year",
      "Number three": "3. 20,000: the second year", "Number four": "4. 3,519: the first quarter of 2026",
      "Number five": "5. $74,990: the price", "Number six": "6. 8,295: the other models line",
      "Number seven": "7. Several thousand: the committed trucks", "So what is the Cybertruck problem": "The bigger picture",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video13", "length_scale": 1.55,
  "title": "The Cybertruck Problem: 250,000 Promised, This Is What Sold (2026)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
