import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One in three new vehicle quotes in America now includes dealer add-ons that the buyer did not ask for, averaging about one thousand four hundred fifty dollars. Ram buyers saw the highest, at one thousand nine hundred. In one state, the average document fee is almost one thousand dollars, while in another it is eighty-five. And a federal rule that was supposed to stop many of these tricks was thrown out by a court. Here are seven dealer tricks to watch for when you buy a truck.""",
   "pickup truck dealership", "7 DEALER TRICKS")
sc("""None of these tricks are illegal on their own. Most dealers are honest businesses trying to make a profit. But the truck business has some of the biggest price tags in retail, and a few small moves in the finance office can add thousands of dollars to your deal. By the end of this video, you will know every one of them, and the one question that beats them all.""",
   "truck dealership finance office", "THOUSANDS HIDDEN IN SMALL MOVES")
sc("""Every number in this video comes from a published source, listed in the description. This is general information, not legal or financial advice. If we could not confirm a figure, we left it out. Let's start with the trick that costs truck buyers the most money.""",
   "Ford F-150 dealership", "EVERY NUMBER IS SOURCED")

# ---------- 1. MONTHLY PAYMENT ----------
sc("""Trick number one: what monthly payment are you looking for? It sounds like a friendly question. It is the most powerful question in the dealership. Once a salesperson knows your target payment, they can hit it in many ways: a longer loan, a smaller trade-in value, a higher interest rate, or extra products folded into the loan. The payment looks right. The deal might not be.""",
   "car salesman customer", "1. 'WHAT PAYMENT DO YOU WANT?'")
sc("""Look at how far loans have stretched. According to Edmunds, twenty-five point five percent of new vehicle loans in the third quarter of twenty twenty-six had terms of eighty-four months or longer, up from twenty-one point eight percent a year earlier. The average new vehicle payment hit a record seven hundred eighty-seven dollars, and the average buyer will pay nine thousand nine hundred thirty-eight dollars in total interest.""",
   "loan contract signing", "84+ MONTH LOANS: 25.5%")
sc("""Here is the twist. Stretching a loan from five years to seven makes the payment smaller, but it adds two more years of interest and keeps you owing more than the truck is worth for longer. Edmunds analyst Ivan Drury said a longer loan term may be the only way for some buyers to get the vehicle they need. That is exactly why it is the first tool a dealer reaches for.""",
   "pickup truck price", "SMALLER PAYMENT, BIGGER COST")
sc("""There is another version of this trick. The dealer offers two choices: a big cash rebate, or a very low interest rate, but not both. The low rate sounds amazing, but if you can get a reasonable loan from your own bank or credit union, taking the rebate can save more money. Always do the math on both options with the same loan length.""",
   "bank credit union loan", "REBATE OR LOW RATE?")
sc("""How to beat it: never answer the payment question first. Say you are focused on the out-the-door price, the total amount you will pay including taxes and fees. Negotiate that number first. Then, and only then, talk about financing. If the dealer insists on talking payments, that tells you something about the deal.""",
   "handshake dealership", "BEAT IT: OUT-THE-DOOR PRICE")

# ---------- 2. ADD-ONS ----------
sc("""Trick number two: the add-ons that are already on the truck. Window tint, door edge guards, wheel locks, nitrogen in the tires, paint protection. Often they are installed before you ever see the truck, and they appear on a separate sticker next to the factory window sticker. According to CarWhere, which studied five thousand two hundred eleven real buyer quotes through June twenty twenty-six, thirty-four point one percent included dealer-installed add-ons.""",
   "pickup truck window sticker", "2. PRE-INSTALLED ADD-ONS")
sc("""And the average add-on total was one thousand four hundred fifty-four dollars per affected quote. By brand, Ford quotes with add-ons averaged one thousand two hundred thirty-five dollars. Chevrolet, one thousand four hundred forty-three. G M C, one thousand four hundred forty-one. Toyota, one thousand six hundred thirty-seven. And Ram was the highest of the truck brands, at one thousand nine hundred dollars.""",
   "Ram 1500 dealership", "RAM ADD-ONS: AVG $1,900")
sc("""Here is what those items cost, according to CarWhere. Window tint averaged five hundred four dollars. Door edge guards, two hundred twenty-four. Wheel locks, one hundred eighty-eight. And general accessories, one thousand three hundred eighty-six. Some of these items cost the dealer very little. A set of wheel locks can be bought at an auto parts store for a fraction of that.""",
   "wheel locks", "WHEEL LOCKS: $188 AVG")
sc("""Some add-ons are dressed up with impressive names. Nitrogen-filled tires, for example, are often sold as a premium feature, even though the air we breathe is already mostly nitrogen. Paint and fabric protection packages can cost hundreds of dollars for products similar to what you can buy and apply yourself. The name does not tell you the value.""",
   "car tires nitrogen", "IMPRESSIVE NAMES, SMALL VALUE")
