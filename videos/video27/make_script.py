import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In twenty twenty-six, the safest pickup truck in America, according to the Insurance Institute for Highway Safety, was the Tesla Cybertruck. The Ford F-150, the Ram fifteen hundred and the Chevrolet Silverado all earned the lowest possible rating in one of the institute's key crash tests. And not a single small pickup won a safety award. These are the truck safety ratings nobody talks about.""",
   "Tesla Cybertruck", "THE SAFEST PICKUP OF 2026?")

# ---------- COLD OPEN ----------
sc("""Most truck buyers assume a big truck is a safe truck. It is tall, it is heavy, and in a crash with a small car, it usually wins. That part is true. But the people who crash test vehicles for a living look at something else. They look at who is sitting in the back seat, how well the headlights work at night, whether the truck stops itself before a crash, and what happens to the person standing in front of it.""",
   "Ford F-150 pickup truck", "BIG DOES NOT MEAN SAFE")
sc("""And when you measure those things, the results are surprising. The Insurance Institute for Highway Safety, known as IIHS, is funded by insurance companies, and its job is to find out which vehicles cost lives and money in crashes. Its tests are tougher than the federal minimum, and they change every year. In twenty twenty-six, the bar went up again, and most pickups did not clear it.""",
   "Chevrolet Silverado 1500 pickup", "IIHS RAISED THE BAR AGAIN")
sc("""So in this video, we go through the safety ratings that never appear in truck commercials. The back seat test that most pickups fail. The headlight scores. The automatic braking test with a motorcycle and a semitrailer. And the hood height research that explains why big trucks are so dangerous for pedestrians. There is a twist in every one, starting with which trucks actually won.""",
   "Ram 1500 pickup truck", "THE RATINGS ADS NEVER MENTION")
sc("""As always, every rating here comes from a published source, mostly IIHS results reported by outlets like Pickup Truck and SUV Talk, GM Authority and Work Truck Online. The sources are in the description. And an important note. These ratings usually apply to a specific cab style and model years, so we will always say which ones. Let's start with the awards.""",
   "Toyota Tundra crew cab", "EVERY RATING IS SOURCED")

sc("""One quick thing about how to read these ratings. IIHS uses four levels, good, acceptable, marginal and poor. Good is the top. Poor is the bottom. There is no partial credit for a famous badge or a big engine. And because the tests get harder over time, a truck that earned good five years ago may not earn good today, even if nothing about the truck changed.""",
   "Ford F-150 XLT", "GOOD, ACCEPTABLE, MARGINAL, POOR")
# ---------- 1. THE AWARDS ----------
sc("""On March twenty-fourth, twenty twenty-six, IIHS announced its first round of twenty twenty-six safety awards. Sixty-three vehicles qualified, up from forty-eight at the same point the year before. Forty-five earned Top Safety Pick Plus, the highest award, and eighteen earned Top Safety Pick. SUVs dominated, with thirty-five of the forty-five top awards.""",
   "Toyota Tundra 2024", "2026: 63 WINNERS")
sc("""And pickups? Only two. The Tesla Cybertruck crew cab earned Top Safety Pick Plus, the only truck to get the top award. The Toyota Tundra crew cab earned Top Safety Pick. That was it. No Ford, no Ram, no Chevrolet, no GMC. And no small pickup earned any award at all, according to IIHS. Out of the best-selling vehicles in America, almost none made the list.""",
   "Tesla Cybertruck crew cab", "ONLY 2 PICKUPS QUALIFIED")
sc("""Why so few? Because the rules got stricter. For twenty twenty-six, a good rating in the updated moderate overlap front test became mandatory for either award. The year before, an acceptable rating was enough for Top Safety Pick. Front crash prevention had to be standard equipment. And for the top award, a vehicle needed a good rating in pedestrian crash prevention, plus an acceptable or good rating in a brand-new test.""",
   "Ford F-150 Lightning", "THE RULES GOT STRICTER")
