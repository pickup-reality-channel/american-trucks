import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""The Chevrolet Corvette Z06 has more power than a Porsche nine eleven G T three R S. It gets to sixty miles per hour faster. It costs about half as much. So why is the Porsche more than twenty seconds faster around the Nürburgring, and why do used ones sell for more than they cost new, while used Z06s sell for less? That is what we are going to explain.""",
   "Chevrolet Corvette Z06", "Z06 vs 911 GT3 RS")
sc("""These two cars are the most famous track-focused sports cars from America and Germany. Both use naturally aspirated engines that rev past eight thousand r p m. Both put their engines behind the driver, but in very different places. And both were built with racing in mind.""",
   "Porsche 911 GT3 RS", "AMERICA vs GERMANY")
sc("""But they win in completely different ways. The Corvette wins on power, acceleration, price, and practicality. The Porsche wins on downforce, weight, lap times, and value over time. By the end of this video, you will know exactly where each one beats the other, and the one number that explains it all.""",
   "Porsche 911 GT3 RS and Corvette Z06", "WHERE EACH ONE WINS")
sc("""Every number in this video comes from a published source, listed in the description. And where a comparison is not perfectly equal, we will tell you.""",
   "Nürburgring Nordschleife", "EVERY NUMBER IS SOURCED")

# ---------- 1. THE CARS ----------
ch("Meet the two cars")
sc("""The Corvette Z06 was unveiled on the twenty-sixth of October twenty twenty-one, according to Wikipedia. It uses the L T six, a five point five liter V8 with a flat-plane crankshaft. The Drive reported six hundred seventy horsepower at eight thousand four hundred r p m, and a redline of eight thousand six hundred.""",
   "Corvette Z06 LT6 engine", "Z06: 670 HP V8")
sc("""Hagerty described it as the most powerful naturally aspirated production V8 ever. Autoblog said its block, heads, valvetrain, and fuel system are shared with the Corvette C eight dot R race car, and that every engine is assembled by a single technician in Bowling Green, Kentucky.""",
   "Corvette C8.R", "A RACE-DERIVED ENGINE")
sc("""The Porsche nine eleven G T three R S of the nine ninety-two generation was revealed on the seventeenth of August twenty twenty-two, The Drive reported. It uses a four liter naturally aspirated flat-six engine, making five hundred eighteen horsepower, with a redline of nine thousand r p m.""",
   "Porsche 911 GT3 RS 992", "GT3 RS: 518 HP FLAT-SIX")
sc("""R S stands for Rennsport, German for racing sport. Porsche has used it on its most extreme nine elevens since the nineteen seventies. And the G T three R S is essentially a road-legal version of the thinking behind Porsche's G T three race cars.""",
   "Porsche 911 Carrera RS 2.7", "RS = RENNSPORT")
sc("""So on paper, the Corvette has about one hundred fifty-two more horsepower. That is a big gap, almost thirty percent more power. If horsepower decided everything, this video would already be over. It does not.""",
   "Corvette Z06 vs Porsche GT3 RS", "+152 HP FOR THE CORVETTE")
sc("""Both names also come from racing. Hagerty reported that the very first Corvette Z06, in nineteen sixty-three, was a racing package created by Zora Arkus-Duntov, and that only one hundred ninety-nine were built that first year. Motor Authority said the first cars went straight to race teams. So the Z06 name is about sixty years old, older than the G T three name by decades.""",
   "1963 Corvette Z06", "THE Z06 NAME: 1963")
sc("""And the two brands have met many times on the track. Corvette Racing and Porsche were long-time rivals in the G T classes at Le Mans. Racer reported that in June twenty twenty-three, the number thirty-three Corvette C eight dot R won the G T E Am class at Le Mans, Corvette's ninth class win, in the final G T E race at the circuit. These road cars carry that rivalry onto the street.""",
   "Corvette C8.R Le Mans 2023", "RIVALS AT LE MANS")

