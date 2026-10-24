import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""A Pagani Utopia launched in twenty twenty-two at about two point one nine million dollars. According to a price guide, a twenty twenty-four car with just forty-eight kilometres on the clock was sold at auction in Zurich in October twenty twenty-five for about four million dollars. So the strange truth about owning a Pagani may be this: the cost is not what you lose. It is what you gain.""",
   "Pagani Utopia", "WHAT IT REALLY COSTS TO OWN A PAGANI")
sc("""But there is a catch, and it is the reason this video exists. Service visits are reported at fifteen to forty thousand dollars each. Insurance has no published price. And nobody can walk into a showroom and buy one. We will go through every number we could find, and tell you clearly what we could not.""",
   "Pagani Utopia service", "THE PRICE YOU PAY VS THE PRICE YOU GET")
sc("""Every figure in this video comes from published sources, listed in the description. Where sources disagree, we will say so. Where we do the maths ourselves, we will say that too. And where a number is only an estimate from a website, we will call it an estimate.""",
   "Pagani Utopia", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE STICKER ----------
ch("The launch price")
sc("""Start with the price on paper. Wikipedia says Utopia pricing starts at two point one nine million dollars. Supercar Blondie, writing on the day of the unveiling, says Pagani will price it from two million, one hundred seventy thousand euros. Top Gear says around two point two million pounds. Three currencies, one car.""",
   "Pagani Utopia launch", "$2.19M · €2.17M · £2.2M")
sc("""A price guide called Hyperluxe, updated in July twenty twenty-six, describes the euro figure as before taxes and options, and says a heavily specified car could reach two point five to two point seven million euros. By our own arithmetic, that is a premium of fifteen to twenty-four percent over the base price.""",
   "Pagani Utopia options", "HEAVILY SPECIFIED: €2.5M TO €2.7M")
sc("""Two other sources give a different base. Hyperluxe says a figure of two point five million dollars is sometimes quoted for an optioned car. Marque Cars, a buyer's guide, says the Utopia base price is roughly two point five million dollars before bespoke options. So some sources treat that number as the base, and some as an optioned car.""",
   "Pagani Utopia price", "$2.5M: BASE OR OPTIONED? SOURCES DISAGREE")
sc("""For the roadster, the numbers are clearer. Wikipedia says it was introduced on the thirtieth of July, twenty twenty-four, with production limited to one hundred thirty units and a base price of three point four million dollars. Pagani's own release says it starts at three point one million euros, excluding local taxes.""",
   "Pagani Utopia Roadster", "ROADSTER: €3.1M, 130 CARS")
sc("""By our arithmetic, that makes the roadster about forty-three percent more expensive than the coupé in euros, an extra nine hundred thirty thousand euros for the removable roof. Pagani's release says the roadster was developed jointly with the coupé, and weighs the same, one thousand two hundred eighty kilograms.""",
   "Pagani Utopia Roadster", "+€930,000 FOR THE ROOF (OUR ARITHMETIC)")
sc("""And compare it with the company's older cars. Wikipedia says each Huayra cost one million pounds before options, about one point zero five million dollars. The Huayra B C cost over two point one million euros. The Zonda Tricolore was priced at one point two million pounds. Every new Pagani has been more expensive than the last.""",
   "Pagani Huayra", "HUAYRA £1M → UTOPIA €2.17M")

sc("""Now consider what the price buys. By our own arithmetic, the launch price of two million, one hundred seventy thousand euros, divided by the dry weight of one thousand two hundred eighty kilograms, is about one thousand, six hundred ninety-five euros for every kilogram of car. Divided by eight hundred sixty-four metric horsepower, it is about two thousand, five hundred twelve euros for each horsepower.""",
   "Pagani Utopia", "€1,695 PER KG · €2,512 PER PS (OUR ARITHMETIC)")
sc("""Options add to that. Hyperluxe says a heavily specified car could reach two point five to two point seven million euros. By our arithmetic, that is three hundred thirty to five hundred thirty thousand euros of extras. Pagani's release mentions some of them: a Sport Pack with seats in leather lightened by twenty percent, special wheels, and the choice of manual or automated gearbox.""",
   "Pagani Utopia options", "€330K–€530K OF EXTRAS (OUR ARITHMETIC)")
sc("""Add up the order book, and the scale becomes clear. By our own arithmetic, ninety-nine coupés at two point one seven million euros, and one hundred thirty roadsters at three point one million, come to roughly six hundred eighteen million euros before options and taxes. It is a very large number for a company that builds twenty-five to thirty cars a year, according to Marque Cars.""",
   "Pagani San Cesario", "ORDER BOOK: ~€618M BEFORE OPTIONS")
