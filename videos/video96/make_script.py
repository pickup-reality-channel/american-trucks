import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Dodge Viper was killed twice. The first time, in two thousand ten, American sales had fallen to three hundred ninety-two cars. The second time, in twenty seventeen, the maker said it was ending the car rather than redesign it for a new safety rule. In twenty twenty-six, the head of S R T explained that the rule would have put airbags right over the driver's ear. This is the story of why the Viper died, and why it died twice.""",
   "Dodge Viper", "WHY THE DODGE VIPER WAS KILLED (TWICE)")
sc("""Here is the twist. The popular explanation, that nobody wanted the car, is only part of the story. The sources point to a safety regulation that the Viper could not meet as built. And the second death came when the car was selling better than it had in years. We will show you the numbers, and tell you where sources disagree.""",
   "Dodge Viper ACR", "IT WASN'T JUST LOW SALES")
sc("""Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so. Let us start at the beginning, in a room at Chrysler.""",
   "Dodge Viper", "EVERY FACT IS SOURCED")

# ---------- 1. THE BIRTH ----------
ch("A modern Cobra")
sc("""Wikipedia says the idea began when Chrysler president Bob Lutz asked Tom Gale, at the Chrysler Design Center, to consider a modern Cobra. A clay model followed. The car was shown as a concept at the nineteen eighty-nine North American International Auto Show, and Metalcrafters built it in sheet metal.""",
   "Dodge Viper concept 1989", "1989 DETROIT: THE CONCEPT")
sc("""The reaction pushed it toward production. Wikipedia says chief engineer Roy Sjoberg was told to develop it, and that chairman Lee Iacocca delayed approval of the seventy million dollars needed until May nineteen ninety. Seventy million dollars is a small budget for a new car. It shows how unusual this project was.""",
   "Chrysler 1990", "$70 MILLION, APPROVED MAY 1990")
sc("""Sjoberg picked eighty-five engineers, and development began in March nineteen eighty-nine. The group was called Team Viper. Wikipedia says Lamborghini, which Chrysler then owned, cast a prototype aluminium block and helped design the V ten. So a Dodge sports car's heart came partly from an Italian supercar company.""",
   "Team Viper engineers", "85 ENGINEERS · LAMBORGHINI HELPED WITH THE V10")
sc("""Carroll Shelby, the man behind the original Cobra, drove a pre-production car as the Indianapolis five hundred pace vehicle in nineteen ninety-one. Wikipedia says it replaced the Japanese-built Dodge Stealth after complaints from the United Auto Workers. A pace car change, and a political one.""",
   "Carroll Shelby Viper pace car", "1991: SHELBY DRIVES THE PACE CAR")
sc("""Reviewers got the car in November nineteen ninety-one, and the first retail cars shipped in January nineteen ninety-two, as the R T ten roadster, priced at fifty-two thousand dollars. Wikipedia says it had no exterior door handles, no airbags, no traction control and no A B S, canvas roofs, and vinyl windows that zipped.""",
   "Dodge Viper RT/10 1992", "1992: $52,000 · NO ABS · NO AIRBAGS")
sc("""The engine was an eight litre V ten. Wikipedia lists four hundred horsepower and four hundred sixty-five pound-feet of torque. The car weighed one thousand four hundred ninety kilograms, and went from zero to a hundred kilometres per hour in four point two seconds. The page quotes a phrase for its early reputation: an intimidating car to drive.""",
   "Dodge Viper V10", "8.0 L V10 · 400 HP")

# ---------- 2. THE RISE ----------
ch("A car that grew and raced")
sc("""The Viper grew steadily. Wikipedia says a mid-nineteen ninety-six exhaust change raised output to four hundred fifteen horsepower, and that the GTS coupé of the same year had four hundred fifty. The GTS was the first Viper with airbags. By our arithmetic, that was four years after the first car, with no airbags at all.""",
   "Dodge Viper GTS", "1996: GTS, THE FIRST VIPER WITH AIRBAGS")
sc("""Racing gave the car a reputation. Wikipedia says the Viper won its class at Le Mans three years in a row, in nineteen ninety-eight, nineteen ninety-nine and two thousand. It won the twenty-four hours of Daytona overall in two thousand. And back-to-back Spa twenty-four hours in two thousand one and two thousand two.""",
   "Dodge Viper GTS-R Le Mans", "LE MANS CLASS WINS: 1998, 1999, 2000")
