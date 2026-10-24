import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""The Lexus LFA has a V ten engine that revs from idle to its redline in point six of a second. That is so fast that the engineers could not use an ordinary needle for the tachometer. And that is only one of two things about this car that almost nobody knows. The other involves a machine, a loom, that Wikipedia says is one of only two of its kind in the world.""",
   "Lexus LFA", "2 THINGS YOU DIDN'T KNOW ABOUT THE LEXUS LFA")
sc("""Here is the twist. Toyota spent about ten years on this car, and Wikipedia says it built only five hundred. Today those five hundred cars sell for more than double what they cost new. But the two things we are going to show you have nothing to do with price. They are about how the car was made, and how it was tuned to sound.""",
   "Lexus LFA V10", "TEN YEARS OF WORK · 500 CARS BUILT")
sc("""Every figure in this video comes from published sources, listed in the description. Where sources disagree, we will say so. Where we do the maths ourselves, we will say that too.""",
   "Lexus LFA", "EVERY NUMBER IS SOURCED")

ch("A project that took a decade")
sc("""Wikipedia says the Lexus LFA, code-named T X S, began development in early two thousand. The first prototype was completed in June two thousand three, and testing at the Nürburgring started in October two thousand four. A first concept was shown at the Detroit auto show in January two thousand five, a second in January two thousand seven, and a roadster in January two thousand eight.""",
   "Lexus LFA concept", "DEVELOPMENT BEGAN IN EARLY 2000")
sc("""Production was confirmed by Akio Toyoda on the fifth of August two thousand nine, and the production car was unveiled at the Tokyo Motor Show on the twenty-first of October that year, for Lexus's twentieth anniversary. Orders opened two days later. Production began on the fifteenth of December two thousand ten, at the Motomachi plant in Toyota, Aichi.""",
   "Lexus LFA Tokyo Motor Show", "UNVEILED OCTOBER 2009 · PRODUCTION DECEMBER 2010")
sc("""By our own arithmetic, from the start of development in early two thousand to the start of production in December two thousand ten is about ten and a half years. Compare that with the Mercedes-AMG One, which took more than five years from its reveal to its first delivery.""",
   "Lexus LFA", "~10.5 YEARS FROM START TO PRODUCTION (OUR ARITHMETIC)")
sc("""Production was small and slow. Wikipedia says five hundred units were built, at twenty a month, from December two thousand ten to December two thousand twelve. The page gives two end dates, the seventeenth and the fourteenth of December two thousand twelve, so we say only that it ended in mid-December two thousand twelve. By our arithmetic, five hundred cars at twenty a month is twenty-five months.""",
   "Lexus LFA assembly", "500 CARS · 20 A MONTH · DEC 2010–DEC 2012")
sc("""The base price was three hundred seventy-five thousand dollars, or three hundred forty thousand pounds, according to Wikipedia. One article on a later sale says Lexus revealed a price of three-quarters of a million dollars at the two thousand ten launch, which conflicts with the other sources. We use three hundred seventy-five thousand, since both Wikipedia and Motor Authority give it.""",
   "Lexus LFA price", "$375,000 BASE · ONE SOURCE CLAIMS $750,000")

ch("Thing one: the engine too fast for a needle")
sc("""Now the first surprise. The engine is the one L R dash G U E, a four point eight litre V ten, four thousand, eight hundred five cubic centimetres, with a seventy-two degree bank angle. Wikipedia says it was co-developed with Yamaha. It makes four hundred twelve kilowatts, five hundred sixty metric horsepower, at eight thousand seven hundred r p m.""",
   "Lexus LFA V10 engine", "4.8 L V10 · 560 PS @ 8,700 RPM · WITH YAMAHA")
sc("""Torque is four hundred eighty newton-metres at six thousand eight hundred r p m, with ninety percent available from three thousand seven hundred. The redline is nine thousand r p m, and fuel cut-off comes at nine thousand five hundred. Those are high numbers for a road car, and they set up the surprise that follows.""",
   "Lexus LFA tachometer", "REDLINE 9,000 RPM · FUEL CUT-OFF 9,500 RPM")
sc("""Here it is. Wikipedia says the engine revs from idle to redline in point six seconds. That speed required a digital tachometer, because a mechanical needle could not keep up. Think about that: the car's engineers designed an instrument display around the engine, because the engine was faster than the ordinary part that normally shows what it is doing.""",
   "Lexus LFA digital tachometer", "IDLE TO REDLINE IN 0.6 SECONDS")
