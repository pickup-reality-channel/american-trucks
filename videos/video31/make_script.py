import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""A Ram with seven hundred seventy-seven horsepower. A Chevy Silverado with two brand-new V8s. An electric Ford pickup for under thirty thousand dollars. And a twenty-five-thousand-dollar truck with manual windows and no touchscreen. Twenty twenty-seven is the biggest year for new pickups in a long time. And one of the most hyped trucks of all just got pushed back again.""",
   "Ram 1500 TRX", "2027: THE BIGGEST TRUCK YEAR IN YEARS")

# ---------- COLD OPEN ----------
sc("""Here is why this matters. The full-size truck is the most profitable vehicle many automakers sell, and when the two best-selling nameplates change at the same time, prices, engines and resale values shift across the whole market. For the twenty twenty-seven model year, General Motors has redesigned both the Chevrolet Silverado and the GMC Sierra. Ford is replacing its electric pickup strategy. And Ram is bringing back a name that disappeared in twenty eleven.""",
   "Chevrolet Silverado 2026", "SILVERADO + SIERRA REDESIGNED")
sc("""In this video, we go through every major new truck coming for twenty twenty-seven, what is actually confirmed, and what is still a rumor. Prices where they have been announced. Engines where they have been confirmed. And release dates, because some of these trucks are much further away than their makers first promised.""",
   "GMC Sierra 1500 2026", "CONFIRMED VS RUMOR")
sc("""Every fact here comes from manufacturer announcements and published reporting, listed in the description. When a spec has not been announced, we will say so. Let's start with the most important truck launch of the year.""",
   "Ford F-150 2025", "EVERY FACT IS SOURCED")

# ---------- 1. SILVERADO ----------
sc("""The next-generation twenty twenty-seven Chevrolet Silverado fifteen hundred made its global debut on June sixteenth, twenty twenty-six, according to Motor Illustrated. GM had confirmed in its investor materials earlier that year that Chevrolet and GMC would reveal the new Silverado and Sierra in twenty twenty-six. Production starts in the fall of twenty twenty-six.""",
   "Chevrolet Silverado 1500 2027", "SILVERADO DEBUT: JUNE 16, 2026")
sc("""The big news is under the hood. Two all-new V8s, a five point seven liter and a six point six liter, replace the old five point three and six point two. GM calls them sixth-generation Small Block V8s. And every engine now pairs with a ten-speed automatic, including the two point seven liter TurboMax four-cylinder, which used to come with an eight-speed.""",
   "Chevrolet small block V8 engine", "NEW 5.7L AND 6.6L V8s")
sc("""Here is the twist. In a market where rivals have been shrinking engines and adding turbos, GM went the other way. Its new V8s are actually larger in displacement than the ones they replace. The three point zero liter Duramax diesel inline-six also stays, and can even be ordered on the base Work Truck. As of the debut, horsepower and torque figures for the new V8s had not been announced, and there is no plug-in hybrid Silverado yet.""",
   "Chevrolet Silverado Duramax", "BIGGER V8s, NOT SMALLER")
sc("""Inside, a sixteen point three inch touchscreen and a twelve point two inch digital gauge cluster are standard on every trim. The lineup is simplified to seven trims: Work Truck, Custom, Custom Trail Boss, the trim simply called Silverado, Trail Boss, ZR2 and High Country. The LT, LTZ and RST names are gone. The ZR2 keeps thirty-five-inch tires, front and rear electronic lockers and Multimatic spool-valve dampers.""",
   "Chevrolet Silverado ZR2", "LT, LTZ, RST: GONE")
sc("""And GM is betting big on volume. According to reporting on its investor presentation, GM aims to build about two million full-size trucks and SUVs in twenty twenty-seven, as it expands U.S. capacity. When the biggest truck maker in America tells investors that number, it is telling you how much it is counting on these trucks.""",
   "Chevrolet Silverado factory", "GOAL: ~2 MILLION IN 2027")

