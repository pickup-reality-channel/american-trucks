import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Right now, some dealers are offering zero percent financing for five years on a new Ram fifteen hundred and a Chevy Silverado. A twenty twenty-five Ford Lightning carries eight thousand dollars cash back. A lease ad shows a full-size Chevy for three hundred twenty-nine dollars a month, with almost ten thousand dollars due at signing. The deals are out there in late twenty twenty-six. The question is whether you know how to get them.""",
   "Ram 1500 dealership", "0% FOR 60 MONTHS. $8,000 CASH BACK")
sc("""This is how to negotiate a new truck price, step by step, using real numbers from twenty twenty-six. Eight steps, from the research you do at home to the moment you sign. Each step has a twist that most buyers miss. Follow them in order, and you can save thousands of dollars on your next truck.""",
   "Chevrolet Silverado dealership", "8 STEPS TO NEGOTIATE")
sc("""Every number in this video comes from a published source, listed in the description. Deals change every month and vary by region, so always confirm with your local dealer. This is general information, not financial advice. If we could not confirm a figure, we left it out. Step one starts before you ever leave the house.""",
   "pickup truck research laptop", "EVERY NUMBER IS SOURCED")

# ---------- STEP 1 ----------
sc("""Step one: know what people really pay. The sticker price is the starting point, not the answer. According to Kelley Blue Book data from Cox Automotive, the average transaction price for a full-size pickup in September twenty twenty-six was sixty-seven thousand, five hundred seventy-three dollars. That average tells you what buyers actually paid across all trims, not what a window sticker says.""",
   "pickup truck window sticker", "1. KNOW WHAT PEOPLE PAY")
sc("""For your exact truck, look up recent selling prices and current offers in your area using pricing tools and deal trackers. According to CarEdge's truck deals page, updated in October twenty twenty-six, one Ram fifteen hundred offer note mentioned a national standalone discount of about twelve percent. When you know that kind of number, a dealer offering two percent off does not look generous anymore.""",
   "Ram 1500 Laramie", "RAM 1500: ~12% DISCOUNT NOTED")
sc("""Also decide exactly what you want before you shop. The cab, the bed length, the engine, two or four-wheel drive, and the trim. Write it down. When you know your exact truck, you can compare quotes fairly, and you are less likely to be talked into a higher trim with features you did not plan to pay for.""",
   "pickup truck configurator", "KNOW YOUR EXACT TRUCK")
sc("""Here is the twist. The best price is not always on the most popular truck. Trucks with lots of inventory on dealer lots usually have bigger discounts. Trucks that are hard to find, like a new performance model, usually have none. Before you fall in love with one truck, check two or three similar ones, because the deal might decide which one you buy.""",
   "pickup trucks dealer lot", "TWIST: INVENTORY DECIDES THE DEAL")

# ---------- STEP 2 ----------
sc("""And look at the brand averages too. According to the same Kelley Blue Book data, in September twenty twenty-six Ram had the highest average transaction price of the big truck brands, at sixty-eight thousand, three hundred fifty-one dollars, up four point six percent, while Chevrolet averaged forty-nine thousand, four hundred sixty-five across all its vehicles. Rising averages can mean fewer discounts. Falling averages can mean more room to negotiate.""",
   "Ram 1500 Chevrolet Silverado", "BRAND AVERAGES MOVE")
sc("""Step two: pick the right time. Timing can matter as much as negotiating skill. In the fall, dealers are selling the new model year while they still have leftover trucks from the previous year. Those leftovers often carry extra incentives, because the dealer needs the space and the manufacturer wants them gone.""",
   "Ford F-150 dealership lot", "2. PICK THE RIGHT TIME")
sc("""You can see it in the October twenty twenty-six offers listed by CarEdge. A twenty twenty-five Ford F-one-fifty Lightning had eight thousand dollars cash back. A twenty twenty-five Toyota Tundra had five thousand dollars cash back. A twenty twenty-five Ford Ranger had zero percent financing for sixty months. These are last year's trucks, brand new, never titled, with real money on the hood.""",
   "Toyota Tundra", "2025 TUNDRA: $5,000 CASH BACK")
sc("""Here is the twist. A leftover truck is new, but it is one model year older on paper, which can mean slightly lower resale value later. If you plan to keep the truck for many years, that difference shrinks to almost nothing. If you trade every three years, it matters more. Do the math against the size of the discount.""",
   "pickup truck new old model year", "LEFTOVER = NEW, BUT OLDER ON PAPER")
