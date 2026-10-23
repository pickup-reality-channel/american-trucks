import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In October twenty twenty-six, a Lamborghini Revuelto test car left the press fleet with a window sticker of eight hundred six thousand five hundred twenty-one dollars. The base price was about six hundred sixty-five thousand. The rest was options, delivery, and a tax most people do not expect on a plug-in hybrid. So what does a Revuelto really cost, from the order form to the day you sell it?""",
   "Lamborghini Revuelto", "THE REAL COST OF A REVUELTO")
sc("""Today we go line by line. The base price and how it climbed, the options that cost more than a normal car, the taxes, the insurance, the fuel, the service, and the used market, where something unusual is happening. Then we add it all up, using only published numbers.""",
   "Lamborghini Revuelto rear", "LINE BY LINE")
sc("""Every figure in this video has a source in the description. Some come from window stickers, some from price guides, some from insurers, and when a number is our own simple example, we will say so. With a car like this, the details are where the money hides.""",
   "Lamborghini Revuelto orange", "EVERY NUMBER IS SOURCED")
sc("""And here is the first twist. The price of a Revuelto went up while it was already sold out. Let's start at the beginning.""",
   "Lamborghini Revuelto front", "THE PRICE KEPT CLIMBING")

# ---------- 1. THE BASE PRICE ----------
ch("The base price")
sc("""When the Revuelto was revealed in March twenty twenty-three, Lamborghini had not announced American pricing. Motor Authority reported that in other markets it started at about five hundred thousand euros, roughly five hundred forty-nine thousand dollars at the time. By July twenty twenty-three, before a single car was delivered, the production for the next two years was already allocated.""",
   "Lamborghini Revuelto reveal", "ABOUT €500,000 TO START")
sc("""In the United Kingdom, Supercars dot net reported a base price of four hundred fifty thousand pounds in twenty twenty-three, about five hundred seventy-five thousand dollars at the time. And it showed how fast that number grows. One customer's configured car came to about five hundred fifty thousand pounds, and another dealer's example reached about five hundred ninety thousand pounds.""",
   "Lamborghini Revuelto UK", "£450,000 BECOMES £590,000")
sc("""In the United States, the base price kept rising. Kelley Blue Book lists a starting sticker of about six hundred seventy-three thousand dollars for the twenty twenty-six Revuelto. Jalopnik's twenty twenty-six test car had a base price of six hundred sixty-four thousand seven hundred ninety-nine dollars. Either way, the entry ticket in America is well above six hundred and fifty thousand dollars.""",
   "Lamborghini Revuelto USA", "~$665,000 TO $673,000 BASE")
sc("""Here is the twist. Rising prices did not slow demand. Lamborghini delivered a record ten thousand six hundred eighty-seven cars in twenty twenty-four, according to duPont Registry, and Wikipedia lists one thousand four hundred six Revueltos built that year. When a car is sold out, the maker sets the price, not the buyer.""",
   "Lamborghini factory Sant'Agata", "SOLD OUT, SO PRICES ROSE")

# ---------- 1b. WHAT THE MONEY BUYS ----------
ch("What the money buys")
sc("""Before we count the costs, let's be clear about what the money buys. A six point five liter naturally aspirated V12 with about eight hundred fourteen horsepower, three electric motors, and a total of one thousand and one horsepower. Zero to one hundred kilometers per hour in two point five seconds, and a top speed of about two hundred seventeen miles per hour, according to Wikipedia.""",
   "Lamborghini Revuelto V12", "WHAT $665,000 BUYS")
sc("""It also buys a car that experts rate highly. In Top Gear's twenty twenty-five Performance Car of the Year, the Revuelto beat the Ferrari twelve Cilindri and the Aston Martin Vanquish on track, and the writer said its chassis can keep pace with its engine. So the price is not only for the badge. It is for one of the best-reviewed V12 cars on sale.""",
   "Lamborghini Revuelto track", "TOP GEAR'S TRACK WINNER")