sc("""The page gives career totals for the racing Viper: four hundred forty-five races, forty-seven championships, one hundred sixty-two wins, two hundred thirteen podiums and one hundred seventeen poles. By our own arithmetic, that is a win in about thirty-six percent of the races it entered. For a car from a company that did not build supercars, that is remarkable.""",
   "Dodge Viper racing", "445 RACES · 162 WINS")
sc("""The road cars grew in size. Wikipedia says the third generation, in two thousand three, had an eight point three litre V ten with five hundred horsepower. The fourth generation, in two thousand eight, had eight point four litres and six hundred horsepower. By our arithmetic, power rose fifty percent from the first car to the fourth, from four hundred to six hundred.""",
   "Dodge Viper SRT-10", "400 HP → 600 HP IN 16 YEARS")

sc("""Special editions kept the legend alive. Wikipedia lists the G T two Champion Edition of nineteen ninety-eight, with four hundred sixty horsepower, only one hundred built, and a price approved at eighty-five thousand, two hundred dollars. And the Viper Competition Coupe, from two thousand three to two thousand six, with five hundred twenty horsepower, of which one hundred fifty were built.""",
   "Dodge Viper GT2 Champion Edition", "GT2 CHAMPION: 100 BUILT · COMPETITION COUPE: 150")
sc("""Car and Driver tested that Competition Coupe, Wikipedia says, and recorded zero to a hundred miles per hour in seven seconds, and one point one nine g on the skidpad. By our arithmetic, the Viper's price had risen from fifty-two thousand dollars in nineteen ninety-two to eighty-five thousand two hundred for the G T two six years later, about sixty-four percent.""",
   "Car and Driver Viper test", "0–100 MPH IN 7.0 SECONDS")
sc("""The engine itself got lighter. Wikipedia lists the first V ten at three hundred twenty-three kilograms, and says that the third generation's engine weighed about five hundred pounds, or two hundred thirty kilograms. By our arithmetic, that is about twenty-nine percent lighter, while power went up by twenty-five percent from four hundred to five hundred horsepower.""",
   "Dodge Viper V10 engine", "ENGINE 29% LIGHTER, POWER +25%")
sc("""The Viper had a life in popular culture too. Wikipedia says the nineteen ninety-four to nineteen ninety-eight television series Viper featured a modified R T ten called The Defender, and only fourteen of those cars were built. In Europe, Wikipedia says, the third generation was sold in the United Kingdom as the Dodge S R T ten, because Viper is a trademark there.""",
   "Dodge Viper TV series", "TV'S \"THE DEFENDER\": 14 BUILT")
sc("""Dodge also showed ideas that never reached production. Wikipedia lists the GTS-R Concept in two thousand, the S R T ten Carbon Concept at the two thousand three SEMA show with six hundred twenty-five horsepower, and a Viper Mopar Concept in two thousand seven with six hundred seventy-five. Each was a hint of what the next car might be.""",
   "Dodge Viper concept", "CONCEPTS: 625 HP AND 675 HP")
sc("""Fuel use was part of the Viper's character. Wikipedia lists the first car at twelve miles per gallon in the city and twenty on the highway. Autoblog, in a two thousand eight comparison for the Corvette Z R one, lists the Viper at thirteen city and twenty-two highway, against the Corvette's fourteen and twenty. Nobody bought either car to save fuel.""",
   "Dodge Viper fuel economy", "12/20 MPG IN 1992 · 13/22 IN 2008")
sc("""The fourth generation was the sharpest of the old Vipers. Wikipedia lists an eight thousand three hundred eighty-two cubic centimetre V ten with six hundred horsepower at six thousand one hundred r p m, improved valvetrain, dual electronic throttle bodies and a new Tremec six-speed manual. A vented engine cover is what tells it from the third generation.""",
   "Dodge Viper ZB II", "2008: 600 HP · TREMEC TR6060")
# ---------- 3. FIRST DEATH ----------
ch("Death number one: 2010")
sc("""Now the first ending. Wikipedia says that in two thousand seven there were no model-year cars, because production of the two thousand six model was extended. In two thousand nine, brand chief executive Ralph Gilles announced that production would end in the summer of twenty ten. The last of the fourth generation, a gold car with orange stripes, was built on the first of July, twenty ten.""",
   "Dodge Viper final 2010", "1 JULY 2010: THE LAST ZB II")
sc("""Look at the sales. Good Car Bad Car lists United States sales of one thousand one hundred seventy-two Vipers in two thousand eight. Then four hundred eighty-two in two thousand nine, three hundred ninety-two in two thousand ten, and one hundred ninety-seven in two thousand eleven. By our arithmetic, sales fell by about sixty-seven percent in two years.""",
   "Dodge Viper sales chart", "2008: 1,172 → 2010: 392 (−67%)")
