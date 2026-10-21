import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""In twenty twenty-two, Ford launched a new pickup for nineteen thousand, nine hundred ninety-five dollars. Four years later, the same truck starts at twenty-seven thousand, one hundred forty-five, before destination. The cheapest full-size pickups now start near forty thousand. And the cheapest new truck in America may soon be one with manual windows and no radio. So what happened to cheap trucks?""",
   "Ford Maverick 2022", "$19,995 → $27,145")

# ---------- COLD OPEN ----------
sc("""For decades, the pickup was the affordable vehicle. A basic regular cab work truck was what farmers, tradespeople and first-time buyers could afford. Today, according to Kelley Blue Book, the average new full-size pickup sells for sixty-seven thousand, five hundred seventy-three dollars, and the average small or midsize pickup for forty-three thousand, seven hundred ninety.""",
   "1988 Chevrolet pickup", "FULL-SIZE AVERAGE: $67,573")
sc("""In this video, we look at what really happened to cheap trucks. How much prices actually rose after inflation, which cheap trucks disappeared, who still sells an affordable pickup in twenty twenty-six, and the new wave of trucks trying to bring prices back down. Some of the answers are not what you would expect. Every number is sourced in the description.""",
   "Ford Ranger 1990s", "WHAT HAPPENED?")
sc("""And here is the first surprise. Part of the story is not that cheap trucks got expensive. It is that buyers stopped buying the cheap ones, and automakers stopped making them. Let's start with the numbers.""",
   "Chevrolet Silverado WT", "BUYERS STOPPED BUYING THEM")

# ---------- 1. THE MAVERICK ----------
sc("""The Ford Maverick is the perfect example. It launched for the twenty twenty-two model year with an XL starting price of nineteen thousand, nine hundred ninety-five dollars before destination, according to Pickup Truck plus SUV Talk. It was a compact hybrid pickup that cost less than many small cars. Buyers rushed to order it.""",
   "Ford Maverick XL 2022", "2022 MAVERICK: $19,995")
sc("""By twenty twenty-six, the cheapest Maverick, the XL with the EcoBoost engine and front-wheel drive, started at twenty-seven thousand, one hundred forty-five dollars, plus a one thousand six hundred ninety-five dollar destination charge. That is a thirty-six percent increase in four years. Ford said the price remained below the key thirty thousand dollar affordability threshold. Pickup Truck Talk's Tim Esterdahl wrote that he remembered that threshold as twenty thousand.""",
   "Ford Maverick 2026", "2026 MAVERICK: $27,145 (+36%)")
sc("""And look at the top of the Maverick range. According to Pickup Truck Talk, twenty twenty-six Maverick prices run from twenty-seven thousand, one hundred forty-five for the XL to forty-one thousand, four hundred twenty-five dollars for the Lobo with the top package. The Tremor starts at forty thousand, six hundred forty-five. So the most expensive Maverick costs more than the base price of a full-size F-150. The affordable truck now has a luxury version.""",
   "Ford Maverick Lobo 2025", "TOP MAVERICK: $41,425")
sc("""The hybrid, which was the standard engine at launch, now costs more. For twenty twenty-six, the XL Hybrid starts at twenty-eight thousand, one hundred forty-five dollars, a thousand more than the XL EcoBoost, according to Ford Authority. And Ford made front-wheel drive standard on EcoBoost models, and removed the spare tire from some all-wheel-drive trims. Those are the kinds of cuts automakers make to protect a price.""",
   "Ford Maverick XLT Hybrid", "NO SPARE TIRE ON SOME TRIMS")
sc("""Here is the twist. Ford actually cut Maverick prices for twenty twenty-six. According to Ford Authority, the XL EcoBoost dropped one thousand dollars, the Lariat EcoBoost dropped four thousand, two hundred twenty dollars, and the destination charge fell by two hundred seventy dollars. So even after a price cut, the cheapest Maverick still costs more than seven thousand dollars above its launch price.""",
   "Ford Maverick Lariat", "EVEN AFTER A $1,000 CUT")
sc("""And Jalopnik's calculation in twenty twenty-five showed what buyers actually pay. With the destination fee and a six hundred ninety-five dollar acquisition fee, the cheapest twenty twenty-five Maverick came to thirty thousand, five hundred thirty-five dollars. Jalopnik still called it the cheapest new pickup truck you could buy that year. The cheapest truck in America had crossed thirty thousand dollars.""",
   "Ford Maverick XL", "REAL PRICE: $30,535")

