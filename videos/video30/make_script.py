import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One heavy-duty pickup is stolen about ten times more often than the average vehicle in America. The Chevrolet Silverado was the fourth most stolen vehicle in the country in twenty twenty-five. And the Ford F-150 was number one for something thieves can take in a couple of minutes from underneath. These are the most stolen trucks in America, and why thieves want them.""",
   "GMC Sierra 2500HD", "10X THE AVERAGE THEFT RATE")

# ---------- COLD OPEN ----------
sc("""Here is the good news first. Vehicle theft in America fell sharply in twenty twenty-five. According to the National Insurance Crime Bureau, known as NICB, thefts dropped twenty-three point two percent, from eight hundred fifty thousand, seven hundred eight in twenty twenty-four to six hundred fifty-nine thousand, eight hundred eighty in twenty twenty-five. That is one hundred ninety thousand fewer stolen vehicles in a single year.""",
   "Chevrolet Silverado 1500 parked", "2025 THEFTS: -23.2%")
sc("""To put that in perspective, NICB called it the lowest total in several decades. And it came after a seventeen percent drop in twenty twenty-four, which at the time was the largest decline in forty years. So two record years in a row. Glawe said prevention efforts are, quote, having a major impact on vehicle thefts nationwide.""",
   "Ford F-150 Lightning parked", "LOWEST IN DECADES")
sc("""And yet, even at that record low, NICB says a vehicle was still stolen in America roughly every forty-eight seconds. By the time you finish this video, around twenty-five more vehicles will have been taken somewhere in the country. Some of them will be pickups.""",
   "pickup truck parking lot night", "ONE THEFT EVERY 48 SECONDS")
sc("""But nearly six hundred sixty thousand vehicles were still stolen. NICB's president, David Glawe, said, quote, the fight against vehicle theft is not over. And according to the federal safety agency, the thefts in twenty twenty-four caused losses of about eight billion dollars, as reported by the Associated Press. And pickups sit right in the middle of this story, for reasons most owners never think about.""",
   "Ford F-150 parked street", "STILL ~660,000 STOLEN")
sc("""In this video, we look at the trucks thieves target most, using two very different kinds of data. One counts how many of each model were stolen. The other measures how likely each model is to be stolen. They give completely different answers, and that is the first twist. Then we look at the parts thieves take, the cities where it happens most, and what actually works to stop it.""",
   "Ram 1500 parked", "TWO KINDS OF DATA")
sc("""Every number comes from a published source, mostly NICB, the Highway Loss Data Institute, Carfax and local police reports, listed in the description. And if you are buying a used truck, stay to the end, because there is a way to end up owning a stolen truck without knowing it. Let's start with the raw numbers.""",
   "Chevrolet Silverado 2500HD", "EVERY NUMBER IS SOURCED")

# ---------- 1. NICB COUNTS ----------
sc("""According to NICB's list of the most stolen vehicles of twenty twenty-five, reported by AutoGuide, the top three were all cars. The Hyundai Elantra with twenty-one thousand, seven hundred thirty-two thefts. The Honda Accord with seventeen thousand, seven hundred ninety-seven. And the Hyundai Sonata with seventeen thousand, six hundred eighty-seven. Then came the first truck.""",
   "Hyundai Elantra", "TOP 3: ALL CARS")
sc("""Number four was the Chevrolet Silverado, with sixteen thousand, seven hundred sixty-four thefts. And it has been near the top for years. It was fourth in twenty twenty-three, with twenty-three thousand, seven hundred twenty-one thefts, and third in twenty twenty-four, with twenty-one thousand, six hundred sixty-six, according to an analysis of NICB data by AmericanTrucks. So even as theft fell, the Silverado stayed one of the most stolen vehicles in America.""",
   "Chevrolet Silverado 1500 2022", "#4: SILVERADO, 16,764")
