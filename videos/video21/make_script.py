import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One recall in twenty twenty-six covered four point three million trucks and SUVs in a single day. Another covered one and a half million Ram pickups because a seat belt anchor might not be attached. And one of America's most popular V8 engines is now under federal investigation, after the recall fix itself kept failing. These are the trucks with the most recalls of twenty twenty-six.""",
   "Ford F-150 pickup truck", "4.3 MILLION IN ONE RECALL")

# ---------- COLD OPEN ----------
sc("""Here is a number that should make every truck owner stop for a second. In twenty twenty-five, Ford issued one hundred fifty-three recalls covering nearly thirteen million vehicles. According to Motor1, that is the most recalls any automaker has ever issued in a single year, more than double the previous record holder, General Motors. And twenty twenty-six did not slow down.""",
   "Ford F-150 XLT pickup", "FORD 2025: 153 RECALLS")
sc("""By the twenty-third of June, twenty twenty-six, Motor1 counted fifty Ford recalls covering more than eleven point two million vehicles. Kelley Blue Book, citing the Department of Transportation, counted fifty-six recalls by early July. Half a year, and Ford was already close to its total number of vehicles from the record year before. So the question is not whether your truck has a recall. The question is how many.""",
   "Ford Super Duty pickup", "2026: 11.2 MILLION BY JUNE")
sc("""But this is not only a Ford story. Stellantis recalled more than one and a half million Ram fifteen hundreds over a hidden seat belt problem. General Motors is under a federal engineering investigation covering almost one million trucks and SUVs with its six point two liter V8. And even Toyota, the brand people buy because they never want to see the inside of a service department, recalled one hundred sixty-two thousand Tundras this year.""",
   "Ram 1500 pickup truck", "RAM, GM, TOYOTA TOO")
sc("""So in this video, we go truck by truck through the seven pickups with the biggest recall stories of twenty twenty-six. For each one, you will hear what failed, how many trucks are involved, and what the fix actually is. And there is a twist in almost every one of them, because the biggest recall of the year is not the most dangerous one, and the most dangerous one is not the biggest.""",
   "Chevrolet Silverado 1500 pickup", "7 TRUCKS. 7 RECALL STORIES.")
sc("""A quick note before we start. Every number in this video comes from a published source, mostly federal recall data reported by outlets like Motor1, Kelley Blue Book and GM Authority. The sources are listed in the description. And remember, a recall is not a verdict that a truck is bad. It is a public admission that something needs fixing, and the fix is free. Let's start with the biggest one.""",
   "Ford F-150 Lightning", "EVERY NUMBER IS SOURCED")

# ---------- 1. FORD F-150 ----------
sc("""Truck number one is the Ford F-150, the best-selling truck in America, and in twenty twenty-six the most recalled one too. On February twentieth, Ford filed a recall covering four million, three hundred eighty-one thousand, eight hundred seventy-eight vehicles. According to Motor1, it covered the twenty twenty-one to twenty twenty-six F-150, the Super Duty, the Maverick, the Ranger, the Expedition, the E-Transit and the Lincoln Navigator.""",
   "Ford F-150 fourteenth generation", "FEB 20: 4,381,878 VEHICLES")
sc("""The problem was trailer communication. According to the federal safety agency, NHTSA, as reported by SlashGear, these trucks could have trouble talking to a trailer. The trailer's brake lights and turn signals could stop working, and the trailer brakes themselves could become nonfunctional. Think about what that means on a highway, with several thousand pounds behind you and a car following too close.""",
   "Ford F-150 towing trailer", "TRAILER LIGHTS AND BRAKES")
sc("""Now the first twist. The largest recall of the year was fixed mostly without a wrench. Motor1 reports that the cause was a software issue, and Ford is fixing it with an over-the-air update, the same way your phone updates overnight. That is why the number is so big. A software bug does not care which plant built the truck. It lives in every truck running the same code, across seven different models.""",
   "Ford F-150 Raptor", "THE FIX: AN OVER-THE-AIR UPDATE")
sc("""But the F-150 had a second recall that is very different. On April fourteenth, twenty twenty-six, Ford recalled one million, three hundred ninety-two thousand, nine hundred thirty-five F-150s from the twenty fifteen to twenty seventeen model years. The problem, according to Motor1, was an unexpected downshift that can cause a loss of control. This one is not about a new truck. It is about trucks that are nine, ten and eleven years old.""",
   "Ford F-150 thirteenth generation", "APRIL 14: 1,392,935 OLDER F-150s")
