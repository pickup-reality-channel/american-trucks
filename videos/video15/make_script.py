import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One pickup truck jumped seventy-three percent in a single quarter, while the best-selling truck in America was almost flat. And the reason is not a new design, or a price cut. It is an engine that the company had dropped, and a warranty that was supposed to end. Ram is surging in twenty twenty-six, and here is the real story, with the numbers, and the catch that nobody mentions.""",
   "Ram 1500 pickup truck", "WHY RAM IS SURGING IN 2026")

# ---------- COLD OPEN ----------
sc("""In the third quarter of twenty twenty-six, Ram sold one hundred thirty-four thousand, seventy-two vehicles in the United States, up twenty-nine percent from one hundred three thousand, seven hundred seventeen a year earlier. That is according to MoparInsiders, reporting the Stellantis figures on October second. In a quarter when Stellantis as a whole was flat, Ram carried it.""",
   "Ram 1500 Big Horn pickup", "RAM Q3 2026: 134,072 (+29%)")
sc("""The truck at the center of it is the Ram one thousand five hundred. In the third quarter, it sold seventy-six thousand, six hundred fifty, up seventy-three percent from forty-four thousand, three hundred forty-nine. Through nine months, it sold two hundred two thousand, one hundred forty-seven, up forty-one percent. Those are the biggest gains of any full-size truck in the table that we use throughout this series.""",
   "Ram 1500 pickup", "RAM 1500: 76,650 IN Q3 (+73%)")
sc("""Every number in this video comes from a published source, and the sources are listed in the description. We used MoparInsiders for the Stellantis figures, Autoblog for the explanations, Pickup Truck Talk for the nine-month table, and the J.D. Power and iSeeCars studies for the quality, resale and longevity numbers. Where we could not confirm something, we say so.""",
   "Ram 2500 pickup", "SOURCES: MOPARINSIDERS, AUTOBLOG, PUTT")
sc("""There is a twist in each part of this story. One engine came back. One warranty almost ended. One rival brand was passed by Ram for the first time in seventeen years. And one set of reliability numbers is not good. Stay with me, because the last twist is the most important one if you are thinking about buying a Ram in twenty twenty-seven.""",
   "Ram 1500 Rebel pickup", "FIVE TWISTS ON THE RAM STORY")

# ---------- 1. THE HEMI ----------
sc("""Number one is the engine, the five point seven liter Hemi V eight. According to Autoblog, Ram dropped the Hemi for twenty twenty-five, replacing it with the new twin-turbo Hurricane inline six. And then it brought the Hemi back. Autoblog writes that, under new leadership, Ram brought back the five point seven liter Hemi V eight, and calls it a big part of the draw.""",
   "Ram 1500 Hemi V8 engine", "THE HEMI IS BACK")
sc("""The twist is what that says about buyers. Autoblog suggests that Ram underestimated how much buyers value the sound, the feel and the familiarity of a V eight. And Ram is not alone in noticing. According to the same article, Ford is adding V eight options to the F-one-fifty, and General Motors is investing one billion dollars in a new generation of V eight engines. So the industry's answer to the electric future, in the middle of twenty twenty-six, includes the engine it was supposed to replace.""",
   "Chevrolet Silverado V8 engine", "FORD AND GM ARE ADDING V8S TOO")
sc("""There is a catch about the Hemi, and it is about towing. According to Autoblog's comparison of the twenty twenty-six trucks, the Hemi is rated at eleven thousand, three hundred twenty pounds, only a few hundred pounds below the Hurricane at eleven thousand, six hundred ten. So buyers who choose the V eight are not giving up much towing. But the same article says the Ram's maximum is about two thousand pounds below the best Ford. Choosing the engine is a feeling, and not a towing decision.""",
   "Ram 1500 towing trailer", "HEMI TOWS 11,320 LB")

# ---------- 2. THE WARRANTY ----------
sc("""Number two is the warranty. According to Autoblog, Ram offers a ten year, one hundred thousand mile powertrain warranty. Ram planned to end the offer in January, and then extended it through the twenty twenty-six model year, after what Autoblog calls reported overwhelming customer and dealer feedback. Ford and Chevrolet offer five years and sixty thousand miles of powertrain coverage.""",
   "Ram 1500 pickup truck dealership", "10-YEAR/100,000-MILE POWERTRAIN WARRANTY")
sc("""The twist is who it helps. Autoblog says that a longer warranty helps buyers who finance over longer periods, because the truck stays covered for most of the loan. A buyer on an eighty-four month loan is still paying seven years from now, and a warranty that lasts ten years gives them cover for all of it. That is a real advantage, and it costs Ram money, which may be why the company planned to end it.""",
   "Ram 1500 Laramie pickup", "WARRANTY FOR LONG LOANS")