sc("""And it buys rarity, at least for now. A car that was sold out for two years before deliveries, built largely by hand in Sant'Agata Bolognese. Keep that in mind, because rarity is the reason some of the numbers later in this video look so strange.""",
   "Lamborghini Sant'Agata Bolognese", "BUILT BY HAND IN SANT'AGATA")
sc("""Now, line by line, here is what that ticket really costs.""",
   "Lamborghini Revuelto badge", "LINE BY LINE")

# ---------- 2. OPTIONS ----------
ch("Options")
sc("""Now options, where Lamborghini makes a lot of its money. Jalopnik published the full option list of its twenty twenty-six test car, painted in Viola thirtieth. Total options came to one hundred thirty-three thousand two hundred twenty-seven dollars. That is more than many new Porsches cost.""",
   "Lamborghini Revuelto purple", "$133,227 IN OPTIONS")
sc("""The biggest items were two carbon fiber packages. A lower exterior carbon pack, with the front splitter, side skirts, rear diffuser, and bumper fins, cost twenty-four thousand six hundred twenty-three dollars. An upper exterior carbon pack, with the windshield surround, mirrors, door handles, side intakes, and engine cover, cost twenty-five thousand nine hundred seventy-eight.""",
   "Lamborghini Revuelto carbon fiber", "TWO CARBON PACKS: $50,601")
sc("""Together, those two packs cost fifty thousand six hundred one dollars. Jalopnik pointed out that this is more than the average transaction price of a new car in America, which Kelley Blue Book put at fifty thousand five hundred sixty-two dollars in September twenty twenty-six. The carbon trim alone costs more than the car most Americans drive.""",
   "Lamborghini Revuelto carbon detail", "MORE THAN AN AVERAGE NEW CAR")
sc("""The rest of the list is a lesson in how small things add up. The paint was fourteen thousand three hundred thirty-one dollars. Silver stripes on the diffuser were four thousand fifty-two. Gray stitching was six thousand ninety-two. Sport seats were eight thousand three hundred eighty-seven. The Sonus faber audio system was six thousand six hundred twenty-eight.""",
   "Lamborghini Revuelto interior", "PAINT: $14,331")
sc("""Even features most cars include were options. The passenger display was four thousand fifty-two dollars. Apple CarPlay and Android Auto were three thousand seven hundred seventeen dollars. A parking pack was three thousand five hundred ninety-six. And an integrated garage door opener was six hundred seventy-one dollars. Black brake calipers were one thousand nine hundred fifty-nine.""",
   "Lamborghini Revuelto screen", "CARPLAY: $3,717")
sc("""Here is the twist. Those are the standard options. Lamborghini also offers Ad Personam, its personalization program, and Supercars dot net reported that Ad Personam options can cost one hundred thousand pounds or more. A unique paint color or a custom interior can push a Revuelto toward a million dollars.""",
   "Lamborghini Ad Personam", "AD PERSONAM: £100,000+")

sc("""At the very top of the market are the one-off cars. Lamborghini's Ad Personam department has built Revuelto Opera Unica cars with hand-painted liveries and custom interiors, including one inspired by the Taurus constellation and one inspired by Sardinia, according to Wikipedia. Those cars have no public price, and that is part of the point. When a car is unique, the price is whatever the buyer and Lamborghini agree on.""",
   "Lamborghini Revuelto Opera Unica", "ONE-OFFS HAVE NO PRICE TAG")
# ---------- 3. TAXES AND FEES ----------
ch("Taxes and fees")
sc("""Then come the fees. Jalopnik's sticker included a destination charge of three thousand nine hundred ninety-five dollars, which is the cost of delivering the car to the dealer. And it included a gas guzzler tax of four thousand five hundred dollars.""",
   "Lamborghini Revuelto delivery", "$3,995 DESTINATION")
