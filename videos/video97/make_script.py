import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Lamborghini Urus that you can buy is not the car Lamborghini showed in twenty twelve. The concept had a ten-cylinder engine borrowed from the Gallardo. The production car has a twin-turbo V eight that starts life as an Audi engine, built in a factory in Hungary, and sits on the same platform as a Porsche, a Bentley and a Volkswagen. There are two things about the Urus that you probably did not know, and both are in published sources.""",
   "Lamborghini Urus", "2 THINGS YOU DIDN'T KNOW ABOUT THE LAMBORGHINI URUS")
sc("""The first is about the car that was shown at the Beijing Auto Show, and what happened to it. The second is about everything hidden under the Urus's skin, and why Lamborghini's own boss says it is still a real Lamborghini. Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will tell you.""",
   "Lamborghini Urus concept", "THE CONCEPT · THE HIDDEN PARTS")

# ---------- 1. THE CAR ----------
ch("What the Urus is")
sc("""Wikipedia says the production Lamborghini Urus was unveiled on the fourth of December, twenty seventeen, at Sant'Agata Bolognese, with deliveries beginning in early twenty eighteen and a target of about three thousand five hundred units a year. It is the first Lamborghini SUV under Volkswagen ownership and the second in the brand's history.""",
   "Lamborghini Urus", "UNVEILED 4 DECEMBER 2017")
sc("""The name comes from the urus, the ancestor of modern domestic cattle, also called the aurochs, according to the same page. The Latin word urus meant wild ox from the time of the Gallic Wars. A bull is Lamborghini's symbol, so the SUV is named after the wild ancestor of the bull.""",
   "Aurochs", "THE NAME: THE WILD OX")
sc("""The base car's numbers are big. Wikipedia lists six hundred fifty metric horsepower at six thousand r p m, and eight hundred fifty newton-metres from two thousand two hundred fifty to four thousand five hundred. It reaches a hundred kilometres per hour in three point six seconds, and two hundred in twelve point eight. The top speed is given as three hundred five or three hundred six.""",
   "Lamborghini Urus", "650 PS · 850 NM · 0–100 IN 3.6 S")
sc("""The page notes that sources disagree on the top speed, three hundred five or three hundred six kilometres per hour, for the base car. That is a difference of one kilometre per hour, the sort of thing that comes from rounding. We report both. The same page gives a curb weight of under two thousand two hundred kilograms, thanks to carbon fibre reinforced polymer.""",
   "Lamborghini Urus top speed", "305 OR 306 KM/H: SOURCES DIFFER")

# ---------- 2. THING ONE ----------
ch("Thing one: the car that never got built")
sc("""Now the first thing. Wikipedia says the Urus concept was unveiled at the Beijing Auto Show on the twenty-third of April, twenty twelve. It had a five point two litre V ten shared with the Gallardo, rated at six hundred metric horsepower, and all-wheel drive. It was shown again at Pebble Beach that year. Filippo Perini is credited as its designer.""",
   "Lamborghini Urus concept", "2012: A 5.2 L V10 WITH 600 PS")
sc("""The production car looks different, and it is. Wikipedia says the production version changed substantially in exterior design and used a different powertrain from the concept. Mitja Borkert is credited with the production design. So the car in the showroom is not a copy of the car on the stand in Beijing. It is a new car with the same idea.""",
   "Lamborghini Urus production", "PRODUCTION DESIGN BY MITJA BORKERT")
sc("""The engine is the biggest change. The V ten of the concept was a natural continuation of the Gallardo. The production engine is a four litre twin-turbo V eight. By our own arithmetic, the production car has two fewer cylinders and one point two litres less displacement than the concept. Yet its output is fifty metric horsepower higher, six hundred fifty against six hundred, since a turbo makes up for size.""",
   "Lamborghini Urus V8", "V10 CONCEPT → TWIN-TURBO V8")
sc("""Look at the time that passed. The concept was shown in April two thousand twelve and the production car in December twenty seventeen. By our arithmetic, that is five years and eight months. Stephan Winkelmann described it in an interview with Yahoo Autos: we decided to do an SUV soon after that, but it took years to get there.""",
   "Lamborghini timeline", "5 YEARS 8 MONTHS FROM CONCEPT TO CAR")
sc("""Wikipedia notes that in two thousand eight, blogs expected the Urus name to be used for another car, one that became the Estoque concept. So the name existed before the car did. Lamborghini had trademarked Urus years before the concept in Beijing, which suggests the idea of a Lamborghini SUV was on the table for a long time.""",
   "Lamborghini Estoque", "THE NAME WAS TRADEMARKED YEARS EARLIER")
