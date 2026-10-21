import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Ford sold seventy-four thousand, three hundred hybrid Mavericks in nine months. That is more than five times what the Hyundai Santa Cruz sold in the same nine months. Meanwhile, two of Detroit's biggest electric truck plans were rewritten around a gas engine, and a third is rumored. The pickup truck is going hybrid, and the numbers show who is winning. Here is the real story of the hybrid truck rush.""",
   "Ford Maverick hybrid pickup", "THE HYBRID TRUCK RUSH")

# ---------- COLD OPEN ----------
sc("""For years, the future of the pickup truck was supposed to be electric. Then buyers did what buyers do. They looked at the price, they looked at the charger, and they chose something in the middle. A truck with an electric motor that does not need a plug. A truck with a battery, and a gas tank, and no range anxiety. And the carmakers noticed, one by one, in public.""",
   "Ford F-150 pickup truck", "THE MIDDLE PATH")
sc("""In December of twenty twenty-five, Ford's chief executive, Jim Farley, said that hybrids are more than just economical now, and have been more popular than the company ever expected. Hybrids, Ford said, were thirty percent of its sales mix, and hybrid sales rose thirty percent in the most recent month while overall sales were flat. A few months later, Ford, Ram and, reportedly, General Motors were all building their next trucks around that idea.""",
   "Ford Rouge Complex Dearborn factory", "FORD: HYBRIDS 30% OF SALES MIX")
sc("""So today we look at six hybrid trucks and hybrid plans, and there is a twist in every one of them. One hybrid outsold its own gas version. One hybrid truck grew four hundred percent in a single year. One plan was rewritten after a cancelled electric truck. And one is only a rumor, and we will say so clearly. Every number comes from a published source, and the sources are listed in the description.""",
   "Toyota Tacoma pickup truck", "EVERY NUMBER IS SOURCED")

# ---------- 1. FORD MAVERICK HYBRID ----------
sc("""Number one is the Ford Maverick Hybrid, and it is the clearest winner in this video. Through the first nine months of twenty twenty-six, Ford sold seventy-four thousand, three hundred Maverick Hybrids, a record for the truck. In the third quarter alone it sold twenty-seven thousand, seven hundred ninety-three, a third-quarter record, up fifty-nine point six percent from the same quarter a year earlier.""",
   "Ford Maverick Hybrid pickup", "MAVERICK HYBRID: 74,300 IN 9 MONTHS")
sc("""Now look at what that means for the whole Maverick. Ford sold one hundred twenty-three thousand, six hundred eighty-one Mavericks through nine months. The hybrid was seventy-four thousand, three hundred of them, or about sixty percent. In the third quarter, the hybrid was twenty-seven thousand, seven hundred ninety-three out of forty-one thousand, nine hundred seventy, or about two thirds. The hybrid is not an option anymore. It is the Maverick.""",
   "Ford Maverick pickup", "HYBRID: ~60% OF ALL MAVERICKS")
sc("""Here is the twist. The Maverick Hybrid set records in the second quarter too, with twenty-nine thousand, four hundred fifty-seven, up nineteen point three percent. But the first half of the year, at forty-six thousand, five hundred seven, was not enough to make the total Maverick grow. It took the third quarter's jump to push the whole nine months above last year. The hybrid carried the truck. The compact pickup market had no other winner.""",
   "Ford Maverick Lariat Hybrid", "Q2: 29,457. Q3: 27,793.")
sc("""And look at the compact truck next to it. The Hyundai Santa Cruz sold fourteen thousand, eight hundred eleven trucks in nine months, down twenty-eight percent. That is fewer than Ford sold in a single quarter of Maverick Hybrids. A Maverick XL Hybrid with front-wheel drive starts at twenty-eight thousand, one hundred forty-five dollars, according to autoevolution. A small truck with a hybrid system, at a small truck price, won the segment.""",
   "Hyundai Santa Cruz pickup", "SANTA CRUZ: 14,811 IN 9 MONTHS")

