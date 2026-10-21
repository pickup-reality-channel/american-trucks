import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

sc("""Six dollars and fifty-one cents. In September twenty twenty-six, the average price of diesel in America hit an all-time record, according to AAA. For decades, truck owners were told that diesel pays off in the long run. But when diesel costs two dollars more per gallon than gasoline, that old rule breaks. And the numbers show something that would have sounded crazy just one year ago.""",
   'diesel pump', 'DIESEL RECORD: $6.51/GALLON')
sc("""So which truck engine actually pays off now: diesel, gas or hybrid? We will look at fuel prices, ownership costs, towing, maintenance and resale, using AAA's twenty twenty-six study, federal fuel data and the latest sales numbers. And we will do the math that most dealers will not do for you.""",
   'Ford F-150 Ram 2500 Toyota Tundra', 'DIESEL VS GAS VS HYBRID')
sc("""Every number here comes from a published source, listed in the description. When we use example fuel economy numbers to show the math, we will tell you clearly that they are examples. Your own results depend on your truck and how you drive. If we could not confirm a figure, we left it out. Let's start with the shock.""",
   'pickup truck gas station', 'EVERY NUMBER IS SOURCED')
sc("""According to NPR, the national average for diesel passed six dollars a gallon for the first time ever on September eleventh, twenty twenty-six, reaching six dollars and five cents, according to AAA. A year earlier, it was about three dollars and seventy cents. The previous record, from twenty twenty-two, was about five dollars and eighty-two cents.""",
   'diesel fuel price sign', 'SEPT 11: DIESEL PASSES $6')
sc("""And it kept climbing. On September twenty-first, AAA reported a new record of six dollars and fifty-one cents a gallon, according to WTOC. In Georgia, truck drivers described lines of trucks at fuel stops, and one owner-operator said a single fill-up of his big rig cost about one thousand two hundred fifty dollars.""",
   'truck stop diesel', 'SEPT 21: $6.51 RECORD')
sc("""Why did this happen? NPR reported that the war with Iran, which began in late February twenty twenty-six, disrupted shipping through the Strait of Hormuz, a key route for oil tankers. Brent crude traded above one hundred five dollars a barrel in September, compared with about seventy dollars before the war.""",
   'oil tanker Strait of Hormuz', 'THE WAR AND THE STRAIT OF HORMUZ')
sc("""Here is the first twist. Diesel was hit harder than gasoline. According to the U S Energy Information Administration, in the week of October nineteenth, twenty twenty-six, regular gas averaged four dollars and twenty-eight cents, and diesel six dollars and twenty-eight cents. That is a gap of exactly two dollars a gallon.""",
   'gas station prices sign', 'GAS $4.28 VS DIESEL $6.28')
sc("""A year earlier, in October twenty twenty-five, the gap was much smaller. According to the same E I A data, gas was about three dollars and two cents, and diesel about three sixty-two. The gap was only about sixty cents. In one year, the diesel penalty more than tripled.""",
   'fuel prices chart', 'THE GAP: $0.60 → $2.00')
sc("""And history shows how extreme this is. NPR noted that the two thousand eight diesel peak of about four seventy-four, adjusted for inflation, equals about seven dollars and twenty cents in today's money. So in real terms, prices have been even higher before. But for today's truck owners, six dollars is a number they have never seen at the pump.""",
   'diesel pump nozzle', '2008 PEAK = ~$7.20 TODAY')
sc("""Now let's look at the big picture of ownership. AAA's Your Driving Costs study for twenty twenty-six compared pickups by powertrain. An electric pickup cost seventeen thousand, four hundred fourteen dollars a year to own. A gas pickup cost sixteen thousand, six hundred twenty-six. And a hybrid pickup cost sixteen thousand, one hundred seventeen.""",
   'AAA car', 'AAA: HYBRID PICKUP CHEAPEST')
sc("""So the hybrid was the cheapest pickup to own in AAA's study, about five hundred dollars a year less than gas, and almost thirteen hundred less than electric. AAA's per-mile numbers tell the same story: about one dollar and seven cents a mile for the hybrid pickup, one ten for gas and one sixteen for electric.""",
   'Ford F-150 hybrid', 'HYBRID $1.07/MI. GAS $1.11. EV $1.16')
sc("""Here is an important detail. AAA's fuel numbers used a twelve-month average gas price of four dollars and fifteen cents through May twenty twenty-six, assuming fifteen thousand miles a year over five years. And AAA's pickup comparison did not include a diesel category. So for diesel, we have to do the math ourselves.""",
   'calculator fuel', "AAA DIDN'T SCORE DIESEL")
