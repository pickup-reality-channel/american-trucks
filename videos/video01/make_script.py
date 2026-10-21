import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- COLD OPEN ----------
sc("""Americans bought more pickup trucks last year than almost anything else on four wheels. Ford sold eight hundred one thousand, five hundred twenty-five F-Series trucks in twenty twenty-five. Chevrolet sold five hundred seventy-seven thousand Silverados. Ram sold three hundred seventy-four thousand. By every measure, the pickup is the most powerful product in the American car business. So here is the question nobody is asking. If trucks are selling like this, why are seven of them being abandoned?""",
   "Ford F-150 pickup truck", "2025: F-SERIES 801,525 SOLD")
sc("""The answer is not what you think. It is not quality. It is not reliability. In most of these cases, the trucks were not even bad. They were caught in the middle of the biggest bet the auto industry has made in decades, and that bet is now being rewritten in public, with billions of dollars attached.""",
   "Chevrolet Silverado 1500 pickup", "SILVERADO 2025: 577,434")
sc("""Stay with me for the next twenty-two minutes, because there is a twist in every one of these stories. One truck was killed by a partner's factory sale. One was cancelled after four delays. One outsold its famous rival and was cancelled anyway. And one is not even built by the company on the badge. By the end, you will know exactly what to check before you sign for a truck in twenty twenty-seven.""",
   "Ram 1500 pickup truck", "7 TRUCKS. 7 TWISTS.")
sc("""Before we start, a quick note on how this channel works. Every number you hear comes from a published source, and the sources are listed in the description. If a figure could not be confirmed, we left it out. Truck buying is expensive, and you deserve facts, not rumors. Let's begin with the truck that is already gone.""",
   "Ford F-250 Super Duty pickup", "EVERY NUMBER IS SOURCED")

# ---------- 1. NISSAN TITAN ----------
sc("""Truck number one is the Nissan Titan. In August of twenty twenty-three, a Nissan spokesman confirmed to Motor Authority that the Titan would end after the twenty twenty-four model year. Production at the plant in Canton, Mississippi, was scheduled to stop in the middle of twenty twenty-four. Not a recall. Not a scandal. A quiet announcement that one of the only full-size pickups from a Japanese brand was finished.""",
   "Nissan Titan Pro-4X pickup", "TITAN: ENDED AFTER 2024")
sc("""Now look at the number that explains why. In twenty twenty-two, Nissan sold fifteen thousand, sixty-three Titans in the United States. That sounds like a lot until you compare it. It was a drop of forty-five percent from the year before. And Motor Authority noted that twenty twenty-three was not on track to do much better. For a truck, that is not a slump. That is a collapse.""",
   "Nissan Titan XD", "2022: 15,063 SOLD (-45%)")
sc("""Here is the first twist. Compare that Titan number with the biggest truck in the country. In twenty twenty-five, the Ford F-Series sold more than fifty times as many trucks as the Titan sold in twenty twenty-two. Same country, same kind of buyer, same kind of truck. One sells every few minutes of every day. The other was selling a few dozen a day.""",
   "Ford F-150 XLT pickup", "F-SERIES: 50X THE TITAN")
sc("""So what happened to the people who wanted a Titan? Mostly, they did not exist in large numbers. Full-size truck buyers are often loyal to a brand, to what their dealer stocks, and to what their friends can fix. A newcomer has to be dramatically better, or dramatically cheaper, to break that habit. The Titan was neither, and buyers did the math.""",
   "Nissan Titan pickup front", "LOYALTY BEATS NEW")
sc("""And here is the second twist. The Canton plant did not close. According to Motor Authority at the time, Nissan said no job losses were planned and that the plant would be retooled for electric vehicles. Two electric models, one for Nissan and one for Infiniti, were to be built there. A truck plant was being converted into an electric car plant, and that tells you where the whole industry was heading.""",
   "Nissan crew cab pickup", "CANTON PLANT: RETOOLED FOR EVS")
