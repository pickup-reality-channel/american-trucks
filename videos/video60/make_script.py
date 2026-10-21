import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""A brand-new Silverado with new V eight engines. A Ford Maverick that will only come as a hybrid at its base trim. A Ram Hemi that came back from the dead. A Ford electric truck that was shut down. And diesel at six dollars a gallon. The truck market heading into twenty twenty-seven looks nothing like it did two years ago, and if you buy with old information, you could pay thousands more than you need to.""",
   'Chevrolet Silverado 2027', 'THE 2027 TRUCK MARKET HAS CHANGED')
sc("""This is the complete breakdown of the Twenty Twenty-Seven Truck Buyer's Guide. We will go through what is changing, what trucks really cost, how to pay for one, which engine makes sense, and how to buy without getting burned, all in one video. Think of it as the whole channel's research, in one place.""",
   'pickup trucks lineup', 'THE COMPLETE BREAKDOWN')
sc("""Every number here comes from a published source, listed in the description. Specs and prices for future models can change before they go on sale, and we will tell you when something is an estimate. If we could not confirm a figure, we left it out. Let's start with the market.""",
   'pickup trucks dealership', 'EVERY NUMBER IS SOURCED')
sc("""Part one: the state of the truck market. According to Kelley Blue Book data from Cox Automotive, the average full-size pickup sold for sixty-seven thousand, five hundred seventy-three dollars in September twenty twenty-six. Trucks are among the most expensive vehicles Americans buy, and among the most popular.""",
   'Ford F-150 Ram 1500 Chevrolet Silverado', 'AVG FULL-SIZE PICKUP: $67,573')
sc("""The sales race is still fierce. According to autoevolution, in the third quarter of twenty twenty-six, Ford delivered two hundred three thousand, seven hundred seven F-Series trucks, down one point nine percent. Chevrolet's Silverado delivered eighty-six thousand, five hundred ninety, and Silverado and G M C Sierra together reached two hundred thirty-three thousand, two hundred twenty-nine.""",
   'Ford F-150', 'Q3 2026: F-SERIES 203,707')
sc("""And the fastest-growing brand was Ram. According to the same report, Ram's trucks were up thirty-three point seven percent in the third quarter, with the Ram fifteen hundred alone reaching seventy-six thousand, six hundred fifty. The reason is one of the strangest stories in the truck world.""",
   'Ram 1500', 'RAM: +33.7% IN Q3 2026')
sc("""Here is the twist. Ram dropped its famous five point seven liter Hemi V eight for the twenty twenty-five model year. Buyers revolted. In June twenty twenty-five, Ram reversed course, and according to Carscoops, Stellantis said the brand received over ten thousand orders in the first twenty-four hours after announcing the Hemi's return. A year later, sales jumped.""",
   'Ram 1500 Hemi V8', 'HEMI RETURN: 10,000+ ORDERS IN 24H')
sc("""And here is what the numbers say about the rivalry. Ford wins the single nameplate, with the F-Series leading every quarter. General Motors wins the combined total when you add the Silverado and the Sierra. And Ram wins momentum. For buyers, that competition is good news, because it keeps incentives and features flowing.""",
   'Ford Chevrolet Ram trucks', 'COMPETITION HELPS BUYERS')
sc("""But high prices are pushing many buyers toward used trucks and smaller trucks. When the average full-size pickup costs more than sixty-seven thousand dollars, a midsize truck, a small hybrid or a lightly used full-size truck can save tens of thousands of dollars. The smartest buyers in twenty twenty-seven will compare all three.""",
   'used pickup trucks lot', 'NEW, USED OR SMALLER?')
sc("""The lesson for buyers is that truck makers listen. When buyers push back, products change. And that means the truck you want may look different next year, which is exactly why timing your purchase matters.""",
   'pickup truck factory', 'TRUCK MAKERS LISTEN')
sc("""Part two: what is changing for twenty twenty-seven. The biggest news is the new Chevrolet Silverado. According to Edmunds, the twenty twenty-seven Silverado gets new five point seven liter and six point six liter V eight engines, replacing the five point three and six point two. Chevy calls the six point six the most powerful naturally aspirated V eight in its class.""",
   'Chevrolet Silverado', '2027 SILVERADO: NEW V8s')
sc("""Edmunds says every twenty twenty-seven Silverado gets a twelve point two inch digital gauge cluster and a sixteen point three inch touchscreen as standard. The two point seven liter turbo four and the three liter turbodiesel carry over. And here is the twist: there is still no hybrid Silverado.""",
   'Chevrolet Silverado interior', 'STILL NO HYBRID SILVERADO')
