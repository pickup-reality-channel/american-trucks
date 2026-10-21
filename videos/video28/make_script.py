import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In one study, the Toyota Tundra had a forty-seven point nine percent chance of reaching two hundred fifty thousand miles. In the newest version of the same study, published in September twenty twenty-six, it had twenty-five percent. Same truck name, same research firm, almost half the number. So how long do trucks really last? Let's look at what the data actually says, and what it cannot tell you.""",
   "Toyota Tundra pickup", "47.9% → 25.0%")

# ---------- COLD OPEN ----------
sc("""Every truck owner has heard it. These things last forever. Somebody's uncle has a truck with four hundred thousand miles. A dealer says this engine will outlive you. And it is true that some trucks run for decades. But a story about one truck is not data. When you are about to spend fifty or sixty thousand dollars, you want to know the odds, not the legends.""",
   "Ford F-150 old pickup", "LEGENDS VS ODDS")
sc("""So in this video we look at three kinds of evidence. How old American vehicles actually get before they leave the road. How many trucks reach two hundred thousand and two hundred fifty thousand miles, according to studies of hundreds of millions of vehicles. And what breaks first, based on recalls and investigations from twenty twenty-five and twenty twenty-six.""",
   "Chevrolet Silverado 1500 pickup", "3 KINDS OF EVIDENCE")
sc("""And there is a twist in each one. The truck that sells the most in America barely shows up in the longevity rankings. Heavy-duty trucks beat half-tons, but not for the reason most people think. And the trucks that earned the best reputations are often not the trucks being sold today. Every figure comes from a published source, listed in the description. Let's begin with the age of America's vehicles.""",
   "Ram 2500 Heavy Duty", "A TWIST IN EACH ONE")

# ---------- 1. AVERAGE AGE ----------
sc("""According to S&P Global Mobility data reported in May twenty twenty-five, the average age of light vehicles on American roads reached a record twelve point eight years. Passenger cars averaged fourteen point five years. Light trucks, which include pickups and SUVs, averaged eleven point nine years. And there were about two hundred eighty-nine million vehicles in operation, up one percent.""",
   "Ford F-150 thirteenth generation", "AVERAGE AGE: 12.8 YEARS")
sc("""Here is the first twist. Light trucks are younger on average than cars, even though trucks have the reputation for lasting longer. Why? Because Americans keep buying new trucks and SUVs in huge numbers, while car sales keep shrinking. Repairer Driven News reported that passenger cars on U.S. roads have fallen below one hundred million. A fleet full of new trucks pulls the average truck age down.""",
   "Chevrolet Silverado 2024", "TRUCKS ARE YOUNGER THAN CARS")
sc("""And the vehicles that are old are staying on the road. The scrappage rate, the share of vehicles taken off the road each year, held at four and a half percent, according to S&P. A collision repair analytics firm, CCC, projected the overall average would reach thirteen years by twenty twenty-six. High new and used prices are part of the reason. When a new truck costs this much, people keep the old one running.""",
   "Ford F-250 old pickup", "SCRAPPAGE: 4.5% A YEAR")
sc("""There is a regional story too. According to the same report, the Northern Plains, the Northwest and the Gulf Coast have older fleets, and Montana has the oldest of any state. That makes sense. These are places where people drive long distances, often in trucks, and where a reliable old pickup is worth more than a new one with a big monthly payment. So how far do those trucks actually go?""",
   "Chevrolet pickup Montana ranch", "MONTANA: THE OLDEST FLEET")

sc("""And trucks now dominate that fleet. In twenty twenty-three, S&P reported that light trucks and utility vehicles made up about sixty-three percent of all vehicles in operation, and seventy-eight percent of new registrations in twenty twenty-two. S&P expected light trucks to reach at least seventy percent of the fleet by twenty twenty-eight. And about one hundred twenty-two million vehicles were already more than twelve years old.""",
   "Ram 1500 2015", "LIGHT TRUCKS: 63% OF THE FLEET")
