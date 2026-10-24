import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""A Shelby Cobra four hundred twenty-seven cost seven thousand, five hundred dollars new. A Hagerty price guide dated April twenty twenty-five values a good condition one at two point two five million. That is three hundred times the original price. But a car that looks the same, a continuation Cobra, sold in March twenty twenty-four for three hundred thirty-five thousand. This is what a real Shelby Cobra costs today, and how to tell which one you are looking at.""",
   "Shelby Cobra 427", "WHAT A REAL SHELBY COBRA COSTS TODAY")
sc("""Here is the twist. The same chassis number can appear in two very different price lists. One Cobra sold in the twenty-tens for nine hundred two thousand dollars and later for one point six five five million. Another sold in two thousand five for five hundred thirty-five thousand and later for one point three two five million. And one of the cars that looks like a Cobra is not an original at all. Stay to the end.""",
   "Shelby Cobra auction", "SAME CAR, TWO PRICES, ONE FAKE QUESTION")
sc("""Every figure comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. This is not buying advice, and we cannot authenticate any car.""",
   "Shelby Cobra", "NOT BUYING ADVICE · EVERY NUMBER IS SOURCED")

ch("What a Cobra cost new")
sc("""Du Pont Registry says the original release price of the four hundred twenty-seven Cobra was seven thousand, five hundred dollars, and that in nineteen sixty-six it was priced well above any other American car. Our sources do not give the new price of the smaller two hundred sixty and two hundred eighty-nine cars, so we do not compare those.""",
   "Shelby Cobra 427 advert", "NEW, 1966: $7,500 FOR A 427 (DU PONT REGISTRY)")
sc("""Production was small. Du Pont Registry says Shelby American built nine hundred ninety-eight Cobras in total. Wikipedia lists a hundred twenty-six Mark One cars, about five hundred twenty-eight Mark Two cars, and fifty-six Mark Three four hundred twenty-sevens, and warns that the numbers do not fit the chassis numbering. So the supply of originals is a few hundred to a thousand, depending on the source.""",
   "Shelby Cobra production", "998 BUILT (DU PONT) · WIKIPEDIA'S COUNTS DIFFER")
sc("""The company itself did not do well. Wikipedia says Ford and Shelby ended imports from England in nineteen sixty-seven, and calls the Cobra a financial failure. So the cars that now sell for millions did not make a fortune for their makers. The market value today was created later, by scarcity and by the legend.""",
   "Shelby American", "THE COBRA WAS A FINANCIAL FAILURE FOR ITS MAKERS")

ch("The price list, car by car")
sc("""Now the prices, from Hagerty's past sales database and other sources. We start with the 427 side-oiler S slash C, chassis C S X three zero four zero, which sold at R M Auctions in Monterey in August two thousand one for four hundred fifty-one thousand dollars. It had about twenty-five thousand miles, was in good condition with a few repaints, and was described as an original factory S slash C.""",
   "Shelby Cobra 427 S/C", "AUG 2001: $451,000 · 427 S/C · ~25,000 MILES")
sc("""Hagerty's price guide, in a chart dated April twenty twenty-five, values that car's category, a number three good condition S slash C, at two million, two hundred fifty thousand dollars, up seven point one percent. By our arithmetic, two point two five million divided by four hundred fifty-one thousand is nearly five times, over about twenty-four years.""",
   "Shelby Cobra 427 S/C", "GUIDE, APRIL 2025: $2.25M (#3 GOOD) · ≈ 5× THE 2001 SALE")
sc("""A rough annual rate, our arithmetic. Five times over twenty-four years is about seven percent a year, compounded. That is before storage, insurance, maintenance and inflation, none of which our sources price. Nor is it a promise. It compares one sale with one guide value, not a market index, and the guide figure is an estimate rather than a sale.""",
   "Calculator", "≈ 7% A YEAR OVER 24 YEARS (OUR ARITHMETIC — NOT A PROMISE)")