sc("""Pricing was not announced when Edmunds reported in June twenty twenty-six. Edmunds expected a starting price at or just below forty thousand dollars, with top High Country and Z R two trims potentially passing eighty thousand when fully optioned. Edmunds expected trucks at dealers by late twenty twenty-six or early twenty twenty-seven. Those are estimates, so check final prices.""",
   'Chevrolet Silverado ZR2', 'EST. ~$40K START (EDMUNDS)')
sc("""What does the new Silverado mean for buyers who do not want one? Often, a new generation means discounts on the outgoing model. When a redesigned truck arrives, dealers usually want to clear the old model year. If you do not need the newest features, a leftover twenty twenty-six model can be one of the best deals of twenty twenty-seven.""",
   'Chevrolet Silverado dealership', 'NEW MODEL = OLD MODEL DISCOUNTS')
sc("""And first-year models can have early problems that get fixed in later years. That is not a rule, and many new trucks are excellent from day one. But buyers who want the lowest risk sometimes wait a year after a redesign, and check recalls and owner reports before buying.""",
   'pickup truck recall', 'FIRST-YEAR MODEL RISK')
sc("""Next, the Ford Maverick. According to Ford Authority, for the twenty twenty-seven model year, the base Maverick X L becomes hybrid only. The cheapest EcoBoost gas version becomes the X L T all-wheel drive, at thirty thousand, seven hundred forty-five dollars, which Ford Authority says is three thousand six hundred dollars more than the cheapest twenty twenty-six gas model.""",
   'Ford Maverick', '2027 MAVERICK XL: HYBRID ONLY')
sc("""That matters because the Maverick is one of the most important trucks in America. According to Ford, it sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, and eighty-one thousand and thirty-four of them were hybrids. The small, affordable hybrid truck is now the default entry point.""",
   'Ford Maverick hybrid', '155,051 MAVERICKS IN 2025')
sc("""And electric trucks are in flux. Ford ended production of the F-one-fifty Lightning in twenty twenty-five and took a large charge as it shifted strategy, according to Fox Business. Meanwhile, the startup Slate Auto opened preorders in June twenty twenty-six for a small two-seat electric pickup starting at twenty-four thousand nine hundred fifty dollars, according to The Next Web.""",
   'Ford F-150 Lightning', 'LIGHTNING ENDS. SLATE AT $24,950.')
sc("""Here is the twist about the small truck class. According to The Autopian, in January twenty twenty-six, the Hyundai Santa Cruz was reportedly heading toward an early end. So while the Maverick booms, not every small truck has found buyers. If you buy a model that is being discontinued, check the resale outlook carefully.""",
   'Hyundai Santa Cruz', 'SANTA CRUZ: REPORTEDLY ENDING')
sc("""Part three: what trucks cost in twenty twenty-six. According to Edmunds' comparison, published in June twenty twenty-six, the Ford F-one-fifty starts at forty thousand and eighty-five dollars for an X L regular cab, and the Platinum with the biggest cab starts at seventy-one thousand, five hundred ninety-five. The current Silverado Work Truck starts at thirty-nine thousand, six hundred ninety-five.""",
   'Ford F-150 XL', 'F-150 FROM $40,085')
sc("""The Ram fifteen hundred Tradesman Quad Cab starts at forty-four thousand, six hundred twenty dollars or more, according to Edmunds, and the luxury Tungsten crew cab starts at ninety-one thousand, three hundred ninety-five. That is a gap of almost forty-seven thousand dollars within a single model name.""",
   'Ram 1500 Tungsten', 'RAM 1500: $44,620 TO $91,395')
sc("""And the very top of the market keeps climbing. In our most expensive trucks video, the priciest pickup we found cost one hundred twenty-two thousand, two hundred sixty-five dollars fully loaded. At the other end, the cheapest new trucks still start under thirty thousand dollars. The range has never been wider.""",
   'GMC Sierra Denali', 'TOP OF MARKET: $122,265')
sc("""Here is the twist. The average buyer does not buy a base truck. That is why the average transaction price is around sixty-seven thousand dollars, even though base trucks start around forty. Every trim level and option package moves the price up, and many of them do not return their full cost at resale.""",
   'pickup truck window sticker', 'BASE $40K, AVERAGE $67K')
