import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One of these engines has been recalled three times in two years, by the brand famous for never breaking down. One is under federal investigation because its recall fix kept failing. And one can fill itself with metal shavings, according to a lawsuit a federal judge just allowed to go forward. These are the engines to avoid in a used truck going into twenty twenty-seven.""",
   "Toyota Tundra 2022", "5 ENGINES TO AVOID")

# ---------- COLD OPEN ----------
sc("""Buying a used truck is a bet on one part more than any other. The engine. Paint can be fixed. A seat can be replaced. But a failed engine in a modern pickup can cost as much as a good used car. And the problem is that the engines with the worst stories do not look different on the lot. They start, they idle, they pull, until the day they do not.""",
   "Chevrolet Silverado 1500 used truck", "THE ENGINE IS THE BET")
sc("""Here is the twist that most buyers miss. The engines on this list are not old, forgotten designs. Most of them were built in the last five years, in some of the best-selling trucks in America, from Toyota, General Motors and Ford. These are the trucks you will find all over the used market in twenty twenty-seven, often at prices that look like a bargain.""",
   "Ford F-150 pickup truck", "RECENT ENGINES. POPULAR TRUCKS.")
sc("""So for each engine, you will hear what goes wrong, which years are involved, what the manufacturer did about it, and what it could cost you if the warranty is gone. Stay until the end, because there is a bonus engine, and a simple checklist that can save you thousands before you sign anything.""",
   "Ram 1500 EcoDiesel", "PLUS A BONUS ENGINE")
sc("""One important rule for this video. Avoiding an engine does not mean every truck with it will fail. Most will not. It means the risk is documented, by recalls, investigations or court cases, and you should either skip it, or buy it only with proof that the problem was handled. Every number here comes from a published source, listed in the description. Let's start with the most surprising one.""",
   "Toyota Tundra TRD Pro", "DOCUMENTED RISK, NOT A VERDICT")

# ---------- 1. TOYOTA 3.4 ----------
sc("""Engine number one is the Toyota three point four liter twin-turbo V6, the engine Toyota put in the new Tundra when it dropped the old V8. And it comes from the brand that built its whole truck reputation on engines that refuse to die. Which is exactly why this story is so surprising. According to Motor1, this engine has now been the subject of three separate recalls.""",
   "Toyota Tundra 2022 i-Force", "TOYOTA 3.4L TWIN-TURBO V6")
sc("""The problem is machining debris. During production, debris may not have been fully cleared from the engine. That debris can damage the number one main bearing, and the result can be a catastrophic engine failure, according to Motor1. Owners could hear banging or popping noises, and the engine could run rough or stall while driving, as the Associated Press reported at the time of the first recall.""",
   "Toyota Tundra pickup", "DEBRIS → MAIN BEARING → FAILURE")
sc("""Now look at how the recall grew. In twenty twenty-four, Toyota recalled about one hundred two thousand twenty twenty-two and twenty twenty-three Tundras and Lexus LX SUVs, and replaced the engines. In November twenty twenty-five, a second recall covered one hundred twenty-seven thousand vehicles, and added the Lexus GX. Then on May twenty-second, twenty twenty-six, a third recall added forty-four thousand non-hybrid twenty twenty-four Tundras.""",
   "Toyota Tundra 2024", "3 RECALLS: 102K, 127K, 44K")
sc("""Here is the twist. Toyota said the engines in the third recall already had additional debris-removal controls during production. And debris could still remain. That is what makes this one so hard. The fix at the factory was not enough the first time, or the second time. Motor1 reports that engines built after these have an improved number one main bearing.""",
   "Toyota Tundra TRD", "EVEN THE IMPROVED ONES")
sc("""And the second twist is good news. Toyota's remedy has been to replace the entire engine, and Motor1 reports that Toyota had repaired seventy-seven thousand vehicles so far. A truck that already received a brand new engine from Toyota could actually be one of the safest used Tundras you can buy. So the question is not just which year. It is whether this exact truck already got its new engine.""",
   "Toyota Tundra Limited", "77,000 ALREADY REPAIRED")
