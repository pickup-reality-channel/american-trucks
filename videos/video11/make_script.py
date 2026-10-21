import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""Five pickup trucks that the data says are worth buying in twenty twenty-seven. One keeps eighty percent of its value after five years. One starts under thirty thousand dollars and has a hybrid engine. One was named first for dependability by one study, and second by another. And one has a catch that most buyers never hear about. Here are the trucks worth buying, with the real numbers and the real warnings.""",
   "Toyota Tacoma pickup", "5 TRUCKS WORTH BUYING IN 2027")

# ---------- COLD OPEN ----------
sc("""There are a lot of lists of the best trucks, and most of them are opinions. This one is different, because every pick comes with numbers from a published source, and every pick also comes with a warning. A truck that is worth buying for one buyer can be the wrong truck for another. So for each one, we will tell you who it is for, who should look somewhere else, and what to check.""",
   "Ford F-150 pickup truck", "EVERY PICK COMES WITH A WARNING")
sc("""We drew on the sales table from Pickup Truck Talk, the iSeeCars resale study, the J.D. Power dependability study, the Pickup Truck Talk reliability ranking from July, the Autoblog price list, and the TFL Car price analysis. Every source is listed in the description. We did not drive these trucks for this video. This is about what the published data says, and where the data disagrees with itself.""",
   "Chevrolet Silverado 1500 pickup", "SOURCES IN THE DESCRIPTION")
sc("""And there is a twist, because the data does disagree. One study ranks the Ram one thousand five hundred first for dependability. Another ranks the Ford F-one-fifty first. One names the Toyota Tundra among the best at keeping its value, and the other puts it last for reliability. So a good list has to be honest about conflicts. Stay with me, because the last pick is a truck that most lists would not include.""",
   "Ram 1500 pickup truck", "THE DATA DISAGREES")

# ---------- 1. TOYOTA TACOMA ----------
sc("""Pick number one is the Toyota Tacoma. It is the best-selling midsize truck in America, with two hundred fourteen thousand, eight hundred seventy-five sold through nine months of twenty twenty-six, up five point one percent. And according to iSeeCars, it keeps eighty and a half percent of its value after five years, which is the best of any truck in the study. SlashGear calls it the fourth-best vehicle of any kind at holding value.""",
   "Toyota Tacoma TRD pickup", "TACOMA: 80.5% RESALE")
sc("""There is also a hybrid. The Tacoma Hybrid grew four hundred three percent in the first nine months of twenty twenty-five, to twenty-two thousand, seven hundred seventy-three, according to Autoblog, and makes three hundred twenty-six horsepower. And the price barely moved. TFL Car found that the popular SR5 trim cost thirty-nine thousand, four hundred fifty dollars in twenty twenty-six, up seven tenths of a percent from twenty twenty-four.""",
   "Toyota Tacoma Hybrid pickup", "SR5: $39,450 (+0.7% IN 2 YEARS)")
sc("""Who is it for? The buyer who wants a truck that holds its value, with a simple, proven nameplate. Who should look elsewhere? A buyer who needs serious towing, because the Tacoma tows up to six thousand, five hundred pounds, about twelve hundred less than the Colorado. And the twist is the price. The starting price is thirty-two thousand, one hundred forty-five dollars, but the popular SR5 trim costs more than seven thousand dollars above that.""",
   "Toyota Tacoma pickup truck", "WHO: VALUE KEEPERS. NOT: HEAVY TOWERS.")

# ---------- 2. FORD MAVERICK HYBRID ----------
sc("""Pick number two is the Ford Maverick Hybrid. It is the cheapest truck you can actually buy, starting at twenty-eight thousand, one hundred forty-five dollars, with forty-two miles per gallon in the city, according to Autoblog. Ford sold seventy-four thousand, three hundred of them through nine months of twenty twenty-six, a record, and in the third quarter the hybrid was about two thirds of every Maverick sold.""",
   "Ford Maverick Hybrid pickup", "MAVERICK HYBRID: FROM $28,145")
sc("""The Maverick keeps sixty-eight point two percent of its value after five years, according to iSeeCars, which is better than any other compact truck on the list. And unlike many cheap vehicles, it has real demand. Ford sold one hundred twenty-three thousand, six hundred eighty-one Mavericks through nine months, more than any midsize truck except the Tacoma. A cheap truck with a market behind it is a safer purchase.""",
   "Ford Maverick pickup", "MAVERICK: 123,681 SOLD")
sc("""Who is it for? A first-time buyer, a city driver, a buyer who wants to save on fuel and does not need a big bed. Who should look elsewhere? Anyone who tows a heavy trailer, because the sources list a payload of fifteen hundred pounds. And the twist is the competition. Its only compact rival, the Hyundai Santa Cruz, sold fourteen thousand, eight hundred eleven in the same period, and reports say it is being phased out.""",
   "Ford Maverick Lariat pickup", "WHO: CITY DRIVERS. NOT: HEAVY TOWERS.")

# ---------- 3. FORD F-150 ----------
sc("""Pick number three is the Ford F-one-fifty. Pickup Truck Talk ranked it the most reliable current full-size truck in July, calling the result a surprise. The reason, according to the article, is that it has no single widespread engine failure pattern, like the GM six point two liter V eight or the Toyota twin-turbo V six. J.D. Power's twenty twenty-five quality and reliability score for the F-one-fifty is eighty-six out of one hundred, tied for the best of the five.""",
   "Ford F-150 XLT pickup", "F-150: MOST RELIABLE (PUTT, JULY 2026)")
