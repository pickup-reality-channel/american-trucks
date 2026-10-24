import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""A Rimac Nevera went up for auction in the spring of twenty twenty-five, with only about thirteen hundred miles on the clock. Its window sticker said two million, three hundred eleven thousand dollars. The highest bid was one million, two hundred seventy thousand. And the car did not sell. This is what an electric hypercar really costs.""",
   "Rimac Nevera", "THE REAL COST OF AN ELECTRIC HYPERCAR")
sc("""Here is the twist. The electricity for all of those miles cost, by our own arithmetic, less than one hundred dollars. The part that cost a fortune was not the energy. It was owning a car that the market valued at roughly half of its sticker price.""",
   "Rimac Nevera charging", "THE ELECTRICITY WAS THE CHEAP PART")
sc("""Every figure in this video comes from published sources, listed in the description. Where sources disagree, we will say so. Where we do the maths ourselves, we will say that too. And where nobody has published a number, we will tell you, and we will not invent one.""",
   "Rimac Nevera", "EVERY NUMBER IS SOURCED")

# ---------- 1. STICKER ----------
ch("The sticker price")
sc("""Start with the price on paper. Wikipedia says Rimac plans to build one hundred fifty Neveras. CNBC puts the price at about two million euros, or two point one million dollars. Top Gear gave one point seven million pounds. Those are early figures, and they differ.""",
   "Rimac Nevera price", "EARLY PRICES: €2M · $2.1M · £1.7M")
sc("""The car at the centre of this story gives us a real document. Autoblog reports that its window sticker shows one hundred forty-seven thousand, one hundred forty-five dollars in options, and a total retail price of two million, three hundred eleven thousand, fifty dollars. That is a United States price, for a twenty twenty-three car.""",
   "Rimac Nevera window sticker", "$2,311,050 WINDOW STICKER")
sc("""Subtract the options and, by our own arithmetic, the car without them cost two million, one hundred sixty-three thousand, nine hundred five dollars. So the options alone were about six point four percent of the final price. In a normal car, that would be a big number. Here, it is a small one.""",
   "Rimac Nevera options", "OPTIONS: $147,145")
sc("""Two options stand out. Autoblog says the pearlescent Nevera Blue paint cost twenty-one thousand, six hundred thirty-nine dollars. The Carbon Level Two package cost eighty-six thousand, five hundred fifty-six. Together, by our arithmetic, they make about seventy-four percent of all the options on this car.""",
   "Rimac Nevera blue paint", "PAINT $21,639 · CARBON $86,556")
sc("""Motor1 and autoevolution give the same options in euros, at twenty thousand for the paint and eighty thousand for the carbon package. And both quote an original sticker of two million, one hundred thirty-six thousand euros. Autoevolution converts that to roughly two million, three hundred twenty-eight thousand dollars.""",
   "Rimac Nevera carbon package", "€2,136,000 IN EUROPE")
sc("""So even the sticker has a footnote. Depending on the source, and on the exchange rate, the same car was priced at two point three million dollars, or two point three three million. We use the Autoblog figure of two million, three hundred eleven thousand, because it comes from the window sticker itself.""",
   "Rimac Nevera", "WHICH PRICE IS RIGHT?")
sc("""And there is a newer car. TechCrunch's headline on the Nevera R, shown in August twenty twenty-four, says it only starts at two point five million dollars. So buying the latest Nevera costs more than the sticker we are discussing.""",
   "Rimac Nevera R", "NEVERA R: FROM $2.5 MILLION")

sc("""Two more sticker numbers help. The remaining options, after paint and carbon, total about thirty-eight thousand, nine hundred fifty dollars, by our arithmetic. We do not know what they were, because the sources do not list them. And the carbon package alone was about three point seven percent of the whole sticker.""",
   "Rimac Nevera interior", "THE OTHER $38,950 OF OPTIONS: UNKNOWN")
sc("""Divide the sticker by the power, and you get another view. Using Autoblog's figure of one thousand eight hundred thirteen horsepower, the sticker works out at about one thousand, two hundred seventy-five dollars for every horsepower. With Wikipedia's one thousand eight hundred eighty-eight, it is about one thousand, two hundred twenty-four. Both are our own arithmetic.""",
   "Rimac Nevera motors", "~$1,250 PER HORSEPOWER")
sc("""Compare that with the newer car. By our arithmetic, the Nevera R, from two point five million dollars, costs about one hundred eighty-nine thousand dollars more than this sticker, or roughly eight percent. In return, Wikipedia says it has two thousand one hundred seven metric horsepower, about ten percent more than the standard car.""",
   "Rimac Nevera R", "NEVERA R: +8% PRICE, +10% POWER")