sc("""And the earlier years were bigger. The same source lists one thousand six hundred fifty-two Vipers in two thousand five and one thousand four hundred fifty-five in two thousand six. By our arithmetic, the two thousand ten figure is less than a quarter of the two thousand five figure. The car had been fading for years before the first death.""",
   "Dodge Viper sales", "2005: 1,652 → 2010: 392")
sc("""The Viper was not forgotten, though. Wikipedia says Sergio Marchionne previewed a two thousand twelve prototype in September twenty ten, only two months after the last car was built. The fifth generation was revealed at the twenty twelve New York Auto Show. So the car that was dead was in fact asleep.""",
   "Sergio Marchionne", "SEPTEMBER 2010: MARCHIONNE PREVIEWS A NEW ONE")

sc("""The Viper had also been a pace car twice. Wikipedia says the G T S was chosen as the nineteen ninety-six Indianapolis five hundred pace car, with its so-called double bubble roof inspired by the Shelby Daytona. Shelby himself drove the pre-production car in nineteen ninety-one. A car with two pace-car appearances in five years was clearly a brand symbol.""",
   "Indianapolis 500 pace car", "1991 AND 1996: INDIANAPOLIS PACE CAR")
# ---------- 4. THE RETURN ----------
ch("The comeback")
sc("""The new Viper was serious. Wikipedia lists an all-aluminium eight point four litre V ten with six hundred forty horsepower and six hundred pound-feet of torque, a six-speed Tremec manual, and a carbon fibre and aluminium body. It reached sixty-two miles per hour in three and a half seconds, and two hundred six miles per hour.""",
   "Dodge Viper 2013", "2013: 640 HP · 206 MPH")
sc("""It also added things the Viper had never had. Wikipedia says the fifth generation was the first Viper with electronic stability control, traction control and four-channel A B S. For a car launched in nineteen ninety-two with none of them, that is a long time coming. By our arithmetic, it took twenty-one years.""",
   "Dodge Viper cockpit", "FIRST ESC, TRACTION CONTROL AND ABS: 2013")
sc("""The sales picked up, at first. Good Car Bad Car lists five hundred ninety-one cars in two thousand thirteen and seven hundred sixty in twenty fourteen. Two thousand twelve shows only twenty, which fits the gap while the new car was being introduced. So in its first full year back, the Viper sold almost twice as many as in two thousand ten.""",
   "Dodge Viper 2014", "2013: 591 · 2014: 760")
sc("""But there were troubles. Wikipedia says that in October twenty thirteen, production was cut by a third because of low sales. In April twenty fourteen, production halted for more than two months. So even as sales rose, the company was building fewer cars than planned. A car that was too expensive for its audience, in our reading.""",
   "Conner Avenue Assembly", "OCT 2013: PRODUCTION CUT BY A THIRD")
sc("""Then the numbers slipped. Motor Authority reported that just six hundred seventy-six Vipers were sold in two thousand fifteen, down eleven percent on the previous year. Good Car Bad Car lists six hundred twenty-six for twenty sixteen and five hundred eighty-five for twenty seventeen. A slow decline, but not a collapse.""",
   "Dodge Viper 2015", "2015: 676 (−11%) · 2016: 626 · 2017: 585")
sc("""The Drive gives a slightly different number for twenty sixteen: six hundred thirty, down eight point seven percent from twenty fifteen. The two sources differ by four cars. That kind of difference is typical of sales tables. For our purpose, the conclusion is the same, a car selling six hundred or so a year.""",
   "Dodge Viper sales", "626 OR 630: SOURCES DIFFER")
sc("""Add up the revival. By our own arithmetic, the five years from twenty thirteen to twenty seventeen total three thousand, two hundred thirty-eight cars. That is about two and three-quarter times the one thousand one hundred seventy-two sold in two thousand eight alone. The fifth generation sold in ordinary numbers for a Viper, not terrible ones.""",
   "Dodge Viper production", "2013–2017: 3,238 CARS (OUR ARITHMETIC)")

sc("""The racing never stopped either. Wikipedia says that in twenty fourteen the Viper won the Brickyard Grand Prix and the Lone Star Le Mans in the United SportsCar Championship, taking the drivers' and teams' titles with Kuno Wittmer. And the Viper G T three R, estimated at four hundred fifty-nine thousand dollars with six hundred eighty horsepower, won G T three class races in twenty fourteen and twenty fifteen.""",
   "Dodge Viper GT3-R", "2014 USCC TITLE · GT3-R: 680 HP")