sc("""The gas guzzler tax is a federal tax on cars with low fuel economy. And here is the twist. The Revuelto is a plug-in hybrid, but it still pays it. Kelley Blue Book lists its fuel economy at ten miles per gallon in the city, seventeen on the highway, and twelve combined. The small battery is for performance, not for saving fuel.""",
   "Lamborghini Revuelto exhaust", "A HYBRID THAT PAYS A GUZZLER TAX")
sc("""After that, there is sales tax, which depends on the state. As a simple example of our own, a seven percent sales tax on an eight hundred thousand dollar car would be fifty-six thousand dollars. That is another new pickup truck, just in tax. Registration fees in some states are also based on the value of the car.""",
   "Lamborghini Revuelto dealer", "EXAMPLE: $56,000 IN SALES TAX")
sc("""So before the car turns a wheel, the real price of a well-optioned Revuelto in America can be well above eight hundred thousand dollars, and close to nine hundred thousand with tax in many states. That is the true starting line for ownership.""",
   "Lamborghini Revuelto showroom", "CLOSE TO $900,000 ON THE ROAD")

# ---------- 4. INSURANCE ----------
ch("Insurance")
sc("""Now insurance. MoneyGeek's August twenty twenty-six analysis estimated full coverage for a Revuelto at about five hundred thirty-nine dollars a month, for a forty-year-old driver with a clean record, good credit, and twelve thousand miles a year. Over twelve months, that is about six thousand four hundred sixty-eight dollars, which is our multiplication.""",
   "Lamborghini Revuelto road", "ABOUT $539 A MONTH")
sc("""That sounds surprisingly low for an eight hundred thousand dollar car. And here is the twist. MoneyGeek's same methodology produced a Bugatti Chiron estimate of about three thousand fifty-six dollars a month. These are model-based estimates from standard insurers, and MoneyGeek itself notes that exotic specialty insurers may quote very differently.""",
   "Lamborghini Revuelto garage", "AN ESTIMATE, NOT A QUOTE")
sc("""In real life, insurance for a car like this depends on where it lives, how it is stored, how much it is driven, and the owner's history. Many owners use collector or exotic policies with agreed values and mileage limits. The honest answer is that a Revuelto can cost a few thousand dollars a year to insure, or much more.""",
   "Lamborghini Revuelto night", "IT DEPENDS ON THE OWNER")
sc("""And the Revuelto has one insurance risk that most cars do not have. Its doors. In twenty twenty-five, Lamborghini recalled twenty-seven United States cars because some pins on the door gas springs were installed incorrectly. A door could drop with force, or become hard to open from inside. Dealers fixed it free. But expensive, complex parts are exactly what makes repairs costly after an accident.""",
   "Lamborghini Revuelto scissor doors", "COMPLEX PARTS, COSTLY REPAIRS")

# ---------- 5. FUEL ----------
ch("Fuel")
sc("""Fuel is the easy part to calculate. Kelley Blue Book lists twelve miles per gallon combined and a twenty-two point five gallon tank, on premium fuel. As our own example, if premium costs five dollars a gallon, one full tank costs about one hundred twelve dollars and fifty cents, and takes you roughly two hundred seventy miles in mixed driving.""",
   "Lamborghini Revuelto fuel", "ONE TANK: ~$112")
sc("""If an owner drives three thousand miles a year at twelve miles per gallon, that is two hundred fifty gallons, or about one thousand two hundred fifty dollars at five dollars a gallon. Again, that is our example. Compared with the price of the car, fuel is close to a rounding error.""",
   "Lamborghini Revuelto highway", "EXAMPLE: ~$1,250 A YEAR")
sc("""And the battery helps a little. Kelley Blue Book lists a charge time of about two hours on a two hundred forty volt outlet, and Wikipedia lists about ten kilometers, or six miles, of electric range on the European test. For a short drive in the city, an owner can use the Citta mode and burn no fuel at all.""",
   "Lamborghini Revuelto charging", "6 MILES ON ELECTRIC")

