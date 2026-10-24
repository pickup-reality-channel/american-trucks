import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""In two thousand ten, the Lexus LFA launched with a price of three hundred seventy-five thousand dollars, and sales were slow. In April twenty twenty-four, one sold for eight hundred ninety thousand dollars. More than double. And a special version has sold for one point six million. This is why the Lexus LFA is worth more now than when it was new, and what the sources say about it.""",
   "Lexus LFA", "WHY THE LEXUS LFA IS WORTH MORE NOW THAN NEW")
sc("""Here is the twist. Not one of the sales we are about to show you is a guarantee. They are single auctions. Some cars did not sell at all. And there is one thing about the LFA's value that has nothing to do with the car's performance. We will show you the numbers, the reasons the sources give, and the limits of what anyone can know.""",
   "Lexus LFA auction", "SINGLE AUCTIONS, NOT A GUARANTEE")
sc("""Every figure comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. This is not investment advice. It is a record of what was reported.""",
   "Lexus LFA", "NOT INVESTMENT ADVICE · EVERY NUMBER IS SOURCED")

ch("The starting line: a slow launch")
sc("""Begin with the original numbers. Wikipedia lists the base price as three hundred seventy-five thousand dollars, or three hundred forty thousand pounds. Production ran from December two thousand ten to December two thousand twelve, with five hundred cars built at twenty a month. Motor16 adds that a car sold in two thousand twenty-four had also carried twelve thousand, five hundred dollars of factory options.""",
   "Lexus LFA", "$375,000 BASE · 500 BUILT · 20 A MONTH")
sc("""The launch was not an easy one. The Drive wrote in September two thousand seventeen that the LFA's price had done nothing but appreciate since its rocky launch, when sales were slow and skepticism was high. Wikipedia adds that one hundred fifty North American cars were initially sold through a two-year lease, which suggests that Lexus needed a way to put buyers in them.""",
   "Lexus LFA showroom", "\"ROCKY LAUNCH · SLOW SALES · HIGH SKEPTICISM\" (THE DRIVE)")
sc("""Note that the lease is Wikipedia's fact and the explanation is our reading. The page does not say why Lexus offered leases. What it does say is that the final LFA was sold in June two thousand twenty-three, an Australian dealer's display car, at a price not disclosed. By our arithmetic, that is more than ten years after production ended.""",
   "Lexus dealership", "FINAL NEW LFA SOLD JUNE 2023")
sc("""So the car that is now so sought after was, for years, a car that dealers still had in stock. That is the opposite of how most limited cars begin. A buyer in two thousand eleven could negotiate. A buyer in two thousand twenty-four could not. What changed? We will look at the prices first, then at the reasons.""",
   "Lexus LFA", "FROM UNSOLD STOCK TO AUCTION STAR (OUR READING)")

ch("The price timeline")
sc("""First data point: September two thousand seventeen. The Drive reported a two thousand twelve LFA, car number two hundred twenty-one of five hundred, with three hundred fifty-six miles, listed on duPont Registry at four hundred thirty-nine thousand, nine hundred dollars. That is an asking price, not a sale, in a dealer listing. The original price was three hundred seventy-five thousand.""",
   "Lexus LFA listing", "2017: ASKING $439,900 · 356 MILES")
sc("""By our own arithmetic, four hundred thirty-nine thousand, nine hundred over three hundred seventy-five thousand is about one point one seven. So in two thousand seventeen, seven years after launch, the asking price was about seventeen percent above the sticker price. A premium, but nothing like what came next.""",
   "Lexus LFA", "2017: ASKING ≈ +17% OVER STICKER (OUR ARITHMETIC)")
sc("""Second: early two thousand twenty-one. Motor Authority says a brown LFA was listed at a dealership in January twenty twenty-one with an asking price of six hundred eighty thousand dollars. A silver LFA sold for seven hundred twenty thousand at auction earlier in twenty twenty-one. By our arithmetic, that is a premium of about eighty-one and ninety-two percent over the sticker price.""",
   "Lexus LFA silver", "EARLY 2021: ASKING $680K · SOLD $720K")