sc("""The Ford F-150 was number seven, with ten thousand, one hundred two thefts. The rest of the top ten were the Honda Civic, the Kia Optima, the Toyota Camry, the Honda CR-V and the Nissan Altima. So two pickups made the national top ten, the Silverado and the F-150, and both of them are the two best-selling trucks in America.""",
   "Ford F-150 pickup truck", "#7: F-150, 10,102")
sc("""And notice who is at the top. Hyundai and Kia models were hit by a theft wave in recent years, after videos showed how to steal certain models that lacked engine immobilizers. According to NICB, Hyundai and Kia thefts have now fallen for three straight years, thanks to software updates and theft-prevention measures. Their share fell from twenty-one percent of all thefts in twenty twenty-three to sixteen percent in twenty twenty-four, and fourteen percent in twenty twenty-five.""",
   "Kia Optima", "HYUNDAI/KIA: 21% → 14%")
sc("""That matters for truck owners. As thieves lose the easiest targets, the remaining top ten is filled with the vehicles that are simply everywhere, and pickups like the Silverado and F-150 are some of the most common, most valuable vehicles on American roads. A truck does not need a design flaw to be a target. It only needs to be popular and worth a lot.""",
   "Chevrolet Silverado 1500 2024", "POPULAR + VALUABLE = TARGET")
sc("""Here is the twist. Those counts mostly reflect how many of each vehicle are on the road. Ford sells hundreds of thousands of F-Series trucks every year, and the F-Series has been America's best-selling pickup for decades. When there are millions of a model on the road, even a low theft rate produces a big number. So the count tells you how often a model is stolen in total. It does not tell you how likely your truck is to be stolen. For that, you need a different study.""",
   "Ford F-150 parking lot", "COUNT ≠ RISK")

# ---------- 2. HLDI RATES ----------
sc("""The Highway Loss Data Institute, the research arm that works with IIHS, measures theft risk differently. It looks at insurance claims for whole-vehicle theft, compared with how many of each model are insured, and scores it so that one hundred is the average. In its study of twenty twenty-two to twenty twenty-four models, as cited by AmericanTrucks, pickup trucks as a group scored two hundred five. That is about double the average. SUVs scored fifty-eight.""",
   "GMC Sierra 1500", "PICKUPS: 205 (AVERAGE = 100)")
sc("""And one truck stood out. According to GM Authority's report on the study, the most stolen GMC Sierra was the twenty-five hundred crew cab four-wheel drive, with a score of one thousand twenty-three. That is roughly ten times the national average. The Sierra thirty-five hundred crew cab four-wheel drive came next among Sierras. And four of the top twenty most stolen entries were Sierra variants.""",
   "GMC Sierra 2500HD Denali", "SIERRA 2500 CREW 4WD: 1,023")
sc("""Other pickups appeared too. The Ram fifteen hundred scored five hundred twenty-four, about five times the average. The Ram thirty-five hundred scored three hundred eighty-seven. The Jeep Gladiator, two hundred sixty-four. A couple of Chevrolet Silverado variants were on the list as well, though less often than the Sierra, even though the two trucks are mechanically almost identical.""",
   "Ram 1500 Laramie", "RAM 1500: 524")
sc("""Now the twist. The Ford F-Series was absent from the HLDI top twenty, according to GM Authority. So the F-150 is among the most stolen vehicles by count, but not among the highest by rate. And the GMC Sierra, which sells far fewer trucks than the F-Series, has the highest theft risk per truck. If you own a heavy-duty crew cab Sierra, your truck is a far more attractive target than an F-150, even though the F-150 shows up more often in the headlines.""",
   "GMC Sierra 3500HD", "SIERRA: HIGHEST RISK PER TRUCK")
sc("""Why the Sierra over the Silverado, when they share almost everything? The study does not say, so we will not guess at a single reason. But the Sierra is often sold in higher trims and at higher prices, and heavy-duty crew cab four-wheel-drive trucks are among the most expensive pickups on the road. Expensive, desirable trucks are worth more to resell, whole or in parts.""",
   "GMC Sierra Denali", "EXPENSIVE TRUCKS, BIGGER TARGETS")