sc("""By our own arithmetic, nine thousand r p m minus an idle of about one thousand is roughly eight thousand r p m in point six seconds. That is more than thirteen thousand r p m every second. We use an assumed idle of one thousand r p m for this sum, which is our own assumption, since the source does not say. The point is only the scale of the speed.""",
   "Lexus LFA engine", "~13,000 RPM PER SECOND (OUR ARITHMETIC, ASSUMED IDLE)")
sc("""Why does it matter to you? Because a driver who blips the throttle sees the revs jump so quickly that an analogue needle would lag behind. A digital display solves that. It is a small piece of engineering that tells you how extreme the engine is. The car was designed from the start around the V ten, not the other way round.""",
   "Lexus LFA cockpit", "THE DISPLAY WAS DESIGNED AROUND THE ENGINE (OUR READING)")
sc("""The engine's sound was also designed. Wikipedia says Toyota engineers called it the roar of an angel. Two octaves of engine sound are channelled into the cabin, tuned in the manner of an Ovation guitar. So the car's sound is not an accident of the exhaust. It was shaped by acoustic design, with help from Yamaha, which also makes musical instruments.""",
   "Lexus LFA sound", "TUNED LIKE AN OVATION GUITAR · \"ROAR OF AN ANGEL\"")
sc("""A note of caution. The Yamaha co-development is on the page. The link between Yamaha's instruments and the tuning is our observation, not a statement from the source. What the page does say is that two octaves are channelled into the cabin. That is the verifiable part, and it is already more attention to sound than most cars receive.""",
   "Yamaha", "YAMAHA CO-DEVELOPED THE ENGINE (WIKIPEDIA)")
sc("""Performance, per Wikipedia. Zero to sixty miles per hour in three point six seconds, officially without launch control, and three point seven to a hundred kilometres per hour. Top speed three hundred twenty-five kilometres per hour on one line and three hundred twenty-six on another. A quarter mile in eleven point six seconds at about two hundred kilometres per hour, from Insideline.""",
   "Lexus LFA acceleration", "0–60: 3.6 S · TOP SPEED ~325 KM/H · 1/4 MILE 11.6 S")

ch("Thing two: the loom")
sc("""The second surprise is the body. Wikipedia says carbon fibre reinforced plastic makes up sixty-five percent of the body mass, with the rest aluminium. The manufacturer says the carbon saves one hundred kilograms compared with aluminium. So two thirds of the car's body is a material most cars use for small trim pieces.""",
   "Lexus LFA carbon fibre", "65% OF BODY MASS IS CARBON FIBRE")
sc("""And here is the unusual part. The page says the carbon fibre is woven on a laser-monitored circular loom, one of only two in the world. In other words, the machine used to make the car's structure is almost unique. Few companies could build the car without it, and the page tells us that the process required a machine of that rarity.""",
   "Carbon fibre loom", "A LASER-MONITORED CIRCULAR LOOM · ONE OF ONLY TWO")
sc("""The page does not say who owns the other loom, so we will not guess. It also does not give the cost of the machine or the time it took to weave. What it gives is the key fact, that the carbon structure of a Lexus was woven on a machine with a single peer. That is a long way from a typical car factory.""",
   "Carbon fibre weaving", "THE OTHER LOOM: NOT IDENTIFIED IN OUR SOURCE")
sc("""Now the weight. Wikipedia gives two numbers for the same car, a kerb weight of one thousand, five hundred eighty kilograms in the infobox and one thousand, four hundred eighty in the specification table. The page is inconsistent, a one hundred kilogram gap. By our arithmetic that is about six percent. We cannot say which is right, so we use the range.""",
   "Lexus LFA weight", "WEIGHT: 1,580 KG (INFOBOX) VS 1,480 KG (TABLE)")
sc("""Using the page's own weight to power ratio of two point six seven kilograms per horsepower, the sum is consistent with the heavier weight. Five hundred fifty-three horsepower times two point six seven is about one thousand, four hundred seventy-seven. That points to the lower weight, one thousand, four hundred eighty. So the specification table, not the infobox, matches the page's own ratio.""",
   "Lexus LFA", "PAGE'S OWN RATIO FAVOURS ~1,480 KG (OUR ARITHMETIC)")
sc("""Whichever number is right, the car is light. The Mercedes-AMG One, a hybrid hypercar, is listed at one thousand, six hundred ninety-five. The LFA's carbon structure is a large part of the difference, though the sources do not break it down exactly.""",
   "Lexus LFA", "LIGHTER THAN A MODERN HYBRID HYPERCAR")

