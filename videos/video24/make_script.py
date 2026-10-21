import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In February twenty twenty-six, J.D. Power named the Ram fifteen hundred the most dependable full-size pickup in America. Two months earlier, Consumer Reports had called the same truck one of the least reliable vehicles it surveyed. Same truck. Opposite answers. So which truck brand is really the most reliable? We put four studies side by side, and the answer is not what either side wants to hear.""",
   "Ram 1500 pickup truck", "#1 OR LAST? SAME TRUCK.")

# ---------- COLD OPEN ----------
sc("""Every truck brand in America says it is the most reliable. Ford points to quality awards. Ram points to J.D. Power. Toyota points to its reputation. Chevrolet points to the number of old Silverados still on the road. And all of them can show you a chart that proves it. That is exactly the problem. When every brand wins, the word reliable stops meaning anything.""",
   "Ford F-150 Chevrolet Silverado Ram 1500", "EVERY BRAND CLAIMS IT")
sc("""So in this video we do something simple. We take the biggest reliability studies published for twenty twenty-six, Consumer Reports, J.D. Power's Vehicle Dependability Study, J.D. Power's Initial Quality Study, and a long-term durability study from iSeeCars. And we look at what each one actually measures. Because once you know what is being counted, the contradictions start to make sense.""",
   "Toyota Tundra pickup", "4 STUDIES. 1 QUESTION.")
sc("""And there is a twist in every round. A brand that finishes near the bottom of one study wins another. A truck famous for lasting forever slips in a new survey. And the brand with the most recalls in history wins an award for quality in the same year. By the end, you will know which brand wins, for which kind of buyer, and what to check before you sign in twenty twenty-seven.""",
   "Toyota Tacoma", "A TWIST IN EVERY ROUND")
sc("""As always, every figure comes from a published source, listed in the description. We will not invent scores that the studies did not publish. Where a study only gives a ranking and not a number, we will tell you. Let's start with the study most buyers know by name.""",
   "Chevrolet Silverado 1500", "EVERY NUMBER IS SOURCED")

# ---------- ROUND 1: CONSUMER REPORTS ----------
sc("""Round one is Consumer Reports. On December fourth, twenty twenty-five, it released its twenty twenty-six Automotive Brand Report Card. The reliability part is based on surveys of about three hundred eighty thousand vehicles, up twenty-seven percent from the year before. Owners are asked about up to twenty problem areas, and serious problems that can lead to expensive repairs count more heavily.""",
   "Toyota Tundra 2024", "CONSUMER REPORTS: 380,000 VEHICLES")
sc("""The winner for predicted reliability was Toyota, its first reliability win since twenty twenty-two, narrowly ahead of Subaru. Now look at the American truck brands. Ford finished eleventh, its best showing in fifteen years. Chevrolet finished seventeenth. GMC twenty-third. Jeep twenty-fourth. And Ram finished twenty-fifth, with the Ram fifteen hundred listed among the least reliable vehicles surveyed.""",
   "Toyota Tacoma TRD", "CR: TOYOTA #1, RAM #25")
sc("""Here is the first twist. Toyota won the brand title, but in the full-size truck ranking, the Tundra did not. According to Pickup Truck and SUV Talk's breakdown of the Consumer Reports results, the Ford F-150 took the top spot among full-size trucks for the second year in a row. The GMC Sierra was next, then the Tundra, then the Chevrolet Silverado, and the Ram fifteen hundred finished last.""",
   "Ford F-150 pickup", "FULL-SIZE: F-150 FIRST")
sc("""Why did the Tundra slip? The report points to lingering engine issues, including a second engine failure recall on its twin-turbo V6. The Silverado was hurt by electrical problems and concerns about its V8 engines, including lifter issues. And the Ram was hurt mostly by in-car electronics, screens and systems that owners said often did not work properly. Three trucks, three completely different weaknesses.""",
   "Toyota Tundra TRD Pro", "TUNDRA: ENGINE. RAM: ELECTRONICS.")
sc("""And for the F-150, the report was not all good news either. Owners mentioned PowerBoost hybrid issues, ten-speed transmission problems, and engine concerns involving turbos and cam phasers. But Consumer Reports also noted that the F-150, the F-150 Hybrid and the Lightning all moved from below average to average. In Consumer Reports terms, average is a big step up.""",
   "Ford F-150 hybrid", "F-150: UP TO AVERAGE")