sc("""Here is why that matters to you. More old trucks on the road means more used trucks for sale, and more of them with high mileage. In twenty twenty-four, new vehicle registrations topped sixteen million for the first time since twenty nineteen, according to Repairer Driven News. A lot of those trades went onto used lots. So if you shop for a used truck in twenty twenty-seven, the question is not whether it has high miles. It is which high-mile trucks are worth it.""",
   "used pickup trucks dealer lot", "MORE OLD TRUCKS FOR SALE")
sc("""And before we look at mileage odds, a quick sense of scale. Two hundred fifty thousand miles is a lot. At fifteen thousand miles a year, that is about sixteen or seventeen years of driving. At twelve thousand miles a year, it is more than twenty years. So when a study says a truck has a twenty-five percent chance of reaching that number, it means one in four of those trucks is still being driven decades after it was built.""",
   "Chevrolet C10 old pickup", "250,000 MILES ≈ 17+ YEARS")
# ---------- 2. THE 250K STUDIES ----------
sc("""The best-known numbers come from iSeeCars, a car research firm that estimates how likely each model is to reach a high mileage. In its twenty twenty-three study, reported by Automotive Fleet, it analyzed more than two hundred sixty million cars sold from twenty twelve to twenty twenty-two. The average vehicle had an eleven point eight percent chance of reaching two hundred fifty thousand miles. And trucks took ten of the twenty-three top spots.""",
   "Ford F-350 Super Duty", "2023 STUDY: AVERAGE 11.8%")
sc("""The top trucks in that study were heavy hitters. The Ford F-three fifty Super Duty at forty-nine point one percent. The Toyota Tundra at forty-seven point nine. The Ford F-two fifty at forty-three point six. The Toyota Tacoma at forty-one point seven. The GMC Sierra twenty-five hundred HD at forty-one point three, and the Chevrolet Silverado twenty-five hundred HD at forty-one point two. The Silverado fifteen hundred was at thirty-one percent.""",
   "Ford F-250 Super Duty", "F-350 49.1%, TUNDRA 47.9%")
sc("""Now look at the newest version. In September twenty twenty-six, TFL Car reported iSeeCars' latest study, based on roughly four hundred million vehicles. The average vehicle now had just a five point three percent chance of reaching two hundred fifty thousand miles. The Toyota Tacoma was fifth overall at twenty-eight point two percent. The Tundra was sixth at twenty-five percent. The Honda Ridgeline was seventeenth, at thirteen point seven.""",
   "Toyota Tacoma", "2026 STUDY: AVERAGE 5.3%")
sc("""And another report on the iSeeCars data, published by MoneyLion in August twenty twenty-six, gave slightly different numbers. An average of four point eight percent. The Tundra at thirty percent, the highest of any light-duty pickup. The Tacoma at twenty-five point three. The Ridgeline at fourteen point seven. The Silverado fifteen hundred at twelve point nine, and the GMC Sierra fifteen hundred at ten point eight.""",
   "Toyota Tundra TRD", "TUNDRA 30%, SILVERADO 12.9%")
sc("""Here is the twist. The average dropped from eleven point eight percent to around five percent, and every truck's number dropped with it. That does not mean trucks suddenly got worse. It means the studies measure different groups of vehicles, with different data. TFL noted that the analysis uses historical mileage data to extrapolate future longevity. So treat these numbers as rankings, not promises. The order matters more than the exact percentage.""",
   "Chevrolet Silverado 1500 2018", "RANKINGS, NOT PROMISES")
sc("""And the ranking tells a consistent story. In every version, Toyota's trucks sit near the top. In the twenty twenty-six list, Toyota and Lexus took most of the top ten spots overall, with the Sequoia SUV first at forty-two point three percent. Among pickups, the Tacoma and Tundra led, and the Honda Ridgeline was the best pickup from any other brand. That is the source of the Toyota reputation, and it is backed by data.""",
   "Toyota Sequoia", "TOYOTA ON TOP, EVERY TIME")