sc("""Before we do, let's understand why each engine exists. Diesel engines are known for strong low-speed torque and efficiency under heavy loads, which is why they dominate heavy-duty towing. Gas engines are usually cheaper to buy and simpler to maintain. And hybrids add an electric motor and battery to save fuel, especially in stop-and-go driving.""",
   'diesel engine', 'WHY EACH ENGINE EXISTS')
sc("""Today, you can find all three in pickups. GM offers the three liter Duramax diesel in its half-ton trucks. According to CarGurus, in the G M C Sierra Denali Ultimate it makes three hundred five horsepower and four hundred ninety-five pound-feet of torque. Heavy-duty trucks from Ford, Ram and GM offer big diesel V eights and inline sixes.""",
   'GMC Sierra Denali', 'DURAMAX 3.0: 495 LB-FT')
sc("""And hybrids have grown fast. According to Ford, it sold eighty-four thousand, nine hundred thirty-four F-one-fifty hybrids in twenty twenty-five, up fifteen percent. The Toyota Tundra's i-Force Max hybrid makes four hundred thirty-seven horsepower and five hundred eighty-three pound-feet of torque, according to CarGurus. That is more torque than the half-ton diesel.""",
   'Toyota Tundra', 'TUNDRA HYBRID: 583 LB-FT')
sc("""Here is the twist about hybrids. Truck hybrids are not just about fuel economy. They are also about torque. Electric motors deliver strong torque instantly, which helps with towing and acceleration. That is why some hybrid pickups are sold as performance options, not just economy options.""",
   'Ford F-150 PowerBoost', 'HYBRIDS ARE ABOUT TORQUE TOO')
sc("""Now the math. We will use example fuel economy numbers, not the rating of any specific truck, to show how prices change the answer. Imagine a gas truck that gets twenty miles per gallon, a diesel truck that gets twenty-five, and a hybrid truck that gets twenty-four. All driven fifteen thousand miles a year.""",
   'pickup trucks highway', 'THE MATH (EXAMPLE NUMBERS)')
sc("""The gas truck uses seven hundred fifty gallons a year. At four dollars and twenty-eight cents, that is about three thousand two hundred ten dollars. The diesel uses six hundred gallons. At six dollars and twenty-eight cents, that is about three thousand seven hundred sixty-eight dollars. The diesel uses fewer gallons, but costs more than five hundred dollars a year more to fuel.""",
   'diesel truck fueling', 'EXAMPLE: GAS $3,210 VS DIESEL $3,768')
sc("""Now the big twist. Run the same example with October twenty twenty-five prices. Gas at three dollars and two cents: about two thousand two hundred sixty-five dollars a year. Diesel at three sixty-two: about two thousand one hundred seventy-two. One year ago, the diesel was cheaper to fuel. Today it is more expensive. Same trucks, same miles, different war.""",
   'fuel prices', '2025: DIESEL WON. 2026: DIESEL LOST')
sc("""And the hybrid? In our example, the hybrid uses six hundred twenty-five gallons of gas a year. At four dollars and twenty-eight cents, that is about two thousand six hundred seventy-five dollars. That is about five hundred thirty dollars less than the gas truck, and about eleven hundred less than the diesel, at today's prices.""",
   'Toyota Tundra hybrid', 'EXAMPLE: HYBRID $2,675')
sc("""Here is a simple rule you can use with any truck. Divide the diesel price by the gas price. Today, six twenty-eight divided by four twenty-eight is about one point four seven. That means a diesel needs to get about forty-seven percent better fuel economy than the gas version just to break even on fuel. A year ago, it needed only about twenty percent better.""",
   'calculator', 'BREAK-EVEN: DIESEL NEEDS +47% MPG')
sc("""And there is another hidden diesel cost: diesel exhaust fluid, often called D E F. Modern diesel trucks use it to reduce emissions, and it must be refilled regularly. It is not expensive compared with fuel, but it is one more cost a gas or hybrid owner never pays.""",
   'diesel exhaust fluid', 'DIESEL EXTRA: DEF FLUID')
sc("""So for fuel alone, at twenty twenty-six prices, a light-duty diesel is hard to justify for most drivers. But fuel is not the whole story. Towing, purchase price, maintenance and resale all matter. Let's go through them.""",
   'pickup truck towing', 'FUEL IS NOT THE WHOLE STORY')