# ---------- 2. WHERE THE Z06 WINS: ACCELERATION ----------
ch("Where the Z06 wins: acceleration")
sc("""Round one, straight-line acceleration. The Drive reported that Chevrolet claims zero to sixty miles per hour in two point six seconds for the Z06. For the G T three R S, The Drive listed three point zero seconds. Four tenths of a second is a big gap in this class.""",
   "Corvette Z06 launch", "0-60: 2.6 s vs 3.0 s")
sc("""Part of the reason is power. The other part is layout. The Corvette's engine sits in the middle of the car, ahead of the rear axle. The Porsche's engine sits behind the rear axle. Both layouts put weight over the driven rear wheels, which helps traction off the line, and both cars use quick dual-clutch gearboxes, eight speeds in the Corvette and seven in the Porsche.""",
   "Porsche 911 GT3 RS engine bay", "MID-ENGINE vs REAR-ENGINE")
sc("""So if you line them up at a drag strip, the Corvette should get to sixty first. The Z06 wins round one. But a race track is not a drag strip, and that is where the story changes.""",
   "drag strip", "ROUND 1: Z06")
sc("""Gearing matters too. Hagerty reported that the Z06 uses only an eight-speed dual-clutch gearbox, with a shorter final drive than the regular Stingray with the Z fifty-one package. The Drive said the G T three R S uses a seven-speed P D K gearbox with shorter, track-focused ratios. Neither car offers a manual. Both are built to shift faster than any human could.""",
   "Porsche PDK gear selector", "NO MANUAL IN EITHER")

# ---------- 3. WHERE THE Z06 WINS: PRICE ----------
ch("Where the Z06 wins: price")
sc("""Round two, price. GM Authority reported a twenty twenty-six Z06 coupe price of about one hundred nineteen thousand seven hundred dollars, including destination. The Drive reported that the twenty twenty-three G T three R S started at about two hundred twenty-five thousand dollars, including fees.""",
   "Corvette Z06 window sticker", "$119,695 vs $225,250")
sc("""To be fair, those are different model years. Prices usually rise over time, so the gap today is likely even larger. Either way, the Porsche costs close to twice as much as the Corvette before options.""",
   "Porsche dealership", "ALMOST DOUBLE")
sc("""And options can make the Porsche far more expensive. CarScoops reported on a twenty twenty-four G T three R S with an original sticker of about three hundred nine thousand dollars, including about ninety thousand dollars in options. The Weissach package alone, with a carbon fiber roof and other lightweight parts, cost about thirty-three thousand five hundred dollars.""",
   "Porsche 911 GT3 RS Weissach", "WEISSACH: ~$33,500")
sc("""The Corvette's options are cheaper. Even a highly equipped Z06 convertible with the Z zero seven package had a sticker of about one hundred seventy thousand dollars, CarScoops reported. That is still far below a well-optioned G T three R S. Round two goes to the Z06, and it is not close.""",
   "Corvette Z06 convertible Z07", "ROUND 2: Z06")

# ---------- 4. WHERE THE Z06 WINS: PRACTICALITY ----------
ch("Where the Z06 wins: daily life")
sc("""Round three, daily life. This is a surprising win for the Corvette. The Associated Press reported that the C eight Corvette has a front trunk that fits an airline-size carry-on, and a rear space that fits two sets of golf clubs. The Z06 is built on the same basic body.""",
   "Corvette C8 frunk", "FRUNK + REAR TRUNK")
sc("""The G T three R S gave up its front trunk. The Drive reported that Porsche replaced the three separate radiators of the regular nine eleven with a single, large, angled radiator in the nose, where the luggage space used to be. Hot air exits through vents in the hood and fins on the roof. It is brilliant for cooling and aerodynamics, but terrible for luggage.""",
   "Porsche GT3 RS hood vents", "NO FRUNK IN THE GT3 RS")
sc("""The Z06 also offers something the G T three R S does not, a convertible. The Drive reported that the Z06 comes as a coupe and a convertible, with the same suspension tuning. If you want an eight thousand six hundred r p m engine with the roof open, the Corvette is the one that offers it.""",
   "Corvette Z06 convertible top down", "Z06 CONVERTIBLE")
