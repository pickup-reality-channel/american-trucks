import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In nineteen seventy-eight, a red Dodge pickup with wooden trim and chrome exhaust stacks beat a Chevrolet Corvette to one hundred miles per hour. In nineteen ninety-one, a small GMC truck could reach sixty in about four point three seconds. In twenty twenty-six, Ram brought back a pickup with seven hundred seventy-seven horsepower. Muscle trucks have a long, wild history, and most people have forgotten the best part of it.""",
   "Dodge Lil Red Express", "MUSCLE TRUCKS NOBODY REMEMBERS")
sc("""Here are six muscle trucks that time forgot. Some were built for only one year. Some were hidden loopholes in the law. And some are quietly becoming valuable collector trucks right now. By the end, you will know which ones are still affordable, which ones already took off, and why the muscle truck is suddenly back in twenty twenty-six.""",
   "GMC Syclone", "6 FORGOTTEN MUSCLE TRUCKS")
sc("""Every number in this video comes from a published source, listed in the description. If we could not confirm a figure, we left it out. Let's start in the late seventies, when the government accidentally created the fastest American vehicle of its time.""",
   "Dodge pickup 1978", "EVERY NUMBER IS SOURCED")

# ---------- 1. LI'L RED EXPRESS ----------
sc("""Number one is the Dodge Li'l Red Express. Built for nineteen seventy-eight and nineteen seventy-nine. It looked like a hot rod from a cartoon: bright red paint, real wood trim on the bed, gold stripes, and two tall chrome exhaust stacks behind the cab, like a big rig. Under the hood was a five point nine liter V eight, Chrysler's three-sixty small block, rated at two hundred twenty-five horsepower.""",
   "Dodge Lil Red Express truck", "1. DODGE LI'L RED EXPRESS")
sc("""That does not sound like much today. But in the late seventies, emissions rules had choked most American performance cars. Here is the twist. According to a report published in twenty twenty-six, the nineteen seventy-eight model did not need a catalytic converter, because of a loophole in the emission rules that excluded trucks with a gross vehicle weight of more than six thousand one hundred pounds. The pickup could breathe when the cars could not.""",
   "Dodge Lil Red Express exhaust stacks", "TWIST: THE WEIGHT LOOPHOLE")
sc("""Why did Dodge build it at all? In the late seventies, custom vans and trucks were a huge trend, and Dodge's Adult Toys line was built to catch young buyers who wanted something wild. The Li'l Red Express was designed as a style statement first. Its performance, thanks to the loophole, turned out to be the bonus that made it a legend.""",
   "Dodge Lil Red Express wood bed", "BUILT AS A STYLE STATEMENT")
sc("""The result was astonishing. The truck reached one hundred miles per hour in nineteen point nine seconds. It was called the fastest American production vehicle of any shape or size to get to one hundred miles per hour, and in a nineteen seventy-eight Car and Driver test, it beat the Chevrolet Corvette. A pickup truck with wood on the bed outran America's sports car.""",
   "Dodge Lil Red Express red", "0-100 MPH: 19.9 SECONDS")
sc("""It did not last. For nineteen seventy-nine, the Li'l Red Express got a catalytic converter, and some of the magic was gone. In total, seven thousand three hundred sixteen were built. Two thousand one hundred eighty-eight for nineteen seventy-eight, and five thousand one hundred eighty-eight for nineteen seventy-nine.""",
   "Dodge Lil Red Express pickup", "7,316 BUILT IN TWO YEARS")
sc("""And here is the surprise for buyers. According to that same twenty twenty-six report, you can pick one up today for less than thirty thousand dollars, and some examples have sold for about half that. For a truck that started the performance pickup movement, that is cheap. If you want a piece of muscle truck history without a six-figure budget, this is where it starts.""",
   "Dodge Lil Red Express classic", "2026: UNDER $30,000")

# ---------- 2. SHELBY DAKOTA ----------
sc("""Number two is the Shelby Dakota, from nineteen eighty-nine. Carroll Shelby, the man behind the Shelby Cobra and the Shelby Mustang, was working with Chrysler at the time. His team took the midsize Dodge Dakota and turned it into a sport truck. According to Carscoops, it was the first Dakota ever fitted with a V eight.""",
   "Shelby Dakota", "2. SHELBY DAKOTA, 1989")