sc("""That plan is the thread that connects most of the trucks in this video. In twenty twenty-three and twenty twenty-four, nearly every automaker was racing to build electric trucks. And the next truck on our list is the one that raced the longest, and never crossed the finish line.""",
   "Nissan Titan Extended Cab", "NEXT: THE TRUCK THAT NEVER SHIPPED")

# ---------- 2. RAM 1500 REV ----------
sc("""Truck number two is the all-electric Ram 1500 REV. On September twelfth, twenty twenty-five, Stellantis announced that it would discontinue development of a full-size battery-electric pickup. The reason, in the company's own words, was slowing demand for full-size battery-electric trucks in North America. A truck that people had been waiting years for was officially dead before a single customer got one.""",
   "Ram 1500 TRX", "SEPT 12, 2025: REV CANCELLED")
sc("""Look at the timeline, because it tells the story better than any headline. The electric Ram debuted as a concept in early twenty twenty-three. Then the launch was pushed to twenty twenty-five. Then to early twenty twenty-six. Then to the middle of twenty twenty-seven. And then, in September of twenty twenty-five, it was pushed to never. Four dates, four delays, one cancellation.""",
   "Ram 1500 Rebel", "4 DELAYS, THEN NEVER")
sc("""Why did it fall apart? Reporting from InsideEVs points to several things at once. Demand for large electric trucks was slowing. Stellantis was struggling with its electric Dodge and Jeep models, which were poorly received and had weak range and charging. Batteries are expensive. And a truck that has to tow and haul heavy loads is the hardest possible job for a battery, because towing cuts range sharply.""",
   "Ram 1500 Laramie", "WHY: DEMAND, COST, TOWING")
sc("""There is a detail in that reporting that most people missed. The article says there are no fuel economy regulations pushing Stellantis to build electric trucks, which lets the company ease off. Think about what that means. A lot of the electric truck push was never driven by buyers asking for it. It was driven by rules and by hope. When the rules loosened, the hope got expensive.""",
   "Ram pickup truck", "THE REAL DRIVER: RULES, NOT BUYERS")
sc("""Now the twist. The name did not die. The Ramcharger, a truck that uses a gas V6 engine to recharge its battery, was scheduled to go on sale in twenty twenty-six, and Stellantis said it would be renamed the Ram 1500 REV. Same badge, completely different idea. The truck that was going to replace the gas engine now depends on a gas engine to work.""",
   "Ram 1500 pickup 2025", "SAME NAME, OPPOSITE IDEA")
sc("""Ram called the Ramcharger a new benchmark in the half-ton segment for range, towing and payload. Whether it earns that claim is a question for the numbers once it sells. But notice the pattern, because it is about to repeat. When a pure electric truck failed to find buyers, the answer was not to give up on electrification. It was to put a gas engine back in the picture. Hold that thought, because the next truck follows the same script.""",
   "Ram 1500 truck", "A BENCHMARK, OR A RETREAT?")

# ---------- 3. FORD F-150 LIGHTNING ----------
sc("""Truck number three is the Ford F-150 Lightning, and this is the one that surprises people. Ford announced in December of twenty twenty-five that it was ending production of the all-electric F-150 Lightning. Not shrinking it. Ending it. And it came with a number that stopped the industry cold. Ford said it would take a nineteen point five billion dollar charge on its electric vehicle assets and product plans.""",
   "Ford F-150 Lightning", "DEC 2025: LIGHTNING ENDS")
sc("""Nineteen point five billion dollars. About five and a half billion of that is cash, mostly paid in twenty twenty-six, with the rest in twenty twenty-seven. To give you a sense of scale, the Wall Street Journal reported that Ford has lost around thirteen billion dollars on electric vehicles since twenty twenty-three. The Lightning was a hit by the standards of electric trucks. And it still could not make the math work.""",
   "Ford F-150 Lightning charging", "$19.5 BILLION CHARGE")