sc("""There is a second timing trick: the outgoing model. When a truck is about to be redesigned, the old version often gets big incentives in its final months. The new version will have updates, but the old one is usually a proven design with known problems already fixed. For some buyers, the last year of a generation is the smartest buy of all.""",
   "pickup truck last model year", "THE LAST YEAR OF A GENERATION")
sc("""The end of the month, the end of the quarter and the end of the year can also help, because dealers and salespeople often have sales targets. Bad weather days and weekday mornings can mean a quieter showroom and more attention. None of these are guaranteed, but every edge helps when the price is sixty thousand dollars or more.""",
   "calendar end of month", "MONTH-END, QUARTER-END, YEAR-END")

# ---------- STEP 3 ----------
sc("""Step three: get your financing first. Before you visit the dealer, get a pre-approved loan from your bank or a credit union. According to Experian, the average new vehicle loan rate in the second quarter of twenty twenty-six was six point three five percent. If your pre-approval beats that, you are in a strong position. If the dealer can beat your pre-approval, even better.""",
   "credit union loan", "3. GET PRE-APPROVED FIRST")
sc("""Why does this matter so much? Because the dealer earns money on financing too. A buyer who arrives without a loan offer has no way to know whether the dealer's rate is good. A buyer with a pre-approval has a benchmark. The dealer must match or beat it to win the financing, and that competition can lower your rate.""",
   "bank loan approval", "A BENCHMARK RATE")
sc("""Now look at the special financing offers. According to CarEdge in October twenty twenty-six, the twenty twenty-six Ram fifteen hundred and the twenty twenty-six Chevrolet Silverado fifteen hundred had zero percent financing for sixty months, as did the twenty twenty-six Nissan Frontier. Zero percent on a fifty thousand dollar loan saves thousands in interest compared with an average rate.""",
   "Chevrolet Silverado 1500", "SILVERADO & RAM: 0% FOR 60 MONTHS")
sc("""But here is the twist. Zero percent offers often replace cash rebates. You may have to choose one or the other. If a truck offers zero percent or a few thousand dollars cash back, compare both using your own pre-approved loan rate. Sometimes the cash is worth more. Zero percent also usually requires excellent credit, so not every buyer qualifies.""",
   "loan calculator", "0% OR CASH? DO THE MATH")
sc("""And remember the new tax rule. According to a January twenty twenty-six report on the Treasury rollout, eligible buyers can deduct up to ten thousand dollars a year in auto loan interest on new vehicles with final assembly in the U S, bought for personal use, from twenty twenty-five through twenty twenty-eight. It has income limits. If you qualify, it changes the math on financing versus paying cash, so ask a tax professional.""",
   "tax forms calculator", "UP TO $10K INTEREST DEDUCTION")

# ---------- STEP 4 ----------
sc("""Step four: get quotes from several dealers, in writing. Email or use the online sales departments of at least three dealers. Ask each for the out-the-door price on the exact truck, including all fees, taxes and add-ons. According to CarEdge, buyers who compare out-the-door quotes from multiple dealers save an average of three to five percent off the first quoted price.""",
   "email laptop quotes", "4. 3+ WRITTEN QUOTES")
sc("""How do you ask? Keep it short. Tell the dealer the exact truck you want, by trim and options, or even by stock number. Ask for the total out-the-door price, with every fee listed. Say you are contacting several dealers and will buy from the best offer. Dealers who want your business will answer with a real number. Those who will not give a price by email are telling you something.""",
   "email message", "HOW TO ASK FOR A QUOTE")
sc("""On a sixty-seven thousand dollar truck, three to five percent is about two thousand to three thousand four hundred dollars. That is real money for a few emails. And here is the twist: the dealer with the lowest sticker price is not always the cheapest. Doc fees and add-ons can change the final number by more than one thousand dollars, which is exactly why you ask for the out-the-door price.""",
   "pickup truck dealer price", "LOWEST STICKER ≠ CHEAPEST")
sc("""According to CarEdge's twenty twenty-six report, the average dealer doc fee in America is four hundred seventy-two dollars, but in Florida it averages nine hundred seventy, while California caps it at eighty-five. And according to CarWhere, thirty-four point one percent of buyer quotes included dealer add-ons, averaging one thousand four hundred fifty-four dollars. Those numbers only show up in an out-the-door quote.""",
   "car purchase contract", "DOC FEES + ADD-ONS ADD UP")