# ---------- 2. THE CAR ----------
ch("The car in the auction")
sc("""Now meet the car. Autoblog says it is number six of the one hundred fifty planned. It was ordered by the Ohio-based Triple F Collection, and delivered in June twenty twenty-three, in the presence of Mate Rimac himself, at Rimac of Naples in Florida.""",
   "Rimac of Naples Florida", "CAR #6 OF 150")
sc("""It has four permanent-magnet electric motors, a carbon fibre monocoque, and a one hundred twenty kilowatt-hour battery. Autoblog quotes one thousand eight hundred thirteen horsepower. It rides on staggered twenty-inch polished wheels, and autoevolution says they carry Michelin Pilot Sport four S tyres.""",
   "Rimac Nevera wheels", "4 MOTORS · 120 KWH · 20-INCH WHEELS")
sc("""Motor1 adds something that is easy to miss. It says that when the car is new, Rimac offers a private driving coach with the purchase. That is part of what the first buyer got for the money, along with a charging cable, two key fobs in a numbered case, and a cover, according to Autoblog.""",
   "Rimac Nevera driving coach", "INCLUDED: PRIVATE DRIVING COACH")
sc("""There was even a detail about the title. Autoblog says it was clean, and Carfax was clean too. In a market where a single scratch can change a price, a clean history matters. This was, in other words, about the best used Nevera a buyer could ask for.""",
   "Carfax report", "CLEAN TITLE, CLEAN CARFAX")
sc("""And the odometer? Autoblog, Carscoops and autoevolution say one thousand, three hundred seventy-one miles. Motor1 says one thousand, three hundred forty-one. That is a thirty-mile difference between sources. We use the figure that most of them agree on, one thousand, three hundred seventy-one.""",
   "Odometer", "1,371 MILES (MOTOR1 SAYS 1,341)")
sc("""Do the arithmetic on that. From June twenty twenty-three to the auction in April twenty twenty-five is roughly twenty-two months. One thousand, three hundred seventy-one miles over twenty-two months is about sixty-two miles a month. That is a hypercar that mostly sat still.""",
   "Hypercar in a garage", "ABOUT 62 MILES A MONTH")

sc("""Production adds context. Wikipedia says the first car went to Nico Rosberg in August twenty twenty-two, and that more than fifty had been delivered by May twenty twenty-four. By our arithmetic, that is about a third of the planned one hundred fifty, so most of the cars were still to be built.""",
   "Nico Rosberg Rimac Nevera", "50+ DELIVERED BY MAY 2024")
sc("""And that is why this auction mattered. For a car this new, there were almost no public sales to compare. Each result was watched by owners, dealers and rivals, because it told them what a used electric hypercar might be worth. One car, in effect, was speaking for all of them.""",
   "Auction crowd", "ONE CAR SPEAKING FOR THE MARKET")

# ---------- 3. THE AUCTION ----------
ch("What the market said")
sc("""The car was listed on Bring a Trailer. Autoblog, on the twenty-eighth of March twenty twenty-five, reported the bid at one million, fifty-one thousand dollars with seven days left. By the first of April, Carscoops reported one million, one hundred fifty-five thousand.""",
   "Bring a Trailer", "MARCH–APRIL 2025: BIDS CLIMB")
sc("""Carscoops noted that the original window sticker said roughly two point three million dollars. By our own arithmetic, a bid of one million, one hundred fifty-five thousand is just under fifty percent of the two million, three hundred eleven thousand on the sticker.""",
   "Rimac Nevera auction", "THE BID: ABOUT HALF THE STICKER")
sc("""Then the auction ended. Autoevolution reported on the eighth of April that the car failed to sell. The highest bid reached one million, two hundred seventy thousand dollars, and the car stayed unsold. Autoevolution put the blame on market conditions and the depreciation of electric cars.""",
   "Rimac Nevera unsold", "HIGHEST BID: $1,270,000 · NOT SOLD")
sc("""Now we have to be careful. A highest bid on a car that did not sell is not a sale price. We do not know if the owner would have taken that money, and we do not know what happened afterwards. Carscoops even said it might sell off the platform if both parties could agree a number.""",
   "Auction hammer", "A BID IS NOT A SALE PRICE")