sc("""Here is the twist inside the twist. The Lightning was not a failure in the showroom, compared with its rivals. Sales peaked in twenty twenty-four at thirty-three thousand, five hundred ten. In twenty twenty-five, Electrek reported about twenty-seven thousand, three hundred, down roughly eighteen percent. Meanwhile, Cox Automotive estimated about twenty thousand, two hundred Cybertrucks sold in the United States. So the Lightning outsold the Cybertruck, and was cancelled anyway.""",
   "Ford F-150 Lightning pickup", "LIGHTNING OUTSOLD CYBERTRUCK")
sc("""Put those numbers next to the truck it was built on. About twenty-seven thousand Lightnings, against more than eight hundred thousand F-Series trucks. That is roughly three percent. The best-selling electric truck from the best-selling truck brand in America was a rounding error inside its own family. That is the real lesson of the Lightning. Even the strongest name in trucks could not turn electric into a mass-market pickup.""",
   "Ford F-150 pickup truck", "ABOUT 3% OF F-SERIES")
sc("""Ford's chief executive, Jim Farley, explained it in plain language. He said Ford would rather not spend billions more on large electric vehicles that have no path to profitability. And he added that hybrids are more than just economical now, and have been more popular than the company ever expected. Hybrids are now thirty percent of Ford's sales mix, and Ford said hybrid sales rose thirty percent in the most recent month while overall sales were flat.""",
   "Ford F-150 Raptor", "FARLEY: HYBRIDS ARE WINNING")
sc("""So what replaces it? A next-generation Lightning built as an extended-range electric vehicle, an EREV, where a gas engine acts as a generator for the battery. Ford estimates it could add up to seven hundred miles or more of total range. It is planned for the Rouge Electric Vehicle Center in Dearborn, with launch timing to be announced. Ford also expects about half of its global volume to be hybrids, EREVs and EVs by twenty thirty, up from seventeen percent in twenty twenty-five.""",
   "Ford Rouge Complex Dearborn factory", "NEXT LIGHTNING: GAS-ASSISTED")
sc("""If you are keeping score, that is two of our seven trucks, from two of the three biggest truck companies in America, where the electric version was cancelled and the answer was a gas engine helping out. Now watch what happens at the third big player, General Motors, because its story is not told by a sales chart. It is told by a factory.""",
   "Ford F-150 pickup", "NEXT: GM'S EV TRUCK FACTORY")


# ---------- 4. HUMMER EV / FACTORY ZERO ----------
sc("""Truck number four is the GMC Hummer EV pickup, and its story is easier to see in a factory than in a sales report. The Hummer EV, along with the Sierra EV, the Chevrolet Silverado EV and the Cadillac Escalade IQ, is built at a single General Motors plant called Factory Zero. It was built to be the home of GM's electric trucks. So when that plant slows down, it tells you what is happening to demand.""",
   "GMC Hummer EV", "FACTORY ZERO: GM'S EV TRUCK PLANT")
sc("""Here is the timeline, as InsideEVs reported it. In October of twenty twenty-five, GM cut one of the plant's two shifts, which roughly halved its output, and permanently laid off twelve hundred workers. Not a temporary pause. Permanent. A company does not take that step when it expects demand to bounce back next week.""",
   "GMC Hummer EV pickup", "OCT 2025: 1,200 JOBS CUT")
sc("""Then came the pauses. From October twenty-seventh to November twenty-fourth, twenty twenty-five, the plant was temporarily idled. Then, according to the union, a second pause began on March sixteenth, with workers expected back on April thirteenth, about four weeks. The remaining thirteen hundred workers were placed on temporary layoff. That is two shutdowns in about five months at the plant built for the electric truck future.""",
   "Chevrolet Silverado EV", "TWO SHUTDOWNS IN 5 MONTHS")
sc("""GM's explanation was short. A spokesperson said Factory Zero would temporarily adjust production to align electric vehicle production with market demand. Read that sentence slowly. The company is not saying the trucks are bad. It is saying there are more being built than people want to buy. And in the car business, that gap is the most expensive problem there is.""",
   "GMC Sierra EV", "\"ALIGN PRODUCTION WITH DEMAND\"")