sc("""And there is a second half to the story. A headline from Torque News said that Ram one thousand five hundred sales jumped seventy-three percent, and owners credit the Hemi, but that discounts averaging seven thousand, nine hundred forty-one dollars tell the rest of the story. We could not open the full article, so we cannot confirm how that discount figure was measured. But the headline is a reminder to ask what a truck really sold for.""",
   "Ram 1500 pickup", "HEADLINE: DISCOUNTS AVERAGING $7,941")

# ---------- 3. RAM VS JEEP ----------
sc("""Number three is the Jeep, the other half of Stellantis. In the third quarter, the Jeep brand sold one hundred twenty-eight thousand, five hundred forty-two, down twenty percent from one hundred sixty thousand, five hundred sixty-four. Through nine months, Jeep fell eight percent, to four hundred thirteen thousand, seven hundred ninety-three. MoparInsiders says Jeep had a tougher three months overall.""",
   "Jeep Wrangler Gladiator", "JEEP Q3: 128,542 (-20%)")
sc("""Now the twist. Ram sold one hundred thirty-four thousand, seventy-two in the same quarter, more than Jeep. A headline from GCN said that a pickup brand sold that number of trucks in one quarter, edging past its longtime Stellantis stablemate SUV brand for the first time since Ram split from Dodge seventeen years ago. We could not open that article either, but the numbers from MoparInsiders support the comparison.""",
   "Ram 1500 pickup truck", "RAM 134,072 VS JEEP 128,542")
sc("""And one of Jeep's own trucks is part of the picture. The Jeep Gladiator sold thirty thousand, nine hundred forty-four through nine months, down nineteen point seven percent, and fell almost thirty-three percent in the second quarter. So in the same company, one pickup brand is surging, and the pickup that carries the other brand's name is shrinking. The company is not one story. It is two.""",
   "Jeep Gladiator pickup", "GLADIATOR: -19.7%")

# ---------- 4. THE HEAVY-DUTY ----------
sc("""Number four is the part of Ram that is not surging, the heavy-duty trucks. According to MoparInsiders, the Ram heavy-duty sold forty-one thousand, one hundred seven in the third quarter, down six percent from forty-three thousand, seven hundred seventeen. For the nine months, it is up three percent, to one hundred twenty-three thousand, two hundred one.""",
   "Ram 2500 pickup", "RAM HD: Q3 -6%, 9 MONTHS +3%")
sc("""The twist is that the surge is not across the whole line. It is in the light-duty truck, the Ram one thousand five hundred, up forty-one percent. The heavy-duty trucks are tracking the rest of the heavy-duty class, which fell more than six percent through nine months. So the engine and the warranty may matter most to the buyer of an everyday truck, and less to the buyer of a work truck, who buys for capability.""",
   "Ram 3500 pickup", "THE SURGE IS IN THE 1500")

# ---------- 5. WHAT'S NEXT ----------
sc("""Number five is what comes next, and it is the Ram one thousand five hundred REV. The range-extended truck is expected in mid-April of twenty twenty-seven, according to a supplier memo reviewed by Automotive News. It has a three point six liter Pentastar V six that runs as a generator, and it will be built at Sterling Heights in Michigan. Ram has not published a price, a range, or a towing figure.""",
   "Stellantis Sterling Heights Assembly Plant", "NEXT: THE 1500 REV, MID-APRIL 2027")
sc("""The twist is the contrast. Ram's surge in twenty twenty-six came from a V eight and a long warranty, and not from an electric truck. And the new truck is neither. So the question for the company is whether the buyers who came for the Hemi will also come for a truck with a generator. That is something the sales numbers of twenty twenty-seven will answer, and we will report them when they come.""",
   "Ram 1500 REV pickup", "THE HEMI BUYER VS THE REV")


# ---------- THE PRICE AND THE RIVALS ----------
sc("""Let's look at what a Ram costs compared with its rivals, using the TFL Car landed price analysis. The Ram one thousand five hundred Big Horn cost forty-nine thousand, five hundred forty-one dollars in twenty twenty-six, up six point four percent from twenty twenty-four, and down six tenths of a percent after inflation. The Ford F-one-fifty XLT cost fifty-two thousand, five hundred ninety, and the Chevrolet Silverado LT fifty-six thousand, two hundred ninety.""",
   "Ram 1500 Big Horn pickup", "BIG HORN $49,541. F-150 XLT $52,590.")
sc("""So the Ram is about three thousand dollars below the Ford, and about six thousand, seven hundred fifty dollars below the Chevrolet. The trims are not identical, and TFL Car says so. But in a year when the cost of trucks rose, a Ram that is cheaper than its two main rivals, with a bigger warranty and the engine many buyers wanted, is a simple story. It does not need a complicated explanation.""",
   "Ram 1500 Laramie pickup", "RAM: $3,000 BELOW FORD, $6,750 BELOW CHEVY")