sc("""And there was an even older idea. Wikipedia says the Urus is the second Lamborghini SUV, after the LM002, built from nineteen eighty-six to nineteen ninety-three. Three hundred one were built, nicknamed the Rambo-Lambo. The LM002 had the Countach's V twelve at the front. So Lamborghini had a front-engine, V twelve SUV forty years before the Urus.""",
   "Lamborghini LM002", "THE FIRST ONE: LM002, 301 BUILT")
sc("""The Urus replaced the LM002 as its spiritual successor, according to the LM002 page. But the two are very different. The LM002 had a tubular steel frame and weighed two thousand seven hundred kilograms. The Urus uses a group platform and weighs under two thousand two hundred. By our arithmetic, that is at least eighteen percent lighter, despite being far more powerful.""",
   "Lamborghini Urus and LM002", "URUS ≥18% LIGHTER THAN LM002")

sc("""Compare the two eras of Lamborghini SUV. The LM002 Evoluzione of nineteen eighty-eight was tuned to six hundred metric horsepower, according to Wikipedia. The Urus makes six hundred fifty from a V eight with about a quarter less displacement than the old V twelve's five point two litres. By our arithmetic, that is eight percent more power from a four litre engine.""",
   "Lamborghini LM002 Evoluzione", "URUS 650 PS VS EVOLUZIONE 600 PS (+8%)")
sc("""Do the weight maths too. If the Urus weighs under two thousand two hundred kilograms, as Wikipedia says, then its power-to-weight ratio is at least about point three metric horsepower per kilogram, by our arithmetic. The LM002 weighed two thousand seven hundred, and the Evoluzione's six hundred horsepower gave about point two two. The Urus is at least thirty percent better.""",
   "Lamborghini Urus power to weight", "≥0.30 PS/KG VS 0.22 FOR THE EVOLUZIONE")
# ---------- 3. THING TWO ----------
ch("Thing two: what's hiding under the skin")
sc("""Now the second thing, and it is the one that surprises people most. Wikipedia says the Urus is built on the Volkswagen Group's M L B Evo platform. The page names the Audi Q seven, the Bentley Bentayga, the Porsche Cayenne and the Volkswagen Touareg as relatives. The infobox also lists the Audi Q eight and the third-generation Cayenne.""",
   "Volkswagen MLB Evo platform", "SAME PLATFORM AS CAYENNE, BENTAYGA, Q7")
sc("""The engine has relatives too. Wikipedia describes it as a reworked version of Audi's four litre V eight, assembled at a Volkswagen plant in Hungary. It says the engine is uprated by a hundred metric horsepower and eighty newton-metres over the one in the Porsche Cayenne Turbo. So the heart of the Urus began life in a car you can buy for much less.""",
   "Audi 4.0 V8 engine", "BUILT IN HUNGARY · +100 PS OVER THE CAYENNE TURBO")
sc("""Is that a problem? Winkelmann answered it directly in the Yahoo Autos article. It has a common platform, he said, but our engineers did a fantastic job creating a car which is a real Lamborghini. And, he added, nobody who drives an Urus ever doubts this. That is the opinion of the man who sells it, so weigh it as such.""",
   "Stephan Winkelmann", "\"A REAL LAMBORGHINI\"")
sc("""The sharing shows up in the recalls. Wikipedia says that in November twenty twenty, the N H T S A recalled two thousand, eight hundred thirty-one Urus from the twenty nineteen and twenty twenty model years, over a fuel-line quick-connect that was a fire risk. The page adds that Porsche identified the issue in twenty nineteen. A shared part can mean a shared problem.""",
   "Lamborghini Urus recall", "NOV 2020: FUEL-LINE RECALL, 2,831 CARS")
sc("""In May twenty twenty-four, a second recall covered two thousand, one hundred thirty-three Urus from the twenty twenty-three and twenty twenty-four model years, Performante and S, because hood latch striker rivets could let the hood detach at speeds above ninety-four miles per hour. That one is not described as a shared part. It is a reminder that every complex car needs fixes.""",
   "Lamborghini Urus hood", "MAY 2024: HOOD LATCH RECALL, 2,133 CARS")
sc("""Sharing also lets Lamborghini build in volume. Wikipedia says the company had to expand its Sant'Agata factory, which grew from eighty thousand to one hundred sixty thousand square metres. In twenty twenty-two it reported twenty thousand Urus built, its best-selling model in the shortest time. A hand-built platform could not have produced numbers like that.""",
   "Sant'Agata factory", "20,000 URUS BY 2022")