sc("""Towing is where diesel fights back. When you tow a heavy trailer, gas engines often lose a lot of efficiency, while diesels tend to hold up better under load. Diesels also offer exhaust braking in many trucks, which helps control speed on long downhill grades without overheating the brakes.""",
   'Ram 3500 towing', 'TOWING: WHERE DIESEL FIGHTS BACK')
sc("""For very heavy trailers, such as big fifth wheel campers, horse trailers and equipment, heavy-duty diesel trucks remain the standard choice. Their engines, transmissions and cooling systems are built to pull big loads for long distances. For those owners, the question is less about fuel and more about the right tool.""",
   'fifth wheel trailer diesel truck', 'HEAVY LOADS: DIESEL STILL RULES')
sc("""Here is the twist for half-ton buyers. Hybrids are now serious tow vehicles too. Ford's F-one-fifty PowerBoost and Toyota's Tundra i-Force Max are rated to tow large trailers, and their electric torque helps at low speeds. But hybrid fuel savings shrink when towing on the highway, because the battery helps most in stop-and-go driving.""",
   'Ford F-150 towing trailer', 'HYBRIDS TOW TOO')
sc("""And electric trucks? They have huge torque, but towing can cut their range dramatically. Ford ended production of the F-one-fifty Lightning in twenty twenty-five and took a large charge as it shifted strategy, according to Fox Business. For long-distance towing, most buyers in twenty twenty-six still choose diesel, gas or hybrid.""",
   'Ford F-150 Lightning', 'ELECTRIC: TOWING CUTS RANGE')
sc("""Now purchase price. Diesel engines usually cost extra as an option, and on heavy-duty trucks the diesel option can add many thousands of dollars. Hybrids also often cost more than the base gas engine. The gas engine is usually the cheapest to buy.""",
   'car dealership window sticker', 'PURCHASE PRICE: GAS IS CHEAPEST')
sc("""And financing makes every extra dollar more expensive. According to Edmunds, the average new vehicle loan in the third quarter of twenty twenty-six carried a seven percent interest rate, and the average total interest over the loan was nine thousand, nine hundred thirty-eight dollars. An expensive engine option on a long loan costs more than its sticker price.""",
   'car loan paperwork', '7% LOANS MAKE OPTIONS COSTLIER')
sc("""Here is the payback twist. If a hybrid option costs a couple of thousand dollars extra and saves about five hundred dollars a year in fuel, as in our example, it could pay for itself in about four years at today's prices. A diesel option that costs much more and saves nothing on fuel at today's prices may never pay back on fuel alone. That is why the price gap matters so much.""",
   'money calculator truck', 'PAYBACK: HYBRID ~4 YEARS (EXAMPLE)')
sc("""And there is a tax angle. According to Fox reporting from January twenty twenty-six, a new federal deduction lets eligible buyers deduct up to ten thousand dollars a year in auto loan interest on new vehicles with final assembly in the United States, bought for personal use. Where your truck is assembled can change your real cost. Check with a tax professional.""",
   'pickup truck assembly plant', 'US-ASSEMBLED: INTEREST DEDUCTION')
sc("""Now maintenance. Gas engines are generally the simplest. Modern diesels have extra emissions equipment, such as particulate filters and exhaust fluid systems, which can be expensive to repair when they fail. Hybrids add a battery and electric motor, but they often reduce brake wear, because regenerative braking does part of the work.""",
   'diesel engine repair', 'MAINTENANCE: GAS IS SIMPLEST')
sc("""And repairs are getting more expensive for everyone. According to Insurify, auto maintenance and repair costs have risen about forty-five percent in the past five years. AAA put maintenance, repairs and tires at eleven point seven cents per mile across all vehicles in twenty twenty-six. A complex engine can cost more when something goes wrong.""",
   'mechanic shop', 'REPAIRS: +45% IN 5 YEARS')
sc("""Here is a diesel warning. Some owners remove emissions equipment to avoid repairs, which is called a delete. In January twenty twenty-six, the Justice Department said it would stop criminal prosecution of diesel deletes, according to Fleet Maintenance. But tampering is still a Clean Air Act violation, with civil penalties listed at forty-five thousand, two hundred sixty-eight dollars per engine.""",
   'diesel truck exhaust', 'DELETES: STILL ILLEGAL')
