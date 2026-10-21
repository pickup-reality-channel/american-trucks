import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""About two point four five million cars on American roads may have had their odometers rolled back, according to Carfax, up fourteen percent in one year. Another half a million water-damaged vehicles were already on the road before this year's floods. And about one in five vehicles still has an unfixed recall. Here are five warning signs to check before you buy a used truck in twenty twenty-seven.""",
   "used pickup trucks dealer lot", "5 WARNING SIGNS")

# ---------- COLD OPEN ----------
sc("""Used trucks are where a lot of buyers are going right now, because new ones are so expensive. And that is exactly why the used truck market is where the biggest mistakes happen. A truck can look clean, drive fine on a short test drive, and still be hiding a problem that costs thousands, or one that makes it unsafe. Most of these problems are not hidden by the truck. They are hidden by paperwork, or by the lack of it.""",
   "Ford F-150 used truck", "THE PROBLEM IS OFTEN IN THE PAPERWORK")
sc("""So in this video, we go through five warning signs that show up again and again in data from Carfax, the federal safety agency, recalls and investigations from twenty twenty-five and twenty twenty-six. For each one, you will hear how common it is, what it can cost you, and exactly how to check, most of the time for free, in a few minutes.""",
   "Chevrolet Silverado 1500 used", "HOW COMMON, HOW COSTLY, HOW TO CHECK")
sc("""And there is a twist in each one. Some of these warning signs are getting worse because trucks got more modern, not older. Some can be spotted with your own eyes and nose. And one of them is so common that you have to assume it is there until you prove it is not. Every figure comes from a published source, listed in the description. Let's start with the number on the dashboard.""",
   "Ram 1500 used pickup", "SOME ARE GETTING WORSE")

# ---------- 1. ODOMETER ----------
sc("""Warning sign number one is mileage that does not add up. On December sixteenth, twenty twenty-five, Carfax said its data suggests about two point four five million vehicles on the road have had their odometers rolled back. That was a fourteen percent increase from the year before, compared with a four percent increase the year before that. The problem is not fading. It is speeding up.""",
   "pickup truck dashboard odometer", "2.45 MILLION ROLLBACKS (+14%)")
sc("""And the cost is real. According to Carfax, vehicles with a rollback lost an average of about three thousand three hundred dollars in value. That is the money you overpay on day one. But the bigger cost comes later, because a truck with far more miles than it shows will need expensive maintenance sooner than you planned, from timing parts to transmissions.""",
   "Ford F-150 instrument cluster", "AVERAGE LOSS: ~$3,300")
sc("""Here is the twist. Odometer fraud got easier because trucks got more modern. Carfax's Faisal Hasan said, quote, as modern vehicles have transitioned from mechanical to digital odometers, tampering has unfortunately become more common. Old mechanical odometers had to be physically taken apart. Digital ones can be changed with cheap electronic tools that are widely available, according to Carfax.""",
   "Chevrolet Silverado digital dashboard", "DIGITAL MADE IT EASIER")
sc("""And it is spreading fastest in truck country. Carfax listed the biggest year-over-year increases in suspected rollbacks. Montana, up thirty-three percent. Tennessee, up thirty percent. Arkansas, twenty-eight. Oklahoma, twenty-five. Kansas, twenty-four. New Jersey, twenty-one, and Florida, twenty. Several of those are states where pickups are a way of life, and where a truck with low miles commands a premium.""",
   "Ford Super Duty ranch Montana", "MONTANA +33%, TENNESSEE +30%")
sc("""So how do you check? First, compare the mileage on the dash with every record you can find, title, service invoices, inspection reports and a vehicle history report. Mileage should only go up, and at a believable pace. Second, Carfax offers a free odometer check by VIN. Third, look at wear on the pedals, the steering wheel, the driver's seat bolster and the floor mat. A truck that shows thirty thousand miles should not look like it has worked for ten years.""",
   "pickup truck interior pedals", "CHECK: RECORDS, VIN, WEAR")
sc("""And fourth, Carfax recommends having a trusted mechanic inspect the vehicle, because a mechanic can often tell when it is older than the odometer says. There is one more good sign here. Carfax notes that mileage is now recorded more often, at oil changes, inspections and service visits, which makes rollbacks easier to catch, if you actually look. Now warning sign number two, and this one you can sometimes smell.""",
   "mechanic inspecting truck", "MILEAGE IS RECORDED MORE OFTEN")

sc("""And the people it happens to usually find out too late. In the Carfax announcement, a buyer from Valencia, California, Seven Beverly, said about the rollback on their vehicle, quote, it's definitely something that I wish I knew before buying. That is the theme of this whole video. Almost every warning sign here can be checked before you pay. After you pay, it becomes your problem.""",
   "used truck buyer", "\"I WISH I KNEW BEFORE BUYING\"")