sc("""Heavy-duty trucks had their own surprise. In the Consumer Reports results for twenty twenty-six heavy-duty pickups, as reported by Pickup Truck and SUV Talk, the Chevrolet Silverado twenty-five hundred HD came out as the most reliable, and its twin, the GMC Sierra twenty-five hundred HD, came out as the least reliable. Same engines, same transmission, opposite ends of the ranking.""",
   "Chevrolet Silverado 2500HD", "HD: SILVERADO BEST, SIERRA WORST")
sc("""How can twins land so far apart? The report noted that the Sierra HD's weak areas were suspension, steering and in-car electronics, while its powertrain improved. Different trim mixes, different features, and different owners can move survey results. Which is the first big lesson of this video. A reliability score is a survey of real owners, and it can be moved by things that have nothing to do with the engine.""",
   "GMC Sierra 2500HD", "TWINS. OPPOSITE SCORES.")

sc("""Two more pickups sit at the very bottom of that Consumer Reports list, and they are easy to forget. Jeep, which sells the Gladiator pickup, finished last overall in the report card for the third year in a row, with the lowest owner satisfaction of any brand. And Rivian, maker of the R one T electric pickup, finished dead last in predicted reliability, with the R one T listed among the least reliable vehicles surveyed.""",
   "Jeep Gladiator", "JEEP AND RIVIAN: AT THE BOTTOM")
sc("""Meanwhile, Tesla, the maker of the Cybertruck, reached ninth in predicted reliability, its highest ranking ever, according to Consumer Reports. That is a brand score, built mostly on the Model 3 and Model Y, so it says little about the Cybertruck itself. And that is an important warning about brand rankings in general. A brand score is an average of everything the brand sells, and most brands sell far more SUVs and cars than trucks.""",
   "Tesla Cybertruck", "A BRAND SCORE IS AN AVERAGE")
sc("""And one more detail about how Consumer Reports builds its numbers. Predicted reliability for a model uses its last three model years, as long as it was not redesigned. When there is not enough data, the brand's own score fills the gap. So a brand-new truck can inherit a good or bad score from its siblings, before owners have said a word about it. Keep that in mind when you see a score for a truck that just launched.""",
   "Ford Ranger 2024", "NEW TRUCKS INHERIT SCORES")
# ---------- ROUND 2: J.D. POWER VDS ----------
sc("""Round two is J.D. Power's twenty twenty-six Vehicle Dependability Study, released in February. It asks original owners of three-year-old vehicles, in this case twenty twenty-three models, about problems in the last twelve months. Thirty-three thousand, two hundred sixty-eight owners responded, according to Pickup Truck and SUV Talk. The score is problems per one hundred vehicles. Lower is better.""",
   "Ram 1500 Laramie", "J.D. POWER: 3-YEAR-OLD TRUCKS")
sc("""And here is the result that started this video. In the large light-duty pickup segment, the Ram fifteen hundred finished first, up from fourth the year before. The Chevrolet Silverado fifteen hundred was second. The GMC Sierra and Ford F-150 tied for third. And the Toyota Tundra was not in the top three at all, which Pickup Truck and SUV Talk said placed it below the segment average.""",
   "Ram 1500 Rebel", "VDS: RAM 1500 #1")
sc("""So how can the Ram be first here and last in Consumer Reports? Look at what each one measures. J.D. Power surveyed twenty twenty-three trucks, three years in. Consumer Reports predicts reliability for new models using the last three model years, and the Ram fifteen hundred changed a lot for twenty twenty-five, with new engines and new electronics. One looks backward at older trucks. The other tries to predict the trucks on sale now.""",
   "Ram 1500 2025", "BACKWARD VS FORWARD")
sc("""Now the brand ranking, as reported by Motor1. The industry average was two hundred four problems per hundred vehicles. Lexus was best at one hundred fifty-one. Chevrolet was fifth overall at one hundred seventy-eight, better than Toyota, which was eighth at one hundred eighty-five. Nissan was tenth at one hundred ninety-four. And at the other end, Ford scored two hundred twenty-eight, GMC two hundred twenty-nine, and Jeep two hundred sixty-seven.""",
   "Chevrolet Silverado 1500 pickup", "CHEVY 178 BEATS TOYOTA 185")
