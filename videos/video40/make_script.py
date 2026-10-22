import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""One pickup on sale today costs about one thousand seven hundred dollars a year to fuel. Another costs six thousand eight hundred fifty. Same fifteen thousand miles, same roads. And with gas above four dollars a gallon for a record number of days in twenty twenty-six, that gap has never mattered more. So which pickup really costs the least to drive?""",
   "Ford Maverick Hybrid", "$1,700 vs $6,850 A YEAR")

# ---------- COLD OPEN ----------
sc("""Most buyers look at the price on the window sticker. Very few look at the other number on that sticker, the fuel economy rating. But over five or ten years of ownership, fuel can cost as much as a big part of the truck itself. And twenty twenty-six turned fuel from a footnote into a monthly shock.""",
   "gas station pump", "THE OTHER NUMBER ON THE STICKER")
sc("""In this video, we go through the official EPA fuel economy ratings of the pickups on sale heading into twenty twenty-seven. Small trucks, midsize trucks, full-size trucks, hybrids, diesels, V8s and the electric Cybertruck. We turn every rating into a yearly fuel bill at today's gas prices. Every number is sourced in the description.""",
   "pickup trucks lineup", "EVERY PICKUP, EVERY RATING")
sc("""And here is the first surprise. The most efficient engine is not always the cheapest one to run. And the hybrid badge does not always save as much as you think. Let's start with why this matters so much right now.""",
   "Toyota Tacoma Hybrid", "THE HYBRID BADGE IS NOT ENOUGH")

# ---------- 1. GAS PRICES IN 2026 ----------
sc("""According to AutoGuide, American regular gasoline averaged above four dollars a gallon for one hundred fifty-eight days in twenty twenty-six, breaking the record set in twenty twenty-two. As of October fourteenth, AAA reported a national average of four dollars and thirty-three cents a gallon. Before the conflict with Iran began in February, it was about two ninety-eight.""",
   "gas prices sign", "GAS: $2.98 → $4.33")
sc("""But here is an interesting detail. Twenty twenty-six did not set the record for the highest gas price ever. According to Fox Business, the all-time high for regular gas is still five dollars and two cents, set in June twenty twenty-two. What twenty twenty-six broke was the record for how long prices stayed high. Fewer spikes, but a longer squeeze on every truck owner.""",
   "gas station prices", "NOT THE HIGHEST, THE LONGEST")
sc("""The cause was the disruption of oil shipments through the Strait of Hormuz. September set a record for the highest average gas price ever recorded for that month. And October became the first October on record with the national average above four dollars a gallon.""",
   "oil tanker", "A RECORD YEAR AT THE PUMP")
sc("""And diesel was hit even harder. According to Fox Business, the AAA national average for diesel hit a record five dollars and eighty-five cents on September fourth, twenty twenty-six, beating the previous record from June twenty twenty-two. A year earlier, diesel cost about three seventy-one. By mid-October, AutoGuide put diesel at roughly six dollars and thirty cents.""",
   "diesel pump truck", "DIESEL: $6.30")
sc("""Look at how unevenly prices rose. On September fourth, twenty twenty-six, regular gas averaged about four dollars and fifteen cents, up from about three twenty a year earlier. That is roughly ninety-five cents more. Diesel went from about three seventy-one to five eighty-five, more than two dollars more. Keep that gap in mind, because it changes the ranking of the trucks later in this video.""",
   "diesel and gasoline pumps", "GAS +$0.95, DIESEL +$2.14")
sc("""So for this video, we use one simple rule. Fifteen thousand miles a year, the EPA combined rating for each truck, and four dollars and thirty-three cents for regular gas. For trucks that require premium fuel, we use the EPA's own premium reference price. Your numbers will vary, but the comparison stays fair.""",
   "fuel economy label", "15,000 MILES, $4.33 A GALLON")

