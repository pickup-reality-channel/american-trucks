import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""Sixteen thousand, four hundred forty-nine dollars. That is what AAA says it costs, every single year, to own and drive a new half-ton pickup in twenty twenty-six. Not the price of the truck. The cost of keeping it. And the biggest piece of that bill never shows up on a receipt, never comes in the mail, and most owners never even notice it.""",
   'Ford F-150 pickup', '$16,449 A YEAR TO OWN A HALF-TON')
sc("""Diesel just broke its all-time record. Tire makers raised prices again. Insurance is climbing in dozens of states. And loans are the longest they have ever been. In this video we break down the five hidden costs of owning a truck, using AAA's twenty twenty-six numbers, federal fuel data and the latest financing reports, so you can see the real price before you buy.""",
   'pickup truck gas station', '5 HIDDEN COSTS OF OWNING A TRUCK')
sc("""Every number here comes from a published source, listed in the description. Your own costs will depend on where you live, how much you drive and what truck you choose. If we could not confirm a figure, we left it out. Let's start with the big picture.""",
   'pickup trucks parking lot', 'EVERY NUMBER IS SOURCED')
sc("""Every year, AAA publishes a study called Your Driving Costs. In twenty twenty-six, AAA looked at thirty-four popular models in seven categories and assumed fifteen thousand miles a year over five years. The average new vehicle cost twelve thousand, eight hundred sixty-three dollars a year to own and operate. That is about one thousand seventy-two dollars a month, or thirty-five dollars a day.""",
   'AAA car', 'AVERAGE NEW VEHICLE: $12,863/YEAR')
sc("""Now the first twist. Pickups cost a lot more than the average. According to AAA, a half-ton pickup cost about one dollar and ten cents per mile, or sixteen thousand, four hundred forty-nine dollars a year. A midsize pickup came in at about eighty-seven cents per mile, or thirteen thousand and eighty-nine dollars a year. Choosing the bigger truck costs more than three thousand dollars a year, before you tow a single thing.""",
   'Chevrolet Silverado Toyota Tacoma', 'HALF-TON: $16,449. MIDSIZE: $13,089')
sc("""And the powertrain matters. In AAA's pickup numbers, an electric pickup cost seventeen thousand, four hundred fourteen dollars a year, a gas pickup sixteen thousand, six hundred twenty-six, and a hybrid pickup sixteen thousand, one hundred seventeen. The hybrid was the cheapest pickup to own in AAA's twenty twenty-six study. We will come back to why.""",
   'Ford F-150 hybrid', 'EV $17,414. GAS $16,626. HYBRID $16,117')
sc("""So where does all that money go? AAA splits the bill into depreciation, finance charges, insurance, license and registration and taxes, fuel, and maintenance, repairs and tires. Some of those costs you feel every week. Others are silent. Let's go through the five hidden costs, from the one people notice least to the one that hurts most at the pump.""",
   'pickup truck dashboard', 'WHERE THE MONEY GOES')
sc("""Hidden cost number one is depreciation, the money your truck loses in value just by getting older. According to AAA, depreciation was the single biggest ownership cost in twenty twenty-six, averaging four thousand, four hundred twenty-two dollars a year for a new vehicle. That is more than insurance and more than fuel.""",
   'used pickup trucks lot', '1. DEPRECIATION: $4,422/YEAR')
sc("""Here is why it is hidden. You never write a check for depreciation. It only appears when you sell or trade in the truck, and the dealer offers far less than you paid. By then, the money is already gone. Over five years, at AAA's average, that is more than twenty-two thousand dollars of value that quietly disappears.""",
   'car dealership trade in', 'YOU NEVER WRITE A CHECK FOR IT')
sc("""The twist is that trucks often hold their value better than many cars. Pickups are popular on the used market, and buyers who need to work or tow keep demand high. But that does not mean depreciation is small. A truck that costs sixty-seven thousand dollars, which Kelley Blue Book says was the average full-size pickup price in September twenty twenty-six, has a lot of value to lose.""",
   'Ram 1500 pickup', 'AVG FULL-SIZE PICKUP: $67,573')