sc("""Look at who is missing from the newest top twenty-five list. No Ford at all. No Ram. No GMC. The only General Motors vehicle was the Chevrolet Suburban, an SUV, at twenty-third with eleven point six percent. The Mercedes-Benz G-Class, a truck-based SUV, was fourteenth. And the Honda Ridgeline, a pickup most truck owners do not take seriously because it is built like a crossover, outranked every American pickup.""",
   "Honda Ridgeline pickup", "NO FORD, RAM OR GMC IN THE TOP 25")
sc("""And notice the gap between twins in the MoneyLion report. The Chevrolet Silverado fifteen hundred at twelve point nine percent, and the GMC Sierra fifteen hundred at ten point eight. They share engines, frames and factories. Yet the data gives the Chevy better odds. The study does not explain it, but buyers of the two trucks are different, the trims are different, and the way the trucks are used can be different. Data about trucks is also data about owners.""",
   "GMC Sierra 1500 Denali", "SILVERADO 12.9% VS SIERRA 10.8%")
# ---------- 3. THE F-150 PARADOX ----------
sc("""Now the strangest part of the data. The Ford F-150 is the best-selling vehicle in America, year after year. Ford sold eight hundred one thousand, five hundred twenty-five F-Series trucks in twenty twenty-five, according to CarScoops. And yet in the newest longevity lists, the F-150 does not appear near the top. MoneyLion said it did not rank as highly as some competitors, and gave no number.""",
   "Ford F-150 pickup truck", "BEST SELLER. NOT A TOP LASTER.")
sc("""Why? The studies do not say, so we will not invent a reason. But notice that Ford's heavy-duty trucks did extremely well in the twenty twenty-three study. The F-three fifty was number one of all vehicles, and the F-two fifty was third. So it is not that Ford trucks cannot last. In that data, the big Fords outlasted almost everything. It is the half-ton that falls behind its own big brothers.""",
   "Ford F-350 dually", "THE BIG FORDS LASTED THE LONGEST")
sc("""There is one possible clue in the F-150's recent history, and we will label it clearly as context, not proof. In earlier videos we covered the three point five EcoBoost cam phaser problems on twenty seventeen to twenty twenty trucks, repairs that can cost four to six thousand dollars out of warranty according to TorqueNews, and the ten-speed transmission complaints. Expensive repairs at high mileage can push an owner to sell or scrap a truck that still runs.""",
   "Ford F-150 EcoBoost", "CONTEXT: EXPENSIVE HIGH-MILE REPAIRS")

sc("""So should F-150 owners worry? Not necessarily. These studies measure the odds of reaching an extreme mileage, not the odds of a reliable first one hundred fifty thousand miles. Consumer Reports ranked the F-150 first among full-size trucks for predicted reliability, as we covered in our reliability video. A truck can be dependable for ten years and still be less likely to reach two hundred fifty thousand. Those are different questions, and the data answers them differently.""",
   "Ford F-150 Lariat", "RELIABLE ≠ LONGEST-LASTING")
# ---------- 4. HEAVY DUTY ----------
sc("""Now the heavy-duty twist. An earlier iSeeCars study, reported by Work Truck Online in twenty twenty-one, looked at how many trucks reached two hundred thousand miles. The Ram thirty-five hundred led the heavy-duty pickups at eight point four percent. The Silverado twenty-five hundred HD was at six point three, and the F-three fifty at five point eight. And iSeeCars found that heavy-duty trucks last up to twice as long as light-duty versions.""",
   "Ram 3500 Heavy Duty", "HD: UP TO 2X LONGER")
sc("""Why do heavy-duty trucks last longer? Part of it is engineering. Their frames, axles, brakes and cooling systems are built for loads far beyond what most owners ever carry. When a truck rated to tow twenty thousand pounds spends most of its life towing ten, every part works at half its limit. And many heavy-duty diesels are designed for long service lives in commercial use.""",
   "Ford F-350 towing", "BUILT FOR MORE THAN THEY DO")
sc("""But here is the twist. Part of it is how they are driven. Many heavy-duty trucks work on long highway routes, at steady speeds, with regular maintenance paid by a business. Highway miles are the easiest miles an engine will ever do. A half-ton that does short trips, cold starts and stop-and-go traffic can wear faster, even with fewer miles on the clock. Longevity is not only how a truck is built. It is how it is used.""",
   "Chevrolet Silverado 2500HD highway", "HOW IT IS DRIVEN MATTERS")