# ---------- 2. THE SMALL TRUCKS ----------
sc("""One more note on these numbers. The EPA's own reference price for regular gas, used on sites like MPG Buddy, was four dollars and forty-seven cents, a little higher than the AAA average we use. So our yearly costs are slightly lower than the EPA's. Either way, the ranking between trucks stays exactly the same.""",
   "EPA fuel economy label", "EPA REFERENCE: $4.47")
sc("""Let's start at the top. The most fuel-efficient gas pickup in America is the Ford Maverick Hybrid with front-wheel drive. According to the EPA ratings published by MPG Buddy, it gets forty-two miles per gallon in the city, thirty-five on the highway, and thirty-eight combined. At four thirty-three a gallon, that is about one thousand seven hundred ten dollars a year.""",
   "Ford Maverick Hybrid XLT", "MAVERICK HYBRID: 38 MPG")
sc("""Notice something unusual. The Maverick Hybrid gets better mileage in the city than on the highway. That is how hybrids work. In stop and go traffic, the electric motor does more of the work and the brakes recharge the battery. On the highway, the gas engine does most of the job.""",
   "Ford Maverick city", "42 CITY, 35 HIGHWAY")
sc("""And over ten years, that difference adds up. Compared with a full-size truck that gets seventeen miles per gallon, the Maverick Hybrid saves about five hundred gallons of fuel a year. At four thirty-three, that is more than two thousand one hundred dollars a year, and more than twenty-one thousand dollars over ten years. That is how a small truck pays for a large part of itself.""",
   "Ford Maverick Lariat", "~$21,000 SAVED IN 10 YEARS")
sc("""Now the twist. Choose the Maverick Tremor, the off-road version with the two liter turbo four-cylinder and all-wheel drive, and the rating drops to twenty-one city, twenty-seven highway and twenty-three combined. That is about two thousand eight hundred twenty-four dollars a year. Same name, same size, about one thousand one hundred dollars more fuel every year.""",
   "Ford Maverick Tremor", "MAVERICK TREMOR: 23 MPG")
sc("""The Hyundai Santa Cruz is the other small pickup. The front-wheel-drive version with the two point five liter four-cylinder gets twenty-two city, thirty highway and twenty-five combined. That is about two thousand six hundred dollars a year. Good, but well behind the Maverick Hybrid.""",
   "Hyundai Santa Cruz", "SANTA CRUZ: 25 MPG")

# ---------- 3. THE MIDSIZE TRUCKS ----------
sc("""Now the midsize trucks. The Ford Ranger with rear-wheel drive and the two point three liter EcoBoost four-cylinder gets twenty-one city, twenty-five highway and twenty-three combined. That is about two thousand eight hundred twenty-four dollars a year, the same as the Maverick Tremor.""",
   "Ford Ranger 2024", "RANGER: 23 MPG")
sc("""The Toyota Tacoma with four-wheel drive and the two point four liter turbo four-cylinder gets nineteen city, twenty-four highway, and twenty-one combined. That is about three thousand ninety-three dollars a year.""",
   "Toyota Tacoma 2024", "TACOMA 4WD: 21 MPG")
sc("""And here is the hybrid surprise. The Tacoma with the i-FORCE MAX hybrid gets twenty-two city, twenty-four highway, and twenty-three combined. Only two miles per gallon better than the regular Tacoma. That saves about sixty-two gallons, or roughly two hundred seventy dollars a year. Toyota designed this hybrid mainly for power, not for mileage.""",
   "Toyota Tacoma TRD Pro", "TACOMA HYBRID: ONLY +2 MPG")
sc("""Remember, the Tacoma hybrid is about power. In the twenty twenty-four TRD Pro, according to SlashGear, the hybrid engine made three hundred twenty-six horsepower and four hundred sixty-five pound-feet of torque. So the hybrid buys you torque first, and a small fuel saving second.""",
   "Toyota Tacoma TRD Pro hybrid", "326 HP, 465 LB-FT")