sc("""That new test is called vehicle-to-vehicle front crash prevention two point oh. It replaced an older test IIHS dropped in twenty twenty-two, which only checked low-speed rear-end crashes against a car target. The new one runs at thirty-one, thirty-seven and forty-three miles per hour, and checks whether the vehicle can avoid or slow down for a passenger car, a motorcycle, and a semitrailer.""",
   "Ram 1500 Rebel", "NEW TEST: CAR, MOTORCYCLE, SEMI")
sc("""Here is the twist. Most vehicles passed it. IIHS says more than seventy percent of the eighty-five twenty twenty-five models tested earned acceptable or good, and more than seventy-seven percent of the twenty twenty-six models tested so far. So the new test was not impossible. Most cars and SUVs handled it. Several of the most popular pickups did not, and that is where the story gets uncomfortable.""",
   "Chevrolet Silverado 1500 LT", "MOST VEHICLES PASSED. MANY TRUCKS DID NOT.")

# ---------- 2. THE BACK SEAT ----------
sc("""Before we get to each truck, you need to know about the test that sank most of them, the updated moderate overlap front test. IIHS changed it after research found that in newer vehicles, belted rear-seat passengers face a higher risk of fatal injury than people in the front, according to Fleet and Insurance magazine. The front seats got better airbags and smarter seat belts over the years. The rear seats mostly did not.""",
   "Ford F-150 crew cab rear seat", "THE BACK SEAT FELL BEHIND")
sc("""So the updated test puts a small dummy, about the size of a twelve-year-old or a small adult, in the rear seat behind the driver. And it measures what happens to that passenger. Does the head hit the front seat? Does the body slide under the lap belt, which IIHS calls submarining? Are the belt forces so high they injure the chest? For a crew cab pickup, which is often a family vehicle, this test matters a lot.""",
   "Ram 1500 crew cab", "THE TEST: A PASSENGER IN THE BACK")
sc("""In twenty twenty-three, IIHS ran four big crew cab pickups through it, according to Work Truck Online. The Ford F-150, the Ram fifteen hundred and the Chevrolet Silverado fifteen hundred all earned poor. The Toyota Tundra earned marginal. All four protected the driver well. The problem was the back seat. In the F-150 and Ram, the rear dummy showed likely chest injuries and head or neck injuries.""",
   "Chevrolet Silverado 1500 crew cab", "2023: F-150, RAM, SILVERADO POOR")
sc("""And here is the line from the IIHS president, David Harkey, that every truck family should hear. Quote, submarining was a problem for all four pickups, and belt forces were too high in all but the Tundra. Submarining means the lap belt rides up from the hips onto the stomach, which can cause internal injuries. In all four of America's best-known full-size trucks, the rear passenger slid under the belt.""",
   "Toyota Tundra crew cab rear", "\"SUBMARINING IN ALL FOUR\"")
sc("""Now the twist. These same trucks did well in the updated side crash test. Ram, Ford and Toyota earned good, and the Silverado earned acceptable. So these pickups are not weak trucks. They are strong trucks with rear seat belts that were not designed for the newest test. Harkey said large pickups do not perform as well in the new moderate overlap evaluation as they do in the updated side test. The structure is fine. The back seat is the problem.""",
   "Ford F-150 side", "STRONG STRUCTURE, WEAK REAR BELTS")

# ---------- 3. THE BIG THREE IN 2026 ----------
sc("""So how do the best-selling trucks look in twenty twenty-six? Start with the Chevrolet Silverado fifteen hundred crew cab. According to Pickup Truck and SUV Talk's summary of the IIHS ratings, it scored acceptable in pedestrian crash prevention and side impact, marginal in the small overlap front test, and poor in both the moderate overlap front test and headlights. The article called it the least safe full-size crew cab pickup for twenty twenty-six.""",
   "Chevrolet Silverado 1500 2023", "SILVERADO: POOR IN 2 TESTS")
sc("""And here is the detail that matters for used buyers. Those Silverado results apply to Silverado fifteen hundred crew cabs built since twenty nineteen. So this is not a one-year problem. It covers the whole current generation. And because the Sierra fifteen hundred shares its structure with the Silverado, buyers should check the GMC's own ratings too, rather than assume they are better.""",
   "GMC Sierra 1500 crew cab", "APPLIES TO SILVERADOS SINCE 2019")