sc("""It also has choices. There is a hybrid, which sold thirty-four thousand, five hundred twenty-seven through nine months, and a price that has barely moved. According to TFL Car, the F-one-fifty XLT cost fifty-two thousand, five hundred ninety dollars in twenty twenty-six, up six percent from twenty twenty-four, and down nine tenths of a percent after inflation. In the same period, the Silverado LT rose twelve point six percent.""",
   "Ford F-150 Hybrid pickup", "F-150 XLT: +6% VS SILVERADO +12.6%")
sc("""Who is it for? The buyer who wants the most mainstream full-size truck, with options. Who should look elsewhere? A buyer who cares most about resale value, because iSeeCars shows the F-one-fifty keeping sixty-one point four percent after five years, about nineteen points below the Tundra. And the twist is the fine print. Pickup Truck Talk notes recurring ten-speed transmission complaints, hub-bolt recalls and a high number of recalls.""",
   "Ford F-150 Lariat pickup", "CATCH: TRANSMISSION COMPLAINTS, RECALLS")

# ---------- 4. RAM 1500 ----------
sc("""Pick number four is the Ram one thousand five hundred, and it is the most debated. The twenty twenty-six J.D. Power Vehicle Dependability Study ranked it first among its truck group, up from fourth place, with Ram saying it improved thirteen points in a year. The study surveyed thirty-three thousand, two hundred sixty-eight owners of twenty twenty-three model year vehicles, after three years of ownership.""",
   "Ram 1500 pickup", "RAM 1500: #1 IN JD POWER 2026 VDS")
sc("""And it has momentum. Ram pickups sold three hundred twenty-five thousand, three hundred forty-eight through nine months, up twenty-four percent, and the light-duty Ram jumped forty-one percent. The Big Horn cost forty-nine thousand, five hundred forty-one dollars in twenty twenty-six, according to TFL Car. That is a drop of six tenths of a percent after inflation, and about three thousand dollars less than the F-one-fifty XLT.""",
   "Ram 1500 Big Horn pickup", "RAM LD: +41%. BIG HORN: $49,541")