sc("""The engine was a five point two liter V eight with one hundred seventy-five horsepower and two hundred seventy pound-feet of torque, sent to the rear wheels through a four-speed transmission. It also had Shelby styling, special wheels and stripes. And according to Carscoops, it was the first V eight, rear-drive vehicle Shelby had worked on in decades.""",
   "Dodge Dakota Shelby", "5.2L V8, 175 HP")
sc("""Production was tiny. According to Carscoops, only one thousand four hundred seventy-five were made, in a single year of production. And here is a fun twist. The very first one built was sold to a private customer and later bought back by Shelby American. It was said to have been driven by Carroll Shelby himself, and it came with an Arizona speeding ticket issued to the company's chief executive.""",
   "Shelby Dakota pickup white", "ONLY 1,475 BUILT")
sc("""Why do people forget it? Because Shelby's name is tied to Mustangs and Cobras, and because one hundred seventy-five horsepower does not sound impressive today. But the Shelby Dakota proved something important: a small truck could be a performance vehicle. It opened the door for the next truck on this list, which took the idea much further.""",
   "Shelby Dakota truck", "THE DOOR-OPENER")

# ---------- 3. SYCLONE ----------
sc("""There is a lesson in the Shelby Dakota for buyers today. Limited production numbers alone do not guarantee high value. A truck has to be remembered, wanted, and well documented. The Shelby Dakota is rare, but because so few people know about it, it can still be found for much less than the famous Shelby cars.""",
   "Shelby Dakota red", "RARE IS NOT ALWAYS VALUABLE")
sc("""Number three is the GMC Syclone, from nineteen ninety-one. It was based on the small GMC Sonoma pickup, the sister truck of the Chevy S-ten. But under the skin, it was something else. A turbocharged V six, all-wheel drive, and a lowered stance. According to V E H Q, it could reach sixty miles per hour in about four point three seconds.""",
   "GMC Syclone", "3. GMC SYCLONE, 1991")
sc("""That number put a small pickup in the same range as the fastest sports cars of its era. And it was built in tiny numbers. According to V E H Q, GMC built fewer than three thousand Syclones in nineteen ninety-one. GMC also made an S U V version, the Typhoon, using the same powertrain.""",
   "GMC Syclone black", "FEWER THAN 3,000 BUILT")
sc("""Here is the twist. The Syclone was not a perfect truck. Its payload was small, and it was more of a street machine than a tool. But that is exactly why collectors love it today. According to Hagerty figures cited by V E H Q, a Syclone was valued at about thirty thousand nine hundred dollars in July twenty twenty-four, and one sold at auction for one hundred thirty thousand dollars in May twenty twenty-five.""",
   "GMC Syclone pickup", "TOP AUCTION: $130,000")
sc("""The gap between the average and the top sale tells the story. A tired Syclone is a fun truck. A perfect, low-mile one is a serious collector car. If you are shopping, condition and documentation are everything, because the difference can be one hundred thousand dollars.""",
   "GMC Typhoon", "CONDITION IS EVERYTHING")

# ---------- 4. 454 SS ----------
sc("""Number four is the Chevrolet four fifty-four S S, built from nineteen ninety to nineteen ninety-three. Chevrolet's answer to the idea of a full-size muscle truck. A regular cab, short bed, mostly black truck with a seven point four liter V eight. According to The Truth About Cars, it got about eight miles per gallon, and General Motors built about seventeen thousand of them.""",
   "Chevrolet 454 SS pickup", "4. CHEVY 454 SS, 1990-1993")
sc("""For years, it was just a thirsty old truck. Then nostalgia arrived. According to Hagerty valuation figures cited by V E H Q, a nineteen ninety-one four fifty-four S S in excellent condition was worth about twenty-three thousand seven hundred dollars in twenty nineteen, and about sixty thousand four hundred in early twenty twenty-six.""",
   "Chevrolet 454 SS black", "$23,700 TO $60,400")