sc("""And hybrid batteries? Many hybrid owners worry about replacement cost. Manufacturers usually cover hybrid batteries with their own long warranty, separate from the basic warranty. Check the battery warranty on the exact truck you are considering, because coverage varies by manufacturer and state.""",
   'hybrid battery', 'HYBRID BATTERY: CHECK THE WARRANTY')
sc("""Now resale value. Diesel trucks have traditionally held their value very well, especially heavy-duty trucks used for towing. But here is the twist: when fuel prices change this fast, used buyers change their minds too. A diesel that was easy to sell when diesel was cheap may be harder to sell when diesel costs two dollars more than gas.""",
   'used diesel trucks lot', 'RESALE: THE MARKET CAN SHIFT')
sc("""Hybrids may benefit from the same shift. When fuel is expensive, used buyers look for efficient trucks. The Ford Maverick is a sign of that demand. According to Ford, the Maverick sold one hundred fifty-five thousand and fifty-one units in twenty twenty-five, and eighty-one thousand and thirty-four of them were hybrids.""",
   'Ford Maverick hybrid', '81,034 MAVERICK HYBRIDS IN 2025')
sc("""And manufacturers are reading the same signal. According to Ford Authority, the twenty twenty-seven Ford Maverick X L becomes hybrid only, and the cheapest EcoBoost gas version moves up to the X L T all-wheel drive. The entry-level small truck in America is becoming a hybrid by default.""",
   'Ford Maverick', '2027 MAVERICK XL: HYBRID ONLY')
sc("""Here is the twist about gas engines. Even as hybrids grow, big gas engines are not going away. According to Carscoops, when Ram announced the return of the Hemi V eight in twenty twenty-five, it received more than ten thousand orders in less than twenty-four hours. Many buyers still want the sound and simplicity of a big gas engine, even when fuel is expensive.""",
   'Ram 1500 Hemi', 'HEMI RETURN: 10,000+ ORDERS IN 24H')
sc("""Let's look at how driving style changes the answer. Hybrids shine in stop-and-go traffic, where the electric motor can do more work and regenerative braking recovers energy. On a long, steady highway drive at high speed, the hybrid advantage usually shrinks. So a hybrid driven mostly on the interstate may save less than you expect.""",
   'highway traffic trucks', 'DRIVING STYLE CHANGES THE ANSWER')
sc("""Diesels are the opposite. They tend to be most efficient on long highway drives and under load, and less suited to many short trips. Modern diesel emissions systems can need longer drives at higher temperatures to clean their particulate filters. A diesel used only for short trips around town can run into extra maintenance.""",
   'diesel pickup highway', 'DIESELS PREFER LONG DRIVES')
sc("""Climate matters too. In very cold weather, diesel fuel can gel without the right winter blend or additives, and some diesel owners use block heaters. Hybrids can lose some efficiency in the cold as well, because the engine runs more to provide heat. Gas engines are generally the least sensitive to cold weather starts.""",
   'pickup truck snow', 'COLD WEATHER AFFECTS EVERY ENGINE')
sc("""And availability matters. Diesel is sold at most truck stops and many gas stations, but not every station has it, especially in some urban areas. Gas is available everywhere. A hybrid uses regular gas, so there is nothing new to find. For most drivers, that convenience is a small but real advantage.""",
   'gas station diesel pump', 'FUEL AVAILABILITY')
sc("""Here is a final cost twist: fuel price swings hit diesel owners harder because diesel moves goods across the country. When diesel rises, the cost of shipping almost everything rises with it, according to NPR's reporting on the strain for hauling everyday goods. So even owners of gas trucks feel the diesel shock in other prices.""",
   'semi truck highway', 'THE DIESEL SHOCK HITS EVERYONE')
sc("""And for businesses, the math is different again. A contractor who tows equipment every day may get a lot of value from a diesel's durability and towing ability, and fuel can be a business expense. A family that tows a camper twice a year will rarely earn back the extra cost of a diesel.""",
   'work truck trailer equipment', 'BUSINESS VS FAMILY MATH')
sc("""Finally, think about how long you will keep the truck. The longer you keep it, the more the fuel savings add up, and the more a reliable powertrain matters. If you trade trucks every three years, the purchase price and resale value matter more than fuel economy.""",
   'old pickup truck', 'HOW LONG WILL YOU KEEP IT?')
sc("""And remember that tires and weight matter for every engine. Big off-road tires, lift kits and heavy accessories can reduce fuel economy no matter what is under the hood. A hybrid with heavy mud tires may lose much of its advantage. Keep the truck close to stock if fuel savings are your goal.""",
   'pickup truck tires', 'TIRES AND WEIGHT MATTER')
