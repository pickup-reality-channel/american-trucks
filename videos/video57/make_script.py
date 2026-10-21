import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""In February twenty twenty-six, more than four hundred fifty thousand Ram and Jeep owners got a warning nobody expects from a truck company: do not tow. A faulty module could leave trailers with no turn signals, no brake lights, and in some cases no trailer brakes at all. And that recall is only one of the ways towing can go wrong without the driver ever noticing.""",
   'Ram 2500 towing trailer', "456,287 VEHICLES: DON'T TOW")
sc("""Towing is one of the main reasons Americans buy pickups. But it is also where trucks get hurt. Overloaded beds, wrong hitches, overheated transmissions and swaying trailers. In this video we go through nine towing mistakes that wreck trucks, with the 2026 lessons every owner should know before hooking up a trailer.""",
   'pickup truck towing camper', '9 TOWING MISTAKES')
sc("""This is general safety information, not a replacement for your owner's manual, which is always the final word for your truck. Every number we use comes from a published source in the description. If we could not confirm a figure, we left it out. Let's start with that recall.""",
   'pickup truck owner manual', 'YOUR MANUAL IS THE FINAL WORD')
sc("""According to Pickup Truck Talk, Chrysler filed safety recall twenty-six V zero five nine with federal regulators on February second, twenty twenty-six. It covered four hundred fifty-six thousand, two hundred eighty-seven vehicles, including more than three hundred twelve thousand Ram fifteen hundreds, almost ninety-seven thousand Ram twenty-five hundreds and more than thirty thousand Ram thirty-five hundreds from the twenty twenty-five and twenty twenty-six model years.""",
   'Ram 1500 pickup', 'RECALL 26V-059')
sc("""The problem was the trailer brake and towing control module. According to the report, trailer turn signals might not flash, trailer stop lamps might not light when braking, and trailer brakes, where equipped, might not work. Owners were told not to tow until the module was replaced, free of charge.""",
   'trailer brake lights', 'NO SIGNALS. NO BRAKE LIGHTS.')
sc("""Here is the first twist. Many drivers would never notice. You cannot see your trailer lights from the driver's seat. That leads us to mistake number one, the simplest and most common one of all.""",
   'pickup truck trailer at night', "YOU CAN'T SEE YOUR OWN LIGHTS")
sc("""Mistake number one: skipping the pre-trip check. The National Association of Trailer Manufacturers recommends checking that the brakes work on both the truck and the trailer, checking tire pressure on both, including the spares, and making sure the wheel lug nuts are tightened to the correct torque before every trip.""",
   'trailer hitch check', '1. SKIPPING THE PRE-TRIP CHECK')
sc("""And check the lights every time. Have someone stand behind the trailer while you test the turn signals, brake lights and running lights. If you are alone, some trucks have a trailer light check feature, or you can use a reflection in a shop window. It takes two minutes and it can prevent a crash.""",
   'trailer lights check', 'TEST EVERY LIGHT, EVERY TIME')
sc("""And check for recalls. You can enter your vehicle identification number on the N H T S A website to see open recalls, as the Ram owners were told to do. Do the same for your trailer. A recall is free to fix, but only if you know about it.""",
   'NHTSA recall website', 'CHECK RECALLS BY VIN')
sc("""Mistake number two: trusting the big towing number. Truck ads love to show maximum towing capacity. But that number usually applies to a specific configuration, often a particular cab, bed, engine, axle ratio and towing package. The truck on the lot may be rated much lower.""",
   'pickup truck towing capacity ad', '2. TRUSTING THE BIG NUMBER')
sc("""Here is the twist: towing capacity is often not the limit you hit first. Payload is. Payload is how much weight your truck can carry, including passengers, cargo in the bed, and the trailer's tongue weight pressing down on the hitch. A family of four, a cooler, some gear and a heavy trailer tongue can use up the payload long before you reach the towing capacity.""",
   'family pickup truck loaded', 'PAYLOAD RUNS OUT FIRST')
sc("""Your truck's payload is printed on a sticker on the driver's door jamb. It is specific to that exact truck, including its options. Heavier trims with more features often have less payload. Read it before you buy a trailer, not after.""",
   'truck door jamb sticker', 'READ THE DOOR STICKER')
