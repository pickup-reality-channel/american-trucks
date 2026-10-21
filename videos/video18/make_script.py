import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The Toyota Tundra keeps eighty percent of its value after five years, and it is one of the trucks most likely to reach two hundred fifty thousand miles. But the same truck was ranked last for reliability by one of the biggest truck sites in America, because of engine failures that sometimes meant a whole new engine. For twenty twenty-seven, Toyota says the problem has been addressed. Here is what changed, what did not, and whether you should believe it.""",
   "Toyota Tundra pickup", "2027 TUNDRA: DID TOYOTA FIX IT?")

# ---------- COLD OPEN ----------
sc("""The Toyota Tundra is a strange truck to talk about, because it has two reputations at once. On one side, the numbers on resale and longevity are among the best of any truck. On the other side, there is a known engine problem on the twenty twenty-two to twenty twenty-four trucks. And now there is a new model year, with new styling, a bigger screen, and a hybrid with more power. We will go through all of it, with sources.""",
   "Toyota Tundra TRD Pro pickup", "TWO REPUTATIONS AT ONCE")
sc("""We used Pickup Truck Talk's two articles on the twenty twenty-seven Tundra, published in July, plus CarGurus from September ninth and Kelley Blue Book for the price estimates. For resale, iSeeCars. For longevity, the iSeeCars study as reported by Work Truck Online. For sales, the Pickup Truck Talk table. A key point. Toyota has not published prices or on-sale dates for the twenty twenty-seven Tundra in these sources, so every price in this video is an estimate.""",
   "Toyota Tundra 1794 Edition pickup", "PRICES ARE ESTIMATES. TOYOTA HAS NOT PUBLISHED THEM.")
sc("""There is a twist in every part of this. One engine is unchanged, and that is the story. One hybrid makes more power than any other Tundra. One feature requires a subscription. And one list of complaints was not addressed. Stay with me, because the last twist is about a sentence in a review that the readers did not accept.""",
   "Toyota Tundra pickup truck", "FOUR TWISTS")

# ---------- 1. THE ENGINE ----------
sc("""Change number one is the engine, and the answer is that there is no new engine. According to Pickup Truck Talk, the twenty twenty-seven Tundra keeps the three point four liter twin-turbocharged V six, either alone or in the i-Force Max hybrid. The V eight is not coming back, and the old five point seven liter V eight, which made three hundred eighty-one horsepower and four hundred one pound-feet, is gone for good.""",
   "Toyota Tundra V6 twin turbo engine", "NO NEW ENGINE. NO V8.")
sc("""Now the problem. According to the same article, failures on certain twenty twenty-two to twenty twenty-four trucks were traced to machining debris trapped in the number one crankshaft main bearing. That could cause knocking, rough running, no-starts, power loss, or complete engine failure. Toyota introduced an improved main bearing and other manufacturing changes, and recall documents say engines built after those changes fall outside the affected production period.""",
   "Toyota Tundra engine recall", "2022-2024: DEBRIS IN THE MAIN BEARING")
sc("""The twist is the remedy. The latest recall repair uses dealer diagnostic software and vehicle operating data to decide whether an engine needs to be replaced. So not every truck gets a new engine. A diagnostic decides. And Toyota says that the manufacturing problem has been addressed. The article adds an important line, which is that buyers must decide for themselves whether enough time has passed to restore confidence.""",
   "Toyota Tundra pickup", "REMEDY: DIAGNOSE, THEN DECIDE")
sc("""A separate Pickup Truck Talk article from January says that a significant number of twenty twenty-two to twenty twenty-four engines were recalled, with no official campaigns published for twenty twenty-five or twenty twenty-six engines for this problem. It does not give a count. And in July, Pickup Truck Talk ranked the Tundra fifth of five full-size trucks for reliability, citing twin-turbo V six failures that in some cases required a complete engine replacement.""",
   "Toyota Tundra Limited pickup", "PUTT RELIABILITY RANK: 5TH OF 5")

# ---------- 2. THE HYBRID ----------
sc("""Change number two is the power. The i-Force Max hybrid makes four hundred thirty-seven horsepower and five hundred eighty-three pound-feet of torque, according to Pickup Truck Talk, compared with three hundred eighty-nine horsepower and four hundred seventy-nine pound-feet for the standard V six in most configurations. That is forty-eight more horsepower and one hundred four more pound-feet of torque. The hybrid is the most powerful Tundra.""",
   "Toyota Tundra i-FORCE MAX hybrid", "HYBRID: 437 HP, 583 LB-FT")