sc("""Next, the four hundred twenty-seven that Du Pont Registry reports sold at Gooding and Company's Amelia Island auction in twenty twenty-two. A nineteen sixty-six car, chassis C S X three one nine two, for one million, fifty thousand dollars. Du Pont says original four hundred twenty-sevens start at over a million, and gives one and a half million as its spec-list figure, a discrepancy in itself.""",
   "Amelia Island auction", "2022: $1,050,000 · 1966 427 (CSX 3192)")
sc("""Another four hundred twenty-seven, or a four twenty-eight by its listing, chassis C S X three two nine nine, sold for one million, three hundred twenty-five thousand dollars, according to Hagerty. Its commentary says R M sold the same car in Boca Raton in two thousand five for five hundred thirty-five thousand. By our arithmetic, that is about two and a half times in the gap between the sales, which Hagerty does not date.""",
   "Shelby Cobra 427", "CSX 3299: $535,000 (2005) → $1,325,000 (LATER, UNDATED)")
sc("""The small-block cars. Hagerty lists a nineteen sixty-four two hundred eighty-nine, chassis C S X twenty-two oh eight, that sold for one million, six hundred fifty-five thousand dollars. The same car had sold at Gooding in Pebble Beach in twenty fifteen for nine hundred two thousand. Hagerty says the hammer bid was twenty-five percent over the high estimate, and that the car had forty-seven years with one owner.""",
   "Shelby Cobra 289", "CSX 2208: $902,000 (2015) → $1,655,000 (LATER, UNDATED)")
sc("""By our arithmetic, one million, six hundred fifty-five thousand over nine hundred two thousand is one point eight three, so the car gained about eighty-three percent between the two sales. We do not know the date of the second sale, so we cannot say per year. Hagerty adds that nothing in that car's history sets it apart from similar two hundred eighty-nines.""",
   "Shelby Cobra 289", "+83% BETWEEN TWO SALES (OUR ARITHMETIC)")
sc("""Two more two hundred eighty-nines from the same database. Chassis C S X twenty-four eighty-seven, Guardsman Blue, sold for one million, seventeen thousand, five hundred dollars. Chassis C S X twenty-two forty-two, Princess Blue, shows one million, two hundred forty-two thousand, five hundred. Neither page gives a sale date, so we do not know how recent they are. Both are rated excellent or better.""",
   "Shelby Cobra 289", "TWO MORE 289s: $1,017,500 AND $1,242,500 (UNDATED)")
sc("""Put the sourced prices for the small-block cars together and they range from just over one million to one point six five five million. Du Pont Registry says the two hundred eighty-nine is just under a million. So the prices in our sources cluster around the one million dollar mark, and the better cars with strong histories reach well above it.""",
   "Shelby Cobra 289 prices", "289s: ~$1.0M–$1.66M IN OUR SOURCES")

ch("How to read a chassis number")
sc("""Before you look at any price, learn to read the number, because the number is the identity. Wikipedia describes the Cobra's chassis numbers in series. The Mark One cars carry C S X numbers in the twenty-oh-one to twenty-six-oh-two range. The Mark Two cars carry C O B or C O X numbers in the sixty-oh-one range. The page itself warns that these ranges do not match the build counts exactly.""",
   "Shelby Cobra chassis plate", "CSX 2001–2602 (MK I) · COB/COX 6001+ (MK II)")
sc("""The four hundred twenty-seven cars in our sources carry C S X numbers in the three thousands. The Super Snake is three zero one five. The S slash C is three zero four zero. The nineteen sixty-six car Du Pont reports is three one nine two. The car Hagerty lists as a four twenty-eight is three two nine nine. The prototype is two thousand. All of these are from the originals' number blocks.""",
   "Shelby Cobra 427", "ORIGINALS: CSX 2000 · 2xxx · 3xxx · COB/COX 6xxx")
sc("""Then there are the C S X four thousand cars and above. Wikipedia says the C S X four thousand to four thousand nine ninety-nine series are four hundred twenty-seven S slash C continuations, and lists later series at six thousand, seven thousand, eight thousand and nine thousand, including a Daytona Coupe continuation. A number in those ranges is not a nineteen sixties Cobra, whatever it looks like.""",
   "Shelby Cobra continuation plate", "CSX 4000–9000: CONTINUATION SERIES (WIKIPEDIA)")