sc("""And there are more ratings to know. The gross vehicle weight rating is the most the truck can weigh, fully loaded. The gross combined weight rating is the most the truck and trailer can weigh together. And the rear axle has its own limit. Going over any one of these can overload brakes, tires and suspension.""",
   'truck scale', 'GVWR. GCWR. AXLE RATINGS.')
sc("""The good news is that major truck makers use a common industry test standard, called S A E J twenty-eight oh seven, to rate towing capacity. It makes ratings more comparable between brands. But it does not change the rule: stay within every rating on your truck, not just one.""",
   'pickup trucks towing test', 'SAE J2807 STANDARD')
sc("""And the easiest way to know your real weights is a public truck scale, like those at many truck stops. For a small fee, you can weigh the truck alone, then with the trailer, and see exactly where you stand. Many experienced towers do it before every big trip.""",
   'truck stop scale', 'WEIGH IT ON A SCALE')
sc("""Mistake number three: getting the tongue weight wrong. Tongue weight is the downward force of the trailer on the hitch. According to the trailer manufacturers' association, a general rule is to place about sixty percent of the load ahead of the trailer axle and forty percent behind it, and check the trailer's manual for the exact figure.""",
   'trailer loading', '3. WRONG TONGUE WEIGHT')
sc("""Here is why it matters. Too little weight on the tongue, with too much weight at the back of the trailer, is a classic cause of sway. Too much weight on the tongue can overload the truck's rear axle, lift the front wheels and reduce steering and braking. Either mistake makes the whole rig less stable.""",
   'trailer sway', 'TOO LITTLE = SWAY. TOO MUCH = OVERLOAD')
sc("""And here is the twist many owners do not know. Hitch maker Blue Ox recommends a weight distribution hitch when tongue weight is more than ten to fifteen percent of the trailer's total weight, when the truck sags at the rear, or when you are close to the towing limit. A weight distribution hitch spreads the load across the truck's axles.""",
   'weight distribution hitch', 'WEIGHT DISTRIBUTION HITCH')
sc("""A simple test: look at your truck from the side after hitching. If the rear squats and the front rises, the load is not balanced. Measure the front fender height before and after hitching. A big change means you should adjust the load or the hitch.""",
   'pickup truck rear sag', 'IF IT SQUATS, FIX IT')
sc("""Mistake number four: not knowing what to do when the trailer sways. Sway is when the trailer starts moving side to side behind the truck. Blue Ox lists common causes: crosswinds, uneven loads, sudden maneuvers, wrong tire pressure, high speed and the wrong hitch.""",
   'trailer highway wind', '4. PANICKING IN SWAY')
sc("""Here is the twist: the natural reaction is the wrong one. Slamming the brakes or jerking the wheel can make sway worse. The trailer manufacturers' association says not to steer into the sway and not to hit the accelerator or the brakes. Steer straight and let the rig slow down.""",
   'highway towing', "DON'T SLAM THE BRAKES")
sc("""Blue Ox adds that if your brake controller allows it, applying the trailer brakes alone can help straighten the trailer. That is why a properly adjusted brake controller is so important. Once you are safe, stop and check the load, the tire pressure and the hitch.""",
   'trailer brake controller', 'USE THE TRAILER BRAKES ALONE')
sc("""And prevention is better than reaction. Load the trailer correctly, keep tires at the right pressure, slow down in strong wind and avoid sudden lane changes. Many modern trucks also have trailer sway control built into their stability systems, but it is a safety net, not a license to tow badly.""",
   'pickup truck towing', 'PREVENTION BEATS REACTION')
sc("""Mistake number five: driving too fast. A truck and trailer take longer to stop than the truck alone, even if the trailer has brakes, according to the trailer manufacturers' association. The faster you go, the more distance you need and the more likely sway becomes.""",
   'pickup trailer highway', '5. DRIVING TOO FAST')
sc("""And there is a legal angle. According to the same association, many states set a fifty-five mile per hour speed limit for vehicles towing trailers. Rules differ by state, so check the laws where you are driving, especially on a long road trip through several states.""",
   'speed limit sign trucks', 'MANY STATES: 55 MPH WHEN TOWING')