sc("""And the Corvette was designed as a road car first, with track ability added. Even its air conditioning, Autoblog reported, is rated to cool the cabin in one hundred degree heat. Round three, daily life, goes to the Z06.""",
   "Corvette Z06 interior", "ROUND 3: Z06")

# ---------- 5. WHERE THE PORSCHE WINS: DOWNFORCE ----------
ch("Where the Porsche wins: downforce")
sc("""Now the Porsche fights back. Round four, downforce. This is the single biggest difference between these two cars. Downforce is the force that the air pushes down onto the car at speed. More downforce means more grip in fast corners, and more confidence under braking.""",
   "Porsche 911 GT3 RS rear wing", "WHAT IS DOWNFORCE?")
sc("""The Drive reported that Porsche claims the G T three R S produces over nine hundred pounds of downforce at about one hundred twenty-four miles per hour, and about one thousand eight hundred ninety-five pounds at one hundred seventy-seven miles per hour.""",
   "Porsche GT3 RS aero", "1,895 LB AT 177 MPH")
sc("""Hagerty reported that the Z06 with the Z zero seven package produces seven hundred thirty-four pounds of downforce at one hundred eighty-six miles per hour. The standard Z06 makes three hundred sixty-five. So at a lower speed, the Porsche makes more than two and a half times the downforce of the best-equipped Z06.""",
   "Corvette Z06 Z07 wing", "734 LB AT 186 MPH")
sc("""How does the Porsche do it? The Drive said its rear wing is so tall that the top edge sits above the roofline, a first for a production Porsche. And it was the first production Porsche with a drag reduction system, or D R S. Flaps on the front and rear wings open to cut drag on straights, then close for maximum grip in corners.""",
   "Porsche GT3 RS DRS wing", "FIRST PORSCHE WITH DRS")
sc("""D R S is a Formula One idea. In F1, drivers open a flap on the rear wing to go faster on the straights. Porsche brought that idea to a road car you can buy at a dealer. Round four, downforce, goes to the Porsche by a wide margin.""",
   "Formula One DRS", "ROUND 4: GT3 RS")

# ---------- 6. WHERE THE PORSCHE WINS: WEIGHT ----------
ch("Where the Porsche wins: weight")
sc("""Round five, weight. The Drive listed the G T three R S at three thousand two hundred sixty-eight pounds. It also reported that the lightest Z06, with the Z zero seven package, weighs three thousand four hundred thirty-four pounds. So the Porsche is about one hundred sixty-six pounds lighter.""",
   "Porsche 911 GT3 RS side", "3,268 LB vs 3,434 LB")
sc("""Weight affects everything on a track. Braking, cornering, and how quickly the tires overheat. A lighter car needs less grip to change direction. So even though the Corvette has more power, the Porsche has less mass to carry around every corner.""",
   "Porsche GT3 RS cornering", "LESS MASS, MORE AGILITY")
sc("""Here is how to think about it. Divide weight by horsepower. The Z06 Z zero seven carries about five point one pounds per horsepower. The G T three R S carries about six point three. So the Corvette has the better power-to-weight ratio on paper, which helps on the straights. But the Porsche's grip advantage is so large that it more than makes up for it in the corners. Round five, by pure weight, goes to the Porsche.""",
   "Porsche GT3 RS and Corvette Z06 track", "ROUND 5: GT3 RS")
sc("""Brakes are part of the weight story. The Drive reported that the Z06 uses Brembo brakes with six-piston front calipers on fourteen point six inch rotors, with optional carbon-ceramic brakes measuring fifteen point seven inches at the front. The Drive also said the G T three R S got larger six-piston brakes with slightly thicker rotors than the regular G T three. Both cars are built to stop again and again without fading.""",
   "Corvette Z06 Brembo brakes", "BIG BRAKES ON BOTH")