sc("""But the bid is still information. By our own arithmetic, one million, two hundred seventy thousand is about fifty-five percent of two million, three hundred eleven thousand. The difference is one million, forty-one thousand and fifty dollars. Even if you ignore every option, it is a gap of more than a million.""",
   "Rimac Nevera", "GAP: $1,041,050")
sc("""Spread that gap over time, and the numbers are stark. Twenty-two months is about six hundred seventy days. One million, forty-one thousand dollars divided by six hundred seventy is roughly one thousand, five hundred fifty dollars per day. We stress that this is our own arithmetic, and the car was never sold at that price.""",
   "Calendar", "ABOUT $1,550 A DAY (OUR ARITHMETIC)")
sc("""Divide it by miles instead, and you get about seven hundred sixty dollars for every mile driven. Again, it is an illustration. The point is not that any owner paid this. The point is that the gap between sticker and bid dwarfs every other cost we can measure.""",
   "Rimac Nevera driving", "ABOUT $760 A MILE (OUR ARITHMETIC)")

# ---------- 4. ELECTRICITY ----------
ch("What the electricity costs")
sc("""Now the cost people expect to be high. How much does it cost to charge? Wikipedia gives the battery as one hundred twenty kilowatt-hours. The American average residential price, from the Energy Information Administration and reported by This Old House for March twenty twenty-five, is seventeen point oh one cents per kilowatt-hour.""",
   "Home charging", "17.01 CENTS PER KWH")
sc("""By our own arithmetic, filling the whole battery at that price costs about twenty dollars and forty-one cents. That assumes the entire hundred twenty kilowatt-hours are used, and it ignores charging losses, so the real number could be a little higher. Treat it as an estimate.""",
   "Electric meter", "~$20.41 FOR A FULL CHARGE")
sc("""The same source lists Hawaii at forty-one point one one cents, the highest, and Nebraska at ten point eight nine cents. In Hawaii, the same fill-up would be, by our arithmetic, about forty-nine dollars and thirty-three cents. In Nebraska, about thirteen dollars and seven cents.""",
   "Hawaii electricity", "HAWAII ~$49 · NEBRASKA ~$13")
sc("""How far does a charge go? Wikipedia gives four hundred ninety kilometres on the W L T P test, about three hundred four miles. Dividing twenty dollars forty-one by three hundred four miles gives about six point seven cents a mile. That is our estimate, from official range, not real driving.""",
   "Rimac Nevera range", "ABOUT 6.7 CENTS A MILE")
sc("""Apply that to the car in the auction. One thousand, three hundred seventy-one miles at six point seven cents is about ninety-two dollars. That is the electricity for the whole life of the car, up to that point, under our assumptions. Compared with a gap of one million forty-one thousand, it is less than one hundredth of one percent.""",
   "Rimac Nevera", "ELECTRICITY FOR 1,371 MILES: ~$92")
sc("""Of course, a Nevera is not meant to be driven gently. Real use at high speed would drain the battery much faster, so the range would be shorter and the cost per mile higher. But even if the cost were ten times higher, it would still be a tiny part of the total. That is the real surprise.""",
   "Rimac Nevera track", "EVEN 10× WOULD BE SMALL")
sc("""Charging time is a different cost. Wikipedia says the Nevera can fast-charge to eighty percent in under thirty minutes. Eighty percent of a hundred twenty kilowatt-hours is ninety-six. Ninety-six in half an hour means an average of at least about one hundred ninety-two kilowatts. That needs a serious public charger, not a wall socket.""",
   "DC fast charger", "AT LEAST ~192 KW TO CHARGE THAT FAST")

sc("""Now stretch the idea to a normal year of driving. If an owner drove ten thousand miles, at six point seven cents a mile, the electricity would be about six hundred seventy dollars, by our arithmetic. Even a full decade of that would cost less than seven thousand dollars. Against a seven-figure gap, it is almost invisible.""",
   "Highway driving", "10,000 MILES ≈ $670 (OUR ARITHMETIC)")
sc("""Compare that with the price of a single option. The carbon package alone, eighty-six thousand, five hundred fifty-six dollars, would pay for the electricity of more than a hundred twenty-five years at ten thousand miles a year. That is a strange sentence to write about a car, but it is what the arithmetic says.""",
   "Rimac Nevera carbon", "ONE OPTION = 125 YEARS OF ELECTRICITY")

# ---------- 5. WARRANTY ----------
ch("The cost nobody can see yet: the battery")
sc("""The biggest unknown in any electric car is the battery. Top Gear says the Nevera's pack holds six thousand, nine hundred sixty cells and weighs seven hundred kilograms. If it ever needed replacing outside warranty, that is a lot of battery. And nobody has published a replacement price we could find.""",
   "Rimac Nevera battery pack", "6,960 CELLS · 700 KG")