# ---------- 6. SERVICE ----------
ch("Service")
sc("""Now service, and this is where Lamborghini is less open than you might expect. Kelley Blue Book lists a warranty of three years with unlimited miles for both basic and powertrain coverage. But Lamborghini does not publish a public price list for Revuelto servicing in the sources we could find.""",
   "Lamborghini service center", "3-YEAR UNLIMITED-MILE WARRANTY")
sc("""Even dealers that advertise fixed-price servicing do not always show the numbers. H R Owen in the United Kingdom, one of the biggest Lamborghini dealers, lists its fixed-price services for the Huracan and Aventador as price on application, and does not list the Revuelto at all. You have to ask.""",
   "Lamborghini dealership", "PRICE ON APPLICATION")
sc("""Some websites publish estimates for Revuelto servicing, but the ones we found gave no sources or methods, so we are not quoting them as facts. What we can say is that a Revuelto combines a V12, three electric motors, a high-voltage battery, carbon-ceramic brakes, and active aerodynamics. Each one needs specialist tools and training.""",
   "Lamborghini Revuelto engine bay", "NO RELIABLE PUBLIC PRICES")
sc("""Here is the twist. The hybrid system may actually help with some wear. The front motors recover energy when slowing down, which can take some load off the brakes. And the new dual-clutch gearbox replaces the Aventador's single-clutch robotized unit, which reviewers often criticized. But the battery adds a component that the Aventador never had.""",
   "Lamborghini Revuelto brakes", "HYBRID HELPS, AND ADDS")
sc("""The brakes alone show the scale. Wikipedia lists carbon-ceramic discs of four hundred ten millimeters at the front with ten-piston calipers, and three hundred ninety at the rear. Carbon-ceramic brakes last a long time with normal use, but when they need replacing, they are among the most expensive parts on any car.""",
   "Lamborghini Revuelto carbon ceramic brakes", "10-PISTON CALIPERS")

# ---------- 7. RESALE ----------
ch("Resale")
sc("""Now the part where the Revuelto surprises people. Most cars lose a big part of their value in the first two years. In October twenty twenty-six, autoevolution looked at a twenty twenty-four Revuelto with about six thousand miles, offered for six hundred twenty-nine thousand nine hundred eighty dollars.""",
   "Lamborghini Revuelto blue", "2 YEARS OLD: $629,980")
sc("""The same article said used Revueltos start around six hundred thousand dollars and can reach almost nine hundred thousand, depending on mileage, condition, and options. For early cars, that is not far from their original sticker. In other words, a buyer who got an early allocation has often lost little, if any, value on paper.""",
   "Lamborghini Revuelto used", "USED: $600K TO $900K")
sc("""Why? Partly because the car was sold out for years, so people who could not get an allocation paid a premium to skip the line. Motor Authority reported back in twenty twenty-three that the only alternatives were waiting or paying hefty markups on the used market. Scarcity protects value.""",
   "Lamborghini Revuelto line", "SCARCITY PROTECTS VALUE")
sc("""But here is the twist. A new, faster version now exists. In August twenty twenty-six, Lamborghini revealed the Revuelto S V, with about one thousand fifty-one horsepower, eighty percent more downforce, and a Hockenheim lap record for production cars, according to Auto123. Motor1 reported a United States order sheet price of seven hundred forty-one thousand one hundred seventy-two dollars before options.""",
   "Lamborghini Revuelto SV", "THE SV: $741,172")
sc("""When a faster version arrives, the regular car can lose some of its shine on the used market. On the other hand, the S V is limited to one thousand nine hundred sixty-three cars, mostly for existing customers. That could keep demand for regular Revueltos strong among buyers who could never get an S V. Nobody can promise which way it goes.""",
   "Lamborghini Revuelto SV rear", "NOBODY CAN PROMISE")