sc("""So what should you do? If you are looking at a twenty twenty-two to twenty twenty-four Tundra, or a Lexus LX or GX from the same era with this engine, run the VIN on Toyota's recall page and on the federal recall site. If the recall is open, ask when the replacement engine will be installed. If it is done, ask for the paperwork. And notice that the hybrid version, the i-Force Max, was not part of the original recall. Now, the engine from General Motors.""",
   "Toyota Tundra hybrid", "CHECK: WAS THE ENGINE REPLACED?")

sc("""There is one more detail from the first Tundra recall that tells you how seriously Toyota took it. According to the Associated Press, the twenty twenty-four recall covered nearly one hundred thousand Tundra pickups plus about three thousand five hundred Lexus LX six hundred SUVs, and only the regular gas versions, not the hybrids. Toyota never said what replacing all of those engines cost. For a company that sells its trucks on durability, the cost to its reputation may matter even more.""",
   "Lexus LX 600", "TOYOTA NEVER SAID WHAT IT COST")
# ---------- 2. GM 6.2 L87 ----------
sc("""Engine number two is the General Motors six point two liter V8, known as the L eighty-seven. It is the top engine in the Chevrolet Silverado and GMC Sierra fifteen hundred, and it also powers the Tahoe, Suburban, Yukon and Cadillac Escalade. It is the engine many buyers pay extra for. And in twenty twenty-five, GM recalled nearly six hundred thousand vehicles with it in the United States, according to GM Authority.""",
   "Chevrolet Silverado 1500 High Country", "GM 6.2L V8 (L87)")
sc("""The recall, twenty-five V two seven four, covered engines built from March first, twenty twenty-one through May thirty-first, twenty twenty-four. The defect is in the connecting rods and the crankshaft. Contamination can damage the rod bearings, and some crankshafts may have been out of specification or improperly finished. The worst case, according to GM Authority, is a seized engine and a loss of power while driving.""",
   "GMC Sierra 1500 Denali", "BUILT MARCH 2021 – MAY 2024")
sc("""And here is where the two biggest truck makers made very different choices. Toyota replaced whole engines. GM estimated about three percent of its engines would need replacement. For the others, the engines that passed inspection, the remedy was a switch from zero W twenty oil to a thicker zero W forty oil, plus a new oil filter and oil fill cap.""",
   "Chevrolet Tahoe", "THE FIX FOR MOST: THICKER OIL")
sc("""Now the twist. On August twentieth, twenty twenty-six, the federal safety agency opened an engineering analysis, E A twenty-six zero zero five, covering nine hundred ninety-seven thousand, seven hundred forty-three vehicles from twenty twenty-one to twenty twenty-six. GM Authority reported four hundred ninety-nine complaints of engine failure after the recall repair, and one hundred ninety-one more involving engines built outside the original recall dates.""",
   "Chevrolet Silverado 1500 pickup", "690 COMPLAINTS. FEDERAL PROBE.")
sc("""Read that carefully, because it changes how you should shop. Of those four hundred ninety-nine post-repair complaints, four hundred seventy-three were on engines that got the thicker oil, and twenty-six were on engines that had already been replaced. And the one hundred ninety-one reports outside the recall range mean that even a truck the recall does not cover might not be in the clear. These are complaints, not confirmed failures. But they are why regulators are looking.""",
   "GMC Yukon Denali", "EVEN OUTSIDE THE RECALL RANGE")
sc("""So if you want a used GM truck with the six point two, do three things. Confirm the recall was done, and how, oil change or new engine. Ask for every oil change record, because the remedy depends on the right oil. And follow the federal investigation, because if it leads to a new remedy, owners with records will be in the best position. Or choose a different engine, which brings us to engine number three, and it is from the same family.""",
   "Cadillac Escalade", "RECORDS, OIL, INVESTIGATION")

sc("""Let's pause for a moment, because the first two engines already teach the most important lesson in this video. In both cases, the manufacturer found the problem, issued a recall and offered a fix. And in both cases, the story did not end there. Toyota needed three recalls. GM's fix is under investigation. A recall is the start of a story, not the end of it. Now, the next engine has no recall at all.""",
   "Toyota Tundra and Chevrolet Silverado", "A RECALL IS THE START, NOT THE END")