# ---------- 2. THE CHEAPEST TRUCKS NOW ----------
sc("""So what are the cheapest trucks now? Jalopnik's list of the five cheapest new pickups put the Maverick first, followed by the Hyundai Santa Cruz at thirty thousand, nine hundred ninety-five dollars with destination, the Toyota Tacoma SR at thirty-three thousand, one hundred eighty-five, the Chevrolet Colorado at thirty-three thousand, five hundred ninety-five, and the Nissan Frontier at thirty-three thousand, eight hundred forty-five.""",
   "Hyundai Santa Cruz", "THE 5 CHEAPEST: ALL $30K+")
sc("""Here is the twist on the Colorado. For twenty twenty-five, Chevrolet dropped the cheaper two hundred thirty-seven horsepower version of its two point seven liter engine, leaving only the three hundred ten horsepower version, according to Jalopnik. And for twenty twenty-seven, the engine goes to three hundred fifty horsepower. So the cheapest Colorado keeps getting more powerful, but it never gets cheaper. The basic version simply disappeared.""",
   "Chevrolet Colorado WT 2025", "THE CHEAP ENGINE DISAPPEARED")
sc("""There is a small twist in that list. Jalopnik noted that the Hyundai Santa Cruz is built in Alabama, which exempts it from direct import tariffs. Where a truck is built now affects its price, and that is a theme we will dig into in our next video, about which trucks are really built in America.""",
   "Hyundai Santa Cruz Alabama", "BUILT IN ALABAMA, NO IMPORT TARIFF")
sc("""The Tacoma tells a similar story. For twenty twenty-six, the cheapest Tacoma, the SR XtraCab, starts at thirty-two thousand, one hundred forty-five dollars, up five hundred fifty-five, though it now includes a tow hitch as standard, according to CarScoops. And the Tacoma range goes up to sixty-four thousand, three hundred fifty dollars. A midsize truck can now cost as much as a well-equipped full-size one.""",
   "Toyota Tacoma SR 2026", "TACOMA: $32,145 TO $64,350")
sc("""For full-size trucks, an overview of twenty twenty-six starting prices, before destination, put the Ford F-150 at just over thirty-nine thousand dollars, the Chevrolet Silverado fifteen hundred at about thirty-nine thousand, four hundred ninety-five, the Ram fifteen hundred at about forty-one thousand, seven hundred fifty-five, and the GMC Sierra fifteen hundred at about forty-one thousand, nine hundred ninety-five. The same overview said base trims that were around twenty-five thousand in twenty twenty now list above thirty thousand.""",
   "Ford F-150 XL 2025", "BASE FULL-SIZE: ~$39,000-$42,000")
sc("""And remember the gap between the base price and what people pay. The average full-size pickup sells for sixty-seven thousand, five hundred seventy-three dollars. That means the typical buyer pays almost thirty thousand dollars more than the base price. The cheap version exists on paper. Most buyers never get near it.""",
   "Ram 1500 Laramie dealership", "BASE $39K. AVERAGE $67.5K.")

# ---------- 3. INFLATION ----------
sc("""But are trucks really more expensive, or is it just inflation? Pickup Truck plus SUV Talk looked at a nineteen eighty-eight Chevrolet thirty-five hundred that sold at auction in twenty twenty-six. Its starting price in nineteen eighty-eight was sixteen thousand, six hundred fifty-seven dollars, roughly forty-five thousand in today's dollars. Its final sticker, with options, was twenty-two thousand, four hundred eighty-eight dollars, about sixty-one thousand, eight hundred in twenty twenty-six dollars.""",
   "1988 Chevrolet 3500 dually", "1988: $16,657 = ~$45,000 TODAY")
sc("""And here is a twist on that old truck. It was a nineteen eighty-eight Chevrolet thirty-five hundred with a four fifty-four V8, a three-speed automatic, four-wheel drive and only fifty-five miles on it, with the original plastic still on the seats. It sold at auction for one hundred thousand dollars, according to Pickup Truck Talk. The cheap work truck of nineteen eighty-eight became a six-figure collector's item.""",
   "1988 Chevrolet C/K 3500", "SOLD AT AUCTION: $100,000")
sc("""And the comparison? A twenty twenty-six regular cab Silverado thirty-five hundred HD dually listed at fifty-three thousand, eight hundred ninety-five dollars, according to the same article. That is more than the inflation-adjusted base price of the nineteen eighty-eight truck, but less than its inflation-adjusted final sticker. And the new truck has a four hundred one horsepower V8, a ten-speed automatic and Apple CarPlay.""",
   "Chevrolet Silverado 3500HD", "2026 3500HD: $53,895")