sc("""A caution, though. Wikipedia also records that in nineteen ninety-three the Los Angeles Times reported forty-three duplicate titles, and Carroll Shelby's page records allegations about skipped blocks of V I N numbers to satisfy homologation, with cars later relabelled as continuation. So the number alone is not a guarantee. Documentation, the history of the car, and an expert are what a buyer needs.""",
   "Shelby Cobra paperwork", "A NUMBER IS NOT ENOUGH: DOCUMENTS AND AN EXPERT")

ch("What drives the price")
sc("""Why does a Cobra cost so much? The sources point to several reasons. First, racing. Carroll Shelby's page says the Daytona Coupe won three G T class wins in nineteen sixty-four, including Le Mans and Goodwood, and that the Cobra won the International Championship for G T Manufacturers in nineteen sixty-five. A car with that record has a story that few road cars can match.""",
   "Shelby Daytona Coupe", "RACING: CLASS WINS 1964 · MANUFACTURERS' TITLE 1965")
sc("""Second, scarcity. Du Pont Registry says nine hundred ninety-eight were built. By our arithmetic, that is fewer than a seventh of the seven thousand, two hundred sixty-five Lamborghini Urus built in a single year, twenty twenty-five, according to Wikipedia. A car built in the hundreds, sixty years ago, with a fraction surviving in original condition, is rare in a way that most collectibles cannot be.""",
   "Shelby Cobra", "998 COBRAS VS 7,265 URUS IN ONE YEAR (OUR COMPARISON)")
sc("""Third, performance. Wikipedia lists a hundred sixty-four miles per hour for the standard four hundred twenty-seven and a hundred eighty-five for the S slash C. Du Pont lists zero to sixty in three point four seconds. In nineteen sixty-six those numbers were beyond almost any road car. Even now they are quick. Few cars from the era remain so impressive on paper.""",
   "Shelby Cobra 427 performance", "164–185 MPH · 0–60 IN 3.4 S (SOURCES VARY)")
sc("""Fourth, the story. Carroll Shelby's page says a film, Ford v Ferrari, depicted him in twenty nineteen and won an Oscar. The film is not about the Cobra, but it renewed public attention on Shelby. Whether it moved prices, our sources do not say. We mention it as a plausible influence, labelled as our reading, and not as a claim.""",
   "Ford v Ferrari", "SHELBY ON FILM: 2019 (OUR READING ON PRICE EFFECT)")
sc("""Fifth, the lack of supply. Du Pont Registry notes that unrestored originals start at over a million, and that the continuation cars pull the A C Cobra market below that. By our reading, that suggests a two-tier market, where authentic originals trade at their own level and the other cars are measured against them, not the reverse.""",
   "Shelby Cobra market", "A TWO-TIER MARKET (OUR READING)")

ch("A small sum on the 427")
sc("""A sum with the figures we have. The original Cobra four hundred twenty-seven cost seven thousand, five hundred dollars and made four hundred twenty-five horsepower, per Wikipedia and Du Pont. That is about seventeen dollars and sixty-five cents per horsepower. A good condition S slash C at two point two five million and four hundred eighty-five horsepower is about four thousand, six hundred thirty-nine dollars per horsepower.""",
   "Calculator", "$17.65/HP NEW → $4,639/HP AT THE 2025 GUIDE (OUR ARITHMETIC)")
sc("""The horsepower did not change. The price per horsepower rose by a factor of about two hundred sixty, by our arithmetic. That factor is the scarcity, the history and the legend, and none of it is mechanical. The same car, driven the same way, does the same things it did in nineteen sixty-six. The difference is what people will pay to own the story.""",
   "Shelby Cobra 427", "PRICE PER HP UP ~260× (OUR ARITHMETIC)")
