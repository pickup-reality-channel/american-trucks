import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The number one problem owners report on three-year-old vehicles is not the engine. It is not the transmission. It is the phone connection. Meanwhile, more than a hundred thousand F-150s could roll away in park, and millions of trucks had trailer brakes that could quietly stop working. These are six truck problems nobody warns you about before you buy.""",
   "Ford F-150 pickup truck", "6 PROBLEMS NOBODY MENTIONS")

# ---------- COLD OPEN ----------
sc("""When you shop for a truck, everybody warns you about the same things. Check the engine. Check for rust. Check the mileage. That advice is fine, but it is from another era. A modern pickup is a rolling network of computers, cameras and modules, and in twenty twenty-five and twenty twenty-six, many of the problems that reached owners came from places a test drive will never show you.""",
   "Chevrolet Silverado 1500 interior", "THE OLD ADVICE IS NOT ENOUGH")
sc("""Here is the proof. In J.D. Power's twenty twenty-six Vehicle Dependability Study, problem counts were the highest since the study was revised in twenty twenty-two, according to Ford Authority. And the leading complaint category was not mechanical. It was infotainment. At the same time, the biggest truck recalls of the year were about cameras, trailer electronics and software, not pistons and bolts.""",
   "Ram 1500 interior screen", "HIGHEST PROBLEM COUNT SINCE 2022")
sc("""So in this video, we go through six problems that show up again and again in recalls, studies, lawsuits and owner reports, and that most buyers never hear about until it is too late. For each one, you will hear which trucks are affected, what the documented fix is, and how to check before you buy. And yes, there is a twist in every one, because some of these problems are worse than they sound, and some are better.""",
   "Ford Super Duty pickup", "WHAT, WHICH TRUCKS, HOW TO CHECK")
sc("""As always, every fact here comes from a published source, listed in the description. Where something is only an allegation in a lawsuit, we will say so. Where a problem is rare, we will say that too. Fear is not the goal. Knowing what to check is. Let's start with the problem almost every owner has, and almost nobody expects.""",
   "Toyota Tundra pickup", "FACTS, NOT FEAR")

# ---------- 1. INFOTAINMENT ----------
sc("""Problem number one is the screen and the phone. In J.D. Power's twenty twenty-six dependability study, which surveyed owners of three-year-old twenty twenty-three vehicles, four of the five most reported problems involved smartphone connectivity, according to Pickup Truck and SUV Talk. Apple CarPlay and Android Auto issues led for the third year in a row, at eight point nine problems per hundred vehicles.""",
   "Ford F-150 interior dashboard", "#1 COMPLAINT: CARPLAY / ANDROID AUTO")
sc("""And the problem goes beyond phones. Bluetooth, wireless charging pads and the manufacturers' own apps made up nearly half of all infotainment problems in the study. On the Ford Super Duty, owners have reported backup camera color distortion, blank screens, and center touchscreens that freeze or reboot while driving, according to Pickup Truck and SUV Talk. Consumer Reports blamed in-car electronics for much of the Ram fifteen hundred's low score.""",
   "Ford Super Duty interior touchscreen", "SCREENS FREEZE. PHONES DROP.")
sc("""Here is the twist. Over-the-air updates were supposed to fix all of this. In the same J.D. Power study, forty percent of owners had received an over-the-air update in the past year. But only twenty-seven percent said it improved their vehicle. And updates were associated with an increase of two point five problems per hundred vehicles. Sometimes the fix brings new problems of its own.""",
   "Tesla Cybertruck interior", "UPDATES: 40% GOT ONE, 27% SAW IMPROVEMENT")
sc("""Why does this matter if it is just a screen? Because on a modern truck, the screen controls far more than music. It shows the backup camera, the trailer settings, the four-wheel-drive modes on some trucks, and in many cases the climate controls. A frozen screen in a truck is not like a frozen phone. It can take away the one camera you need to back up a trailer.""",
   "Ram 1500 Laramie interior", "THE SCREEN RUNS THE TRUCK")