sc("""And there is a new feature that comes only with the hybrid. A two point four kilowatt inverter, which Pickup Truck Talk calls the most significant change for twenty twenty-seven, with uses for job sites, camping and emergency power. The twist is that Toyota has not yet said where the outlets are, what the operating limits are, or whether it delivers full output while parked. So the feature is real, and the details are not.""",
   "Toyota Tundra camping pickup", "2.4-KW INVERTER: DETAILS PENDING")
sc("""Fuel economy, for reference, is a modest part of this truck. KBB's page lists twenty miles per gallon in the city, twenty-four on the highway and twenty-two combined for the powertrain it shows, with a range of nineteen to twenty-two combined across the page. CarGurus lists seventeen to twenty in the city, twenty to twenty-four on the highway, and nineteen to twenty-two combined for twenty twenty-six. These are last year's numbers, and the twenty twenty-seven ratings are not confirmed.""",
   "Toyota Tundra pickup truck", "2026 MPG: 19-22 COMBINED")

# ---------- 3. THE DESIGN AND TECH ----------
sc("""Change number three is what you see and touch. The front end is redesigned, with a squared-off look and a stronger vertical grille, and the body-colored mustache trim is gone. There is a new Trailhunter package based on the SR5, with Old Man Emu suspension, Michelin tires, front recovery hooks, underbody protection, Multi-Terrain Select, Crawl Control, a locking rear differential and bronze wheels. Toyota says it is meant to offer an adventure-ready Tundra at a more accessible price.""",
   "Toyota Tundra Trailhunter pickup", "NEW: TRAILHUNTER, SR5-BASED")
sc("""Inside, a fourteen inch screen is standard on every twenty twenty-seven Tundra, replacing the eight inch screen on base trucks. A dash camera is standard, recording twenty second clips. Toyota Safety Sense four point oh is standard, and there is a digital key that works through a phone wallet app. The twist is the key. It requires an active Remote Connect trial or subscription, so a feature you use every day can depend on a service you may have to pay for.""",
   "Toyota Tundra interior screen", "DIGITAL KEY NEEDS A SUBSCRIPTION")

# ---------- 4. WHAT WAS NOT ADDRESSED ----------
sc("""Change number four is what did not change. Pickup Truck Talk notes that the initial announcement did not specifically address cracking plastic panels around the front seats, squeaky brakes, tailgate problems and wind noise. The article says production changes may still have been made, but they were not mentioned. These are small problems compared with an engine, and they are the kind of problems that owners talk about.""",
   "Toyota Tundra tailgate pickup", "NOT ADDRESSED: PANELS, BRAKES, TAILGATE")
sc("""And here is the last twist, about that sentence. The reviewer wrote that the recalls over the engine issues are done. The article presents it as the author's opinion, not as a Toyota statement, and the readers' comments dispute it. That is a fair summary of where the Tundra stands. One side believes the problem is behind the truck. The other side does not. Neither can prove it yet, because the newer engines have fewer miles.""",
   "Toyota Tundra pickup", "AUTHOR: RECALLS ARE DONE. READERS: NOT SURE.")

# ---------- THE PRICE ----------
sc("""Now the price, and we will be careful. Toyota has not published twenty twenty-seven prices in the sources we found. CarGurus says that the twenty twenty-six base price was forty-one thousand, two hundred sixty dollars including destination, and that the top Capstone model topped eighty thousand. Kelley Blue Book estimates the twenty twenty-seven SR Double Cab at forty-five thousand dollars, and the Capstone at eighty-four thousand. The KBB numbers are estimates, not Toyota's.""",
   "Toyota Tundra Capstone pickup", "KBB ESTIMATE: $45,000 TO $84,000")
sc("""KBB's estimates for the middle of the range are forty-nine thousand, five hundred for the SR5, fifty-three thousand, five hundred for the Trailhunter, fifty-eight thousand for the Limited CrewMax, sixty-six thousand, five hundred for the Platinum, sixty-seven thousand, five hundred for the Tundra 1794 Edition, and seventy-five thousand, five hundred for the TRD Pro. Again, these are estimates. They tell you that the Tundra is expected to cost about what the average full-size truck costs, which was sixty-seven thousand, four hundred forty-six dollars in August.""",
   "Toyota Tundra 1794 Edition", "ESTIMATES: TRAILHUNTER $53,500. TRD PRO $75,500.")