sc("""Rimac knows this fear, and has answered it. According to Indigo Auto Group, on the twenty-third of January twenty twenty-four, Rimac extended the Nevera's warranty to eight years with unlimited miles, with the battery guaranteed to keep at least seventy-five percent of its capacity.""",
   "Rimac Nevera warranty", "8 YEARS · UNLIMITED MILES")
sc("""Indigo also reports that the motors are described as maintenance free for life. That is a claim from the company, and we have not seen it tested over many years. But it shows that Rimac is selling the Nevera on the idea that an electric hypercar has fewer parts that wear out.""",
   "Rimac Nevera motors", "\"MAINTENANCE FREE FOR LIFE\"")
sc("""Here is the arithmetic of that warranty. If the eight years count from delivery, as we would expect but cannot confirm, this car's coverage would run to June twenty thirty-one. For a car with fewer than fifteen hundred miles, the mileage will not matter. The real test will be the years. Seventy-five percent of a hundred twenty kilowatt-hours is ninety kilowatt-hours.""",
   "Rimac Nevera dashboard", "75% OF 120 KWH = 90 KWH")
sc("""It is worth saying what a warranty cannot protect. It does not protect the resale price. A battery can be perfectly healthy, as this one almost certainly was, and the car can still be valued at half of its sticker price. Warranty covers failures, not fashions or market moods.""",
   "Rimac Nevera", "WARRANTY DOESN'T COVER RESALE")

# ---------- 6. WHAT NOBODY PUBLISHES ----------
ch("The costs nobody publishes")
sc("""So what costs did we not find? Insurance for a Nevera. A price for a set of tyres. A replacement price for a battery. The cost of a service visit. None of the sources we read gave a figure, and we will not guess. If you own one, those are the numbers we would love to see.""",
   "Hypercar garage", "NOT PUBLISHED: INSURANCE, TYRES, SERVICE")
sc("""We do know what the car is fitted with. Autoevolution says the tyres are Michelin Pilot Sport four S, and that the car has a hydraulic lift system, active aero elements and butterfly doors. Every one of those features is a thing that can, in principle, need care. But we have no cost to attach to them.""",
   "Rimac Nevera butterfly doors", "LIFT SYSTEM · ACTIVE AERO · BUTTERFLY DOORS")
sc("""Autoblog also says the car has carbon ceramic brakes with six-piston calipers, electro-hydraulic. Carbon ceramic brakes are known for being expensive on any car, but we did not find a published price for these. Honest answer: the running cost of a Nevera is mostly a blank on the page.""",
   "Carbon ceramic brake", "CARBON CERAMIC BRAKES: NO PRICE FOUND")

# ---------- 7. THE LARGER MARKET ----------
ch("Is that one auction typical?")
sc("""One auction is one data point. So we looked for more. The Classic Valuer, a price guide, lists three Neveras that went to auction on Bring a Trailer. One was the twenty twenty-three car we have been discussing, in April twenty twenty-five. It did not sell.""",
   "Bring a Trailer Rimac", "THREE AUCTIONS, ONE SALE")
sc("""A twenty twenty-four Nevera also failed to sell, on the thirteenth of April twenty twenty-six, according to the same guide. And a twenty twenty-three Nevera Time Attack car sold on the fifteenth of June twenty twenty-six, for one million, two hundred fifty-one thousand, five hundred eighty-three pounds.""",
   "Rimac Nevera Time Attack", "SOLD: £1,251,583 (JUNE 2026)")
sc("""The guide gives a sell-through rate of thirty-three percent, because one of its three listed cars sold. Three auctions is a tiny sample, and the Time Attack car is a special version, so we cannot say what an average Nevera is worth. But it fits a pattern: bids well below the new price.""",
   "Rimac Nevera", "SELL-THROUGH RATE: 33%")
sc("""There is an important lesson in how to read this. Hypercars often hold their value because they are rare. Wikipedia says only one hundred fifty Neveras are planned. Yet these results show that rarity alone does not guarantee a price. A new technology, and a new brand, carry their own risk.""",
   "Rimac Nevera", "RARE DOESN'T MEAN SAFE")

sc("""Think about the buyer on the other side. Someone who bids one million dollars on a used Nevera is getting a car with fewer than fifteen hundred miles, a clean history, and the same one hundred twenty kilowatt-hour battery. For that buyer, the drop in price is an opportunity. For the seller, it is a loss.""",
   "Rimac Nevera buyer", "A LOSS FOR ONE, A BARGAIN FOR ANOTHER")