sc("""How do you shrink depreciation? Buy the trims and engines that used buyers want. Avoid paying for options you will not use, because they rarely return their full cost at resale. Keep service records. And consider a lightly used truck, where the first owner has already absorbed the steepest part of the drop.""",
   'used pickup truck', 'HOW TO SHRINK DEPRECIATION')
sc("""And watch the market. When a model is discontinued, or when big rebates hit new trucks, used values can fall. The Ford F-one-fifty Lightning is an example. Ford ended production of the electric truck in twenty twenty-five and took a large charge as it shifted strategy, according to Fox Business. Changes like that can move resale values for years.""",
   'Ford F-150 Lightning', 'WHEN MODELS END, VALUES MOVE')
sc("""Hidden cost number two is the cost of borrowing. According to AAA, finance charges averaged one thousand, one hundred eighty-four dollars a year. But for truck buyers, the real numbers can be much bigger, because trucks are expensive and loans are getting longer.""",
   'car loan paperwork', '2. FINANCE CHARGES: $1,184/YEAR')
sc("""According to Edmunds, in the third quarter of twenty twenty-six, the average new vehicle loan carried a seven percent interest rate on a record forty-four thousand, six hundred sixty-four dollars financed. The average monthly payment was seven hundred eighty-seven dollars. And the total interest over the life of the average new loan was nine thousand, nine hundred thirty-eight dollars.""",
   'car dealership finance office', 'AVG LOAN INTEREST: $9,938')
sc("""Here is the twist. Twenty-five point five percent of new vehicle loans in that quarter had terms of eighty-four months or longer, according to Edmunds. Seven years. A longer loan makes the payment look smaller, but you pay interest for longer, and you may owe more than the truck is worth for much of that time. That is called being upside down.""",
   'calendar seven years', '25.5% OF LOANS: 84+ MONTHS')
sc("""There is good news in twenty twenty-six. According to Fox reporting from January, a new federal deduction lets eligible buyers deduct up to ten thousand dollars a year in auto loan interest. But there are strict rules. The vehicle must be new, bought for personal use, and have final assembly in the United States, and the deduction phases out for higher incomes. Check with a tax professional.""",
   'pickup truck assembly plant', 'UP TO $10,000 INTEREST DEDUCTION')
sc("""How do you cut the cost of borrowing? Get pre-approved by a bank or credit union before you visit the dealer. Put more money down. Choose the shortest loan you can afford. And compare the total cost of the loan, not just the monthly payment. A lower payment over more months often costs thousands more.""",
   'credit union', 'GET PRE-APPROVED FIRST')
sc("""Hidden cost number three is insurance. According to AAA, insurance averaged two thousand and ninety-eight dollars a year for a new vehicle in twenty twenty-six. Insurify put the national average for full coverage at two thousand, two hundred thirty-seven dollars in the first half of twenty twenty-six.""",
   'insurance paperwork', '3. INSURANCE: ~$2,100-$2,237/YEAR')
sc("""Now the surprise. Trucks are not always more expensive to insure. In Insurify's comparison, full coverage for a full-size pickup averaged one hundred ninety-seven dollars a month, compared with two hundred forty-six for a sedan. Trucks are popular in rural areas with fewer accidents, which helps.""",
   'pickup truck rural road', 'PICKUP $197/MO VS SEDAN $246/MO')
sc("""But performance trucks flip the math. According to Insure dot com data, the Ram fifteen hundred T R X cost three thousand, two hundred fifty-five dollars a year to insure in twenty twenty-six, and the Ford F-one-fifty Raptor two thousand, six hundred eighty-two. And theft matters. The National Insurance Crime Bureau ranked the Chevrolet Silverado fifteen hundred as the fourth most stolen vehicle in America in twenty twenty-five.""",
   'Ram TRX', 'TRX: $3,255/YEAR TO INSURE')
sc("""Another reason insurance keeps climbing is repairs. According to Insurify, auto repair and maintenance costs have risen about forty-five percent in five years. Modern trucks are full of cameras, radar and sensors. A small fender bender can mean recalibrating safety systems, and that bill lands on your insurer, and then on your premium.""",
   'pickup truck repair shop', 'REPAIR COSTS: +45% IN 5 YEARS')
sc("""The fix is simple and free: get insurance quotes on the exact truck and trim before you buy. Two trucks with the same price can have very different premiums. And shop your policy again at every renewal. It is one of the easiest truck costs to lower.""",
   'laptop insurance quote', 'GET QUOTES BEFORE YOU BUY')