sc("""Towing and payload are not confirmed either. CarGurus says that the twenty twenty-six Tundra could tow up to twelve thousand pounds, with a payload of up to eighteen hundred fifty pounds. KBB's page shows eleven thousand, four hundred fifty pounds of towing and sixteen hundred sixty-five pounds of payload, for the configuration it displays. The two sources disagree, probably because they describe different trims. So check the door sticker for the exact truck.""",
   "Toyota Tundra towing trailer", "TOWING: 12,000 OR 11,450 LB?")

# ---------- THE NUMBERS THAT MATTER ----------
sc("""Now the numbers that made the Tundra's reputation. The truck sold one hundred ten thousand and eighty through nine months of twenty twenty-six, down eight tenths of a percent. In the third quarter, thirty-five thousand, seven hundred twelve, down seven tenths. It is very steady. And iSeeCars shows it keeping eighty and three tenths percent of its value after five years, about eighteen points above the Ram one thousand five hundred, and nineteen above the Ford F-one-fifty.""",
   "Toyota Tundra pickup truck", "TUNDRA: 110,080. RESALE: 80.3%")
sc("""On longevity, the Tundra is second in the twenty twenty-six iSeeCars study, at twenty-eight point two percent, about two and a half times the truck average. In the earlier edition, it was second too, at forty-seven point nine. So on resale and on lasting, the Tundra is at the top. On reliability, according to Pickup Truck Talk, it is at the bottom. The same truck, and three very different answers.""",
   "Toyota Tundra TRD pickup", "LONGEVITY: 28.2%, 2ND IN BOTH EDITIONS")
sc("""How can all three be true? Because they measure different things. Resale measures what buyers are willing to pay, which includes trust in the brand. Longevity measures how many trucks reach a high mileage, which includes trucks with replaced engines. And the reliability ranking measures problems, recalls and repair cost. A truck can be trusted by the market, last a long time, and still have a serious flaw on some model years. That is what the Tundra is.""",
   "Toyota Tundra pickup", "THREE MEASURES, THREE ANSWERS")

# ---------- WHO SHOULD BUY ----------
sc("""So who should buy a twenty twenty-seven Tundra? A buyer who values resale, who keeps trucks for a long time, and who accepts that Toyota has said the manufacturing problem has been addressed. Also a buyer who wants a hybrid with real power, and the inverter. And who should wait? A buyer who wants proof. Because a twenty twenty-seven truck has no track record yet, and the twenty twenty-two to twenty twenty-four trucks are the ones with the known problem.""",
   "Toyota Tundra pickup", "WHO: LONG-TERM KEEPERS. WAIT: SKEPTICS.")
sc("""And if you are shopping for a used Tundra, the advice is different. Check the build date of the exact truck, and check whether the recall repair was done. A twenty twenty-two to twenty twenty-four truck that has had a documented repair is a different purchase from one that has not. Ask for the paperwork. A Toyota dealer can look up the recall status with the vehicle identification number, and it takes a few minutes.""",
   "Toyota Tundra used pickup", "USED TUNDRA: CHECK THE RECALL STATUS")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a Tundra in twenty twenty-seven? First, the official price and the on-sale date, once Toyota announces them. Second, the warranty for the engine and the hybrid system, in writing. Third, the recall status for any used truck. And fourth, the towing and payload on the door sticker. We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Toyota Tundra pickup", "CHECK 1, 2, 3 AND 4")
sc("""If you want to know how the Toyota Tacoma compares with its rivals for twenty twenty-seven, subscribe, because that is coming soon. Thanks for watching.""",
   "Toyota Tacoma pickup", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The Toyota Tundra keeps eighty": "Intro", "Change number one": "1. The engine", "Change number two": "2. The hybrid power",
      "Change number three": "3. Design and tech", "Change number four": "4. What did not change",
      "Now the price": "The price (estimates)", "Now the numbers that made": "Resale and longevity",
      "So who should buy": "Who should buy it", "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video18", "length_scale": 2.0,
  "title": "2027 Toyota Tundra: Did Toyota Fix the Engine? What We Know So Far", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