sc("""Here is a money tip about trim levels. The biggest jumps in price often come from luxury trims, not from capability. A mid-level trim with the right engine and towing package can do almost everything a top trim can do, for tens of thousands less. Pay for capability you will use, and be careful with luxury you will not.""",
   'pickup truck interior', 'PAY FOR CAPABILITY, NOT LUXURY')
sc("""Part four: what it costs to keep a truck. According to AAA's Your Driving Costs study for twenty twenty-six, a new half-ton pickup costs about sixteen thousand, four hundred forty-nine dollars a year to own and operate, and a midsize pickup about thirteen thousand and eighty-nine, assuming fifteen thousand miles a year over five years.""",
   'pickup truck highway', 'HALF-TON: $16,449/YEAR TO OWN')
sc("""That includes depreciation, which averaged four thousand, four hundred twenty-two dollars a year across all new vehicles, plus finance charges, insurance, registration and taxes, fuel, and maintenance. And the cheapest pickup to own in AAA's study was the hybrid, at sixteen thousand, one hundred seventeen dollars a year.""",
   'Ford F-150 hybrid', 'HYBRID: $16,117/YEAR')
sc("""And remember the fees nobody budgets. According to AAA, license, registration and taxes averaged eight hundred two dollars a year in twenty twenty-six, and sales tax at purchase can add thousands more on an expensive truck. Put those numbers in your budget before you shop.""",
   'DMV office', 'REGISTRATION & TAXES: $802/YEAR')
sc("""Insurance is the next big piece. According to Insurify, full coverage averaged two thousand, two hundred thirty-seven dollars a year nationally in the first half of twenty twenty-six. Full-size pickups can actually be cheaper to insure than sedans in Insurify's comparison. But performance trucks like the Ram T R X cost more than three thousand dollars a year to insure, according to Insure dot com data.""",
   'insurance paperwork', 'INSURANCE: $2,237 AVERAGE')
sc("""And theft is part of the cost. According to the National Insurance Crime Bureau, the Chevrolet Silverado fifteen hundred was the fourth most stolen vehicle in America in twenty twenty-five, with sixteen thousand, seven hundred sixty-four thefts, and the Ford F-one-fifty was seventh. Popular trucks attract thieves, and that affects insurance prices.""",
   'Chevrolet Silverado', 'SILVERADO: #4 MOST STOLEN')
sc("""So before you choose a truck, get insurance quotes on the exact trims you are considering. It takes a few minutes online, and it can change which truck makes sense. And shop your policy again at every renewal. It is one of the easiest truck costs to lower.""",
   'laptop insurance quote', 'QUOTE BEFORE YOU CHOOSE')
sc("""And repairs keep getting more expensive. According to Insurify, auto repair and maintenance costs have risen about forty-five percent in the past five years. Tires are rising too. According to SlashGear, the federal Producer Price Index for tire manufacturing climbed again in August twenty twenty-six, and Michelin blamed higher raw material and energy costs on the Middle East conflict.""",
   'pickup truck tires', 'REPAIRS +45%. TIRES RISING.')
sc("""Part five: fuel and engines, and this is where twenty twenty-six changed everything. According to AAA, diesel hit a record six dollars and fifty-one cents a gallon in September twenty twenty-six. NPR reported that the war with Iran disrupted oil shipping through the Strait of Hormuz, pushing Brent crude above one hundred five dollars a barrel.""",
   'diesel pump', 'DIESEL RECORD: $6.51')
sc("""According to the Energy Information Administration, in the week of October nineteenth, gas averaged four dollars and twenty-eight cents and diesel six twenty-eight. Here is the twist: one year earlier, the gap between them was only about sixty cents. Now a light-duty diesel needs about forty-seven percent better fuel economy than the gas version just to break even on fuel.""",
   'gas station prices', 'DIESEL NEEDS +47% MPG')
sc("""Here is an example to show the fuel math. These are example numbers, not any specific truck. A gas truck at twenty miles per gallon, driven fifteen thousand miles at four twenty-eight a gallon, costs about three thousand two hundred ten dollars a year in fuel. A diesel at twenty-five miles per gallon at six twenty-eight costs about three thousand seven hundred sixty-eight. One year ago, with the same trucks, the diesel would have been cheaper.""",
   'diesel truck fueling', 'EXAMPLE: GAS $3,210 VS DIESEL $3,768')
