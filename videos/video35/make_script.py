import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In twenty twenty-five, the Ford F-Series had a fire at its aluminum supplier, a record number of recalls, and a rival company that sold more full-size pickups. And it still finished as America's best-selling truck, for the forty-ninth year in a row. In twenty twenty-six, it is on track for fifty. How does one truck stay on top for half a century? The answer is not what most people think.""",
   "Ford F-150 2024", "49 YEARS AT #1")

# ---------- COLD OPEN ----------
sc("""Let's start with the scale. According to Ford, the F-Series sold eight hundred twenty-eight thousand, eight hundred thirty-two trucks in the United States in twenty twenty-five, including the electric Lightning, up eight point three percent. That is more than two thousand two hundred trucks every single day of the year.""",
   "Ford F-150 parking lot", "828,832 IN 2025")
sc("""And the streak is older than most of the people watching this video. According to Ford, the F-Series has been America's best-selling truck every year since nineteen seventy-seven, and the country's best-selling vehicle overall for more than four decades. Ford says it has sold more than thirty-three million F-Series trucks since nineteen seventy-seven.""",
   "1977 Ford F-150", "SINCE 1977: 33 MILLION+")
sc("""The F-150 itself turned fifty in twenty twenty-five, according to Ford. And Ford's president of Ford Blue, Andrew Frick, credited the streak to trust between Ford, its dealers and its customers. He said, quote, the enduring legacy of the F-Series is not just a result of our relentless pursuit of improvement. Keep that word, trust, in mind. It explains a lot of what follows.""",
   "Ford F-150 50th anniversary", "THE F-150 TURNED 50")
sc("""In this video, we look at the real reasons the F-Series stays on top, using sales reports, Ford's own data and independent reporting. Some of them are smart. Some are a little surprising. And a few show that the F-Series is not as untouchable as its streak suggests. Every number is sourced in the description.""",
   "Ford F-150 Raptor", "THE REAL REASONS")

# ---------- 1. THE TRICK IN THE NAME ----------
sc("""Reason one is the name itself, and it is also the first twist. The F-Series is not one truck. It is a family that, according to Ford, runs from the F-150 up through the Super Duty F-250, F-350 and beyond, up to the F-600. Ford counts all of them together. GM sells its trucks under two names, Chevrolet Silverado and GMC Sierra, and each brand counts separately.""",
   "Ford Super Duty F-350", "F-150 + SUPER DUTY = F-SERIES")
sc("""And here is what happens when you add GM's two trucks together. In twenty twenty-five, the Silverado sold five hundred seventy-seven thousand, four hundred thirty-four, and the Sierra three hundred forty-eight thousand, two hundred twenty-two, according to CarScoops. Together, nine hundred twenty-five thousand, six hundred fifty-six, more than the F-Series.""",
   "Chevrolet Silverado GMC Sierra", "GM COMBINED: 925,656")
sc("""In the fourth quarter of twenty twenty-five alone, Ford Authority reported that GM's combined full-size pickups outsold Ford by nearly forty-seven thousand trucks, with a forty-two percent share of the segment. So as a company, GM sells more full-size pickups than Ford. But as a single nameplate, the F-Series wins, and the title of best-selling truck goes to a nameplate.""",
   "Chevrolet Silverado 1500", "Q4 2025: GM 42% SHARE")
sc("""And the rest of the field in that quarter? Ram sold one hundred eleven thousand, six hundred seventy-three pickups, up six point nine percent. The Silverado sold one hundred fifty-four thousand, seven hundred forty-nine, up six point two. The Sierra sold ninety-six thousand, three hundred seventy-seven, up two point six. And the Toyota Tundra sold thirty-six thousand, six hundred sixty-five, down twelve point seven percent, according to Ford Authority. Every big American rival grew that quarter while the F-Series fell.""",
   "Ram 1500 2025", "Q4 2025: RAM +6.9%, TUNDRA -12.7%")
sc("""Even so, the F-Series held thirty-three percent of the full-size pickup segment in the fourth quarter, thirty-four including the Lightning, in a segment of six hundred eleven thousand, four hundred eighty trucks. One in three full-size pickups sold in America was a Ford F-Series, in a quarter Ford would describe as difficult.""",
   "Ford F-150 Lariat", "1 IN 3 FULL-SIZE PICKUPS")