sc("""Here is why that matters if you are shopping for a used truck. An eleven-year-old F-150 has usually been through two or three owners. The person selling it to you may not even know there is an open recall. And a sudden downshift at speed, on a wet road, is the kind of defect you do not want to discover yourself. Motor1 also lists a separate downshift recall for forty-four thousand, nine hundred sixty-three twenty fourteen F-150s.""",
   "Ford F-150 2015", "USED BUYERS: CHECK THE VIN")
sc("""And the list keeps going. Motor1 counted daytime running lights that may not dim on ninety-one thousand, one hundred ninety-eight F-150s from twenty nineteen and twenty twenty. Unintended vehicle movement on ten thousand, seven hundred forty-two twenty eighteen trucks. An instrument cluster failure on four thousand, four hundred forty-five twenty seventeen trucks. Six separate F-150 recalls in the first half of the year alone.""",
   "Ford F-150 pickup", "6 F-150 RECALLS IN 6 MONTHS")
sc("""Now the second twist, and it is a strange one. In twenty twenty-six, J.D. Power named Ford the top mass-market brand in its Initial Quality Study, according to Kelley Blue Book. It was the first time since twenty ten. So the same company that set the all-time recall record was also ranked best for quality in the first months of ownership. How can both be true? The answer is in what each one measures.""",
   "Ford F-150 Platinum", "TOP QUALITY. MOST RECALLS.")
sc("""The quality study asks new owners about problems in the first ninety days. A recall can cover a truck that is ten years old, and it can come from Ford's own internal audits. Kelley Blue Book reports that a software audit forced Ford to repeat some earlier recalls, because some vehicles were recorded as repaired even though they never got the remedy. In other words, part of the recall flood is Ford cleaning up its own records.""",
   "Ford F-150 Lightning pickup", "THE AUDIT FOUND MISSED REPAIRS")
sc("""Ford's chief executive, Jim Farley, has said the company needs to improve its overall quality reputation, including long-term durability. According to Kelley Blue Book, Ford has tied bonuses to quality metrics, restructured its leadership, and hired three hundred fifty technical specialists since twenty twenty-three. Farley has said new vehicle launches must go out perfectly. That is a big promise, and twenty twenty-seven will show whether it holds.""",
   "Ford F-150 XL", "FARLEY: LAUNCHES MUST BE PERFECT")
sc("""There is one more fact about Ford's recall history that most owners never heard. In late twenty twenty-four, the federal safety agency fined Ford for failing to comply with federal recall requirements, as Motor1 notes. The government was not only counting Ford's recalls. It was checking whether Ford reported and fixed them the right way. And that is exactly the pressure that led to the audits we just talked about. Now let's go to the big brother.""",
   "Ford F-250 Super Duty", "NEXT: SUPER DUTY")

# ---------- 2. FORD SUPER DUTY ----------
sc("""Truck number two is the Ford Super Duty, the F-250, F-350 and up. These are the trucks people buy to tow horse trailers, campers and equipment. So it hurts that the Super Duty was part of the same four point three million trailer recall. For a heavy-duty truck, trailer lights and trailer brakes are not a feature. They are the whole job.""",
   "Ford F-250 Super Duty pickup", "SUPER DUTY: IN THE TRAILER RECALL")
sc("""Then came a recall that sounds even more serious. On March third, twenty twenty-six, Ford recalled eleven thousand, four hundred thirty-one Super Duty trucks from the twenty twenty-five and twenty twenty-six model years, because the driveshaft may separate, according to Motor1. A driveshaft that comes apart while driving is not a slow, gradual failure. It happens all at once, and it can leave a heavy truck without drive power.""",
   "Ford F-350 Super Duty", "MARCH 3: DRIVESHAFT MAY SEPARATE")
sc("""Here is the twist. The biggest Super Duty recalls by number are not the scariest ones. The driveshaft recall covered about eleven thousand trucks. Meanwhile, a windshield wiper recall from March thirty-first covered four hundred twenty-two thousand, six hundred thirteen vehicles, including twenty twenty-two and twenty twenty-three Super Duty trucks, according to Motor1. A big number makes the headline. A small number can still be the one that matters for your truck.""",
   "Ford Super Duty truck", "SMALL RECALL. BIG RISK.")