sc("""So how do you check? On a test drive, connect your own phone, wired and wireless. Make a call. Start navigation. Put the truck in reverse three or four times and watch how fast the camera appears. Then turn the truck off and on again and repeat. It takes five minutes, and it tests the exact problem owners complain about most. Now, problem number two, and it is the camera itself.""",
   "Chevrolet Silverado 1500 LTZ interior", "TEST: YOUR PHONE, 5 MINUTES")

# ---------- 2. BACKUP CAMERAS ----------
sc("""Problem number two is the backup camera. Since twenty eighteen, federal rules have required backup cameras on new vehicles, so a camera that fails is a safety issue, not a convenience. And in the last two years, camera recalls have hit almost every truck brand. In January twenty twenty-six, Toyota recalled one hundred sixty-two thousand Tundras because the display could freeze or go black, according to Autoblog.""",
   "Toyota Tundra 2024", "TUNDRA: 162,000 CAMERA RECALL")
sc("""Ram's heavy-duty trucks were part of a camera recall covering eight hundred forty-four thousand and twenty-seven vehicles, because the image may not display in reverse, according to federal campaign data compiled by Lemberg Law. And Ford recalled sixty-five thousand, three hundred eighty-five twenty twenty-three and twenty twenty-four Super Duty trucks whose SYNC four software could show a delayed, frozen or missing camera image, according to Pickup Truck and SUV Talk.""",
   "Ram 2500 Heavy Duty", "RAM HD: 844,027. SUPER DUTY: 65,385.")
sc("""But Ford's camera story is the biggest. In October twenty twenty-five, Reuters reported a recall of nearly one point four five million older Ford vehicles for distorted, intermittent or blank camera images, after one point nine million vehicles worldwide the month before. Ford knew of about twelve thousand, five hundred warranty claims and five crashes, with no injuries. And in November twenty twenty-four, Ford had agreed to a one hundred sixty-five million dollar penalty for recalling cameras too slowly.""",
   "Ford Explorer", "FORD: $165 MILLION CAMERA PENALTY")
sc("""Here is the twist that most F-150 owners do not know. Along with the October recall, Ford extended rear camera coverage on millions of vehicles with a fifteen-year warranty program, covering more than two dozen models, including twenty fifteen to twenty twenty F-150 trucks, according to Reuters. If you own one of those F-150s and your camera fails, you may not have to pay for it. If you are buying one, ask the dealer to confirm.""",
   "Ford F-150 thirteenth generation", "F-150 2015-2020: 15-YEAR CAMERA COVERAGE")
sc("""How do you check? Put the truck in reverse several times, cold and warm, and watch for a delay, a black screen, or a distorted image. Then run the VIN, because a camera recall may already be open on that truck. And remember that camera problems are often software, so a dealer update can fix them in minutes. The camera is cheap to check, and expensive to ignore. Problem number three is invisible from the driver's seat.""",
   "Ford F-150 rear tailgate camera", "REVERSE 5 TIMES. RUN THE VIN.")

# ---------- 3. TRAILER ELECTRONICS ----------
sc("""Problem number three is the trailer connection. Not the hitch. The electronics. On February twentieth, twenty twenty-six, Ford recalled four million, three hundred eighty-one thousand, eight hundred seventy-eight vehicles, including the F-150, Super Duty, Maverick and Ranger, because the truck could lose communication with the trailer. The trailer's brake lights and turn signals could malfunction, and the trailer brakes could stop working, according to Motor1 and SlashGear.""",
   "Ford F-150 towing trailer", "4.38 MILLION: TRAILER BRAKES COULD FAIL")
sc("""Pickup Truck and SUV Talk describes one part of it on the Super Duty, recall twenty-six V one zero four. A software error can make the integrated trailer module lose communication at startup. That can disable trailer brake lights and turn signals, and on higher-series modules, the trailer brakes themselves. Ford offered an over-the-air update or dealer reprogramming.""",
   "Ford F-250 Super Duty towing", "THE MODULE CAN DROP OUT AT STARTUP")
sc("""Here is the twist. Ram had almost the same problem in the same month. A recall reported in early February twenty twenty-six covered four hundred fifty-six thousand, two hundred eighty-seven Ram heavy-duty vehicles, because a trailer tow module could make trailer lights fail and trailer brakes stop working, according to federal campaign data compiled by Lemberg Law. Two rivals, two suppliers, one weak point.""",
   "Ram 3500 towing trailer", "RAM HD: 456,287, SAME MONTH")