# ---------- 2. FLOOD DAMAGE ----------
sc("""Warning sign number two is flood damage. On October thirteenth, twenty twenty-six, Carfax estimated that about forty-eight thousand vehicles may have been damaged by flooding from storms earlier in the year, between April and August, in states including Michigan, Wisconsin, Mississippi, Indiana and West Virginia, according to Carrier Management.""",
   "flooded pickup truck", "2026: ~48,000 FLOODED VEHICLES")
sc("""And those are only the new ones. More than half a million water-damaged vehicles were already on U.S. roads before these storms, according to Carfax. Half a million. Some were repaired properly and disclosed. Many were simply cleaned up and sold. Carfax's chief product officer, Paul Nadjarian, said, quote, floodwater can leave behind damage that isn't always obvious when a vehicle is cleaned up and put back on the market.""",
   "flood damaged vehicles lot", "500,000+ ALREADY ON THE ROAD")
sc("""Here is the twist. A flooded truck does not stay where it flooded. Law enforcement warns that these vehicles can enter the used market far from where the flooding happened. A truck that went underwater in Mississippi can be sold, clean and shiny, in Arizona months later. So the question is not whether your area flooded. It is where the truck has been.""",
   "pickup truck on transport trailer", "FLOOD TRUCKS TRAVEL")
sc("""Why is flood damage so bad for a modern truck? Because a modern truck is full of electronics, modules, wiring and sensors, many of them low in the body or under the seats. Water and silt can cause corrosion that takes months to show up. A truck can seem fine on the test drive and start having electrical faults later, in the cameras, the screens, the trailer module, the very systems we have covered in earlier videos.""",
   "pickup truck wiring under dashboard", "ELECTRONICS + WATER = LATER FAILURES")
sc("""So what do you check? Carfax lists the warning signs. A musty or moldy smell. Damp carpet. Upholstery or carpet that looks loose, new, stained or mismatched. Rust near the doors, under the dashboard, on the pedals, or on the hood latch. Mud or silt in the glove box, under the seats, or in odd places. Brittle wiring under the dashboard. And fog or moisture inside the headlights, taillights or the instrument panel.""",
   "pickup truck carpet seat inspection", "SMELL, CARPET, RUST, SILT, FOG")
sc("""And use the free tools. Carfax offers a free flood check by VIN. A history report may show a flood or salvage title. But here is the honest limit. If a truck was flooded and never reported to insurance, no database will show it. That is why your nose and eyes still matter, and why a professional inspection is worth the money. Now, warning sign number three, and it is the most common one on this list.""",
   "Ford F-150 headlight moisture", "FREE FLOOD CHECK, BUT USE YOUR NOSE")

sc("""And notice the twist in where the twenty twenty-six flooding happened. Not only on the hurricane coast. Michigan, Wisconsin, Indiana and West Virginia are not places most buyers associate with flood cars. Storms and flash floods can put vehicles underwater anywhere. That is why a flood check is worth doing on every used truck, no matter which state it is coming from.""",
   "flooded road Midwest", "FLOODS ARE NOT ONLY COASTAL")
sc("""Let's pause and count what we have so far. Two warning signs, and both can be checked with a VIN and a few minutes, for free, before you ever see the truck. If more buyers did only that, millions of rolled-back and flooded vehicles would be much harder to sell. Now the next sign is so common that you should assume it is there until you prove it is not.""",
   "Chevrolet Silverado used truck", "2 SIGNS, BOTH FREE TO CHECK")
# ---------- 3. OPEN RECALLS ----------
sc("""Warning sign number three is an unfixed recall. And this one is everywhere. In January twenty twenty-five, Carfax estimated that about one in five vehicles on U.S. roads had an unresolved recall, about fifty-eight point one million vehicles, and that more than fourteen million had two or more, as reported by FOX twenty-six Houston. In March twenty twenty-six, Carfax said about one in five vehicles still has an unfixed recall.""",
   "Chevrolet Silverado 1500 2020", "1 IN 5 VEHICLES: UNFIXED RECALL")
sc("""And the camera recalls we covered in earlier videos made it worse. In May twenty twenty-six, Carfax said nearly seven million U.S. vehicles had an unfixed recall tied to the backup camera system, and that camera recalls had risen by more than one point five million since the start of the year. Texas led with about six hundred ninety-six thousand, then California, Florida and Michigan.""",
   "Ford F-150 rear camera", "7 MILLION UNFIXED CAMERA RECALLS")