sc("""And there was one more for diesel and gas owners of older trucks. Motor1 lists a recall of seven thousand, one hundred five Super Duty trucks from twenty twenty to twenty twenty-two, plus the twenty twenty-two F-seven fifty, because the high-pressure fuel pump may fail. When a fuel pump fails, the engine can stall. On a heavy truck pulling a heavy load, that is not a small inconvenience.""",
   "Ford F-450 Super Duty", "FUEL PUMP MAY FAIL")
sc("""So what is the lesson for a heavy-duty buyer? The recall count on a Super Duty is not a reason to panic, but it is a reason to ask one specific question at the dealer. Ask for the full recall history of the exact VIN, and ask which ones were completed. A dealer can print that in minutes. If a seller cannot or will not, that tells you something. Now let's go from the biggest Ford truck to the smallest.""",
   "Ford F-250 pickup", "ASK FOR THE VIN RECALL HISTORY")

# ---------- 3. FORD MAVERICK ----------
sc("""Truck number three is the Ford Maverick, the small hybrid pickup that became a hit because it is cheap and efficient. And here is a number you might not expect. In a study by iSeeCars, based on federal recall data, the Maverick was projected to have more recalls over its lifetime than any other pickup, twenty point seven, about six point four times the industry median of three point two, as Work Truck Online reported.""",
   "Ford Maverick pickup", "MAVERICK: MOST PROJECTED RECALLS")
sc("""Twenty twenty-six did not change that picture. Besides the giant trailer recall, Motor1 lists a recall of forty-seven thousand, eight hundred four twenty twenty-five Mavericks and Rangers for a loss of drive power caused by an E G R valve failure. Three thousand, one hundred seventy twenty twenty-five and twenty twenty-six Mavericks and Bronco Sports where the front passenger airbag may not deploy. And three hundred twenty-three where the moonroof glass may detach.""",
   "Ford Maverick Lariat", "EGR, AIRBAG, MOONROOF")
sc("""But the one that matters most is small. On May twenty-seventh, twenty twenty-six, Ford recalled four thousand, six hundred fifty-three Mavericks and Bronco Sports from twenty twenty-two to twenty twenty-six for a control arm that can separate. And this recall came with a do not drive warning, according to Motor1. Of Ford's first nineteen recalls of the year, SlashGear noted, only one carried that warning. A do not drive warning means exactly what it says.""",
   "Ford Maverick Tremor", "DO NOT DRIVE WARNING")
sc("""Here is the twist. The Maverick shares a lot of parts with the Ford Bronco Sport and the Escape, because they come from the same family of vehicles. That is how Ford keeps the price low. But it also means a problem in one model can show up in another. When you buy a shared-platform truck, you share the savings, and sometimes you share the recalls too.""",
   "Ford Bronco Sport", "SHARED PARTS. SHARED RECALLS.")
sc("""And yet, the Maverick keeps selling. In twenty twenty-five, Ford sold one hundred fifty-five thousand, fifty-one of them, according to The Autopian, outselling the Hyundai Santa Cruz six to one. Buyers clearly decided that a cheap, efficient pickup with a long recall list is still a better deal than the alternatives. That tells you something about how buyers weigh recalls. They care, but price and fuel economy usually win.""",
   "Ford Maverick XLT", "155,051 SOLD IN 2025 ANYWAY")

# ---------- 4. FORD RANGER ----------
sc("""Truck number four is the Ford Ranger, and the new generation had a rough first full year. On April fourteenth, twenty twenty-six, Ford recalled one hundred forty thousand, two hundred one Rangers from twenty twenty-four to twenty twenty-six, because the wiring in the sun visor may cause a fire, according to Motor1. A fire risk from a sun visor. That is not something any buyer thinks to check on a test drive.""",
   "Ford Ranger 2024", "SUN VISOR WIRING: FIRE RISK")
sc("""Two weeks later, on April twenty-eighth, Ford recalled one hundred seventy-nine thousand, six hundred ninety-eight twenty twenty-five and twenty twenty-six Rangers and Broncos for a loose bolt in the front seat frame. A seat that is not properly secured can move in a crash and raise the risk of injury. The Ranger is also in the trailer recall, the E G R valve recall, and a smaller engine failure recall covering one thousand, five hundred thirty-six vehicles.""",
   "Ford Ranger Raptor", "APRIL 28: LOOSE SEAT BOLT")