sc("""That does not make the streak fake. It is a real number of real trucks. But it tells you something important. Part of Ford's advantage is simply that it puts its light-duty and heavy-duty trucks, from work trucks to luxury trims, under one powerful name. Every one of those trucks advertises the same badge.""",
   "Ford F-250 Super Duty", "ONE NAME, MANY TRUCKS")

# ---------- 2. SUPER DUTY ----------
sc("""Reason two, the heavy-duty trucks. In twenty twenty-five, Ford said Super Duty sales rose nine point five percent, the segment's best year since two thousand four. And in the third quarter of twenty twenty-six, Ford built one hundred ten thousand, two hundred seventy-five Super Duty trucks, its best quarterly result in nineteen years.""",
   "Ford Super Duty F-450", "SUPER DUTY: BEST IN 19 YEARS")
sc("""Super Duty trucks are the ones contractors, ranchers and fleets buy, often for towing and hauling that half-ton trucks cannot do. Ford has advertised Super Duty ratings of up to eight thousand pounds of payload and forty thousand pounds of towing, depending on configuration. And because they count inside the F-Series total, every one of them helps protect the streak.""",
   "Ford F-350 towing", "UP TO 40,000 LB TOWING")

# ---------- 3. BUSINESS CUSTOMERS ----------
sc("""And Ford builds trucks in huge volume. In the third quarter of twenty twenty-six, Ford said it produced two hundred sixty-six thousand, seven hundred seventy-seven F-Series trucks, up four point five percent. Production capacity matters. A dealer cannot sell a truck it does not have, and Ford's ability to fill dealer lots is a competitive weapon on its own.""",
   "Ford Kentucky Truck Plant", "Q3 2026: 266,777 BUILT")
sc("""Reason three is the customer most people never think about, businesses. Ford reported a forty-two point nine percent share of Class one through seven trucks and vans in twenty twenty-five, based on registration data, and forty-one percent in twenty twenty-six data through July. That category includes pickups and work vans used by companies and governments.""",
   "Ford Transit van", "41-43% OF COMMERCIAL TRUCKS & VANS")
sc("""Ford sells to businesses through its Ford Pro division. In twenty twenty-five, Ford said Ford Pro had roughly eight hundred forty thousand active paid software subscriptions, up about thirty percent in the fourth quarter. Those services help fleets track vehicles, maintenance and fuel. Here is the twist. Once a company's entire fleet runs on one maker's software, switching to another brand is harder.""",
   "Ford Pro fleet", "840,000 SOFTWARE SUBSCRIPTIONS")
sc("""The broader Ford work lineup backs this up. In twenty twenty-five, the Transit van sold a record one hundred sixty-one thousand, seven hundred ninety-seven, up five point nine percent. And through September twenty twenty-six, Ford said it sold eight hundred ninety-one thousand, four hundred trucks and vans, which it says makes it America's top truck manufacturer. A business that buys Ford vans often buys Ford pickups from the same dealer.""",
   "Ford Transit fleet", "891,400 TRUCKS + VANS (YTD 2026)")
sc("""And the work features keep coming. Ford's own list includes Pro Power Onboard, which turns the truck into a generator for tools, a Pro Access tailgate, BlueCruise hands-free highway driving, and towing aids. For someone who uses the truck to earn money, features like a built-in generator are not luxuries. They are reasons to stay loyal.""",
   "Ford F-150 Pro Power Onboard", "THE TRUCK IS A TOOL")

# ---------- 4. AN ENGINE FOR EVERYONE ----------
sc("""Reason four, choice. The F-Series offers gas and diesel engines, the PowerBoost hybrid, and until recently a fully electric Lightning. And the hybrid has quietly become a big business. In twenty twenty-five, Ford said F-150 Hybrid sales hit a record eighty-four thousand, nine hundred thirty-four, up fifteen percent.""",
   "Ford F-150 PowerBoost hybrid", "F-150 HYBRID: 84,934")
sc("""Through September twenty twenty-six, Ford reported thirty-four thousand, five hundred twenty-seven F-150 Hybrids sold. And across all its models, Ford sold a record two hundred twenty-eight thousand and seventy-two hybrids in twenty twenty-five. Here is the twist. While other brands bet on fully electric trucks, Ford's real electrified success was the hybrid most people never noticed.""",
   "Ford F-150 Platinum", "FORD HYBRIDS: 228,072")