sc("""Here is the twist. Adjusted for inflation, a basic heavy-duty work truck is not dramatically more expensive than it was in the nineteen eighties. And TFLcar found that, adjusted for inflation, the popular F-150 XLT and Ram fifteen hundred Big Horn trims were slightly cheaper in twenty twenty-six than in twenty twenty-four. The trucks did not explode in price as much as people think. What changed is what people buy.""",
   "Ford F-150 XLT", "INFLATION EXPLAINS A LOT")
sc("""And remember what the average buyer pays for any new vehicle. Jalopnik reported that the average new car transaction price crossed fifty thousand dollars in late twenty twenty-five, and Edmunds reported a record average payment of seven hundred eighty-seven dollars a month in the third quarter of twenty twenty-six. So even when trucks keep pace with inflation, the overall cost of a new vehicle has moved beyond what many first-time buyers can afford.""",
   "car dealership lot", "AVERAGE NEW CAR: $50,000+")
sc("""And one popular truck actually got cheaper in real terms. TFLcar found that the Toyota Tacoma SR five landed at thirty-nine thousand, four hundred fifty dollars in twenty twenty-six, up only zero point seven percent from twenty twenty-four. Adjusted for inflation, that is almost six percent cheaper. Some trucks are fighting the trend, and those are the ones value buyers should look at first.""",
   "Toyota Tacoma SR5 2024", "TACOMA SR5: -5.9% AFTER INFLATION")
sc("""But the Maverick does not fit that story. Its price rose thirty-six percent from twenty twenty-two to twenty twenty-six, far faster than inflation. And TFLcar found the Silverado fifteen hundred LT up twelve point six percent over two years. Some trucks really did get more expensive, faster than wages and prices in general. Cheap trucks were hit hardest, because there is less room to cut.""",
   "Ford Maverick Tremor", "SOME TRUCKS BEAT INFLATION")

# ---------- 4. WHERE THE CHEAP TRUCKS WENT ----------
sc("""So where did the cheap trucks go? First, the regular cab almost disappeared from dealer lots. As far back as about twenty twelve, the site Curbside Classic reported visiting a dealer with three hundred twenty-five new F-150s on the lot, and fewer than one percent were regular cabs. Only three were in stock. Buyers wanted crew cabs, and dealers stocked what sold.""",
   "Ford F-150 regular cab", "REGULAR CABS: UNDER 1% OF A LOT")
sc("""Second, the small trucks left. The compact pickups that used to sell cheaply, like the old Ranger and the small Toyota and Nissan trucks, grew into today's midsize trucks. Today's Ranger starts at about thirty-five thousand, two hundred forty-five dollars before destination. The Tacoma and Colorado are also in the thirty thousands. For years, the small, cheap truck category was nearly empty.""",
   "Ford Ranger 1998", "THE SMALL TRUCKS GREW UP")
sc("""And the electric trucks did not help. The twenty twenty-five F-150 Lightning Pro, the cheapest work version, started at fifty-four thousand, seven hundred eighty dollars, according to Equipment World. Ford's CEO later said the fifty, seventy and eighty thousand dollar EVs just weren't selling. The first wave of electric pickups made trucks more expensive, not less.""",
   "Ford F-150 Lightning Pro", "LIGHTNING PRO: $54,780")
sc("""Third, the features got expensive. A modern truck comes with screens, cameras, sensors and safety systems as standard. We saw in our tailgate theft story that a modern tailgate with a camera and sensors can cost thousands of dollars to replace and recalibrate. Every one of those features adds cost, even on the base truck.""",
   "Ford F-150 interior screen", "STANDARD TECH ADDS COST")
sc("""And fourth, automakers make more money on expensive trucks. Ram's average transaction price was sixty-eight thousand, three hundred fifty-one dollars in September twenty twenty-six, according to Kelley Blue Book. When a company can sell a sixty-eight thousand dollar truck, building forty thousand dollar trucks becomes less attractive. The cheap truck is not just expensive to build. It is less profitable to sell.""",
   "Ram 1500 Limited", "EXPENSIVE TRUCKS = BIGGER PROFITS")

