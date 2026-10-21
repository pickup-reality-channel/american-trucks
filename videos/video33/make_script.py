import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One of these trucks just had the best sales year in its history. One grew more than fifty percent in a single year. And one just got a forty horsepower upgrade for twenty twenty-seven that most buyers have not heard about. The Toyota Tacoma, the Ford Ranger and the Chevrolet Colorado. Three trucks, almost the same price. Only one of them can be the right one for you.""",
   "Toyota Tacoma 2024", "TACOMA VS RANGER VS COLORADO")

# ---------- COLD OPEN ----------
sc("""The midsize truck is back. In twenty twenty-five, Americans bought six hundred sixty thousand, four hundred twelve midsize pickups, up twenty-four point four percent from the year before, according to TFLtruck's sales report. That is a huge jump in a market where full-size trucks keep getting more expensive.""",
   "Ford Ranger 2024", "MIDSIZE SALES: +24.4% IN 2025")
sc("""And the reason is simple. TFLtruck put it this way, consumers are appreciating these smaller than full-size, more affordable pickup trucks. A full-size truck can easily cost more than sixty thousand dollars. These three start in the low to mid thirty thousands. For many buyers, that is the difference between affording a new truck and not.""",
   "Chevrolet Colorado 2023", "THE AFFORDABLE TRUCK IS BACK")
sc("""But keep it in perspective. All the midsize pickups in TFLtruck's report together, six hundred sixty thousand trucks, still sold fewer than the Ford F-Series alone, which sold eight hundred one thousand, five hundred twenty-five in twenty twenty-five, according to CarScoops. Midsize trucks are growing fast, but full-size trucks still rule America.""",
   "Ford F-150 2025 parked", "ALL MIDSIZE < F-SERIES ALONE")
sc("""In this video, we compare the twenty twenty-six and twenty twenty-seven Tacoma, Ranger and Colorado on six things that matter. Sales, price, power, towing, reliability and safety. And in almost every category, the winner changes, which is why choosing between them is so hard. Every number is sourced in the description.""",
   "Toyota Tacoma Ford Ranger Chevrolet Colorado", "6 CATEGORIES, SOURCED")

# ---------- 1. SALES ----------
sc("""Round one, sales. The Toyota Tacoma sold two hundred seventy-four thousand, six hundred thirty-eight trucks in twenty twenty-five, up forty-two point four percent, its best sales year ever in the United States, according to TFLtruck. The article said the gain came largely from the fourth-generation Tacoma, launched in twenty twenty-four, reaching full production.""",
   "Toyota Tacoma TRD Off Road", "TACOMA: 274,638 (BEST YEAR EVER)")
sc("""The Chevrolet Colorado sold one hundred seven thousand, eight hundred sixty-seven, up ten point one percent. Add its twin, the GMC Canyon, with thirty-six thousand, four hundred seventy-seven, and GM sold one hundred forty-four thousand, three hundred forty-four midsize trucks. The Ford Ranger sold seventy thousand, nine hundred sixty, up fifty-three point six percent.""",
   "Chevrolet Colorado Z71", "COLORADO: 107,867. RANGER: 70,960")
sc("""Here is the twist. The Ranger had the biggest growth of the three, but TFLtruck noted that Ford struggled with its production numbers in previous years. So part of that fifty-three percent jump is the Ranger simply catching up to demand. And another surprise. The Nissan Frontier sold sixty-five thousand, two hundred thirty-two, close to the Ranger, and the Jeep Gladiator grew thirty-five percent.""",
   "Nissan Frontier 2022", "RANGER: +53.6%")
sc("""And there is a smaller truck stealing buyers from all three. The Ford Maverick, a compact pickup, sold one hundred fifty-five thousand and fifty-one trucks in twenty twenty-five, up eighteen point two percent, according to TFLtruck. That is more than twice the Ranger's sales. For buyers who do not need to tow much, the Maverick has become a real alternative to a midsize truck.""",
   "Ford Maverick 2024", "MAVERICK: 155,051")
sc("""The Tacoma outsold the Colorado and Ranger combined. It is not just the best-selling midsize truck. It sold almost four times as many trucks as the Ranger. Round one goes to the Tacoma, by a mile. But sales do not tell you which truck is best for you, so let's look at price.""",
   "Toyota Tacoma 2024 TRD", "ROUND 1: TACOMA")