sc("""Next, the Ford F-150 crew cab. It scored good in the small overlap front test, side impact, pedestrian crash prevention, and headlights on some versions. But it scored poor in the moderate overlap front test, and poor in the new vehicle-to-vehicle crash prevention test. Those results apply to F-150s built after March twenty twenty-one. So America's best-selling truck failed the back seat test and the new automatic braking test.""",
   "Ford F-150 fourteenth generation", "F-150: POOR IN MODERATE OVERLAP AND V2V")
sc("""Then the Ram fifteen hundred crew cab. Good in the small overlap front test, side impact, pedestrian crash prevention, and headlights on some versions. Poor in the moderate overlap front test, and marginal in vehicle-to-vehicle crash prevention. Pickup Truck and SUV Talk called it the safest American pickup in the testing, with results that apply to twenty twenty-five and twenty twenty-six models.""",
   "Ram 1500 2025", "RAM: SAFEST AMERICAN PICKUP, STILL POOR")
sc("""Here is the twist. The safest American pickup still earned a poor rating in the same back seat test as the others. So when an ad says a truck earned top marks in a crash test, ask which test. Every one of these trucks can honestly advertise good ratings. And every one of them, in its crew cab form, has a poor rating in the test that measures what happens to your passenger in the back.""",
   "Ford F-150 Ram 1500 Chevrolet Silverado", "ASK: WHICH TEST?")

# ---------- 4. TUNDRA ----------
sc("""Now the Toyota Tundra crew cab, the only traditional pickup with an award in twenty twenty-six. According to Pickup Truck and SUV Talk, it scored good in the three crashworthiness tests, good or acceptable in headlights, and acceptable in pedestrian crash prevention. It also scored good on seat belt reminders. That is a big improvement from the marginal rating in the twenty twenty-three back seat test.""",
   "Toyota Tundra 2025", "TUNDRA: TOP SAFETY PICK")
sc("""But here is the twist. The Tundra was a Top Safety Pick Plus in twenty twenty-five, and it dropped to plain Top Safety Pick in twenty twenty-six. Not because it got worse in a crash, but because it had no score in the new vehicle-to-vehicle crash prevention test, which the top award now requires. The truck did not change. The rules did. That is how fast the safety bar moves.""",
   "Toyota Tundra TRD Pro", "TSP+ IN 2025, TSP IN 2026")
sc("""And notice the difference from twenty twenty-three. Back then, IIHS said belt forces were too high in all four big pickups except the Tundra, and the Tundra's main issue was belt positioning that raised chest injury risk. Toyota's rear seat design was already closer to passing. That is why it is the only traditional pickup that qualified. It is a reminder that rear seat safety is a design choice, not something only small cars can do.""",
   "Toyota Tundra crew cab interior", "REAR SAFETY IS A DESIGN CHOICE")

# ---------- 5. CYBERTRUCK ----------
sc("""And then the Tesla Cybertruck crew cab, the only pickup with Top Safety Pick Plus in twenty twenty-six. According to Pickup Truck and SUV Talk, it scored good in all six award categories. That includes the back seat test that the F-150, Ram and Silverado failed, the headlights, pedestrian crash prevention, and the new vehicle-to-vehicle test.""",
   "Tesla Cybertruck", "CYBERTRUCK: GOOD IN ALL 6")
sc("""Here is the twist. The Cybertruck is the most polarizing truck on the road. It has been recalled for a glued-on panel, for an accelerator pedal pad, and for wheel studs, as we covered in earlier videos. And yet, in the crash tests that decide this award, it beat every other pickup. A truck can be controversial, recalled, and still be the best performer in the official safety tests. Those are simply different questions.""",
   "Tesla Cybertruck front", "RECALLED. CONTROVERSIAL. TOP RATED.")
sc("""It was not perfect. Outside the award categories, it scored marginal on seat belt reminders, and acceptable on LATCH ease of use, the anchors for child seats, according to the same report. So if you install child seats often, or you want the strongest seat belt reminders, those details are worth checking. But on the tests that IIHS uses to decide its top award, no pickup did better.""",
   "Tesla Cybertruck rear", "MARGINAL: SEAT BELT REMINDERS")

