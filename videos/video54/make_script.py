import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Insuring one electric pickup costs more than four thousand dollars a year. A giant Ram thirty-five hundred heavy-duty truck can be cheaper to insure than a midsize Toyota Tacoma. And according to one major study, the average full-size pickup can actually cost less to insure than a sedan. Truck insurance in twenty twenty-six is full of surprises, and most buyers only discover them after they sign.""",
   "GMC Hummer EV pickup", "TRUCK INSURANCE: THE SURPRISES")
sc("""So why does truck insurance cost so much, and when does it not? We will look at the national numbers, the most expensive and cheapest trucks to insure, the hidden reasons behind the prices, and what you can do before you buy. Because the time to check insurance is before you choose the truck, not after.""",
   "Ford F-150 Chevrolet Silverado", "CHECK INSURANCE BEFORE YOU BUY")
sc("""Every number in this video comes from a published source, listed in the description. Insurance prices depend heavily on your age, location, driving record and coverage, so your quote will be different. This is general information. If we could not confirm a figure, we left it out. Let's start with the big picture.""",
   "insurance paperwork", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE BIG PICTURE ----------
sc("""According to Insurify, the average annual cost of full coverage car insurance in America rose one percent in the first half of twenty twenty-six, to two thousand two hundred thirty-seven dollars. Insurify projects drivers will pay two thousand two hundred forty-two dollars a year by the end of twenty twenty-six.""",
   "car insurance", "1. US AVG FULL COVERAGE: $2,237")
sc("""Here is the first twist. Rates actually fell six percent in twenty twenty-five, according to Insurify. So the big shock of the early twenty twenties has slowed. But insurance is still far more expensive than it was a few years ago, and twenty twenty-six is moving up again. Insurify projected increases in thirty-two states by the end of the year.""",
   "insurance rates chart", "2025: -6%. 2026: RISING AGAIN")
sc("""Why? One big reason is repair costs. According to Insurify, auto maintenance and repair costs have risen forty-five percent in the past five years, about double the rate of inflation. Modern vehicles, and especially modern trucks, are full of sensors, cameras and computers. A minor collision that once needed a new bumper can now require calibrating radar and camera systems.""",
   "pickup truck repair shop", "REPAIR COSTS: +45% IN 5 YEARS")
sc("""Weather is another reason. According to Insurify, Kentucky saw about one hundred seventy-eight hail events per year from twenty twenty-three to twenty twenty-five, up from seventy-six per year from twenty twenty to twenty twenty-two. Hail damage is usually covered by full coverage insurance, and a big pickup has a lot of metal for hail to hit.""",
   "hail storm car damage", "HAIL EVENTS MORE THAN DOUBLED")
sc("""And location matters enormously. According to Insurify's June twenty twenty-six data, the most expensive places for full coverage were Washington, D C at three thousand eight hundred eighty dollars a year, Maryland at three thousand six hundred forty-six, Rhode Island at three thousand six hundred eleven, Michigan at three thousand two hundred twenty-nine, and Georgia at three thousand one hundred nine.""",
   "Washington DC traffic", "DC: $3,880. MARYLAND: $3,646")

# ---------- 2. TRUCK VS CAR ----------
sc("""Now the twist most people do not expect. Are trucks more expensive to insure than cars? According to Insurify's comparison, updated in June twenty twenty-six, full coverage for a full-size pickup averaged one hundred ninety-seven dollars a month, compared with two hundred forty-six dollars for a sedan and two hundred eight for an S U V, in its table.""",
   "pickup truck sedan", "2. TRUCKS VS CARS")
sc("""Why would a big truck cost less? Insurify gives several reasons. Trucks are popular in rural areas, where there are fewer drivers and less risk of accidents and theft. Body-on-frame construction can limit damage in some collisions. And few trucks appear among the most stolen vehicles, according to Insurify, which helps lower premiums.""",
   "pickup truck rural road", "WHY TRUCKS CAN COST LESS")