sc("""And light-duty pickups still beat ordinary cars. In that twenty twenty-one study, light-duty pickups had a one point nine percent chance of reaching two hundred thousand miles, nearly double the average for all vehicles, according to Work Truck Online. The Tundra ranked first among light-duty pickups, followed by the Honda Ridgeline and the Toyota Tacoma. Different study, same order at the top.""",
   "Honda Ridgeline", "LIGHT-DUTY: NEARLY 2X THE AVERAGE CAR")

sc("""And what about electric and hybrid trucks? For longevity, there is almost no data yet. According to S&P, the average battery electric vehicle on the road was only three point seven years old, and the average traditional hybrid six point four years. They have not been around long enough to reach two hundred fifty thousand miles in large numbers. So anyone who tells you exactly how long an electric pickup will last is guessing.""",
   "Ford F-150 Lightning", "EV TRUCKS: TOO NEW TO KNOW")
sc("""The same is true for the newest gas engines. The twin-turbo V6 engines in the Tundra and many F-150s, the newest GM V8s, the updated Ram engines, all of them are too recent for the twenty-year data. That does not make them bad. It makes them unproven. The trucks with the longest track records are the ones with the oldest designs.""",
   "Ram 1500 2025", "NEW ENGINES ARE UNPROVEN")
# ---------- 5. WHAT BREAKS FIRST ----------
sc("""So what ends a truck's life? Usually not rust or a worn seat. It is the cost of one big repair compared with what the truck is worth. And in twenty twenty-five and twenty twenty-six, the most expensive stories were engines and transmissions. According to J.D. Power, replacing a truck transmission typically costs two thousand five hundred to six thousand dollars, and heavy-duty trucks can cost more.""",
   "Chevrolet Silverado 1500 engine", "THE REPAIR THAT ENDS A TRUCK")
sc("""Look at the engines. Toyota's twin-turbo V6 in the newer Tundra has been recalled three times for machining debris that can destroy a main bearing, according to Motor1, with Toyota replacing whole engines. GM's six point two liter V8 was recalled on nearly six hundred thousand vehicles, and the federal safety agency opened an investigation in August twenty twenty-six after hundreds of complaints of failures after the fix, according to GM Authority.""",
   "Toyota Tundra 2023", "NEW ENGINES, BIG RECALLS")
sc("""Here is the twist that matters most for this video. The trucks that built the longevity reputation were mostly older designs. TFL Car warned that the longevity analysis may not reflect recent redesigns and new powertrain or software issues at Toyota and Lexus. The Tundra that reached two hundred fifty thousand miles in the data mostly had a V8. The Tundra on sale today has a twin-turbo V6 with three engine recalls. The reputation is real. It just belongs to the previous truck.""",
   "Toyota Tundra 2021 V8", "THE REPUTATION BELONGS TO THE OLD TRUCK")
sc("""The same is true for the Silverado and Sierra. The GM V8s that powered millions of older trucks have a strong history. The newer six point two is under investigation. So when someone tells you a brand's trucks last forever, ask which engine and which years they are talking about. The data is usually about trucks that are ten or twenty years old, not the one on the lot.""",
   "GMC Sierra 1500", "ASK: WHICH ENGINE, WHICH YEARS?")

sc("""Diesels are their own story. Heavy-duty diesel trucks have a reputation for huge mileage, and the twenty twenty-three study backs up the heavy-duty advantage in general, although it did not separate diesel engines from gas engines. But even diesels have weak points. Ford's six point seven Power Stroke has a high-pressure fuel pump that has been part of recalls and a class action that a judge partly certified in October twenty twenty-six, according to Pickup Truck and SUV Talk. A long-life engine can still be ended by one part.""",
   "Ford F-250 Power Stroke diesel", "A LONG-LIFE ENGINE, ONE WEAK PART")
