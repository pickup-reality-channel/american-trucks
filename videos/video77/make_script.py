import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Ford GT is one of the most exclusive American cars ever built. About one thousand three hundred fifty were made, buyers had to apply just to be allowed to buy one, and it won its class at Le Mans in its very first try. But two secrets about this car are almost never told. One is about a door. The other is about what this car did to Porsche.""",
   "Ford GT 2017", "2 SECRETS HIDDEN INSIDE THE FORD GT")
sc("""Here is the hint. The Ford GT was designed behind a door that looked like a broom cupboard, by a team that started without permission from Ford's own bosses. And once it hit the race track, it was so effective that Porsche reportedly redesigned its most famous race car. Both stories are documented, and both are true.""",
   "Ford GT Le Mans 2016", "A BROOM CUPBOARD AND A PORSCHE")
sc("""Along the way, you will see the Mustang that had to die so the GT could live, the seats that do not move, the lawsuit against a famous wrestler, and the final version that set a lap record in twenty twenty-six. Every number comes from a published source, listed in the description.""",
   "Ford GT Mk IV", "EVERY NUMBER IS SOURCED")
sc("""And there is one more twist. The car that Ford sold for about half a million dollars was being valued at close to eight hundred thousand dollars years later. But first, the car itself.""",
   "Ford GT blue", "THE VALUE TWIST")

# ---------- 1. THE CAR ----------
ch("The car")
sc("""According to Wikipedia, Ford showed the second-generation GT at the twenty fifteen North American International Auto Show in Detroit. Production began in December twenty sixteen. The cars were built not by Ford itself, but by Multimatic, a Canadian engineering company, in Markham, Ontario, at a planned rate of about one car per day.""",
   "Ford GT Detroit auto show 2015", "REVEALED: DETROIT 2015")
sc("""Its engine surprised people. Instead of a V8, the GT used a three point five liter twin-turbo EcoBoost V6, related to the engines Ford uses in its trucks. Gear Patrol reported six hundred forty-seven horsepower and five hundred fifty pound-feet of torque, a top speed of two hundred sixteen miles per hour, and zero to sixty in two point nine seconds. Wikipedia says power rose to six hundred sixty horsepower for twenty twenty.""",
   "Ford GT EcoBoost V6", "647 HP V6, 216 MPH")
sc("""The V6 was chosen for a reason. Gear Patrol said the engine's slim packaging allowed the designers to build Ford's most aerodynamically efficient car. Look at the body. Between the cabin and the rear wheels, there are huge open channels where air flows through the car. That shape was only possible because the engine was narrow.""",
   "Ford GT rear flying buttress", "SHAPED BY THE AIR")
sc("""The chassis is a carbon fiber monocoque, Wikipedia says, and Gear Patrol listed a dry weight of about three thousand fifty-four pounds. There is an active rear wing, and in Track mode, which can only be selected when the car is stopped, the GT drops about two inches and its spoiler rises about a foot.""",
   "Ford GT active wing", "TRACK MODE: -2 INCHES")
sc("""Gear Patrol listed a starting price of about four hundred fifty thousand dollars. That is the car. Now, the first secret, which starts years before anyone saw it.""",
   "Ford GT", "$450,000")

# ---------- 2. SECRET ONE ----------
ch("Secret 1: the broom cupboard")
sc("""Secret number one. The Ford GT was born out of a cancelled Mustang. Jalopnik reported that Raj Nair, then Ford's head of product development, had backed a racing Mustang for Le Mans, a program called Project Silver, named after the Lone Ranger's horse. It would even have had a carbon fiber passenger cell.""",
   "Ford Mustang race car", "SECRET 1: PROJECT SILVER")
sc("""But Project Silver was cancelled. Jalopnik, citing the Auto Extremist, said it ground to a halt at the final go or no-go meeting in Mark Fields' office, because of cost and reluctance among some regional executives to pay their share. The racing Mustang was dead.""",
   "Ford headquarters Dearborn", "CANCELLED")
sc("""So Nair did something unusual. Jalopnik reported that he started a new program in secret, without his bosses' approval, in a basement warehouse at Ford's Product Development Center in Dearborn, Michigan. The team called it Project Phoenix, the bird that rises from the ashes.""",
   "Ford Product Development Center Dearborn", "PROJECT PHOENIX")