# ---------- 2. FORD F-150 HYBRID ----------
sc("""Number two is the Ford F-one-fifty Hybrid, and its story is about a different kind of buyer. Through the first half of twenty twenty-six, Ford sold twenty-four thousand, five hundred ninety-six of them, and Ford calls it America's best-selling full-size hybrid pickup. Through nine months, the number was thirty-four thousand, five hundred twenty-seven. That means about nine thousand, nine hundred thirty-one were sold in the third quarter.""",
   "Ford F-150 PowerBoost hybrid pickup", "F-150 HYBRID: 34,527 IN 9 MONTHS")
sc("""Now put that number in context. The F-Series sold five hundred sixty-one thousand, five hundred eight trucks through nine months, counting the Lightning. The F-one-fifty Hybrid is about six percent of that. In the full-size truck market, hybrids are still a small slice. But a slice of thirty-four thousand trucks is bigger than the entire electric Lightning, which sold four thousand, seven hundred seventy in the same months.""",
   "Ford F-150 pickup truck", "HYBRID: ~6% OF F-SERIES")
sc("""That is the twist. The F-one-fifty Hybrid outsold the F-one-fifty Lightning by more than seven to one in the first nine months of the year. One truck cost Ford a nineteen point five billion dollar charge. The other quietly sold thirty-four thousand units. And it explains why Ford's new plan for the Lightning, an extended-range electric truck with a generator, looks so much like a hybrid.""",
   "Ford F-150 Lightning pickup", "HYBRID BEAT LIGHTNING 7 TO 1")

# ---------- 3. TOYOTA TACOMA HYBRID ----------
sc("""Number three is the Toyota Tacoma Hybrid, and its numbers are the most dramatic. According to Autoblog, in the first nine months of twenty twenty-four, Toyota sold four thousand, five hundred twenty-six Tacoma Hybrids. In the same months of twenty twenty-five, twenty-two thousand, seven hundred seventy-three. That is a jump of four hundred three percent. One caveat from the article: the hybrid was not on sale for all of twenty twenty-four.""",
   "Toyota Tacoma Hybrid pickup", "TACOMA HYBRID: +403%")
sc("""The reason is not mysterious. The hybrid Tacoma uses a two point four liter turbocharged engine with electric motors, and Autoblog lists it at three hundred twenty-six horsepower and four hundred sixty-five pound-feet of torque. The best non-hybrid Tacoma makes two hundred seventy-eight horsepower and three hundred seventeen pound-feet. And it is rated at up to twenty-three miles per gallon combined with four-wheel drive, against twenty-one for the non-hybrid.""",
   "Toyota Tacoma TRD pickup", "326 HP VS 278 HP")
sc("""Here is the twist, and it is a very honest one. The hybrid Tacoma is more powerful and more efficient. Autoblog says total Tacoma sales rose just over sixty percent in the same period, so the hybrid grew much faster than the lineup. But growth from a small base is not the same as market share, and the article does not give a share number. So we will not guess one.""",
   "Toyota Tacoma pickup", "BIG GROWTH FROM A SMALL BASE")

# ---------- 4. RAM 1500 REV ----------
sc("""Number four is the Ram one thousand five hundred REV, which is the hybrid that used to be an electric truck. In September of twenty twenty-five, Ram cancelled the battery-only version. It kept the name, and changed the truck to a range-extended one. A four hundred volt battery drives the electric motors, and a three point six liter Pentastar V six runs only as a generator. It never turns the wheels.""",
   "Ram 1500 pickup truck", "RAM REV: V6 GENERATOR ONLY")
sc("""And here is the twist. The launch, according to a supplier memo reviewed by Automotive News, has now slipped to mid-April twenty twenty-seven. Ram's official line is that plans continue to be a twenty twenty-seven arrival. The truck will be built at the Sterling Heights Assembly Plant in Michigan. And Ram has not published a price, an electric range, or a towing capacity. So this is a hybrid with no numbers, and we will wait for them before judging it.""",
   "Stellantis Sterling Heights Assembly Plant", "REV: MID-APRIL 2027, NO PRICE YET")