# ---------- 3. WHY TRUCKS ----------
sc("""So why are pickups such good targets? According to Associated Press reporting on Ford's anti-theft work in December twenty twenty-five, pickups are attractive partly because of the valuable tools and products often stored in their beds. A contractor's truck can carry thousands of dollars of equipment. Steal the truck, and you get everything in it.""",
   "Ford F-250 work truck tools", "THE TOOLS IN THE BED")
sc("""And the thieves have changed. The same reporting says most thefts are now professional. Vehicles are often stolen for resale, with their identification numbers changed. Some thieves break into a vehicle and reprogram its computer to accept a different key. And some stolen vehicles are used in other crimes, like carjackings and smash-and-grab robberies.""",
   "pickup truck at night", "PROFESSIONAL THIEVES, ALTERED VINs")
sc("""Here is the twist. Many thefts still happen the easy way. The reporting notes that thieves look for easy targets, such as key fobs left inside vehicles. For all the talk of high-tech theft, a truck left with the fob in the cup holder is still the simplest target in America. And trucks are often left running or unlocked at job sites, gas stations and driveways.""",
   "Chevrolet Silverado key fob", "THE EASIEST THEFT: A FOB LEFT INSIDE")

# ---------- 4. PARTS ----------
sc("""But many truck thieves do not want the truck at all. They want the parts. In June twenty twenty-six, Carfax estimated that more than one hundred thirty-seven thousand catalytic converters were stolen in twenty twenty-five, with thousands more early in twenty twenty-six. And the number one vehicle targeted was the Ford F-150.""",
   "Ford F-150 underside", "CATALYTIC CONVERTERS: 137,000+ IN 2025")
sc("""Pickups dominated that list. The Ford F-150 was first. The Ram twenty-five hundred was fourth. The Chevrolet Silverado was fifth. The Ram thirty-five hundred was seventh. Carfax said the reason is simple. Their height makes it easier for thieves to get underneath. A thief does not need to jack up a tall truck. They slide under with a battery-powered saw.""",
   "Ram 2500 underside", "F-150 #1, RAM 2500 #4, SILVERADO #5")
sc("""Why do they want them? Precious metals. Carfax said the price of rhodium more than doubled in a year, to about eleven thousand dollars an ounce in March twenty twenty-six, still far below its peak of about thirty thousand in twenty twenty-one. Thieves sell standard converters for about twenty-five to three hundred dollars, and hybrid converters for up to one thousand four hundred. For the owner, replacement can cost up to three thousand dollars.""",
   "catalytic converter", "THIEF GETS $300. YOU PAY $3,000.")
sc("""And then there are tailgates. In twenty twenty-four, police in Costa Mesa, California, counted at least twenty pickup tailgates stolen over several months, nineteen of them from Toyota Tacomas, according to ABC seven. In one case, a tailgate was removed in under sixty seconds. A local body shop estimated two thousand five hundred to four thousand five hundred dollars to repaint, install and recalibrate a replacement.""",
   "Toyota Tacoma tailgate", "TACOMA TAILGATES: UNDER 60 SECONDS")
sc("""Here is the twist. Tailgates got expensive because trucks got smarter. A modern tailgate can carry a backup camera, sensors and wiring, which is why replacement needs recalibration. The same shop owner said newer Chevrolets and F-150s were being hit for parts like cameras, door handles and assist steps. The features that make trucks nicer also make them worth stripping.""",
   "Ford F-150 tailgate camera", "SMARTER TRUCKS, PRICIER PARTS")

# ---------- 5. WHERE ----------
sc("""Where does it happen most? According to an analysis by AmericanTrucks, based on FBI crime data and Census population estimates, the cities with the highest theft rates per one hundred thousand residents were Oakland, California, St. Louis, Minneapolis, Dayton, Ohio, and Philadelphia. By state, the highest rates were in Washington, D.C., Nevada, California, Maryland and New Mexico.""",
   "Oakland California street", "OAKLAND, ST. LOUIS, MINNEAPOLIS")