sc("""Ford's Andrew Frick summed up the strategy in January twenty twenty-six. This past year proved that Ford has the right product and powertrain offering for the lives of our customers. Notice the phrase, powertrain offering. Ford does not ask buyers to choose between gas and electric. It lets them choose from almost everything, inside the same truck.""",
   "Ford F-150 engine bay", "\u201CTHE RIGHT POWERTRAIN OFFERING\u201D")
sc("""Not every bet worked. F-150 Lightning sales fell to twenty-seven thousand, three hundred seven in twenty twenty-five, down eighteen point five percent, and only four thousand, two hundred seventy-three in the fourth quarter, down sixty percent, according to Ford Authority. Ford discontinued the Lightning in December twenty twenty-five and plans an extended-range electric F-150 instead.""",
   "Ford F-150 Lightning", "LIGHTNING: -60% IN Q4 2025")
sc("""Ford CEO Jim Farley explained the problem to CNBC. The very high-end EVs, the fifty, seventy and eighty thousand dollar vehicles, just weren't selling. The Lightning Pro work version started at fifty-four thousand, seven hundred eighty dollars in twenty twenty-five, according to Equipment World. For a fleet buyer, that was a hard number to justify against a gas F-150.""",
   "Ford F-150 Lightning Pro", "\u201CJUST WEREN'T SELLING\u201D")
sc("""And yet the Lightning's failure barely dented the F-Series. Ford's gas and diesel F-Series grew nine point five percent to eight hundred one thousand, five hundred twenty-five trucks. That is the advantage of a huge lineup. When one version struggles, the others carry the total.""",
   "Ford F-150 XLT", "ICE F-SERIES: +9.5%")

# ---------- 5. PERFORMANCE AND PRICING ----------
sc("""And Ford's smaller trucks feed the same funnel. In twenty twenty-five, the Maverick sold a record one hundred fifty-five thousand and fifty-one, up eighteen point two percent, and the Ranger sold seventy thousand, nine hundred sixty, up fifty-three point six percent. Through September twenty twenty-six, Maverick Hybrid sales hit a record seventy-four thousand, three hundred. Many young buyers start with a Maverick and, years later, move up to an F-150.""",
   "Ford Maverick Hybrid", "MAVERICK: 155,051")
sc("""Reason five, the halo trucks. Ford reported its off-road performance lineup, including the Raptor and Tremor models along with Bronco SUVs, sold three hundred sixty-four thousand, one hundred forty-one vehicles through September twenty twenty-six, up eight point four percent. Raptor sales rose four point six percent, and Tremor-series sales were up one hundred twenty-two percent.""",
   "Ford F-150 Raptor R", "TREMOR SALES: +122%")
sc("""In October twenty twenty-six, Frick pointed to the same mix again, saying F-Series, Bronco and Ford's hybrid truck lineup were posting standout results. The Tremor numbers matter here. Tremor is an off-road package on regular F-150, Super Duty and Maverick trucks, so it brings some Raptor attitude to a truck that more people can afford.""",
   "Ford F-150 Tremor", "TREMOR: RAPTOR LOOK, LOWER PRICE")
sc("""Halo trucks like the Raptor sell in smaller numbers, but they make the whole lineup feel desirable. A buyer who cannot afford a Raptor may still buy an F-150 XLT, because it wears the same name. That is marketing that compounds over decades.""",
   "Ford F-150 Raptor 2024", "THE HALO EFFECT")
sc("""And here is a twist about price. In the third quarter of twenty twenty-six, Ford said the F-Series had the highest retail share and retail revenue among full-line truck brands, with the lowest incentive spending in the segment. In other words, Ford sold its trucks with the smallest discounts, and still led. That suggests the demand is real, not bought.""",
   "Ford F-150 dealership", "LOWEST INCENTIVES IN THE SEGMENT")
sc("""TFLcar's price comparison supports that. The popular F-150 XLT landed at fifty-two thousand, five hundred ninety dollars in twenty twenty-six, up six percent from twenty twenty-four, and slightly down when adjusted for inflation. The Silverado fifteen hundred LT rose twelve point six percent over the same period, to fifty-six thousand, two hundred ninety. Ford's core trim stayed relatively competitive.""",
   "Ford F-150 XLT 2025", "F-150 XLT: $52,590")