# ---------- 5. FORD LIGHTNING ----------
sc("""Number five is the next Ford Lightning, the electric truck that is coming back as something else. Ford ended production of the all-electric Lightning in November of twenty twenty-five. And it dropped a planned fully electric second generation in favor of range-extenders. The new truck is planned for the Rouge plant in Dearborn, and Cars dot com notes that Ford has not announced when it will go on sale.""",
   "Ford Rouge Complex Dearborn", "NEXT LIGHTNING: EXTENDED RANGE")
sc("""There is a twist here too, and it is about money. Ford took a nineteen point five billion dollar charge, of which about five and a half billion was cash, as it changed its electric strategy. That is the price of being early with a pure electric truck. The hybrid trucks that Ford was already selling, the F-one-fifty Hybrid and the Maverick Hybrid, did not need a charge. They simply sold.""",
   "Ford F-150 Lightning pickup", "$19.5B CHARGE. HYBRIDS: NO CHARGE.")

# ---------- 6. GM ----------
sc("""Number six is General Motors, and this one is a rumor, so we will be careful. According to a report from Crain's Detroit Business, citing Automotive News, insiders say the Silverado EV and Sierra EV are likely to become plug-in hybrids, built on a new combustion platform called T-one-two. GM has not confirmed that. A GM spokesperson said only that the company has not disclosed plans or timing for next-generation battery-electric trucks.""",
   "Chevrolet Silverado EV", "GM PLUG-IN HYBRIDS: UNCONFIRMED")
sc("""What GM has said publicly is more cautious. In January, chief executive Mary Barra told Automotive News the company is evaluating plug-in hybrids, and that electric vehicles remain the end game, but that reaching that goal will take longer without incentives. So the honest summary is this. GM is looking at hybrids, it has not announced a truck, and the Silverado EV and the Sierra EV sold fewer trucks in the third quarter of this year than a year earlier.""",
   "General Motors Factory Zero Detroit", "BARRA: EVS TAKE LONGER")


# ---------- WORDS EXPLAINED ----------
sc("""Before the verdict, let's clear up three words that get mixed together. A hybrid, like the Maverick Hybrid and the F-one-fifty Hybrid, has an engine and an electric motor working together, and you never plug it in. A plug-in hybrid has a bigger battery that you can charge from the wall, so it can drive some distance on electricity alone. And an extended-range electric truck, like the new Ram REV, drives its wheels only with electric motors, and uses a gas engine as a generator.""",
   "Ford F-150 Hybrid pickup", "HYBRID, PLUG-IN, EXTENDED-RANGE")
sc("""Why does the difference matter to a buyer? Because each one asks something different. The plain hybrid asks nothing. The plug-in asks you to plug in, or you lose most of the benefit. And the extended-range truck is the newest idea of the three, so there are no long-term owner records yet. A careful buyer should know which one they are looking at, because the dealer might use the word hybrid for all of them.""",
   "Chevrolet Silverado pickup", "KNOW WHICH ONE YOU ARE BUYING")
sc("""Now back to the numbers, because there is one more figure from Ford that adds to the picture. Ford's total sales in the third quarter of twenty twenty-six were five hundred nine thousand, seven hundred sixty-four vehicles, down six point six percent. Yet the F-Series was up two point four percent in September, to sixty-seven thousand, four hundred forty-eight trucks, and Ford built two hundred sixty-six thousand, seven hundred seventy-seven F-Series trucks in the quarter, up four and a half percent.""",
   "Ford F-150 pickup truck factory", "FORD Q3: 509,764 VEHICLES (-6.6%)")