# ---------- 2. THE MARKET ----------
ch("What the used market says")
sc("""Now what happened after the cars were delivered. Wikipedia says the first Utopia was delivered in October twenty twenty-three. Hyperluxe says the clearest public sale was a twenty twenty-four car with forty-eight kilometres, sold for three million, two hundred sixty-seven thousand, five hundred Swiss francs at R M Sotheby's in Zurich in October twenty twenty-five.""",
   "RM Sotheby's Zurich", "OCTOBER 2025: CHF 3,267,500 IN ZURICH")
sc("""Hyperluxe converts that to about four million to four point one million dollars. By our own arithmetic, that is between eighty-three and eighty-seven percent above the two point one nine million launch price, and a gain of roughly one point eight to one point nine million dollars. On a car with fewer than thirty miles.""",
   "Pagani Utopia sale", "+83% TO +87% OVER THE LAUNCH PRICE")
sc("""Hyperluxe also says a Utopia coupé is worth three point eight to four point eight million dollars in twenty twenty-six, with asking prices from about four point one to four point eight million. It says speculative figures up to five point five million are ambitious asking prices rather than demonstrated transactions. We agree with that distinction.""",
   "Pagani Utopia for sale", "ASKING PRICES: $4.1M TO $4.8M")
sc("""Classic dot com, a market-data site, shows a benchmark value of four million, seventy-four thousand, one hundred thirty-eight dollars for the Utopia. Its listings are mostly without public prices: ask for price, or price undisclosed. Those are the words dealers use when the number is a negotiation, not a sticker.""",
   "Classic.com Pagani Utopia", "BENCHMARK: $4,074,138")
sc("""The listings show something else too: very low mileage. The site lists a twenty twenty-four Utopia with three thousand miles in Florida, one with six hundred twenty miles in a Mecum auction dated for the sixteenth of January, twenty twenty-seven, and one with one thousand miles in Illinois. These are cars that mostly sit.""",
   "Pagani Utopia mileage", "620 · 1,000 · 3,000 MILES")
sc("""By our arithmetic, a benchmark of four million, seventy-four thousand against two point one nine million is about eighty-six percent above launch. So three different sources, a price guide, a market-data site and an auction report, point in the same direction. A caveat: the Classic dot com page did not fully load, so we treat the benchmark as indicative.""",
   "Pagani Utopia", "THREE SOURCES, ONE DIRECTION: +86%")

sc("""Hyperluxe also reports one car offered off-market at about four million, three hundred fifty-six thousand dollars. By our arithmetic, that is almost double the launch price, an increase of about ninety-nine percent. Again, an offer is not a sale. But it shows the level at which owners are willing to part with their cars, if they part with them at all.""",
   "Pagani Utopia off-market", "OFF-MARKET ASK: ~$4.36M")
sc("""Time matters too. The Zurich car sold about three years and one month after the unveiling. If the gain was around one point eight to one point nine million dollars, by our arithmetic, that works out to roughly fifty thousand dollars for every month since launch. Of course, a single car does not make a trend, and the gain was only realised by the seller.""",
   "Pagani Utopia", "~$50,000 A MONTH SINCE LAUNCH (ONE CAR)")
sc("""Also worth noting: forty-eight kilometres is only about thirty miles. The car in Zurich was effectively new. That detail is probably part of the price. The same car with ten thousand miles on it, we suspect, would have attracted a different bid, though none of our sources tests that. It is an inference, and we flag it as one.""",
   "Pagani Utopia odometer", "48 KM ≈ 30 MILES")
# ---------- 3. SERVICE ----------
ch("Service: the cost you can't avoid")
sc("""Now the costs. Marque Cars says that service intervals run twelve months or six thousand miles for the Huayra and Zonda lineages. Note the wording. That is for the older models. For the Utopia, the page says the programme is too new to establish a multi-year track record, and we found no official Utopia service schedule.""",
   "Pagani service", "SERVICE EVERY 12 MONTHS OR 6,000 MILES")
sc("""The same page says service costs are at the top of the segment, typically fifteen thousand to forty thousand dollars per visit at an authorised facility. It is an estimate from a buyer's guide, not a Pagani price list, and it is not about the Utopia specifically. But it is the only number we could find.""",
   "Pagani workshop", "$15,000 TO $40,000 PER VISIT (ESTIMATE)")