sc("""And this is the scary part about trailer problems. You cannot see them. From the driver's seat, everything looks normal. The trailer is behind you, the lights are behind the trailer, and the brakes are inside the trailer's wheels. The driver behind you is the first person to find out your brake lights are dead. That is why this problem deserves a place on this list.""",
   "Ford Super Duty with camper trailer", "YOU CANNOT SEE IT FROM THE SEAT")
sc("""So how do you check? Before every trip, have someone stand behind the trailer while you press the brake and use both turn signals. Watch the trailer brake controller display on the dash while you roll slowly and apply the trailer brakes manually. And if you are buying a truck to tow, confirm the trailer module recall was completed. It is one of the cheapest safety checks you can make.""",
   "Ford F-150 hitch trailer", "THE TWO-PERSON LIGHT CHECK")

# ---------- 4. TRANSMISSIONS ----------
sc("""Problem number four is the transmission, and specifically how it shifts. Many full-size trucks now use ten-speed automatics. Ford's ten R eighty was developed through a joint venture between Ford and General Motors, according to Law three sixty Canada. More gears help fuel economy and towing. But owners of trucks with this transmission have reported harsh shifts, shudder and unexpected downshifts.""",
   "Ford F-150 Raptor", "10-SPEED: MORE GEARS, MORE COMPLAINTS")
sc("""In April twenty twenty-five, a proposed class action was filed in Vancouver against Ford, covering Canadian owners of the F-150, Ranger, Expedition, Mustang and Lincoln Navigator with the ten R eighty, from model years twenty seventeen and twenty eighteen onward. The suit alleges difficulty shifting, lunging when shifting from park to drive, shuddering, and sudden shifts the driver did not request. These are allegations, and the class has not been certified.""",
   "Ford Expedition", "ALLEGED: LUNGING, SHUDDER, SUDDEN SHIFTS")
sc("""Here is the twist. One of those complaints turned into a real recall. On April fourteenth, twenty twenty-six, Ford recalled one million, three hundred ninety-two thousand, nine hundred thirty-five twenty fifteen to twenty seventeen F-150s, because of an unexpected downshift that can cause a loss of control, according to Motor1. Federal regulators had investigated unexpected downshifts on these trucks before, according to Law three sixty Canada.""",
   "Ford F-150 2016", "1.39 MILLION F-150s: DOWNSHIFT RECALL")
sc("""And Ford is not alone with ten-speed questions. Consumer Reports noted transmission complaints on GM trucks, and Pickup Truck and SUV Talk reported that some twenty twenty-four and twenty twenty-five Silverado heavy-duty owners described valve body failures and full transmission replacements, with GM running a customer satisfaction program for a transmission bearing issue on certain twenty twenty-four trucks. So this is an industry-wide issue, not one brand's.""",
   "Chevrolet Silverado 2500HD", "GM HD: VALVE BODY REPORTS")
sc("""How do you check on a test drive? Drive the truck cold, not after the dealer has warmed it up. Pay attention to the shift from park to drive, the first few upshifts, and coasting down to a stop. A clunk, a shudder or a delayed engagement is worth asking about. Then ask whether the transmission software has been updated, because many shift complaints are addressed with reprogramming. Now, problem number five could let your truck roll away.""",
   "Ford F-150 XLT", "DRIVE IT COLD")

# ---------- 5. ROLLAWAY / AXLES ----------
sc("""Problem number five is the rear axle, and it can show up in the worst possible moment, when you think the truck is parked. In August twenty twenty-five, Ford recalled up to one hundred three thousand, one hundred seventy-four twenty twenty-three to twenty twenty-five F-150s with a nine point seven five inch heavy-duty rear axle, according to RV Travel. The rear axle hub bolt can wear and snap, damaging the axle hub splines.""",
   "Ford F-150 2023", "F-150: 103,174 AXLE HUB BOLTS")