# ---------- 2. SIERRA ----------
sc("""The twenty twenty-seven GMC Sierra fifteen hundred followed on June twenty-fifth, twenty twenty-six. GMC called it the most advanced, luxurious and powerful Sierra ever. It shares the new five point seven and six point six liter V8s, the TurboMax and the Duramax diesel, all with the ten-speed. GMC expects the first trucks at dealerships before the end of twenty twenty-six.""",
   "GMC Sierra 1500 Denali", "SIERRA REVEAL: JUNE 25, 2026")
sc("""And here is a number that tells you where trucks are going. The top Denali Ultimate has more than sixty inches of combined digital displays. A sixteen point three inch center screen, an eleven point five inch passenger screen with an articulating cover, a twelve point two inch driver display, a fifteen inch head-up display and a rear camera mirror. Super Cruise hands-free driving, with trailering capability, is standard on AT4, AT4X, Denali and Denali Ultimate.""",
   "GMC Sierra Denali interior", "60+ INCHES OF SCREENS")
sc("""In September twenty twenty-six, GMC released the numbers, as reported by AutoGuide. The standard two point seven liter TurboMax makes three hundred fifty horsepower and four hundred fifty-five pound-feet. The three point zero liter Duramax diesel makes three hundred five horsepower and four hundred ninety-five pound-feet. The new five point seven liter V8 makes four hundred two horsepower and four hundred twenty-eight pound-feet, with up to thirteen thousand, five hundred pounds of towing.""",
   "GMC Sierra 1500 towing trailer", "5.7L V8: 402 HP, 13,500 LB TOW")
sc("""And the flagship six point six liter V8 makes four hundred eighty-one horsepower and five hundred one pound-feet of torque. For comparison, the six point two it replaces made four hundred twenty horsepower. Both new V8s are pushrod engines with two valves per cylinder, aluminum blocks and heads, variable valve timing, and both port and direct fuel injection. A thirty-four-gallon fuel tank is available.""",
   "GMC Sierra Denali 2026", "6.6L V8: 481 HP")
sc("""Here is why that matters. AutoGuide noted that hundreds of thousands of GM's six point two liter engines were recalled over rotating assembly components that were out of specification. We covered that recall in our engine videos. So the new V8s are not only about more power. They are GM's chance to reset its reputation for V8 reliability, and the first owners will be the ones who find out whether it worked. Fuel economy figures had not been released yet.""",
   "Chevrolet 6.2L V8 engine", "A CHANCE TO RESET V8 TRUST")
sc("""The twist with the Sierra is what it means for theft and repair. Remember that heavy-duty crew cab Sierras already had the highest theft rate of any vehicle in the latest Highway Loss Data Institute study. More screens, cameras and sensors make a truck nicer to own, but every one of them is a part that can break or be stolen. GMC had not announced pricing at the reveal.""",
   "GMC Sierra AT4", "MORE TECH, MORE TO FIX")

# ---------- 3. RAM ----------
sc("""Ram's big twenty twenty-seven news is loud. The twenty twenty-seven Ram fifteen hundred Rumble Bee SRT uses a supercharged six point two liter HEMI V8, the Hellcat engine, with seven hundred seventy-seven horsepower and six hundred eighty pound-feet of torque, according to SlashGear. That is more power than the Ram TRX it follows.""",
   "Ram 1500 TRX", "RUMBLE BEE SRT: 777 HP")
sc("""SlashGear reports Ram's performance claims of zero to sixty in about three point four seconds, a quarter mile in eleven point six seconds, and a top speed of one hundred seventy miles per hour. It comes only as a quad cab with a short bed, with six-piston Brembo front brakes and twenty-two-inch wheels. Here is the twist. Just a few years after the industry said big V8s were on their way out, the most powerful half-ton truck Ram has ever announced is a supercharged V8.""",
   "Ram 1500 SRT", "0-60 IN ~3.4 SECONDS")
sc("""But Ram's most important new truck may be its smallest. In December twenty twenty-five, Ram CEO Tim Kuniskis confirmed the return of the Dakota name, according to Auto123. The midsize pickup will be built at the Belvidere Assembly Plant in Illinois, with production scheduled to start in twenty twenty-seven. The name was abandoned in twenty eleven.""",
   "Dodge Dakota", "THE DAKOTA IS BACK")