sc("""Here is a twist many people miss: trailer tires. Many trailer tires have lower speed ratings than the tires on your truck. Driving faster than the tire is rated for can cause heat buildup and blowouts. The rating is printed on the sidewall. Check it before your next trip.""",
   'trailer tires', 'CHECK TRAILER TIRE SPEED RATING')
sc("""And the fuel bill rises with speed. Towing already uses a lot more fuel, and air resistance grows quickly as speed increases. With diesel at six dollars and twenty-eight cents a gallon in the week of October nineteenth, twenty twenty-six, according to the Energy Information Administration, slowing down saves real money.""",
   'diesel pump price', 'DIESEL $6.28: SLOW DOWN')
sc("""Mistake number six: cooking the brakes. On long downhill grades, a heavy rig can overheat its brakes. The trailer manufacturers' association warns that prolonged braking can cause overheating and loss of braking effectiveness. That is when brakes fade, and stopping distance grows dramatically.""",
   'mountain road truck', '6. COOKING THE BRAKES')
sc("""The fix is to use the engine and transmission to help slow down. Most modern trucks have a tow or haul mode, and many have engine braking or exhaust braking, especially diesels. Shift to a lower gear before the descent, not halfway down, and brake firmly and occasionally instead of riding the pedal.""",
   'truck tow haul mode', 'USE TOW/HAUL MODE')
sc("""And check the trailer brakes. Many states require brakes on trailers above a certain weight, and the thresholds vary. A brake controller in the truck must be set for the trailer's weight. Too little gain, and the truck does all the work. Too much, and the trailer wheels can lock.""",
   'trailer brakes', 'SET THE BRAKE CONTROLLER')
sc("""Mistake number seven: forgetting the safety chains and the breakaway cable. The trailer manufacturers' association says safety chains should be crossed under the tongue, connected, kept off the road, and given enough slack for turns. If the hitch fails, crossed chains can catch the tongue.""",
   'trailer safety chains', '7. CHAINS & BREAKAWAY')
sc("""And here is the twist: the breakaway cable. If the trailer separates, the cable pulls a pin that applies the trailer's brakes. The association says to connect the breakaway lanyard to the truck, not to the safety chains or the ball mount. If it is attached to the wrong place, it may not activate when it is needed.""",
   'trailer breakaway cable', 'CONNECT BREAKAWAY TO THE TRUCK')
sc("""Also make sure the coupler is fully latched on the ball, and the ball is the correct size. A ball that is too small can let the trailer pop off over a bump. The ball size is usually stamped on the top of the ball and on the trailer coupler. Match them every time.""",
   'trailer hitch ball coupler', 'MATCH THE BALL SIZE')
sc("""Mistake number eight: ignoring maintenance. Towing is hard work for a truck. Many owner's manuals list towing as severe service, which usually means more frequent oil changes, transmission fluid changes and inspections. Skipping them can shorten the life of the transmission and engine.""",
   'truck transmission service', '8. IGNORING MAINTENANCE')
sc("""The transmission is often the part that suffers most. Heat is its enemy, and towing creates a lot of heat. Watch the transmission temperature if your truck shows it, use tow or haul mode, and follow the severe service schedule. A transmission repair can cost thousands of dollars.""",
   'truck transmission', 'HEAT KILLS TRANSMISSIONS')
sc("""Here is a twist about the trailer itself. Trailers need maintenance too. Wheel bearings need grease, tires age even when they sit, and trailer brakes and lights wear out. A trailer that sits all winter can come back with dry bearings and cracked tires. Inspect it before the first trip of the season.""",
   'trailer wheel bearing', 'TRAILERS NEED MAINTENANCE TOO')
sc("""And check the tires on the truck as well. When towing heavy loads, many manufacturers recommend a higher rear tire pressure, which is listed in the owner's manual or on the door sticker. Under-inflated tires overheat and wear quickly under heavy loads.""",
   'truck tire pressure gauge', 'CHECK TOW TIRE PRESSURE')
sc("""Mistake number nine: the wrong truck for the job. A half-ton pickup can tow a lot, but a large travel trailer can push it to its limits, especially in wind. Heavy-duty trucks are built with stronger frames, brakes and axles for big loads. If you tow near the limit every weekend, the bigger truck may be the safer and cheaper choice in the long run.""",
   'Ford Super Duty towing', '9. THE WRONG TRUCK')
