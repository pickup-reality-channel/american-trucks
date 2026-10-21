import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""Fifteen billion dollars. That is how much Americans spent modifying their pickups in a single year, according to SEMA. Nearly thirteen million trucks got new parts. Lift kits, giant tires, bed covers, lights. Some of those upgrades make a truck better and even save money. Others quietly cost their owners thousands, every year, for as long as they own the truck.""",
   'lifted pickup truck', '$15 BILLION ON PICKUP MODS')
sc("""And there is one myth that stops many owners from making smart upgrades: the idea that any aftermarket part voids your warranty. The federal government says that is not how it works. In this video we go through bed covers, tires, wheels, lifts and more, and separate the mods worth your money from the ones that are not.""",
   'pickup truck bed cover', 'WHICH MODS ARE WORTH IT?')
sc("""Every number in this video comes from a published source listed in the description. Prices for parts vary widely by truck and brand, so we will focus on what the data shows and the trade-offs you should know. If we could not confirm a figure, we left it out. Let's start with how big this market really is.""",
   'truck accessories store', 'EVERY NUMBER IS SOURCED')
sc("""According to SEMA's twenty twenty-six market report, accessory and performance parts sales in America reached fifty-two point nine two billion dollars in twenty twenty-five. Pickup parts were the largest category, at thirty percent of all sales. Pickups and S U Vs together made up forty-three percent of the market.""",
   'SEMA show trucks', 'AFTERMARKET: $52.92 BILLION')
sc("""SEMA says nearly thirteen million pickups were accessorized in twenty twenty-five. Owners spent more than three billion dollars on suspension products like lift kits, and more than two billion on off-road tires for pickups and S U Vs. And here is the first twist: only twenty-six percent of people who accessorize their pickups actually use them off-road.""",
   'pickup truck off-road', 'ONLY 26% GO OFF-ROAD')
sc("""So most modified trucks spend their lives on pavement. That matters, because many off-road parts make a truck worse on the road: more noise, less fuel economy, slower braking and a harsher ride. The best mod is the one that matches how you actually use your truck, not how you imagine using it.""",
   'lifted truck highway', 'MATCH MODS TO REAL USE')
sc("""And the buyers are young. According to SEMA, more than half of accessory and performance parts buyers are under forty, and about one in four drivers bought aftermarket products to personalize their vehicles in twenty twenty-five. Truck modification is not a niche hobby. It is a mainstream American habit.""",
   'custom pickup truck show', 'HALF OF BUYERS UNDER 40')
sc("""Before we rank the mods, let's kill the biggest myth. Many owners believe that installing any aftermarket part voids the truck's warranty. According to the Federal Trade Commission, your warranty stays in effect if you use aftermarket or recycled parts.""",
   'Federal Trade Commission building', '2. THE WARRANTY MYTH')
sc("""Here is how it works. Under the federal warranty law, the F T C says that a manufacturer or dealer must prove that an aftermarket part caused the damage before denying coverage. And it is illegal for a dealer to deny your warranty just because someone else did the maintenance or repair work.""",
   'pickup truck service', 'THEY MUST PROVE THE PART CAUSED IT')
sc("""Now the twist. That protection has limits. If a defective or badly installed part damages something the warranty covers, the F T C says the manufacturer can deny coverage for that damaged part and charge you for the repair. So a poorly installed lift kit that damages the front axle may not be covered, even if the rest of your warranty is fine.""",
   'truck suspension lift kit', 'BAD INSTALLS CAN COST YOU')
sc("""The F T C also says to keep your maintenance records, because the warranty company can ask for them. Keep receipts for oil changes, tire rotations and inspections, and keep the receipts for every part you install. If a claim is ever questioned, paperwork is your best defense.""",
   'receipts folder', 'KEEP EVERY RECEIPT')
sc("""Now the mods. We will start with the one most truck owners buy first: the bed cover, also called a tonneau cover. Bed covers come in soft roll-up, folding, hard hinged and retractable styles, and prices range from budget soft covers to expensive powered systems.""",
   'pickup truck tonneau cover', '3. BED COVERS')