sc("""And the tires are enormous. The Drive reported that the Z06's rear tires are three hundred forty-five millimeters wide, made possible by a body three point six inches wider than the regular Stingray. Hagerty said standard tires are Michelin Pilot Sport four S, and the Z zero seven package uses even stickier Michelin Cup two R tires. The Corvette uses mechanical grip to fight the Porsche's aerodynamic grip.""",
   "Corvette Z06 rear tire", "345 MM REAR TIRES")

# ---------- 7. THE LAP TIME ----------
ch("The one number")
sc("""And now the one number that explains it all, the lap time at the Nürburgring Nordschleife, the twenty point eight kilometer German track that carmakers use as a benchmark. Motor1 reported that the G T three R S lapped it in six minutes forty-nine point three two eight seconds, driven by Porsche's Jörg Bergmeister.""",
   "Nürburgring Nordschleife", "GT3 RS: 6:49.328")
sc("""Top Gear reported that the Corvette Z06 lapped the same circuit in seven minutes eleven point eight two six seconds, driven by Aaron Link, in twenty twenty-five. That is about twenty-two and a half seconds slower than the Porsche.""",
   "Corvette Z06 Nürburgring", "Z06: 7:11.826")
sc("""Twenty-two seconds is a huge gap at the Nürburgring. Motor1 said the G T three R S was more than ten seconds faster than the regular nine eleven G T three, which lapped in six minutes fifty-nine point nine two seven. So the Z06 was not only slower than the G T three R S, it was also slower than the regular G T three.""",
   "Porsche 911 GT3", "SLOWER THAN THE GT3 TOO")
sc("""And this is where everything comes together. The Nordschleife has long, fast corners, where downforce matters enormously. The Porsche's extra downforce and lower weight beat the Corvette's extra power. On the straights, the Corvette can pull. In the fast corners, the Porsche is in another world. Round six, the lap time, goes to the Porsche.""",
   "Nürburgring fast corner", "ROUND 6: GT3 RS")
sc("""To be fair to Chevrolet, the Corvette family does have faster cars. Top Gear reported that on the same trip, the twin-turbo Z R one lapped in six minutes fifty point seven six three, and the hybrid Z R one X in six minutes forty-nine point two seven five. The Z R one X was actually about five hundredths of a second quicker than the G T three R S. But those cars have more than one thousand horsepower.""",
   "Corvette ZR1X", "ZR1X: 6:49.275")
sc("""And price brings us back to value. GM Authority listed the twenty twenty-six Z R one at about one hundred eighty-two thousand dollars, including destination. That is still less than the twenty twenty-three G T three R S starting price reported by The Drive. So Chevrolet can match the Porsche's lap time, but only by adding twin turbochargers and about four hundred more horsepower than the Z06.""",
   "Corvette ZR1 twin turbo", "ZR1: ~$182,395")

# ---------- 8. VALUE OVER TIME ----------
ch("Where the Porsche wins: value")
sc("""Round seven, and this one surprises people. What happens to your money after you buy? CarScoops reported in May twenty twenty-five that a twenty twenty-four G T three R S with about one thousand four hundred miles and an original sticker of about three hundred nine thousand dollars sold on Bring a Trailer for three hundred fifty-one thousand dollars. That is about forty-two thousand dollars above its sticker price.""",
   "Porsche 911 GT3 RS auction", "SOLD $41,700 OVER STICKER")
sc("""The Corvette went the other way. CarScoops reported a Z06 coupe with an original sticker of about one hundred forty-six thousand dollars and two thousand one hundred miles that sold for one hundred eighteen thousand, and a twenty twenty-five Z06 convertible with a sticker of about one hundred seventy thousand that sold for one hundred thirty-seven thousand five hundred. Both about twenty percent below sticker.""",
   "Corvette Z06 auction", "Z06: ~20% BELOW STICKER")
sc("""Why? Supply. Motorious reported in August twenty twenty-five that about one thousand seven hundred Z06s were sitting at American dealers, with discounts of up to twelve thousand dollars. Porsche builds the G T three R S in far smaller numbers, and buyers often struggle to get one at sticker price. Scarcity keeps values high.""",
   "Corvette dealer inventory", "1,700 Z06s UNSOLD")