# ---------- 2. PRICE ----------
sc("""Round two, price. For twenty twenty-six, the cheapest Tacoma, the SR XtraCab, starts at thirty-two thousand, one hundred forty-five dollars, plus a one thousand five hundred ninety-five dollar destination fee, according to CarScoops. That was up five hundred fifty-five dollars, partly offset by a tow hitch that is now standard. The top Tacoma trims reach sixty-four thousand, three hundred fifty.""",
   "Toyota Tacoma SR", "TACOMA SR: $32,145")
sc("""The twenty twenty-six Chevrolet Colorado started at thirty-two thousand, four hundred dollars on Chevrolet's online configurator, according to Autoevolution. And Auto123 put the starting prices of the Colorado, Ranger and Tacoma all at about thirty-five thousand dollars, when comparing them with the coming Ram Dakota. In other words, the three trucks start within a few hundred to a couple of thousand dollars of each other.""",
   "Chevrolet Colorado WT", "ALL THREE: LOW TO MID $30,000s")
sc("""Toyota also made small changes for twenty twenty-six. The SR XtraCab gets a standard tow hitch, the previous towing package cost five hundred forty dollars. Several TRD trims get a black Toyota logo instead of chrome, the TRD Off-Road with the Premium Package gets eighteen-inch wheels with thirty-two-inch Goodyear all-terrain tires, and the TRD Pro gets an exclusive color called Wave Maker, according to CarScoops. Most other trims rose between fifteen and two hundred fifteen dollars.""",
   "Toyota Tacoma TRD Sport", "2026 TACOMA: +$15 TO +$555")
sc("""Chevrolet's twenty twenty-seven Colorado changes are also about equipment. According to Pickup Truck plus SUV Talk, the lineup is WT, LT, Trail Boss, Z71 and ZR2, all crew cab with a short bed. Convenience Package three, with ventilated front seats, driver seat memory, a heated steering wheel and wireless charging, becomes optional on the Z71 and available on the ZR2. And the ZR2 keeps ten point seven inches of ground clearance.""",
   "Chevrolet Colorado ZR2 2023", "2027 COLORADO: MORE FEATURES")
sc("""Here is the twist. The entry price is almost meaningless, because few buyers choose the base truck. The Tacoma's range runs from about thirty-two thousand to more than sixty-four thousand dollars. That top-end price is full-size truck territory. So the real question is not which truck is cheapest. It is which one gives you the equipment you need for the least money.""",
   "Toyota Tacoma TRD Pro 2024", "TOP TACOMA: $64,350")
sc("""The Tacoma also offers the most choice. A dealer comparison lists eight trims, two cab styles, two bed lengths, and a manual transmission option, while the twenty twenty-seven Colorado comes only as a crew cab with a short bed. If you want a manual, an extra-cab or a long bed, the Tacoma is the only one of the three that offers all of them. That flexibility is part of why it sells so well.""",
   "Toyota Tacoma XtraCab", "TACOMA: MANUAL + LONG BED")
sc("""Round two is a tie on paper. But the Colorado deserves a mention, because its base engine is far more powerful than the base engines of its rivals, which brings us to round three.""",
   "Chevrolet Colorado Trail Boss", "ROUND 2: TIE")

# ---------- 3. POWER ----------
sc("""Round three, power. The Ford Ranger's standard two point three liter EcoBoost four-cylinder makes two hundred seventy horsepower and three hundred ten pound-feet. The Tacoma's base engine ranges from two hundred twenty-eight to two hundred seventy-eight horsepower depending on the trim. And the Colorado's two point seven liter TurboMax made three hundred ten horsepower and four hundred thirty pound-feet, as standard.""",
   "Ford Ranger EcoBoost", "BASE ENGINES: COLORADO LEADS")
sc("""And now the twenty twenty-seven twist. According to Autoevolution, the twenty twenty-seven Colorado and Canyon get a revised two point seven liter turbo four-cylinder that makes three hundred fifty horsepower and four hundred fifty-five pound-feet of torque. That is forty horsepower more than before, in a truck that already had the most powerful base engine of the three. Production was expected to begin in October twenty twenty-six, at GM's Wentzville plant in Missouri.""",
   "Chevrolet Colorado ZR2", "2027 COLORADO: 350 HP")
sc("""Pickup Truck Talk first noticed the change in GM's order guide, where the engine code changed from L three B to L four B, before Chevrolet announced the power. The Colorado keeps an eight-speed automatic, while the Silverado and Sierra move to a ten-speed. And it gets a five G Wi-Fi hotspot and new colors.""",
   "Chevrolet Colorado interior", "NEW ENGINE CODE: L4B")