sc("""And look at the size of the change over a year. Through nine months of twenty twenty-five, Ram pickups sold two hundred sixty-two thousand, three hundred eighty-six. Through nine months of twenty twenty-six, three hundred twenty-five thousand, three hundred forty-eight. That is sixty-two thousand, nine hundred sixty-two more trucks. That is more than the entire Ford Ranger sold in the same nine months, which was fifty-one thousand, six hundred thirty, and more than half of what the Toyota Tundra sold.""",
   "Ram 1500 pickup truck", "+62,962 TRUCKS IN ONE YEAR")
sc("""There is also the matter of what Ram's rivals did. Ford's F-Series, without the Lightning, fell six point eight percent through nine months. The Chevrolet Silverado was down less than one percent. The GMC Sierra was flat. So the extra sixty-three thousand trucks that Ram sold, and the forty thousand that Ford lost, are a large share of the same buyers. It is a market where one company's gain is often another's loss.""",
   "Ford F-150 Chevrolet Silverado pickups", "FORD -40,808. RAM +62,962.")
sc("""What should a buyer take from that? Competition is working in your favor right now. Ram has momentum, Ford is recovering in the third quarter, and General Motors is adding V eights. That means every company has a reason to make a deal. Compare the same truck from all three, ask for the full price in writing, and use each offer to improve the others. That is the most reliable way to turn a market surge into savings.""",
   "Ford F-150 pickup", "USE THE COMPETITION")
sc("""One more point about the warranty. A ten year, one hundred thousand mile powertrain warranty covers the engine, the transmission and the drive system, according to the general meaning of a powertrain warranty. It does not cover everything on the truck. The electronics, which are the area where reviewers have criticized Ram, are not necessarily in that coverage. So read the warranty booklet, and ask the dealer what is covered and what is not.""",
   "Ram 1500 pickup", "READ THE WARRANTY BOOKLET")

# ---------- THE CATCH ----------
sc("""Now the catch that we promised. Sales are one thing, and quality is another. Pickup Truck Talk ranked the Ram one thousand five hundred second in its July reliability ranking, citing mostly electronics and build quality problems, and an ABS software recall that covered over a million trucks. J.D. Power's twenty twenty-five quality and reliability score for the Ram is seventy-seven out of one hundred, the lowest of the five full-size trucks.""",
   "Ram 1500 pickup", "CATCH: JD POWER Q&R 77 OF 100")
sc("""And there is a conflict, which we want to be fair about. The twenty twenty-six J.D. Power Vehicle Dependability Study ranked the Ram first among trucks, up from fourth, with Ram saying it improved thirteen points in a year. That study looked at twenty twenty-three model year trucks after three years of ownership. So an owner survey puts the Ram first, and a reporter's analysis puts it second, and a quality score puts it last. All three are true at the same time.""",
   "Ram 1500 Tradesman pickup", "SURVEY #1. RANKING #2. SCORE: LAST.")
sc("""Resale is the other side of the catch. According to iSeeCars, the Ram one thousand five hundred keeps sixty-one point eight percent of its value after five years. That is the best of the Detroit half-tons, but about eighteen points behind the Tundra. And in the longevity study, the Ram one thousand five hundred is not in the top twelve. So the surge in sales has not yet turned into the best resale, or the best longevity numbers, for the everyday truck.""",
   "Ram 1500 pickup truck", "RESALE: 61.8%")

# ---------- THE LESSON ----------
sc("""So what is the final twist? Sales surge when a company listens to what buyers actually want. Ram listened on the engine, and on the warranty, and it was rewarded with seventy-three percent growth in a quarter. But a surge does not make a truck more reliable, and it does not change what the truck will be worth in five years. The lesson for a buyer is that popularity and quality are two separate numbers, and you should look up both.""",
   "Ram 1500 pickup", "POPULARITY IS NOT QUALITY")
sc("""If you are thinking about a Ram in twenty twenty-seven, here is a simple approach. Check the warranty terms for the exact model year, because the ten year offer was extended only through the twenty twenty-six model year. Check the recalls for the year you want. Compare the price you are offered with the Ford and the Chevrolet. And ask how the Hemi or the Hurricane has done in the model year you are considering.""",
   "Ram 1500 Big Horn pickup", "WARRANTY IS FOR MODEL YEAR 2026")

# ---------- BUYER GUIDE: HOW TO USE THESE NUMBERS ----------
sc("""Before the checklist, let's talk about what the surge means for you. A seventy-three percent gain in a quarter is a headline about the company's sales, and not a promise about your truck. Ram sold more trucks because buyers liked the Hemi and the long warranty. That tells you what buyers wanted. It does not tell you how a particular truck will hold up, what it will be worth later, or how the dealer will treat you. Those are separate questions, and each one needs its own check.""",
   "Ram 1500 pickup truck", "A SURGE IS NOT A PROMISE")