sc("""Let's stop and count what we have so far. Among the five best-known full-size crew cabs, one earned the top award, one earned the second award, and three earned poor in the back seat test. And the two winners were the newest designs to be updated for the tougher tests. That pattern tells you something. Safety ratings reward recent engineering, so the model year can matter as much as the brand.""",
   "Toyota Tundra and Ford F-150", "THE SCORE SO FAR: 2 WINNERS, 3 POOR")
# ---------- 6. SMALL PICKUPS ----------
sc("""Now the small and midsize pickups, which many families buy because they are easier to park and cheaper. In twenty twenty-three, IIHS tested five small crew cabs in the updated back seat test. None earned good. The Nissan Frontier earned acceptable. The Ford Ranger earned marginal. And the Chevrolet Colorado, the Jeep Gladiator and the Toyota Tacoma all earned poor, according to Work Truck Online.""",
   "Toyota Tacoma crew cab", "SMALL PICKUPS: NONE GOOD")
sc("""The details matter. In the Colorado, Frontier, Ranger and Tacoma, the rear dummy's head came too close to the front seatback. The Gladiator's rear seat had no side curtain airbag, which raised the risk of injury in a hard impact. And in the Ranger, the rear dummy submarined under the lap belt. IIHS president David Harkey said, quote, the rear seat belts need improvement.""",
   "Jeep Gladiator", "GLADIATOR: NO REAR CURTAIN AIRBAG")
sc("""And in twenty twenty-six, the problem was still there. On September third, twenty twenty-six, GM Authority reported that the twenty twenty-six GMC Canyon crew cab earned marginal in the updated moderate overlap test. The structure was rated good, and the driver was well protected. But the rear passenger's head approached the front seatback, and measurements showed a moderate risk of head, neck and chest injury.""",
   "GMC Canyon AT4", "2026 CANYON: MARGINAL")
sc("""Here is the twist for small truck buyers. Many people choose a smaller pickup because it feels safer and easier to drive than a giant full-size truck. But in the back seat test, the small crew cabs did not do better than the big ones. And IIHS listed no small pickup award winners for twenty twenty-six. If your kids ride in the back, a small truck is not automatically the safe choice.""",
   "Ford Ranger crew cab", "SMALLER ≠ SAFER IN THE BACK")
sc("""One important point, so nobody takes the wrong message. IIHS says the rear seat is still the safest place for young children, according to Fleet and Insurance magazine. Children in proper car seats should stay in the back. The test is about older kids and adults in regular seat belts. The answer is not to move kids to the front. The answer is to buy a truck that protects the back.""",
   "Chevrolet Colorado crew cab", "KIDS STILL BELONG IN THE BACK")

# ---------- 7. HEADLIGHTS AND V2V ----------
sc("""Now the rating almost nobody checks, headlights. IIHS measures how far a vehicle's headlights light the road on straightaways and curves, and whether they create glare. The Silverado fifteen hundred crew cab scored poor. The F-150 and Ram scored good on some versions and acceptable on others. And the word versions is the key. Headlight ratings often change by trim level, because different trims use different lights.""",
   "Chevrolet Silverado 1500 headlights", "HEADLIGHTS: SILVERADO POOR")
sc("""Why does that matter? Trucks are often driven on rural roads at night, with no streetlights, where seeing an animal or a stopped car a few seconds earlier can decide everything. A cheaper trim with weaker headlights may be the more dangerous truck, even if everything else is identical. So if you drive a lot at night, check the headlight rating for the exact trim you are buying.""",
   "Ford F-150 night", "CHECK THE TRIM, NOT JUST THE MODEL")
sc("""And the automatic braking test is the other surprise. The F-150 was poor in the new vehicle-to-vehicle test, and the Ram was marginal. The GMC Canyon was poor in standard front crash prevention in vehicle-to-vehicle testing, according to GM Authority. Remember, this test includes a motorcycle and a semitrailer at highway speeds. If the system cannot see them in time, the driver has to.""",
   "Ford F-150 front", "AUTOMATIC BRAKING: F-150 POOR")