# ---------- 5. THE MAVERICK EFFECT ----------
sc("""Here is the twist. When Ford finally built a cheap truck, buyers loved it. In twenty twenty-five, the Maverick sold a record one hundred fifty-five thousand and fifty-one units, up eighteen point two percent, according to Ford. That is more than twice the Ford Ranger. And Maverick Hybrid sales set records again in twenty twenty-six.""",
   "Ford Maverick Hybrid 2025", "MAVERICK: 155,051 SOLD")
sc("""And the whole small truck market grew. Midsize pickups sold six hundred sixty thousand, four hundred twelve units in twenty twenty-five, up twenty-four point four percent, according to TFLtruck, and the Ford Ranger alone grew fifty-three point six percent. TFLtruck said consumers are appreciating these smaller than full-size, more affordable pickup trucks. As full-size prices climbed, buyers moved down a size.""",
   "Ford Ranger 2024", "MIDSIZE: +24.4% IN 2025")
sc("""The Maverick proved the industry wrong. For years, automakers said Americans did not want small, affordable trucks. The Maverick showed that they did, as long as the truck was practical and cheap to run. The problem was that even the Maverick could not stay cheap.""",
   "Ford Maverick Lobo", "AMERICANS DO WANT CHEAP TRUCKS")
sc("""And not every small truck succeeded. The Hyundai Santa Cruz, the Maverick's closest rival, fell twenty percent in twenty twenty-five, to twenty-five thousand, four hundred ninety-nine sales, according to TFLtruck. Hyundai raised its twenty twenty-six entry price by seven hundred fifty dollars, according to Jalopnik. Cheap is not enough. The truck still has to be the one buyers want.""",
   "Hyundai Santa Cruz 2025", "SANTA CRUZ: -20%")

# ---------- 6. THE NEW CHEAP TRUCKS ----------
sc("""And there is one more way trucks got pricier, the fees. TFLcar found that destination fees on the half-ton pickups it sampled rose about forty percent over three years. On a cheap truck, a fee of more than one and a half thousand dollars is a much bigger share of the price than on a luxury truck. The cheaper the truck, the more the fees hurt.""",
   "car carrier trailer trucks", "DESTINATION FEES: +40%")
sc("""Now the good news. A new wave of trucks is trying to bring prices back down. The Slate Truck, an electric pickup backed by Jeff Bezos, starts at twenty-four thousand, nine hundred fifty dollars, according to Electrive. SlashGear called it the most affordable new pickup in America. It has a two-seat cab, up to two hundred five miles of range, and a five-foot bed.""",
   "Slate electric truck", "SLATE: $24,950")
sc("""And Slate got there by going back to basics. The base truck has no touchscreen, no speakers, and manual windows. Owners can add features later, and a kit can turn it into a five-seat SUV. Here is the twist. The way to build a cheap truck in twenty twenty-six is to build it like a truck from the nineteen eighties, and let the buyer add the rest.""",
   "1980s pickup truck interior", "MANUAL WINDOWS ARE BACK")
sc("""The Slate is a working truck, not a toy. According to Electrive, it carries about one thousand five hundred fifty pounds of payload, fast charges in about thirty minutes, and comes with a ten-year, one hundred ten thousand mile battery and drivetrain warranty. And it had about one hundred eighty thousand non-binding reservations. The demand for a truly cheap truck is still there.""",
   "small pickup truck bed", "180,000 RESERVATIONS")
sc("""But even Slate could not hold its first number. It originally advertised a price under twenty thousand dollars, which included the seventy-five hundred dollar federal EV tax credit. When the credit was abolished, the price became twenty-four thousand, nine hundred fifty, according to Electrive. First deliveries were scheduled for the fourth quarter of twenty twenty-six.""",
   "electric pickup charging", "UNDER $20K BECAME $24,950")
sc("""Ford is also attacking the price. Its new Fathom midsize electric pickup starts at twenty-eight thousand, three hundred fifty dollars, plus a one thousand five hundred ninety-five dollar delivery fee, according to Electrek, and goes on sale in early twenty twenty-seven. Ford compared the price to the inflation-adjusted price of the original Model T. A century later, the affordable Ford is a pickup again.""",
   "Ford Model T", "FORD FATHOM: $28,350")
sc("""The Fathom is also bigger than it sounds. Ford claims it has more passenger room than a Toyota RAV four, plus a bed and a front trunk, and a zero to sixty time of about four and a half seconds, according to Equipment World. And Ford says five-year ownership costs will be lower than for a three-year-old used Tesla Model Y. Those are Ford's claims, not independent tests, but they show what Ford is aiming at, buyers who think a new truck is out of reach.""",
   "Ford Louisville Assembly Plant", "MORE ROOM THAN A RAV4 (FORD CLAIM)")