sc("""At the top of each lineup, the picture changes. The Tacoma's i-Force Max hybrid makes three hundred twenty-six horsepower and four hundred sixty-five pound-feet. And the Ford Ranger Raptor, with its twin-turbo V6, makes four hundred five horsepower, the most of any truck here. So the most powerful midsize truck you can buy is a Ford. But the most powerful standard engine for twenty twenty-seven is a Chevy.""",
   "Ford Ranger Raptor", "RANGER RAPTOR: 405 HP")
sc("""What about fuel economy? According to published EPA-based comparisons, the best combined rating is about twenty-three miles per gallon for both the Tacoma and the Ranger, and about twenty-one for the Colorado. So the Colorado's extra power comes with a small penalty at the pump. The Colorado also carries a twenty-one point four gallon fuel tank, according to Pickup Truck Talk, while some Tacoma owners have complained about a small fuel tank.""",
   "gas station pickup truck", "MPG: TACOMA/RANGER 23, COLORADO 21")
sc("""Round three goes to the Colorado for everyday power, and to the Ranger Raptor for maximum power. The Tacoma's strength is not raw power. It is something else, which we will see in reliability.""",
   "Chevrolet Colorado 2024", "ROUND 3: COLORADO")

# ---------- 4. TOWING ----------
sc("""Round four, towing and payload. The Colorado tows up to seven thousand, seven hundred pounds when properly configured, and that figure stays the same for twenty twenty-seven, according to Autoevolution. The Ranger tows up to seven thousand, five hundred. The Tacoma tows up to six thousand, five hundred pounds, and six thousand with the hybrid.""",
   "Chevrolet Colorado towing", "COLORADO: 7,700 LB")
sc("""Here is the twist. The off-road versions tow less. The Colorado ZR2 and the Canyon AT4X are limited to six thousand pounds, and the Bison and AEV versions to five thousand five hundred, according to Autoevolution. The Ranger Raptor is rated at about five thousand five hundred pounds. So if you want the toughest-looking version and you tow a heavy trailer, you may be buying the wrong truck.""",
   "Chevrolet Colorado ZR2 Bison", "OFF-ROAD VERSIONS TOW LESS")
sc("""And always check the real number for your truck. Maximum towing applies only to specific configurations. Some reports list base Colorado work trucks at only three thousand five hundred pounds without the trailering package. The number in the ad is the best case, not the number on your door sticker. Payload is close for all three, around one thousand seven hundred pounds. Round four goes to the Colorado, narrowly.""",
   "pickup truck towing trailer", "ROUND 4: COLORADO (BARELY)")

# ---------- 5. RELIABILITY ----------
sc("""Round five, reliability. In Consumer Reports' predicted reliability for twenty twenty-six, as summarized by Pickup Truck plus SUV Talk, the Tacoma ranked first among midsize trucks, with top scores in every category. It regained the top spot after a dip in its first model years.""",
   "Toyota Tacoma 2024 Limited", "CR 2026: TACOMA #1")
sc("""And here is the twist. The Colorado and its twin, the GMC Canyon, ranked last. Their biggest weak spots were the powertrain and brakes, though in-car electronics improved after an over-the-air update in July twenty twenty-five. The Ranger fell below average overall, even though no single area was below average. It had been the top midsize pick for twenty twenty-five. The article said the drop was mainly because other trucks improved.""",
   "GMC Canyon AT4", "CR 2026: COLORADO/CANYON LAST")
sc("""The Ranger's drop is a good example of how these rankings work. The article notes that recalls do not affect Consumer Reports' overall rankings, because they are based on owner-reported problems. So a truck can have serious recalls and still score well, or score worse simply because its rivals improved. That is why we use more than one source.""",
   "Ford Ranger XLT 2024", "RECALLS ≠ CR SCORE")
sc("""A different ranking agreed on first place. In August twenty twenty-six, Pickup Truck plus SUV Talk ranked the most reliable midsize trucks using complaints, recalls and service bulletins. The Tacoma was first, though early automatic transmission complaints were noted. Then came the Nissan Frontier, the Honda Ridgeline, the Colorado and Canyon tied, the Ford Ranger, and the Jeep Gladiator.""",
   "Toyota Tacoma Trailhunter", "PUTT 2026: TACOMA #1 AGAIN")