sc("""Now, one honest note. None of the sources we used publish a sales number for the Hummer EV pickup alone, so we will not invent one. What we can say, with sources, is what the plant did: it cut a shift, laid off workers, and paused twice. Those are decisions, not guesses. When a manufacturer changes its factory schedule this fast, it is reading demand more accurately than any outside analyst can.""",
   "Cadillac Escalade IQ", "NO HUMMER NUMBER? WE WON'T GUESS")
sc("""Here is the twist. The Hummer EV is one of the most capable electric trucks ever built, and that is exactly the problem for its buyers. It is a very expensive truck in a market where buyers are suddenly cautious about expensive electric trucks. Great engineering does not fix a demand problem. And the next truck on our list has the opposite issue. Nothing is wrong with it. It is not electric at all. And it was not even built by the company on its badge.""",
   "GMC Hummer EV pickup -H2 -\"Hummer H2\"", "GREAT ENGINEERING, SMALL AUDIENCE")

# ---------- 5. SILVERADO MEDIUM DUTY ----------
sc("""Truck number five is the biggest Chevrolet Silverado you have probably never noticed. The Silverado four thousand five hundred HD, fifty-five hundred HD and sixty-five hundred HD. These are the medium-duty work trucks, the kind you see hauling equipment, running as tow rigs, and working for small businesses. And according to Motor1 and GM Authority, their production ended on September thirtieth, twenty twenty-six.""",
   "Chevrolet Silverado 4500HD", "SILVERADO MD: ENDED SEPT 30, 2026")
sc("""Here is the twist. General Motors never built them, and neither of the last two electric stories explains this one. These trucks were built by International Trucks at its plant in Springfield, Ohio, under a manufacturing agreement with GM. The Silverado medium-duty line launched for the twenty nineteen model year. It was a Chevrolet on the badge and an International truck underneath, and the end of that agreement is what ended the trucks.""",
   "Chevrolet Silverado HD pickup", "BADGE: CHEVY. BUILDER: INTERNATIONAL")
sc("""The partner side of the story is straightforward. International announced on March thirtieth that it was selling its Ohio factory. Once the factory changed hands, the manufacturing agreement was not going to continue. GM's statement made clear that production would end after the agreement concluded on September thirtieth. The Motor1 report put it bluntly, saying GM did not really have a choice.""",
   "International truck", "INTERNATIONAL SOLD THE OHIO PLANT")
sc("""The sales numbers explain why nobody fought to save them. In twenty twenty-four, GM sold ten thousand, three hundred nineteen of these medium-duty trucks in the United States. In twenty twenty-five, eight thousand, three hundred forty-one, a drop of nineteen point two percent. And through March of twenty twenty-six, only one thousand, two hundred seventy-three, down thirty-seven point four percent from the same stretch a year earlier.""",
   "Chevrolet Silverado 6500HD", "2025: 8,341 (-19.2%)")
sc("""Compare those figures with the half-ton Silverado, which sold more than five hundred seventy-seven thousand. Medium-duty trucks are a niche. A niche tied to a partner is fragile, and when the partner moved, there was nothing underneath to hold the program up. This is a very different failure from the Titan or the Lightning. Nobody stopped wanting these trucks. The structure that built them went away.""",
   "Chevrolet Silverado pickup", "A NICHE WITH ONE FRAGILE PARTNER")
sc("""What happens next? GM says it is evaluating future portfolio options for medium-duty trucks. GM Authority cites unnamed sources saying a next-generation Silverado medium-duty is taking shape, reportedly built on the coming Silverado HD architecture and developed in-house, possibly around the twenty twenty-nine model year. That is reporting, not confirmation, so treat it as a possibility. For now, if you want a new one, they are gone.""",
   "Chevrolet Silverado HD", "NEXT-GEN: REPORTED, NOT CONFIRMED")