sc("""Think about what the shared platform means for drivers. The Urus's torque is delivered early: eight hundred fifty newton-metres from two thousand two hundred fifty r p m, according to Wikipedia. The page says that is flat until four thousand five hundred. By our arithmetic, that is a band of two thousand two hundred fifty r p m where the full torque is available. For a heavy SUV, that is what matters in everyday driving.""",
   "Lamborghini Urus engine", "FULL TORQUE FROM 2,250 TO 4,500 RPM")
sc("""Acceleration to two hundred kilometres per hour is a more honest measure of an engine than zero to a hundred. Wikipedia lists twelve point eight seconds for the base Urus. We will compare it with the Ferrari Purosangue in another video.""",
   "Lamborghini Urus acceleration", "0–200 KM/H IN 12.8 SECONDS")
# ---------- 4. THE VARIANTS ----------
ch("The variants")
sc("""The Urus did not stay the same. Wikipedia lists the Urus Performante, with six hundred sixty-six metric horsepower and the same torque, forty-seven kilograms lighter than the other variants, and a claimed zero to a hundred of three point three seconds. The top speed is given as three hundred six.""",
   "Lamborghini Urus Performante", "PERFORMANTE: 666 PS · 3.3 S · −47 KG")
sc("""Then the race car. The Urus S T-X, a one-make racing version, produces six hundred forty-one horsepower, the same as the street car. But Wikipedia says it is twenty-five percent lighter than the street Urus. By our arithmetic, a twenty-five percent weight cut on a car under two thousand two hundred kilograms would be a saving of more than five hundred kilograms.""",
   "Lamborghini Urus ST-X", "ST-X: SAME POWER, 25% LIGHTER")
sc("""Then the plug-in. The Urus S E has a four litre V eight making six hundred twenty horsepower, plus an electric motor making a hundred eighty-nine, with a combined seven hundred ninety-nine horsepower and nine hundred fifty newton-metres, according to Wikipedia. It reaches a hundred in three point four seconds, and its top speed is three hundred twelve.""",
   "Lamborghini Urus SE", "URUS SE: 799 HP COMBINED")
sc("""Wikipedia calls it the fastest production SUV in the world at launch. It weighs about three hundred kilograms more than the Urus S, because of its twenty-five point nine kilowatt-hour battery. CARFAX lists the two thousand twenty-six Urus S E at seven hundred eighty-nine horsepower, ten fewer than Wikipedia. The difference is probably a rounding or unit matter, but we flag it.""",
   "Lamborghini Urus SE", "799 HP OR 789 HP? SOURCES DIFFER")
sc("""CARFAX also says the S and Performante trims leave the lineup for twenty twenty-six, leaving the S E as the only Urus, with a starting price of two hundred seventy-six thousand, seven hundred forty-one dollars. It lists thirty-five miles of electric range, forty-eight miles per gallon equivalent, and twenty miles per gallon with the engine alone.""",
   "Lamborghini Urus SE 2026", "2026: ONLY THE SE · $276,741")
sc("""By our own arithmetic, the plug-in costs a lot more than the early cars. Motor1 said in twenty twenty-four that the Ferrari Purosangue, at three hundred ninety-three thousand, was roughly a hundred seventy thousand dollars more than a standard Urus, which would put that Urus near two hundred twenty-three thousand. The twenty twenty-six S E is about twenty-four percent above that.""",
   "Lamborghini Urus price", "$223K (2024) → $277K (2026): +24%")

sc("""CARFAX lists the Urus S E as a five-seater with sixteen cubic feet of cargo space behind the rear seats. It calls the cargo room so-so. That is a rare honest note about a car this expensive: it is an SUV with five seats, but not a very practical one. The sources suggest buyers are paying for performance and presence, not for space.""",
   "Lamborghini Urus interior", "5 SEATS · 16 CU FT OF CARGO")
sc("""A rental company's guide estimates the price. The Premier Auto Miami page says the two thousand twenty-five Urus starts at around two hundred forty-one thousand, eight hundred dollars, and that the S E starts at around two hundred sixty-two thousand, six hundred thirty. It says a fully optioned model can reach well over three hundred thousand. These are hedged estimates from a marketing page.""",
   "Lamborghini Urus price", "ESTIMATE: $241,800 BASE · $262,630 SE")
sc("""By our own arithmetic, the S E estimate is about nine percent above the base estimate. And a fully optioned car at three hundred thousand would be about twenty-four percent above the base. Those are rough figures, but they show the ladder: a base car, a plug-in hybrid, and a loaded plug-in, each a step up in price.""",
   "Lamborghini Urus options", "BASE → SE +9% → LOADED +24%")