sc("""The twist? Toyota had the highest share of quotes with add-ons, at thirty-seven point seven percent. The brands with the most in-demand trucks often see the most add-ons, because dealers know buyers want the truck badly. How to beat it: ask for the price without add-ons, in writing. If the dealer says they are already installed, ask them to remove the charge, or find a dealer who does not add them.""",
   "Toyota Tacoma dealership", "TOYOTA: 37.7% OF QUOTES")

# ---------- 3. DOC FEE ----------
sc("""Trick number three: the document fee. It is the charge for processing the paperwork, and it can be very different from one dealer to the next. According to CarEdge's State of Dealer Fees twenty twenty-six report, which covered more than twenty-four thousand dealers, the average doc fee in America is four hundred seventy-two dollars.""",
   "car dealer paperwork", "3. DOC FEE: AVG $472")
sc("""But the range is enormous. According to CarEdge, Florida had the highest average, at nine hundred seventy dollars, followed by Virginia at eight hundred forty-one. California had the lowest, at eighty-five, followed by Arkansas at one hundred thirty-one. The highest single doc fee CarEdge found was one thousand eight hundred fifty dollars.""",
   "Florida car dealership", "FLORIDA $970 VS CALIFORNIA $85")
sc("""Here is the twist. Paperwork costs about the same everywhere. The difference is the law. According to CarEdge, nineteen states enforce caps on doc fees, including California at eighty-five dollars, Texas at two hundred twenty-five, and Ohio at three hundred ninety-eight. In states without caps, the fee is whatever the dealer decides. Many dealers say the fee is not negotiable. But the truck price is, so you can ask for a discount that offsets it.""",
   "Texas car dealership", "19 STATES CAP DOC FEES")

# ---------- 4. MARKUP ----------
sc("""And here is a detail many buyers miss. The doc fee is often printed on the paperwork as if it were a government fee, next to taxes and registration. It is not. Taxes and registration go to the state. The doc fee goes to the dealer. Ask the dealer to show you which fees are government fees and which are dealer fees.""",
   "car purchase contract fees", "DEALER FEE OR GOVERNMENT FEE?")
sc("""Trick number four: the market adjustment. When a truck is new, rare or popular, some dealers add a charge above the sticker price, often called a market adjustment or additional dealer markup. It is pure profit, and it shows up most often on hot performance trucks and limited editions.""",
   "Ram TRX", "4. THE MARKET ADJUSTMENT")
sc("""Here is a current example. In January twenty twenty-six, Ram announced the return of the T R X for the twenty twenty-seven model year, with seven hundred seventy-seven horsepower. According to Pickup Truck Talk, its price lands just shy of one hundred thousand dollars before destination fees and the likely dealer markups. When a truck review warns you about markups in the same sentence as the price, you know it is a real risk.""",
   "Ram TRX pickup", "2027 TRX: 'LIKELY DEALER MARKUPS'")
sc("""The twist is that markups usually fade. When a hot truck first launches, supply is short. A few months later, more trucks arrive, early buyers are served, and the markups shrink or disappear. How to beat it: be patient, contact several dealers, and order from the factory at sticker price if a dealer allows it. The buyer who waits often pays thousands less.""",
   "pickup trucks dealer lot", "MARKUPS FADE WITH TIME")

# ---------- 5. TRADE-IN ----------
sc("""There is also a softer version of the markup: limited inventory. A dealer may only have the high trim with every option in stock, and suggest that the cheaper version will take months. Sometimes that is true. Sometimes the dealer simply makes more on the expensive truck. Ask other dealers, and ask about factory orders, before you accept a truck with options you do not need.""",
   "pickup trucks inventory", "ONLY THE LOADED ONE IN STOCK")
sc("""Trick number five: the trade-in shuffle. You get a great discount on the new truck, but a low offer for your old one. Or a great offer for your trade, but no discount on the new truck. The dealer moves money between the two numbers so that the total profit stays the same. On a worksheet with several numbers at once, it is easy to miss.""",
   "used pickup trade in", "5. THE TRADE-IN SHUFFLE")
sc("""Here is the twist. Your trade-in is a separate deal, and it can be priced separately. Before you visit the dealer, get offers for your current truck from other sources, such as other dealers or online buyers. Then you know what it is really worth. If the dealer's trade-in offer is lower, you can sell it elsewhere, or ask them to match.""",
   "used pickup truck for sale", "GET TRADE OFFERS FIRST")
sc("""A good habit is to negotiate the new truck price first, as if you had no trade-in at all. Once that price is agreed in writing, bring up the trade. That way, the dealer cannot hide a low trade value inside a big discount, or the other way around. Each number has to stand on its own.""",
   "truck dealer handshake", "PRICE FIRST, TRADE SECOND")