sc("""Belvidere has been idle since February twenty twenty-three, when it last built the Jeep Cherokee. According to The Drive, about fifteen hundred UAW workers would return when the truck goes into production. And the Dakota will be body-on-frame, like the Tacoma, Ranger and Colorado it will compete with.""",
   "Belvidere Assembly Plant", "BELVIDERE: IDLE SINCE 2023")
sc("""Here is the twist on the Dakota. A midsize truck is supposed to be the affordable option. But according to Auto123, Kuniskis hinted at a starting price around forty thousand dollars, compared with about thirty-five thousand for the Colorado, Ranger and Tacoma. And the same report refers to it as a twenty twenty-eight Ram Dakota at dealerships. So production may start in twenty twenty-seven, but the first trucks you can buy may wear a twenty twenty-eight badge.""",
   "Ram Dakota", "DAKOTA: ~$40,000?")

# ---------- 4. FORD ----------
sc("""Now Ford, and the biggest change of strategy on this list. Ford discontinued the F-150 Lightning in December twenty twenty-five, according to Electrek. It stayed on sale for a few months and then disappeared from Ford's website, which says the truck is no longer available in its current form. Ford CEO Jim Farley explained it bluntly to CNBC. The very high-end EVs, the fifty, seventy and eighty thousand dollar vehicles, just weren't selling.""",
   "Ford F-150 Lightning", "F-150 LIGHTNING: DISCONTINUED")
sc("""Its replacement is two very different trucks. The first is the Fathom, a midsize all-electric pickup. According to Electrek, it starts at twenty-eight thousand, three hundred fifty dollars for the standard-range model, plus a one thousand five hundred ninety-five dollar delivery fee, so just under thirty thousand. It goes on sale in early twenty twenty-seven, built at Ford's Louisville Assembly Plant in Kentucky.""",
   "Ford Louisville Assembly Plant", "FORD FATHOM: $28,350")
sc("""Ford announced the plan in August twenty twenty-five, with a five billion dollar investment, about two billion for Louisville and three billion for its battery plant in Marshall, Michigan, according to Equipment World. The truck uses lithium iron phosphate battery cells, and Ford says it will be the first automaker to make that type of prismatic cell in the United States. Ford also claimed it would have more passenger room than a Toyota RAV4, and a zero to sixty time of about four and a half seconds.""",
   "Ford BlueOval Battery Park Michigan", "$5 BILLION INVESTMENT")
sc("""How does Ford plan to make money at that price? With a new way of building. Ford says its new Universal EV Platform uses twenty percent fewer parts, twenty-five percent fewer fasteners, and forty percent fewer workstations than a typical vehicle, and the new production system is expected to speed assembly by forty percent. Farley said, quote, we tore up the moving assembly line concept and designed a better one.""",
   "Ford assembly line", "20% FEWER PARTS")
sc("""Here is the twist. Ford said the Fathom's price matches the inflation-adjusted price of the original Model T. A century later, Ford is pitching the same idea, a vehicle ordinary workers can afford. And it is doing it with a midsize electric pickup, not a full-size truck. Range and charging times were not part of the original announcement.""",
   "Ford Model T", "THE NEW MODEL T?")
sc("""The second truck is for the people who want an F-150. Ford is developing an extended-range electric F-150 with a gasoline generator on board. According to Electrek, Ford says it will offer more than seven hundred miles of total range. Farley described it as, quote, seven hundred miles on a tank of gas, and for ninety percent of the time, is all-electric. Ford has not given a final on-sale date or full specs.""",
   "Ford F-150 2024 Platinum", "F-150 EREV: 700+ MILES")
sc("""And for performance fans, Ford already added the Maverick Lobo SV three hundred T package for twenty twenty-six. It raises the two point zero liter EcoBoost from two hundred fifty to three hundred horsepower, and from two hundred seventy-seven to three hundred fifty pound-feet of torque, with a bigger turbo, an upgraded intercooler and a Borla exhaust, covered by a three-year, thirty-six-thousand-mile warranty, according to SlashGear.""",
   "Ford Maverick", "MAVERICK LOBO: 300 HP")