sc("""Here is the twist. Most of these Ranger recalls hit trucks that are brand new. The twenty twenty-four Ranger was a new generation for the United States. New generations bring new parts, new suppliers and new software, and the first two or three model years are when problems are found. That is why so many experienced buyers say the same thing. Do not buy the first year of a new truck.""",
   "Ford Ranger pickup", "FIRST-YEAR TRUCKS GET RECALLED")
sc("""There is even a recall that sounds almost funny until you think about it. Motor1 lists two hundred sixty-eight twenty twenty-six Rangers and Broncos with incorrect tire and weight capacity information on the label. On a truck that people use to haul and tow, the payload label is the number you trust. If it is wrong, you can overload the truck without knowing. That closes our Ford chapter. Now we go to Ram, and a recall that hid behind the back seat.""",
   "Ford Ranger Wildtrak", "EVEN THE PAYLOAD LABEL")

# ---------- 5. RAM 1500 ----------
sc("""Truck number five is the Ram fifteen hundred. On August third, twenty twenty-six, Stellantis recalled more than one and a half million Ram fifteen hundred pickups from the twenty nineteen to twenty twenty-six model years, as reported by Fox and Reuters. About one point two seven million of them are in the United States, one hundred fifty-six thousand in Canada, fifteen thousand in Mexico, and about seventy-five thousand elsewhere.""",
   "Ram 1500 2019", "AUG 3: 1.5 MILLION RAM 1500s")
sc("""The problem is hidden. Some trucks may have a second-row center or driver-side seat belt buckle anchor that was not properly attached to the body. You would never see it. The belt clicks, it looks normal, and the passenger in the back seat believes they are protected. In a crash, an anchor that is not attached properly may not hold. Stellantis said it was aware of one possible injury linked to the issue.""",
   "Ram 1500 crew cab interior", "REAR SEAT BELT ANCHOR")
sc("""Here is the twist. This recall covers eight model years. Twenty nineteen to twenty twenty-six is the entire current generation of the Ram fifteen hundred. Think about how many families have been driving their kids around in the back seat of these trucks for seven years without knowing. The fix is simple, an inspection, and if needed, the anchor is attached properly. But you only get that fix if you take the truck in.""",
   "Ram 1500 Laramie", "8 MODEL YEARS. ONE GENERATION.")
sc("""And remember the iSeeCars study. It projected nineteen point one lifetime recalls for the Ram fifteen hundred, and nineteen point three for the older Ram fifteen hundred Classic, not counting over-the-air updates. That put two Ram models among the four most recalled pickups in the study, next to the Maverick and the F-150. So the seat belt recall was not a surprise to anyone who follows recall data. It was the biggest example of a pattern.""",
   "Ram 1500 Classic", "RAM 1500: 19.1 PROJECTED RECALLS")
sc("""What should a Ram owner do? Do not wait for the letter. You can check any truck for open recalls on the federal safety website by entering the seventeen-character VIN, the vehicle identification number. It is free and it takes about one minute. And if you are buying a used Ram fifteen hundred from any year between twenty nineteen and twenty twenty-six, ask for proof that this inspection was done.""",
   "Ram 1500 Rebel", "CHECK YOUR VIN FOR FREE")

# ---------- 6. RAM HEAVY DUTY ----------
sc("""Truck number six is the Ram heavy duty, the twenty-five hundred and thirty-five hundred. And this is where you see that the trailer problem was not only a Ford problem. According to federal campaign data compiled by Lemberg Law, a recall reported in February twenty twenty-six covered four hundred fifty-six thousand, two hundred eighty-seven vehicles because a trailer tow module may cause trailer lights to fail and trailer brakes to stop working.""",
   "Ram 2500 Heavy Duty", "RAM HD: TRAILER TOW MODULE")
sc("""Here is the twist. Two of the biggest truck companies in America had almost the same problem in the same month. Ford's trailer recall was filed on February twentieth. Ram's was reported in early February. Two different companies, two different suppliers, and the same weak point. Modern trucks talk to trailers through electronics, and electronics are now where many recalls begin.""",
   "Ram 3500 pickup", "SAME MONTH. SAME WEAK POINT.")