sc("""And the twist: Hagerty still sees room to grow. In December twenty twenty-five, the four fifty-four S S was named on Hagerty's twenty twenty-six Bull Market list, a selection of eleven vehicles expected to rise in value. A truck that people once laughed at for its fuel economy is now on the most watched list in collector cars.""",
   "Chevrolet C1500 454 SS", "HAGERTY 2026 BULL MARKET LIST")
sc("""Why is it so forgotten, then? Because Ford's S V T Lightning, which arrived in nineteen ninety-three, got more attention and more magazine covers. The four fifty-four S S was there first, and for a while, it lived in the Lightning's shadow. Now, buyers are rediscovering it, and prices show it.""",
   "Ford SVT Lightning 1993", "LIVING IN THE LIGHTNING'S SHADOW")

# ---------- 5. SILVERADO SS ----------
sc("""One more detail makes the four fifty-four S S special. It was a regular cab, short bed truck, the simplest and lightest full-size layout. Today, that layout is rare in new trucks, because most buyers choose crew cabs. That makes clean, original short-bed trucks from the early nineties even more appealing to collectors who want that classic shape.""",
   "Chevrolet 454 SS regular cab", "THE SHORT-BED SHAPE")
sc("""Number five is the Chevrolet Silverado S S, from two thousand three to two thousand seven. Many truck fans do not even know it existed. According to Driving Line, it had a six liter V eight with three hundred forty-five horsepower and three hundred eighty pound-feet of torque, and all-wheel drive borrowed from the G M C Denali and the Cadillac Escalade.""",
   "Chevrolet Silverado SS", "5. CHEVY SILVERADO SS, 2003-2007")
sc("""According to Driving Line, it could reach sixty miles per hour in the low six second range. Fast for a full-size truck in the early two thousands. A cheaper rear-wheel drive version was added in two thousand five. It had a sport suspension, wide tires and a body kit that made it look lower and meaner than a normal Silverado.""",
   "Chevrolet Silverado SS 2003", "0-60 IN THE LOW 6s")
sc("""Here is the twist. It was squeezed from both sides. Ford had the supercharged S V T Lightning, and Dodge had the Viper-powered Ram, which we are about to meet. Against those two, the Silverado S S looked mild. Driving Line called it a milder alternative to the Lightning and the S R T ten. It did not win the horsepower war, so people forgot it.""",
   "Chevrolet Silverado SS red", "SQUEEZED FROM BOTH SIDES")
sc("""But that is also what makes it interesting today. According to Driving Line, used examples are still in fairly high demand, though it does not have quite the collector appeal of the Lightning or the S R T ten. That usually means a lower price for a buyer. For someone who wants an all-wheel drive V eight muscle truck that can still be used every day, it is a hidden option.""",
   "Chevrolet Silverado SS truck", "A HIDDEN OPTION")

# ---------- 6. RAM SRT-10 ----------
sc("""Number six is the craziest of them all. The Dodge Ram S R T ten, built from two thousand four to two thousand six. Dodge put a giant V ten engine into its light-duty Ram pickup. According to Hagerty, it was an eight point three liter V ten making five hundred horsepower, the same displacement as the Dodge Viper sports car.""",
   "Dodge Ram SRT-10", "6. DODGE RAM SRT-10, 2004-2006")
sc("""And here is the first twist. According to Hagerty, the truck's V ten shared little with the Viper's engine beyond the bore spacing and displacement, and the Viper engine was cast from aluminum. So it was a Viper engine in spirit more than in parts. Dodge launched it first as a regular cab with a six-speed manual, and added a Quad Cab with an automatic in two thousand five.""",
   "Dodge Ram SRT-10 Viper engine", "500 HP V10")
sc("""Collectors noticed it before most people did. According to Hagerty in twenty twenty-one, number two condition values had risen forty-six percent to fifty-four thousand two hundred dollars for regular cabs, and eleven percent to thirty-one thousand seven hundred for Quad Cabs. Over five years, regular cabs were up one hundred seventeen percent.""",
   "Dodge Ram SRT-10 pickup", "REGULAR CAB: +117% IN 5 YEARS")