sc("""So who should choose which engine? Let's go through the most common types of truck owners, starting with the commuter. If you mostly drive to work, run errands and rarely tow, the hybrid is usually the winner. It saves the most fuel in city and suburban driving, and AAA's study shows it was the cheapest pickup to own.""",
   'pickup truck commute city', 'COMMUTER: HYBRID')
sc("""Next, the highway driver who tows occasionally. A gas engine or a hybrid usually makes sense. The gas engine is cheaper to buy and simpler to maintain. The hybrid saves more fuel if you do a lot of mixed driving. A light-duty diesel is hard to justify at twenty twenty-six fuel prices unless you get very high highway mileage.""",
   'pickup truck highway trailer', 'OCCASIONAL TOWER: GAS OR HYBRID')
sc("""Then the heavy tower. If you pull a large camper, horse trailer or equipment every week, a heavy-duty diesel is still often the best tool. The fuel cost hurts more now, but the towing capability, engine braking and durability under load are hard to replace. For these owners, safety and capability come first.""",
   'Ford Super Duty towing', 'HEAVY TOWER: DIESEL')
sc("""And the budget buyer. If the lowest purchase price matters most, a base gas engine is usually the cheapest way into a truck. And in the small truck class, the Maverick hybrid shows that the cheapest choice and the most efficient choice can be the same truck.""",
   'Ford Maverick', 'BUDGET BUYER: BASE GAS OR SMALL HYBRID')
sc("""Here is one more twist: fuel prices can change again. President Trump said oil prices likely would not fall until after the November midterm elections, according to NPR. And S and P Global's Jim Burkhard said the market is adjusting to a new normal. Nobody knows where diesel will be in twenty twenty-seven. So choose a truck that makes sense across a range of prices, not just today's.""",
   'oil refinery', 'PRICES CAN CHANGE AGAIN')
sc("""A simple way to do that is to run your own math at three prices: today's price, last year's price and a higher price. If one engine wins in all three cases, it is a safe choice. If it only wins when fuel is cheap, you are taking a bet.""",
   'calculator budget', 'TEST 3 FUEL PRICES')
sc("""Let's summarize what the numbers say. In twenty twenty-six, the hybrid pickup was the cheapest to own in AAA's study. Diesel's fuel advantage disappeared for most drivers when diesel became two dollars more expensive than gas. Gas engines are still the cheapest to buy and the simplest to maintain. And heavy-duty diesels still rule heavy towing.""",
   'pickup trucks lineup', 'WHAT THE NUMBERS SAY')
# ---------- CLOSE ----------
sc("""So here is your engine checklist for twenty twenty-seven. One: divide the diesel price by the gas price to see how much better the diesel must be. Two: estimate fuel for your real miles. Three: compare the option prices and payback time. Four: think about towing needs honestly. And five: test your choice at different fuel prices.""",
   'checklist', 'YOUR ENGINE CHECKLIST')
sc("""We put a fuel cost worksheet and the full engine comparison into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe for the next video: the complete truck buyer's checklist for twenty twenty-seven. And tell us in the comments: diesel, gas or hybrid, what is in your truck? Thanks for watching.""",
   'pickup truck sunset', "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {'Six dollars and fifty-one cents.': 'Intro', 'According to NPR, the national': '1. The diesel shock', "Now let's look at the": '2. What AAA found', "Before we do, let's understand": '3. How each engine works', 'Now the math. We will': '4. The fuel math', 'Towing is where diesel fights': '5. Towing', 'Now purchase price. Diesel engines': '6. Purchase price and financing', 'Now maintenance. Gas engines are': '7. Maintenance', 'Now resale value. Diesel trucks': '8. Resale', "Let's look at how driving": 'Driving style and climate', 'So who should choose which': '9. Which engine for you?', 'Here is one more twist:': '10. What happens next', "Let's summarize what the numbers": 'The verdict', 'So here is your engine': 'Your checklist for 2027'}
CUTS = {0: 8, 1: 8, 2: 5}
for idx, sc_ in enumerate(S):
    sc_["cuts"] = CUTS.get(idx, 3)
    for k, v in CH.items():
        if sc_["text"].startswith(k): sc_["chapter"] = v
json.dump({"id": 'video58', "length_scale": 1.45,
  "title": 'Diesel vs Gas vs Hybrid Truck in 2026: The $6.51 Diesel Shock Changed the Math', "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.45/212,1), "min")