sc("""And nobody knows where fuel prices will go next. According to NPR, President Trump said oil prices likely would not fall until after the November midterm elections, and S and P Global's Jim Burkhard said the market is adjusting to a new normal. So test your choice at different fuel prices, not just today's.""",
   'oil refinery', 'TEST DIFFERENT FUEL PRICES')
sc("""So which engine wins in twenty twenty-seven? For commuters and mixed driving, the hybrid usually wins, which is exactly what AAA's study found. For buyers who want the lowest price and simplest maintenance, a gas engine. And for heavy towing, a heavy-duty diesel is still often the right tool, even with expensive fuel.""",
   'Toyota Tundra hybrid', 'HYBRID, GAS OR DIESEL?')
sc("""Part six: how to pay for it. According to Edmunds, the average new vehicle loan in the third quarter of twenty twenty-six had a seven percent rate, a record forty-four thousand, six hundred sixty-four dollars financed, and a seven hundred eighty-seven dollar monthly payment. Twenty-one point two percent of financed buyers paid one thousand dollars or more a month.""",
   'car loan paperwork', 'AVG LOAN: $787/MONTH AT 7%')
sc("""And loans are getting longer. Edmunds found that twenty-five point five percent of new vehicle loans had terms of eighty-four months or longer, and the average total interest was nine thousand, nine hundred thirty-eight dollars. A longer loan lowers the payment but raises the total cost.""",
   'calendar seven years', '25.5% OF LOANS: 7+ YEARS')
sc("""Get pre-approved before you go to the dealer. A bank or credit union pre-approval gives you a rate to beat. According to Experian, the average new vehicle loan rate in the second quarter of twenty twenty-six was six point three five percent, while used vehicle loans averaged eleven point one nine percent. Your credit score can change your rate a lot, so check it early.""",
   'credit union', 'GET PRE-APPROVED')
sc("""And think about leasing honestly. According to Experian, the average lease payment was one hundred forty-eight dollars lower than the average loan payment in the second quarter of twenty twenty-six. But leases have mileage limits and wear charges, and most do not qualify for the new interest deduction. For trucks kept a long time and worked hard, buying usually wins.""",
   'pickup truck towing', 'LEASE OR BUY?')
sc("""Here is the twist that can be worth the most money. According to Fox reporting from January twenty twenty-six, a new federal deduction lets eligible buyers deduct up to ten thousand dollars a year in auto loan interest. The vehicle must be new, bought for personal use, with final assembly in the United States, and the deduction phases out for higher incomes.""",
   'pickup truck assembly plant', 'UP TO $10,000 INTEREST DEDUCTION')
sc("""So the assembly plant on the window sticker now matters for your taxes. Leases generally do not qualify, because there is no loan secured by the vehicle. For buyers who qualify, that tips the lease versus buy decision further toward buying. Talk to a tax professional before you decide.""",
   'window sticker', 'CHECK THE ASSEMBLY PLANT')
sc("""Part seven: how to buy without getting burned. According to CarEdge's State of Dealer Fees twenty twenty-six report, the average document fee is four hundred seventy-two dollars, ranging from eighty-five in California, which caps it, to nine hundred seventy on average in Florida. Always negotiate the out-the-door price, which includes every fee.""",
   'car dealership', 'AVG DOC FEE: $472')
sc("""Get written quotes by email from several dealers, with the out-the-door price on a specific truck. Check rebates and incentives, because leftover trucks can carry large discounts. According to CarEdge's deal list updated in October twenty twenty-six, a twenty twenty-five Ford F-one-fifty Lightning carried eight thousand dollars cash back.""",
   'laptop email', 'WRITTEN QUOTES + REBATES')
sc("""And negotiate your trade-in separately. Get offers for your current truck from several buyers before you talk about the new one. When everything is mixed together, it is easy to lose track of what you are paying and what you are getting.""",
   'used truck trade in', 'TRADE-IN: NEGOTIATE SEPARATELY')
sc("""And watch for add-ons. According to CarWhere, which studied more than five thousand real buyer quotes through June twenty twenty-six, thirty-four point one percent included dealer-installed add-ons, like window tint at an average of five hundred four dollars. Add-ons and finance office products are optional, and anything added to the loan costs interest too.""",
   'dealer add-on sticker', '34.1% OF QUOTES HAD ADD-ONS')
sc("""Here is the twist about protection. The federal CARS Rule, which would have banned some deceptive dealer practices, was vacated by the Fifth Circuit Court of Appeals in January twenty twenty-five, according to ConsumerAffairs. So your protection depends on state laws and on reading every line of the contract.""",
   'courthouse', 'THE CARS RULE NEVER TOOK EFFECT')
