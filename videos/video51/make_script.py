import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The average new car payment in America just hit a record seven hundred eighty-seven dollars a month. One in four new loans now lasts seven years or longer. More than one in five buyers is paying over one thousand dollars a month. And a new tax break in twenty twenty-six can save truck buyers real money, but only if they buy, not lease, and only if the truck was assembled in the right place.""",
   "pickup truck dealership", "RECORD $787/MONTH")
sc("""So should you lease or buy your next truck in twenty twenty-seven? We will go through it round by round: the monthly payment, the total cost, the new tax rule, the mileage trap, the modification trap, and what happens when the contract ends. At the end, you will know exactly which choice fits the way you use a truck.""",
   "Ford F-150 Chevrolet Silverado", "LEASE OR BUY? ROUND BY ROUND")
sc("""Why does this matter so much for trucks? Because trucks are expensive. According to Kelley Blue Book data from Cox Automotive, the average full-size pickup sold for sixty-seven thousand, five hundred seventy-three dollars in September twenty twenty-six. At that price, the difference between a good and a bad financing decision can easily be worth ten thousand dollars or more over the life of the truck.""",
   "Ram 1500 Chevrolet Silverado", "AVG FULL-SIZE PICKUP: $67,573")
sc("""Every number in this video comes from a published source, listed in the description. This is general information, not financial or tax advice. Your situation is different, so check with a professional before signing. If we could not confirm a figure, we left it out. Let's start with the number every dealer wants you to focus on.""",
   "car loan paperwork", "EVERY NUMBER IS SOURCED")

# ---------- ROUND 1 ----------
sc("""Round one: the monthly payment. According to Edmunds, in the third quarter of twenty twenty-six, the average monthly payment on a new vehicle loan was seven hundred eighty-seven dollars, up from seven hundred fifty-six a year earlier. The average amount financed was a record forty-four thousand, six hundred sixty-four dollars, and the average interest rate was seven percent.""",
   "car dealership finance office", "1. THE MONTHLY PAYMENT")
sc("""Leasing usually wins this round. According to Experian, in the second quarter of twenty twenty-six, the average new vehicle loan payment was seven hundred sixty-five dollars, and the average lease payment was one hundred forty-eight dollars lower. For one popular Ford S U V, the Explorer, Ford Authority reported that lessees paid six hundred eleven dollars a month, versus seven hundred ninety-five dollars for buyers with a loan.""",
   "Ford Explorer", "LEASE: ~$148/MONTH LESS")
sc("""There is one more payment number that shows the pressure on buyers. According to Edmunds, twenty-one point two percent of financed new vehicle purchases in the third quarter of twenty twenty-six had payments of one thousand dollars or more a month. A year earlier, it was nineteen point one percent. For many truck buyers, one thousand dollars a month is no longer unusual. It is becoming normal.""",
   "pickup truck finance", "21.2% PAY $1,000+/MONTH")
sc("""Why is a lease cheaper per month? Because you only pay for the part of the truck's value that you use during the lease, plus interest and fees. If a truck is expected to keep a lot of its value, the lease payment can be low. When you buy, you pay for the whole truck, even the part you will still own at the end.""",
   "pickup truck keys", "WHY LEASES COST LESS PER MONTH")
sc("""And here is the first twist. Lower monthly payments are exactly why leasing can feel like a win, even when it is not. Experian reported that leases made up twenty-three point seven five percent of new vehicle financing in the second quarter of twenty twenty-six, slightly down from a year earlier. Loans rose to fifty-nine point five seven percent. Buyers are leaning back toward owning.""",
   "pickup truck dealership lot", "LEASE SHARE: 23.75%")
sc("""Part of the reason is the type of vehicle. Trucks are often kept for many years, used for work, and modified. Those habits fit buying better than leasing. In Experian's lease data, the most leased brands were Honda and Toyota, while Ford's lease share rose to six point five seven percent. Trucks are not the typical leased vehicle, and the next rounds explain why.""",
   "Ford F-150 work truck", "TRUCKS ARE OFTEN KEPT FOR YEARS")

# ---------- ROUND 2 ----------
sc("""Round two: the total cost. This is where buying usually fights back. According to Edmunds, the average new vehicle loan in the third quarter of twenty twenty-six will cost the buyer nine thousand nine hundred thirty-eight dollars in total interest over its life. That is almost ten thousand dollars just to borrow the money.""",
   "loan calculator", "2. TOTAL INTEREST: $9,938")