sc("""And watch for negative equity. If you owe more on your current truck than it is worth, some dealers will roll that debt into the new loan. The new truck then starts its life already upside down. With seven-year loans becoming common, according to Edmunds, this cycle can follow buyers from truck to truck. Always ask to see exactly how much of the old loan is being added.""",
   "car loan debt", "WATCH FOR ROLLED-IN DEBT")

# ---------- 6. F&I ----------
sc("""Trick number six: the finance office menu. After you agree on a price, you are taken to a separate office to sign the paperwork. This is where extra products are offered: extended warranties, protection plans, tire and wheel coverage, theft protection and more. Some can be useful. Many are expensive, and they are added to your loan.""",
   "finance office paperwork", "6. THE FINANCE OFFICE MENU")
sc("""According to CarEdge, among the most common add-ons on quotes were protection plans, averaging one thousand four hundred ninety-four dollars, and theft protection, averaging seven hundred eighty-two dollars. Financed over seven years, every dollar of those products also collects interest. A one thousand five hundred dollar plan can cost much more by the time the loan is paid.""",
   "extended warranty contract", "PROTECTION PLAN: AVG $1,494")
sc("""Another finance office move is the interest rate markup. The lender may approve you at one rate, and the dealer can offer you a slightly higher rate and keep part of the difference. It is a common, legal practice. That is why getting a pre-approved loan from your own bank or credit union before you visit gives you a number to compare. If the dealer can beat it, great. If not, you use your own loan.""",
   "bank pre-approval", "THE RATE MARKUP")
sc("""Here is the twist. Many of these products are negotiable, and many can be bought later, often from other providers. You do not have to decide in the finance office, under pressure, after hours at the dealer. How to beat it: decide before you go which products you want, if any. Ask for the price of each product separately, and do not let them be bundled into the monthly payment.""",
   "car contract signing", "YOU CAN DECIDE LATER")

# ---------- 7. URGENCY ----------
sc("""Trick number seven: urgency. This price is only good today. Another buyer is coming to look at this truck this afternoon. My manager will only approve this once. Urgency is designed to stop you from comparing. A buyer who leaves to think it over might find a better deal somewhere else, and the dealer knows it.""",
   "car salesman", "7. 'THIS PRICE IS ONLY FOR TODAY'")
sc("""Here is the twist. Comparing pays. According to CarEdge, buyers who compare out-the-door quotes from multiple dealers save an average of three to five percent off the first quoted price. On a truck that costs sixty-seven thousand dollars, the average full-size pickup price in September twenty twenty-six according to Kelley Blue Book, five percent is more than three thousand dollars.""",
   "pickup trucks dealer comparison", "COMPARING SAVES 3-5%")
sc("""Urgency also shows up at the end of the month or the end of the year. Dealers often have sales targets, and they may genuinely offer better deals to hit them. That kind of urgency can work in your favor. The trick is knowing the difference between real deadlines that help you and fake deadlines designed to stop you from shopping around.""",
   "calendar end of month", "GOOD URGENCY VS FAKE URGENCY")
sc("""How to beat it: get written quotes from at least three dealers, by email if possible. A real price will still exist tomorrow. If the deal truly disappears overnight, it was probably not as good as it sounded. There are many trucks and many dealers. There is almost never only one.""",
   "email quote", "BEAT IT: 3 WRITTEN QUOTES")

# ---------- THE RULE THAT DIED ----------
sc("""Now the twist that affects every buyer in America. In twenty twenty-four, the Federal Trade Commission created a new rule, called the CARS Rule, to fight many of these practices. According to ConsumerAffairs, it would have required dealers to disclose the total vehicle cost upfront, state that add-ons are optional, and get consumer consent for extra fees.""",
   "Federal Trade Commission building", "THE FTC CARS RULE")
sc("""It never took effect. On January twenty-seventh, twenty twenty-five, the Fifth Circuit Court of Appeals vacated the rule in a two to one decision, after a challenge by the National Automobile Dealers Association and the Texas Automobile Dealers Association. The court said the F T C violated its own regulations by skipping a required early step in the rulemaking process.""",
   "courthouse", "JAN 27, 2025: RULE THROWN OUT")
sc("""According to ConsumerAffairs, dealers are still at risk of F T C scrutiny for deceptive practices, and the agency could revisit the rule. But for now, the protections it promised are not law. That means the job of spotting add-ons, fees and pressure tactics still falls on you, the buyer. This video, in a way, is the rule that never arrived.""",
   "pickup truck buyer", "THE JOB IS STILL YOURS")

# ---------- PATTERN ----------
sc("""And remember that good dealers exist. Many dealers publish clear prices, skip add-ons and charge reasonable fees. According to CarEdge, fifty-six percent of the dealers in its twenty twenty-six report earned an A grade for their fees. Your goal is not to fight every dealer. It is to find the honest ones, and the tools in this video make them easy to spot.""",
   "friendly car dealership", "GOOD DEALERS EXIST")