sc("""There is a broader lesson here for electric cars of every price. Technology moves quickly, and a newer version often arrives before the older one is paid for. The Nevera R came out in August twenty twenty-four, only about fourteen months after the first deliveries to American owners, by our arithmetic.""",
   "Rimac Nevera R", "A NEWER VERSION ARRIVES QUICKLY")

# ---------- 8. WHO PAYS ----------
ch("So what does it really cost?")
sc("""Let us put it all together, in our own words. The sticker for this car was two million, three hundred eleven thousand dollars. The electricity for its first thirteen hundred miles was about ninety dollars. The unsold bid left a gap of over one million dollars. The tyres, insurance and service are unknown.""",
   "Rimac Nevera", "THE WHOLE PICTURE")
sc("""That means the cost of an electric hypercar is nothing like the cost of a normal car. For a family car, fuel and repairs matter. For a Nevera, according to every figure we could find, the dominant cost is the difference between what you pay and what someone will pay you later.""",
   "Rimac Nevera", "THE BIGGEST COST: THE PRICE GAP")
sc("""And yet owners are not necessarily unhappy. Motor1 notes that the car came with a private driving coach. People who buy a Nevera are buying an experience, a place among one hundred fifty owners, and a record-setting machine. Not everything fits in a spreadsheet.""",
   "Rimac Nevera cockpit", "AN EXPERIENCE, NOT A SPREADSHEET")
sc("""The records are real. Wikipedia says the Nevera set twenty-three records on the seventeenth of May twenty twenty-three, including zero to one hundred kilometres per hour in one point eight two seconds. Some buyers value that. Others, as the auction suggests, may feel differently about the price once the car has been delivered.""",
   "Rimac Nevera records", "0–100 KM/H: 1.82 SECONDS")
sc("""So here is our verdict. If you are buying an electric hypercar, do not worry about the electricity bill. Worry about what the car will be worth in two years. If you cannot accept a loss of a large share of the price, in a market this young, it is a decision to make with open eyes.""",
   "Rimac Nevera", "WORRY ABOUT RESALE, NOT ELECTRICITY")
sc("""One last caveat. All of this comes from one car, one auction, and a few price guides. The market could change. Rimac's newer cars, the warranty, and a growing used market could all move the numbers. We will revisit the figures when more sales are published.""",
   "Rimac Nevera", "ONE CAR, ONE AUCTION")
sc("""Do you think a Nevera will hold its value in ten years? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Nevera, compare it with the Bugatti Tourbillon, and tell the story of the kid from Croatia who ended up running Bugatti.""",
   "Rimac Nevera", "WILL IT HOLD ITS VALUE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more honest numbers about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video87", "The Real Cost of an Electric Hypercar", [
    "Autoblog, A rare 1-of-150 $2.2M Rimac Nevera just landed on Bring a Trailer: https://www.autoblog.com/news/a-rare-1-of-150-2-2m-rimac-nevera-just-lander-on-bring-a-trailer",
    "Carscoops, We're about to find out what Rimac's Nevera is worth on the open market (1 April 2025): https://www.carscoops.com/2025/04/were-about-to-see-what-a-rimac-nevera-is-worth-on-the-open-market/",
    "autoevolution, 2023 Rimac Nevera fails to sell (8 April 2025): https://www.autoevolution.com/news/2023-rimac-nevera-fails-to-sell-127-million-bid-falls-way-short-of-233-million-msrp-249664.html",
    "Motor1, For sale: Rimac Nevera, barely driven: https://www.motor1.com/news/755011/used-rimac-never-for-sale-bring-a-trailer/",
    "The Classic Valuer, Price guide: Rimac Nevera: https://www.theclassicvaluer.com/cars/rimac/nevera",
    "TechCrunch, Rimac Nevera R (16 August 2024): https://techcrunch.com/2024/08/16/rimac-squeezes-more-power-into-its-new-all-electric-hypercar-nevera-r-and-it-only-starts-at-2-5-million",
    "Wikipedia, Rimac Nevera: https://en.wikipedia.org/wiki/Rimac_Nevera",
    "Top Gear, Rimac Nevera (battery pack)",
    "Indigo Auto Group, Rimac Nevera warranty extension (23 January 2024)",
    "CNBC, Rimac Nevera price coverage",
    "This Old House, average electricity cost per kWh by state (EIA, March 2025)",
], "C")