sc("""By our own arithmetic, one visit a year for ten years would cost between one hundred fifty thousand and four hundred thousand dollars. That is a lot of money for maintenance, and it is almost certainly not a bill that applies unchanged to every car. We stress: this is a calculation from an unattributed estimate.""",
   "Pagani mechanic", "10 YEARS: $150K TO $400K (OUR ARITHMETIC)")
sc("""Major items cost more. Marque Cars says that clutch and transmission service is materially higher, without giving a figure. That matters on a Utopia, since Xtrac built a special seven-speed gearbox with a triple-disc clutch, according to Pagani's release. A part built for one car costs what the car costs to make.""",
   "Xtrac gearbox", "CLUTCH & GEARBOX: HIGHER, NO FIGURE")
sc("""Tyres are another unknown. Pagani's release says standard tyres are Pirelli P Zero Corsa and P Zero Winter, with P Zero Trofeo R S optional, in twenty-one inch at the front and twenty-two at the rear. We found no published price for a set. It would be easy to guess, and we will not.""",
   "Pirelli P Zero tyres", "21/22-INCH PIRELLI: NO PRICE FOUND")
sc("""Brakes are the same. Top Gear says the Utopia has carbon ceramic discs, with six-piston calipers at the front and four-piston at the rear. Replacement prices for carbon ceramic brakes are not in our sources. What we can say is that a car with this hardware will not be cheap to keep in perfect order.""",
   "Carbon ceramic brake", "CARBON CERAMIC DISCS: NO PRICE FOUND")

sc("""There is another number in the Marque Cars guide that helps. It says depreciation on standard Huayra and Zonda models has historically tracked closer to zero, and that value on limited variants is firmly positive over the multi-year period. The page gives no figures for either claim, and it admits it cannot build a depreciation curve. We treat both statements as opinions.""",
   "Pagani Huayra", "\"CLOSER TO ZERO\" · NO FIGURES GIVEN")
sc("""The Hyperluxe page makes a similar point about the Utopia. It says a coupé is worth three point eight to four point eight million dollars in twenty twenty-six, but it names only one sale. It also says the figures are not attributed to a named dataset. The gap between a price guide and a verified transaction is wide, and we have tried to stay on the verified side.""",
   "Pagani Utopia", "ONE NAMED SALE, MANY ESTIMATES")
# ---------- 4. INSURANCE ----------
ch("Insurance and where it lives")
sc("""Insurance is next. Marque Cars says cover at this value is individually underwritten by specialist carriers rather than quoted off a rate table. No premium figures are published. So there is no annual number we can give you. Anyone who offers one for a Pagani is guessing.""",
   "Insurance paperwork", "INDIVIDUALLY UNDERWRITTEN: NO PUBLISHED RATE")
sc("""There is a further point about risk. The listing data above shows that Utopias are being kept at very low mileage. In our reading, that makes sense. When a car is valued at around four million dollars, every mile and every scratch matters to the next buyer. In market terms, the safest way to use a Pagani may be to barely use it.""",
   "Pagani Utopia garage", "THE SAFEST PAGANI IS A PARKED PAGANI")
sc("""Pagani's own release tells a different story. It lists the P Zero Winter among the standard tyres for the roadster. A company that lists winter tyres expects someone to drive in winter. Marque Cars suggests the sweet spot for used Huayras is a coupé with documented service history, which implies a car that has been used and serviced.""",
   "Pagani winter tyres", "WINTER TYRES ARE AN OPTION")

sc("""Pagani's release adds details of what a roadster owner gets. The soft top is stored in a suitcase in place of the vanity case, and the hard top can be displayed on a stand. A buyer is also paying for the presentation: Habanero Red exposed carbon, and wheels in brushed silver or Pearl Beige. These are things that no spreadsheet can price.""",
   "Pagani Utopia Roadster", "SOFT TOP IN A SUITCASE, HARD TOP ON A STAND")
# ---------- 5. FUEL ----------
ch("The V12 question: fuel and emissions")
sc("""What about fuel? Top Gear says the Utopia's engine is a bespoke Mercedes-AMG twin-turbo V twelve of six litres, with eight hundred sixty-four brake horsepower. We found no official fuel economy figure for the car, so we cannot say what a tank costs. We can say only that a twin-turbo V twelve is not designed to save fuel.""",
   "Pagani Utopia V12", "NO OFFICIAL FUEL ECONOMY FOUND")
sc("""But Top Gear adds that Pagani says the engine meets California's emissions rules. That means the car can be registered in the biggest American state for cars. For an owner, that is a practical point: a Pagani that cannot be driven in California would have a smaller market and a lower resale value.""",
   "California emissions", "MEETS CALIFORNIA'S EMISSIONS RULES")

