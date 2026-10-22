import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""In February, a report said the Hyundai Santa Cruz was being discontinued. Hyundai would not confirm it. Eight months later, Hyundai says the Santa Cruz continues for twenty twenty-seven. So which one is true? Both, in a way, and the numbers behind this little truck are stranger than the headlines. It sold twenty-five thousand units last year, and it is down twenty-eight percent this year, while its rival is up. Here is the real story.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: DEAD OR ALIVE IN 2027?")
sc("""The Hyundai Santa Cruz is a compact pickup built on the same platform as the Tucson, with a four foot bed, and it has always been a small, odd, interesting truck. It is also a truck that Americans seem to like when they own one, and that they do not buy in large numbers. That gap between how owners feel and how many people buy is what this video is about.""",
   "Hyundai Santa Cruz XRT pickup", "SMALL, ODD, AND LOVED BY OWNERS")
sc("""Our sources. Kelley Blue Book for twenty twenty-seven pricing, specs and owner ratings. The Philadelphia Inquirer, from October fifteenth, for the review and for Hyundai's confirmation. The Autopian, for the discontinuation report and the sales context. And Autoevolution for the third quarter sales. Where two sources disagree, we will say so. And there are a few places where they do.""",
   "Hyundai Santa Cruz Limited pickup", "SOURCES: KBB, INQUIRER, AUTOPIAN, AUTOEVOLUTION")
sc("""Four twists are coming. A report that said it was dead. A confirmation that says it lives. A sales gap so large that one rival sold more hybrids in a single quarter than the Santa Cruz sold in nine months. And a replacement that is not coming until the end of the decade. Let us start with the report.""",
   "Hyundai Santa Cruz pickup truck", "FOUR TWISTS")

# 1 THE REPORT
sc("""Part one, the report. According to The Autopian, citing Automotive News and unnamed sources, Hyundai was going to end Santa Cruz production early. The truck was originally set to run through the second quarter of twenty twenty-seven. The reasons given were weak sales and high inventory. Dealers held nearly five months of supply at the end of last year.""",
   "Hyundai dealership pickup trucks", "REPORT: PRODUCTION ENDS EARLY")
sc("""The report added that Hyundai told suppliers it was cutting production by roughly half in that quarter. And that ending the truck would free up space at the Montgomery, Alabama plant, which also builds the Tucson. Kelley Blue Book wrote on February second that the Santa Cruz would reportedly be discontinued for twenty twenty-seven. Notice the word reportedly. Hyundai did not confirm.""",
   "Hyundai Montgomery Alabama plant", "KBB, FEB 2: REPORTEDLY DISCONTINUED")
sc("""What Hyundai did say was careful. It said the Santa Cruz helped the company gain valuable experience and visibility in the open-bed market. It said long range product planning is guided by many factors, including consumer demand and market trends. And it said it does not comment on future product speculation. That is not a denial. It is also not a confirmation. It is a company choosing its words.""",
   "Hyundai Motor America headquarters", "HYUNDAI: NO COMMENT ON SPECULATION")

# 2 THE CONFIRMATION
sc("""Part two, the confirmation. In the Inquirer review from October fifteenth, the writer says it had been unclear since early this year whether the Santa Cruz was still sold in the United States, and that Hyundai now confirms it continues for twenty twenty-seven. The twenty twenty-seven model is a carryover. The review lists no specific changes for the new model year.""",
   "Hyundai Santa Cruz SEL pickup", "OCTOBER: HYUNDAI CONFIRMS 2027")
sc("""So what is the twenty twenty-seven Santa Cruz? According to Kelley Blue Book, there are three trims. The SE and the SEL Activity use a two point five liter four cylinder with one hundred ninety-one horsepower and one hundred eighty-one pound-feet. The XRT uses a turbocharged version of that engine, with two hundred eighty-one horsepower and three hundred eleven pound-feet.""",
   "Hyundai Santa Cruz turbo engine", "190 HP BASE. 281 HP TURBO.")