sc("""Third: July twenty twenty-one. A Pearl Yellow two thousand twelve LFA with seventy-two miles sold for eight hundred eight thousand dollars on Bring a Trailer, according to Motor Authority. That is four hundred thirty-three thousand dollars over the sticker price, a premium of about one hundred fifteen percent, by our arithmetic.""",
   "Lexus LFA Pearl Yellow", "JULY 2021: $808,000 · 72 MILES (+115%)")
sc("""Fourth: April twenty twenty-two. Supercar Blondie reported a white two thousand twelve LFA with eight hundred fifty miles, chassis two hundred thirty-five of five hundred, sold on Bring a Trailer for eight hundred forty-five thousand dollars. By our arithmetic, that is a premium of about one hundred twenty-five percent over the original three hundred seventy-five thousand.""",
   "Lexus LFA white", "APRIL 2022: $845,000 · 850 MILES (+125%)")
sc("""Fifth: twenty twenty-three, and a pause. Motor16 says an LFA in the same Absolutely Red color as the next record car sold for six hundred seventy-five thousand dollars in twenty twenty-three, with higher mileage. By our arithmetic, that is about eighty percent over the sticker price, lower than the sales in the year before. Prices do not rise in a straight line.""",
   "Lexus LFA red", "2023: $675,000 (HIGHER MILEAGE) — A LOWER DATA POINT")
sc("""Sixth: April twenty twenty-four. Motor16 reported that a two thousand twelve LFA in Absolutely Red, unit one hundred seven of five hundred, with two hundred sixty-eight miles, sold for eight hundred ninety thousand dollars on Bring a Trailer after forty-five bids. The article calls that a record for a Lexus LFA. The original price was three hundred seventy-five thousand, plus twelve thousand, five hundred in factory options.""",
   "Lexus LFA Absolutely Red", "APRIL 2024: $890,000 · 268 MILES · 45 BIDS · \"RECORD\"")
sc("""By our arithmetic, eight hundred ninety thousand over a total original price of three hundred eighty-seven thousand, five hundred is about two point three. That is a premium of about one hundred thirty percent, including the options. The car has driven only two hundred sixty-eight miles, with eighty-eight miles under the last owner. Low mileage is part of what the price pays for.""",
   "Lexus LFA odometer", "APRIL 2024: 2.3× TOTAL ORIGINAL PRICE (OUR ARITHMETIC)")
sc("""There is a counterpoint in the same article. Motor16 says two LFAs in that same color were offered by Mecum months earlier, and neither sold. One had lower mileage. So a high reserve, or an unmet price, can stop a sale. The list of results we have is not a list of all attempts. It is a list of those that were reported, which skews toward the successes.""",
   "Auction block", "TWO LFAs OFFERED BY MECUM DID NOT SELL")

ch("The special one")
sc("""Then there is the special version. The Nürburgring Edition, Wikipedia says, had five hundred seventy-one metric horsepower, a top speed of two hundred ninety-eight kilometres per hour, and a lap of seven minutes, fourteen point six four seconds. Sixty-four were built, against a planned fifty. Motor Authority says the package added seventy thousand dollars to the base price.""",
   "Lexus LFA Nürburgring Edition", "NÜRBURGRING EDITION: 64 BUILT · +$70,000 PACKAGE")
sc("""In August twenty twenty-one, Motor Authority reported that a black Nürburgring Edition, with nine hundred thirty miles, sold at R M Sotheby's in California for one point six million dollars. The estimate was nine hundred thousand to one point one million. It was one of twenty-five delivered to the United States. By our arithmetic, one point six million over four hundred forty-five thousand is about three point six.""",
   "RM Sotheby's Monterey", "AUG 2021: $1.6M · 930 MILES · EST. $0.9–1.1M")
