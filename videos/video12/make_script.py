import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Only one truck in the whole study has a better than three in ten chance of reaching two hundred fifty thousand miles. The average pickup has just eleven percent. And a truck that was number ten in the earlier edition we could read just jumped to number one. This is the twenty twenty-six ranking of the trucks most likely to last, with the real numbers, and the one warning that every list leaves out.""",
   "Ram 3500 Heavy Duty pickup", "WHICH TRUCKS LAST THE LONGEST?")

# ---------- COLD OPEN ----------
sc("""Everyone says they want a truck that lasts. A truck that reaches two hundred fifty thousand miles is a truck that can serve a family, a business, or a ranch for fifteen years or more. But how do you know which one it will be? One way is a study that looks at what happened to millions of other trucks, and that is what iSeeCars published in twenty twenty-six.""",
   "Toyota Tundra pickup truck", "WHAT THE ISEECARS STUDY SAYS")
sc("""According to Work Truck Online, which reported the study on October twentieth, twenty twenty-six, iSeeCars analyzed data from more than three hundred ninety-five million vehicles, measured the average odometer reading at each age, and used a statistical model to estimate the chance that each model reaches two hundred fifty thousand miles. The overall truck average in the study is eleven point one percent.""",
   "Chevrolet Silverado 1500 pickup", "395 MILLION VEHICLES ANALYZED")
sc("""An important note on method. These percentages are estimated probabilities, not observed survival rates. They are not guarantees of reliability, and they do not measure maintenance cost. The study also excluded models that were discontinued as of the twenty twenty-two model year. So this is a guide to which trucks are more likely to go the distance, and not a promise about the truck you buy.""",
   "Ford F-250 Super Duty pickup", "PROBABILITIES, NOT PROMISES")
sc("""There is a twist in every group of trucks on this list. One truck jumped from the middle to the top in a single edition. One truck is the best at lasting, and the worst for reliability in another ranking. One group of trucks is losing sales while it is winning on longevity. And one family has two members with almost the same number, and very different futures. Stay with me, because the last twist changes how you should read every list.""",
   "Ram 2500 pickup", "SIX GROUPS. SIX TWISTS.")

# ---------- 1. RAM 3500 ----------
sc("""Number one is the Ram three thousand five hundred. According to the study, it has a thirty-one point nine percent chance of reaching two hundred fifty thousand miles, which is about three times the truck average of eleven point one. It is the only truck in the study with a chance above three in ten. Work Truck Online describes it as nearly three times the overall truck average.""",
   "Ram 3500 pickup", "RAM 3500: 31.9%")
sc("""Now the twist. In the earlier edition of the study that we could read, the one with a truck average of twenty-five point nine percent, the Ram three thousand five hundred was tenth, at twenty-four point three percent. The Ford F-three-fifty Super Duty was first, at forty-nine point one. In twenty twenty-six, the Ram is first at thirty-one point nine, and the Ford F-three-fifty is sixth at fifteen point one. The top of the list can change a lot from one edition to the next.""",
   "Ford F-350 Super Duty pickup", "EARLIER EDITION: F-350 FIRST, RAM 3500 TENTH")
sc("""Why does that matter? Because it tells you not to treat any one ranking as final. The Ram three thousand five hundred also keeps seventy-nine point eight percent of its value after five years, according to iSeeCars, the best of the heavy-duty trucks. So the evidence points the same way on both studies for this truck. But the ranking is a snapshot, and a careful buyer reads it with that in mind.""",
   "Ram 3500 Laramie pickup", "RAM 3500 RESALE: 79.8%")

# ---------- 2. TOYOTA TUNDRA ----------
sc("""Number two is the Toyota Tundra, the only half-ton truck near the top. It has a twenty-eight point two percent chance, about two and a half times the truck average. In the earlier edition, it was second at forty-seven point nine percent, behind only the Ford F-three-fifty. So the Tundra is consistent. It has been at or near the top in both editions that we could read.""",
   "Toyota Tundra pickup", "TUNDRA: 28.2%")
sc("""And now the twist, because the Tundra has a second story. Pickup Truck Talk ranked it last of the five full-size trucks for reliability in July, citing twin-turbo V six failures that in some cases required a complete engine replacement. So a truck can be likely to last a long time, and also have a known weakness. The study measures how long the truck is likely to stay on the road. It does not tell you what the repair bills will look like on the way.""",
   "Toyota Tundra 1794 pickup", "TUNDRA: LASTS LONG, KNOWN ENGINE ISSUES")
sc("""That is an honest conflict, and we do not want to hide it. The Tundra sold one hundred ten thousand and eighty trucks through nine months of twenty twenty-six, almost flat, and it keeps eighty and three tenths percent of its value. Millions of owners have trucks that run well. And some owners have engine trouble. If you consider a Tundra, check the engine in the exact model year and look at the warranty in writing.""",
   "Toyota Tundra pickup truck", "CHECK THE EXACT MODEL YEAR")

# ---------- 3. GMC SIERRA HD ----------
sc("""Number three is the GMC Sierra three thousand five hundred HD, at twenty-six point two percent, about two and a half times the average. And the Sierra two thousand five hundred HD is fifth, at seventeen point two percent. In the earlier edition, the Sierra two thousand five hundred HD was fifth too, at forty-one point three percent. So the GMC heavy-duty trucks have been consistent at being near the top.""",
   "GMC Sierra 3500HD pickup", "SIERRA 3500HD: 26.2%")
sc("""The twist is in the sales. The heavy-duty Sierra fell seven point seven percent through nine months of twenty twenty-six, to seventy-eight thousand, two hundred forty-six. And its Chevrolet twin, the heavy-duty Silverado, fell thirteen percent. In the longevity study, the Chevrolet Silverado two thousand five hundred HD is ninth at fourteen point one, and the three thousand five hundred HD is twelfth at eleven point seven, barely above the average. Same factory, same basic truck, very different positions.""",
   "Chevrolet Silverado 2500HD pickup", "SIERRA HD -7.7%. SILVERADO HD -13%.")

# ---------- 4. TOYOTA TACOMA ----------
sc("""Number four is the Toyota Tacoma, the best midsize truck on the list, at twenty-five percent, more than twice the truck average. In the earlier edition, it was fourth, at forty-one point seven. So it has been fourth in both editions. It is the most consistent truck in this ranking, and it is also the best seller among the midsize trucks, with two hundred fourteen thousand, eight hundred seventy-five sold through nine months.""",
   "Toyota Tacoma pickup", "TACOMA: 25.0%, 4TH IN BOTH EDITIONS")
sc("""The twist is who is missing. Of the midsize trucks, only the Tacoma and the Honda Ridgeline are in the top twelve. The Ridgeline is tenth at thirteen point seven percent. The Ford Ranger and the Nissan Frontier, which were at fourteen point one and twelve and a half in the earlier edition, are not in the top twelve this time. So among the midsize trucks, the Tacoma has a big lead, and the rest are near the average or below it.""",
   "Honda Ridgeline pickup", "RIDGELINE: 13.7%")
sc("""That is consistent with what we found on resale. The Tacoma keeps eighty and a half percent of its value, the Ranger sixty-eight point eight, and the Frontier sixty-three point four. The market and the study agree on one thing. The Tacoma is the midsize truck that holds up, both in use and in price. But it is not the cheapest. The popular SR5 trim cost thirty-nine thousand, four hundred fifty dollars in twenty twenty-six, according to TFL Car.""",
   "Toyota Tacoma TRD pickup", "TACOMA: BEST HOLD, NOT CHEAPEST")

# ---------- 5. FORD SUPER DUTY ----------
sc("""Number five is the Ford Super Duty family. The F-three-fifty is sixth at fifteen point one percent, the F-four-fifty seventh at fourteen point nine, and the F-two-fifty eleventh at thirteen point four. All three are above the truck average of eleven point one, but not by much, about one point two to one point four times. In the earlier edition, the F-three-fifty and the F-two-fifty were first and third, at forty-nine and forty-three percent.""",
   "Ford F-350 Super Duty pickup", "F-350: 15.1%. F-450: 14.9%. F-250: 13.4%.")
sc("""The twist is the average itself. According to the article, the truck average fell from twenty-five point nine percent in twenty twenty-three, to nineteen point four in twenty twenty-four, to thirteen in twenty twenty-five, to eleven point one in twenty twenty-six. But the article cautions that this does not prove newer trucks are less durable, because methodology and data changes can affect the results. So a fall in all the percentages may be partly the way the study is built.""",
   "Ford F-250 pickup", "TRUCK AVERAGE: 25.9% TO 11.1%")
sc("""That is the most important warning in this video. Do not compare a percentage from one year with a percentage from another. Compare trucks within the same edition. Within twenty twenty-six, the Ram three thousand five hundred is almost three times the average, and the Silverado three thousand five hundred HD is about one point one times. That ratio is more useful than the raw percentage, and it is the way we have shown it here.""",
   "Ram 2500 pickup truck", "COMPARE WITHIN ONE EDITION")

# ---------- 6. HONDA RIDGELINE AND RAM 2500 ----------
sc("""Number six is the two trucks in the middle, the Ram two thousand five hundred, eighth at fourteen point three percent, and the Honda Ridgeline, tenth at thirteen point seven. They are close to each other, and about one and a quarter times the average. In the earlier edition, the Ram two thousand five hundred was ninth at twenty-six point three. The Ridgeline sold thirty-seven thousand and twenty-eight through nine months of twenty twenty-six, down one percent.""",
   "Honda Ridgeline pickup", "RAM 2500: 14.3%. RIDGELINE: 13.7%")
sc("""The twist is that these are not the trucks that people talk about, and they have solid numbers. A buyer who wants a truck that lasts does not have to buy the number one. A truck with a fourteen percent chance is above the average, and it may cost less, and be easier to find. The ranking is a guide for the whole market, not only for the winners.""",
   "Ram 2500 Heavy Duty pickup", "ABOVE AVERAGE IS ENOUGH FOR MANY")


# ---------- HOW TO READ A PROBABILITY ----------
sc("""Let's think about what a probability like thirty-one point nine percent means in practice. It does not mean that a Ram three thousand five hundred has a one in three chance of lasting, and a Silverado three thousand five hundred HD has a one in nine chance. It means that, across all the trucks of that model, about that share are expected to reach that mileage. For any single truck, the care it gets matters as much as the model.""",
   "Ram 3500 pickup truck", "A MODEL AVERAGE, NOT YOUR TRUCK")