sc("""Here is the twist. In J.D. Power's dependability ranking, Chevrolet beat Toyota. And GMC, which sells almost the same trucks as Chevrolet, finished near the bottom, fifty-one points worse. Again, twins with very different scores. The difference likely comes from the mix of vehicles each brand sells, but the study does not break that down, so we will not guess.""",
   "GMC Sierra 1500 Denali", "CHEVY VS GMC: 51 POINTS APART")
sc("""And look at what owners actually complained about. According to the study's summary, four of the top five problems involved smartphone connectivity. Android Auto and Apple CarPlay issues led for the third year in a row, at eight point nine problems per hundred vehicles. That means a truck can lose points because a phone will not connect, even if the engine never misses a beat.""",
   "Ford F-150 interior dashboard", "#1 PROBLEM: PHONE CONNECTIVITY")
sc("""There was one more number that matters for truck buyers. Gasoline vehicles were the most dependable powertrain type, at one hundred ninety-eight problems per hundred vehicles. Plug-in hybrids had the most problems, two hundred eighty-one, up thirty-nine points. Electric vehicles and hybrids each rose fourteen points. So in this study, the old-fashioned gas engine was the safest bet.""",
   "Ford F-150 Lightning", "GAS 198 VS PLUG-IN 281")

sc("""And this study found something that should worry every brand. Problem counts were the highest since J.D. Power revised the study in twenty twenty-two, extending a three-year slide in dependability, according to Ford Authority. Over-the-air updates were part of it. Forty percent of owners got one in the past year, but only twenty-seven percent said it improved their vehicle, and updates were linked to an increase of two point five problems per hundred vehicles.""",
   "Ram 1500 TRX", "UPDATES ADDED PROBLEMS")
sc("""Think about what that means for a truck in twenty twenty-seven. The more software a truck has, the more ways it can annoy its owner, and the more often it gets updated. In the past, a reliable truck was one that started every morning. Now a truck can start every morning for ten years and still score badly, because its screen freezes or its phone connection drops. Reliability is being redefined in real time.""",
   "Chevrolet Silverado interior", "RELIABILITY IS BEING REDEFINED")
sc("""There was one more gap in the study worth noting. The difference between premium brands and mass-market brands widened to seventeen problems per hundred vehicles, and premium models did worse in seven of nine categories, according to Pickup Truck and SUV Talk. In other words, the expensive brands did worse, not better. More features, more screens, more things to go wrong. That is why a top-trim truck is not automatically the most dependable one.""",
   "GMC Sierra Denali Ultimate", "MORE FEATURES, MORE PROBLEMS")
# ---------- ROUND 3: J.D. POWER IQS ----------
sc("""Round three is J.D. Power's twenty twenty-six Initial Quality Study, announced in late June. This one measures problems in the first ninety days of ownership. And the winner among mainstream brands was Ford, for the first time since twenty ten, according to Ford's own announcement of the results. Ford said it had forty-one fewer problems per hundred vehicles than the year before, the largest improvement of any mainstream brand.""",
   "Ford F-150 Platinum", "IQS 2026: FORD #1")
sc("""And Ford's trucks led their segments. According to Ford, the F-150 ranked highest in its segment for the second year in a row, and so did the Super Duty. The Maverick placed in the top three of its segment. So in the same year, Ford was below average for three-year dependability, and first for new-vehicle quality.""",
   "Ford Super Duty", "F-150 AND SUPER DUTY: SEGMENT WINNERS")
sc("""Here is the twist that makes this one hard to believe. That same Ford set the all-time record for recalls in twenty twenty-five, one hundred fifty-three of them covering nearly thirteen million vehicles, according to Motor1. How can the most recalled brand win a quality award? Because initial quality measures what new owners notice in three months. Recalls can cover trucks a decade old, and many are found by the automaker's own audits.""",
   "Ford F-150 XLT", "MOST RECALLS. BEST INITIAL QUALITY.")
sc("""Ford's chief executive, Jim Farley, has said the company needs to improve its quality reputation, including long-term durability, according to Kelley Blue Book. And that phrase, long-term durability, is the key. Initial quality tells you how a truck leaves the factory. It does not tell you how it will feel at one hundred fifty thousand miles. For that, you need a different kind of data.""",
   "Ford F-150 Raptor", "FARLEY: LONG-TERM DURABILITY")