sc("""And the market benchmark agrees. Classic dot com listed a market benchmark of about three hundred eighty-eight thousand dollars for the nine ninety-two G T three R S in twenty twenty-six. That is far above the original starting price. Round seven, value over time, goes to the Porsche.""",
   "Porsche 911 GT3 RS front", "ROUND 7: GT3 RS")
sc("""But here is the twist. That also means a used Z06 can be a bargain. If the original buyer lost twenty percent, the second buyer gets a hand-built, six hundred seventy horsepower car for much less money. For someone buying used, the Corvette's weakness becomes a strength.""",
   "used Corvette Z06", "THE USED BARGAIN")
sc("""There is one more cost to consider, reliability and recalls. In August twenty twenty-five, Auto123 reported a recall of about twenty-five thousand Corvettes, including twenty twenty-three to twenty twenty-five Z06 models, because fuel could spill onto the left radiator during refueling and create a fire risk. Sales were suspended while GM worked on a fix. News like that can also weigh on used prices.""",
   "Corvette Z06 fuel door", "THE 2025 RECALL")

# ---------- 9. THE INTERIOR AND FEEL ----------
ch("How they feel")
sc("""Inside, the two cars show their different priorities. The Drive reported that the G T three R S steering wheel has a D R S button plus four rotary dials to adjust things like suspension and traction, compared with one dial on the normal G T three. It is a cockpit built for adjusting the car lap after lap.""",
   "Porsche GT3 RS steering wheel", "4 DIALS ON THE WHEEL")
sc("""The Corvette uses its distinctive cockpit layout with a long row of controls on the center console, and a driver-focused design. Autoblog said its exhaust can be tuned through presets called Tour, Sport, and Track. The Z06 is designed to be comfortable on a road trip, then loud and sharp on a track day.""",
   "Corvette C8 interior", "TOUR, SPORT, TRACK")
sc("""And they sound different. The Corvette's flat-plane V8 screams to eight thousand six hundred r p m. The Porsche's flat-six howls to nine thousand. Both are among the last high-revving, naturally aspirated engines in the world, at a time when most rivals have switched to turbochargers or electric motors.""",
   "Porsche flat six engine", "8,600 vs 9,000 RPM")
sc("""Top speed is another difference. The Drive reported that the G T three R S reaches about one hundred eighty-four miles per hour, in seventh gear. All that downforce comes with drag, which limits top speed. That is the price of grip. The Porsche gives up some speed on the straights to gain huge speed in the corners.""",
   "Porsche GT3 RS high speed", "184 MPH: THE PRICE OF GRIP")
sc("""Both engines are also becoming rare in a wider sense. Many of today's fastest cars use turbochargers, hybrid systems, or both, including the Corvette Z R one X. The Z06 and the G T three R S are two of the few that still rely only on displacement, revs, and clever engineering. Whichever one you prefer, you are buying the end of an era.""",
   "Corvette Z06 and Porsche 911 GT3 RS parked", "THE END OF AN ERA")

# ---------- 10. VERDICT ----------
ch("The verdict")
sc("""So let's count the rounds. The Corvette Z06 wins acceleration, price, and daily life. The Porsche nine eleven G T three R S wins downforce, weight, the lap time, and value over time. Four rounds to three, for the Porsche.""",
   "Corvette Z06 and Porsche GT3 RS", "GT3 RS WINS 4-3")
sc("""But the real answer depends on what you want. If you want the fastest car around a race track, and a car that may hold its value, the G T three R S is the better tool, if you can afford it and can get one. If you want huge power, a convertible option, and space for luggage, at about half the price, the Z06 is the better deal.""",
   "Porsche GT3 RS on track", "WHAT DO YOU WANT?")
sc("""And here is the final twist. The difference nobody explains is not power. It is air. The Porsche was designed around downforce, and the Corvette was designed around its engine. That single choice explains the lap time, the price, the trunk, and even the resale value.""",
   "Porsche GT3 RS wing and Corvette Z06", "IT'S NOT POWER. IT'S AIR")