sc("""Another Nürburgring Edition, Club Lexus reported, sold at Barrett-Jackson in Scottsdale for nine hundred eighteen thousand, five hundred dollars, with eight hundred eighty-five miles. The article does not date the sale. The two results are about seven hundred thousand dollars apart for similar cars, which shows how much a single auction, a single room, or a single bidder can matter.""",
   "Barrett-Jackson", "ANOTHER N-EDITION: $918,500 · 885 MILES (UNDATED)")
sc("""A note on the sources. Club Lexus says fifty Nürburgring Editions were built. Wikipedia says sixty-four, from a planned fifty. Motor Authority says sixty-four. We use sixty-four, since two of three agree, and since Wikipedia explains the difference. It matters, because scarcity is what the price is paying for, and a count of fifty is more scarce than sixty-four.""",
   "Lexus LFA", "SOURCES DISAGREE: 50 VS 64 BUILT")

ch("In company at the auction")
sc("""Context helps. Motor Authority's report on the one point six million dollar sale listed other results from the same Monterey week. A Mercedes-Benz three hundred S L gullwing sold for one point three five two million. A Ford G T sold for one point two one five million. A Bugatti Veyron sold for one point five four five million. So the LFA Nürburgring Edition beat all three.""",
   "Monterey Car Week", "SAME WEEK: 300SL $1.352M · FORD GT $1.215M · VEYRON $1.545M")
sc("""That is striking, because the comparison cars are not obscure. A gullwing is one of the most famous classics. The Veyron was the fastest production car of its day. By our arithmetic, one point six million is about three point six percent more than the Veyron's one point five four five million. A nine year old Japanese car had passed a Bugatti at that sale.""",
   "Bugatti Veyron", "LFA N-EDITION ≈ 3.6% ABOVE THE VEYRON AT THE SAME SALE")
sc("""Club Lexus offers another comparison. At the Barrett-Jackson Scottsdale sale where a Nürburgring Edition made nine hundred eighteen thousand, five hundred dollars, the first production McLaren Senna sold for one million, four hundred fifty-seven thousand, and a Mercedes G sixty-three six by six, one of a hundred, for one million, two hundred ten thousand. The LFA was the third highest regular lot.""",
   "Barrett-Jackson Scottsdale", "SCOTTSDALE: LFA 3RD-HIGHEST REGULAR LOT ($918,500)")
sc("""The same article says that auction took one hundred thirty-one point six million dollars in total, Barrett-Jackson's highest-grossing Scottsdale sale. That is the setting: a room full of money, and a Lexus holding its own among Mercedes, McLaren and others. A reader should note that the article does not date the sale, so we cannot say how this compares to the other results in time.""",
   "Auction room", "$131.6M TOTAL SALES AT THAT AUCTION")

ch("The premium, sale by sale")
sc("""Let us put the premiums in a row, all our arithmetic from the sourced prices, against the three hundred seventy-five thousand dollar base. September twenty seventeen, asking, plus seventeen percent. January twenty twenty-one, asking, plus eighty-one. Early twenty twenty-one, sold, plus ninety-two. July twenty twenty-one, sold, plus one hundred fifteen.""",
   "Calculator", "+17% (2017 ASK) · +81% (JAN 2021 ASK) · +92% · +115% (JULY 2021)")
sc("""April twenty twenty-two, sold, plus one hundred twenty-five. Twenty twenty-three, sold, plus eighty. April twenty twenty-four, sold, plus one hundred thirty, counting the options, or plus one hundred thirty-seven against the base alone. The pattern is a climb with a pause, not a smooth curve, and it rests on single sales.""",
   "Price chart", "+125% (2022) · +80% (2023) · +137% VS BASE (2024)")
sc("""Look at the sold results alone. Seven hundred twenty thousand, eight hundred eight thousand, eight hundred forty-five thousand, six hundred seventy-five thousand, and eight hundred ninety thousand dollars. By our arithmetic, they all sit between one point eight and two point four times the base price. Five sales is far too few to call a market, but the range is narrow enough to be worth noting.""",
   "Lexus LFA", "FIVE SOLD RESULTS: 1.8× TO 2.4× THE BASE PRICE (OUR ARITHMETIC)")