sc("""Lincoln, Ford's luxury brand, also climbed from eighth to sixth among premium brands, according to Ford. And Ford said its infotainment quality was eleven points better than the industry average. That matters, because infotainment was the number one complaint in J.D. Power's dependability study. So Ford's win may come partly from fixing exactly the problem that hurts every other brand.""",
   "Ford F-150 Lariat interior", "FORD FIXED THE SCREENS")
# ---------- ROUND 4: LONGEVITY ----------
sc("""Round four is longevity. iSeeCars studied more than two hundred sixty million vehicles sold from twenty twelve to twenty twenty-two, and calculated the chance that each model reaches two hundred fifty thousand miles, according to Automotive Fleet. One important note. This study was published in twenty twenty-three, so it is older than the others. But it measures something none of the surveys can, how far trucks actually go.""",
   "Ford F-350 Super Duty", "WHO REACHES 250,000 MILES?")
sc("""The average vehicle had an eleven point eight percent chance of reaching two hundred fifty thousand miles. And trucks dominated the list, ten of the twenty-three top spots. The Ford F-three fifty Super Duty was first, at forty-nine point one percent. The Toyota Tundra was second, at forty-seven point nine. The Ford F-two fifty was third, at forty-three point six. And the Toyota Tacoma was fourth, at forty-one point seven.""",
   "Ford F-350", "F-350: 49.1%. TUNDRA: 47.9%")
sc("""Then came General Motors' heavy-duty twins. The GMC Sierra twenty-five hundred HD at forty-one point three percent, and the Chevrolet Silverado twenty-five hundred HD at forty-one point two. The Silverado fifteen hundred was at thirty-one percent. The old Chevrolet Avalanche at twenty-six point seven. And Ram appeared with the twenty-five hundred at twenty-six point three and the thirty-five hundred at twenty-four point three.""",
   "GMC Sierra 2500HD", "GM HD TWINS: ~41%")
sc("""Here is the twist. In long-term durability, the winners were heavy-duty trucks and Toyotas, and the half-ton trucks most people actually buy were mostly missing. No F-150 in the top list. No Ram fifteen hundred. The Silverado fifteen hundred was the only full-size half-ton. Heavy-duty trucks are overbuilt for work, and many are driven on long highway routes, which is easy on an engine.""",
   "Chevrolet Silverado 2500HD", "HALF-TONS MOSTLY MISSING")
sc("""And remember the Tundra in that study. Those were trucks sold from twenty twelve to twenty twenty-two, mostly the old V8 Tundra. The new twin-turbo V6 Tundra, launched for twenty twenty-two, has had three engine recalls, according to Motor1. So the Tundra's legendary reputation was earned by a truck Toyota no longer builds. That does not mean the new one is bad. It means its reputation is still being written.""",
   "Toyota Tundra 2022", "THE LEGEND WAS THE OLD V8")

sc("""And Toyota's dominance in that study went beyond trucks. Toyota had eight models among the twenty-three vehicles with at least a twenty percent chance of reaching two hundred fifty thousand miles. More than any other brand. That is the source of the reputation you hear at every dealership. It is real. It is just based on vehicles from before the current generation.""",
   "Toyota Tacoma 2015", "TOYOTA: 8 OF THE 23")
sc("""Now there is one more ranking worth hearing, because it measures something the surveys ignore, how bad the problems are. In July twenty twenty-six, Pickup Truck and SUV Talk ranked the full-size trucks by repair severity, recalls, investigations and owner complaints. Its ranking put the Ford F-150 first, the Ram fifteen hundred second, the Silverado and Sierra tied for third, and the Tundra fifth.""",
   "Ford F-150 pickup truck", "SEVERITY RANKING: F-150 FIRST")
sc("""Its reasoning is the twist. The F-150 won not because it is problem-free, but because the reviewers found no widespread current-generation engine failure pattern. The Ram finished second because its problems were mostly electronics, and its ZF eight-speed transmission was rated strong. The GM trucks were held back by the six point two V8 recall, and the Tundra by its twin-turbo V6 engine replacements.""",
   "Ram 1500 Big Horn", "NUISANCE VS CATASTROPHE")
sc("""That article also listed J.D. Power's twenty twenty-five quality and reliability ratings, out of one hundred. The F-150 and the Silverado fifteen hundred tied at eighty-six. The Tundra scored eighty-three. The Sierra eighty-two. And the Ram fifteen hundred seventy-seven, the lowest of the five. So even inside J.D. Power, the Ram's results depend on which study you read.""",
   "Chevrolet Silverado 1500 LT", "F-150 86, SILVERADO 86, RAM 77")