sc("""Here is the twist. Open recalls are worse for pickups than you might think. In Canada, Carfax Canada reported that crew cab pickups were among the top three vehicle types for reported recalls in its twenty twenty-five data. And the biggest recalls of twenty twenty-five and twenty twenty-six were truck recalls, four point four million Fords for trailer brakes, one and a half million Ram fifteen hundreds for rear seat belt anchors, and one point four million older F-150s for unexpected downshifts.""",
   "Ram 1500 crew cab", "CREW CAB PICKUPS: TOP 3 FOR RECALLS")
sc("""The good news is that this warning sign is the easiest to fix. Recall repairs are free. So an open recall is not a reason to walk away from a truck. It is a reason to know before you buy, and to get it fixed. Carfax Canada's president, Shawn Vording, put it well. A recall or an accident does not automatically make a used vehicle a bad choice. What matters is that buyers know about it.""",
   "Ford Super Duty dealer service", "FREE TO FIX, IF YOU KNOW")
sc("""So how do you check? Go to the federal safety website, NHTSA dot gov slash recalls, enter the seventeen-character VIN, and search. It takes a minute. Then check the manufacturer's own recall page too. If there is a recall with a do not drive warning, like the twenty twenty-six Maverick control arm recall we covered, do not drive the truck home until it is fixed. And if a seller says the recall was done, ask for the invoice.""",
   "Ford Maverick", "NHTSA.GOV/RECALLS + THE INVOICE")

sc("""And the tools to check are better than ever. In March twenty twenty-six, Carfax said its free recall search service had checked U.S. vehicles more than ten billion times, and that more than thirty million of the open recalls it found were repaired. Eight state motor vehicle departments use it, including California, New York, Ohio, Arizona and Texas. When owners are told, many do get the fix. The problem is the trucks nobody checks.""",
   "Ram 2500 Heavy Duty", "10 BILLION CHECKS, 30 MILLION FIXED")
# ---------- 4. HARD USE ----------
sc("""Warning sign number four is a hard-use history with no records. Trucks are tools. Many used trucks have spent years towing, plowing, carrying heavy loads, or working in a fleet. That is not automatically bad. Heavy-duty trucks are built for it. But hard use changes which problems you should look for, and without records you have no idea what has already been done.""",
   "Ford F-250 work truck", "HARD USE + NO RECORDS")
sc("""Look at how many of the recalls and problems we have covered are tied to towing and heavy use. Ford's recall of about one hundred three thousand F-150s for rear axle hub bolts that can snap was limited to trucks with the heaviest-duty rear axle, according to RV Travel. The Super Duty's low-pressure fuel pump problem was more likely with low fuel and hot weather. And trailer module recalls only matter if the truck tows. The work a truck has done shapes what breaks.""",
   "Ford F-150 heavy duty towing", "TOWING SHAPES WHAT BREAKS")
sc("""Here is the twist. Records matter even more than mileage. In the federal investigation of GM's six point two V8, owners who can prove the right oil was used are in the best position. In the Ford diesel fuel pump lawsuit, Ford argued some failures came from owners who did not change fuel filters, according to Pickup Truck and SUV Talk. A truck with high miles and a thick folder of receipts can be a safer buy than a low-mile truck with nothing.""",
   "Chevrolet Silverado 1500 service records", "RECEIPTS BEAT LOW MILES")
sc("""So how do you spot hard use? Look at the hitch receiver for heavy wear, and check whether a trailer brake controller was installed. Look under the truck for bent or scraped parts. Check the bed for deep damage. Look for a lift kit or oversized tires, which change the front-end geometry and can make problems like the death wobble more likely on solid-axle trucks. Then ask for the service history, and if there is none, price that risk into your offer.""",
   "pickup truck hitch receiver", "HITCH, BED, UNDERBODY, LIFT")

sc("""And to be fair to work trucks, hard use is not the same as abuse. iSeeCars found that heavy-duty trucks last up to twice as long as light-duty versions, according to Work Truck Online. A fleet truck that was serviced on schedule by a business can be in better shape than a weekend truck that was ignored. The warning sign is not that the truck worked. It is that nobody can show you how it was cared for.""",
   "Ford F-350 fleet truck", "WORKED IS NOT THE SAME AS ABUSED")
# ---------- 5. THE ENGINE AND YEAR ----------
sc("""Warning sign number five is a specific engine and model year with a known problem, combined with a cold-start test the seller does not want you to do. In earlier videos we covered the documented cases. Toyota's twin-turbo V6 in twenty twenty-two to twenty twenty-four Tundras, with three recalls for machining debris. GM's six point two in engines built from March twenty twenty-one to May twenty twenty-four, now under federal investigation.""",
   "Toyota Tundra 2022", "KNOWN ENGINES, KNOWN YEARS")