sc("""And the asking prices tell another story. A dealer asked six hundred eighty thousand in January twenty twenty-one, and a car sold for seven hundred twenty thousand later that year. So the asking price was not wildly out of line with what the market paid. By our reading, owners and dealers knew what the car was worth, even before the record sales.""",
   "Lexus LFA dealership", "ASKING PRICES WERE NOT WILDLY OUT OF LINE (OUR READING)")
sc("""For the Nürburgring Edition the base for comparison is higher. Motor Authority says the package added seventy thousand dollars, so the original price was about four hundred forty-five thousand. One point six million is three point six times that. Nine hundred eighteen thousand, five hundred is two point one times that. The two results differ by a lot, which is the point of caution we made.""",
   "Lexus LFA Nürburgring Edition", "N-EDITION: 3.6× AND 2.1× THE $445K ORIGINAL (OUR ARITHMETIC)")

ch("Against the modern hypercars")
sc("""It is interesting to compare the LFA's price today with the cars that came after it. Wikipedia lists the Mercedes-AMG One at two point seven two million dollars new. Fortune says the Aston Martin Valkyrie costs at least three million. An LFA at eight hundred ninety thousand is, by our arithmetic, about thirty-three percent of the AMG One's price and about thirty percent of the Valkyrie's.""",
   "Hypercar prices", "LFA AT $890K ≈ 33% OF AMG ONE · ≈ 30% OF VALKYRIE")
sc("""Those cars are very different. Each has a hybrid system, more than a thousand horsepower, and a production run of two hundred seventy-five. The LFA has five hundred sixty metric horsepower and no hybrid system. So the comparison is not about performance. It is about where buyers draw the line, and a Japanese V ten sits, in the sales we have, well below it.""",
   "Lexus LFA and hypercars", "A DIFFERENT KIND OF CAR, A DIFFERENT PRICE BAND (OUR READING)")
sc("""Per horsepower, the sums are our own. The LFA at eight hundred ninety thousand dollars and five hundred fifty-three horsepower is about sixteen hundred nine dollars per horsepower. The AMG One at two point seven two million and one thousand forty-nine horsepower is about twenty-five hundred ninety-three. So the LFA costs about sixty-two percent as much per horsepower, even at today's price.""",
   "Price per horsepower", "LFA $1,609/HP VS AMG ONE $2,593/HP (OUR ARITHMETIC)")

ch("What changes the picture")
sc("""Two things could change the story. The first is condition. A car with a replaced engine, accident damage or missing documents would not sell at these prices, though our sources describe no such cars. The second is the buyer pool. If fewer collectors want Japanese V tens in future, prices could fall. We cannot know. We can only report what was paid.""",
   "Lexus LFA documents", "CONDITION AND BUYER DEMAND CAN CHANGE THE PICTURE")
sc("""There is also the matter of the last new car. Wikipedia says it sold in June twenty twenty-three, an Australian dealer's display car, at an undisclosed price. A new car, sold at a time when used ones were fetching more than double the sticker price. We would love to know the price. We do not, and neither does any source we found.""",
   "Lexus LFA last car", "THE LAST NEW LFA: PRICE NOT DISCLOSED")

ch("What a collector should ask")
sc("""If you were thinking about an LFA, what would you ask? First, the mileage, since the sources show that low mileage cars sold for the most. Second, the version, because the Nürburgring Edition sold at much higher prices. Third, the colour and history, since the red cars in our sources had notable sales, and the article stresses the low number of cars in that colour, thirty-eight.""",
   "Lexus LFA inspection", "ASK: MILEAGE · VERSION · COLOUR · HISTORY")