# ---------- 3. GM 5.3 ----------
sc("""Engine number three is the General Motors five point three liter V8, known as the L eighty-four. It is one of the most common engines in America, because it sits in an enormous number of Silverados and Sierras. And it is at the center of a long-running class action lawsuit over its lifters, the small parts that open and close the engine's valves.""",
   "Chevrolet Silverado 1500 5.3", "GM 5.3L V8 (L84)")
sc("""Both the five point three and the six point two use cylinder deactivation, a system that shuts off some cylinders to save fuel. GM called it Active Fuel Management in earlier engines, and Dynamic Fuel Management in newer ones. According to Pickup Truck and SUV Talk, plaintiffs claim lightweight lifters were improperly positioned, causing failures, with symptoms like misfires, ticking, rough running and sometimes stalling.""",
   "GMC Sierra 1500 SLT", "CYLINDER DEACTIVATION LIFTERS")
sc("""Here is the twist that worries owners most. The plaintiffs allege that the replacement parts carry the same design flaw, so a repair may not permanently fix the problem. That is an allegation, not a ruling. GM has not lost this case. But it explains why so many owners talk about lifter failures coming back, and why some buyers pay to have the cylinder deactivation system disabled or removed.""",
   "Chevrolet Silverado Trail Boss", "ALLEGED: THE REPAIR HAS THE SAME FLAW")
sc("""Where does the case stand? It has been consolidated in federal court in the Eastern District of Michigan since December twenty twenty-one. In March twenty twenty-six, Judge Laurie Michelson refused the plaintiffs' request to split it into two separate cases, one for each system, according to Pickup Truck and SUV Talk. So it continues as one case. No verdict on the merits has been reached.""",
   "Chevrolet Silverado 1500 LTZ", "COURT: STILL ONE CASE, NO VERDICT")
sc("""So what does a used buyer do? Listen to a cold start. A lifter problem often shows up as ticking or a misfire, especially when the engine is cold. Ask whether any lifters or camshaft work has been done, and get the invoice. And if the truck has high mileage and no service records, factor the cost of a possible lifter job into your price. The five point three is not a guaranteed failure. But it is a known risk with a court case attached.""",
   "Chevrolet Silverado pickup truck", "LISTEN TO A COLD START")

sc("""The lawsuit has had its own twists. Pickup Truck and SUV Talk reports that a January twenty twenty-three ruling noted the claims appeared to describe three separate part failures, that seventeen claims were temporarily sent to arbitration, and that some plaintiffs and attorneys left the case. GM opposed splitting the case, arguing it would mean duplicate expert work and potentially two trials. Years after it began, owners are still waiting for an answer.""",
   "GMC Sierra 1500 AT4", "YEARS IN COURT, NO ANSWER YET")
# ---------- 4. FORD 6.7 CP4 ----------
sc("""Engine number four is the Ford six point seven liter Power Stroke diesel, the engine in millions of Super Duty trucks. It is a powerful, respected engine. But one part has become its weak point, the Bosch C P four high-pressure fuel pump. And in October twenty twenty-six, that part became the subject of a class action that a federal judge partly certified.""",
   "Ford F-250 Super Duty diesel", "FORD 6.7L POWER STROKE")
sc("""According to Pickup Truck and SUV Talk, the lawsuit, Droesser versus Ford, alleges that the pump can send metal shavings through the fuel system, which can lead to catastrophic engine failure. The case centers on lubrication. The C P four relies on the fuel itself to lubricate it, and American ultra-low-sulfur diesel has lower lubricity than European diesel. Plaintiffs allege repairs costing nine thousand dollars or more.""",
   "Ford F-350 Super Duty", "ALLEGED: METAL SHAVINGS, $9,000+")
sc("""The judge certified classes in five states, California, Louisiana, Ohio, Pennsylvania and South Carolina, covering twenty eleven to twenty twenty-three trucks with this engine, according to the report. The order does not decide whether Ford is liable. And Ford argues that some failures came from owners who did not change dirty fuel filters, used too much diesel exhaust fluid, poor-quality fuel, or additives.""",
   "Ford F-450 Super Duty", "5 STATES CERTIFIED")
sc("""Here is the twist. There has been a recall on this pump, but not for the reason in the lawsuit. In December twenty twenty-four, Ford recalled two hundred ninety-five thousand, four hundred forty-nine twenty twenty to twenty twenty-two Super Duty, F-six fifty and F-seven fifty trucks, according to TFL Truck. The reason was aged biodiesel deposits that could build up inside the pump and cause a loss of power.""",
   "Ford Super Duty truck", "RECALL: 295,449 TRUCKS")