sc("""The Chevrolet Colorado with rear-wheel drive and the two point seven liter turbo four gets nineteen city, twenty-four highway, and twenty-one combined. With four-wheel drive, it drops to nineteen combined. The Nissan Frontier with rear-wheel drive also gets twenty-one combined, with nineteen city and twenty-four highway.""",
   "Chevrolet Colorado 2023", "COLORADO / FRONTIER: 21 MPG")
sc("""The Honda Ridgeline, with its three point five liter V6 and all-wheel drive, gets eighteen city, twenty-four highway, and twenty-one combined. And the Jeep Gladiator, with its three point six liter V6 and four-wheel drive, gets seventeen city, twenty-two highway, and nineteen combined. That is about three thousand four hundred eighteen dollars a year.""",
   "Jeep Gladiator", "GLADIATOR: 19 MPG")
sc("""So here is the strange result. The most fuel-efficient midsize trucks get about twenty-three miles per gallon. And as we will see, that is about the same as some full-size half-ton pickups. Going smaller does not automatically save fuel anymore.""",
   "Ford Ranger and F-150", "MIDSIZE ≈ FULL-SIZE?")

# ---------- 4. THE FULL-SIZE TRUCKS ----------
sc("""Now the full-size trucks, the ones America buys most. The best gas-powered full-size pickup on the EPA list is the Ford F-150 Hybrid, the PowerBoost. With rear-wheel drive, it gets twenty-three city, twenty-five highway, and twenty-four combined. With four-wheel drive, it gets twenty-two, twenty-four and twenty-three.""",
   "Ford F-150 Hybrid", "F-150 HYBRID: 24 MPG")
sc("""That four-wheel-drive F-150 Hybrid costs about two thousand eight hundred twenty-four dollars a year. Exactly the same as the Maverick Tremor and the Ranger. A full-size truck that can tow and carry far more, for the same fuel bill as a compact.""",
   "Ford F-150 PowerBoost", "SAME BILL AS A RANGER")
sc("""Now the regular F-150 engines with four-wheel drive. The two point seven liter EcoBoost gets twenty combined. The three point five liter EcoBoost gets nineteen. And the five liter V8 also gets nineteen combined, with sixteen city and twenty-four highway. That is about three thousand four hundred eighteen dollars a year.""",
   "Ford F-150 XLT", "F-150 V8 = 3.5 ECOBOOST: 19 MPG")
sc("""Here is the twist. The twin-turbo three point five liter EcoBoost, the engine that was supposed to deliver V8 power with V6 fuel economy, gets the same combined rating as the V8 in this four-wheel-drive configuration. Nineteen and nineteen. And the V8 even gets one more mile per gallon on the highway.""",
   "Ford F-150 Coyote", "TURBO V6 = V8 ON FUEL")
sc("""Now Ram. The Ram fifteen hundred with four-wheel drive and the three point six liter V6 gets twenty-one combined. The three liter Hurricane twin-turbo six gets twenty. And the returning five point seven Hemi V8 gets eighteen, with sixteen city and twenty highway. That is about three thousand six hundred eight dollars a year.""",
   "Ram 1500 2025", "RAM HEMI 4WD: 18 MPG")
sc("""So the Hemi costs about three hundred sixty dollars a year more in fuel than the Hurricane. Over five years, that is around one thousand eight hundred dollars. Add the one thousand two hundred dollar Hemi option, and the V8 Ram costs about three thousand dollars more over five years. Some buyers will gladly pay it for the sound.""",
   "Ram 1500 Hemi", "HEMI: ~$3,000 MORE OVER 5 YEARS")
sc("""And the most efficient Ram is the one nobody talks about. The base three point six liter Pentastar V6 with rear-wheel drive gets twenty city, twenty-five highway, and twenty-two combined. The cheapest engine in the Ram lineup is also its most efficient, and about six hundred fifty dollars a year cheaper to fuel than the Hemi with four-wheel drive.""",
   "Ram 1500 Tradesman", "BASE RAM V6: 22 MPG")