sc("""Fourth, what the service history says about the engine and the carbon structure, which are specialised. Our sources give no repair costs, so we do not know the figures. Fifth, how the car will be stored and insured. We have no price for either. These are the unpriced lines in any ownership of a car like this, and they are real.""",
   "Lexus LFA service", "SERVICE, STORAGE, INSURANCE: NO FIGURES IN OUR SOURCES")
sc("""We close with the most honest sentence we can write. The Lexus LFA is worth more now than new, on the evidence of single sales reported between twenty seventeen and twenty twenty-four. The reasons are partly sourced, partly our reading. And no source we found says what comes next. Anyone who tells you otherwise is telling you something they do not know.""",
   "Lexus LFA", "WORTH MORE THAN NEW: YES, ON THE REPORTED SALES")

ch("Why did the price rise?")
sc("""Now the question. None of our sources gives a single explanation, so what follows is partly what they report and partly our reading, which we label. The first reason is simple and sourced: scarcity. Five hundred cars were built, for the whole world. And a share of them, like the fifty or sixty-four Nürburgring Editions, are rarer still.""",
   "Lexus LFA", "REASON 1: SCARCITY — 500 CARS FOR THE WORLD")
sc("""The second reason is the engine. Wikipedia describes a naturally aspirated four point eight litre V ten, co-developed with Yamaha, with two octaves of sound channelled into the cabin, tuned in the manner of an Ovation guitar. Toyota engineers called it the roar of an angel. A sound like that cannot be added to a new car today. It is a product of a particular era.""",
   "Lexus LFA V10", "REASON 2: THE SOUND — NATURALLY ASPIRATED V10 (OUR READING)")
sc("""The third reason is the way it was made. A carbon fibre body, woven on a laser-monitored loom that Wikipedia says is one of only two in the world. Lexus's own magazine says the machine uses a hundred forty-four bobbins and builds parts like the roof pillar in twelve woven layers. A car made this way is a piece of manufacturing history as well as a car.""",
   "Lexus LFA carbon loom", "REASON 3: THE MANUFACTURING STORY")
sc("""The fourth reason is the ten years. Development began in early two thousand and production in December two thousand ten, according to Wikipedia. By our arithmetic, that is more than ten years of work for five hundred cars. A project like that is unlikely to be repeated, since companies rarely have the appetite for it.""",
   "Lexus LFA development", "REASON 4: A DECADE OF DEVELOPMENT FOR 500 CARS")
sc("""The fifth reason is the time that has passed. Cars that were cheap to buy new, or that sat unsold, can become icons when people look back. Our sources do not say this about the LFA directly, so we offer it as our reading. The Drive's line about a rocky launch followed by appreciation is consistent with it, but is not proof.""",
   "Lexus LFA", "REASON 5: HINDSIGHT (OUR READING)")
sc("""The sixth is the lack of a replacement. We found no source saying that Lexus plans another car like the LFA, and we will not claim that it does not. What we can say is that Mercedes, in a different case, was reported by Motor1 to have ruled out another Formula One engined road car. Rarity of the type, not just the car, may matter to buyers.""",
   "Lexus LFA", "REASON 6: NO CLEAR SUCCESSOR IN OUR SOURCES (OUR READING)")

ch("What this does not tell you")
sc("""Now the limits. First, these are nominal prices, not adjusted for inflation. The sources do not give inflation figures, so we have not adjusted them. A part of the rise between two thousand ten and twenty twenty-four is simply the fall in the value of money. How much, we do not say, because we have no sourced figure.""",
   "Calculator", "NOT ADJUSTED FOR INFLATION")
sc("""Second, these are the results that were reported. Cars that did not sell at auction, such as the two at Mecum, appear in only one of our sources. A list of sales is not a market index. A true value for one car needs comparable sales, and for a car with five hundred examples, there are few comparables.""",
   "Auction results", "REPORTED SALES ARE NOT A MARKET INDEX")