# ---------- 6. THE CRACKS ----------
sc("""Now the cracks, because the streak hides some real problems. In September twenty twenty-five, a fire broke out at the Novelis aluminum plant in Oswego, New York, which supplies much of the aluminum used in the F-150, according to Pickup Truck plus SUV Talk. Novelis supplies roughly forty percent of the aluminum sheet used by U.S. automakers, and Ford is its biggest customer.""",
   "aluminum sheet coils factory", "NOVELIS FIRE: SEPT 16, 2025")
sc("""Analysts at Evercore ISI expected Ford to lose about one billion dollars, and Ford's stock fell six percent the day after the fire was announced. The plant was expected to stay shut until the first quarter of twenty twenty-six, according to Reuters reporting cited in the article. And importing replacement aluminum was expensive because of a fifty percent tariff on aluminum imports.""",
   "Ford Dearborn Truck Plant", "~$1 BILLION HIT")
sc("""The fire was serious. It broke out around ten p.m. on September sixteenth, twenty twenty-five, and firefighters from more than twenty departments needed over four hours to put it out, according to Pickup Truck Talk. The fire mostly destroyed the roof of the one point four million square foot plant. And in November twenty twenty-five, Insurance Journal reported another fire at the same Novelis plant.""",
   "industrial fire night", "20+ FIRE DEPARTMENTS, 4+ HOURS")
sc("""Evercore called it, quote, largely a Ford issue, because other automakers use Novelis aluminum for parts like hoods, doors and tailgates, but Ford relies on it for the F-150's whole body. That is the hidden cost of being so big. When the best-selling truck in America depends on one plant, one fire can show up in national sales numbers.""",
   "Ford F-150 body shop", "\u201CLARGELY A FORD ISSUE\u201D")
sc("""Here is the twist. The F-150's aluminum body, which Ford adopted to cut weight, became a supply chain weakness. In the fourth quarter of twenty twenty-five, F-Series sales fell three percent, while the Silverado rose six point two percent, and Ford Authority pointed to the Novelis fire as part of the reason. Ford's spokesperson said Novelis is one of several aluminum suppliers to Ford.""",
   "Ford F-150 aluminum body", "Q4 2025: F-SERIES -3%")
sc("""The second crack is quality. Ford issued one hundred fifty-three recalls in twenty twenty-five, according to Ford Authority, citing federal data. That was one hundred more than second-place Stellantis, and far above the previous calendar-year record of seventy-seven, set by General Motors in twenty fourteen. Ford passed that old record by July.""",
   "Ford F-150 recall", "153 RECALLS IN 2025")
sc("""Rearview camera problems were a big part of it. Ford Authority noted that Ford recalled millions of vehicles over that single feature. And GM, the company that held the old record, had only twenty-seven recalls in twenty twenty-five, placing it fourth behind Ford, Stellantis and the RV maker Forest River.""",
   "Ford F-150 backup camera screen", "GM: 27 RECALLS. FORD: 153.")
sc("""Not all of those recalls involved trucks, and many were software or camera fixes. But it is a strange combination. The best-selling truck in America comes from the brand with the most recalls in America. It shows that buyers are loyal enough to keep buying through problems, and it is also a warning to check every recall on any Ford you buy.""",
   "Ford F-150 rear camera", "MOST POPULAR + MOST RECALLS")
sc("""And the third crack is supply. At the end of September twenty twenty-six, Ford said a supplier issue affected F-150 production, though it said the impact was containable within its financial guidance. When you build more than eight hundred thousand trucks a year, any single supplier problem can cost tens of thousands of trucks.""",
   "Ford truck assembly line", "ONE SUPPLIER CAN STOP THOUSANDS")

# ---------- 7. THE THREAT ----------
sc("""So why do buyers keep coming back, despite the recalls and the supply problems? The sales data cannot measure loyalty directly. But the pattern is clear. Ford sold more F-Series trucks in twenty twenty-five than in twenty twenty-four, even as it set a record for recalls, and in twenty twenty-six it sold with the smallest incentives in the segment. Whatever buyers feel about the F-Series, it is strong enough to survive bad news.""",
   "Ford F-150 owners", "LOYALTY SURVIVES BAD NEWS")
sc("""So can anyone end the streak? Through September twenty twenty-six, Ford reported five hundred sixty-one thousand, five hundred eight F-Series sales, more than one hundred forty thousand ahead of the Chevrolet Silverado. And Ford said the F-Series remains on track for a fiftieth consecutive year as America's best-selling truck. For twenty twenty-six, the answer looks like no.""",
   "Ford F-150 2026", "2026: 140,000+ AHEAD OF SILVERADO")