# ---------- 8. PEDESTRIANS ----------
sc("""And the last rating is about the person outside the truck. In November twenty twenty-three, IIHS published a study of nearly eighteen thousand pedestrian crashes, according to NPR. It found that pickups, SUVs and vans with hood heights above forty inches were forty-five percent more likely to cause pedestrian fatalities than vehicles with hoods of thirty inches or less.""",
   "Ram 2500 front hood", "HOOD OVER 40 INCHES: +45% FATALITY RISK")
sc("""Among medium-height vehicles, between thirty and forty inches, those with blunt, vertical front ends were twenty-six percent more likely to cause pedestrian fatalities than those with sloped fronts. Harkey explained why. A tall, flat front strikes a person higher on the torso, pushing them forward and down, which often causes more severe injuries, frequently to the head.""",
   "Chevrolet Silverado HD front", "BLUNT FRONTS: +26%")
sc("""Here is the twist. Trucks did not get dangerous by accident. They got bigger because buyers wanted them bigger. According to IIHS, over the past three decades the average American passenger vehicle has become about four inches wider, ten inches longer, eight inches taller, and one thousand pounds heavier. And NPR reported that pedestrian deaths are at their highest level in more than forty years, up more than eighty percent since twenty oh nine.""",
   "Ford Super Duty front", "+8 INCHES TALLER. +1,000 LB.")

sc("""So what can a buyer do about it? Look at the pedestrian crash prevention rating, which measures whether the truck brakes for people in front of it. According to Pickup Truck and SUV Talk, the F-150 and Ram scored good, while the Silverado and the Tundra scored acceptable. Front cameras and parking sensors help in a driveway too. A tall truck will always have a blind zone in front. The technology is how you shrink it.""",
   "Ram 1500 front camera", "PEDESTRIAN BRAKING: F-150, RAM GOOD")
# ---------- CLOSE ----------
sc("""So what does all of this tell a truck buyer? Big pickups protect their front-seat occupants very well, and most have strong structures. But in twenty twenty-six, the back seat, the headlights, and the newest automatic braking test are where trucks fall behind. And those are exactly the things that ads, dealers and spec sheets almost never mention.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "THE GAPS: BACK SEAT, LIGHTS, BRAKING")
sc("""And here is the final twist. The two pickups that won awards are the one with the most traditional reputation, the Toyota Tundra, and the one with the least traditional design, the Tesla Cybertruck. The three best-selling American trucks, the ones on every dealer lot, did not qualify. Popularity and safety ratings are two completely different things.""",
   "Toyota Tundra and Tesla Cybertruck", "POPULAR ≠ TOP RATED")
sc("""So here is your safety checklist for twenty twenty-seven. One, look up the IIHS ratings for the exact cab style and model years. Two, if anyone rides in the back, check the moderate overlap rating, and specifically the rear passenger. Three, check the headlight rating for your exact trim. Four, confirm front crash prevention is standard, and check its vehicle-to-vehicle score. Five, think about who walks around your truck, especially children in your driveway.""",
   "Ram 1500 Laramie", "5 SAFETY CHECKS FOR 2027")
sc("""We put this checklist into the Twenty Twenty-Seven Truck Buyer's Guide, along with every other check from this channel. The link is in the description and in the pinned comment. If this helped, subscribe, because next we answer how long trucks really last, using real mileage data. And tell us in the comments, did any of these ratings surprise you? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In twenty twenty-six, the safest pickup": "Intro", "On March twenty-fourth": "The 2026 safety awards", "Before we get to each truck": "The back seat test",
      "So how do the best-selling trucks": "F-150, Ram and Silverado in 2026", "Now the Toyota Tundra crew cab": "Toyota Tundra",
      "And then the Tesla Cybertruck crew cab": "Tesla Cybertruck", "Now the small and midsize": "Small and midsize pickups",
      "Now the rating almost nobody": "Headlights and automatic braking", "And the last rating": "Hood height and pedestrians",
      "So what does all of this tell": "Safety checklist for 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video27", "length_scale": 1.45,
  "title": "The Truck Safety Ratings Nobody Talks About (F-150, Ram and Silverado Failed This Test)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