sc("""But here is the other side. According to Insurify, trucks can cost more when they are large and expensive to repair, when they have high sticker prices and top trims, when they are lifted or modified, or when they are used for business, which can require commercial coverage. So the average hides a huge range. The truck you choose decides which side of the average you land on.""",
   "lifted pickup truck", "WHY TRUCKS CAN COST MORE")

# ---------- 3. MOST EXPENSIVE ----------
# ---------- BRANDS & THEFT ----------
sc("""Brands matter too. According to Consumer Reports data based on Insurify's analysis of more than ninety million insurance quotes, reported by Ford Authority in August twenty twenty-six, Chevrolet was among the cheapest brands to insure, at an average of two thousand seven hundred four dollars a year. G M C averaged two thousand seven hundred eighty-six, and Ford two thousand eight hundred thirty-five. Subaru was the cheapest brand overall, at two thousand one hundred eighty-two.""",
   "Chevrolet Silverado GMC Sierra Ford F-150", "CHEVY $2,704. GMC $2,786. FORD $2,835")
sc("""According to the same report, the gap between the cheapest and the most expensive brand was around two thousand one hundred dollars a year. That is a huge difference, and it shows how much the vehicle you choose affects what you pay, even before your age and driving record come into play.""",
   "insurance quote comparison", "BRAND GAP: ~$2,100/YEAR")
sc("""Now theft, which is one of the hidden drivers of truck insurance. According to the National Insurance Crime Bureau, as reported by Ford Authority in March twenty twenty-six, the Chevrolet Silverado fifteen hundred was the fourth most stolen vehicle in America in twenty twenty-five, with sixteen thousand seven hundred sixty-four thefts. The Ford F-one-fifty was seventh, with ten thousand one hundred two.""",
   "Chevrolet Silverado 1500", "SILVERADO: #4 MOST STOLEN (16,764)")
sc("""Here is the twist. Total vehicle thefts in America fell twenty-three percent in twenty twenty-five, to six hundred fifty-nine thousand, eight hundred eighty, according to the same report, the biggest year-over-year drop in over forty years. That is good news for premiums over time. But full-size pickups are still among the most targeted vehicles, and their parts, like tailgates and catalytic converters, are valuable to thieves.""",
   "pickup truck parking lot night", "THEFTS DOWN 23%, TRUCKS STILL TARGETS")
sc("""So if you live in an area with high truck theft, expect that to show up in your quote. Anti-theft devices, a garage, and good lighting can help reduce risk, and some insurers offer discounts for approved anti-theft systems. Ask your insurer what counts before you spend money on any device.""",
   "garage pickup truck", "ANTI-THEFT CAN HELP")
sc("""So which trucks are the most expensive to insure? According to data from Insure dot com, the number one most expensive truck to insure in twenty twenty-six is the G M C Hummer E V truck, at four thousand one hundred eleven dollars a year. Number two is the Ram fifteen hundred T R X, at three thousand two hundred fifty-five.""",
   "GMC Hummer EV", "3. HUMMER EV: $4,111/YEAR")
sc("""After that come the Ford Super Duty at two thousand eight hundred fifteen dollars, the Ram heavy-duty at two thousand seven hundred fifty-nine, the Toyota Tundra Hybrid at two thousand seven hundred fifty-five, and the Ford F-one-fifty Lightning at two thousand seven hundred forty-three. The Ford F-one-fifty Raptor came in at two thousand six hundred eighty-two.""",
   "Ford F-150 Raptor", "TRX $3,255. LIGHTNING $2,743")
sc("""Do you see the pattern? Electric trucks, performance trucks and expensive heavy-duty trucks fill the list. The Hummer E V and the Lightning are expensive to repair, with large battery packs and specialized parts. The T R X and the Raptor are high-performance trucks with high prices and powerful engines. Insurers price the risk of paying for a very expensive repair.""",
   "electric truck battery", "EV + PERFORMANCE = EXPENSIVE")