sc("""The problems listed are worth knowing. For the twenty twenty-four to twenty twenty-six Ranger, recalls for two point three liter engines that can suddenly lose drive power, sometimes requiring a long-block replacement, plus EGR valve failures and harsh ten-speed shifts. For the Colorado, false emergency braking, coolant leaks, electrical glitches and rough shifting. For the Tacoma, recalls for the instrument display, rear brake hoses, a driveshaft and a weight label.""",
   "Ford Ranger 2024 engine", "RANGER: LOSS-OF-POWER RECALLS")
sc("""The same ranking listed the others' problems too. For the Nissan Frontier, rough or delayed shifts, warning messages, infotainment trouble and batteries that drain. For the Jeep Gladiator, steering wander and death wobble, Pentastar V6 valvetrain ticks, coolant leaks, and roof and window leaks. And Pickup Truck Talk stressed that complaints to the federal safety agency are not failure rates, so they show patterns, not odds.""",
   "Jeep Gladiator Rubicon", "COMPLAINTS ARE NOT FAILURE RATES")
sc("""Even the Honda Ridgeline, often praised for reliability, had issues in that ranking, including fuel pump failures, fuel injector trouble, water leaks and battery drain, plus an older rear subframe corrosion recall in salt-belt states. And the Colorado's list included battery drain after software updates and camera and screen failures. Modern trucks fail more often in electronics than in the engine block.""",
   "Honda Ridgeline 2021", "ELECTRONICS FAIL MORE THAN ENGINES")
sc("""And the Tacoma's earlier history is a reminder. In February twenty twenty-four, Toyota recalled about three hundred eighty-one thousand twenty twenty-two and twenty twenty-three Tacomas, because welding debris on the rear axle could cause retaining nuts to loosen, according to FOX seven Austin. No reliable truck is perfect. Check every recall before you buy, new or used. Round five goes clearly to the Tacoma.""",
   "Toyota Tacoma 2022", "ROUND 5: TACOMA")

# ---------- 6. SAFETY ----------
sc("""Round six, safety, and this one surprises people. When the Insurance Institute for Highway Safety first ran its updated moderate overlap crash test on small crew cab pickups in twenty twenty-three, none earned a good rating, according to Work Truck Online. The test adds a dummy in the rear seat, sized like a small woman or a twelve-year-old child.""",
   "IIHS crash test", "NONE EARNED 'GOOD'")
sc("""In that round, the Colorado and the Tacoma were rated poor, with the rear dummy's head too close to the front seatback and a moderate to likely risk of neck and chest injury. The Ranger was rated marginal, after its rear dummy slid under the lap belt. The Nissan Frontier did best, with acceptable. Those were older versions, but they show where midsize trucks were weak.""",
   "Ford Ranger 2023", "TACOMA + COLORADO: POOR (2023)")
sc("""And the problem has not disappeared. In September twenty twenty-six, the twenty twenty-six GMC Canyon, the Colorado's twin, earned a marginal rating in the updated test, according to GM Authority. The driver was well protected, but IIHS said the rear passenger's head moved close to the front seatback, raising the risk of head injury. The Canyon was rated good in the small overlap and side tests, but poor in vehicle-to-vehicle front crash prevention.""",
   "GMC Canyon 2023", "2026 CANYON: MARGINAL")
sc("""The Canyon's other scores are worth knowing too. Its headlights were rated acceptable, and pedestrian front crash prevention was acceptable, but vehicle-to-vehicle front crash prevention was rated poor. The test truck was a Canyon AT4 crew cab with four-wheel drive. Its structure and safety cage were rated good, so the weakness is in how the rear-seat passenger is restrained, not in the body itself.""",
   "GMC Canyon AT4 2024", "STRUCTURE GOOD, REAR SEAT WEAK")
sc("""Here is the takeaway. If you regularly carry kids or adults in the back seat, check the IIHS rating of the exact truck, cab and model year you are buying. Midsize crew cabs protect the front seats well, but rear-seat protection has been the weak spot. Round six has no clear winner, which is itself the warning.""",
   "pickup truck rear seat", "ROUND 6: NO CLEAR WINNER")

# ---------- 7. THE REST ----------
sc("""And do not forget the others. The Nissan Frontier ranked second in Pickup Truck Talk's reliability ranking and scored above average with Consumer Reports. The Jeep Gladiator grew thirty-five percent in twenty twenty-five, though TFLtruck said Jeep had overpriced it before. And the Honda Ridgeline, a Consumer Reports top pick, is going on pause until a next generation expected in twenty twenty-eight, according to SlashGear.""",
   "Jeep Gladiator", "DON'T IGNORE THE FRONTIER")