# ---------- 6. HYUNDAI SANTA CRUZ ----------
sc("""Truck number six is the Hyundai Santa Cruz, the small pickup from a Korean brand that is built in Alabama. And here we have to be careful, because this one is reported, not confirmed. Automotive News, citing unnamed sources, reported that Hyundai plans to cut and eventually end Santa Cruz production, with no direct replacement. Hyundai declined to confirm it, and said it does not comment on future product speculation.""",
   "Hyundai Santa Cruz", "REPORTED: SANTA CRUZ PHASE-OUT")
sc("""Why would a company do that? Look at the numbers The Autopian reported. In twenty twenty-five, Ford sold one hundred fifty-five thousand, fifty-one Mavericks. Hyundai sold twenty-five thousand, four hundred ninety-nine Santa Cruzes. The Maverick outsold it six to one. Same kind of truck, same kind of buyer. And Hyundai dealers had nearly five months of supply sitting in stock at the end of the year.""",
   "Ford Maverick", "MAVERICK 155,051 VS SANTA CRUZ 25,499")
sc("""The Autopian also compared the two directly. The Maverick gets thirty-eight miles per gallon combined, against twenty-five for the Santa Cruz. The Maverick's bed is four and a half feet long, against four feet. And the Maverick started at twenty-nine thousand, eight hundred forty dollars including destination, against thirty-one thousand, three hundred fifty for the Santa Cruz. Cheaper, thriftier and with a longer bed. That is not a fair fight.""",
   "Ford Maverick pickup", "MAVERICK: CHEAPER, THRIFTIER, LONGER BED")
sc("""One source said production was originally planned to continue through the second quarter of twenty twenty-seven and is now expected to end sooner. Another said Hyundai told suppliers it was cutting Santa Cruz production by roughly half in that quarter. These are unnamed sources, so treat them as strong signals rather than facts. But they match the sales gap almost perfectly.""",
   "Hyundai Santa Cruz pickup", "PRODUCTION CUT BY ROUGHLY HALF")
sc("""Here is the twist. The Santa Cruz is built at Hyundai's plant in Montgomery, Alabama, alongside the Tucson, which sold more than two hundred thousand last year, up fourteen percent. Automotive News noted that ending the Santa Cruz would free up space there. In other words, the factory has a better use for the room. Hyundai said the truck helped the company gain valuable experience and visibility in the open-bed market.""",
   "Hyundai Tucson", "ENDING IT FREES UP FACTORY SPACE")
sc("""And Hyundai is not leaving trucks. It confirmed a new midsize body-on-frame pickup, due in the United States before twenty thirty, which Automotive News reportedly places at twenty twenty-nine. So the company is not quitting the pickup market. It is changing what kind of pickup it wants to sell. The lesson for a buyer is simple. Learning about a model before it vanishes is cheaper than learning after.""",
   "Hyundai pickup truck", "HYUNDAI IS NOT QUITTING TRUCKS")

# ---------- 7. CYBERTRUCK ----------
sc("""Truck number seven is the one everybody has an opinion about. The Tesla Cybertruck. And let us be careful here, because the Cybertruck has not been cancelled. It is still for sale. But its sales tell a story that belongs on this list, because the distance between what was promised and what happened is one of the largest in recent automotive history.""",
   "Tesla Cybertruck", "NOT CANCELLED. BUT LOOK AT THIS.")
sc("""Cox Automotive estimates, reported by InsideEVs, say Americans bought about twenty thousand, two hundred Cybertrucks in twenty twenty-five. In twenty twenty-four, it was close to thirty-nine thousand. That is nearly cut in half, a drop of roughly nineteen thousand trucks. According to the analysis, it was the steepest sales drop of any electric vehicle in the country in twenty twenty-five, by volume.""",
   "Tesla Cybertruck front", "2024: ~39,000 → 2025: ~20,200")