sc("""And here is the twist. Some of these trucks are no longer even built. The Nissan Titan X D, at two thousand seven hundred six dollars, and the Nissan Titan, at two thousand six hundred forty-eight, are on the list, even though Nissan ended Titan production in twenty twenty-four. Discontinued trucks can be harder and more expensive to repair as parts become harder to find.""",
   "Nissan Titan XD", "TITAN: DISCONTINUED, STILL PRICEY")
sc("""The list also includes the Ford Ranger Raptor at two thousand six hundred thirty-seven dollars and the Chevrolet Silverado Z R two at two thousand five hundred seventy-five. Off-road performance versions of normal trucks often cost more to insure than the regular versions, because they cost more to buy and to fix, and because of how they tend to be driven.""",
   "Ford Ranger Raptor", "OFF-ROAD TRIMS COST MORE")

# ---------- 4. CHEAPEST ----------
sc("""Now the cheapest. According to a Compare dot com study reported by Pickup Truck Talk in August twenty twenty-six, the cheapest compact truck to insure was the Ford Maverick, at two thousand two hundred ninety-one dollars a year, with the Hyundai Santa Cruz right behind at two thousand two hundred ninety-six.""",
   "Ford Maverick", "4. MAVERICK: $2,291/YEAR")
sc("""Among midsize trucks, the Honda Ridgeline was cheapest at two thousand three hundred ninety-eight, followed by the Ford Ranger at two thousand four hundred thirteen. Among conventional full-size trucks, the Ford F-Series was cheapest at two thousand seven hundred sixty-six, followed by the Chevrolet Silverado at two thousand eight hundred five.""",
   "Honda Ridgeline", "RIDGELINE $2,398. F-SERIES $2,766")
sc("""Compare dot com economic analyst Julia Taliesin explained that compact and midsize trucks are cheaper to insure because larger, heavy-duty trucks can cause more damage in a collision. She added that the Maverick and Santa Cruz have light-duty, unibody designs, which bring their rates closer to sedans and S U Vs.""",
   "Hyundai Santa Cruz", "WHY SMALL TRUCKS ARE CHEAPER")
sc("""And now the strangest twist in the whole video. In the same study, the heavy-duty Ram thirty-five hundred averaged two thousand three hundred thirty-two dollars a year. That is cheaper than every midsize and full-size truck listed. The Toyota Tacoma, at two thousand seven hundred thirty-one, was the most expensive midsize truck in the study.""",
   "Ram 3500", "TWIST: RAM 3500 $2,332 VS TACOMA $2,731")
sc("""How is that possible? Taliesin said the result reflects differences in driver demographics, trims, geography, usage and insurer appetite in Compare dot com's dataset. Pickup Truck Talk noted that it does not mean larger trucks are inherently cheaper to insure. Heavy-duty trucks are often owned by older, experienced drivers who use them for towing, not for daily commuting. Who drives the truck matters as much as the truck.""",
   "Ram 3500 towing trailer", "WHO DRIVES IT MATTERS")
sc("""The Ram twenty-five hundred, by contrast, averaged three thousand thirty-three dollars in the same study, and the Silverado thirty-five hundred two thousand seven hundred eighty-nine. So even within heavy-duty trucks, the range is large. That is exactly why you should never assume a truck's insurance cost from its size.""",
   "Ram 2500", "RAM 2500: $3,033")

# ---------- 5. HIDDEN FACTORS ----------
sc("""Now the hidden factors that change your price. The first is the trim. Pickup Truck Talk noted that larger wheels, towing equipment and other options can change a truck's value and repair costs, so different versions of the same model can get different quotes. A base work truck and a top-trim luxury version of the same truck can have very different premiums.""",
   "pickup truck trims", "5. TRIM CHANGES THE PRICE")
sc("""Color and body style usually matter less than people think. Insurers focus on the vehicle's value, repair costs, safety data and theft rates, and on you as a driver. A red truck does not cost more to insure just because it is red. But a crew cab top trim with expensive LED lights and big wheels can cost more than a regular cab work truck of the same model.""",
   "red pickup truck", "COLOR? MOSTLY A MYTH")