sc("""And the secrecy was extreme. Motoring Research reported that the studio sat in a basement at Ford's Dearborn design center, while colleagues upstairs worked on cars like the Edge and the Fusion. The door to the studio was disguised as a broom cupboard, and designer Chris Svensson unlocked it with a physical key. He called it old school.""",
   "Ford GT design studio clay model", "A DOOR DISGUISED AS A BROOM CUPBOARD")
sc("""Svensson also said that, fortunately, no one really asked what he was working on. Wikipedia quotes him saying that only a handful of about twelve people had access to the design studio. One of the most important Fords in decades was designed by a dozen people behind a fake cupboard door.""",
   "Ford GT sketch", "ONLY ABOUT 12 PEOPLE KNEW")
sc("""Here is the twist. Motoring Research said the performance team was involved from the start, while the accountants were kept away. That is why the design changed so little from the early clay model to the production car. In most car projects, the budget shapes the design. Here, the design came first.""",
   "Ford GT clay model", "THE ACCOUNTANTS WERE KEPT AWAY")
sc("""And the reveal was a form of revenge. Jalopnik reported that Nair later took each executive who had rejected Project Silver down to the secret room to show them the car. The project that had been killed came back as something far bigger, a carbon fiber supercar built to win Le Mans.""",
   "Ford GT reveal", "THE PHOENIX RISES")
sc("""Nair later told this story in public. Jalopnik reported that he described it at the S A E World Congress in Detroit, saying the GT had risen from the ashes of the Mustang project. It is rare for a senior car executive to admit that one of the company's most famous cars started as an unapproved side project.""",
   "Ford GT Detroit", "FROM THE ASHES")

# ---------- 3. LE MANS 2016 ----------
ch("Le Mans, fifty years later")
sc("""Why Le Mans? Because of history. In nineteen sixty-six, Ford's G T forty finished first, second, and third at the twenty-four hours of Le Mans, ending Ferrari's run of six straight victories, Petrolicious reported. The new GT was designed to return exactly fifty years later.""",
   "Ford GT40 1966 Le Mans", "1966: FORD 1-2-3")
sc("""And that rivalry started with a failed deal. Petrolicious reported that in nineteen sixty-three, Ford tried to buy Ferrari, spending several million dollars on negotiations and audits. The deal collapsed when Ford refused to give Enzo Ferrari full control of his racing programs. Ford decided to beat Ferrari on the track instead.""",
   "Enzo Ferrari", "1963: THE FAILED DEAL")
sc("""Even the nineteen sixty-six win had drama. Wikipedia says Ken Miles was leading when Ford told him to slow down so three of its cars could cross the line together for a photo. Because Bruce McLaren's car had started further back and covered more distance, McLaren and Chris Amon were declared the winners. Miles finished second.""",
   "Ford GT40 1966 photo finish", "THE STAGED FINISH")
sc("""And it worked. Wikipedia says that in twenty sixteen, a Ford Chip Ganassi Racing GT won the L M G T E Pro class at Le Mans, fifty years after the nineteen sixty-six victory. A car designed in a basement behind a fake broom cupboard had won the world's most famous endurance race, in its class, at its first attempt.""",
   "Ford GT Le Mans 2016 win", "2016: CLASS WIN AT LE MANS")
sc("""The original G T forty did not stop at one win either. Petrolicious reported that in nineteen sixty-seven, the G T forty Mark four became the first entirely American-designed and built car to win Le Mans, and that Ford won again in nineteen sixty-eight and nineteen sixty-nine, four Le Mans victories in a row. The new GT carried that legacy on its shoulders.""",
   "Ford GT40 Mk IV 1967", "FOUR LE MANS WINS IN A ROW")
sc("""It is a story Hollywood would love. And in fact, three years later, Hollywood told the original one. The twenty nineteen film Ford versus Ferrari dramatized the nineteen sixties G T forty program, with Matt Damon as Carroll Shelby and Christian Bale as driver Ken Miles, according to Wikipedia.""",
   "Ford v Ferrari film", "FORD v FERRARI")

# ---------- 4. SECRET TWO ----------
ch("Secret 2: what it did to Porsche")
sc("""Secret number two. The Ford GT race car was so effective that it changed one of Porsche's most famous race cars. Gear Patrol reported that after the GT's success, Porsche re-engineered its nine eleven R S R Le Mans race car for twenty seventeen, moving its flat-six engine from the very back of the car to the middle.""",
   "Porsche 911 RSR 2017", "SECRET 2: PORSCHE MOVED THE ENGINE")