sc("""Hidden cost number four is the one that surprises people every month: maintenance, repairs and tires. According to AAA, these costs averaged eleven point seven cents per mile in twenty twenty-six. At fifteen thousand miles a year, that is about one thousand, seven hundred fifty-five dollars a year.""",
   'pickup truck oil change', '4. MAINTENANCE & TIRES: 11.7¢/MILE')
sc("""And trucks have a special problem: big tires. A full-size truck can wear large, expensive tires, and a set can cost far more than tires for a small car. In twenty twenty-six, tire prices kept rising. According to SlashGear, the federal Producer Price Index for tire manufacturing climbed again in August twenty twenty-six, and some manufacturers announced increases of up to five to ten percent.""",
   'pickup truck tires', 'TIRE PRICES KEEP RISING')
sc("""Why? According to SlashGear, Michelin said in April twenty twenty-six that the conflict in the Middle East was raising its raw material and energy costs. Rubber and many tire materials are made from oil. So when oil prices jump, tire prices follow, and truck owners with big tires feel it the most.""",
   'tire factory', 'OIL PRICES PUSH TIRE PRICES')
sc("""Here is the twist about maintenance. It is the one hidden cost you can really control. Follow the maintenance schedule in your owner's manual, especially if you tow, because towing usually counts as severe service. Rotate the tires, check the pressure every month, and fix small problems before they become big ones.""",
   'pickup truck owner manual', 'THE COST YOU CAN CONTROL')
sc("""And plan for the big items. Brakes, batteries, shocks and tires do not wear out every year, but when they do, the bill can be large. Setting aside money each month for maintenance, as if it were a small payment, makes those bills much easier to handle.""",
   'brake repair', 'SAVE FOR THE BIG ITEMS')
sc("""Hidden cost number five is fuel, and in twenty twenty-six it stopped being hidden. AAA's study used a twelve-month average gas price of four dollars and fifteen cents a gallon through May twenty twenty-six, up almost thirty-two percent from the year before. Fuel averaged seventeen point three cents a mile across all vehicles.""",
   'gas station prices', '5. FUEL: $4.15/GAL IN AAA STUDY')
sc("""And then it got worse. According to AAA, as reported by NPR, the national average for diesel hit a record six dollars and five cents a gallon on September eleventh, twenty twenty-six. Ten days later, AAA reported a new record of six dollars and fifty-one cents. The previous record, from twenty twenty-two, was about five dollars and eighty-two cents.""",
   'diesel pump', 'DIESEL RECORD: $6.51/GAL')
sc("""Why? NPR reported that the war with Iran, which began in late February twenty twenty-six, disrupted oil shipments through the Strait of Hormuz. Brent crude traded above one hundred five dollars a barrel in September, compared with about seventy dollars before the war. Diesel, which moves goods across the country, was hit especially hard.""",
   'oil tanker ship', 'WAR PUSHED OIL ABOVE $105')
sc("""According to the U S Energy Information Administration, in the week of October nineteenth, twenty twenty-six, regular gasoline averaged four dollars and twenty-eight cents a gallon, and diesel six dollars and twenty-eight cents. A year earlier, gas was about three dollars and two cents, and diesel three sixty-two. For a truck that burns a lot of fuel, that difference adds up fast.""",
   'gas station sign prices', 'GAS $4.28. DIESEL $6.28 (OCT 2026)')
sc("""Here is the twist. For a truck owner driving fifteen thousand miles a year, the type of engine now matters more than ever. A hybrid that uses less fuel saves more when fuel is expensive. A diesel that is efficient on the highway can still cost more per mile when diesel is two dollars more than gas. We cover this in detail in our diesel versus gas versus hybrid video.""",
   'Toyota Tundra hybrid', 'THE ENGINE MATTERS MORE THAN EVER')
sc("""How do you cut fuel costs? Choose the smallest truck and engine that really does your job. Keep tires properly inflated. Remove heavy items you do not need from the bed. Avoid long idling. And remember that lift kits and big off-road tires usually reduce fuel economy. Every choice adds up over fifteen thousand miles.""",
   'pickup truck highway', 'HOW TO CUT FUEL COSTS')