sc("""The plug-in adds to the base car in clear steps. Wikipedia says the electric motor contributes a hundred eighty-nine horsepower, which is about thirty percent of the engine's six hundred twenty, by our arithmetic. The combined torque of nine hundred fifty newton-metres is twelve percent above the base car's eight hundred fifty. And zero to a hundred drops from three point six to three point four.""",
   "Lamborghini Urus SE hybrid", "SE: +30% POWER FROM THE MOTOR, +12% TORQUE")
sc("""Put the recalls in proportion, with a warning that production years and model years are not the same thing. Two thousand, eight hundred thirty-one cars recalled in twenty twenty compare with nine thousand, five hundred ninety-seven built in twenty nineteen and twenty twenty, about thirty percent. And two thousand, one hundred thirty-three in twenty twenty-four compare with twelve thousand, six hundred eighty-one built in twenty twenty-three and twenty twenty-four, about seventeen percent.""",
   "Lamborghini Urus recalls", "RECALLS: ~30% AND ~17% OF TWO MODEL YEARS (ROUGH)")
# ---------- 5. SALES ----------
ch("The surprise of its success")
sc("""The target was three thousand five hundred a year, according to Wikipedia. In the first full year, twenty nineteen, the Urus did far better. Carscoops reported four thousand, nine hundred sixty-two Urus delivered, a whopping sixty-one percent of total Lamborghini sales of eight thousand, two hundred five. By our arithmetic, that is about forty-two percent above the target.""",
   "Lamborghini Urus sales 2019", "2019: 4,962 URUS (+42% OVER TARGET)")
sc("""Wikipedia's production table shows the later years: five thousand, two hundred forty in twenty twenty-one, five thousand, seven hundred eighty-five in twenty twenty-two, six thousand in twenty twenty-three, six thousand, six hundred eighty-one in twenty twenty-four, and seven thousand, two hundred sixty-five in twenty twenty-five.""",
   "Lamborghini Urus production", "2021: 5,240 → 2025: 7,265")
sc("""By our own arithmetic, those nine years add up to forty-three thousand, two hundred fifty-four cars. The 10,000th Urus was announced in July twenty twenty. In twenty twenty-two, the Urus became Lamborghini's best-selling model in the shortest time, with twenty thousand units, according to Wikipedia. The target of three and a half thousand a year was passed in the first full year and never looked back.""",
   "Lamborghini Urus", "43,254 BUILT 2017–2025 (OUR SUM)")
sc("""The Yahoo Autos article says the Urus accounts for significantly more than half of the firm's annual sales, and calls it a huge profit driver for the Volkswagen Group. For a car that began as a concept with a V ten engine, and ended with a shared platform, it is an impressive result. Both of our two things are part of that success.""",
   "Lamborghini Urus", "\"A HUGE PROFIT DRIVER\"")

sc("""Let us go through the whole VinAssessment table, with its caveats. Median asking prices: one hundred sixty-eight thousand, six hundred ninety-six for twenty nineteen; one hundred seventy-nine thousand, nine hundred ninety-seven for twenty twenty; one hundred ninety-four thousand, nine hundred ninety for twenty twenty-one; two hundred twelve thousand, nine hundred ninety-nine for twenty twenty-two.""",
   "Lamborghini Urus asking prices", "2019: $168,696 → 2022: $212,999")
sc("""Then two hundred fifty-three thousand, one hundred twelve for twenty twenty-three; two hundred seventy-nine thousand, five hundred sixty-seven for twenty twenty-four; two hundred ninety-five thousand, three hundred sixty-six for twenty twenty-five; and three hundred thirty-seven thousand, seven hundred twenty-five for twenty twenty-six. The page notes the twenty twenty-five median is forty-two thousand, three hundred fifty-nine below the twenty twenty-six.""",
   "Lamborghini Urus asking prices", "2023: $253,112 → 2026: $337,725")
sc("""By our arithmetic, each year of age takes between about five and sixteen percent off the median asking price, with the largest step between twenty twenty-two and twenty twenty-three, about sixteen percent. But the newer years include the hybrid. So the real steps for a single model may be different. The honest summary is that older Urus are cheaper, in steps of five to sixteen percent.""",
   "Lamborghini Urus value", "5%–16% OFF PER YEAR OF AGE (ASKING)")
sc("""Where were the cars going? Carscoops reported that the United States was the biggest market in twenty nineteen, with two thousand, three hundred seventy-four Lamborghinis delivered of all models. That is about twenty-nine percent of the company's eight thousand, two hundred five, by our arithmetic. China, with Hong Kong and Macau, was next with seven hundred seventy.""",
   "Lamborghini US market", "US: 2,374 OF 8,205 DELIVERIES (29%)")