# ---------- STEP 5 ----------
sc("""Step five: negotiate the price, and only the price. When you sit down with a dealer, talk about the out-the-door price of the truck first. Do not discuss monthly payments, trade-ins or financing yet. If the salesperson asks what monthly payment you want, say you will discuss financing after you agree on the price.""",
   "truck dealer negotiation", "5. NEGOTIATE ONLY THE PRICE")
sc("""Why? Because a monthly payment can be bent in many directions. According to Edmunds, twenty-five point five percent of new vehicle loans in the third quarter of twenty twenty-six were eighty-four months or longer, and the average new vehicle payment reached a record seven hundred eighty-seven dollars. A longer loan can make an expensive deal look affordable. The price is the only number that cannot hide.""",
   "loan contract", "THE PRICE CAN'T HIDE")
sc("""Expect some common responses. The salesperson might say they need to check with a manager, that the price is already the lowest possible, or that the online quote was a mistake. Stay calm and return to the out-the-door number. Ask what they can do on the total price. You do not need to explain why you want a better deal. The competing quote explains it for you.""",
   "car salesman manager", "COMMON RESPONSES")
sc("""Here is the twist. Use your written quotes. Show the dealer the best out-the-door offer you have and ask if they can beat it. Be polite and specific. A real competing offer is much more powerful than saying you think the price is too high. And if they cannot beat it, you already know where to buy.""",
   "handshake dealership", "USE COMPETING QUOTES")

# ---------- STEP 6 ----------
sc("""Step six: handle the trade-in separately. Before you visit, get offers for your current truck from other dealers or online buyers. Only bring up the trade after the new truck price is agreed in writing. That way, the dealer cannot give you a big discount on one side and take it back on the other.""",
   "used pickup trade in", "6. TRADE-IN SEPARATELY")
sc("""Here is the twist. In many states, trading in at the dealer reduces the sales tax you pay, because tax is charged only on the difference between the new truck and the trade. That can make a slightly lower trade offer from the dealer worth the same as a higher offer from a private buyer. Check your state's rules and compare the real numbers.""",
   "sales tax calculator", "TRADE-IN TAX CREDIT")

# ---------- STEP 7 ----------
sc("""And be honest about your trade's condition. Clean it, gather the service records, and fix small, cheap problems before you get offers. A truck that looks cared for gets better offers. But do not spend big money on repairs right before selling, because you rarely get that money back in a higher trade value.""",
   "used pickup truck clean", "PREP YOUR TRADE")
sc("""Step seven: survive the finance office. After you agree on the price, you will go to the finance office to sign. This is where extended warranties, protection plans and other products are offered. According to CarEdge, protection plans on quotes averaged one thousand four hundred ninety-four dollars, and theft protection averaged seven hundred eighty-two.""",
   "finance office", "7. THE FINANCE OFFICE")
sc("""Here is the twist. Products sold in the finance office are often negotiable, and many can be bought later. Decide before you arrive what you want, if anything. Ask for the price of each item separately. And check the final contract carefully: the price, the interest rate, the loan length and every line item should match what you agreed. Do not sign until they do.""",
   "contract signing", "CHECK EVERY LINE")

# ---------- STEP 8 ----------
sc("""One more finance office tip. Ask for the interest rate as a number, not just the payment. If the rate is higher than your pre-approval, ask them to match it or use your own loan. Dealers can legally offer a rate above the lender's approval and keep part of the difference. Knowing your number stops that from happening quietly.""",
   "interest rate paper", "ASK FOR THE RATE AS A NUMBER")
sc("""Step eight: be ready to walk away. This is the step that makes every other step work. If the numbers are not right, thank the salesperson, leave your contact information, and go. You have other quotes, your own financing and a clear target price. The dealer knows that a buyer who walks away might not come back.""",
   "pickup truck parking lot", "8. BE READY TO WALK AWAY")
sc("""Here is the twist. Many buyers find the best offer comes after they leave, in a phone call or an email the next day. Walking away is not a failure. It is a negotiation tool. The only buyer who cannot walk away is one who has already fallen in love with a single truck on a single lot.""",
   "phone call", "THE BEST OFFER OFTEN COMES LATER")

# ---------- LEASE TRAP ----------
sc("""And walk away early if something feels wrong. If the price changes between the quote and the visit, if add-ons appear that were not mentioned, or if the dealer refuses to show an itemized out-the-door price, those are signs that the deal will not get better. There are many trucks and many dealers. You can always find another.""",
   "dealership exit door", "RED FLAGS TO WALK")