sc("""And loans are getting longer. Edmunds reported that twenty-five point five percent of new vehicle loans had terms of eighty-four months or longer in the third quarter of twenty twenty-six, up from twenty-one point eight percent a year earlier. Among buyers paying one thousand dollars or more a month, sixty-nine percent chose terms of seventy-two months or longer.""",
   "car loan contract", "84+ MONTH LOANS: 25.5%")
sc("""Interest rates matter too. According to Experian, the average new vehicle loan rate in the second quarter of twenty twenty-six was six point three five percent, down from six point seven nine a year earlier. Used vehicle loans averaged eleven point one nine percent. Leases have their own version of interest, called the money factor, and it is worth asking the dealer to show it to you as a percentage.""",
   "bank loan rate", "NEW LOAN RATE: 6.35%")
sc("""Here is the twist. A seven-year loan makes the monthly payment look smaller, but the truck may be worth less than you owe for much of that time. That is called being upside down. If you want to trade the truck in early, you may have to roll the remaining debt into the next loan. Edmunds analyst Ivan Drury said a longer loan term may be the only way for some buyers to get the vehicle they need.""",
   "used pickup trade in", "THE UPSIDE-DOWN TRAP")
sc("""So which is cheaper overall? If you keep a truck for a long time, well past the end of the loan, buying almost always costs less. The years with no payment are where buying wins. If you replace your truck every three years, leasing can cost less, because you never pay for the years when the truck is old.""",
   "old pickup truck", "KEEP IT LONG = BUY")
sc("""And remember that trucks often last longer than cars. A well-maintained pickup can run for many years and many miles. That makes the years after the loan especially valuable. Every year you drive a paid-off truck is a year without a payment, and that is where owning builds its advantage over leasing.""",
   "old pickup truck farm", "PAID-OFF YEARS WIN")
sc("""Think of a simple example with round numbers. A buyer who finances a truck for six years and then drives it for four more years with no payment spreads the cost over ten years. A person who leases three trucks back to back over nine years always has a payment. Over a decade, the person who keeps the truck usually comes out ahead, as long as the truck stays reliable.""",
   "pickup truck highway", "10-YEAR VIEW")

# ---------- ROUND 3: TAX ----------
sc("""Round three: the new tax twist, and this one is big in twenty twenty-six. According to Fox reporting in January twenty twenty-six, Treasury Secretary Scott Bessent announced the rollout of a new deduction for car loan interest. Eligible taxpayers can deduct up to ten thousand dollars a year in auto loan interest, whether they itemize or take the standard deduction.""",
   "US Treasury building", "3. UP TO $10,000 INTEREST DEDUCTION")
sc("""But there are rules. According to the same report, it covers new vehicles purchased from twenty twenty-five through twenty twenty-eight, including pickup trucks under fourteen thousand pounds. The vehicle must have its final assembly at a U S plant. It must be for personal use, not business. The buyer must be the first owner. And the loan must be secured by a lien on the vehicle.""",
   "pickup truck factory assembly line", "NEW, US-ASSEMBLED, PERSONAL USE")
sc("""Here is the twist that matters for this video. Because the deduction is for interest on a loan secured by the vehicle, the report implies that leases would not qualify. So in twenty twenty-six, buying with a loan has a tax advantage that leasing does not. The deduction also phases out for higher earners, starting above one hundred thousand dollars for individuals and two hundred thousand for joint filers.""",
   "tax forms", "TWIST: LEASES LIKELY DON'T QUALIFY")
sc("""And here is the second twist: where the truck is built. Not every pickup sold in America is assembled in America. For example, the Ford Maverick is built in Mexico, and so is the current Toyota Tacoma. A buyer who wants this deduction should check the final assembly location on the window sticker or the vehicle information before signing. According to the report, the I R S had not yet released an official list of qualifying models.""",
   "Ford Maverick", "CHECK WHERE IT WAS ASSEMBLED")
sc("""And there is a refinancing angle. According to Experian, the average refinance rate in the second quarter of twenty twenty-six was seven point nine seven percent, compared with an original rate of ten point four zero for those loans. Buyers who took a high rate can sometimes lower it later. That option exists with a loan. With a lease, the terms are usually fixed until the end.""",
   "refinance loan", "REFINANCING: A LOAN-ONLY OPTION")