sc("""And the fix was not a new pump. It was software. Dealers reflashed the engine computer to increase cooling around the pump. TFL Truck noted it was unclear whether this would solve the problem long-term. And according to Pickup Truck and SUV Talk, a follow-up recall, twenty-six V one five eight, came in twenty twenty-six. So a used Super Duty diesel may have had two pump-related software updates, and still carry the original pump.""",
   "Ford F-250 pickup", "THE FIX: SOFTWARE, TWICE")
sc("""If you are shopping for a used six point seven, check the recall status, ask for fuel filter change records, and ask whether the pump has ever been replaced. Diesel owners talk about aftermarket protection kits, but those are not part of any recall, so treat them as your own choice. A diesel with clean records and documented filter changes is a very different truck from one with none.""",
   "Ford F-350 dually", "FUEL FILTER RECORDS MATTER")

sc("""The recall numbers break down like this, according to TFL Truck. One hundred forty-nine thousand, one hundred eighty twenty twenty Super Duty trucks. One hundred twenty thousand, five hundred ninety-seven from twenty twenty-one. Sixteen thousand, three hundred sixty-one from twenty twenty-two. Plus about nine thousand F-six fifty and F-seven fifty work trucks. And in twenty twenty-one, before the recall, Ford had blamed fuel that sat in trucks during the COVID shutdowns.""",
   "Ford F-650", "2020 MODEL YEAR: 149,180 TRUCKS")
sc("""And there is one more pump recall worth knowing. According to Motor1, in March twenty twenty-six, Ford recalled seven thousand, one hundred five twenty twenty to twenty twenty-two Super Duty trucks, plus the twenty twenty-two F-seven fifty, because the high-pressure fuel pump may fail. A failed pump can stall the engine. So the high-pressure fuel pump on these trucks has now been the subject of a recall, a follow-up, another recall, and a class action. That is a lot of attention on one part.""",
   "Ford F-750", "ANOTHER PUMP RECALL IN 2026")
# ---------- 5. FORD 3.5 ECOBOOST ----------
sc("""Engine number five is the Ford three point five liter EcoBoost V6, the twin-turbo engine that helped the F-150 become a towing machine. The problem here is the cam phasers, the parts that adjust the timing of the camshafts. According to SlashGear, owners point to the twenty seventeen to twenty twenty trucks as the main years for cam phaser failures, with some having them replaced more than once.""",
   "Ford F-150 EcoBoost", "FORD 3.5L ECOBOOST 2017-2020")
sc("""The usual sign is a rattle at startup, a few seconds of noise that sounds like a diesel. Ford extended warranty coverage for cam phaser noise on these trucks, but SlashGear reports that coverage ran until January first, twenty twenty-three. Ford has since updated the design. But here is the twist. NHTSA records show no recall for the cam phaser issue, according to SlashGear.""",
   "Ford F-150 Raptor", "NO RECALL. EXTENSION ENDED.")
sc("""Think about what that means. With a recall, the fix is free forever. With an extended warranty that has expired, the cost is yours. TorqueNews cites out-of-warranty cam phaser repairs of four thousand to six thousand dollars. That is why some writers now tell twenty twenty-six F-150 shoppers to choose the five point oh V8 instead, though that is advice, not data.""",
   "Ford F-150 XLT", "$4,000–6,000 OUT OF WARRANTY")
sc("""And to be fair, not every three point five is a problem. SlashGear notes that owners consider twenty fifteen and twenty sixteen among the most reliable years, while the earliest years, twenty eleven to twenty fourteen, are linked to timing chain problems. So with this engine, the year matters as much as the model. If you buy a twenty seventeen to twenty twenty, listen to a cold start, and ask whether the phasers were replaced with the updated parts.""",
   "Ford F-150 2016", "2015-2016: OWNER FAVORITES")

sc("""Here is why the three point five is still so popular despite all this. According to TorqueNews, it makes five hundred pound-feet of torque, and it is paired with a ten-speed transmission. For towing, that torque is the whole point. So the trade-off for buyers is real. More pulling power, with a part that has a documented history. The five point oh V8 makes less torque, but it does not have turbochargers or the same phaser story.""",
   "Ford F-150 towing trailer", "500 LB-FT VS PEACE OF MIND")