sc("""Now a special warning about lease ads, because they are some of the most confusing numbers in the truck market. According to CarEdge's October twenty twenty-six list, a twenty twenty-six Chevrolet Silverado fifteen hundred lease was advertised at three hundred twenty-nine dollars a month for twenty-four months, with nine thousand six hundred eighty-eight dollars due at signing.""",
   "Chevrolet Silverado 1500", "$329/MONTH + $9,688 DUE")
sc("""Here is how to see the real cost. Spread the due-at-signing amount across the months. Nine thousand six hundred eighty-eight dollars over twenty-four months adds about four hundred dollars a month. So the real cost is closer to seven hundred thirty dollars a month, not three hundred twenty-nine. Compare that with a twenty twenty-six Ram fifteen hundred lease listed at three hundred twenty-five dollars a month with only three hundred twenty-five due at signing, for twenty-seven months.""",
   "Ram 1500 lease", "REAL COST: ~$730/MONTH")
sc("""Two ads with almost the same monthly payment can be very different deals. Always add the due-at-signing amount, divide it by the number of months, and add it to the monthly payment. That simple math reveals which lease is really cheaper, and it takes ten seconds with a phone calculator.""",
   "phone calculator", "DO THE 10-SECOND MATH")

# ---------- PATTERN ----------
sc("""Lease ads also hide other details in the fine print: the annual mileage limit, the fees at the end, and whether the offer requires excellent credit. A Ford Maverick lease listed by CarEdge at three hundred ninety-nine dollars a month for forty-eight months, with one thousand three hundred ninety-eight due, looks very different from a twenty-four month deal. Always compare lease length, mileage and total cost, not just the payment.""",
   "Ford Maverick lease", "READ THE FINE PRINT")
sc("""So what is the pattern behind all eight steps? Control the information. The dealer negotiates every day. You negotiate a truck every few years. The steps in this video close that gap: you know the market price, the incentives, your financing, your trade value, and your walk-away number before you sit down.""",
   "pickup truck buyer dealership", "CONTROL THE INFORMATION")
sc("""And here is the final twist. Negotiating is not about being aggressive. The best negotiators are calm, polite and prepared. They ask clear questions, they compare real offers, and they are willing to leave. In twenty twenty-six, with record payments and long loans, that preparation is worth more than ever.""",
   "friendly handshake car", "CALM, POLITE, PREPARED")

# ---------- CLOSE ----------
sc("""A quick example shows how the steps add up. Imagine a buyer who saves three percent by comparing quotes, avoids one thousand four hundred dollars in add-ons, skips a fifteen hundred dollar protection plan they did not need, and uses a zero percent offer instead of an average rate. On a sixty thousand dollar truck, that can add up to many thousands of dollars, without any yelling or tricks.""",
   "money savings truck", "HOW THE SAVINGS ADD UP")
sc("""And none of these steps require special skills. They require time: an evening of research, a few emails, a call to your bank. That time can easily be worth more per hour than almost any job. Treat buying a truck like the major financial decision it is, and the dealer will treat you like a serious buyer.""",
   "pickup truck research", "TIME IS YOUR LEVERAGE")
sc("""So here is the eight-step checklist one more time. Know what people pay. Pick the right time. Get pre-approved. Get three written out-the-door quotes. Negotiate only the price. Handle the trade-in separately. Check every line in the finance office. And be ready to walk away.""",
   "car buying checklist", "THE 8-STEP CHECKLIST")
sc("""We put the full version, with scripts for what to say and the numbers to compare, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, about why truck insurance costs so much. And tell us in the comments: what is the best truck deal you ever got? Thanks for watching.""",
   "pickup truck dealership", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Right now, some dealers": "Intro", "Step one": "1. Know what people really pay", "Step two": "2. Pick the right time",
      "Step three": "3. Get your financing first", "Step four": "4. Get written quotes", "Step five": "5. Negotiate only the price",
      "Step six": "6. Trade-in separately", "Step seven": "7. The finance office", "Step eight": "8. Be ready to walk away",
      "Now a special warning about lease": "The lease ad trap", "So here is the eight-step": "The checklist"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video53", "length_scale": 1.5,
  "title": "How to Negotiate a New Truck Price in 2026 (8 Steps Dealers Hope You Skip)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