sc("""Kelley Blue Book lists the starting prices as thirty-one thousand, nine hundred fifty dollars for the SE, thirty-six thousand, three hundred fifty for the SEL Activity, and forty-four thousand, four hundred twenty-five for the XRT. The Autopian, in an older article, gave the starting price with destination as thirty-one thousand, three hundred fifty dollars. The Inquirer tested a twenty twenty-six XRT at forty-three thousand, three hundred thirty-five dollars as tested. These are different model years and different methods, so treat the prices as a range.""",
   "Hyundai Santa Cruz XRT price", "FROM $31,950 TO $44,425 (KBB)")
sc("""Towing is the first real limit. Kelley Blue Book lists three thousand, five hundred pounds for the SE and the SEL Activity, and five thousand pounds for the XRT. The bed is four feet long, with twenty-seven cubic feet of volume. For comparison, the Inquirer says the Nissan Frontier tows nearly seven thousand pounds. So the Santa Cruz is a small truck by design, not by accident.""",
   "Hyundai Santa Cruz bed towing", "TOWS 3,500 TO 5,000 LB. BED: 4 FT.")
sc("""Fuel economy is the second limit, and here the Santa Cruz loses to its main rival. Kelley Blue Book lists twenty-two city and thirty highway for the SE and SEL Activity, and eighteen city and twenty-five highway for the XRT. The Autopian puts the Santa Cruz at twenty-five miles per gallon combined against thirty-eight for the Ford Maverick. Hyundai has no hybrid Santa Cruz. The Autoevolution article says it remains restricted to combustion-only powertrains.""",
   "Hyundai Santa Cruz gas pump", "25 MPG VS 38 MPG FOR THE MAVERICK")

# 3 THE GAP
sc("""Part three, the sales gap, and it is huge. In twenty twenty-five the Ford Maverick sold one hundred fifty-five thousand and fifty-one trucks, and the Santa Cruz sold twenty-five thousand, four hundred ninety-nine. The Autopian says the Maverick outsold it six to one. That is the real reason for the reports of its end. The truck is not bad. It is just overwhelmed.""",
   "Ford Maverick pickup", "2025: MAVERICK 155,051. SANTA CRUZ 25,499.")
sc("""This year it is worse. Autoevolution reports that the Santa Cruz sold fourteen thousand, eight hundred eleven through September, against twenty thousand, six hundred thirty-three at this point last year. That is a drop of about twenty-eight percent. In the third quarter alone, four thousand, eight hundred thirty, against six thousand, four hundred twelve. A drop of about twenty-five percent. In September, sixteen hundred twenty, down about nine percent.""",
   "Hyundai Santa Cruz sales lot", "2026 YTD: 14,811, DOWN ABOUT 28%")
sc("""Now compare. The Maverick sold one hundred twenty-three thousand, six hundred eighty-one through September, up from one hundred twenty thousand, nine hundred four. In the third quarter, forty-one thousand, nine hundred seventy, up twenty point four percent. And the Maverick Hybrid alone sold twenty-seven thousand, seven hundred ninety-three in the third quarter, up almost sixty percent, a record. That one quarter of hybrids is nearly double the Santa Cruz for the whole nine months.""",
   "Ford Maverick Hybrid pickup", "ONE QUARTER OF MAVERICK HYBRIDS = 1.9X SANTA CRUZ YTD")
sc("""Autoevolution's own text has a mistake, so we checked. It says two thirds of Maverick deliveries were hybrids. But seventy-four thousand, three hundred, divided by one hundred twenty-three thousand, six hundred eighty-one, is about sixty percent. So the hybrid share is about six in ten, not two thirds. The conclusion still holds. The hybrid is carrying the Maverick, and the Santa Cruz has no answer to it.""",
   "Ford Maverick Hybrid sales", "CORRECTION: HYBRID SHARE IS ABOUT 60%")
sc("""The Honda Ridgeline, for context, sold thirty-seven thousand and twenty-eight through September, and four thousand, four hundred seventeen in September alone, up twenty-four point four percent. So the class is not dead. The Ridgeline and the Maverick are growing. Only the Santa Cruz is shrinking, which suggests that the problem is the truck's position, not buyers' interest in small trucks.""",
   "Honda Ridgeline pickup", "RIDGELINE YTD: 37,028. MAVERICK UP.")