sc("""How much could it save? That depends on your tax bracket and how much interest you pay. With the average loan costing almost ten thousand dollars in interest over its life, according to Edmunds, the deduction can reduce the true cost of buying by a meaningful amount for eligible buyers. It does not make a bad deal good, but it can tip a close decision toward buying.""",
   "calculator money", "IT CAN TIP THE DECISION")

# ---------- ROUND 4: MILES ----------
sc("""Round four: the mileage trap. Most leases come with an annual mileage limit, and you pay a fee for every mile above it when you return the truck. Truck owners often drive more than car owners, especially those who tow trailers, drive to job sites, or live in rural areas. If you go over the limit, the extra charges can wipe out the savings of a lower monthly payment.""",
   "pickup truck towing trailer highway", "4. THE MILEAGE TRAP")
sc("""Some leases let you buy extra miles at the start, at a lower price per mile than the penalty at the end. If you know you will drive more, buying miles up front can make a lease work. But it also raises the monthly payment, which reduces the main advantage of leasing in the first place. Always compare the final numbers.""",
   "pickup truck road trip", "BUY MILES UP FRONT?")
sc("""Here is the twist. Many people underestimate how much they drive. A family road trip, a new job farther away, or a summer of towing a boat can add thousands of miles. Before you lease, look at your last few years of driving, using old service records or your current odometer, and add a safety margin. Buying has no mileage penalty at all, although higher miles do lower resale value.""",
   "pickup truck odometer", "KNOW YOUR REAL MILEAGE")

# ---------- ROUND 5: MODS & WEAR ----------
sc("""Round five: modifications and wear. Truck owners love to customize. Lift kits, bigger tires, bed covers, racks and tow hitches. On a leased truck, many modifications are not allowed or must be removed before return. And trucks used for work get scratches, dents and worn interiors. A lease contract can charge you for wear beyond what it considers normal.""",
   "lifted pickup truck", "5. MODS AND WEAR")
sc("""Insurance is another detail. A leased vehicle usually requires higher coverage limits and gap coverage, because the lender owns the truck. That can raise your insurance bill compared with owning a truck outright, especially once a loan is paid off and you can choose your own coverage levels. Get insurance quotes for both options before you decide.""",
   "insurance paperwork", "LEASES CAN RAISE INSURANCE")
sc("""This is why leasing is often a poor fit for a working truck. If your truck carries tools, lumber, gravel or equipment, it will show it. When you own the truck, wear only affects resale. When you lease it, wear can become a bill at the end of the contract. For a weekend truck that stays clean and stock, a lease is much safer.""",
   "work truck bed tools", "WORK TRUCK = OWN IT")

# ---------- ROUND 6: END ----------
sc("""Round six: the end of the contract. When a lease ends, you can return the truck, buy it at a price set in the contract, or lease a new one. If the truck turns out to be worth more than the contract buyout, buying it can be a good deal. If it is worth less, you can simply hand back the keys. That flexibility is a real advantage of leasing.""",
   "truck dealership return", "6. THE END OF THE CONTRACT")
sc("""Here is the twist that has burned some buyers recently. When a model is discontinued or demand collapses, its value can drop fast. A leased truck protects you from that, because the risk belongs to the lender. A bought truck does not. If you are considering a truck whose future is uncertain, like a model with falling sales, leasing can shift the resale risk away from you.""",
   "Ford F-150 Lightning", "LEASING SHIFTS RESALE RISK")
sc("""Look at the electric pickups. Ford ended the all-electric F-one-fifty Lightning in December twenty twenty-five, after a nineteen point five billion dollar charge, according to Fox Business. In the third quarter of twenty twenty-six, according to autoevolution, Ford sold just two hundred eighty-nine Lightnings. Many people who leased electric trucks could simply return them. Owners had to deal with the resale value themselves.""",
   "Ford F-150 Lightning pickup", "LIGHTNING: LEASE VS OWN")