sc("""There is one more cost that hides in plain sight: license, registration and taxes. According to AAA, these averaged eight hundred two dollars a year in twenty twenty-six. On an expensive truck, sales tax at purchase can add thousands more, and some states charge registration fees based on the vehicle's value or weight.""",
   'DMV office', 'BONUS: REGISTRATION & TAXES $802/YEAR')
sc("""And then there are costs AAA does not count at all: parking, tolls, accessories, bed covers, hitches and modifications. These can add hundreds or thousands of dollars a year. They are the ones owners forget to budget, because they come one at a time.""",
   'pickup truck accessories', 'THE COSTS NOBODY COUNTS')
sc("""So let's add it up. For a new half-ton pickup, AAA's twenty twenty-six number is sixteen thousand, four hundred forty-nine dollars a year. That is about one thousand, three hundred seventy dollars a month, before accessories and before the diesel spike that came after AAA's fuel data. That is the real price of truck ownership.""",
   'Ford F-150 Chevrolet Silverado Ram 1500', 'THE REAL TOTAL: ~$1,370/MONTH')
sc("""Now the final twist. The truck with the lowest sticker price is not always the cheapest to own. A truck that holds its value, is cheap to insure and uses less fuel can cost less over five years than a cheaper truck that loses value fast and drinks fuel. That is exactly why the hybrid pickup came out cheapest in AAA's study.""",
   'Ford Maverick hybrid', 'LOWEST PRICE ≠ LOWEST COST')
sc("""Consider the Ford Maverick. According to Ford, the Maverick sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, and eighty-one thousand and thirty-four were hybrids. Buyers clearly understood that a small hybrid truck could save money every month. For twenty twenty-seven, Ford Authority reports the base Maverick X L becomes hybrid only.""",
   'Ford Maverick', 'MAVERICK: 81,034 HYBRIDS IN 2025')
sc("""And the same idea works with bigger trucks. According to Ford, it sold eighty-four thousand, nine hundred thirty-four F-one-fifty hybrids in twenty twenty-five, up fifteen percent. For buyers who need a full-size truck, the hybrid can trim fuel costs without giving up towing capability.""",
   'Ford F-150 PowerBoost', '84,934 F-150 HYBRIDS IN 2025')
sc("""Let's put real numbers on a five-year plan. Using AAA's half-ton pickup estimate, five years of ownership adds up to about eighty-two thousand dollars. That is more than the price of the average full-size pickup. In other words, over five years, the cost of keeping a truck can be bigger than the cost of buying it.""",
   'pickup truck', '5 YEARS: ~$82,000 TO OWN A HALF-TON')
sc("""And that assumes fifteen thousand miles a year. Drive twenty thousand miles, and fuel, tires and maintenance go up. Drive less, and depreciation becomes a bigger share of the bill, because the truck loses value even when it sits in the driveway. There is no way to avoid every cost, but you can choose which ones you pay.""",
   'pickup truck driveway', 'MILES CHANGE THE MATH')
sc("""Here is the twist many owners miss. The costs do not stay the same each year. In the first years, depreciation and finance charges are heaviest. In later years, depreciation slows and the loan is paid off, but repairs and tires start to grow. Knowing that curve helps you decide when to keep a truck and when to sell it.""",
   'old pickup truck', 'COSTS SHIFT OVER TIME')
sc("""Many owners find a sweet spot after the loan is paid off. If the truck is reliable, a few years without a payment can save a lot of money, even with higher repair bills. The most expensive habit in truck ownership is trading in every few years and starting a new loan each time.""",
   'pickup truck paid off', 'THE NO-PAYMENT SWEET SPOT')
sc("""Now let's talk about the people who tow. Towing adds costs that AAA's averages do not fully show. Towing increases fuel use, wears brakes and transmissions faster, and often means following the severe service maintenance schedule. A truck that tows every weekend will cost more to own than the same truck that does not.""",
   'pickup truck towing trailer', 'TOWING ADDS HIDDEN COSTS')
sc("""And towing can require extra equipment: a proper hitch, a brake controller, wiring, mirrors and sometimes a weight distribution hitch. These parts protect your truck and your safety, so they are worth buying right. But they belong in your budget before you buy the trailer.""",
   'trailer hitch', 'BUDGET FOR TOWING GEAR')