sc("""California alone accounted for about twenty-one percent of U.S. vehicle thefts, about one hundred thirty-seven thousand vehicles, according to the same analysis. But here is the twist. California also had the biggest drop, with forty-five thousand, two hundred seventy-eight fewer thefts in twenty twenty-five, according to NICB as reported by The Shop. Texas had twenty-three thousand fewer, and Washington state almost twelve thousand fewer. The places with the worst problems are also improving the fastest.""",
   "California highway pickup", "CALIFORNIA: -45,278 THEFTS")
sc("""NICB's own metro ranking tells a similar story. By total thefts, the Los Angeles area led with fifty-three thousand, nine hundred eleven, followed by New York with twenty-seven thousand, one hundred thirty-eight, Chicago, Houston, and the San Francisco Bay Area. More than one-third of all U.S. thefts happened in just the top ten metro areas. By rate, among large metros, San Francisco and Oakland had the highest, about four hundred seventy-eight per one hundred thousand people, almost tied with Bakersfield, California.""",
   "Los Angeles freeway traffic", "LOS ANGELES: 53,911 THEFTS")
sc("""And here is a twist on the twist. Memphis, Tennessee, previously had the worst metro theft rate in the country, and dropped out of first place. Washington state saw the biggest percentage drop of any state, thirty-nine percent, followed by Colorado at thirty-five. Texas still had seventy-five thousand, two hundred sixty-nine thefts, the second highest total in the country.""",
   "Texas pickup truck", "WASHINGTON STATE: -39%")
sc("""One caution about city rankings. The same analysis notes that some cities in Texas, Florida and California may show low rates because of incomplete reporting to the FBI system, and it excluded Florida from state trends for that reason. So if your city does not appear on a list, it does not mean your truck is safe. It may only mean the data is incomplete.""",
   "Chevrolet Silverado city street", "LOW RATE MAY = MISSING DATA")

# ---------- 6. WHAT WORKS ----------
sc("""First, understand how modern trucks get stolen. Security company Compustar describes three common methods. In a relay attack, thieves use electronic devices to amplify the signal from a key fob, even one sitting inside the owner's house, so the truck thinks the key is nearby. In key programming, a device plugged into the diagnostic port under the dashboard programs a blank fob. And in a CAN bus attack, thieves reach the vehicle's internal network through wiring, such as behind a headlamp, and command it to unlock and start.""",
   "Toyota Tundra 2022", "RELAY, KEY PROGRAMMING, CAN BUS")
sc("""Here is the twist. None of those methods needs a broken window. A truck can be gone in minutes, with no glass on the ground and no alarm, which is why owners sometimes assume it was towed. That is also why the newest defenses are software, not just locks.""",
   "Toyota Tacoma 2024", "NO BROKEN GLASS")
sc("""So what actually works? The manufacturers are finally fighting back with software. Ford introduced a feature called Start Inhibit with the twenty twenty-four F-150, and extended it to the twenty twenty-five Super Duty, according to the Associated Press. From the FordPass app, an owner can disable the engine, so the truck will not start even with a key fob inside. Ford planned to add it to more vehicles for twenty twenty-six.""",
   "Ford F-150 2024", "FORD START INHIBIT")
sc("""The system also sends smartphone alerts if someone enters the truck, opens a door, or moves or tows it. It is included for one year after activation, then costs seven dollars ninety-nine a month. And after a theft is reported, a Ford call center confirms it with police and works with them to use Start Inhibit and locate the truck. Detroit police aim to recover vehicles within about an hour, while they are still intact.""",
   "Ford Super Duty 2025", "ALERTS + POLICE: RECOVERY IN ~1 HOUR")
sc("""Here is the twist from the HLDI data. The least stolen vehicles were mostly electric and plug-in models, Teslas, the Mustang Mach-E, the Volkswagen ID four, the Kia EV six. According to GM Authority, the study attributed that partly to plug-in vehicles often being kept in garages, or being highly visible while charging in public. In other words, where you park matters as much as what you drive.""",
   "Ford Mustang Mach-E", "LEAST STOLEN: PLUG-INS")