# 4 OWNERS
sc("""Now the paradox. Owners like it. On Kelley Blue Book, the Santa Cruz has a four point five out of five rating from forty consumer reviews. The sub-scores include four point seven for reliability and four point seven for styling, four point six for comfort. Praise focuses on versatility, styling and the bed. Complaints include interior plastics, visibility and rear air vents on the lower trims.""",
   "Hyundai Santa Cruz interior", "OWNERS: 4.5 OUT OF 5")
sc("""Safety and warranty are strong too. The National Highway Traffic Safety Administration gave it five stars overall. Hyundai's warranty is five years and sixty thousand miles basic, ten years and one hundred thousand miles for the powertrain. Consumer Reports predicts a reliability score of four out of five, the same as the Frontier, according to the Inquirer. On paper, this is a solid truck.""",
   "Hyundai Santa Cruz crash test", "5 STARS. 10-YEAR POWERTRAIN WARRANTY.")
sc("""The Inquirer review adds some driving numbers. The XRT with the turbo goes from zero to sixty in six and a half seconds, according to Motor Trend, and the writer says it beats the Frontier by almost a second. For twenty twenty-six, an eight speed automatic replaced the dual clutch on the XRT and Limited. The reviewer saw about twenty miles per gallon. Car and Driver lists the limits as the bed, the turbo upcharge and the limited off-road ability.""",
   "Hyundai Santa Cruz driving", "0-60 IN 6.5 SECONDS (MOTOR TREND)")
sc("""So here is the paradox. Owners give it high marks. Safety is strong. The warranty is long. And still the truck sells twenty-eight percent fewer units. The answer is probably price and size. A forty-four thousand dollar XRT is expensive for a four foot bed. A Maverick costs less at the start, according to The Autopian. The article lists twenty-nine thousand, eight hundred forty dollars for the Maverick against thirty-one thousand, three hundred fifty for the Santa Cruz.""",
   "Ford Maverick XL pickup", "MAVERICK $29,840. SANTA CRUZ $31,350.")

sc("""Let us look closer at why the Maverick wins, because the reason is simple. It starts at a lower price. It is rated at thirty-eight miles per gallon combined, according to The Autopian. And it is sold in far larger numbers, which means more dealers, more parts, and more used trucks to choose from later. The Santa Cruz has a better turbo engine and a more car-like design, but a buyer who is shopping with a calculator will usually end up on the Maverick side.""",
   "Ford Maverick Hybrid pickup", "WHY THE MAVERICK WINS: PRICE, MPG, SCALE")
sc("""There is also a question of what a buyer wants to carry. The Santa Cruz bed is four feet long and holds twenty-seven cubic feet, and the Maverick bed is four and a half feet long, according to The Autopian. That half foot matters for things like a mountain bike, a few bags of mulch, or two sheets of plywood. If your hauling is occasional, either truck works. If it is every week, the bed will decide the purchase before the engine does.""",
   "Hyundai Santa Cruz bed cargo", "BED: 4.0 FT VS 4.5 FT")
sc("""Now think about what happens to the owner of a truck that may not get a successor. The warranty stays in place, and Hyundai has to keep supplying parts for years. That part is not a real risk. The real risk is resale. If buyers believe a model is ending, used prices can fall faster. We do not have a resale figure for the Santa Cruz in our sources, so we will not invent one. But it is fair to say that this is the number a careful buyer should ask the dealer about.""",
   "Hyundai Santa Cruz used truck", "THE REAL RISK IS RESALE, NOT PARTS")
sc("""And what about the twenty twenty-seven price? Kelley Blue Book lists the range as thirty-one thousand, nine hundred fifty to forty-four thousand, four hundred twenty-five dollars. At the same time it shows a deal ending November second, so dealers are willing to move trucks. A buyer who is patient, and who has a Maverick quote in hand, can use it as leverage. The best time to negotiate on a model with high inventory is when the dealer has had the truck for months.""",
   "Hyundai Santa Cruz dealership", "HIGH INVENTORY MEANS ROOM TO NEGOTIATE")