# ---------- 6. GETTING ONE ----------
ch("The real obstacle: getting one")
sc("""Now the biggest cost of all: access. Top Gear says only ninety-nine coupés will be built and all were reportedly allocated. Wikipedia says the same: all ninety-nine coupés were assigned to customers before the first delivery. Marque Cars says allocation is closed at the manufacturer level for current production.""",
   "Pagani Utopia production", "ALL 99 COUPÉS ASSIGNED")
sc("""So the only way to get one is to buy from an owner. Hyperluxe says these cars change hands privately and discreetly. Which is another reason for the missing prices. A dealer listing that says ask for price is not a mistake. It is how the market works. And a price you cannot see is a price you cannot compare.""",
   "Pagani Utopia dealer", "CARS CHANGE HANDS PRIVATELY")
sc("""How long does a Pagani take to build? Marque Cars says overall output is roughly twenty-five to thirty cars per year. By our own arithmetic, building two hundred twenty-nine Utopias, ninety-nine coupés and one hundred thirty roadsters, at that rate would take between about seven and a half and nine years.""",
   "Pagani factory", "229 CARS AT 25–30 A YEAR = 7.6–9.2 YEARS")
sc("""That is a cost of its own: time. Wikipedia says the first car was delivered thirteen months after the unveiling, in October twenty twenty-three, by our arithmetic. But the last of the roadsters could be delivered years after that. Waiting, in the world of Pagani, is part of the price.""",
   "Pagani deliveries", "WAITING IS PART OF THE PRICE")

# ---------- 7. OLDER CARS ----------
ch("What about older Paganis?")
sc("""The older cars tell the same story, only bigger. Marque Cars lists a twenty fourteen Pagani Zonda L M Roadster sold for eleven million, eighty-six thousand, two hundred fifty dollars at R M Sotheby's in Dubai in December twenty twenty-four. And a twenty twenty-two Huayra R sold for three million, forty-two thousand, five hundred euros in Paris in February twenty twenty-five.""",
   "RM Sotheby's Dubai", "ZONDA LM ROADSTER: $11.09M (DEC 2024)")
sc("""The same page lists a twenty fourteen Huayra at one million, nine hundred twenty-five thousand dollars at Barrett-Jackson Scottsdale in January twenty twenty-five. Compare that with the one million pounds, about one point zero five million dollars, that Wikipedia gives for a new Huayra before options. By our arithmetic, that is about eighty-three percent more.""",
   "Barrett-Jackson Scottsdale", "HUAYRA: £1M NEW → $1.925M AT AUCTION")
sc("""Marque Cars also gives a warning that we want to repeat. Auction results are evidence of what specific cars made on specific days, not a valuation of any other example. And it says no series of retail transactions exists to build a depreciation curve for Pagani. So there is no guarantee that your Pagani will behave like these ones.""",
   "Auction hammer", "A RESULT IS NOT A VALUATION")
sc("""Not every auction works out. Gulf News reported that at the Riyadh Season sale in twenty nineteen, a Zonda Riviera made five point five million dollars, but only eighteen of sixty-eight cars sold in total. By our arithmetic, that is about twenty-six percent of the cars. So even a famous brand does not mean every car sells.""",
   "Riyadh Season auction", "18 OF 68 CARS SOLD")
sc("""And Wikipedia says two of the three Zonda HP Barchettas cost fifteen million dollars each. By our own arithmetic, that is about seven times the Utopia's launch price. It is the top of the range. Attic Capital's interview summary quotes Pagani saying that his cars cost roughly three to fifteen million euros. The Utopia, at two point one seven, starts below that.""",
   "Pagani Zonda HP Barchetta", "$15M HP BARCHETTA · UTOPIA STARTS BELOW €3M")

sc("""The track-only Huayra R is another data point. Marque Cars lists a twenty twenty-two Huayra R at three million, forty-two thousand, five hundred euros in Paris in February twenty twenty-five. Wikipedia says the Utopia's suspension is based on experience from the Huayra R. So the car that taught the Utopia how to handle is itself worth more than the Utopia's launch price.""",
   "Pagani Huayra R", "HUAYRA R: €3.04M AT AUCTION (FEB 2025)")
sc("""Go back to the Riyadh sale. Gulf News said eighteen of sixty-eight cars sold, for a total of sixteen point seven five million dollars. By our arithmetic, that is an average of about nine hundred thirty thousand dollars. Take out the Zonda Riviera and the Chiron, which made five point five and three point four million, and the other sixteen averaged about four hundred ninety thousand.""",
   "Riyadh Season sale", "AVERAGE ~$930K · WITHOUT TWO STARS ~$490K")