sc("""And the S R T ten earned a reputation as a wild machine. A five hundred horsepower pickup with a six-speed manual was something no other company offered. It was loud, fast and thirsty, and it made no sense as a work truck. But that was never the point. It was built to show what Dodge could do, and it made people talk about the Ram brand.""",
   "Dodge Ram SRT-10 red", "BUILT TO MAKE PEOPLE TALK")
sc("""The second twist is who was buying. According to Hagerty, Gen Xers and millennials made up sixty percent of the collectors for this truck, and sixty-six percent of insurance quotes. The S R T ten was bought by people who saw it in magazines and video games as teenagers. Like almost every muscle truck on this list, its value is driven by memory.""",
   "Dodge Ram SRT-10 black", "GEN X + MILLENNIALS: 60%")

# ---------- THE COMEBACK ----------
# ---------- MENTION ----------
sc("""Before we get to twenty twenty-six, one honorable mention that is not forgotten at all, and that is the point. The Ford S V T Lightning. Ford built it from nineteen ninety-three to ninety-five, and again from ninety-nine to two thousand four with a supercharged V eight. It became the most famous muscle truck of its era, and its values show it.""",
   "Ford SVT Lightning", "MENTION: FORD SVT LIGHTNING")
sc("""According to Ford Authority in February twenty twenty-six, the average value of a number two condition second-generation Lightning went from around twenty thousand dollars in twenty sixteen to forty-eight thousand seven hundred by twenty twenty-four. The first generation went from about fifteen thousand to forty-two thousand four hundred. And millennials were the largest group of buyers, at forty percent of the first-generation market.""",
   "Ford SVT Lightning red", "LIGHTNING: $20K TO $48,700")
sc("""Here is why it matters for this list. The Lightning shows where the forgotten trucks could go. Once a muscle truck becomes famous among collectors, its price can more than double in a few years. The Silverado S S and the Li'l Red Express are still cheap because they are still forgotten. That may not last.""",
   "Ford SVT Lightning pickup", "WHERE FORGOTTEN TRUCKS COULD GO")
sc("""So why does this matter in twenty twenty-six? Because the muscle truck is back, and it is bigger than ever. According to Pickup Truck Talk, in January twenty twenty-six, Ram announced the return of the T R X, now with an S R T badge, for the twenty twenty-seven model year. It has a supercharged six point two liter V eight with seven hundred seventy-seven horsepower and six hundred eighty pound-feet of torque.""",
   "Ram 1500 TRX", "2027 RAM TRX: 777 HP")
sc("""And the price shows how far muscle trucks have come. According to Pickup Truck Talk, the new T R X lands just shy of one hundred thousand dollars before destination fees and likely dealer markups. Compare that with the Li'l Red Express, which you can buy today for under thirty thousand. The new muscle truck costs more than three of the old ones.""",
   "Ram TRX pickup", "NEW TRX: ~$100,000")
sc("""Here is the twist that connects all of this. The T R X came back after a short break, and Ram also brought back its Hemi V eight in twenty twenty-five after dropping it for a year. According to Carscoops, Ram received over ten thousand orders in the first twenty-four hours after announcing the Hemi's return. Buyers keep telling truck companies the same thing: they want V eight power.""",
   "Ram 1500 Hemi", "BUYERS WANT V8 POWER")
sc("""And Ford has its own super trucks, like the Raptor, which turned off-road performance into a big business. The modern muscle truck is no longer a rare, one-year experiment. It is a permanent, profitable part of the lineup. The forgotten trucks on this list are the reason it exists.""",
   "Ford F-150 Raptor", "FROM EXPERIMENT TO BUSINESS")

# ---------- PATTERN ----------
sc("""So what is the pattern? Every forgotten muscle truck was built in small numbers, for a short time, and often sold poorly when new. The Li'l Red Express lasted two years. The Shelby Dakota and the Syclone lasted one. The S R T ten lasted three. They were too expensive, too thirsty, or too impractical for most buyers at the time.""",
   "Dodge Lil Red Express GMC Syclone", "SHORT RUNS, SMALL NUMBERS")
sc("""And that is exactly why they are rising now. Small production means few survivors. The buyers who wanted them as teenagers now have money. And the trucks are simple enough to restore and enjoy. The muscle trucks that failed in the showroom are winning at auction decades later.""",
   "Chevrolet 454 SS Dodge Ram SRT-10", "FAILED NEW, WINNING NOW")