sc("""Here is a bonus trick, because there is always one more. The spot delivery. You sign the papers and drive the truck home before the financing is final. Days later, the dealer calls to say the loan was not approved at that rate, and asks you to come back and sign a new contract at a higher one. Before you drive away, make sure the financing is fully approved, in writing.""",
   "pickup truck driving away dealership", "BONUS: THE SPOT DELIVERY")
sc("""And a second bonus: the payment packing. A salesperson quotes a monthly payment that already includes extra products, without saying so. When you agree to the payment, you have unknowingly agreed to the products. The fix is the same as always. Ask for an itemized breakdown of the price, the fees, the products and the interest rate before you agree to any payment.""",
   "itemized receipt", "BONUS: PAYMENT PACKING")
sc("""What can you do if something goes wrong after you buy? Keep copies of every document and every email. If you believe a dealer misled you, you can contact the dealer's management, the manufacturer's customer service, your state attorney general or the consumer protection office in your state. Documentation is what makes a complaint work.""",
   "documents folder", "KEEP EVERY DOCUMENT")
sc("""And remember that the paperwork rules everything. Whatever the salesperson promised, the signed contract is what counts. If a promise matters, like free maintenance, a second key or a repair, make sure it is written into the contract or a signed form called a due bill. A verbal promise disappears the moment you drive off the lot.""",
   "contract signing pen", "GET PROMISES IN WRITING")
sc("""So what do all seven tricks have in common? They move your attention away from the total price. The monthly payment hides the loan length. The add-on sticker hides extra profit. The doc fee hides in the paperwork. The trade-in shuffle hides in the math. And urgency hides the competition. Every trick works by making the total harder to see.""",
   "pickup truck deal paperwork", "EVERY TRICK HIDES THE TOTAL")
sc("""And that is why one question beats all seven: what is my out-the-door price? Ask it in writing, from several dealers, before you talk about payments, trade-ins or extras. Everything else is detail. The buyer who controls the total controls the deal.""",
   "Ford F-150 Chevrolet Silverado dealer", "ONE QUESTION BEATS THEM ALL")

sc("""And a final note on timing your visit. Dealers are busiest on weekends, when salespeople juggle several buyers and decisions are rushed. A weekday visit, with an appointment and your written quotes in hand, usually means a calmer conversation and more attention. A calm buyer makes better decisions.""",
   "car dealership weekday", "VISIT ON A WEEKDAY")
sc("""Bring a friend if you can. A second person can notice things you miss, ask questions you forget, and remind you of your limits when the pressure rises. Many dealer tricks work because buyers are tired and alone at the end of a long day. Do not give them that advantage.""",
   "two people car dealership", "BRING A FRIEND")

# ---------- CLOSE ----------
sc("""One more tool that works: walk away politely. Thank the salesperson, leave your phone number, and go. Many buyers find that the best offer arrives after they leave, by phone or email, once the dealer realizes the sale might be lost. Walking away is not rude. It is the strongest negotiating move a buyer has.""",
   "pickup truck parking lot", "THE POWER OF WALKING AWAY")
sc("""And bring the numbers with you. Write down the out-the-door quotes from other dealers, the trade-in offers you received, and your pre-approved loan rate. When a buyer shows up with real numbers, the conversation changes. It stops being about what you might accept, and starts being about whether the dealer can beat a real offer.""",
   "notebook numbers", "BRING YOUR NUMBERS")
sc("""So here is your checklist for twenty twenty-seven. First, ask for the out-the-door price in writing. Second, ask for the price without dealer add-ons. Third, know your state's doc fee rules. Fourth, get your trade-in valued elsewhere first. And fifth, decide on any extra products before you enter the finance office, and never let them be bundled into the payment.""",
   "car buying checklist", "YOUR 5-STEP CHECKLIST")
sc("""We put the full version, with the exact questions to ask and the numbers to compare, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, where we go step by step through how to negotiate a new truck price. And tell us in the comments: which dealer trick have you seen? Thanks for watching.""",
   "pickup truck dealership", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One in three new vehicle quotes": "Intro", "Trick number one": "1. The monthly payment question",
      "Trick number two": "2. Pre-installed add-ons", "Trick number three": "3. The doc fee", "Trick number four": "4. The market adjustment",
      "Trick number five": "5. The trade-in shuffle", "Trick number six": "6. The finance office menu", "Trick number seven": "7. Urgency",
      "Now the twist that affects": "The rule that never arrived", "So here is your checklist": "Your checklist for 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video52", "length_scale": 1.45,
  "title": "7 Dealer Tricks When Buying a Truck in 2026 (The Rule That Would Have Stopped Them Died)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