sc("""The same data shows more. A recall covering eight hundred forty-four thousand and twenty-seven vehicles because the rearview camera image may not display in reverse. A software error that may cause the instrument panel display to fail on sixty-five thousand, three hundred forty-eight vehicles. And a powertrain software error on twelve thousand, seven hundred thirty-six vehicles that could let the truck exceed the speed rating of its tires.""",
   "Ram 2500 Power Wagon", "CAMERA, DISPLAY, SPEED LIMITER")
sc("""Notice the pattern. Almost every recall on this list is software. A camera that does not display. A screen that goes blank. A computer that lets the truck go faster than its tires are rated for. Twenty years ago, recalls were mostly about bolts, welds and hoses. In twenty twenty-six, a truck is a computer that tows, and the recall list looks more like a software update log. But the next truck is different. Its problem is pure metal.""",
   "Ram 3500 dually", "A TRUCK IS NOW A COMPUTER")

# ---------- 7. GM 6.2L V8 ----------
sc("""Truck number seven is the Chevrolet Silverado and GMC Sierra fifteen hundred, and the story is an engine, the six point two liter V8, known inside GM as the L eighty-seven. In twenty twenty-five, GM recalled nearly six hundred thousand vehicles with this engine in the United States, under recall twenty-five V two seven four, according to GM Authority. It covered engines built from March twenty twenty-one through May twenty twenty-four.""",
   "Chevrolet Silverado 1500 2022", "GM 6.2L V8: 600,000 RECALLED")
sc("""The defect is serious. GM Authority reports manufacturing problems with the connecting rods and the crankshaft, including rod bearing damage from contamination and crankshafts that may be out of specification. The result can be severe engine damage, a seized engine, and a loss of power while driving. The recall covered the Silverado and Sierra fifteen hundred, plus the Tahoe, Suburban, Yukon and Cadillac Escalade.""",
   "GMC Sierra 1500 Denali", "RODS AND CRANKSHAFT")
sc("""And the fix surprised a lot of owners. GM estimated that roughly three percent of the engines would need replacement. For the engines that passed inspection, the remedy was to switch from a thin zero W twenty oil to a thicker zero W forty oil, and replace the oil filter and the oil fill cap. In other words, for most trucks, the fix for a crankshaft problem was thicker oil.""",
   "Chevrolet Tahoe", "THE FIX: THICKER OIL")
sc("""Now the twist that turned this into one of the biggest truck stories of twenty twenty-six. On August twentieth, twenty twenty-six, the federal safety agency opened an engineering analysis, numbered E A twenty-six zero zero five, covering nine hundred ninety-seven thousand, seven hundred forty-three vehicles from model years twenty twenty-one to twenty twenty-six. The reason was simple. Engines kept failing after the recall repair.""",
   "Chevrolet Silverado 1500 pickup", "AUG 20: FEDERAL INVESTIGATION")
sc("""According to GM Authority, there were four hundred ninety-nine complaints of engine failure after the recall repair. Four hundred seventy-three of those engines had received the thicker oil fix. Twenty-six had received full replacement engines. And there were another one hundred ninety-one reports involving engines built outside the original recall's dates. Six hundred ninety complaints in total. These are complaints alleging failures, not confirmed failures, but the number is why regulators stepped in.""",
   "GMC Sierra 1500", "690 NEW FAILURE COMPLAINTS")
sc("""Think about what that means for a buyer. A truck with a completed recall is normally the safest used truck to buy, because the problem has been fixed. Here, regulators are asking whether the fix itself works. If you are looking at a twenty twenty-one to twenty twenty-six GM truck or SUV with the six point two, the recall paperwork is not the end of the story. Follow the investigation, and keep every oil change receipt.""",
   "Cadillac Escalade", "IS THE FIX ENOUGH?")

# ---------- THE BRANDS YOU EXPECT LEAST ----------
sc("""Before we wrap up, two trucks that did not make the top seven, but tell an important story. The first is the Toyota Tundra. In January twenty twenty-six, Toyota recalled one hundred sixty-two thousand twenty twenty-four and twenty twenty-five Tundra and Tundra Hybrid pickups, because the rearview camera display can freeze or go black, according to Autoblog. The fix is a free software update to the parking assist computer.""",
   "Toyota Tundra 2024", "TUNDRA: 162,000 RECALLED")