sc("""Now put that against the promise. Reporting from Pickup Truck Talk notes that Elon Musk once floated a volume of half a million Cybertrucks a year. Half a million. The truck is selling at a tiny fraction of that number. This is not an attack. It is arithmetic. A product designed and marketed for enormous volume is selling like a niche vehicle.""",
   "Tesla Cybertruck rear", "PROMISED: 500,000 A YEAR")
sc("""There were other signals. Electrek reported that Tesla confirmed Cybertruck sales fell to about five thousand units in the second quarter of twenty twenty-five. In September of twenty twenty-five, Tesla discontinued the cheapest Cybertruck trim only months after launching it. And in the final quarter, the Autopian reported that companies owned by Elon Musk bought nearly one in five of the Cybertrucks Tesla sold.""",
   "Tesla Cybertruck Gigafactory Texas", "CHEAPEST TRIM DROPPED IN SEPT 2025")
sc("""Here is the twist that keeps the Cybertruck on this list for the right reason. The sales gap is not a verdict on the engineering. It is the gap between a forecast and a market. A product can be famous, discussed everywhere, and still sell to a much smaller audience than its maker predicted. Fame sells headlines. It does not automatically sell trucks.""",
   "Tesla Cybertruck pickup", "FAME ISN'T THE SAME AS SALES")
sc("""To be fair, the Cybertruck still has something Ford and Ram could not keep. It is still in production, and Tesla has not announced an end. The EV pickup market is smaller than anyone predicted, but the Cybertruck can survive on a smaller scale. Pickup Truck Talk reports that the Model 3 and Model Y made up ninety-seven percent of Tesla's volume. The company does not depend on the truck. That is a very different position from a company that needed its truck to be a hit.""",
   "Tesla Cybertruck", "STILL IN PRODUCTION")

# ---------- CLOSE ----------
sc("""So what is the pattern across all seven? Four of them are electric trucks, or were planned to be. One was a Japanese brand's full-size truck that never found enough buyers. One was a medium-duty truck that depended on a partner who sold the factory. One is a small Korean-brand pickup beaten six to one by a cheaper rival. Different problems, same lesson. A truck is not just a vehicle. It is a bet on a factory, a partner, a battery, and a buyer, and any one of them can break.""",
   "Ford F-150 Chevrolet Silverado pickups dealership lot", "THE PATTERN: A TRUCK IS A BET")
sc("""That matters for you, because buying a truck is a long commitment. Here is what to check before you sign in twenty twenty-seven. First, look at the sales trend of the exact model, not just the brand. A truck whose sales are falling year after year is a warning sign for resale value and parts support. Second, find out who actually builds it, and whether a partner or a factory change could end it.""",
   "Ford F-150 pickup", "CHECK 1 AND 2: TREND AND BUILDER")
sc("""Third, ask what the warranty and service plan look like if the model is discontinued. A warranty normally stays valid on a discontinued model, but get that in writing, because parts and dealer attention can fade. Fourth, compare the full cost, not just the sticker. Charging, fuel, insurance and what the truck will be worth in five years all belong on the same page. A cheap truck nobody wants can be the most expensive one you ever owned.""",
   "Chevrolet Silverado 1500", "CHECK 3 AND 4: WARRANTY AND TOTAL COST")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we just walked through. The link is in the description and in the pinned comment. And if you want to see which trucks are actually worth buying next, subscribe, because the next video covers exactly that. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Americans bought more pickup": "Intro", "Truck number one": "1. Nissan Titan", "Truck number two": "2. Ram 1500 REV",
      "Truck number three": "3. Ford F-150 Lightning", "Truck number four": "4. GMC Hummer EV and Factory Zero",
      "Truck number five": "5. Chevrolet Silverado medium-duty", "Truck number six": "6. Hyundai Santa Cruz",
      "Truck number seven": "7. Tesla Cybertruck", "So what is the pattern": "What to check before you buy in 2027"}
for sc_ in S:
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video01",
  "title": "7 Pickups Americans Are Walking Away From Before 2027 (The Real Reasons)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words ~", round(words/150, 1), "min")