# ---------- 5. TOYOTA + HONDA ----------
sc("""Toyota's twenty twenty-seven update is smaller but real. The twenty twenty-seven Tundra TRD Pro gets adjustable Fox Q three S shocks tuned for the Tundra, red front tow hooks, the IsoDynamic seats first seen in the Tacoma TRD Pro, and a new color called Honeycomb, according to SlashGear. Toyota also mentioned a new TRD Performance package, but had not released details.""",
   "Toyota Tundra TRD Pro", "TUNDRA TRD PRO: FOX Q3S SHOCKS")
sc("""And here is a twist many shoppers missed. The Honda Ridgeline, Consumer Reports' top pick for midsize trucks according to SlashGear, is going on pause. Honda paused production until the next generation, which is expected to be hybridized and unveiled in twenty twenty-eight. So one of the best-rated midsize trucks on the market will be harder to find, just as new competitors arrive.""",
   "Honda Ridgeline", "RIDGELINE: PAUSED UNTIL NEXT GEN")

# ---------- 6. SLATE ----------
sc("""Now the strangest truck on this list. The Slate Truck, from a startup backed by Jeff Bezos, starts at twenty-four thousand, nine hundred fifty dollars, according to Electrive. SlashGear called it the most affordable new pickup in America. It is a two-seat electric pickup with a rear motor, a sixty-three kilowatt-hour usable LFP battery, and up to two hundred five miles of range.""",
   "electric pickup truck prototype", "SLATE TRUCK: $24,950")
sc("""And it is radically basic. The base truck has no touchscreen, no speakers, and manual windows. Owners add what they want later, and a kit can turn it into a five-seat SUV. It is built in Warsaw, Indiana. Slate raised six hundred fifty million dollars in a Series C round, bringing its total to about one point four billion, and reported about one hundred eighty thousand non-binding reservations.""",
   "Warsaw Indiana", "NO SCREEN. MANUAL WINDOWS.")
sc("""The numbers are modest but honest. According to Electrive, payload is about one thousand five hundred fifty pounds, charging peaks at one hundred twenty kilowatts on a NACS port, and a DC fast charge takes about thirty minutes. Slate offers a ten-year, one hundred ten thousand mile warranty on the battery and drivetrain. Towing is rated at up to two thousand pounds, according to SlashGear. It is a work tool, not a status symbol.""",
   "small electric pickup truck", "1,550 LB PAYLOAD, 10-YR WARRANTY")
sc("""Here is the twist. Slate originally advertised a price under twenty thousand dollars. That number included the seventy-five hundred dollar federal EV tax credit, which has since been abolished, according to Electrive. So the cheapest truck in America got about five thousand dollars more expensive before a single one was delivered. First deliveries were scheduled for the fourth quarter of twenty twenty-six.""",
   "electric truck charging", "UNDER $20K BECAME $24,950")

# ---------- 7. SCOUT ----------
sc("""And now the truck that got pushed back. Scout Motors, the American brand revived by Volkswagen, revealed the Terra pickup and the Traveler SUV with the goal of a twenty twenty-seven launch. But in March twenty twenty-six, Scout CEO Scott Keogh said he expects customers to receive vehicles sometime in twenty twenty-eight, according to Electrive.""",
   "Scout Terra", "SCOUT: NOW 2028")
sc("""The reason is a change of plan. Scout decided to launch the Traveler and Terra first as extended-range models, with a gas generator, instead of battery-electric only. And that is what buyers asked for. Of about one hundred sixty thousand reservations, about eighty-seven percent chose the range-extender version. Scout claims about three hundred fifty miles for the electric version and five hundred miles for the range extender.""",
   "Scout Traveler", "87% CHOSE THE RANGE EXTENDER")
sc("""Scout is also fighting a battle that has nothing to do with engineering. It plans to sell directly to customers instead of through traditional dealers. According to Reuters, as cited by Electrive, two U.S. dealers sued Volkswagen over that plan, and the suit could expand into a class action. Volkswagen declined to comment. Scout plans to build its first prototypes at its new plant in Blythewood, South Carolina, by the end of twenty twenty-six, and reservations cost one hundred dollars and are refundable.""",
   "Scout Traveler concept", "DEALERS SUE OVER DIRECT SALES")