sc("""So here is what you can do as an owner. Never leave the key fob in the truck, even at home. Park in a garage or a well-lit, visible spot. Lock the tailgate if your truck has a lock, and consider a tailgate lock if it does not. Ask a muffler shop about a catalytic converter shield or marking the converter with your VIN. Turn on any connected-app alerts your truck offers. And keep valuable tools out of the open bed.""",
   "pickup truck in garage", "6 HABITS THAT STOP THIEVES")
sc("""NICB adds its own basic tips. Park in well-lit areas, roll up the windows, lock the doors, never leave a running vehicle unattended and take the keys with you. And it suggests layers of protection, like a steering wheel lock, an alarm, a kill switch or a GPS tracker. A visible steering wheel lock will not stop a determined professional, but it makes your truck slower and more obvious to steal than the one next to it.""",
   "steering wheel lock", "LAYERS: LOCK, ALARM, KILL SWITCH, GPS")
sc("""And check your insurance. A catalytic converter or a tailgate theft is usually covered only by comprehensive coverage. Carfax noted that replacement can reach three thousand dollars, especially for drivers without comprehensive insurance. For a truck that thieves love, comprehensive coverage is not an optional extra. It is part of the cost of owning that truck.""",
   "Ram 3500 parked", "COMPREHENSIVE COVERAGE MATTERS")

# ---------- 7. BUYING A STOLEN TRUCK ----------
sc("""Now the warning for used truck buyers. Remember that most thefts are now professional, and vehicles are often stolen for resale with their identification numbers changed. That means some of those stolen trucks end up for sale, sometimes online, sometimes at a price that looks like a great deal. And if a truck you bought turns out to be stolen, it can be taken from you, and your money may be gone.""",
   "used pickup trucks for sale", "YOU CAN BUY A STOLEN TRUCK")
sc("""So check the VIN in more than one place. The number on the dashboard, the sticker in the driver's door jamb, and the title should all match. NICB offers a free VIN check that shows whether a vehicle has been reported stolen and not recovered, or reported as a salvage vehicle by participating insurers. And a vehicle history report can show title problems. If a seller cannot produce a clean title in their own name, walk away.""",
   "pickup truck door jamb VIN sticker", "MATCH THE VIN: DASH, DOOR, TITLE")

# ---------- CLOSE ----------
sc("""So which trucks are the most stolen in America? By count, the Chevrolet Silverado and the Ford F-150, because there are so many of them. By risk per truck, heavy-duty crew cab GMC Sierras, followed by the Ram fifteen hundred and Ram thirty-five hundred. And by parts, the F-150, the Ram heavy-duty trucks and the Silverado lead for catalytic converters, while Tacomas lose tailgates.""",
   "Chevrolet Silverado GMC Sierra Ram 1500", "COUNT, RISK, PARTS")
sc("""And the final twist. The truck thieves want most is not always the most popular truck. It is the most valuable one, in the easiest place, with the fewest defenses. Theft dropped twenty-three percent in twenty twenty-five, which proves that better technology and better habits work. Your job is to make your truck a harder target than the one parked next to it.""",
   "Ford F-150 parked night", "BE THE HARDER TARGET")
sc("""We put the anti-theft checklist and the used truck VIN checks into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. If this helped, subscribe, because next we look at every new truck coming in twenty twenty-seven. And tell us in the comments, has your truck, your tailgate or your catalytic converter ever been stolen? Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One heavy-duty pickup": "Intro", "According to NICB's list": "The most stolen by count", "The Highway Loss Data Institute": "The most stolen by risk",
      "So why are pickups such good targets": "Why thieves want trucks", "But many truck thieves": "Catalytic converters and tailgates",
      "Where does it happen most": "Where trucks are stolen", "So what actually works": "What actually stops thieves",
      "Now the warning for used truck buyers": "How not to buy a stolen truck", "So which trucks are the most stolen": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video30", "length_scale": 1.45,
  "title": "The Most Stolen Trucks in America (One Is Stolen 10x More Than Average)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