sc("""Here is the twist about the cost. A bigger truck costs more to buy, and according to AAA, a half-ton pickup already costs about sixteen thousand, four hundred forty-nine dollars a year to own in twenty twenty-six. But a lighter truck pushed to its limits can wear out brakes, tires and transmissions faster. The cheapest truck is the one that does the job without strain.""",
   'pickup trucks lineup', 'STRAIN COSTS MONEY')
sc("""And engine choice matters. Diesels are known for strong torque and engine braking, which help with heavy trailers. Hybrids like the F-one-fifty PowerBoost can offer strong torque too. But with diesel at record prices in twenty twenty-six, the fuel math has changed. We break it down in our diesel versus gas versus hybrid video.""",
   'diesel pickup truck', 'DIESEL, GAS OR HYBRID?')
sc("""There is also the electric question. Electric pickups have huge torque, but towing can cut their range dramatically, and charging with a trailer attached can be difficult at stations not designed for it. Ford ended production of the F-one-fifty Lightning in twenty twenty-five, according to Fox Business. For long-distance towing, most buyers still choose gas, diesel or hybrid.""",
   'electric pickup towing', 'EVS AND TOWING')
sc("""Now let's look at the most common towing situations, starting with the travel trailer. Travel trailers are tall and wide, which makes them catch wind like a sail. Even a trailer within your truck's ratings can feel unstable on a windy highway. That is why weight distribution and sway control hitches are so popular with campers.""",
   'travel trailer camper highway', 'TRAVEL TRAILERS CATCH WIND')
sc("""And here is a camper twist. The weight printed on a new travel trailer is often its dry weight, without water, propane, batteries or gear. Once you load it for a trip, the real weight can be much higher. Always plan using the loaded weight, or the trailer's maximum rating, not the brochure number.""",
   'camper trailer loading', 'DRY WEIGHT IS NOT REAL WEIGHT')
sc("""Water is heavy. Fresh water weighs about eight point three pounds per gallon. A full fresh water tank on a large trailer can add hundreds of pounds. Many campers travel with the tank nearly empty and fill it at the campground, which saves weight and fuel on the road.""",
   'camper water tank', 'WATER IS HEAVY')
sc("""Next, the boat trailer. Boat trailers are often backed into water at ramps, which exposes bearings and brakes to water and, in some places, salt. Rinse the trailer after saltwater use and check the bearings often. A seized bearing can ruin a trip and damage the axle.""",
   'boat trailer ramp', 'BOAT TRAILERS AND WATER')
sc("""And the ramp itself is a test. Steep, slippery boat ramps can be hard on a truck's traction, especially a two-wheel-drive truck. Four-wheel drive, good tires and a careful driver make a big difference. Practice launching on a quiet day before the busy holiday weekend.""",
   'boat ramp pickup truck', 'PRACTICE AT THE RAMP')
sc("""Then the utility and car trailer. These trailers are often loaded with heavy, compact cargo like equipment or a vehicle. Strapping matters. The trailer manufacturers' association recommends one tie-down for every ten feet of cargo, and at least two for any piece, regardless of length, secured low on the trailer when possible.""",
   'car hauler trailer', 'TIE-DOWNS: 1 PER 10 FEET')
sc("""And position the car or equipment carefully. On a car trailer, the vehicle's engine usually goes toward the front to keep enough tongue weight. Loading a car backward can shift weight behind the axle and make the trailer sway. A few feet forward or back can change everything.""",
   'car on trailer', 'POSITION THE LOAD CAREFULLY')
sc("""Then there are fifth wheel and gooseneck trailers. These hitch inside the truck bed, over the rear axle, which makes them much more stable for heavy loads. But they put a lot of weight in the bed, so payload becomes even more important. Many fifth wheel owners use heavy-duty trucks for this reason.""",
   'fifth wheel trailer truck', 'FIFTH WHEELS AND GOOSENECKS')
sc("""Here is a fifth wheel twist. Short-bed trucks can have very little clearance between the cab and the front of a fifth wheel trailer during tight turns. Some owners use a sliding hitch to avoid hitting the cab. Check the clearance before you buy the trailer.""",
   'short bed pickup fifth wheel', 'WATCH CAB CLEARANCE')