sc("""Here is the biggest twist. According to the same report, forecasting firm AutoForecast Solutions said Traveler production had moved to September twenty twenty-eight, and Terra pickup production would not start until March twenty thirty. Scout said it had not spoken with the firm and had no new schedule updates. Either way, if you were waiting for a Scout pickup in twenty twenty-seven, the plan has changed. We look at Scout against the Big Three in our next video.""",
   "Scout Motors Blythewood", "TERRA PICKUP: 2030?")

# ---------- 8. WHAT IT MEANS ----------
sc("""So what do all these trucks tell us? First, the V8 is not dead. GM launched two new V8s, and Ram's most powerful new half-ton is a supercharged V8. Second, the electric truck is shrinking. Ford killed the full-size Lightning and replaced it with a midsize Fathom near thirty thousand dollars, and Slate is selling a basic EV for under twenty-five thousand.""",
   "Ford F-150 Raptor", "THE V8 IS NOT DEAD")
sc("""Third, the range extender is the new compromise. Ford's next F-150 and both Scouts lean on gas generators to deliver hundreds of miles of range. And fourth, everyone is chasing a cheaper truck. Ram's CEO has said the brand needs a more affordable smaller truck, Ford is pitching the Fathom as a modern Model T, and Slate removed the touchscreen to hit its price.""",
   "Ram 1500 2025", "RANGE EXTENDERS + CHEAPER TRUCKS")
sc("""For buyers, here is the practical part. A first model year of a redesigned truck often brings early recalls, as we covered in our recall videos. If you want a twenty twenty-seven Silverado or Sierra, consider waiting for the first months of production and checking the recall database before you sign. And if you want a current-generation truck, the arrival of the new ones can be a good moment to negotiate on the outgoing model.""",
   "Chevrolet Silverado dealership", "FIRST YEAR = WAIT AND CHECK")
sc("""And check what is confirmed. Many twenty twenty-seven prices, power figures and towing ratings had not been announced when these trucks were revealed. A truck you saw in a reveal video may cost more, arrive later, or change before it reaches a dealer, as Scout and Slate have already shown.""",
   "GMC Sierra 1500", "CHECK WHAT IS CONFIRMED")

# ---------- CLOSE ----------
sc("""So here is every major new truck for twenty twenty-seven. A redesigned Chevrolet Silverado and GMC Sierra with new five point seven and six point six liter V8s. A seven hundred seventy-seven horsepower Ram Rumble Bee SRT. The return of the Ram Dakota. Ford's Fathom electric pickup at twenty-eight thousand, three hundred fifty dollars, and an extended-range F-150 coming. An updated Tundra TRD Pro. And the twenty-four thousand, nine hundred fifty dollar Slate.""",
   "Chevrolet Silverado GMC Sierra", "EVERY NEW TRUCK FOR 2027")
sc("""And the final twist. The truck that may change the market most is not the most powerful one. It is whichever one finally brings a new pickup back near thirty thousand dollars, in a market where the average new vehicle costs far more. That is the battle to watch in twenty twenty-seven.""",
   "Ford Maverick 2025", "THE REAL BATTLE: PRICE")
sc("""We put the twenty twenty-seven truck calendar, and what to check before buying a first-year model, into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we put Scout Motors against the Big Three. And tell us in the comments, which twenty twenty-seven truck would you actually buy? Thanks for watching.""",
   "Ram 1500 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"A Ram with seven": "Intro", "The next-generation twenty twenty-seven Chevrolet": "2027 Chevrolet Silverado", "The twenty twenty-seven GMC Sierra": "2027 GMC Sierra",
      "Ram's big twenty twenty-seven": "Ram Rumble Bee SRT and Dakota", "Now Ford, and the biggest": "Ford Fathom and F-150 EREV",
      "Toyota's twenty twenty-seven": "Toyota and Honda", "Now the strangest truck": "The $24,950 Slate", "And now the truck that got pushed back": "Scout's delay",
      "So what do all these trucks": "What it means for buyers", "So here is every major": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video31", "length_scale": 1.48,
  "title": "Every New Truck Coming in 2027 (One Just Got Delayed Again)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words")