sc("""Now the price. The Torque News headline spoke of discounts averaging seven thousand, nine hundred forty-one dollars, and we could not confirm how that was measured. So here is a way to protect yourself. Ask each dealer for the out-the-door price in writing, listing the truck, the discount, the fees and the taxes on separate lines. Then compare the final number, not the discount. A large discount from a high starting price can end up above a small discount from a lower one, and only the final number shows that.""",
   "Ram 1500 Big Horn pickup", "COMPARE THE FINAL NUMBER, NOT THE DISCOUNT")
sc("""Then the recall check. The ABS software recall covered over a million trucks, and a recall that was announced is not the same as a recall that was done on the truck you are buying. Take the VIN, run it through the official recall lookup, and ask the dealer for proof that any open work was completed. Do this for the exact model year, because problems can differ from one year to the next. It takes a few minutes, it is free, and it is the single most useful thing you can do with a number from a headline.""",
   "Ram 1500 pickup", "RUN THE VIN THROUGH A RECALL CHECK")
sc("""About the warranty, one more practical step. The ten year, one hundred thousand mile offer was extended only through the twenty twenty-six model year. So ask the dealer for the warranty terms in writing for the exact truck, with the model year and the date it starts. Ask what it covers, since a powertrain warranty is not a promise about everything. And if you are buying a used Ram, ask whether the coverage applies to a second owner. The answer may be different from what you expect, and it is better to know before you sign.""",
   "Ram 1500 Laramie pickup", "GET THE WARRANTY TERMS IN WRITING")
sc("""Now the engines, Hemi against Hurricane. The towing ratings are close, eleven thousand, three hundred twenty pounds for the Hemi and eleven thousand, six hundred ten for the Hurricane. So the real difference is how each one feels and sounds, and that is something only a test drive can tell you. If you tow near the limit, remember that the Ram's maximum is about two thousand pounds below the best Ford, and check the rating for your exact truck on the door sticker. Drive both engines back to back, on the same day, on the same road.""",
   "Ram 1500 Hemi V8 engine", "DRIVE BOTH ENGINES BACK TO BACK")
sc("""Who suits a Ram right now, and who should wait? It suits the everyday driver who wants a V eight, a lower price than the Ford and the Chevrolet, and a long loan covered by a long warranty. It may not suit a buyer whose first concern is resale, since the Ram keeps sixty-one point eight percent while the Tundra is about eighteen points higher. And a buyer who wants the range-extended truck should wait until mid-April of twenty twenty-seven, when Ram is expected to show it, with no price or towing figure yet.""",
   "Ram 1500 Big Horn pickup", "WHO IT SUITS, AND WHO SHOULD WAIT")
sc("""And the mistakes. Buying because everyone else is buying. Reading one survey, the one that puts Ram first, and ignoring the quality score at seventy-seven out of one hundred. Signing a deal without seeing the warranty booklet. Letting a long loan hide a high price, since a low monthly payment can sit on top of a bad deal. And buying the first truck you drive. Compare the same truck from all three brands, on the same day, and let the written numbers decide.""",
   "Ram 1500 Rebel pickup", "COMMON BUYER MISTAKES")

sc("""A short routine for the day you go shopping. Bring the numbers with you, the Ram price from TFL Car, the Ford and the Chevrolet prices, and the warranty terms you want. Ask each dealer for the out-the-door price in writing. Ask for the warranty booklet for the model year. Run the VIN for recalls before you talk about money. Then compare the three written offers at home, away from the pressure of the showroom. The surge in sales may be real, but your deal is a separate thing, and it is the only one you control. Take your time, bring a friend who will ask the awkward questions, and remember that you are always free to walk out and come back tomorrow.""",
   "Ram 1500 pickup truck", "A SHORT ROUTINE FOR SHOPPING DAY")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a Ram, or any truck, in twenty twenty-seven? First, the warranty for the exact model year. Second, the recalls and known problems. Third, the five-year resale value. And fourth, the real price, with the incentives and the fees, compared across brands. We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Ram 1500 pickup", "CHECK 1, 2, 3 AND 4")
sc("""If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. And tell us in the comments which truck you think will surprise the market next. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One pickup truck jumped": "Intro", "Number one": "1. The Hemi V8", "Number two": "2. The warranty",
      "Number three": "3. Ram passes Jeep", "Number four": "4. The heavy-duty Ram", "Number five": "5. What comes next",
      "Now the catch that we promised": "The catch", "So what is the final twist": "The final twist",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video15", "length_scale": 1.55,
  "title": "Why Ram Trucks Are Surging in 2026 (And the Catch Nobody Mentions)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