sc("""The second is technology. Modern trucks are packed with cameras, radar and sensors for safety features. These features can help prevent crashes, which insurers like. But when a crash does happen, replacing and calibrating those systems is expensive. A cracked windshield on a truck with a camera behind it may need more than just new glass.""",
   "pickup truck windshield camera", "SAFETY TECH: HELPS AND HURTS")
sc("""The third is modifications. Lift kits, big wheels, aftermarket bumpers and performance parts can raise your premium, and if you do not tell your insurer about them, they may not be covered after a claim. Many truck owners discover this only after an accident. Always report modifications, and ask how each one affects your rate.""",
   "lifted truck big wheels", "REPORT YOUR MODS")
sc("""The fourth is use. If you use your truck for business, hauling for pay or carrying tools to job sites as a contractor, your personal policy may not cover it. According to Insurify, business use can require commercial auto coverage, which costs more. Using a personal policy for business use can lead to denied claims.""",
   "work truck job site", "BUSINESS USE = COMMERCIAL POLICY")
sc("""Towing is another detail worth checking. Your truck's insurance often covers liability when you tow a trailer, but damage to the trailer itself, or to what is on it, may need separate coverage. If you tow a boat, a camper or equipment, ask your insurer exactly what is covered before your first trip.""",
   "pickup truck towing camper", "WHAT DOES TOWING COVER?")
sc("""And the fifth is financing. If you lease or finance a truck, the lender usually requires full coverage, and often gap coverage, which pays the difference if the truck is totaled while you owe more than it is worth. With long loans becoming common, gap coverage matters more. According to Edmunds, twenty-five point five percent of new vehicle loans in the third quarter of twenty twenty-six were eighty-four months or longer.""",
   "car loan paperwork", "LONG LOANS = GAP COVERAGE")

# ---------- 6. ELECTRIC ----------
sc("""Electric trucks deserve their own section, because they are often the most expensive to insure. The Hummer E V leads the most expensive list at four thousand one hundred eleven dollars, and the Lightning is close to the top at two thousand seven hundred forty-three. Battery packs are expensive, and even moderate damage near the battery can lead an insurer to total the truck.""",
   "Ford F-150 Lightning", "6. EV TRUCKS: TOP OF THE LIST")
sc("""There is also the question of repair shops. Not every body shop is certified to work on electric truck batteries or aluminum-intensive bodies, like many Ford trucks. Fewer qualified shops can mean longer repairs and higher costs, and insurers include that in their prices. As more shops get certified, those costs may come down, but in twenty twenty-six they remain high.""",
   "auto body shop truck", "FEWER QUALIFIED SHOPS")
sc("""Here is the twist that links this to the market. The high cost of insuring and repairing electric trucks is one of the reasons buyers have been cautious. Ford ended production of the all-electric F-one-fifty Lightning in December twenty twenty-five, according to Fox Business. Insurance is part of the total cost of ownership, and electric pickups have struggled on that total.""",
   "Ford F-150 Lightning pickup", "INSURANCE IS PART OF THE COST")

# ---------- 7. HOW TO SAVE ----------
sc("""So how do you pay less? First, get insurance quotes before you choose the truck. Compare the exact trims you are considering. The difference between two trucks you like can be hundreds of dollars a year, and over five years, that can add up to more than the discount you negotiated at the dealer.""",
   "insurance quote laptop", "7. QUOTE BEFORE YOU BUY")
sc("""Second, shop your policy every year or two. Rates change, and loyalty is not always rewarded. Third, consider a higher deductible if you have savings to cover it. That can lower your premium. Fourth, ask about discounts: bundling with home insurance, safe driving programs, and low mileage. Many truck owners in rural areas drive less than they think.""",
   "insurance discounts", "SHOP, DEDUCTIBLE, DISCOUNTS")
sc("""Also think about telematics programs, where an app or device tracks your driving. Careful drivers can earn discounts, sometimes significant ones. But these programs record braking, speed and time of day, so drivers who often drive late at night or brake hard may not benefit. Read the program details before you sign up.""",
   "phone app driving", "TELEMATICS DISCOUNTS")