sc("""The first year of Urus production, twenty eighteen, shows how quickly the car ramped up. Wikipedia lists one hundred twenty-one built in twenty seventeen, then two thousand, five hundred sixty-five in twenty eighteen, then five thousand, two hundred thirty-three in twenty nineteen. By our arithmetic, production doubled in the second year, and more than doubled again after that.""",
   "Lamborghini Urus production line", "121 → 2,565 → 5,233")
sc("""The Yahoo article notes that Winkelmann has been at the helm of Lamborghini for fifteen of the past twenty years. So the man who decided to do an SUV, and who defended it as a real Lamborghini, is also the man who has run the company for most of its growth. The Urus is, in that sense, his car, as much as it is Sant'Agata's.""",
   "Stephan Winkelmann", "15 OF 20 YEARS AT THE HELM")
# ---------- 6. SECOND-HAND ----------
ch("What it's worth now")
sc("""A price tracker gives a view of the used market. VinAssessment, updated in October twenty twenty-six, lists median dealer asking prices by model year, from 848 listings. For twenty nineteen, the median asking price is one hundred sixty-eight thousand, six hundred ninety-six dollars. For twenty twenty-four, it is two hundred seventy-nine thousand, five hundred sixty-seven.""",
   "Lamborghini Urus used", "2019: $168,696 · 2024: $279,567 (ASKING)")
sc("""The page stresses that these are dealer asking prices, not sale prices. And the newer years include the plug-in S E, which costs more. So the table mixes models and should not be read as a depreciation curve. But it does show that a seven-year-old Urus is still being offered for over one hundred sixty thousand dollars.""",
   "Lamborghini Urus dealer", "ASKING PRICES, NOT SALE PRICES")

sc("""Winkelmann's own description of Lamborghini is in the Yahoo article. We see ourselves as brave, unexpected and authentic, he says. The article adds that in two thousand five, when he was appointed, the brand sold sixteen hundred cars. By our arithmetic, the Urus alone sold more than four times that number in twenty twenty-five, seven thousand, two hundred sixty-five against sixteen hundred.""",
   "Stephan Winkelmann", "1,600 CARS IN 2005 VS 7,265 URUS IN 2025")
# ---------- 7. CLOSING ----------
ch("Why it matters")
sc("""So here are the two things again. First, the Urus you can buy is not the Urus of twenty twelve: the V ten was replaced by a turbo V eight, and the design was changed substantially. Second, under its skin the Urus shares a platform with a Porsche, a Bentley, an Audi and a Volkswagen, and its engine starts as an Audi's.""",
   "Lamborghini Urus", "THE TWO THINGS, AGAIN")
sc("""Does that make it less of a Lamborghini? That is a question about taste. The sources say it is fast, light for its size, and a great commercial success. They say its boss believes it is a real Lamborghini. They also say that its platform is shared. The truth, we think, includes both statements.""",
   "Lamborghini Urus", "FAST, SHARED AND SUCCESSFUL")
sc("""Which of the two things surprised you more, the lost V ten or the shared platform? Tell us in the comments. In the other videos of this series, we compare the Urus with the Ferrari Purosangue, work out what it really costs to own one, and tell why Lamborghini bet everything on an SUV.""",
   "Lamborghini Urus", "WHICH SURPRISED YOU MORE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video97", "2 Things You Didn't Know About the Lamborghini Urus", [
    "Wikipedia, Lamborghini Urus: https://en.wikipedia.org/wiki/Lamborghini_Urus",
    "Wikipedia, Lamborghini LM002: https://en.wikipedia.org/wiki/Lamborghini_LM002",
    "Carscoops, Lamborghini sold nearly 5,000 Urus SUVs last year (January 2020): https://www.carscoops.com/2020/01/lamborghini-sales-soar-43-percent-in-2019-thanks-to-urus-suv/",
    "Yahoo Autos, We're not selling mobility: how Stephan Winkelmann transformed Lamborghini: https://autos.yahoo.com/people-and-culture/articles/were-not-selling-mobility-stephan-083648052.html",
    "CARFAX, 2026 Lamborghini Urus review, pricing and specs: https://www.carfax.com/Research-Lamborghini-Urus_w9540",
    "Motor1, 2024 Ferrari Purosangue is predictably expensive: https://www.motor1.com/news/652734/2024-ferrari-purosangue-suv-price/",
    "VinAssessment, Lamborghini Urus prices by year: https://vinassessment.com/prices/lamborghini/urus",
], "A")