# ---------- BONUS: ECODIESEL ----------
sc("""And now the bonus engine, the three liter EcoDiesel V6 in the twenty fourteen to twenty nineteen Ram fifteen hundred. In October twenty nineteen, a recall covered about one hundred eight thousand of these trucks because of the exhaust gas recirculation cooler, according to CarComplaints. Owners later alleged in court that failed coolers could cause fires.""",
   "Ram 1500 EcoDiesel", "BONUS: RAM 3.0 ECODIESEL")
sc("""Here is the twist. Stellantis says every truck was repaired for free under the recall. But a class action continued, and in January twenty twenty-six, a settlement got preliminary approval. It includes a five-year warranty extension on the replacement cooler, reimbursement for towing, rental cars and coolant, and up to three thousand dollars for owners whose truck caught fire from a failed cooler. The company denies any wrongdoing.""",
   "Ram 1500 pickup", "SETTLEMENT: UP TO $3,000 FOR FIRES")
sc("""So if you are looking at a twenty fourteen to twenty nineteen EcoDiesel, find out when the cooler was replaced, because the warranty extension counts from that date. That single piece of paper can be worth a lot. And that takes us to the pattern behind every engine in this video.""",
   "Ram 1500 Laramie", "THE DATE OF THE REPAIR MATTERS")

sc("""The settlement details, as reported by CarComplaints, show how these cases usually end. Twenty-six named plaintiffs, including a construction company, were set to receive five thousand dollars each. The lawyers were set to receive two point four five million dollars. And the covered trucks were those built between June twelfth, twenty thirteen, and October twenty-third, twenty nineteen. For an ordinary owner, the most valuable part is the extended warranty, not the cash.""",
   "Ram 1500 Big Horn", "26 PLAINTIFFS, $2.45M FOR LAWYERS")
# ---------- CLOSE ----------
sc("""Look at the five engines together. Two were built by GM, two by Ford, one by Toyota. Three are V8 or diesel engines that buyers pay extra for. And the problems are rarely the big obvious parts. It is debris left in machining, a bearing, a lifter, a fuel pump, a cam phaser. Small parts, deep inside, that a test drive will almost never reveal.""",
   "Ford F-150 Chevrolet Silverado Toyota Tundra", "SMALL PARTS. BIG BILLS.")
sc("""And here is the final twist. In almost every case, the most important information is not the engine name. It is the paperwork. A Tundra with a factory replacement engine. A Silverado with documented oil changes. A Super Duty with fuel filter records. An EcoDiesel with a dated cooler replacement. The same engine can be the riskiest truck on the lot, or one of the safest, depending on what was done to it.""",
   "Toyota Tundra 2023", "THE PAPERWORK IS THE ENGINE")
sc("""So here is your checklist for any used truck in twenty twenty-seven. One, run the VIN for open recalls on the federal site and the brand's page. Two, ask for every service invoice, especially oil and fuel filter changes. Three, listen to a cold start, ideally when the engine has sat overnight. Four, pay for an independent inspection before you sign. It costs far less than a single engine repair.""",
   "Chevrolet Silverado 1500", "4 CHECKS BEFORE YOU SIGN")
sc("""We put all of this into the Twenty Twenty-Seven Truck Buyer's Guide, including the engine years to watch and the exact questions to ask the seller. The link is in the description and in the pinned comment. If this video helped, subscribe, because next we look at which truck brand is the most reliable, according to the data, and the answer may surprise you. Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One of these engines": "Intro", "Engine number one": "1. Toyota 3.4L twin-turbo V6", "Engine number two": "2. GM 6.2L V8 (L87)",
      "Engine number three": "3. GM 5.3L V8 (L84)", "Engine number four": "4. Ford 6.7L Power Stroke (CP4 pump)",
      "Engine number five": "5. Ford 3.5L EcoBoost (2017-2020)", "And now the bonus": "Bonus: Ram 3.0 EcoDiesel",
      "Look at the five engines": "Checklist before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video23", "length_scale": 1.4,
  "title": "5 Truck Engines to Avoid Before 2027 (Even Toyota Made the List)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