ch("How the loom works")
sc("""The Lexus UK magazine explains the loom in detail. It says Lexus engineers created it while building the LFA's carbon fibre body and chassis. Toyota has roots in weaving, the article notes, and its automatic loom helped fund the company's entry into car manufacturing in nineteen thirty-six. So a weaving machine was the origin of Toyota, and it came back for the LFA.""",
   "Toyota automatic loom", "TOYOTA'S FIRST FORTUNE CAME FROM A LOOM")
sc("""Why build a loom at all? The article says conventional methods mould layered woven carbon sheet around a form, which leaves a seam that can become a weak point. The new machine weaves individual strands of carbon yarn directly around a form, producing a three-dimensional part with no seam. Its example is the roof pillar of the LFA.""",
   "Carbon fibre weave", "NO SEAM: THE WEAK POINT OF CONVENTIONAL CARBON")
sc("""The machine uses a hundred forty-four bobbins mounted around the inner edge of a rotary loom, their movements synchronised under laser control. The roof pillar is built in twelve woven layers. By our own arithmetic, twelve layers each woven from a hundred forty-four strands means the process is anything but simple, although the article does not give the weaving time.""",
   "Rotary carbon loom", "144 BOBBINS · LASER-SYNCHRONISED · 12 LAYERS")
sc("""The article calls the finished roof pillar one of the strongest and thinnest ever produced. That is a manufacturer's magazine describing its own part, so we treat it as a claim rather than a measurement. It also says the loom has since been displayed at the Design Museum in London, which recognised its contribution to future manufacturing methods.""",
   "Design Museum London", "LOOM DISPLAYED AT LONDON'S DESIGN MUSEUM")
sc("""Note the small difference between sources. Wikipedia says the loom is one of only two in the world. The Lexus article does not repeat that claim, and does not name any other machine. We therefore report the Wikipedia statement as stated, and add that the Lexus article describes the loom without comparing it with anything else.""",
   "Carbon fibre factory", "\"ONE OF ONLY TWO\" IS WIKIPEDIA'S CLAIM, NOT LEXUS'S")
sc("""What does this mean in practice? That the shape of the LFA's carbon structure came from a manufacturing choice. Where other makers laid sheets of cloth into moulds, Lexus wove the part. It is the kind of decision that adds cost and time, and Wikipedia's ten year development timeline is consistent with the idea that the team had to invent its own tools.""",
   "Lexus LFA structure", "INVENTING THE TOOLS TAKES TIME (OUR READING)")

ch("Some more arithmetic on the five hundred")
sc("""Let us run some numbers on the production run, all our own arithmetic from Wikipedia's figures. Five hundred cars in total. Sixty-four of them were Nürburgring Package cars, which is about thirteen percent. One hundred fifty North American cars were first sold on a two-year lease, which is thirty percent of the total.""",
   "Lexus LFA production", "64 N-PACKAGE = 12.8% · 150 LEASED = 30% (OUR ARITHMETIC)")
sc("""In Europe, Wikipedia says thirty-eight LFAs had been sold as of September two thousand twenty. By our arithmetic, that is just under eight percent of production. Motor Authority adds that fewer than two hundred were imported to the United States, although it says sources differ on the exact count. Put the figures side by side and they do not add up to five hundred, because the sources cover different things.""",
   "Lexus LFA Europe", "38 IN EUROPE · FEWER THAN 200 IMPORTED TO THE US")
sc("""That is a useful reminder. Different sources count different things, such as cars sold, cars leased, cars imported and cars built. We do not have a full breakdown of where all five hundred went, and we will not invent one. What the sources do agree on is the total, five hundred, and that the cars were hand-assembled at twenty a month.""",
   "Lexus LFA", "THE SOURCES COUNT DIFFERENT THINGS")
sc("""Price per horsepower, our arithmetic again. Three hundred seventy-five thousand dollars divided by five hundred fifty-three horsepower is about six hundred seventy-eight dollars per horsepower. At the eight hundred forty-five thousand dollar auction price, it is about fifteen hundred twenty-eight dollars. The same car, with the same horsepower, now costs more than two and a quarter times as much per unit of power.""",
   "Lexus LFA price per horsepower", "$678/HP NEW → $1,528/HP AT THE 2022 AUCTION (OUR ARITHMETIC)")