sc("""Finally, a note about reading headlines. The first report said the Santa Cruz was dead. Hyundai did not confirm it, and then it confirmed the opposite, that the truck continues. Both can be true, because a model can continue for a year and still be near the end. Companies rarely announce an ending far in advance. So treat a continuing model as a truck with an uncertain future, and decide whether that uncertainty matters to you.""",
   "Hyundai Santa Cruz pickup", "CONTINUES FOR 2027, NOT FOREVER")

# 5 THE FUTURE
sc("""Part four, what comes next. Hyundai confirmed a new midsize body-on-frame pickup at its twenty twenty-five CEO Investor Day. The company says it will reach the United States before twenty thirty. Automotive News reports twenty twenty-nine. The Autopian expects it to be bigger than the Santa Cruz, and to compete with the Ford Ranger, the Chevrolet Colorado, the Toyota Tacoma and the Honda Ridgeline.""",
   "Hyundai pickup concept", "NEXT: A MIDSIZE TRUCK BEFORE 2030")
sc("""That tells us what the Santa Cruz was. It was Hyundai's test. The company called it a new type of consumer, one who values capability, versatility and rugged image. So the Santa Cruz may have done its job, even if it did not sell like a hit. It showed Hyundai that Americans would buy a Hyundai pickup. The next one is the real attempt.""",
   "Hyundai Santa Cruz night", "THE TEST TRUCK")

# 6 BUYERS
sc("""Should you buy one? If you want a small, stylish truck with a long warranty and you do not tow much, yes, with one condition. Discounts. Kelley Blue Book lists a deal on the SE that ends November second, with financing at three point four nine percent for up to sixty months, up to twelve hundred fifty dollars in cash savings, or a lease at three hundred forty-nine dollars a month for thirty-six months. Check whether it is still valid.""",
   "Hyundai Santa Cruz SE pickup", "DEAL ENDS NOV 2: 3.49% APR OR $349/MO")
sc("""If you tow, or if you want better fuel economy, the Maverick is the safer choice, especially the hybrid. If you want more capability, the Frontier tows nearly seven thousand pounds. And if you want a truck that will keep its parts and service for years, remember that an orphan truck is a risk. Hyundai says the Santa Cruz continues. But the company has not promised a second generation.""",
   "Ford Maverick Hybrid XLT pickup", "TOW OR SAVE FUEL? MAVERICK OR FRONTIER.")
# NEWSCENES
sc("""Let us compare two numbers from the sales section, because together they say a lot. The Maverick sold one hundred fifty-five thousand and fifty-one trucks in twenty twenty-five, and the Santa Cruz sold twenty-five thousand, four hundred ninety-nine. When one truck sells six times as many as another, the smaller one gets fewer dealers who care about it, fewer used examples to compare, and fewer accessories. That is not a flaw in the truck. It is the cost of being small in a market that rewards scale.""",
   "Ford Maverick pickup", "SCALE MATTERS: 155,051 VS 25,499")
sc("""Now the engine choice. The base Santa Cruz has one hundred ninety-one horsepower, and the XRT with the turbo has two hundred eighty-one. That is a big step, and it also changes towing from three thousand, five hundred pounds to five thousand. So the turbo is not only about speed. It is the difference between a truck that can pull a small trailer and one that can pull a larger one. If you will ever tow, the base engine is probably the wrong place to save money.""",
   "Hyundai Santa Cruz XRT turbo pickup", "THE TURBO CHANGES THE TOW RATING")
sc("""But the turbo costs money. Kelley Blue Book lists the SE at thirty-one thousand, nine hundred fifty dollars and the XRT at forty-four thousand, four hundred twenty-five. That is a long climb for a truck with a four foot bed. A buyer should ask honestly whether the extra power is needed. If you want performance, the XRT is the one. If you want a small, stylish truck for commuting and light hauling, the lower trims already cover most of what the truck does well.""",
   "Hyundai Santa Cruz SE pickup", "XRT: POWER. SE: VALUE.")