sc("""That tells you something about what Ford is betting on. The company is building more trucks, and it is selling more hybrid trucks, while its total sales dip. Trucks are the part of the business that Ford is protecting. And the hybrid is a part of how it protects it, because a hybrid truck costs the buyer less than an electric one and still reaches the customers who care about fuel.""",
   "Ford F-150 Lariat pickup", "FORD PROTECTS ITS TRUCKS")
sc("""Think about the Maverick again for a moment, because it holds a lesson for the whole industry. It is a small truck, priced at a small truck price, with a hybrid system that most buyers chose. The company did not need an electric truck to reach those buyers. It needed a truck that did what the buyer wanted, at a price the buyer could pay. That is a simple idea, and it is not easy to copy.""",
   "Ford Maverick Hybrid pickup", "THE LESSON OF THE MAVERICK")
sc("""And what about the big trucks? The numbers are smaller, but the direction is the same. The F-one-fifty Hybrid sold nearly ten thousand trucks in the third quarter, by our calculation. That is not a rounding error, and not a boom either. It is a steady, growing group of buyers who want a full-size truck with a different engine. The next few years will show whether that group becomes ten percent of the market, or twenty, or stays where it is.""",
   "Ford F-150 pickup", "FULL-SIZE HYBRIDS: STILL SMALL, GROWING")

# ---------- THE VERDICT ----------
sc("""So who is winning the hybrid truck rush? On the numbers, Ford is. The Maverick Hybrid and the F-one-fifty Hybrid together sold about one hundred eight thousand, eight hundred trucks in nine months. Toyota is growing fast with the Tacoma Hybrid. Ram has a plan with no numbers yet, and General Motors has a rumor. The winners in this market are the companies that already had hybrid trucks on sale before the electric ones stalled.""",
   "Ford Maverick Hybrid F-150 Hybrid pickups", "FORD: ~108,800 HYBRID TRUCKS")
sc("""But a careful buyer should hold two thoughts at once. First, the hybrid is a real, tested, selling product, and the numbers are large. Second, the market for hybrid pickups is still new, and a lot of the future models have no price and no date. A hybrid that exists on a lot today is a very different thing from a hybrid that is promised for April of twenty twenty-seven.""",
   "Toyota Tacoma pickup", "REAL TODAY VS PROMISED LATER")
sc("""One more reason the hybrid is rising is the simplest one. It does not ask the buyer to change habits. No home charger, no planning a trip around a charging station, no waiting. A truck is a tool, and a tool that works the same way on Monday as it did last year is easy to trust. The hybrid is a bridge, and right now the bridge is where the buyers are standing.""",
   "Ford F-150 pickup truck", "A HYBRID ASKS NOTHING NEW")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a hybrid truck in twenty twenty-seven? First, look at the real fuel economy for your kind of driving. Towing can cut the advantage a lot, and the official number is not the same as the one you will see. Second, check the warranty on the battery and the hybrid system, in writing. Third, compare the price of the hybrid with the gas truck, and work out how many years it takes to earn the difference back.""",
   "Ford F-150 pickup", "CHECK 1, 2 AND 3")
sc("""Fourth, do not buy a hybrid that has not been built yet. A promised truck can slip, as the Ram REV did, from twenty twenty-four to twenty twenty-seven. And fifth, check the sales trend of the exact model. A truck that sells in the tens of thousands, like the Maverick Hybrid, will have parts, service and resale demand. We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Chevrolet Silverado 1500", "CHECK 4 AND 5")
sc("""If you want to know what it really costs to own a new truck for five years, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Ford sold seventy-four thousand": "Intro", "Number one": "1. Ford Maverick Hybrid", "Number two": "2. Ford F-150 Hybrid",
      "Number three": "3. Toyota Tacoma Hybrid", "Number four": "4. Ram 1500 REV", "Number five": "5. The next Ford Lightning",
      "Number six": "6. General Motors", "So who is winning": "The verdict",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video06", "length_scale": 1.6,
  "title": "6 Hybrid Pickups Taking Over in 2027 (Who Is Really Winning)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