# ---------- 6. HOW TO MAKE ONE LAST ----------
sc("""So can you make a truck last longer than the averages? The data cannot prove what any single owner does, but the recalls and investigations we have covered point to a few clear habits. First, oil. GM's recall remedy for the six point two depended on a specific thicker oil. Ford's lawyers in the diesel fuel pump case argued that some failures came from owners who did not change dirty fuel filters. Maintenance is not a detail. It is the defense.""",
   "Ford Super Duty engine", "MAINTENANCE IS THE DEFENSE")
sc("""Second, keep every record. In the GM engine investigation, owners with documented oil changes are in the best position if a new remedy appears. In the Ram EcoDiesel settlement, the extended warranty counts from the date of the original repair. A folder of receipts is worth real money when something goes wrong, and when you sell the truck.""",
   "Ram 1500 EcoDiesel", "KEEP EVERY RECEIPT")
sc("""Third, check and complete every recall. Many of the biggest truck problems of twenty twenty-six were fixed for free, with software or new parts. A recall left open can turn a fixable problem into the repair that ends a truck's life. And fourth, think about how you drive. Short trips, extreme heat, heavy towing and low fuel all showed up in the recall reports we covered. If your truck does those things, service it like a work truck.""",
   "Ford F-150 XLT", "COMPLETE EVERY RECALL")

sc("""And one last habit, which is about buying, not driving. If you buy a truck with high mileage, the mileage itself matters less than what has already been replaced. A truck at one hundred eighty thousand miles with a new transmission, recent timing work and documented oil changes can be a better bet than one at one hundred twenty thousand with no records. The longevity studies count miles. You should count receipts.""",
   "Toyota Tacoma used", "COUNT RECEIPTS, NOT JUST MILES")
sc("""S&P Global Mobility put it this way. The graying of the U.S. fleet is more than a statistic. More people are keeping vehicles longer because new ones are so expensive. For truck buyers, that means the most valuable skill in twenty twenty-seven may not be negotiating a new truck price. It may be knowing which used truck will keep going, and which one is about to need its most expensive repair.""",
   "Ford F-150 2010", "\"MORE THAN A STATISTIC\"")
# ---------- CLOSE ----------
sc("""So how long do trucks really last? Here is the honest summary. The average American light truck on the road is about twelve years old. The average vehicle has only around a five percent chance of reaching two hundred fifty thousand miles, in the newest study. Toyota pickups and heavy-duty trucks have the best odds by far. And the best-selling half-ton in America is not near the top.""",
   "Toyota Tacoma and Ford F-350", "THE HONEST SUMMARY")
sc("""And the final twist is simple. Every longevity study is a look in the rearview mirror. It tells you how trucks built years ago have done. It cannot tell you how a twenty twenty-seven truck with a new engine, new transmission and new software will do at two hundred thousand miles. For that, your best tools are the recall record, the engine history, and the maintenance you do.""",
   "Chevrolet Silverado 1500", "STUDIES LOOK BACKWARD")
sc("""Here is your longevity checklist for twenty twenty-seven. One, if you want the best odds, look at Toyota pickups and heavy-duty trucks, but check the engine generation. Two, avoid first model years of new engines. Three, ask for full service records on any used truck. Four, run the VIN for recalls. And five, budget for one major repair after the warranty ends, because that is the moment that decides how long your truck lasts.""",
   "Ford Super Duty", "5 LONGEVITY CHECKS")
sc("""We put all of this into the Twenty Twenty-Seven Truck Buyer's Guide, including which engines and years to watch. The link is in the description and in the pinned comment. If this helped, subscribe, because next we cover five warning signs before buying a used truck. And tell us in the comments, how many miles does your truck have? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In one study, the Toyota Tundra": "Intro", "According to S&P Global Mobility": "How old America's vehicles get",
      "The best-known numbers": "Who reaches 250,000 miles", "Now the strangest part": "The F-150 paradox",
      "Now the heavy-duty twist": "Heavy-duty vs half-ton", "So what ends a truck's life": "What ends a truck's life",
      "So can you make a truck last": "How to make a truck last", "So how long do trucks really last": "The verdict and checklist for 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video28", "length_scale": 1.45,
  "title": "How Long Do Trucks Really Last? The 250,000-Mile Data (2027)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