sc("""Weather is the hidden factor in every towing trip. Rain, snow, ice and wind all reduce control. The best towers check the forecast for the whole route and are ready to wait out a storm. No trip is worth driving into dangerous crosswinds with a tall trailer.""",
   'storm highway', 'WATCH THE WEATHER')
sc("""And plan rest stops. Towing is tiring because you have to concentrate more. Stopping every couple of hours lets you rest and also walk around the rig: check the hitch, the chains, the lights and feel the trailer hubs for unusual heat, which can be an early warning of a bearing problem.""",
   'rest stop truck trailer', 'WALK AROUND AT EVERY STOP')
sc("""Finally, think about insurance. Your auto policy may cover liability when you tow, but damage to the trailer itself may need separate coverage. Campers and boats often need their own policies. Ask your insurer before your first trip, not after an accident.""",
   'insurance paperwork', 'IS YOUR TRAILER INSURED?')
sc("""And rent before you buy. If you are new to towing, renting a trailer for a weekend can teach you a lot about how your truck handles a load. You will quickly learn whether your truck feels comfortable, whether you need better mirrors, and whether a bigger truck might be worth it before you spend thousands on a trailer.""",
   'rental trailer pickup', 'RENT BEFORE YOU BUY')
sc("""Let's add some practical habits. Practice backing up in an empty parking lot before your first trip. Use a spotter when backing. Plan fuel stops where a truck and trailer can fit. And give yourself extra space around other vehicles, because everything takes longer when you tow.""",
   'trailer backing up parking lot', 'PRACTICE BEFORE THE TRIP')
sc("""And use the technology your truck has. Many modern pickups offer trailer backup assist, trailer cameras, blind spot monitoring that covers the trailer, and trailer tire pressure monitoring. These features can make towing easier and safer, but they only help if they are set up correctly for your trailer.""",
   'pickup truck trailer camera', 'USE THE TECH')
sc("""Here is one last twist. The most dangerous moment is often not the highway. It is the first and last few minutes: hitching, unhitching and leaving the driveway. Most mistakes happen when people are in a hurry. A slow, careful routine at the start of every trip is the best safety system you have.""",
   'hitching trailer driveway', 'THE DANGER IS IN THE HURRY')
# ---------- CLOSE ----------
sc("""So here is your towing checklist. One: check lights, tires, brakes and recalls before every trip. Two: know your payload and every weight rating. Three: balance the tongue weight. Four: stay calm in sway and slow down. Five: use the engine to brake on hills. And six: cross the chains and connect the breakaway cable to the truck.""",
   'checklist', 'YOUR TOWING CHECKLIST')
sc("""We put a printable towing checklist and a full guide to choosing the right truck for your trailer into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video: diesel versus gas versus hybrid, and which one really pays off now. And tell us in the comments: what do you tow? Thanks for watching.""",
   'pickup truck sunset trailer', "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {'In February twenty twenty-six, more': 'Intro', 'According to Pickup Truck Talk,': 'The 2026 towing recall', 'Mistake number one: skipping the': 'Mistake 1: Skipping the check', 'Mistake number two: trusting the': 'Mistake 2: Trusting the big number', 'Mistake number three: getting the': 'Mistake 3: Wrong tongue weight', 'Mistake number four: not knowing': 'Mistake 4: Panicking in sway', 'Mistake number five: driving too': 'Mistake 5: Driving too fast', 'Mistake number six: cooking the': 'Mistake 6: Cooking the brakes', 'Mistake number seven: forgetting the': 'Mistake 7: Chains and breakaway', 'Mistake number eight: ignoring maintenance.': 'Mistake 8: Ignoring maintenance', 'Mistake number nine: the wrong': 'Mistake 9: The wrong truck', "Now let's look at the": 'Common towing situations', "Let's add some practical habits.": 'Habits of good towers', 'So here is your towing': 'Your towing checklist'}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": 'video57', "length_scale": 1.45,
  "title": "9 Towing Mistakes That Wreck Your Truck (And the Recall That Told 456,000 Owners: Don't Tow)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.45/212,1), "min")