sc("""Part eight: owning it well. Check for recalls by vehicle identification number. In February twenty twenty-six, Chrysler recalled four hundred fifty-six thousand, two hundred eighty-seven vehicles, mostly Ram pickups, because a towing module could disable trailer lights and brakes, according to Pickup Truck Talk. Owners were told not to tow until the free fix was done.""",
   'Ram 2500 towing', 'CHECK RECALLS: 456,287 RAMS')
sc("""And know your warranty rights. According to the Federal Trade Commission, your warranty stays in effect if you use aftermarket parts, and the manufacturer must prove an aftermarket part caused the damage before denying coverage. Keep every receipt and maintenance record.""",
   'pickup truck service', "AFTERMARKET PARTS DON'T VOID IT")
sc("""And choose mods carefully. According to SEMA, Americans spent more than fifteen billion dollars modifying pickups in twenty twenty-five, but only twenty-six percent of pickup accessorizers use their trucks off-road. Bed covers, liners and the right tires usually pay off. Big lifts and emissions changes usually do not.""",
   'pickup truck bed cover', 'SEMA: $15 BILLION ON PICKUP MODS')
sc("""And if you tow, follow the basics every time: check the lights, tires and brakes, balance the tongue weight, cross the safety chains, connect the breakaway cable to the truck, and slow down. Towing mistakes can damage a truck faster than years of normal driving.""",
   'trailer hitch safety chains', 'TOW SAFELY')
sc("""Finally, follow the maintenance schedule, especially the severe service schedule if you tow or drive in extreme conditions. According to AAA, maintenance, repairs and tires averaged eleven point seven cents a mile in twenty twenty-six. Regular maintenance is the cheapest way to keep that number from growing.""",
   'pickup truck oil change', 'MAINTENANCE: 11.7¢/MILE')
sc("""Now let's turn all of this into a plan. If you are buying in the next few months, here is the order that saves the most money. First, decide what you really need: size, towing, passengers and engine. Second, run the real cost of ownership for two or three trucks. Third, get insurance quotes and a loan pre-approval.""",
   'pickup truck planning', 'YOUR BUYING PLAN')
sc("""Fourth, check the assembly plant and whether you qualify for the interest deduction. Fifth, get written out-the-door quotes from several dealers. Sixth, inspect the truck, check recalls and read every line before you sign. And seventh, keep every document, because it protects your warranty and your wallet.""",
   'signing contract', '7 STEPS IN ORDER')
sc("""Here is the final twist. The most important factor in your truck's real cost is not the brand, the engine or even the price. It is the decisions you make before you sign. Two buyers can drive away in the same truck, on the same day, and one can pay thousands of dollars more over five years. The difference is information.""",
   'two pickup trucks', 'INFORMATION IS THE DIFFERENCE')
# ---------- CLOSE ----------
sc("""That is exactly why we made the Twenty Twenty-Seven Truck Buyer's Guide. It puts everything from this channel in one place: the real cost worksheets, the fuel math for diesel, gas and hybrid, the financing and tax checklist, the dealer fee and add-on guide, the towing checklist and the mods worth buying. The link is in the description and in the pinned comment.""",
   'truck buyer guide book', "THE 2027 TRUCK BUYER'S GUIDE")
sc("""Thank you for watching this series. Subscribe for more truth about American trucks, and tell us in the comments: which truck are you thinking about buying in twenty twenty-seven? We read every comment, and your questions shape our next videos.""",
   'pickup truck sunset', "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {'A brand-new Silverado with new': 'Intro', 'Part one: the state of': 'Part 1: The market', 'Part two: what is changing': "Part 2: What's new for 2027", 'Part three: what trucks cost': 'Part 3: What trucks cost', 'Part four: what it costs': 'Part 4: The cost of keeping it', 'Part five: fuel and engines,': 'Part 5: Fuel and engines', 'Part six: how to pay': 'Part 6: How to pay', 'Part seven: how to buy': 'Part 7: How to buy', 'Part eight: owning it well.': 'Part 8: Owning it well', "Now let's turn all of": 'Your 2027 buying plan'}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": 'video60', "length_scale": 1.45,
  "title": "2027 Truck Buyer's Guide: Everything Changing Before You Buy (New Silverado, Hybrid-Only Maverick, $6 Diesel)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.45/212,1), "min")