sc("""Compare it with a modern car. In another video of this series, we saw a Lexus LFA sell for eight hundred ninety thousand dollars in April twenty twenty-four, about sixteen hundred dollars per horsepower. The Cobra's guide value per horsepower is about three times that. The LFA was twelve years old at that sale. The Cobra is sixty. Age, in this market, matters a lot.""",
   "Lexus LFA and Shelby Cobra", "LFA ~$1,609/HP VS COBRA S/C ~$4,639/HP (OUR ARITHMETIC)")

ch("The famous ones")
sc("""Some Cobras sit in a different league. Wikipedia says the Super Snake, chassis C S X three zero one five, converted in nineteen sixty-six with twin Paxton superchargers and used personally by Shelby, sold for five million dollars at Barrett-Jackson in January two thousand seven. The page converts that to about seven point two seven million in two thousand twenty-four dollars.""",
   "Shelby Cobra Super Snake", "SUPER SNAKE: $5M (JAN 2007) ≈ $7.27M IN 2024 DOLLARS")
sc("""And the very first car, C S X two thousand, sold for thirteen point seven five million dollars at R M Sotheby's in Monterey in August two thousand sixteen, EVO reports. Jalopnik called it a record for an American car at auction, beating an eleven million dollar G T forty. Those are unique cars. They tell you what the best of the best fetches, not what a Cobra costs.""",
   "Shelby Cobra CSX2000", "CSX 2000: $13.75M (AUGUST 2016)")
sc("""By our arithmetic, the prototype's price is more than eight times the highest ordinary sale in our list, the one point six five five million for the two hundred eighty-nine. And it is about six times the Hagerty guide figure for a good S slash C. Provenance is the multiplier. The first car, the car Shelby used, the car with the story, outsells the typical example by a wide margin.""",
   "Shelby Cobra CSX2000", "PROVENANCE: THE FIRST CAR ≈ 8× THE TYPICAL 289 SALE (OUR ARITHMETIC)")

ch("The other Cobras")
sc("""Now the twist. Wikipedia lists continuation series of Cobras, with chassis numbers from four thousand to nine thousand. The C S X four thousand series, a four hundred twenty-seven S slash C continuation built from McCluskey chassis, took about twenty years, ending in two thousand nine. These are new cars built to the old pattern, and they are not the nineteen sixties originals.""",
   "Shelby Cobra continuation", "CSX4000 SERIES: A 427 S/C CONTINUATION, ~20 YEARS TO BUILD")
sc("""Hagerty's database lists a nineteen sixty-five Shelby Cobra, chassis C S X four five six six, described as a C S X four thousand, four hundred twenty-seven S slash C, with an aluminium body, sold by R M Sotheby's in Coral Gables, Florida, on the first and second of March, twenty twenty-four, for three hundred thirty-five thousand dollars. The page does not itself say continuation. The chassis series number tells us that.""",
   "Shelby Cobra continuation", "MARCH 2024: $335,000 · CSX 4566 · 427 S/C (CSX4000 SERIES)")
sc("""By our arithmetic, three hundred thirty-five thousand is about fifteen percent of the two point two five million Hagerty guide value for an original S slash C. It is about one seventh. So a car that looks nearly identical, and has the same engine size, costs a fraction of an original. That fraction is the price of authenticity.""",
   "Shelby Cobra original and continuation", "CONTINUATION ≈ 15% OF AN ORIGINAL S/C'S GUIDE VALUE (OUR ARITHMETIC)")
sc("""Du Pont Registry makes the same point in words: A C Cobra prices have stayed under seven figures, partly because of continuation cars. And Wikipedia says most continuations are fibreglass, with some aluminium or carbon fibre. A buyer who confuses the two could pay a million dollars for a car worth a third of that, or the reverse. This is why chassis documentation matters most.""",
   "Shelby Cobra continuation", "\"PRICES HAVE STAYED UNDER SEVEN FIGURES\" — DU PONT, ON CONTINUATIONS")
sc("""And the paperwork has had its problems. Wikipedia says that in nineteen ninety-three the Los Angeles Times reported that Shelby had obtained forty-three duplicate titles for Cobras not in A C's records. Shelby said the chassis were built by McCluskey in nineteen ninety-one to ninety-two, and claimed a rival was behind the report. Carroll Shelby's page adds an allegation about skipped serial number blocks.""",
   "Los Angeles Times 1993", "1993: 43 DUPLICATE TITLES REPORTED · SHELBY DISPUTED IT")