sc("""Third, condition and mileage matter enormously. The cars that sold for the most had very low mileage: seventy-two miles, two hundred sixty-eight miles, nine hundred thirty. The car with three hundred fifty-six miles was only asking four hundred thirty-nine thousand, nine hundred in two thousand seventeen. We cannot separate the effect of age from the effect of mileage.""",
   "Low-mileage Lexus LFA", "LOW MILEAGE IS PART OF THE PRICE")
sc("""Fourth, collectors' tastes change. A price that is a record one year may be a bargain, or a peak, in the next. The pause in twenty twenty-three, with six hundred seventy-five thousand for a car with higher mileage, reminds us that auction results move up and down. Nobody in our sources predicts where the price goes from here.""",
   "Auction", "NO ONE IN OUR SOURCES PREDICTS THE FUTURE")

ch("What it would have taken")
sc("""A sum to finish, all our arithmetic. A buyer who paid three hundred seventy-five thousand in two thousand eleven and sold for eight hundred ninety thousand in two thousand twenty-four would see a gain of five hundred fifteen thousand dollars. Over thirteen years, that is about thirty-nine thousand six hundred dollars a year, before costs and inflation.""",
   "Calculator", "+$515K OVER 13 YEARS ≈ $39,600/YEAR (OUR ARITHMETIC)")
sc("""But a buyer in two thousand eleven also paid for storage, insurance and upkeep, none of which our sources price. And money invested elsewhere might have grown too. So it is not correct to call the LFA a certain winner. It is correct to say that, at the sales we have, the buyer who held a low-mileage car did well.""",
   "Lexus LFA garage", "WE HAVE NO FIGURES FOR COSTS OF HOLDING THE CAR")
sc("""For those who want to understand the car rather than trade it, there is a simpler lesson. The LFA is worth more today because it was built to a standard that did not care about cost, and because only five hundred exist. Whether that is rational is not our business. Whether it is true, in the sales we have cited, is. And it is.""",
   "Lexus LFA", "THE PRICE REFLECTS HOW AND HOW FEW")
sc("""Do you think the LFA's price will keep rising, or has it peaked? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the LFA, compare it with the Nissan GT-R, and tell the story behind it. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video107", "Why the Lexus LFA Is Worth More Now Than New", [
    "Wikipedia, Lexus LFA: https://en.wikipedia.org/wiki/Lexus_LFA",
    "The Drive, There's a 356-mile Lexus LFA for sale in Ohio (23 Sept 2017): https://www.thedrive.com/article/14584/theres-a-356-mile-lexus-lfa-for-sale-in-ohio.md",
    "Motor Authority, Pearl Yellow 2012 Lexus LFA with 72 miles sells for $808,000 on Bring a Trailer (7 July 2021): https://www.motorauthority.com/news/1132702_pearl-yellow-2012-lexus-lfa-with-72-miles-sells-for-808-000-on-bring-a-trailer",
    "Motor Authority, Rare Lexus LFA Nürburgring Edition sells for $1.6M at auction (23 Aug 2021): https://www.motorauthority.com/news/1133164_rare-lexus-lfa-n-rburgring-edition-sells-for-1-6m-at-auction",
    "Supercar Blondie, Super rare Lexus LFA sells for massive $845k at auction (25 April 2022): https://supercarblondie.com/cars/lexus-lfa-850-miles-sells-845k/",
    "Motor16, Estrenar un Lexus LFA se paga a precio de oro (16 April 2024): https://www.motor16.com/noticias/estrenar-lexus-lfa-precio-oro-record/",
    "Club Lexus, Lexus LFA Nürburgring Edition nabs nearly $1M at auction: https://clublexus.com/articles/lexus-lfa-nurburgring-edition-nabs-nearly-1m-at-auction",
    "Lexus UK Magazine, Engineering innovations: the Lexus carbon loom: https://mag.lexus.co.uk/engineering-innovations-the-lexus-carbon-loom",
    "Motor1, Mercedes-AMG won't allow Project One owners to flip their cars: https://www.motor1.com/news/260939/mercedes-amg-project-one/",
], "C")