sc("""And here is what that means. With damaged splines, the truck can roll away while in park, if the parking brake is not set. Or it can lose drive power. The fix is replacing both rear axle shafts, and owner letters were scheduled in phases from August twenty twenty-five all the way through May twenty-second, twenty twenty-six. That recall expanded an earlier one, numbered twenty-three V eight nine six.""",
   "Ford F-150 parked", "PARK CAN FAIL. SET THE PARKING BRAKE.")
sc("""Here is the twist. The trucks affected are the ones built to tow the most, with the heaviest-duty rear axle Ford offers on the F-150. The option buyers choose for strength was the part being recalled. And the Super Duty had a similar story. In twenty twenty-three, Ford recalled forty-one thousand, four hundred sixty-eight twenty twenty-three F-two fifty and F-three fifty trucks because an incomplete heat treatment could let the left rear axle shaft fracture, leaving the truck unable to hold in park, according to Pickup Truck and SUV Talk.""",
   "Ford F-350 Super Duty", "THE HEAVY-DUTY OPTION WAS THE PROBLEM")
sc("""That makes the cheapest habit in this whole video also one of the most important. Always set the parking brake, every time, even on flat ground. Truck owners often skip it, because park feels like enough. These two recalls show that park depends on a small part inside the transmission and on the axle staying in one piece. The parking brake is a second, separate system. Use it.""",
   "Ford Super Duty parking", "ALWAYS USE THE PARKING BRAKE")

sc("""There is one more hidden problem that belongs next to the axle, because it also takes power away without warning. In twenty twenty-five, Ford recalled about eight hundred fifty thousand Ford and Lincoln vehicles, including more than one hundred thirteen thousand Super Duty trucks with the six point two, six point eight and seven point three liter gas engines, because the low-pressure fuel pump could lose pressure and stall the engine, according to Pickup Truck and SUV Talk.""",
   "Ford F-250 Super Duty gas", "SUPER DUTY GAS: FUEL PUMP STALL")
sc("""And here is the detail that makes it a nobody-warns-you problem. The report says failure is more likely with low fuel or in hot weather. That is exactly the situation of a work truck in the summer, running on the last quarter of the tank between jobs. Ford says the affected trucks were built from July twenty twenty-one to July twenty twenty-two. The Power Stroke diesels were not included.""",
   "Ford F-350 work truck", "LOW FUEL + HEAT = HIGHER RISK")
# ---------- 6. DEATH WOBBLE ----------
sc("""Problem number six has the scariest name. Owners call it the death wobble. It is a violent shaking of the front end that can start after hitting a bump at highway speed, according to Pickup Truck and SUV Talk. It is most associated with solid front axle trucks, like the Ford Super Duty. And when it happens, the steering wheel shakes so hard that many drivers have to slow down almost to a stop before it ends.""",
   "Ford F-250 Super Duty front", "THE \"DEATH WOBBLE\"")
sc("""Here is what is documented. Pickup Truck and SUV Talk reports that Ford redesigned the suspension, that the redesign did not fully fix the problem, and that reports now suggest it is far less common than before. Owners typically fix it by replacing track bars, ball joints and steering dampers. And no recall has been issued for this issue on twenty twenty-three to twenty twenty-six F-Series Super Duty trucks.""",
   "Ford F-350 front suspension", "NO RECALL FOR 2023-2026")
sc("""And here is the twist in court. A class action over death wobble on older Super Duty trucks has been running for about seven years. In twenty twenty-six, according to Autoblog, a federal appeals court, the Ninth Circuit, reversed the class certification and sent the case back to the lower court. It accepted Ford's argument that the problem showed up at different rates across years and platforms. The case is not over, but it looks weaker for owners.""",
   "Ford F-250 pickup", "APPEALS COURT REVERSED CLASS STATUS")
sc("""So if you are buying a used heavy-duty truck with a solid front axle, drive it on the highway, and over a few expansion joints or rough patches at speed. Ask whether the track bar, ball joints or steering damper have been replaced, and when. And be careful with oversized tires and lifts, because they change the front-end geometry. A front end that has been maintained is a very different truck from one that has not.""",
   "Ford Super Duty lifted", "TEST AT HIGHWAY SPEED")