sc("""Why is it often worth it? Security and weather. A locking hard cover keeps tools and luggage out of sight and protected from rain and snow. For many owners, that turns the bed into a giant trunk, and it can prevent the theft of expensive tools, which is a real risk for work trucks.""",
   'pickup truck bed tools', 'THE BED BECOMES A TRUNK')
sc("""And fuel economy? This is where you hear big claims. Some owners say a cover saves a lot of fuel, others say it does nothing. We could not find a current, independent number we trust, so we will not give you one. If a seller promises a specific fuel savings, ask for the independent test behind it.""",
   'pickup truck highway', 'FUEL CLAIMS? ASK FOR PROOF')
sc("""The downside is space. A cover can make it harder to haul tall items like furniture or appliances. Hard covers can be heavy, and some block part of the bed opening. If you often carry tall loads, a roll-up or folding cover that opens fully may be the better choice.""",
   'pickup truck hauling furniture', 'COVERS LIMIT TALL LOADS')
sc("""Verdict on bed covers: worth it for most owners who carry tools, luggage or groceries and want security. Less useful for owners who constantly haul tall cargo. Buy one that fits your exact truck and bed length, and choose security level based on what you carry.""",
   'pickup truck bed cover closed', 'VERDICT: WORTH IT FOR MOST')
sc("""Next: tires, the mod that affects everything. Tires decide how your truck brakes, steers, rides and how much fuel it uses. And in twenty twenty-six, tires got more expensive. According to SlashGear, the federal Producer Price Index for tire manufacturing rose again in August twenty twenty-six, and some manufacturers announced increases of up to five to ten percent.""",
   'pickup truck tires', '4. TIRES: PRICES RISING')
sc("""Why are tire prices rising? According to SlashGear, Michelin said in April twenty twenty-six that the conflict in the Middle East was raising its raw material and energy costs. Tires are made with oil-based materials, so when oil jumps, tires follow. That makes choosing the right tire more important than ever.""",
   'tire shop', 'OIL PUSHES TIRE PRICES')
sc("""Here is the twist about big off-road tires. They look great, and SEMA says owners spend billions on them. But aggressive mud-terrain tires are usually louder on the highway, heavier, and can wear faster and reduce fuel economy compared with all-season or highway tires. If you rarely leave the pavement, you pay for that look every day.""",
   'mud terrain tires', 'BIG TIRES: YOU PAY EVERY DAY')
sc("""The middle ground for many owners is an all-terrain tire. It handles gravel, dirt and light snow better than a highway tire, without the full penalty of a mud tire. For a truck that sees a mix of highway and back roads, all-terrains are often the best balance.""",
   'all terrain tires truck', 'ALL-TERRAIN: THE BALANCE')
sc("""And bigger tires can create hidden problems. Larger tires can make the speedometer read wrong, change shift points and affect braking and stability systems. Some owners need to recalibrate the truck's computer after a tire size change. Always check what size your truck can handle without rubbing or other changes.""",
   'pickup truck wheel well', 'BIGGER TIRES, HIDDEN PROBLEMS')
sc("""Verdict on tires: a good set of the right tires is one of the best upgrades you can make for safety. The wrong tires are one of the most expensive mistakes, because you pay in fuel and wear for tens of thousands of miles. Choose tires for how you really drive.""",
   'new tires', 'VERDICT: RIGHT TIRES = BEST MOD')
sc("""Now wheels. Aftermarket wheels are among the most popular pickup mods, according to SEMA, along with body parts and suspension. Wheels are mostly about style, but they can also change the truck's weight, ride and handling.""",
   'custom truck wheels', '5. WHEELS')
sc("""The twist is that larger wheels with thinner tires can make the ride harsher and the tires more expensive, and they may be more easily damaged by potholes. Wheels that push far outside the fenders can throw mud and rocks, and some states have rules about tire coverage. Check your state's rules before you buy.""",
   'pickup truck big wheels', 'BIG WHEELS: HARSHER RIDE')