sc("""That is why the same model can show up on both sides of a conversation. One owner has a truck that passed three hundred thousand miles with only oil changes. Another had a transmission fail at one hundred thousand. Both are real, and both are in the average. A buyer who checks the service history of a specific used truck has more information than any study can give, and should use it first.""",
   "Ford F-250 Super Duty pickup", "THE SERVICE HISTORY BEATS THE STUDY")
sc("""There is also the question of what counts as lasting. A truck can reach two hundred fifty thousand miles with a new engine, a new transmission and a new set of suspension parts along the way. The study estimates the odometer reading, not how much was spent to get there. So a truck on this list can still be expensive to keep, and a truck that is not on it can be cheap. Longevity and cost are different questions.""",
   "Toyota Tacoma pickup", "LONGEVITY IS NOT COST")
sc("""For a buyer, the practical lesson is to use the ranking as a filter, not a verdict. If you want a truck to keep for a very long time, start with the group that sits near the top, the heavy-duty trucks, the Tundra and the Tacoma. Then check the exact model year, the engine, the recalls and the maintenance records. The study narrows the list from dozens of trucks to a handful. The rest is your own inspection.""",
   "Toyota Tundra pickup", "USE THE RANKING AS A FILTER")
sc("""And what about new trucks? The study can only look at trucks that have been on the road for years. A truck built in twenty twenty-six has no odometer history yet. So when you buy new, you are relying on the company's track record, the warranty, and the early reports. That is one more reason to read the warranty terms, and to check what happens if the model is discontinued, as the Nissan Titan was after the twenty twenty-four model year.""",
   "Nissan Titan pickup", "NEW TRUCKS HAVE NO HISTORY")