sc("""Now Chevy. The Silverado with four-wheel drive and the five point three liter V8 gets fifteen city, nineteen highway, and seventeen combined. The six point two liter V8 also gets seventeen combined. At four thirty-three a gallon, seventeen miles per gallon costs about three thousand eight hundred twenty dollars a year.""",
   "Chevrolet Silverado 1500", "SILVERADO V8 4WD: 17 MPG")
sc("""Now put the full-size trucks side by side. A four-wheel-drive Silverado V8 at seventeen miles per gallon costs about three thousand eight hundred twenty dollars a year. A four-wheel-drive F-150 Hybrid at twenty-three costs about two thousand eight hundred twenty-four. That is about one thousand dollars a year, or five thousand dollars over five years, between two trucks that do the same job.""",
   "Chevrolet Silverado and Ford F-150", "$1,000 A YEAR DIFFERENCE")
sc("""And here is what the gas price spike did to that same Silverado. At two ninety-eight a gallon, the price before the Iran conflict, seventeen miles per gallon cost about two thousand six hundred thirty dollars a year. At four thirty-three, it costs about three thousand eight hundred twenty. The truck did not change. The bill went up nearly one thousand two hundred dollars a year.""",
   "Chevrolet Silverado Trail Boss", "+$1,190 A YEAR FROM GAS PRICES")
sc("""And the Toyota Tundra with four-wheel drive and the twin-turbo V6 gets seventeen city, twenty-two highway, and nineteen combined. The Tundra Hybrid with rear-wheel drive gets twenty, twenty-four and twenty-two. Toyota's full-size hybrid, like the Tacoma's, is tuned more for power than for maximum mileage.""",
   "Toyota Tundra", "TUNDRA: 19 / HYBRID: 22")

# ---------- 5. THE DIESEL TWIST ----------
sc("""And the Tundra hybrid does deliver that power. According to Pickup Truck plus SUV Talk, the i-FORCE MAX makes four hundred thirty-seven horsepower and five hundred eighty-three pound-feet of torque, compared with three hundred eighty-nine horsepower for the standard twin-turbo V6. So like the Tacoma, Toyota's full-size hybrid is a performance option that happens to save a little fuel.""",
   "Toyota Tundra i-Force Max", "437 HP, 583 LB-FT")
sc("""Now the most efficient non-hybrid full-size truck. It is the Chevrolet Silverado and GMC Sierra with the three liter Duramax inline-six turbo-diesel. With rear-wheel drive, the Silverado gets twenty-three city, twenty-eight highway and twenty-five combined. With four-wheel drive, twenty-two, twenty-five and twenty-three.""",
   "Chevrolet Silverado Duramax", "DURAMAX DIESEL: 25 MPG")
sc("""On paper, the diesel is the champion of full-size trucks. Twenty-five miles per gallon in a full-size pickup. But here is the twist of twenty twenty-six. Diesel costs much more than gasoline. At six dollars and thirty cents a gallon, the rear-wheel-drive diesel Silverado costs about three thousand seven hundred eighty dollars a year to fuel.""",
   "diesel fuel nozzle", "25 MPG x $6.30 = $3,780")
sc("""Now compare that with the Silverado's two point seven liter turbo four-cylinder gas engine, which gets only twenty combined with rear-wheel drive. At four thirty-three a gallon, it costs about three thousand two hundred forty-eight dollars a year. So the less efficient gas engine costs about five hundred dollars a year less to fuel than the diesel.""",
   "Chevrolet Silverado Custom", "LESS MPG, LOWER BILL")