sc("""Next, lift kits, the most dramatic mod. According to SEMA, owners spent more than three billion dollars on suspension products like lift kits in twenty twenty-five, mostly for pickups and S U Vs. A lift raises the truck for bigger tires and more ground clearance.""",
   'lifted pickup truck', 'LIFT KITS: $3 BILLION+')
sc("""Here is the big twist. A lift can make a truck worse for most of what owners actually do. A higher truck catches more wind, usually uses more fuel, has a higher center of gravity and can be harder to load and tow with. A lifted truck can also be harder to park in garages and parking structures.""",
   'lifted truck parking garage', 'LIFTS CAN MAKE IT WORSE')
sc("""And lifts can raise insurance costs. According to Insurify, trucks can cost more to insure when they are lifted or modified. Always tell your insurer about modifications. If you do not, a claim could be denied or your aftermarket parts might not be covered after an accident.""",
   'insurance form', 'TELL YOUR INSURER')
sc("""Verdict on lift kits: worth it if you really go off-road and need clearance. For most highway trucks, a small leveling kit, which raises the front to match the rear, can give the look with fewer downsides. And remember the warranty lesson: installation quality matters.""",
   'leveling kit truck', 'VERDICT: ONLY IF YOU GO OFF-ROAD')
sc("""Now the mods that often pay for themselves. Number one: a quality bed liner. A spray-in or drop-in liner protects the bed from scratches, dents and rust. That protection helps resale value, because a beat-up bed is one of the first things used buyers notice.""",
   'spray in bed liner', '6. BED LINERS')
sc("""Number two: floor liners. Custom floor liners trap mud, snow and spills. They are cheap compared with replacing carpet, and they keep the interior looking newer for resale. It is one of the simplest ways to protect your truck's value.""",
   'truck floor mats', 'FLOOR LINERS PROTECT VALUE')
sc("""Number three: a proper towing setup, if you tow. A correct hitch, a brake controller and the right mirrors are not just accessories, they are safety equipment. A good setup protects your truck, your trailer and everyone around you.""",
   'trailer hitch brake controller', 'PROPER TOWING GEAR')
sc("""Number four: lighting, done carefully. Better headlights can improve safety on dark rural roads. But aftermarket lights that are too bright or aimed wrong can blind other drivers and may not be street legal. Choose parts made for road use and aim them correctly.""",
   'truck LED lights', 'LIGHTING: STREET LEGAL ONLY')
sc("""Now the mods that rarely pay you back. Performance tunes and engine modifications can add power, but they can also affect emissions compliance and warranty coverage on the parts they change. Under the F T C rules, if a tune damages the engine, the manufacturer may deny that repair.""",
   'truck engine bay', '7. TUNES: HIGH RISK')
sc("""And emissions are a legal minefield. In January twenty twenty-six, the Justice Department said it would no longer bring criminal charges for diesel emissions deletes, according to Fleet Maintenance. But here is the twist: tampering is still a violation of the Clean Air Act. The Justice Department said civil enforcement with the E P A will continue when appropriate, with penalties listed at forty-five thousand, two hundred sixty-eight dollars per tampered engine.""",
   'diesel truck exhaust', 'DELETES: STILL ILLEGAL')
sc("""And states can have their own inspection and emissions rules. A deleted truck may fail inspection, be impossible to register in some places, and be very hard to sell to a dealer. No jail time does not mean no risk. It is one of the worst mods you can make for resale and peace of mind.""",
   'vehicle emissions inspection', 'NO JAIL ≠ NO RISK')
sc("""Another mod that rarely pays back is extreme cosmetic changes. Loud exhaust, unusual paint or wraps and extreme stances may make the truck unique, but they can shrink the pool of used buyers. When you sell, a truck that is close to stock often sells faster and for more.""",
   'custom painted pickup', 'EXTREME CHANGES SHRINK BUYERS')
sc("""Here is the resale twist. Most mods do not return their full cost when you sell. Buyers rarely pay extra for someone else's taste. The parts that hold value tend to be the practical ones: bed covers, liners, towing gear and quality tires. Keep the original parts if you can, so you can return the truck to stock.""",
   'used pickup truck for sale', 'KEEP THE ORIGINAL PARTS')