sc("""Think about how big that is. The nine eleven has always had its engine behind the rear axle. It is the car's identity. For decades, Porsche engineered around that layout instead of abandoning it. Gear Patrol said Porsche moved the engine to improve aerodynamic efficiency and close the gap with the Ford on the track.""",
   "Porsche 911 rear engine", "BREAKING THE 911 RULE")
sc("""Why would the engine position matter so much? A race car makes much of its downforce with a large diffuser under the rear. With the engine hanging at the very back, there is less room for that diffuser. Moving the engine forward freed up space at the rear for aerodynamics, exactly where the Ford GT was so strong.""",
   "race car rear diffuser", "ROOM FOR THE DIFFUSER")
sc("""So the Ford GT's narrow V6 and its air channels did not only win races. They pushed a rival to rethink a design that had defined it for half a century. That is the kind of impact few cars ever have.""",
   "Ford GT race car", "IT CHANGED A RIVAL")

# ---------- 5. THE FIXED SEATS ----------
ch("A cockpit built around the driver")
sc("""There is another detail inside the car that surprises people. The seats do not move. Gear Patrol reported that the bucket seats are fixed directly to the carbon fiber tub. Instead, the pedal box and the steering wheel move to fit the driver. The pedal box adjusts with a nylon pull strap.""",
   "Ford GT interior seats", "THE SEATS DON'T MOVE")
sc("""This is race car thinking. Fixing the seats to the structure saves weight, keeps the driver low, and makes the seat part of the chassis. It is unusual in a road car, and it tells you what the Ford GT really is. A Le Mans car with license plates.""",
   "Ford GT cockpit", "A LE MANS CAR WITH PLATES")
sc("""Gear Patrol also noted that the engine uses an anti-lag system that keeps the turbochargers spooled in Sport and Track modes, so all six hundred forty-seven horsepower and five hundred fifty pound-feet are ready the moment the driver presses the throttle. Another idea taken straight from racing.""",
   "Ford GT engine turbo", "ANTI-LAG FROM RACING")
sc("""The gearbox was a seven-speed automatic, Gear Patrol reported, and there was no manual option. Combined with the anti-lag system and the active aerodynamics, the GT was built to be fast every lap, not just exciting on a back road. That focus is exactly why it worked so well when Ford took it racing.""",
   "Ford GT gear selector", "7-SPEED, NO MANUAL")

# ---------- 6. THE APPLICATION ----------
ch("You had to apply")
sc("""Buying one was not simple either. Car Showroom, an Australian outlet, reported that buyers had to submit an application to Ford for review, and that Ford reportedly preferred buyers who would drive the car rather than treat it as a status symbol. Previous ownership of Ford performance cars helped.""",
   "Ford GT application", "YOU HAD TO APPLY")
sc("""Production was supposed to be small. Ford started with five hundred cars, then doubled it to one thousand, then added three hundred fifty more, Car Showroom reported. Jalopnik said the plan was two hundred fifty cars per year, but Ford built only one hundred thirty-eight for the twenty seventeen model year, as Multimatic slowly ramped up.""",
   "Ford GT production Multimatic", "500, THEN 1,000, THEN 1,350")
sc("""Why so slow? Jalopnik reported that a Ford spokesman described a planned, extended ramp-up. Multimatic had never built cars at this scale, and it did not reach its daily build rate until mid twenty seventeen. There were also supplier issues and painting delays on special Victory edition cars. Building a race car for the road, one per day, turned out to be hard.""",
   "Ford GT assembly", "138 CARS IN YEAR ONE")
sc("""And the waiting list kept growing. Car Showroom said demand was out of control all over the world, and that when Ford added the extra three hundred fifty cars, the application books reopened from the eighth of November to the seventh of December. Once again, buyers had to apply and wait to be chosen.""",
   "Ford GT showroom", "THE BOOKS REOPEN")
sc("""And there was a contract. Autoblog reported that buyers approved for the first five hundred GTs agreed not to resell their cars for twenty-four months. Ford wanted owners, not flippers.""",
   "Ford GT contract", "NO RESALE FOR 24 MONTHS")
sc("""Then came the famous case. Autoblog reported that the wrestler and actor John Cena received his Ford GT in late September twenty seventeen and sold it in October. Ford sued him in November, seeking seventy-five thousand dollars in damages and more. The case was settled out of court in June twenty eighteen, and Cena's lawyers said the undisclosed amount would go to charity. Cena said, I love the Ford GT and apologize to Ford.""",
   "John Cena", "FORD SUED JOHN CENA")