sc("""The ACR name has its own history. Wikipedia says the first ACR was a package on the nineteen ninety-nine G T S, using G T two intake parts and BBS wheels. The fourth-generation ACR produced about a thousand pounds of downforce at a hundred fifty miles per hour. The last ACR produced fifteen hundred pounds in corners, or two thousand with the Extreme Aero Package.""",
   "Dodge Viper ACR aero", "ACR DOWNFORCE: 1,000 → 2,000 LB")
sc("""That aero cost something. Wikipedia says the last ACR's top speed fell by up to twenty miles per hour. A car built for corners, not straights. And Wikipedia says Kuno Wittmer drove a street-legal two thousand ten ACR to one fifty-nine point nine nine five at Miller Motorsports Park, the first production car under two minutes there.""",
   "Miller Motorsports Park", "FIRST PRODUCTION CAR UNDER 2:00 AT MILLER")
sc("""In twenty fifteen, the car was renamed S R T Viper, and Wikipedia says power rose to six hundred forty-five horsepower, with highway economy of twenty miles per gallon. So at the moment the end was announced, the Viper was at its strongest and most refined. A car does not die because it is bad at being a car.""",
   "SRT Viper 2015", "2015: SRT VIPER, 645 HP")
sc("""The timing matters. The announcement of the end came in October twenty fifteen, according to Wikipedia, only a few months after the car's best power figure. The Drive says the new safety rules took effect on the first of September, twenty seventeen. By our arithmetic, the company gave the Viper about twenty-two months between the announcement and the end of production.""",
   "Dodge Viper Final", "OCT 2015 → AUG 2017: 22 MONTHS")
# ---------- 5. DEATH TWO ----------
ch("Death number two: 2017")
sc("""Now the second ending. Wikipedia says that in October twenty fifteen, Fiat Chrysler announced that the Viper would end in twenty seventeen. The Drive says the Conner Avenue plant in Detroit, where every Viper had been hand-built since nineteen ninety-five, would shut down on the thirty-first of August, twenty seventeen.""",
   "Conner Avenue plant Detroit", "OCTOBER 2015: THE END IS ANNOUNCED")
sc("""The Drive says it was the smallest F C A plant in North America, with just over eighty employees, who were expected to move to other plants. The plant had also built the Plymouth and Chrysler Prowler, and the Viper's V ten engine since two thousand one. Eighty people built a car that carried a company's reputation.""",
   "Hand-built Viper", "A PLANT OF ~80 PEOPLE")
sc("""What was the reason? Fiat Chrysler, Motor Authority said, hadn't come out and stated why it was killing the Viper. The Drive wrote that F C A chose to discontinue the car rather than redesign it to meet new safety regulations that took effect on the first of September. It also cited low sales.""",
   "Dodge Viper", "\"RATHER THAN REDESIGN IT\"")
sc("""The regulation was federal motor vehicle safety standard two twenty-six. Motor Authority says that, starting in twenty seventeen, all new cars would need to comply with the standard, which requires side curtain airbags. A car designed in the nineteen nineties, with a low roof and a carbon body, had little room for them.""",
   "Side curtain airbags", "FMVSS 226: SIDE CURTAIN AIRBAGS")
sc("""In May twenty twenty-six, the head of S R T finally explained it in his own words. Tim Kuniskis told The Drive that the car had to be discontinued because of a new ejection-mitigation rule. In his words, you would have to put airbags right over you, as a driver, right over your ear. That made the car impossible to build as it was.""",
   "Tim Kuniskis SRT", "\"AIRBAGS RIGHT OVER YOUR EAR\" — KUNISKIS, 2026")
sc("""Kuniskis went further, according to the same article. He said the Viper reached the end of its life cycle, and called it an analogue car with a manual transmission that had downsides. To stay competitive today, he said, it would have needed to become an automatic or a dual-clutch. A Viper like that, in our reading, would not be a Viper.""",
   "Dodge Viper manual", "\"IT REACHED THE END OF ITS LIFE CYCLE\"")
sc("""So there are two explanations, and the sources give both. Low sales are the one most people repeat. The airbag rule is the one that the S R T chief says was the real reason. The Yahoo article that reports his comment says common guesses like emissions, the V ten and low sales were not the actual cause. We report that as his claim.""",
   "Dodge Viper", "SALES OR REGULATION? THE SOURCES SAY BOTH")