ch("A cheaper way into the same family")
sc("""If a Cobra is out of reach, the family has cheaper members. The A C Ace shares the Cobra's ancestry, as we showed in another video. Hagerty's past sales list a nineteen fifty-nine Ace Bristol sold at Coys in London in December two thousand three for a hundred sixteen thousand, five hundred sixty-two dollars, and a nineteen fifty-six car at Bonhams in September twenty eleven for two hundred twenty-three thousand, one hundred twenty-four.""",
   "AC Ace Bristol", "ACE BRISTOL: $116,562 (2003) · $223,124 (2011)")
sc("""By our arithmetic, the two hundred twenty-three thousand dollar Ace is about ten percent of the two point two five million Cobra guide value. The cars share a chassis lineage, but the market treats them as different things. Hagerty's commentary on the 2011 sale called the price high for a standard Bristol-engined Ace, so even the cheaper cars are not cheap.""",
   "AC Ace and Shelby Cobra", "AN ACE BRISTOL ≈ 10% OF A COBRA S/C'S GUIDE VALUE (OUR ARITHMETIC)")
sc("""And there is the continuation route, with the three hundred thirty-five thousand dollar sale in March twenty twenty-four. A buyer who wants the shape, the sound and the driving experience, and who is content with a car that is not an original, has options in the low hundreds of thousands. That is still a lot of money, but it is a fraction of the original's price.""",
   "Shelby Cobra continuation", "THE CONTINUATION ROUTE: ONE SALE AT $335,000")
sc("""Different auction houses appear in these results, among them R M Auctions, R M Sotheby's, Gooding and Company, Bonhams and Barrett-Jackson. Each has its own fees and its own buyers, and our sources do not say whether the quoted prices include fees. So when you compare a number from one house with a number from another, keep that uncertainty in mind.""",
   "Auction houses", "FEES AND BUYERS DIFFER BY AUCTION HOUSE")
sc("""Finally, a note on timing. Prices in this video span from two thousand one to twenty twenty-five. Over that period, money itself changed value, and the market for American classics changed with it. We did not adjust for inflation, since our sources give no inflation figures, apart from Wikipedia's own conversion of the Super Snake price. So treat the rises we computed as nominal.""",
   "Calendar", "ALL PRICES NOMINAL: NOT ADJUSTED FOR INFLATION")

ch("What we could not find")
sc("""Now the limits. Our sources give prices for buying. They give nothing reliable for owning. We found no verified figures for insurance, storage, restoration or repair on a Cobra. Anyone who gives you a number for the annual cost has a source we did not find. We would rather say so than guess.""",
   "Classic car garage", "INSURANCE, STORAGE, REPAIRS: NO RELIABLE FIGURES")
sc("""There are other gaps. Several Hagerty pages we used do not date their sales. The Hagerty price guide is an estimate. Auction prices include buyer's fees in some houses and not in others, and our sources do not say which. And the condition ratings, number one to number four, mean that one car at one million and another at two can both be called real.""",
   "Auction results", "UNDATED SALES · GUIDE VALUES ARE ESTIMATES · FEES UNCLEAR")
sc("""Condition matters, as the Hagerty commentary shows. One two hundred eighty-nine had a driver's door that did not close fully when latched, and a stretched seat, yet still fetched more than a million and a half. Another was described as drives like new. Cars in this range are valued for history and originality first, and for freshness second.""",
   "Shelby Cobra 289 interior", "HISTORY AND ORIGINALITY BEFORE FRESHNESS")

ch("What a real Cobra costs")
sc("""So what does a real Shelby Cobra cost today? On the evidence we have. About one million dollars for an original small-block car, up to about one point six five million for a strong one. About one to two point two five million for a four hundred twenty-seven, depending on version and condition. Five million and up for a famous individual car. Thirteen point seven five million for the first.""",
   "Shelby Cobra", "~$1M–$1.66M (289) · $1M–$2.25M (427) · $5M–$13.75M (FAMOUS CARS)")