sc("""And not every small truck grew. The GMC Canyon fell four point five percent in twenty twenty-five, the Nissan Frontier fell four point three percent, and the Hyundai Santa Cruz, a compact pickup, fell twenty percent, according to TFLtruck. Buyers were not simply buying any smaller truck. They were choosing specific ones, mostly the Tacoma.""",
   "Hyundai Santa Cruz", "CANYON -4.5%, SANTA CRUZ -20%")
sc("""And a new rival is coming. Ram has confirmed the Dakota name for a new midsize pickup, built in Belvidere, Illinois, with production scheduled for twenty twenty-seven, according to Auto123. Ram CEO Tim Kuniskis hinted at a price around forty thousand dollars. So by twenty twenty-eight, this comparison could have a fourth American player.""",
   "Dodge Dakota", "THE RAM DAKOTA IS COMING")

# ---------- 8. WHICH TO BUY ----------
sc("""And remember why the Tacoma's sales jumped. The fourth-generation truck launched in twenty twenty-four, and TFLtruck said its record twenty twenty-five came largely from reaching full production. Consumer Reports' scores also show the Tacoma regained the top spot after a dip in its first model years. That pattern, early problems followed by improvement, is common with redesigned trucks. It is a reason to favor a later model year of any new generation.""",
   "Toyota Tacoma 2024 TRD Off Road", "LATER MODEL YEARS ARE SAFER BETS")
sc("""That applies to the twenty twenty-seven Colorado too. Its new L four B engine is a revised version of an engine that has been in production for years, but any change brings some risk. If you buy a twenty twenty-seven, ask whether any recall or service bulletin applies to the new engine, and keep your service records, because a warranty claim is easier with a clean history.""",
   "Chevrolet Colorado LT", "NEW ENGINE CODE = CHECK BULLETINS")
sc("""So which one should you buy? If reliability and resale are your top priority, the Tacoma wins. It ranked first in both reliability rankings, and Americans bought more of them than any other midsize truck, which tends to help resale. Just check that any early transmission concerns and recalls have been addressed on the truck you buy.""",
   "Toyota Tacoma 2025", "BUY THE TACOMA IF: RELIABILITY")
sc("""If you want the most power and towing for the money, the twenty twenty-seven Colorado is hard to beat on paper, with three hundred fifty horsepower as standard and up to seven thousand, seven hundred pounds of towing. But it ranked last in Consumer Reports' predicted reliability, so a long warranty and a careful look at recalls matter more with this truck.""",
   "Chevrolet Colorado 2027", "BUY THE COLORADO IF: POWER")
sc("""And if you want the best-driving off-road performance truck, or the most powerful midsize truck you can buy, the Ranger Raptor is the one, with four hundred five horsepower. For the regular Ranger, make sure any two point three liter engine recall work has been completed before you sign.""",
   "Ford Ranger Raptor 2024", "BUY THE RANGER IF: PERFORMANCE")

# ---------- CLOSE ----------
sc("""Final scorecard. Sales, Tacoma. Price, a tie. Power, Colorado, with the Raptor as the most powerful. Towing, Colorado, narrowly. Reliability, Tacoma. Safety, no clear winner. On points, the Tacoma and the Colorado each take two rounds. But they win very different rounds, and that is the real answer.""",
   "Toyota Tacoma Chevrolet Colorado", "TACOMA 2, COLORADO 2, TIE 2")
sc("""And the final twist. The truck that sells the most is not the most powerful, does not tow the most, and is not the cheapest. Buyers chose the Tacoma for the thing that is hardest to see in an ad, how likely it is to keep working. Decide which round matters most to you, and the choice becomes easy.""",
   "Toyota Tacoma TRD Pro", "PICK YOUR ROUND")
sc("""We put a full midsize truck comparison, with the recall checks for each model, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we look at why truck payments hit record highs. And tell us in the comments, Tacoma, Ranger or Colorado? Thanks for watching.""",
   "Ford Ranger pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One of these trucks just had": "Intro", "Round one, sales": "Round 1: Sales", "Round two, price": "Round 2: Price", "Round three, power": "Round 3: Power",
      "Round four, towing": "Round 4: Towing and payload", "Round five, reliability": "Round 5: Reliability", "Round six, safety": "Round 6: Safety",
      "And do not forget the others": "Frontier, Gladiator, Ridgeline and Dakota", "So which one should you buy": "Which one to buy", "Final scorecard": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video33", "length_scale": 1.4,
  "title": "Tacoma vs Ranger vs Colorado for 2027: The Winner Changes in Every Round", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