sc("""Let's put the cost in perspective. According to AAA, a new half-ton pickup already costs about sixteen thousand, four hundred forty-nine dollars a year to own in twenty twenty-six. Mods are added on top of that number. A two thousand dollar lift with expensive tires that cut fuel economy can add to the yearly bill for as long as you own the truck.""",
   'pickup truck', 'MODS ADD TO A $16,449 BILL')
sc("""And fuel makes it worse in twenty twenty-six. According to the U S Energy Information Administration, regular gasoline averaged four dollars and twenty-eight cents a gallon and diesel six dollars and twenty-eight cents in the week of October nineteenth. Any mod that reduces fuel economy costs more when fuel is this expensive.""",
   'gas station prices', 'GAS $4.28. DIESEL $6.28')
sc("""So do the math before you buy. Estimate how much fuel a mod might cost you, add any insurance increase, and think about resale. A mod that costs one thousand dollars to install might cost several thousand over five years. A mod that protects the truck might pay you back at resale.""",
   'calculator', 'DO THE MATH FIRST')
sc("""Financing mods is another trap. Some dealers add accessories to a new truck and roll them into the loan. With average new loans at seven percent interest, according to Edmunds, you pay interest on those parts for years. Many accessories cost less from independent sellers, installed after you buy.""",
   'car dealership accessories', "DON'T FINANCE MODS AT 7%")
sc("""And watch for dealer-installed add-ons you did not ask for. Some trucks arrive on the lot with extras like wheels, lift kits or protection packages already added to the price. You can negotiate those prices or look for a truck without them.""",
   'dealer add-on sticker', 'NEGOTIATE DEALER ADD-ONS')
sc("""Now the installation question: do it yourself or pay a shop? Simple mods like floor liners and many bed covers are easy to install at home. Suspension, lighting wiring and engine work are better left to professionals, because a bad install can cost you warranty coverage and safety.""",
   'mechanic shop truck', 'DIY OR PRO?')
sc("""If you use a shop, choose one with experience on your truck model, ask for a written estimate and keep the invoice. That invoice is proof of professional installation if a warranty question ever comes up. Remember the F T C rule: the manufacturer must prove the part caused the damage.""",
   'mechanic invoice', 'GET A WRITTEN INVOICE')
sc("""Here is one last twist. Some manufacturers sell their own accessories and performance parts through dealers, sometimes with warranty coverage included. They can cost more, but they may be the safest choice for owners worried about warranty claims. Compare both options before you buy.""",
   'Ford Performance parts', 'FACTORY ACCESSORIES: A SAFER BET')
sc("""Now let's look at mods by type of owner, starting with the commuter. If your truck mostly drives to work and back, the best mods are about comfort and protection: floor liners, a bed cover, quality highway tires and maybe a better sound system. Skip the lift and the mud tires. They will cost you every single day at the pump.""",
   'pickup truck commute', 'THE COMMUTER')
sc("""Next, the weekend camper. If you camp or haul gear, a bed cover or a camper shell, a bed organizer and all-terrain tires can make a real difference. A modest lift may help on rough forest roads, but think twice before going big, because a heavy, lifted truck can be harder to drive on the long highway trip to get there.""",
   'pickup truck camping', 'THE WEEKEND CAMPER')
sc("""Then the tower. If you pull a trailer, every mod should support towing. That means the right hitch, a brake controller, towing mirrors and tires with the correct load rating. A lift and oversized tires can reduce your truck's towing stability, so towers usually keep the truck close to stock.""",
   'pickup truck towing camper', 'THE TOWER')
sc("""And the contractor. For work trucks, the best mods are about organization and security: toolboxes, ladder racks, locking bed covers and good lighting for early mornings. These upgrades can save time every day, and time is money for a business. A work truck rarely needs a lift.""",
   'work truck toolbox', 'THE CONTRACTOR')