sc("""And here is the twist for the brand known for reliability. In twenty twenty-four, Toyota recalled about one hundred thousand twenty twenty-two and twenty twenty-three Tundras, plus about three thousand five hundred Lexus LX six hundreds, because machining debris may have been left inside the engine. The remedy, according to the Associated Press, was to replace the entire engine. Toyota did not say what that cost. Even the most trusted name in trucks can get a recall that big.""",
   "Toyota Tundra TRD Pro", "TOYOTA REPLACED WHOLE ENGINES")
sc("""The second is the Tesla Cybertruck. In May twenty twenty-six, Tesla recalled Cybertrucks with eighteen-inch steel wheels, because rough roads and cornering may cause cracks around the brake rotor stud holes, which can lead to wheel studs separating, according to NHTSA as reported by iHeart. Tesla said there were no reported crashes or injuries, and it is replacing the rotors, hubs and lug nuts for free.""",
   "Tesla Cybertruck", "CYBERTRUCK: WHEEL STUDS")
sc("""It joins a short but memorable list. In twenty twenty-four, the Cybertruck was recalled because the accelerator pedal pad could come loose and get trapped, because the wiper motor could overheat, and because trim on the bed could detach. Then in twenty twenty-five came a recall because the front lights, including the light bar, were too bright for oncoming drivers, fixed with a software update. Small production numbers, but a lot of firsts.""",
   "Tesla Cybertruck front", "PEDAL, WIPER, TRIM, LIGHTS")

# ---------- CLOSE ----------
sc("""So what does all of this mean? Here is the pattern across every truck in this video. The biggest recalls of twenty twenty-six were mostly software, fixed over the air or at the dealer in minutes. The most dangerous ones were often small, a few thousand trucks with a do not drive warning or a driveshaft that can separate. And the hardest ones were mechanical, like an engine where even the fix is under investigation.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "BIG ≠ DANGEROUS")
sc("""And here is the twist that ties it all together. A truck with many recalls is not automatically a bad truck, and a truck with few recalls is not automatically a good one. The F-150 set records for recalls and also won an initial quality award. The Maverick has the highest projected recall count of any pickup and still sells over one hundred fifty thousand a year. What matters is whether the recalls on your truck were actually done.""",
   "Ford Maverick pickup", "WHAT MATTERS: WAS IT FIXED?")
sc("""So here is your checklist before you buy any truck in twenty twenty-seven, new or used. First, enter the VIN on the federal safety website, and on the brand's own recall page. Second, ask the dealer for the recall and service history of that exact truck, and look for completed repairs, not just notices. Third, if a recall has a do not drive warning or involves the engine, get it in writing that the remedy was done.""",
   "Ram 1500 pickup", "CHECK 1-3: VIN, HISTORY, PROOF")
sc("""Fourth, avoid the first model year of a brand new generation if you can, because that is when most problems surface. And fifth, if a recall remedy is still under development, ask what the dealer will do in the meantime. SlashGear reported that for one of Ford's camera recalls this year, the federal listing said the remedy was still under development. We put every one of these checks, plus the questions to ask a dealer, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Chevrolet Silverado HD", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")
sc("""If this video saved you from buying the wrong truck, or reminded you to check your own, subscribe, because next we look at the biggest truck recalls of the last two years, the ones that changed how the industry builds pickups. And tell us in the comments, has your truck been recalled this year? Thanks for watching.""",
   "Ford F-150 pickup truck", "HAS YOUR TRUCK BEEN RECALLED?")

CH = {"One recall in twenty twenty-six": "Intro", "Truck number one": "1. Ford F-150", "Truck number two": "2. Ford Super Duty",
      "Truck number three": "3. Ford Maverick", "Truck number four": "4. Ford Ranger", "Truck number five": "5. Ram 1500",
      "Truck number six": "6. Ram 2500 and 3500", "Truck number seven": "7. Chevrolet Silverado and GMC Sierra 6.2L V8",
      "Before we wrap up": "Toyota Tundra and Tesla Cybertruck", "So what does all of this mean": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video21", "length_scale": 1.32,
  "title": "7 Trucks With the Most Recalls in 2026 (Check Yours Before 2027)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