sc("""Ford's three point five EcoBoost cam phaser issues on twenty seventeen to twenty twenty trucks, with no recall and an extended warranty that ended in twenty twenty-three, according to SlashGear. GM's eight-speed transmission shudder on twenty fifteen to twenty nineteen trucks, and its ten-speed valve body recall. And the Ram EcoDiesel's EGR cooler recall on twenty fourteen to twenty nineteen trucks. None of these mean every truck is bad. They mean you know exactly what to check.""",
   "Ford F-150 EcoBoost", "PHASERS, SHUDDER, VALVE BODIES, EGR")
sc("""Here is the twist. Many of these problems show up most clearly on a cold start. The EcoBoost cam phaser rattle is a few seconds of noise at startup. A lifter tick on a GM V8 is often loudest cold. A transmission that engages harshly cold may feel normal once warm. So if you arrive for a test drive and the engine is already warm, ask why. A seller who warmed up the truck before you got there may be hiding exactly what you came to hear.""",
   "pickup truck cold start morning", "A WARM ENGINE CAN HIDE THINGS")
sc("""So how do you check? Ask the seller not to start the truck before you arrive. Put your hand on the hood when you get there. Start it yourself and listen for the first ten seconds. Then drive it, and feel every shift from park to drive and below twenty miles per hour. If the truck has one of the engines we mentioned, ask whether the recall or warranty work was done, and ask for the paperwork.""",
   "Chevrolet Silverado 1500 engine bay", "HAND ON THE HOOD")

sc("""And heavy-duty buyers have one more thing to test. According to Pickup Truck and SUV Talk's report on Consumer Reports data, some Ram heavy-duty owners reported software problems that left trucks limited to about fifteen miles per hour, or made tow haul mode unavailable. So on any heavy-duty test drive, switch into tow haul mode and make sure it works, and check the dash for any warning messages before you leave the lot.""",
   "Ram 3500 Heavy Duty", "TEST TOW/HAUL MODE")
# ---------- BONUS ----------
sc("""And here is a bonus warning sign, accident history. In its twenty twenty-five data, Carfax Canada said one in four vehicles searched on its reports had damage or accident history. An accident does not make a truck a bad buy. But a hidden one, or one repaired badly, can affect safety, especially on a truck whose frame and structure carry heavy loads. Look for paint that does not match, uneven gaps between panels, and overspray on rubber trim.""",
   "pickup truck body panel gap", "BONUS: 1 IN 4 HAD DAMAGE HISTORY")
sc("""And remember the safety ratings we covered in the last video. A used truck's crash protection depends on its structure being repaired correctly after any accident. If a history report shows structural damage or airbag deployment, that is a reason to get a professional inspection, not just a test drive. The cost of an inspection is tiny compared with the cost of finding out later.""",
   "Ram 1500 front end", "STRUCTURAL DAMAGE? GET IT INSPECTED")

# ---------- CLOSE ----------
sc("""So look at all five warning signs together. Mileage that does not add up. Signs of water. An open recall. Hard use with no records. And a problem engine or transmission that sounds wrong when cold. Notice that three of them can be checked online for free, using only the VIN. The other two need your eyes, your ears, and a mechanic. Every one of them can be checked before you hand over any money.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "3 ONLINE, 2 IN PERSON")
sc("""And here is the final twist. None of these warning signs automatically means walk away. A truck with an open recall can be fixed for free. A truck with high miles and great records can be a great buy. Even a truck with an accident in its history can be fine if it was repaired properly. The danger is not the problem. The danger is not knowing about it, and paying as if it was not there.""",
   "Toyota Tacoma used", "THE DANGER IS NOT KNOWING")
sc("""So here is your used truck checklist for twenty twenty-seven. One, run the VIN on the federal recall site and get a vehicle history report. Two, run the free flood and odometer checks. Three, compare the mileage with every record. Four, do the smell, carpet, rust and silt check. Five, start the engine cold yourself. Six, look at the hitch, bed and underbody. And seven, pay for an independent inspection before you sign.""",
   "used pickup truck inspection", "THE 7-STEP USED TRUCK CHECK")
sc("""We put this checklist, plus the engines and years to watch, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. If this helped, subscribe, because next we look at the most stolen trucks in America, and why thieves love them. And tell us in the comments, which warning sign have you run into? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"About two point four five million": "Intro", "Warning sign number one": "1. Mileage that does not add up", "Warning sign number two": "2. Flood damage",
      "Warning sign number three": "3. Unfixed recalls", "Warning sign number four": "4. Hard use with no records",
      "Warning sign number five": "5. Known engines and the cold start", "And here is a bonus": "Bonus: accident history",
      "So look at all five": "Used truck checklist for 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video29", "length_scale": 1.45,
  "title": "5 Warning Signs Before You Buy a Used Truck in 2027 (2.45 Million Odometers Rolled Back)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