sc("""Autoblog said Cena first claimed he did not know about the resale restriction, and in February twenty eighteen he asked a judge to dismiss the case. In the end, he settled. The message to every other owner was clear. Ford was serious about its contract.""",
   "courthouse", "FORD WAS SERIOUS")

# ---------- 7. THE NAME ----------
ch("Why it's not called GT40")
sc("""Here is another detail many fans do not know. Why is it called the GT and not the G T forty? Wikipedia says that when Ford built the first-generation GT in two thousand five, it tried to buy the rights to the G T forty name. The owners wanted forty million dollars. So the production car was simply called the GT.""",
   "Ford GT 2005", "WHY NOT 'GT40'?")
sc("""The original name came from the car's height. Petrolicious and Car and Classic both reported that the G T forty was named for its overall height of forty inches. A car so low that it gave its name to a number. The modern GT kept the spirit, but not the name.""",
   "Ford GT40 low", "40 INCHES TALL")
sc("""And the G T forty itself was partly British. Car and Classic reported that it was based on Eric Broadley's Lola Mark six, a British, aluminum-bodied V8 GT car, and that early development took place in Slough, England, with Broadley, Ford engineer Roy Lunn, and team manager John Wyer. Only later did the project move to America, under Carroll Shelby.""",
   "Lola Mk6 GT", "BORN IN ENGLAND")
sc("""Wikipedia says Ford built four thousand thirty-eight first-generation GTs, with a supercharged five point four liter V8 of five hundred fifty horsepower, and a suggested price of about one hundred forty thousand dollars. The second generation was far rarer, far more expensive, and far more of a race car.""",
   "Ford GT 2005 first generation", "FIRST GEN: 4,038 BUILT")
sc("""Even that first generation became hard to buy. Wikipedia says production ended in September two thousand six, short of the planned four thousand five hundred cars, and that some early buyers paid up to one hundred thousand dollars over the sticker price. One of the first production cars sold for more than five hundred fifty-seven thousand dollars at a charity auction.""",
   "Ford GT 2005 auction", "$557,000 AT A CHARITY AUCTION")

# ---------- 8. THE FINAL VERSIONS ----------
ch("The final versions")
sc("""Ford did not stop with the road car. Wikipedia lists the GT Mark two, a track-only version with about seven hundred horsepower, of which only forty-five were built, at about one point two million dollars each. And a twenty twenty Liquid Carbon edition, with exposed carbon fiber bodywork, at about seven hundred fifty thousand dollars.""",
   "Ford GT Mk II", "MK II: 45 CARS, $1.2M")
sc("""There were also special editions that looked back to the nineteen sixties. Wikipedia mentions the twenty twenty-two sixty-four Heritage Edition, which mimics an early G T forty prototype called the GT slash one oh five, and the twenty twenty-two L M Edition in Liquid Silver with red or blue accents. Each one tied the modern car to its history.""",
   "Ford GT Heritage Edition", "HERITAGE EDITIONS")
sc("""Then came the last one. The GT Mark four, a final send-off with sixty-seven examples planned, at about one point seven million dollars, according to Wikipedia. And in April twenty twenty-six, Ford reported that the Mark four lapped the Nürburgring Nordschleife in six minutes fifteen point nine seven seven seconds, driven by Frédéric Vervisch.""",
   "Ford GT Mk IV", "MK IV: 6:15.977")
sc("""Ford called it the third fastest car ever to lap the Nordschleife, and the fastest internal combustion engine car around the circuit, with more than eight hundred horsepower from a twin-turbo EcoBoost engine. But note the detail. Ford describes the Mark four as a track-only vehicle, and Corvette Blogger called it a non-street-legal car.""",
   "Nürburgring Nordschleife", "3RD FASTEST EVER")
sc("""So the car that began behind a fake cupboard door ended with one of the fastest laps in Nürburgring history. From a cancelled Mustang to a Le Mans win to a lap record, the GT's life was one long revenge story.""",
   "Ford GT Mk IV track", "ONE LONG REVENGE STORY")

# ---------- 9. THE VALUE ----------
ch("What it's worth now")
sc("""And the value twist. Gear Patrol listed a starting price of about four hundred fifty thousand dollars, and Car Showroom said Ford estimated around five hundred thousand. Hagerty's valuation tool listed a twenty twenty-two Ford GT at about seven hundred eighty-eight thousand dollars in January twenty twenty-six.""",
   "Ford GT auction", "HAGERTY: ~$788,000")