# ---------- 7b. PAYING FOR IT ----------
ch("Paying for it")
sc("""Now a question most videos skip. How do people actually pay for a car like this? Many buyers at this level pay cash. But some finance, or lease, to keep their money invested elsewhere. Let's do a clearly simple example of our own, using round numbers, to show what financing a Revuelto would look like.""",
   "Lamborghini Revuelto dealer office", "HOW DO PEOPLE PAY?")
sc("""Take a car at about eight hundred sixty thousand dollars on the road. Put twenty percent down, which is one hundred seventy-two thousand dollars. Finance the remaining six hundred eighty-eight thousand over seventy-two months at an example rate of seven percent. The monthly payment comes out to about eleven thousand seven hundred thirty dollars.""",
   "Lamborghini Revuelto calculator", "EXAMPLE: $11,730 A MONTH")
sc("""Over six years, the interest alone in that example adds up to about one hundred fifty-six thousand five hundred dollars. That is more than the total cost of the options on Jalopnik's test car. So for a financed buyer, the loan can cost more than the carbon fiber, the paint, and the audio system combined.""",
   "Lamborghini Revuelto interior detail", "INTEREST: ~$156,500")
sc("""And for cash buyers, there is a hidden cost too. Money in a car is money not earning anything elsewhere. As another simple example, if eight hundred sixty thousand dollars could earn four percent a year in a savings product, that would be about thirty-four thousand four hundred dollars a year. Economists call that an opportunity cost.""",
   "Lamborghini Revuelto garage", "EXAMPLE: $34,400 A YEAR NOT EARNED")
sc("""Here is the twist. With a car that holds its value well, like many early Revueltos, the opportunity cost can be the biggest yearly cost of all, bigger than insurance, fuel, and service together. The car may not lose much value, but the money inside it is not growing.""",
   "Lamborghini Revuelto front", "THE BIGGEST YEARLY COST?")

# ---------- 7c. THE AVENTADOR LESSON ----------
ch("The Aventador lesson")
sc("""To guess the Revuelto's future, look at the car it replaced. The Aventador was built from twenty eleven to twenty twenty-two, and reports at the end of its run put production at about eleven thousand four hundred sixty-five cars. That is a lot of V12 Lamborghinis, and it meant that used Aventadors became much easier to find than new ones were to order.""",
   "Lamborghini Aventador", "11,465 AVENTADORS")
sc("""The Revuelto is built in much smaller numbers per year. Wikipedia lists one thousand four hundred six in twenty twenty-four. If production stays at a similar pace over a long life, the total could still be large. And the larger the total, the more the used market behaves like a normal luxury car market over time.""",
   "Lamborghini Revuelto production", "HOW MANY WILL BE BUILT?")
sc("""The lesson is simple. Short-term values are protected by waiting lists. Long-term values depend on how many cars are built and how they are remembered. The Revuelto is the first hybrid V12 Lamborghini, which may help it be remembered. But no source can tell you what it will be worth in ten years.""",
   "Lamborghini Revuelto rear view", "FIRST HYBRID V12: A COLLECTIBLE?")

# ---------- 8. THE TOTAL ----------
ch("Adding it up")
sc("""So let's add it up for one example car, using the numbers in this video. Jalopnik's test car came to eight hundred six thousand five hundred twenty-one dollars, including options, destination, and the gas guzzler tax. Add an example seven percent sales tax, and the car is around eight hundred sixty thousand dollars on the road.""",
   "Lamborghini Revuelto front view", "~$860,000 ON THE ROAD")
sc("""Add insurance at MoneyGeek's estimate of about six thousand five hundred dollars a year, fuel of around one thousand two hundred fifty dollars a year in our example, and service at whatever the dealer quotes. Over three years, the running costs we can document are in the tens of thousands of dollars, small next to the price of the car.""",
   "Lamborghini Revuelto road trip", "RUNNING COSTS: TENS OF THOUSANDS")