sc("""Now the warning, and it is a serious one. Pickup Truck Talk ranked the Ram second in its own reliability list, citing mostly electronics and build quality problems, and an ABS software recall that covered over a million trucks. The J.D. Power twenty twenty-five quality and reliability score for the Ram is seventy-seven, the lowest of the five. And Consumer Reports, according to that article, placed the latest Ram near the bottom.""",
   "Ram 1500 Rebel pickup", "CATCH: JD POWER Q&R 77, LOWEST OF 5")
sc("""So who is it for? A buyer who values the price, the ride and the momentum, and who is willing to check the specific model year for recalls and problems. Who should look elsewhere? Anyone who wants the safest reliability record across several sources. And the twist is the tie between two opposite stories. One study says first, and another says near the bottom. Both are published, and a careful buyer reads both.""",
   "Ram 1500 pickup truck", "WHO: VALUE BUYERS. NOT: RISK-AVOIDERS.")

# ---------- 5. HEAVY DUTY ----------
sc("""Pick number five is a group that most lists skip, the heavy-duty trucks, and the reason is resale. On the iSeeCars list, the Ram three thousand five hundred keeps seventy-nine point eight percent of its value after five years, the Ford F-three-fifty seventy-nine point six, the F-four-fifty seventy-seven, the F-two-fifty seventy-five point seven, and the Ram two thousand five hundred seventy-four point nine. That is far better than the half-ton trucks, which lose close to forty percent.""",
   "Ram 3500 Heavy Duty pickup", "HEAVY DUTY: 75% TO 80% RESALE")
sc("""There is a catch, and it is in the sales. The heavy-duty Silverado fell thirteen percent through nine months, to one hundred thirty-three thousand, seven hundred sixty-nine, and the heavy-duty Sierra fell seven point seven. The heavy-duty Ram rose three point four percent. So the work truck market is shrinking at two of the three Detroit companies, even while the trucks hold their value. A buyer who needs a heavy-duty truck should buy it for work, not as an investment.""",
   "Chevrolet Silverado HD pickup", "SILVERADO HD -13%. RAM HD +3.4%")
sc("""Who is it for? Someone who tows or hauls heavy loads every week, and plans to keep the truck for years. Who should look elsewhere? A daily commuter, because a heavy-duty truck costs more to buy and to run. And the twist is the price of entry. Without a published price in our sources, we will not quote one. But a buyer should compare the cost of the heavy-duty with the resale value, because that is where it can pay off.""",
   "Ford F-350 Super Duty pickup", "WHO: WEEKLY HEAVY USERS.")


# ---------- THE SCORECARD ----------
sc("""Let's put the five picks on one scorecard. On resale, the Tacoma keeps eighty and a half percent after five years, the heavy-duty trucks keep between seventy-five and almost eighty, the Maverick sixty-eight, and the Ram and the Ford about sixty-one to sixty-two. On the starting price, the Maverick is lowest at twenty-eight thousand, one hundred forty-five, and the Tacoma next at thirty-two thousand, one hundred forty-five.""",
   "Toyota Tacoma Ford Maverick pickups", "SCORECARD: RESALE AND PRICE")
sc("""On sales momentum, the Ram is the leader, up twenty-four percent through nine months, with the Maverick growing two point three and the Tacoma five point one. And the Ford F-Series, down six point eight percent without the Lightning, is still the biggest of all, at five hundred fifty-six thousand, seven hundred thirty-eight. On reliability, the sources disagree, and we showed each one. That scorecard has no perfect row, and that is the point.""",
   "Ram 1500 Ford F-150 pickups", "SCORECARD: SALES MOMENTUM")
sc("""Why do the reliability sources disagree? Because they measure different things. J.D. Power's dependability study asks owners of three-year-old trucks about problems they had, and counts them per one hundred vehicles. Pickup Truck Talk's ranking weighs its own reporting, recalls, investigations, complaints, repair cost and whether problems persist across model years. One counts how often something goes wrong. The other also weighs how serious it is. Both are useful, and neither is the whole answer.""",
   "Ford F-150 pickup truck", "WHY THE SOURCES DISAGREE")