sc("""There is a strange connection between all of these trucks: rules. The Li'l Red Express used an emissions loophole for heavy trucks. Later muscle trucks were built just as fuel economy rules were tightening. And today's T R X returns at a time when many rivals are moving to smaller turbocharged engines. Muscle trucks have always lived in the gaps between regulations.""",
   "Ram TRX", "MUSCLE TRUCKS LIVE IN THE GAPS")
sc("""Another connection is price. When new, most of these trucks cost more than a normal pickup, but less than a true sports car. That made them a back door into performance for buyers who needed a truck anyway. A muscle truck could haul on Saturday and race on Sunday, at least in theory.""",
   "Chevrolet 454 SS", "A BACK DOOR TO PERFORMANCE")
sc("""And there is the insurance angle. According to Insure dot com data, the Ram fifteen hundred T R X was the second most expensive truck to insure in twenty twenty-six, at three thousand two hundred fifty-five dollars a year, and the Ford F-one-fifty Raptor cost two thousand six hundred eighty-two. Performance trucks cost more to own, not just to buy.""",
   "Ford F-150 Raptor", "TRX INSURANCE: $3,255/YEAR")
sc("""For classic muscle trucks, insurance works differently. Collector policies are often much cheaper than regular policies, but they come with limits, like restricted mileage and secure storage. If you buy a forgotten muscle truck as a weekend toy, ask about a collector policy. It can make owning one far more affordable.""",
   "classic truck garage", "COLLECTOR INSURANCE CAN HELP")
sc("""And finally, think about parts. Some of these trucks, like the four fifty-four S S and the Silverado S S, share many parts with normal Chevrolet trucks, which makes them easier to keep running. Rare trucks like the Syclone and the Shelby Dakota have special parts that can be hard to find. Before you buy, find out where the hard-to-get parts will come from.""",
   "Chevrolet Silverado SS", "CHECK PARTS AVAILABILITY")

sc("""Before you buy any forgotten muscle truck, get a pre-purchase inspection from a mechanic who knows older trucks. Check for rust in the frame and the bed, look for signs of hard racing, and confirm the engine and transmission numbers match the paperwork. A matching-numbers truck with clean records is usually worth far more than one with a swapped engine, even if both look the same in photos.""",
   "classic pickup truck inspection", "GET A PRE-PURCHASE INSPECTION")

# ---------- CLOSE ----------
sc("""So if you want a muscle truck, old or new, here is what to check in twenty twenty-seven. First, check originality. On a collector truck, the original engine, paint and trim can be worth tens of thousands of dollars. Second, check the trend. Use a valuation tool to see whether the truck is rising, flat or falling.""",
   "classic pickup truck show", "CHECKS 1 AND 2: ORIGINAL, TREND")
sc("""Third, count the running costs. Eight miles per gallon, like the four fifty-four S S, adds up quickly. Fourth, on a new truck like the T R X, watch out for dealer markups above the sticker price. And fifth, decide what you want: a weekend toy, an investment, or a daily driver. Each one points to a different truck on this list.""",
   "Ram TRX dealership", "CHECKS 3, 4 AND 5")
sc("""We put all of these checks, for new and used trucks, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, about the most expensive pickups you can buy right now. And tell us in the comments: which forgotten muscle truck would you put in your garage? Thanks for watching.""",
   "Dodge Lil Red Express", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In nineteen seventy-eight": "Intro", "Number one": "1. Dodge Li'l Red Express", "Number two": "2. Shelby Dakota",
      "Number three": "3. GMC Syclone", "Number four": "4. Chevrolet 454 SS", "Number five": "5. Chevrolet Silverado SS",
      "Number six": "6. Dodge Ram SRT-10", "Before we get to twenty twenty-six": "Honorable mention: Ford SVT Lightning", "So why does this matter": "The muscle truck is back (2027 Ram TRX)",
      "So if you want a muscle truck": "What to check before you buy in 2027"}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": "video47", "length_scale": 1.45,
  "title": "6 Muscle Trucks Nobody Remembers (One Beat a Corvette)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