sc("""And then the biggest number, depreciation, may be smaller than for a normal luxury car. If a two-year-old car can sell for around six hundred thirty thousand dollars, the loss compared with a base price in the mid six hundreds could be modest. But options rarely hold their value. Those carbon packs and that special paint are worth far less to the next buyer.""",
   "Lamborghini Revuelto parked", "OPTIONS DON'T HOLD VALUE")
sc("""So the real cost of a Revuelto is not mainly fuel or insurance. It is the options you choose and the timing of when you buy and sell. An early buyer with a simple spec can lose very little. A late buyer with a heavy spec who sells after the S V arrives could lose a lot.""",
   "Lamborghini Revuelto color", "TIMING IS THE REAL COST")
sc("""And then there is the Ferrari alternative. Kelley Blue Book lists the Ferrari twelve Cilindri from four hundred seventy-two thousand dollars, about two hundred thousand less than a Revuelto. We compare the two in detail in another video of this series.""",
   "Ferrari 12Cilindri", "THE FERRARI: ~$200,000 LESS")
sc("""Tell us in the comments: would you spend fifty thousand dollars on carbon fiber, or put that money into a whole second car? And watch the rest of this Revuelto series, two secrets hidden inside it, the Ferrari comparison, and the story of why Lamborghini built it this way.""",
   "Lamborghini Revuelto carbon", "CARBON OR A SECOND CAR?")
sc("""If your next purchase is a little more down to earth, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more honest numbers about the cars and trucks people really talk about.""",
   "Lamborghini Revuelto sunset", "SUBSCRIBE: PICKUP REALITY")

save("video67", "The Real Cost of a Lamborghini Revuelto (Options, Taxes, Insurance)", [
    "Jalopnik, Revuelto test car options and sticker (Oct 2026): https://www.jalopnik.com/2288310/lamborghini-revuelto-optional-carbon-fiber-costs-more-than-average-new-car/",
    "Kelley Blue Book, Lamborghini Revuelto (price, mpg, warranty, charging): https://www.kbb.com/lamborghini/revuelto/",
    "Motor Authority, Revuelto sold out for 2 years (July 2023): https://www.motorauthority.com/news/1140333_lamborghini-revuelto-already-sold-out-for-next-2-years",
    "Supercars.net, configuring a Revuelto gets expensive (2023): https://www.supercars.net/blog/configuring-a-lamborghini-revuelto-gets-expensive-very-quickly/",
    "duPont Registry, Lamborghini 2024 deliveries: https://news.dupontregistry.com/blogs/lamborghini-news/lamborghini-celebrates-a-record-breaking-year-with-10687-new-car-deliveries",
    "Wikipedia, Lamborghini Revuelto: https://en.wikipedia.org/wiki/Lamborghini_Revuelto",
    "MoneyGeek, Lamborghini insurance costs (Aug 2026): https://www.moneygeek.com/insurance/auto/lamborghini-car-insurance/",
    "MoneyGeek, Bugatti Chiron insurance (Apr 2026): https://www.moneygeek.com/insurance/auto/bugatti-chiron-insurance/",
    "AutoGuide, Revuelto door recall (July 2025): https://www.autoguide.com/auto/manufacturers/lamborghini/why-these-lambo-doors-could-fall-on-your-head-or-hold-you-hostage-44623369",
    "HR Owen, Lamborghini fixed price servicing: https://hrowen.co.uk/lamborghini/aftersales/servicing/fixed-price-servicing",
    "autoevolution, used Revuelto values (Oct 2026): https://www.autoevolution.com/news/how-much-is-a-2024-lamborghini-revuelto-worth-today-after-6000-miles-276767.html",
    "Auto123, Revuelto SV debut (Aug 2026): https://www.auto123.com/en/news/lamborghini-revuelto-sv-debut-monterey/74145/",
    "Motor1, Revuelto SV US price: https://www.motor1.com/news/805408/lamborghini-revuelto-sv-price-options/",
    "Kelley Blue Book, Ferrari 12Cilindri: https://www.kbb.com/ferrari/12cilindri/",
], "C")