sc("""That is a gain of roughly fifty to seventy-five percent over the original price, by our own arithmetic. For buyers who followed the rules and kept their cars for at least two years, the GT turned out to be not only a thrill, but a good investment. And that makes the John Cena story even more striking.""",
   "Ford GT parked", "A GOOD INVESTMENT")
sc("""So why did values rise? Small production, a racing story, an application process, and a no-resale contract all made the car feel rare. Ford deliberately controlled who got one. That scarcity is a big part of what owners are paying for.""",
   "Ford GT Heritage Edition", "CONTROLLED SCARCITY")
sc("""And it explains why Ford fought so hard over a single resale. If owners could buy at sticker and flip immediately for a profit, the application process would become a lottery for speculators. By enforcing the two-year rule, even against a celebrity, Ford protected the idea that the GT was meant to be driven by people who loved it.""",
   "Ford GT owner driving", "MEANT TO BE DRIVEN")

# ---------- 10. RECAP ----------
ch("The two secrets, again")
sc("""So let's recap the two secrets hidden inside the Ford GT. Number one, it was born after the cancellation of a racing Mustang called Project Silver, and designed in secret as Project Phoenix, behind a door disguised as a broom cupboard, by a team of about a dozen people.""",
   "Ford GT design", "1. THE BROOM CUPBOARD")
sc("""Number two, its race car was so effective that Porsche reportedly redesigned its nine eleven R S R for twenty seventeen, moving the engine from the very back to the middle, to improve aerodynamics and close the gap with the Ford. A Ford changed the most famous rear-engined car in the world.""",
   "Porsche 911 RSR and Ford GT", "2. IT CHANGED PORSCHE")
sc("""In the other videos of this series, we compare the modern GT with the original G T forty, we look at the real cost of owning one and why owners had to sign a contract, and we tell the story of the man who made Ford beat Ferrari. Tell us in the comments which secret surprised you more.""",
   "Ford GT40 and Ford GT", "3 MORE ANGLES")
sc("""And if you are shopping for a Ford with a bed instead of a wing, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford GT sunset", "SUBSCRIBE: PICKUP REALITY")

save("video77", "2 Secrets Hidden Inside the Ford GT", [
    "Wikipedia, Ford GT: https://en.wikipedia.org/wiki/Ford_GT",
    "Gear Patrol, The car that forced Porsche to redesign its fastest 911 (May 2017): https://www.gearpatrol.com/cars/a352077/ford-gt-review-specs-images-porsche-911-ferrari-488gtb/",
    "Jalopnik, The Ford GT was born to avenge the death of a secret Mustang: https://www.jalopnik.com/the-ford-gt-was-born-to-avenge-the-death-of-a-secret-mu-1794070410/",
    "Motoring Research, 2017 Ford GT: inside the top secret design studio (May 2017): https://www.motoringresearch.com/car-news-list/features/2017-ford-gt-design-studio/",
    "Petrolicious, Ford's quest to beat Ferrari with the GT40: https://petrolicious.com/blogs/articles/ford-gt40",
    "Car and Classic, Legend of Le Mans: Ford's GT40 turns 60: https://www.carandclassic.com/magazine/legend-of-le-mans-fords-gt40-turns-60/",
    "Car Showroom, Ford will build 350 more GTs: https://www.carshowroom.com.au/news/ford-will-build-350-more-gts-books-open-november-8th/",
    "Jalopnik, Ford missed its production target for the first year of the Ford GT: https://jalopnik.com/1827701915",
    "Autoblog, John Cena and Ford settle over flipped GT (June 2018): https://www.autoblog.com/2018/06/19/john-cena-ford-gt-flip-settlement",
    "Ford, Ford GT Mk IV makes Nürburgring history (Apr 2026): https://www.at.ford.com/us/en/home/news-media/news/2026/4/ford-gt-mk-iv-makes-nuerburgring-history-with-third-fastest-lap-.html",
    "Corvette Blogger, Ford needed a non-production race car to beat the ZR1X record (Apr 2026): https://www.corvetteblogger.com/2026/04/04/video-ford-needed-a-non-production-race-car-to-beat-the-corvette-zr1xs-record-at-the-nurburgring/",
    "Hagerty valuation tools, 2022 Ford GT (Jan 2026): https://www.hagerty.com/valuation-tools/ford/gt/2022/2022-ford-gt",
    "Wikipedia, Carroll Shelby: https://en.wikipedia.org/wiki/Carroll_Shelby",
], "A")