sc("""And what does a Cobra-shaped car cost? On the single sale we found, three hundred thirty-five thousand dollars for a continuation, though the sources hint at a wide range for continuations and replicas, which we did not sample. The headline is that two cars that look alike can differ by a factor of seven or more in price, and the chassis number tells you which is which.""",
   "Shelby Cobra", "CONTINUATION: $335,000 (ONE SALE) · 2.25M ÷ 335K ≈ 6.7×")
sc("""A last caution. We have not bought, sold or authenticated a Cobra, and we are not advisers. These are figures reported by Hagerty, Du Pont Registry, EVO, Jalopnik and Wikipedia, some of them undated. If you are thinking of buying one, hire a specialist and read the chassis history first. If you own one and know a verified detail we missed, tell us in the comments.""",
   "Shelby Cobra", "NOT ADVICE · HIRE A SPECIALIST")
sc("""Would you rather own an original or a continuation? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Cobra, compare it with the A C Ace, and tell the story of the man who built it. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video111", "What a Real Shelby Cobra Costs Today", [
    "Hagerty, 1965 Shelby Cobra 427 S/C (CSX3040), price guide April 2025: https://hagerty.com/valuation-tools/past-sales/1965-shelby-cobra/CSX3040/f33aeb97-e529-47a0-8f48-6136a6b53fde",
    "Hagerty, 1964 Shelby Cobra 289 R&P (CSX2208): https://www.hagerty.com/valuation-tools/past-sales/1964-shelby-cobra/CSX2208/fe4f3048-b49a-429e-93ab-1ff270bd4e6b",
    "Hagerty, 1964 Shelby Cobra 289 R&P (CSX2487): https://www.hagerty.com/valuation-tools/past-sales/1964-shelby-cobra/CSX2487/508d390d-cf5c-4893-a305-2d31e7849c8f",
    "Hagerty, 1964 Shelby Cobra 289 R&P (CSX2242): https://hagerty.com/valuation-tools/past-sales/1964-shelby-cobra/CSX2242/1c73c862-8bba-4cf2-8456-1681a53b057e",
    "Hagerty, 1967 Shelby Cobra 428 (CSX3299): https://hagerty.com/valuation-tools/past-sales/1967-shelby-cobra/CSX3299/e1f75911-e24a-4463-92e0-8ef7a889b60d",
    "Hagerty, 1965 Shelby Cobra CSX4000 427 S/C (CSX4566), RM Sotheby's Coral Gables, March 2024: https://www.hagerty.com/valuation-tools/past-sales/1965-shelby-cobra/CSX4566/23b78ba4-8c78-4aef-9d8a-20811f33adef",
    "Hagerty, 1959 AC Ace Bristol (BEX1117): https://www.hagerty.com/valuation-tools/past-sales/1959-ac-ace/BEX1117/1941242a-4d75-4ac0-bb77-074a95444bf2",
    "Hagerty, 1956 AC Ace Bristol (BE172): https://www.hagerty.com/valuation-tools/past-sales/1956-ac-ace/BE172/572ff6cd-fdbd-4ac0-9fb2-66be383447e4",
    "Du Pont Registry, Shelby 427 Cobra price, specs, photos and review: https://news.dupontregistry.com/blogs/specs/shelby-427-cobra-price-specs-photos-and-review",
    "EVO, First-ever Shelby Cobra sells for record $13.75 million (22 Aug 2016): https://evo.co.uk/news/17955/first-ever-shelby-cobra-sells-for-record-1375-million",
    "Jalopnik, The very first Shelby Cobra just sold for a staggering record $13.75 million (21 Aug 2016): https://www.jalopnik.com/the-very-first-shelby-cobra-just-sold-for-a-staggering-1785559850/",
    "Wikipedia, AC Cobra: https://en.wikipedia.org/wiki/Shelby_Cobra",
    "Wikipedia, Carroll Shelby: https://en.wikipedia.org/wiki/Carroll_Shelby",
], "C")