# ---------- THE BIG TWIST ----------
sc("""Now the twist we promised. Look at who is not on the list. The Ford F-one-fifty, the Chevrolet Silverado one thousand five hundred, the Ram one thousand five hundred and the GMC Sierra one thousand five hundred, the four best-selling pickups in America, are not among the top twelve in twenty twenty-six. In the earlier edition, they were between eleventh and fourteenth for the F-one-fifty, Sierra and Ram, with the Silverado at seventh.""",
   "Ford F-150 Chevrolet Silverado Ram 1500 pickups", "THE BEST SELLERS ARE NOT ON THE LIST")
sc("""That means the trucks that most Americans buy are not the ones that the study thinks are most likely to last. The heavy-duty trucks and the two Toyotas are. That does not mean the half-ton trucks are bad. Those four brands sold more than one and a half million pickups through nine months, heavy-duty included. It means that the work trucks, built for heavier loads, tend to survive longer, according to the model. A bigger frame and a bigger engine are built for more.""",
   "Ford F-150 pickup truck", "WORK TRUCKS LAST LONGER")
sc("""Think about what that means. If you tow, and haul, and plan to keep the truck for years, the heavy-duty trucks make sense. If you drive mostly on the highway, and the truck is a family vehicle, a half-ton truck is built for that, and the study says it is not the likeliest to reach two hundred fifty thousand. But how many families keep a truck that long? If you drive fifteen thousand miles a year, two hundred fifty thousand miles takes almost seventeen years.""",
   "Ram 1500 pickup truck", "250,000 MILES = ~17 YEARS AT 15,000/YR")

# ---------- CLOSE ----------
sc("""So what should you check before you buy a used truck in twenty twenty-seven? First, the service records, because a truck that was maintained is more likely to last than one that was not. Second, the recalls and the known problems for the exact engine. Third, the mileage and the age, together. And fourth, the price, because a truck that lasts is only a good deal if you do not overpay at the start.""",
   "Ford F-150 pickup", "CHECK 1, 2, 3 AND 4")
sc("""We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. It covers the numbers to check, the questions to ask a dealer, and the warning signs we walked through. The link is in the description and in the pinned comment. If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Only one truck in the whole study": "Intro", "Number one": "1. Ram 3500", "Number two": "2. Toyota Tundra",
      "Number three": "3. GMC Sierra HD", "Number four": "4. Toyota Tacoma", "Number five": "5. Ford Super Duty",
      "Number six": "6. Ram 2500 and Honda Ridgeline", "Now the twist we promised": "The best sellers are not on the list",
      "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video12", "length_scale": 1.6,
  "title": "Which Trucks Last the Longest? The 2026 Ranking (250,000 Miles)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