sc("""Here is how to check the deal that Kelley Blue Book lists. The offer on the SE ends November second, with financing at three point four nine percent for up to sixty months, up to twelve hundred fifty dollars in cash savings, or a lease. Offers like this usually have conditions, and you often cannot combine them. Ask the dealer which offers apply to the exact truck on the lot, and ask for the out-the-door price in writing with each offer applied. Then compare.""",
   "Hyundai Santa Cruz dealer deal", "ASK WHICH OFFER APPLIES TO THIS TRUCK")
sc("""A common buyer mistake with a model that may be ending is to assume a big discount means a bargain. A discount can mean the dealer needs to move inventory, which is good for you. It can also mean the market values the truck less, which shows up when you sell. The Autopian said dealers held nearly five months of supply. So take the discount, but do not count it as proof that the truck is a great value over time.""",
   "Hyundai Santa Cruz inventory lot", "A DISCOUNT IS NOT PROOF OF VALUE")
sc("""Warranty is where the Santa Cruz is genuinely comforting. Five years and sixty thousand miles basic, ten years and one hundred thousand miles for the powertrain. Before you rely on that, ask the dealer for the warranty booklet and read what it says about transfer to a second owner and about required maintenance. Warranties usually require that you follow the service schedule. Keep every receipt. If a claim ever comes up, the paperwork is what protects you.""",
   "Hyundai Santa Cruz service", "READ THE WARRANTY TERMS, KEEP RECEIPTS")
sc("""Let us compare the Santa Cruz with the Ridgeline for a moment, since they are the two car-like trucks. The Ridgeline sold thirty-seven thousand and twenty-eight through September, and it is growing. The Santa Cruz sold fourteen thousand, eight hundred eleven and it is shrinking. Both are comfortable and unconventional. So the market is not rejecting the idea. It is choosing which version it likes, and right now it is choosing the other ones.""",
   "Honda Ridgeline pickup", "SAME IDEA, DIFFERENT SALES TREND")
sc("""So who is the Santa Cruz right for? A person who wants a small truck that drives like a crossover, who tows little, who likes the styling, and who values a long warranty. Someone who will keep it for years and does not worry about what it is worth later. Who should wait? Anyone who tows a lot, anyone who cares about fuel economy, and anyone who wants to know what Hyundai will do next. For them, the Maverick or a future Hyundai may fit better.""",
   "Hyundai Santa Cruz Limited pickup", "WHO IT SUITS AND WHO SHOULD WAIT")

sc("""One more way to use what we have covered. Write down the three things that matter most to you in a small truck. For some people it is price, for some it is fuel economy, and for others it is the bed or the towing. Then score the Santa Cruz and the Maverick against your own list, using the figures in this video. The truck that wins on your list is the right one, whatever the headlines say about which model is ending.""",
   "Hyundai Santa Cruz and Ford Maverick pickups", "SCORE THEM ON YOUR OWN LIST")

sc("""So what should you check before you buy a Santa Cruz? First, the real price, with the discount, against the Maverick. Second, the trim, because the turbo is what gives you the power and the towing. Third, parts and service, since the model may be a short run. And fourth, resale, which is the number nobody can promise. The Twenty Twenty-Seven Truck Buyer's Guide has this checklist. The link is in the description and in the pinned comment.""",
   "Hyundai Santa Cruz pickup", "CHECK 1, 2, 3 AND 4")
sc("""If you want to see how the Ford Maverick Hybrid compares in more detail, subscribe, because that comparison is coming. Thanks for watching.""",
   "Ford Maverick pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In February, a report": "Intro", "Part one": "1. The report: is it dead?", "Part two": "2. Hyundai says it continues",
      "Towing is the first": "Towing and bed", "Part three": "3. The sales gap", "Now the paradox": "4. Owners love it",
      "Part four": "5. What comes next", "Should you buy": "Should you buy one?", "So what should you check": "What to check before you buy"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video19", "length_scale": 1.55,
  "title": "Hyundai Santa Cruz: Dead or Alive for 2027? The Real Numbers", "scenes": S}, open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