sc("""Finally, the true off-roader. If you really go off-road, then lifts, skid plates, off-road tires and recovery gear make sense. But even here, the smartest builds start small and add parts as you learn what your trails need. SEMA's data shows only about a quarter of pickup accessorizers actually go off-road, so if you are one of them, build for real trails, not for photos.""",
   'off-road pickup trail', 'THE TRUE OFF-ROADER')
sc("""Here is a twist about safety equipment. Modern trucks have cameras, radar and sensors for systems like automatic emergency braking. Some mods, like a lift, a new bumper or a light bar in the wrong spot, can block or misalign these sensors. After any change to the front of the truck, make sure safety systems still work and are calibrated.""",
   'pickup truck front sensors', 'MODS CAN BLOCK SAFETY SENSORS')
sc("""And check your payload. Every accessory adds weight: a steel bumper, a winch, a toolbox, a camper shell. That weight reduces how much you can carry and tow. Your truck's payload is printed on a sticker in the driver's door jamb. Add up what your mods weigh before you load the truck.""",
   'truck door jamb sticker', 'MODS EAT YOUR PAYLOAD')
sc("""Theft is the last consideration. Expensive wheels, tailgates, catalytic converters and tools in the bed can attract thieves. Locking lug nuts, a locking tailgate and a secure bed cover are inexpensive protection. And the National Insurance Crime Bureau ranked full-size pickups like the Silverado among the most stolen vehicles of twenty twenty-five.""",
   'locking lug nuts', 'PROTECT YOUR MODS')
sc("""One more thing before you buy any part: check that it is made for your exact truck. Model year, cab size, bed length and trim can all change what fits. A cheap part that almost fits can cost more in installation time, rattles and leaks than a quality part that fits perfectly the first time.""",
   'pickup truck bed measuring', 'CHECK EXACT FITMENT')
sc("""And read reviews from owners of the same truck. Forums and owner groups often reveal problems that product pages never mention, like a cover that leaks in heavy rain or a tire that wears fast on a heavy truck. Real owners are your best free research.""",
   'truck owners meet', 'LEARN FROM REAL OWNERS')
sc("""Let's summarize. Worth it for most owners: a bed cover for security, good tires for how you drive, a bed liner, floor liners and proper towing gear if you tow. Worth it only for some: lifts, big off-road tires and aggressive wheels. Rarely worth it: engine tunes, emissions changes and extreme cosmetic changes.""",
   'pickup truck', 'THE FINAL RANKING')
sc("""And never forget the three rules. Tell your insurer about modifications. Keep every receipt and maintenance record. And choose quality installation. Those three habits protect your warranty, your insurance and your resale value.""",
   'pickup truck garage', 'THE THREE RULES')
# ---------- CLOSE ----------
sc("""So here is your mod checklist for twenty twenty-seven. One: buy mods for how you really use the truck. Two: know your warranty rights and keep records. Three: tell your insurer. Four: avoid financing accessories. And five: keep the original parts so you can return to stock when you sell.""",
   'checklist', 'YOUR MOD CHECKLIST')
sc("""We put the full mod list, with what to buy and what to skip, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, about towing mistakes that wreck your truck. And tell us in the comments: what is the best mod you ever put on your truck? Thanks for watching.""",
   'pickup truck sunset', "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {'Fifteen billion dollars. That is': 'Intro', "According to SEMA's twenty twenty-six": '1. The $15 billion habit', 'Before we rank the mods,': '2. The warranty myth', 'Now the mods. We will': '3. Bed covers', 'Next: tires, the mod that': '4. Tires', 'Now wheels. Aftermarket wheels are': '5. Wheels and lifts', 'Now the mods that often': '6. Mods that pay you back', 'Now the mods that rarely': '7. Mods that rarely pay back', "Let's put the cost in": '8. The real cost of mods', 'Now the installation question: do': '9. Installation', "Now let's look at mods": 'Mods by type of owner', "Let's summarize. Worth it for": 'The final ranking', 'So here is your mod': 'Your checklist for 2027'}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": 'video56', "length_scale": 1.45,
  "title": 'Truck Mods Worth the Money in 2026: Bed Covers, Tires, Lifts (And the Warranty Myth)', "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.45/212,1), "min")