sc("""Which one would you pick? Tell us in the comments. In the other videos of this series, we reveal two things you didn't know about the Z06, we work out what it really costs to own one, and we tell the insane story behind the mid-engine Corvette.""",
   "Corvette Z06 Torch Red", "WHICH WOULD YOU PICK?")
sc("""If you are looking for something with a bed instead of a wing, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Corvette Z06 sunset", "SUBSCRIBE: PICKUP REALITY")

save("video74", "Why the Corvette Z06 Beats the 911 GT3 RS (And Where It Loses)", [
    "The Drive, 2023 Chevy Corvette Z06: 670 hp from a naturally aspirated flat-plane V8 (Oct 2021): https://www.thedrive.com/news/42882/2023-chevy-corvette-z06-670-hp-from-a-naturally-aspirated-flat-plane-v8",
    "The Drive, 2023 Porsche 911 GT3 RS specs, debut and price (Aug 2022): https://www.thedrive.com/news/2023-porsche-911-gt3rs-specs-debut-reveal-price.md",
    "Hagerty, 2023 Corvette Z06 arrives with world's most powerful naturally aspirated V-8: https://www.hagerty.com/media/?p=179871",
    "Autoblog, 2023 Chevy Corvette Z06: the 9 coolest things: https://www.autoblog.com/2022/02/18/2023-chevy-corvette-z06-coolest-9-things/",
    "Wikipedia, Chevrolet Corvette (C8): https://en.wikipedia.org/wiki/Chevrolet_Corvette_(C8)",
    "GM Authority, 2026 Corvette pricing uncovered: https://gmauthority.com/blog/2025/06/2026-corvette-pricing-uncovered/",
    "AP via WFYI, Corvette goes mid-engine for first time (July 2019): https://www.wfyi.org/news/articles/corvette-goes-mid-engine-for-first-time-to-raise-performance",
    "Motor Authority, The 2023 Corvette Z06 exists because of Zora Arkus-Duntov: https://www.motorauthority.com/news/1136291_the-2023-chevrolet-corvette-z06-exists-because-of-zora-arkus-duntov",
    "Racer, Corvette Racing takes final GTE victory at Le Mans (June 2023): https://racer.com/2023/06/11/corvette-racing-fights-through-to-take-final-gte-victory-at-le-mans/",
    "Auto123, Corvette Z06 and ZR1 recall (Aug 2025): https://www.auto123.com/en/news/chevrolet-corvette-recall-z06-zr1/73126",
    "Motor1, 2023 Porsche 911 GT3 RS laps the Nürburgring in 6:49.328: https://www.motor1.com/news/616069/porsche-911-gt3-rs-nurburgring-lap-record/",
    "Top Gear, Corvette ZR1X fastest American car around the Nürburgring (Aug 2025): https://www.topgear.com/car-news/usa/chevrolet-corvette-zr1x-fastest-american-car-ever-around-nurburgring",
    "CarScoops, This Porsche 911 GT3 RS sold for $40k profit after 1.4k miles (May 2025): https://www.carscoops.com/2025/05/this-porsche-911-gt3-rs-was-sold-for-40k-profit-after-1-4k-miles/",
    "CarScoops, Corvette Z06 prices crashing on the used market (Aug 2025): https://www.carscoops.com/2025/08/corvette-z06-prices-crashing-used-market-losses/",
    "CarScoops, Corvette Z06 flippers learn what happens when the hype fades (Oct 2025): https://www.carscoops.com/2025/10/corvette-z06-flippers-are-learning-the-hard-way-what-happens-when-the-hype-fades/",
    "Motorious, Over 1,700 Corvette Z06s sit unsold (Aug 2025): https://www.motorious.com/articles/news/dealers-offer-deep-discounts-as-over-1-700-chevrolet-corvette-z06s-sit-unsold",
    "CLASSIC.COM, Porsche 992.1 GT3 RS market benchmark: https://www.classic.com/m/porsche/911/992/9921/gt3-rs/standard/",
], "B")