sc("""And the performance has not changed. The car still does zero to sixty in three point six seconds according to the official figure, and still revs to nine thousand. What changed is scarcity, and what people are willing to pay for the sound and the story. We will leave the question of whether that is rational to the economists.""",
   "Lexus LFA", "THE CAR DIDN'T CHANGE · THE MARKET DID")

ch("The track version")
sc("""There was a more extreme LFA. The Nürburgring Package, Wikipedia says, produces four hundred twenty kilowatts, five hundred seventy-one metric horsepower. Lexus planned a run of fifty units, but sixty-four were built. In September two thousand eleven, Lexus confirmed a lap of seven minutes, fourteen point six four seconds, with a top speed of two hundred ninety-eight kilometres per hour.""",
   "Lexus LFA Nürburgring Package", "NÜRBURGRING PACKAGE: 571 PS · 64 BUILT (50 PLANNED)")
sc("""Earlier, in June two thousand eleven, Akira Iida set a time of seven twenty-two point eight five in a test for a warm-up video. By our arithmetic, the later confirmed lap was about eight seconds faster. Both are on Wikipedia, and both are presented as manufacturer times, so treat them as claims rather than independent measurements.""",
   "Nürburgring Nordschleife", "7:22.85 (JUNE 2011) → 7:14.64 (SEPT 2011)")
sc("""The car also raced. Wikipedia says the number fifteen car in the two thousand nine twenty-four hours race finished with a driveshaft failure and a fire. In twenty ten, the number fifty car won its class, S P eight, finishing eighteenth overall after one hundred forty-two laps. So the car's engine and structure were tested in a famous endurance race.""",
   "Nürburgring 24 Hours", "2010: CLASS WIN AT THE NÜRBURGRING 24H (18TH OVERALL)")

ch("The engine in numbers")
sc("""Some arithmetic on the V ten, all ours, from Wikipedia's figures. Five hundred sixty metric horsepower from four point eight litres is about one hundred seventeen horsepower per litre. That is a naturally aspirated figure, with no turbochargers. Compare it with the Ferrari Purosangue's V twelve, which makes about one hundred twelve per litre, as we calculated in another video of this series.""",
   "Lexus LFA V10", "~117 PS PER LITRE · NO TURBOS (OUR ARITHMETIC)")
sc("""The engine's character is in its torque curve. Ninety percent of the four hundred eighty newton-metres is available from three thousand seven hundred r p m, and the peak comes at six thousand eight hundred, while power peaks at eight thousand seven hundred. By our arithmetic, the engine delivers its maximum power only about three hundred r p m below the redline of nine thousand. It wants to be revved.""",
   "Lexus LFA engine", "POWER PEAK 8,700 · REDLINE 9,000 (SPREAD: 300 RPM)")
sc("""The weight to power ratio on Wikipedia is two point six seven kilograms per horsepower. By our arithmetic, that is about three hundred seventy-five horsepower per tonne. The figure sounds ordinary today, when hybrid hypercars list a thousand horsepower. But the LFA reached it with a naturally aspirated engine, in two thousand ten, and with a body mostly of carbon.""",
   "Lexus LFA", "~375 HP PER TONNE (OUR ARITHMETIC)")
sc("""Let us also put the testing history in order. The first prototype was completed in June two thousand three. Nürburgring testing began in October two thousand four. The Nürburgring Package lap was confirmed in September two thousand eleven. By our arithmetic, that is almost seven years between the start of testing on that track and the confirmed lap, which says something about how much work went into the car.""",
   "Nürburgring Nordschleife", "NÜRBURGRING: TESTS FROM 2004 · LAP CONFIRMED 2011")
sc("""One more detail. Wikipedia says the Nürburgring Package had a top speed of two hundred ninety-eight kilometres per hour, lower than the standard car's three hundred twenty-five. That is because the package adds aerodynamic parts that create downforce, which also add drag. A track car is not simply a faster road car. It is a different compromise, and the numbers show it.""",
   "Lexus LFA aerodynamics", "N-PACKAGE TOP SPEED 298 KM/H VS 325 KM/H STANDARD")
sc("""So here is what we have shown. A V ten that revs faster than a needle can follow, tuned for sound. A body woven on a loom built for the purpose. A development that took more than ten years, for five hundred cars. And a price that has more than doubled since. None of it is a guess. Each fact is attributed to a source, and where we did arithmetic, we said so.""",
   "Lexus LFA", "RECAP: ENGINE · LOOM · TEN YEARS · 500 CARS")