sc("""And Ram wants back in. Ram's CEO said the brand desperately needs a more affordable smaller truck, according to TFLtruck, and Ram confirmed the return of the Dakota name for a midsize pickup with production scheduled for twenty twenty-seven. But Auto123 reported that Ram CEO Tim Kuniskis hinted at a starting price around forty thousand dollars. So even the new affordable Ram may not be cheap.""",
   "Dodge Dakota", "DAKOTA: ~$40,000?")

# ---------- 7. HOW TO GET A CHEAP TRUCK ----------
sc("""So how do you get a cheap truck in twenty twenty-six? First, look at the smallest truck that does your job. A Maverick, Santa Cruz, Tacoma, Colorado or Frontier starts in the low thirty thousands with destination. Kelley Blue Book's average for small and midsize pickups was about twenty-four thousand dollars less than for full-size trucks.""",
   "Ford Maverick Toyota Tacoma", "1. BUY THE SMALLEST TRUCK THAT WORKS")
sc("""Here is what that means for your payment. Take the cheapest twenty twenty-five Maverick at about thirty thousand, five hundred dollars, subtract Edmunds' average down payment of about six thousand two hundred, and finance the rest at seven percent for five years. That is about four hundred eighty dollars a month, before taxes and fees, by our calculation. The same math on an average full-size truck is about one thousand two hundred fifteen. A small truck can cut your payment by more than half.""",
   "Ford Maverick XL 2025", "SMALL TRUCK: ~$480/MONTH")
sc("""Second, buy the base trim, and add only what you need. The base Silverado, F-150 and Ram start near forty thousand, but the average buyer pays more than sixty-seven thousand. Every trim step, package and option widens that gap. A work truck trim with a few chosen options can save tens of thousands of dollars compared with the average truck sold.""",
   "Chevrolet Silverado WT", "2. BUY THE BASE TRIM")
sc("""Third, consider the timing. As the redesigned twenty twenty-seven Silverado and Sierra arrive, the outgoing models may be easier to negotiate on. And Ford cut some twenty twenty-six Maverick prices by up to four thousand, two hundred twenty dollars on the Lariat EcoBoost. Prices do come down, but you have to watch for it.""",
   "Ford Maverick dealer lot", "3. WATCH FOR PRICE CUTS")
sc("""And fourth, consider a used truck, but carefully. As we covered in our used truck video, rolled-back odometers and unfixed recalls are real risks. And as Edmunds data showed, used loans carried an average rate of ten point six percent in twenty twenty-six. A cheaper truck with an expensive loan is not always a cheap truck.""",
   "used pickup trucks lot", "4. USED: CHECK THE RATE")

# ---------- CLOSE ----------
sc("""So what happened to cheap trucks? Some of it is inflation. A basic heavy-duty work truck today costs roughly what a basic truck cost in the nineteen eighties after inflation. But the cheapest small trucks disappeared, buyers moved to crew cabs and expensive trims, standard technology added cost, and automakers make more money on luxury trucks. And even the Maverick, the truck that brought cheap back, rose thirty-six percent in four years.""",
   "Ford Maverick 2026", "WHAT REALLY HAPPENED")
sc("""And the final twist. The cheap truck is coming back, but it does not look like the cheap trucks of the past. It looks like a twenty-five thousand dollar electric Slate with crank windows, a twenty-eight thousand dollar electric Ford, and a hybrid Maverick. The cheapest truck of the future may be the most basic truck in decades, and it may plug in.""",
   "Slate truck", "THE CHEAP TRUCK IS COMING BACK")
sc("""We put a list of every pickup under thirty-five thousand dollars, and how to spec a truck without paying for options you do not need, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we look at which trucks are really built in America. And tell us in the comments, what did your first truck cost? Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"In twenty twenty-two, Ford launched": "Intro", "The Ford Maverick is the perfect": "The Maverick's price climb", "So what are the cheapest trucks now": "The cheapest trucks in 2026",
      "But are trucks really more expensive": "Is it just inflation?", "So where did the cheap trucks go": "Where the cheap trucks went",
      "Here is the twist. When Ford finally": "The Maverick effect", "Now the good news": "The new cheap trucks: Slate, Fathom, Dakota",
      "So how do you get a cheap truck": "How to get a cheap truck now", "So what happened to cheap trucks": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video37", "length_scale": 1.4,
  "title": "What Happened to Cheap Trucks? The $19,995 Pickup Now Costs $27,145", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