sc("""And remember the heavy-duty trucks. Pickups like the Super Duty, the Silverado twenty-five hundred and the Ram twenty-five hundred sit above eight thousand five hundred pounds gross vehicle weight, so they are not part of these EPA ratings at all. Many of them run on diesel. For heavy-duty owners, twenty twenty-six diesel prices hit harder than for anyone else.""",
   "Ram 2500 diesel", "HEAVY DUTY: NO EPA RATING")
sc("""SlashGear noted that the EPA put the annual fuel cost of the two point seven and the diesel nearly identical, even before diesel's record run. In twenty twenty-six, the diesel's mileage advantage disappeared at the pump. Diesel still makes sense for heavy towing and long engine life, but not for saving money on fuel this year.""",
   "Chevrolet Silverado 2500HD", "DIESEL'S ADVANTAGE: GONE")

# ---------- 6. THE THIRSTIEST TRUCKS ----------
sc("""Now the other end of the list. The thirstiest light-duty pickups are the performance trucks. The Ford F-150 Raptor R, with its supercharged five point two liter V8, gets ten miles per gallon in the city, fifteen on the highway, and twelve combined. And it requires premium fuel.""",
   "Ford F-150 Raptor R", "RAPTOR R: 12 MPG")
sc("""Using the EPA's premium reference price of five dollars and forty-eight cents, MPG Buddy puts the Raptor R's yearly fuel cost at six thousand eight hundred fifty dollars. That is four times the Maverick Hybrid. Over five years, the fuel difference between them is more than twenty-five thousand dollars, nearly the price of a new Maverick.""",
   "Ford Raptor R", "$6,850 A YEAR")
sc("""The supercharged six point two liter V8 Ram fifteen hundred with all-wheel drive is rated the same, ten city, fourteen highway and twelve combined. And the Ram fifteen hundred RHO, with the high-output Hurricane twin-turbo six, gets fourteen city, sixteen highway, and fifteen combined, on premium fuel. Removing two cylinders did not make the performance Ram efficient.""",
   "Ram 1500 RHO", "RAM RHO: 15 MPG")
sc("""Even the less extreme Rams pay a price. The Ram fifteen hundred HO with four-wheel drive and the Warlock with four-wheel drive are both rated at seventeen miles per gallon combined, according to the EPA listings. That is three miles per gallon below the standard Hurricane with four-wheel drive, which gets twenty.""",
   "Ram 1500 Warlock", "RAM HO / WARLOCK: 17 MPG")
sc("""And the Chevrolet Silverado ZR2, with the six point two liter V8, gets fourteen city, seventeen highway and fifteen combined, also on premium. MPG Buddy puts its yearly fuel bill at about five thousand five hundred dollars. Off-road capability costs money at every fill-up.""",
   "Chevrolet Silverado ZR2", "SILVERADO ZR2: 15 MPG")
sc("""So here is the pattern. Big tires, off-road suspension and supercharged engines cut fuel economy sharply. The Raptor R gets twelve miles per gallon, compared with nineteen for a regular four-wheel-drive F-150 V8. The fastest, most capable version of a pickup is almost always its thirstiest.""",
   "pickup off-road tires", "OFF-ROAD = THIRSTY")

# ---------- 7. THE ELECTRIC OPTION ----------
sc("""And then there is the electric option. The twenty twenty-six Tesla Cybertruck Long Range is rated at seventy-eight miles per gallon equivalent combined, with eighty-nine in the city and sixty-seven on the highway, and an EPA range of three hundred thirty-five miles. MPG Buddy estimates about one thousand dollars a year in electricity for fifteen thousand miles.""",
   "Tesla Cybertruck", "CYBERTRUCK: 78 MPGe, ~$1,000")
sc("""The Rivian R1T is rated between eighty-two and eighty-seven miles per gallon equivalent depending on the version. And here is the twist. Even with gas at record levels, the electric pickup market shrank. Ram canceled its fully electric Ram fifteen hundred in twenty twenty-five, and the federal electric vehicle tax credit was repealed that September.""",
   "Rivian R1T", "R1T: 82–87 MPGe")