# ---------- SCORECARD ----------
sc("""So let's build a scorecard, brand by brand. Toyota first. Consumer Reports' most reliable brand. Eighth in J.D. Power dependability, at one hundred eighty-five. Second and fourth in long-term durability with the Tundra and Tacoma. But the new Tundra's engine recalls cost it points with truck owners right now. Toyota's strength is history. Its question mark is the new engine.""",
   "Toyota Tundra and Tacoma", "TOYOTA: STRONG HISTORY, NEW QUESTION")
sc("""Ford next. The best Consumer Reports showing in fifteen years, at eleventh, and the top full-size truck in Consumer Reports. First in J.D. Power initial quality, with the F-150 and Super Duty both winning their segments. First and third in long-term durability with the F-three fifty and F-two fifty. But below average in J.D. Power three-year dependability, and the recall record holder.""",
   "Ford F-150 and Super Duty", "FORD: WINS NEW, RECALLS OLD")
sc("""Chevrolet and GMC. Chevrolet fifth in J.D. Power dependability, ahead of Toyota, with the Silverado second among full-size trucks. Strong heavy-duty durability. And the Silverado twenty-five hundred HD the most reliable heavy-duty truck in Consumer Reports. But GMC finished near the bottom of J.D. Power, and the six point two liter V8 is under federal investigation. Strong trucks, with one big engine story.""",
   "Chevrolet Silverado and GMC Sierra", "GM: STRONG TRUCKS, ONE ENGINE STORY")
sc("""And Ram. First in J.D. Power three-year dependability for the Ram fifteen hundred. But twenty-fifth in Consumer Reports, and lowest of the five full-size trucks in J.D. Power's quality and reliability ratings, as reported by Pickup Truck and SUV Talk. Ram backs its trucks with a ten-year, one hundred thousand mile limited powertrain warranty, according to Stellantis. For Ram, the warranty may matter more than any score.""",
   "Ram 1500 Limited", "RAM: #1 OR #25, PLUS A 10-YEAR WARRANTY")

# ---------- CLOSE ----------
sc("""So which truck brand is the most reliable? Here is the honest answer. If you want the best odds of a truck that lasts for decades, the data favors heavy-duty trucks and Toyota's older designs. If you want a new truck with the fewest problems in the first months, Ford won twenty twenty-six. If you are buying a three-year-old truck, J.D. Power says the Ram fifteen hundred and the Silverado had the fewest problems.""",
   "Ford F-350 Toyota Tundra Ram 1500", "THE ANSWER DEPENDS ON YOUR TRUCK'S AGE")
sc("""And here is the final twist. Brand matters less than the specific truck. The same Consumer Reports that ranked Toyota first put the Tundra third among full-size trucks. The same J.D. Power that ranked Chevrolet fifth ranked GMC near the bottom. Consumer Reports' own testing director, Jake Fisher, says to steer clear of newly introduced or redesigned vehicles in their first model year. That one rule beats any brand loyalty.""",
   "Chevrolet Silverado 1500", "SKIP THE FIRST MODEL YEAR")
sc("""So here is your checklist for twenty twenty-seven. One, look up the exact model and year, not the brand. Two, check whether that year was a redesign. Three, look up the engine, because engines carry most of the expensive stories. Four, run the VIN for recalls. And five, compare the warranty, because the longest warranty can be worth more than the best survey score.""",
   "Ram 1500 pickup", "5 CHECKS FOR 2027")
sc("""We put every one of these checks into the Twenty Twenty-Seven Truck Buyer's Guide, with the engines and years to watch for each brand. The link is in the description and in the pinned comment. And if this helped, subscribe, because next we cover six common truck problems nobody warns you about. Tell us in the comments, which brand has been the most reliable for you? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In February twenty twenty-six": "Intro", "Round one": "Round 1: Consumer Reports", "Round two": "Round 2: J.D. Power dependability",
      "Round three": "Round 3: J.D. Power initial quality", "Round four": "Round 4: Who reaches 250,000 miles",
      "So let's build a scorecard": "Brand scorecard", "So which truck brand": "The verdict and what to check in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video24", "length_scale": 1.4,
  "title": "Which Truck Brand Is Actually the Most Reliable? 4 Studies Disagree (2027)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