sc("""Tariffs add another layer of uncertainty. In twenty twenty-five and twenty twenty-six, tariffs on imported vehicles and parts pushed some prices up. When new truck prices rise, used truck values often rise too, which helps owners. When prices fall, owners lose. A lease locks in the end value at the start, so you know exactly where you stand.""",
   "pickup trucks port", "TARIFFS AND RESALE")
sc("""On the other hand, trucks with strong resale reputations, like the Toyota Tacoma, reward owners. A truck that holds its value well builds equity, and that equity is yours when you sell or trade. With a lease, any value above the contract buyout belongs to the lender unless you buy the truck.""",
   "Toyota Tacoma", "STRONG RESALE REWARDS OWNERS")

# ---------- VERDICT ----------
sc("""Before the verdict, one more real-world factor: your credit. The best lease deals and the lowest loan rates go to buyers with strong credit scores. Buyers with weaker credit often see much higher rates, which can make both options expensive. Checking your credit before you visit the dealer, and getting a loan offer from a bank or credit union first, gives you a number to compare against the dealer's offer.""",
   "credit score", "CHECK YOUR CREDIT FIRST")
sc("""And never negotiate only the monthly payment. A dealer can hit almost any monthly number by changing the loan length, the down payment or the lease terms. Negotiate the price of the truck first, then the financing. That one habit protects you whether you lease or buy.""",
   "truck dealership negotiation", "NEGOTIATE PRICE, NOT PAYMENT")
sc("""So who should lease a truck in twenty twenty-seven? Someone who drives a predictable, moderate number of miles, keeps the truck clean and stock, wants a new truck every few years, and is not eligible for the loan interest deduction, or is choosing a truck not assembled in America. Leasing can also make sense for a model with an uncertain future.""",
   "pickup truck clean new", "WHO SHOULD LEASE")
sc("""And who should buy? Someone who keeps trucks for many years, drives a lot of miles, tows, works the truck hard, or likes to modify it. Buying also gets the edge in twenty twenty-six for eligible buyers of new, U S assembled trucks, thanks to the loan interest deduction. For most traditional truck owners, buying remains the better long-term choice.""",
   "work pickup truck", "WHO SHOULD BUY")
sc("""There is also a middle path. Some buyers finance a truck with a shorter loan, like four or five years, and a bigger down payment. That reduces total interest, avoids being upside down, and still qualifies for the interest deduction if the truck and buyer meet the rules. It is less exciting than a low lease payment, but it is often the cheapest path to owning a truck.""",
   "pickup truck keys handshake", "THE MIDDLE PATH")
sc("""And here is the final twist. The worst choice is not leasing or buying. It is stretching a loan to eighty-four months to afford a truck that is too expensive. According to Edmunds, twenty-one point two percent of new vehicle buyers who financed were paying one thousand dollars or more a month in the third quarter of twenty twenty-six. If the payment only works with a seven-year loan, the truck may simply cost too much.""",
   "pickup truck price sticker", "THE REAL MISTAKE: TOO MUCH TRUCK")

# ---------- CLOSE ----------
sc("""So here is your checklist before you decide. First, compare the total cost of both options over the time you plan to keep the truck, not just the monthly payment. Second, check your real yearly mileage. Third, check whether the truck is assembled in the U S and whether you qualify for the interest deduction, with a tax professional.""",
   "car buying checklist", "CHECKS 1, 2 AND 3")
sc("""Fourth, think about how you use the truck: work, towing and modifications point to buying. And fifth, read the end of the lease contract carefully: the buyout price, the mileage fee, and the wear rules. Those three lines decide whether a lease is a deal or a trap.""",
   "lease contract", "CHECKS 4 AND 5")
sc("""We put all of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the questions to ask the finance office and the numbers to compare. The link is in the description and in the pinned comment. Subscribe for the next video, about seven dealer tricks to watch for when you buy a truck. Thanks for watching.""",
   "pickup truck dealership", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The average new car payment": "Intro", "Round one": "1. The monthly payment", "Round two": "2. The total cost",
      "Round three": "3. The 2026 loan interest deduction", "Round four": "4. The mileage trap", "Round five": "5. Mods and wear",
      "Round six": "6. The end of the contract", "So who should lease": "Who should lease, who should buy",
      "So here is your checklist": "What to check before you sign in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video51", "length_scale": 1.5,
  "title": "Lease vs Buy a Truck in 2027: The $10,000 Tax Twist Most Buyers Miss", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