sc("""And check your coverage, not just your price. The cheapest policy may have low liability limits that leave you exposed if you cause a serious accident with a heavy truck. Pickups are heavy, and a collision can cause a lot of damage to another vehicle. Many experts suggest higher liability limits for truck owners for exactly that reason.""",
   "insurance policy document", "DON'T SKIMP ON LIABILITY")
sc("""And fifth, choose the truck with insurance in mind. If two trucks fit your needs, the one with a lower insurance cost, lower repair costs and less theft risk can save you money every single month. A Maverick, a Ranger or a Ridgeline might cost hundreds less per year to insure than a performance or electric truck. That is real money over the life of the truck.""",
   "Ford Ranger Honda Ridgeline", "CHOOSE WITH INSURANCE IN MIND")

# ---------- PATTERN ----------
sc("""Here is a simple example of how these choices add up. In the Compare dot com study, the Maverick averaged two thousand two hundred ninety-one dollars a year, while the Ram twenty-five hundred averaged three thousand thirty-three. That is a difference of about seven hundred forty dollars a year, or more than three thousand seven hundred dollars over five years. Insurance belongs in the price of the truck.""",
   "Ford Maverick Ram 2500", "$740/YEAR DIFFERENCE")
sc("""So what is the pattern? Truck insurance is not expensive because trucks are big. It is expensive when trucks are costly to repair, packed with technology, modified, used for work, or driven in high-risk places. Small, simple, popular trucks driven by experienced owners in quiet areas can be cheaper to insure than many cars.""",
   "pickup truck countryside", "WHAT REALLY DRIVES THE PRICE")
sc("""And here is the final twist. The biggest factor in your premium is not on any list in this video. It is you: your age, your driving record, your credit in many states, and where you park at night. The same truck can cost one driver half as much to insure as another. That is why your own quote is the only number that really matters.""",
   "driver pickup truck", "THE BIGGEST FACTOR IS YOU")

# ---------- CLOSE ----------
sc("""One more thing to know before you buy: insurance quotes are free and fast. Most insurers can give you a quote online in minutes if you have the vehicle identification number or the exact model and trim. There is no reason to wait until you are sitting in the finance office. A few quotes the night before you shop can change which truck you choose.""",
   "laptop insurance quote", "QUOTES ARE FREE AND FAST")
sc("""And when you renew, look at what changed. If your truck is older, its value has dropped, and you might not need the same collision coverage. If you moved, your rate may have changed. If your driving has improved, ask for a review. Insurance is not a set-and-forget bill. It is one of the easiest truck costs to lower.""",
   "insurance renewal", "REVIEW EVERY RENEWAL")
sc("""So here is your insurance checklist for twenty twenty-seven. First, get quotes on the exact trims you are considering, before you negotiate. Second, tell your insurer about modifications and business use. Third, consider gap coverage if you finance with a long loan or lease. Fourth, compare deductibles and discounts. And fifth, shop your policy again at every renewal.""",
   "insurance checklist", "YOUR INSURANCE CHECKLIST")
sc("""We put insurance, financing and all the other ownership costs into the Twenty Twenty-Seven Truck Buyer's Guide, so you can see the real cost of a truck before you buy it. The link is in the description and in the pinned comment. Subscribe for the next video, about five hidden costs of owning a truck. And tell us in the comments: how much do you pay to insure your truck? Thanks for watching.""",
   "pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Insuring one electric pickup": "Intro", "According to Insurify, the average annual": "1. The big picture in 2026",
      "Now the twist most people": "2. Trucks vs cars", "Brands matter too": "Brands and theft", "So which trucks are the most expensive": "3. Most expensive trucks to insure",
      "Now the cheapest.": "4. Cheapest trucks to insure", "Now the hidden factors": "5. The hidden factors",
      "Electric trucks deserve": "6. Electric trucks", "So how do you pay less?": "7. How to pay less",
      "So here is your insurance checklist": "Your checklist for 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video54", "length_scale": 1.4,
  "title": "Why Truck Insurance Costs So Much in 2026 (And the $4,111 Surprise)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