sc("""Work trucks have their own costs. If you use your truck for a business, you may need commercial insurance, which can cost more than a personal policy, according to Insurify. On the other hand, business use can come with tax deductions. A tax professional can tell you which applies to you.""",
   'work truck', 'WORK TRUCKS: COMMERCIAL INSURANCE')
sc("""Now the electric question. In AAA's twenty twenty-six numbers, the electric pickup was the most expensive to own, at seventeen thousand, four hundred fourteen dollars a year, even though electricity cost much less per mile than gas. Why? Mostly higher purchase prices and depreciation. Cheaper fuel did not make up for the rest.""",
   'electric pickup truck charging', 'EV PICKUP: MOST EXPENSIVE TO OWN')
sc("""That could change as prices fall and more used electric trucks hit the market. But for now, AAA's study shows that the cheapest fuel does not automatically mean the cheapest truck. Fuel is only one of six costs, and depreciation is still the biggest.""",
   'electric pickup', 'CHEAP FUEL ≠ CHEAP TRUCK')
sc("""There is also the question of used versus new. A used truck usually has lower depreciation and lower insurance, but it may need more repairs and come with a higher interest rate. According to Experian, used vehicle loans averaged eleven point one nine percent in the second quarter of twenty twenty-six, compared with six point three five percent for new.""",
   'used pickup trucks', 'USED LOANS: 11.19% VS NEW 6.35%')
sc("""So a used truck is not automatically cheaper to own. If you pay cash, a used truck can be a big win. If you finance at a high rate, the interest can eat the savings. Compare the total cost of both, including interest, before you decide.""",
   'pickup truck for sale', 'COMPARE THE TOTAL COST')
sc("""And one more hidden cost hides inside the payment itself: the add-ons sold in the finance office. Extended warranties, paint protection and service plans can add thousands to a loan, and then you pay interest on them for years. Some can be useful, but they are always optional, and they can usually be bought later or not at all.""",
   'car dealership finance office', 'FINANCE OFFICE ADD-ONS')
sc("""The simple rule is this: if you would not pay cash for an add-on today, think twice before financing it for seven years. A two thousand dollar product on a long loan can cost far more once interest is included.""",
   'money calculator', 'WOULD YOU PAY CASH FOR IT?')
sc("""Before you buy, run your own numbers. Look up the insurance quote, estimate fuel for your real driving, check the loan's total interest, and look at resale values for the truck you want. Twenty minutes with a calculator can save you thousands of dollars over the life of the truck.""",
   'calculator budget', 'RUN YOUR OWN NUMBERS')
# ---------- CLOSE ----------
sc("""So here is your hidden cost checklist for twenty twenty-seven. One: estimate depreciation and buy the trims used buyers want. Two: compare the total cost of the loan, not the payment. Three: get insurance quotes before you choose. Four: budget for tires and maintenance. And five: choose the engine that fits fuel prices and your real driving.""",
   'checklist', 'YOUR HIDDEN COST CHECKLIST')
sc("""We put every one of these costs, with worksheets to calculate your own, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video, about which truck mods are actually worth the money. And tell us in the comments: what is the most surprising cost of owning your truck? Thanks for watching.""",
   'pickup truck sunset', "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {'Sixteen thousand, four hundred forty-nine': 'Intro', 'Every year, AAA publishes a': 'The big picture', 'Hidden cost number one is': '1. Depreciation', 'Hidden cost number two is': '2. The cost of borrowing', 'Hidden cost number three is': '3. Insurance', 'Hidden cost number four is': '4. Maintenance, repairs and tires', 'Hidden cost number five is': '5. Fuel', 'There is one more cost': 'Bonus: the cost nobody budgets', "So let's add it up.": 'Adding it all up', "Let's put real numbers on": 'The five-year reality', "Now let's talk about the": 'Towing and work trucks', 'Now the electric question. In': 'The electric twist', 'There is also the question': 'New or used?', 'So here is your hidden': 'Your checklist for 2027'}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": 'video55', "length_scale": 1.45,
  "title": 'The Real Cost of Owning a Truck in 2026: 5 Hidden Costs (One Is $4,422 a Year)', "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.45/212,1), "min")