sc("""Notice something about problems five and six. Both are made worse by how trucks are used. Towing, hauling, lifting, big tires, hot days, low fuel. The trucks most likely to show these problems are the ones that work the hardest. So if a used truck spent its life towing or carries a lift kit, the checks we just covered matter twice as much.""",
   "Ford F-250 towing", "HARD WORK, HIGHER RISK")
# ---------- BONUS ----------
sc("""Before we finish, a bonus problem that is rare but expensive, and that is exactly why you should know it. The General Motors three liter Duramax diesel, the L Z zero, in the Silverado and Sierra fifteen hundred. According to Pickup Truck and SUV Talk, a small number of owners have reported failures of the crankshaft thrust bearings, which can cause excessive crankshaft end play, low oil pressure, and in some cases a complete engine replacement.""",
   "Chevrolet Silverado 1500 Duramax", "BONUS: 3.0L DURAMAX THRUST BEARINGS")
sc("""In June twenty twenty-six, a teardown of one failed engine with about seven thousand five hundred miles found only one complete thrust bearing, plus fragments of another. The writer suggested the engine may have left the factory with a bearing missing, but noted that cannot be proven. The report stresses that failures are relatively uncommon among the thousands of these trucks on the road. Rare, but worth asking about.""",
   "GMC Sierra 1500 diesel", "RARE, BUT DOCUMENTED")
sc("""And one more quiet problem from Ram. In September twenty twenty-four, Stellantis recalled one million, two hundred twenty-seven thousand, eight hundred eight Ram fifteen hundreds in the United States, because the anti-lock brake module software could disable electronic stability control, according to CarScoops. The brakes still worked normally. But a safety system that helps prevent skids could switch off without the driver knowing. A software update fixed it.""",
   "Ram 1500 2022", "RAM: 1.2 MILLION, ESC SOFTWARE")

sc("""Put those two together and you see why software matters even for the most basic safety systems. In one case, a stability system could be turned off by code. In another, trailer brakes could be turned off by code. Neither one would show up on a quick test drive, and neither one shows up as a warning light you would notice. The only way to know is the recall record.""",
   "Ram 1500 Rebel", "CODE CAN SWITCH OFF SAFETY")
# ---------- CLOSE ----------
sc("""So look at the six problems together. A screen that freezes. A camera that goes black. A trailer module that drops out. A transmission that shifts on its own. An axle that lets the truck roll in park. And a front end that shakes at highway speed. Only two of them are the kind of mechanical problem your grandfather would recognize. The rest are electronics and software.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "4 OF 6: ELECTRONICS")
sc("""And here is the final twist. The electronic problems are the most common, but often the easiest to fix, a software update at the dealer or over the air. The mechanical ones are rarer, but they are the ones that can cost you, or put you in danger. So a smart buyer tests both. You play with the screen and the camera like a kid, and you drive the truck cold, on the highway, like a mechanic.""",
   "Ford Super Duty pickup", "TEST THE SCREEN AND THE STEEL")
sc("""Here is the checklist for twenty twenty-seven. One, connect your phone and test the screen. Two, reverse five times and watch the camera. Three, test trailer lights with a helper. Four, drive cold and feel every shift. Five, check that the parking brake holds on a slope. Six, test the steering at highway speed over bumps. And seven, run the VIN for every open recall.""",
   "Chevrolet Silverado 1500", "THE 7-POINT TEST DRIVE")
sc("""We put this full test-drive checklist into the Twenty Twenty-Seven Truck Buyer's Guide, along with the questions to ask a dealer. The link is in the description and in the pinned comment. If this helped you, subscribe, because next we look at five transmission problems that cost owners thousands. And tell us in the comments, which of these six problems have you had? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The number one problem owners report": "Intro", "Problem number one": "1. Screens and phone connection", "Problem number two": "2. Backup cameras",
      "Problem number three": "3. Trailer electronics", "Problem number four": "4. 10-speed transmissions", "Problem number five": "5. Rear axles and rollaway",
      "Problem number six": "6. Death wobble", "Before we finish, a bonus": "Bonus: 3.0L Duramax and Ram ESC software",
      "So look at the six problems": "The 7-point test drive for 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video25", "length_scale": 1.42,
  "title": "6 Truck Problems Nobody Warns You About (Check Before You Buy in 2027)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