ch("Who bought it, and what it is worth now")
sc("""The sales story is unusual. Wikipedia says one hundred fifty North American cars were initially sold through a two-year lease. And as of September two thousand twenty, thirty-eight LFAs had been sold in Europe. The final LFA was sold in June two thousand twenty-three, an Australian dealer's display car, at a price the page does not disclose.""",
   "Lexus dealership", "150 N. AMERICAN CARS LEASED · FINAL CAR SOLD JUNE 2023")
sc("""By our arithmetic, that final sale came more than ten years after production ended in December two thousand twelve. A new car, sold ten and a half years after it was made. That tells you how slowly the last cars moved at the original price, and how the story changed afterwards.""",
   "Lexus LFA", "LAST CAR SOLD 10+ YEARS AFTER PRODUCTION ENDED")
sc("""What are they worth now? Motor Authority reported in July two thousand twenty-one that a Pearl Yellow two thousand twelve LFA with seventy-two miles sold for eight hundred eight thousand dollars on Bring a Trailer. That is four hundred thirty-three thousand dollars over its three hundred seventy-five thousand dollar sticker price. By our arithmetic, a markup of about one hundred fifteen percent.""",
   "Lexus LFA Pearl Yellow", "2021: $808,000 FOR A 72-MILE CAR (+115% OVER STICKER)")
sc("""The same article mentions a silver LFA that sold for seven hundred twenty thousand dollars earlier in twenty twenty-one. And Supercar Blondie reported that a white two thousand twelve LFA with eight hundred fifty miles sold on Bring a Trailer for eight hundred forty-five thousand dollars in April twenty twenty-two. By our arithmetic, that is a markup of about one hundred twenty-five percent over the sticker price.""",
   "Lexus LFA auction", "2022: $845,000 · 850 MILES · CHASSIS 235 OF 500")
sc("""These are single auction results, not a market index, and the cars differ in mileage and condition. But they point the same way. We will look at the value story in more detail in another video of this series. For this one, the lesson is that a car from a long project turned into one of the most sought-after Japanese cars of its generation.""",
   "Lexus LFA", "SINGLE AUCTIONS, NOT AN INDEX")

ch("What the two surprises tell you")
sc("""Put the two surprises together. The engine was so fast that the instrument display had to be redesigned. The body was woven on a machine with a single peer. Both are signs of a company that solved every problem from first principles, rather than borrowing parts from other cars. That approach is why the project took ten years, and why it could not be repeated cheaply.""",
   "Lexus LFA", "EVERY PROBLEM SOLVED FROM FIRST PRINCIPLES (OUR READING)")
sc("""Akio Toyoda confirmed production on the fifth of August two thousand nine. Wikipedia presents the car as a showpiece for the twentieth anniversary of Lexus. The car was not meant to make money. It was meant to show what the company could do, and the sources we used do not give a profit figure, so we make no claim about one.""",
   "Akio Toyoda", "A SHOWPIECE FOR LEXUS'S 20TH ANNIVERSARY")
sc("""One last caution. We have not driven an LFA. Every figure is from published sources, some of which disagree with each other, such as the weight and the original price. Where we did arithmetic, we said so. If you have a verified detail we missed, tell us in the comments, with where it comes from.""",
   "Lexus LFA", "WEIGHT AND PRICE: SOURCES DISAGREE")
sc("""Which surprise stayed with you more, the point six second needle problem, or the loom? Tell us in the comments. In the other videos of this series, we compare the LFA with the Nissan GT-R, explain why it is worth more now than new, and tell the story behind the car. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video105", "2 Things You Didn't Know About the Lexus LFA", [
    "Wikipedia, Lexus LFA: https://en.wikipedia.org/wiki/Lexus_LFA",
    "Lexus UK Magazine, Engineering innovations: the Lexus carbon loom: https://mag.lexus.co.uk/engineering-innovations-the-lexus-carbon-loom",
    "Motor Authority, Pearl Yellow 2012 Lexus LFA with 72 miles sells for $808,000 on Bring a Trailer (7 July 2021): https://www.motorauthority.com/news/1132702_pearl-yellow-2012-lexus-lfa-with-72-miles-sells-for-808-000-on-bring-a-trailer",
    "Supercar Blondie, Super rare Lexus LFA sells for massive $845k at auction (25 April 2022): https://supercarblondie.com/cars/lexus-lfa-850-miles-sells-845k/",
], "A")