sc("""Look at the example of the Ram. A truck can have many small problems, like a screen that freezes, and rank poorly with owners who are annoyed. Another truck can have fewer problems, but one serious failure, like an engine that needs replacement, and rank poorly with a reporter who tracks repair cost. A smart buyer asks two questions. How often does it go wrong, and how bad is it when it does?""",
   "Ram 1500 pickup truck", "HOW OFTEN? HOW BAD?")
sc("""There is also the matter of the model year. The J.D. Power study looked at twenty twenty-three model year trucks. That is not the truck you will buy in twenty twenty-seven. Companies change engines, transmissions and software every year or two. So use these studies as a signal about a company's direction, and then check the recalls and complaints for the exact year you want to buy. That is a free check, and it takes ten minutes.""",
   "Chevrolet Silverado pickup", "THE MODEL YEAR MATTERS")
sc("""And one more thing about warnings. Every truck on this list has a recall history, and so does every truck on every other list. A recall is not always a reason to avoid a truck. It is a reason to check that the repair was done. When you buy a used truck, ask for the record of open recalls. When you buy a new one, ask whether any are known. The existence of a recall is normal. A recall that nobody fixed is the problem.""",
   "Ford F-150 pickup", "A RECALL IS NOT A VERDICT")

# ---------- THE TRUCK WE LEFT OUT ----------
sc("""You may have noticed what is missing, the Toyota Tundra. It keeps eighty and three tenths percent of its value after five years, according to iSeeCars, almost the same as the Tacoma. But Pickup Truck Talk ranked it last of the five full-size trucks for reliability, because of twin-turbo V six failures that in some cases required a complete engine replacement. And J.D. Power's dependability study did not list it.""",
   "Toyota Tundra pickup", "TUNDRA: BEST RESALE, WORST RELIABILITY RANK")
sc("""That is the lesson of this list. The best truck on paper depends on what you measure. If you measure resale, the Toyotas win. If you measure reliability by one source, the Ford wins. If you measure price and momentum, the Ram wins. If you measure the lowest price you can actually buy, the Maverick wins. No truck wins everything, and the honest answer to which truck is worth buying is the one that fits your own priorities.""",
   "Toyota Tacoma Ford F-150 Ram 1500 pickups", "NO TRUCK WINS EVERYTHING")
sc("""Here is a way to decide in five minutes. Write down your three priorities, for example price, resale and towing. Then look up the exact numbers for the three trucks you like, from the sources in this video. And write the warnings next to each one. A truck with one clear warning that you can live with is a better choice than a truck with no warnings that you could not find.""",
   "Ford F-150 pickup", "DECIDE IN FIVE MINUTES")

# ---------- CLOSE ----------
sc("""So what should you check before you buy in twenty twenty-seven? First, the recalls on the exact model year. Second, the full price with the destination fee. Third, the five-year resale value. And fourth, the towing and payload numbers for the exact configuration. We put all of this into a checklist, the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment.""",
   "Chevrolet Silverado 1500", "CHECK 1, 2, 3 AND 4")
sc("""If you want to know which engines to avoid in a used truck, subscribe, because that is coming soon. And if you think we missed a truck that deserves a place on this list, tell us in the comments, and tell us which number we should check. Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"Five pickup trucks that the data": "Intro", "Pick number one": "1. Toyota Tacoma", "Pick number two": "2. Ford Maverick Hybrid",
      "Pick number three": "3. Ford F-150", "Pick number four": "4. Ram 1500", "Pick number five": "5. Heavy-duty trucks",
      "You may have noticed": "The truck we left out", "So what should you check": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, sc_ in enumerate(S):
    if idx in CUTS: sc_["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video11", "length_scale": 1.89,
  "title": "5 Pickups Actually Worth Buying in 2027 (And the Warning for Each)", "scenes": S},
  open("script.json", "w"), indent=1)
print(len(S), "scenes", sum(len(s["text"].split()) for s in S), "words")