sc("""There is a useful comparison with the Corvette. Vette Vues lists Corvette Z R one production at four thousand, six hundred eighty-four cars from two thousand nine to two thousand thirteen. By our arithmetic, that is about nine hundred thirty-seven a year. Good Car Bad Car lists Viper sales of about three hundred thirty-six a year over the same five years.""",
   "Chevrolet Corvette ZR1", "ZR1: ~937 A YEAR · VIPER: ~336 A YEAR")
sc("""That is production against sales, and the two are not identical, so we keep the claim modest. But the direction is clear. In the years after the first death, the Corvette's top model was being built in roughly three times the quantity of the Viper, at a price of a hundred three thousand dollars. The sources do not say how many Corvette buyers would have chosen a Viper instead.""",
   "Corvette ZR1 and Dodge Viper", "THE CORVETTE OUTSOLD THE VIPER ~3 TO 1")
sc("""Wikipedia also records two body styles. The convertible was built from nineteen ninety-one to twenty ten, and the liftback coupé from nineteen ninety-six to twenty seventeen. So the final Viper was a coupé, and the open car had already gone seven years earlier. The first death took the roadster, and the second took everything else.""",
   "Dodge Viper coupe and roadster", "ROADSTER ENDED 2010 · COUPÉ ENDED 2017")
# ---------- 6. THE LEGACY ----------
ch("What the Viper left behind")
sc("""In all, Wikipedia says thirty-one thousand, nine hundred eighty-nine Vipers were built in twenty-six years. By our own arithmetic, that is an average of about twelve hundred thirty a year. It was built at the New Mack plant until nineteen ninety-five, and then at Conner Avenue. A modest total, for a car that left such a mark.""",
   "Dodge Viper production line", "31,989 BUILT IN 26 YEARS")
sc("""The Viper kept racing records after it died. Wikipedia says an ACR-X set seven minutes three seconds at the Nürburgring in February twenty twelve. And a Viper ACR with the extreme aero package, driven by Dominik Farnbacher, did an unofficial seven oh one point six seven in October twenty fifteen.""",
   "Nürburgring Dodge Viper ACR", "NÜRBURGRING: 7:01.67 (UNOFFICIAL, 2015)")
sc("""In twenty seventeen a crowdfunded attempt tried to beat the Lamborghini Huracán Performante's six fifty-two oh one. Wikipedia says one car crashed and the attempt failed. But it did make the Viper ACR the fastest American, rear-wheel-drive, manual-transmission car on the track at the time. A fitting last chapter for a car like this.""",
   "Dodge Viper ACR crash", "THE LAST ATTEMPT: FASTEST AMERICAN MANUAL RWD")
sc("""And the value of the used cars tells a story of its own. Classic dot com's data shows eight Viper ACR sales between May and November twenty twenty-five, from one hundred eighty-seven thousand dollars to four hundred six thousand five hundred. By our arithmetic, the average was two hundred ninety-three thousand, eight hundred forty-six. A car that died of low sales is now collected.""",
   "Dodge Viper ACR auction", "ACR SALES 2025: $187K TO $406K")
sc("""Which brings us to the question of why it died twice. The first time, sales had collapsed and the company was in trouble. The second time, the car was selling around six hundred a year, and a rule made the next version impossible without changing what it was. One was a business problem. The other was a design problem.""",
   "Dodge Viper", "A BUSINESS PROBLEM, THEN A DESIGN PROBLEM")
sc("""Which death do you think hurt more, the first or the second? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the Viper, compare the Viper ACR with the Corvette Z R one, and work out what it really costs to own a Viper today.""",
   "Dodge Viper ACR", "WHICH DEATH HURT MORE?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video96", "Why the Dodge Viper Was Killed (Twice)", [
    "Wikipedia, Dodge Viper: https://en.wikipedia.org/wiki/Dodge_Viper",
    "Good Car Bad Car, Dodge Viper sales figures: https://www.goodcarbadcar.net/dodge-viper-sales-figures/",
    "Motor Authority, Dodge Viper production ending due to airbag regulations: https://www.motorauthority.com/news/1101880_dodge-viper-production-ending-due-to-airbag-regulations",
    "The Drive, Dodge Viper factory to close August 31: https://www.thedrive.com/article/12390/dodge-viper-factory-to-close-august-31",
    "Yahoo / The Drive, The Dodge Viper era is dead, head of SRT says (29 May 2026): https://autos.yahoo.com/people-and-culture/articles/dodge-viper-era-dead-head-164100036.html",
    "Classic.com, Dodge Viper ACR VX I market: https://www.classic.com/m/dodge/viper/5th-gen/acr/",
], "D")