sc("""So the cheapest pickup to fuel in America is an electric truck that costs far more to buy, and the cheapest gas truck to fuel is the Maverick Hybrid. Your real savings depend on your electricity price, where you charge, and how long you keep the truck.""",
   "electric pickup charging", "CHEAPEST TO FUEL: ELECTRIC")

# ---------- 8. WHAT IT MEANS FOR BUYERS ----------
sc("""So what should you do with all of these numbers? First, compare the yearly cost, not just the miles per gallon. A two mile per gallon difference at seventeen miles per gallon saves far more fuel than a two mile per gallon difference at thirty-five. The gains are biggest at the bottom of the list.""",
   "fuel economy window sticker", "1. COMPARE THE YEARLY COST")
sc("""Think about it per month, too. The Maverick Hybrid at about one thousand seven hundred ten dollars a year is roughly one hundred forty-two dollars a month in fuel. A seventeen mile per gallon V8 truck is roughly three hundred eighteen dollars a month. That one hundred seventy-six dollar gap is bigger than many people's phone and internet bills combined.""",
   "family pickup truck", "$142 vs $318 A MONTH")
sc("""Second, pick the drivetrain you really need. Four-wheel drive usually costs one to two miles per gallon. The Colorado drops from twenty-one to nineteen, and the F-150 Hybrid from twenty-four to twenty-three. If you live where it rarely snows and you do not go off-road, rear-wheel drive saves money every month.""",
   "pickup truck snow", "2. 4WD COSTS 1–2 MPG")
sc("""Third, be careful with the fuel type. Several performance trucks require premium, which the EPA prices more than a dollar above regular. And diesel cost about two dollars more than regular gas in October twenty twenty-six. The best rating on the sticker can still produce the biggest bill.""",
   "premium gasoline pump", "3. CHECK THE FUEL TYPE")
sc("""And fourth, if fuel cost is your top priority, the full-size hybrid is the sweet spot. The F-150 PowerBoost gets twenty-four combined with rear-wheel drive, close to the best midsize trucks, while towing and hauling like a full-size truck. And if you do not need a full-size truck, the Maverick Hybrid is in a class of its own.""",
   "Ford F-150 Hybrid Pro Power Onboard", "4. HYBRID = SWEET SPOT")

# ---------- CLOSE ----------
sc("""So, what is the real fuel economy of every pickup heading into twenty twenty-seven? The Maverick Hybrid leads at thirty-eight miles per gallon. The F-150 Hybrid leads the full-size gas trucks. The diesel Silverado has the best non-hybrid rating, but this year it costs more to fuel than a gas engine. And the performance trucks sit at twelve to fifteen miles per gallon.""",
   "Ford Maverick", "THE VERDICT")
sc("""And the final twist. The fuel economy rating that matters most is not printed on the sticker. It is the price at the pump. In twenty twenty-six, record gas and diesel prices turned a few miles per gallon into hundreds or thousands of dollars a year. The right truck is the one whose fuel bill you can live with for the next ten years.""",
   "gas station at night", "THE PUMP DECIDES")
sc("""We put the yearly fuel cost of every twenty twenty-seven pickup, at three different gas prices, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for more truck data every day. And tell us in the comments, what mileage does your truck really get? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"One pickup on sale today": "Intro", "According to AutoGuide, American regular": "Gas prices in 2026",
      "Let's start at the top": "The small trucks", "Now the midsize trucks": "The midsize trucks",
      "Now the full-size trucks": "The full-size trucks", "Now the most efficient non-hybrid": "The diesel twist",
      "Now the other end of the list": "The thirstiest trucks", "And then there is the electric option": "The electric option",
      "So what should you do with all": "What it means for buyers", "So, what is the real fuel economy": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video40", "length_scale": 1.4,
  "title": "The Real Fuel Cost of Every Pickup in 2027 (One Costs 4x More Than Another)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