sc("""But twenty twenty-seven is different. GM launched redesigned Silverado and Sierra trucks with two new V8s, and GM told investors it aims to build about two million full-size trucks and SUVs in twenty twenty-seven. Ram is adding the Rumble Bee SRT and the range-extended Ram fifteen hundred REV. And the next all-new F-150, which some reports said was planned soon, could face delays after the aluminum fire, according to Pickup Truck Talk.""",
   "Chevrolet Silverado 2027", "2027: GM RELOADS")
sc("""And the market itself is shifting. Midsize trucks grew twenty-four percent in twenty twenty-five, and the Tacoma had its best year ever, according to TFLtruck. The Maverick is pulling buyers who might once have bought a base F-150. Ford owns two of those smaller trucks, the Maverick and the Ranger, so even if buyers move down a size, Ford keeps many of them. But those sales do not count toward the F-Series streak.""",
   "Toyota Tacoma Ford Maverick", "BUYERS ARE MOVING DOWN A SIZE")
sc("""Here is the twist. The real threat to the F-Series is not one truck. It is GM's two-brand strategy getting stronger. If GM keeps outselling Ford as a company while Ford wins only as a nameplate, the streak will keep going, but the argument about who really sells the most trucks will get louder every year.""",
   "GMC Sierra 2027", "THE TWO-BRAND THREAT")

# ---------- 8. WHAT IT MEANS FOR BUYERS ----------
sc("""Canada tells the same story. Ford Authority reported one hundred thirty-eight thousand, four hundred seventy F-Series trucks sold in Canada in twenty twenty-five, and almost fourteen thousand in Mexico, up about eight percent. The F-Series is not just an American habit. It is a North American one, and that extra volume helps Ford spread the cost of developing the truck.""",
   "Ford F-150 snow Canada", "CANADA: 138,470")
sc("""So what does this mean if you are buying a truck? First, popularity has real advantages. A truck that sells eight hundred thousand a year has parts and repair knowledge everywhere, and a huge used market. Second, popularity is not the same as reliability. As we covered in our reliability video, the studies disagree on which truck brand is most reliable, and Ford led the industry in recalls in twenty twenty-five.""",
   "Ford F-150 used", "POPULAR ≠ MOST RELIABLE")
sc("""Third, because the F-Series sells with the lowest incentives in the segment, according to Ford, you may find bigger discounts on its rivals. If you are shopping on price, get quotes on a Silverado, Sierra and Ram as well. And fourth, check how a supply problem affected the truck you are buying, especially any truck built around the time of the aluminum shortage.""",
   "Ram 1500 Silverado F-150", "SHOP ALL THREE")

# ---------- CLOSE ----------
sc("""So how does the F-Series stay on top? One name that covers everything from the F-150 to Super Duty. Dominance with businesses and fleets. An engine for everyone, including a hybrid that quietly sold eighty-five thousand trucks. Halo trucks like the Raptor. And demand strong enough to sell with the smallest discounts in the segment. Not even a fire, a record recall year and a failed electric truck could stop it.""",
   "Ford F-Series lineup", "HOW IT STAYS ON TOP")
sc("""And the final twist. The F-Series is America's best-selling truck, but Ford is not America's biggest full-size pickup seller, GM is, when you add its two brands. Both statements are true. The streak is a triumph of product, and also a triumph of how you count. Fifty years in, that may be the smartest decision Ford ever made.""",
   "Ford F-150 2025 sunset", "BOTH STATEMENTS ARE TRUE")
sc("""We put a full-size truck buying checklist, with the recall checks for the F-150, Silverado, Sierra and Ram, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we look at which truck companies are betting on hybrids. And tell us in the comments, could anything end the F-Series streak? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In twenty twenty-five, the Ford F-Series had": "Intro", "Reason one is the name": "Reason 1: The name", "Reason two, the heavy-duty": "Reason 2: Super Duty",
      "Reason three is the customer": "Reason 3: Businesses and fleets", "Reason four, choice": "Reason 4: An engine for everyone",
      "Reason five, the halo": "Reason 5: Halo trucks and pricing", "Now the cracks": "The cracks: fire, recalls, supply",
      "So can anyone end the streak": "Can anyone end the streak?", "So what does this mean": "What it means for buyers", "So how does the F-Series": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video35", "length_scale": 1.4,
  "title": "How the F-150 Stays No. 1 for 50 Years (Even Though GM Sells More Trucks)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