sc("""That comparison shows why Pagani is special. A Riviera sold for more than ten times the average of the rest. At a sale with sixty-eight cars, the two stars carried more than half the money, by our arithmetic. A Pagani is not priced like a normal collector car. It is priced like a work of art, and the market treats it so.""",
   "Pagani Zonda Riviera", "2 CARS = 53% OF THE SALE")
# ---------- 8. THE MATH ----------
ch("The honest maths")
sc("""Now put it together, with every caveat in place. The launch price was two point one nine million dollars. A well-reported sale of a nearly new car was about four million. Service might run fifteen to forty thousand dollars a year, from an unattributed estimate. Tyres, brakes and insurance are unknown. Fuel is unknown.""",
   "Pagani Utopia", "THE WHOLE PICTURE")
sc("""By our arithmetic, the unrealised gain on the Zurich car, about one point eight million dollars, would cover forty-five to one hundred twenty years of service at the quoted rate. We are not saying that every owner earned that. We are saying that, on the evidence we found, appreciation has been much larger than any running cost.""",
   "Pagani Utopia", "GAIN ≈ 45–120 YEARS OF SERVICE (OUR ARITHMETIC)")
sc("""Compare that with the electric hypercar we covered in another video of this series. That one failed to sell, with the highest bid far below its sticker, in the one auction we examined. The Utopia has done the opposite so far. The difference may come from the brand, from the number of cars, or from the manual gearbox, or from all three. We do not know.""",
   "Rimac Nevera and Pagani Utopia", "THE OPPOSITE OF THE NEVERA, SO FAR")
sc("""Marque Cars suggests one reason. It says manual-transmission Utopias are expected to trade at meaningful premiums to the automated-manual cars. The page marks that as a forecast, not data. But it fits the story of this car: people want what is rare, mechanical and hard to find, and the manual is all three.""",
   "Pagani Utopia manual", "MANUAL UTOPIAS: EXPECTED TO TRADE AT A PREMIUM")
sc("""A word of caution. Prices at the top of the market can fall as well as rise. The Utopia programme is too new, in Marque Cars' words, to have a multi-year track record, and we have only a handful of data points. Anyone telling you a Pagani is a guaranteed investment is going beyond the evidence.""",
   "Pagani Utopia", "NO GUARANTEES")
sc("""So what does it really cost to own a Pagani? On the evidence, less than most people think, if you can get one, and if the market holds. And more than you can see, because the biggest costs are the ones with no public price: access, insurance, tyres, brakes, and the time you wait.""",
   "Pagani Utopia", "LESS THAN YOU THINK, MORE THAN YOU CAN SEE")
sc("""Do you think a Utopia will hold its value? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Utopia, compare it with the Zonda, and tell the story of Horacio Pagani, the man who started in Italy with a broom.""",
   "Pagani Utopia", "WILL IT HOLD ITS VALUE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more honest numbers about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video91", "What It Really Costs to Own a Pagani", [
    "Wikipedia, Pagani Utopia: https://en.wikipedia.org/wiki/Pagani_Utopia",
    "Wikipedia, Pagani (company): https://en.wikipedia.org/wiki/Pagani_(company)",
    "Wikipedia, Pagani Zonda: https://en.wikipedia.org/wiki/Pagani_Zonda",
    "Hyperluxe, Pagani Utopia price (updated July 2026): https://hyper.luxe/price/pagani/utopia-price/",
    "Marque Cars, Pagani buyer's guide, pricing, depreciation: https://marquecars.com/brands/pagani",
    "Classic.com, Pagani Utopia market: https://www.classic.com/m/pagani/utopia/",
    "Top Gear, This is the brand new Pagani Utopia: https://www.topgear.com/car-news/first-look/brand-new-pagani-utopia-v12-engined-throwback",
    "Supercar Blondie, The Pagani Utopia is here: https://supercarblondie.com/pagani-utopia-c10-v12-manual-supercar-revealed/",
    "Pagani Automobili press release, Pagani Utopia Roadster: https://www.pagani.com/press/utopia-roadster/",
    "Gulf News, Pagani Zonda Riviera sold for $5.5 million at Riyadh Season car auction: https://gulfnews.com/amp/auto/news/pagani-zonda-riviera-sold-for-55-million-at-riyadh-season-car-auction-1.1574581887664",
    "Attic Capital, Horacio Pagani and the Zonda: https://atticcapital.com/horacio-pagani-zonda/",
], "C")
