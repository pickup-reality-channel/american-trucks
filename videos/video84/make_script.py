import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In nineteen eighty-eight, four men sat at an airport in Italy, and one of them started sketching a car. McLaren had never built a road car. The sketch showed a three-seater with the driver in the middle. Four years later, that sketch became the McLaren F one, one of the most famous cars ever made. This is the insane story behind it, and it starts with a boy from South Africa.""",
   "McLaren F1", "THE INSANE STORY BEHIND THE McLAREN F1")
sc("""Here is the twist. The man who designed the F one had already shocked the racing world once, with a Formula One car that won its only race and was then withdrawn. And decades later, he would list everything he disliked about the F one, and build a new car to fix it.""",
   "Gordon Murray", "HE LISTED WHAT HE HATED ABOUT HIS OWN CAR")
sc("""Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. And there is one disagreement right at the start, about where that airport actually was.""",
   "McLaren F1 prototype", "EVERY FACT IS SOURCED")

# ---------- 1. DURBAN ----------
ch("A boy from Durban")
sc("""Wikipedia says Ian Gordon Murray was born on the eighteenth of June, nineteen forty-six, in Durban, South Africa. His parents were Scottish immigrants. His father raced motorcycles and later prepared racing cars. So Murray grew up around engines, in a family where racing was normal.""",
   "Durban South Africa", "BORN 1946, DURBAN")
sc("""He studied mechanical engineering at what is now the Durban University of Technology. Then, Wikipedia says, he moved to England in nineteen sixty-nine, hoping to join Lotus. Instead, after meeting designer Ron Tauranac, he was offered a job at Brabham.""",
   "Lotus Formula One 1969", "1969: TO ENGLAND, HOPING FOR LOTUS")
sc("""At Brabham, Murray rose quickly. Wikipedia says Bernie Ecclestone later made him chief designer. So by the nineteen seventies, a young South African engineer was designing Formula One cars for one of the sport's most famous teams. And he was about to build one of the most controversial.""",
   "Brabham Formula One car", "CHIEF DESIGNER AT BRABHAM")

# ---------- 2. THE FAN CAR ----------
ch("The fan car")
sc("""Wikipedia says that in mid-nineteen seventy-seven, Murray started work on the ambitious design of the Brabham B T forty-six. It was intended to compensate for the weight of its engine and fuel, and to let the team take a large technical step forward. The engine was an Alfa Romeo flat twelve.""",
   "Brabham BT46", "1977: THE BT46 PROJECT")
sc("""The page says the flat twelve was a three-liter engine, and produced about five hundred twenty brake horsepower at twelve thousand r p m in nineteen seventy-eight, about fifty more than the Cosworth engines most teams used. But it came with a cost. It was larger, used more fuel and oil, and weighed about forty kilograms more.""",
   "Alfa Romeo flat-12 engine", "ALFA ROMEO FLAT-12: ~520 HP")
sc("""Wikipedia says Murray realized the flat twelve was too wide to permit the tunnels needed for really significant ground effect. At Murray's instigation, Alfa went on to produce a V twelve engine for nineteen seventy-nine. In our reading, the fan car was a way of getting downforce another way.""",
   "Lotus 79 ground effect", "TOO WIDE FOR GROUND EFFECT")
sc("""Murray then found a radical idea. Wikipedia says his design used a complex series of clutches running from the engine to a large single fan. The faster the engine ran, the stronger the suction effect. Sliding skirts sealed the gap between the car and the ground. The car could be seen to squat on its suspension as downforce increased.""",
   "Brabham BT46B fan car", "A FAN THAT SUCKED THE CAR TO THE ROAD")
sc("""The team argued the fan was for cooling. Wikipedia says that using a fan to assist cooling was legal, while rules banned moveable aerodynamic devices. The team claimed cooling was the primary effect, and the claim gained some legitimacy because the car had cooling problems. The page says the original B T forty-six had only about thirty percent of the cooling surface required.""",
   "Brabham BT46B rear fan", "\"IT'S FOR COOLING\"")
sc("""The car raced once. Wikipedia says the two modified cars were prepared for the Swedish Grand Prix at Anderstorp on the seventeenth of June, nineteen seventy-eight. They qualified second and third behind the championship leader, Mario Andretti. In the race, John Watson spun off on lap nineteen. And Niki Lauda won.""",
   "Anderstorp Swedish Grand Prix 1978", "SWEDEN, 17 JUNE 1978")
sc("""The page says Lauda won by over half a minute from Riccardo Patrese, passing Andretti around the outside of a corner. After another driver dropped oil, the Brabham was in a class of its own, seemingly unaffected by the slippery surface. The fan car had won its first race.""",
   "Niki Lauda Brabham", "LAUDA WON BY OVER 30 SECONDS")
sc("""Andretti was not happy. Wikipedia quotes him saying it was like a bloody great vacuum cleaner. Murray disputed that it threw debris. He said the fan could not spit anything out the back because the fan's exit speed was only fifty-five miles per hour, and that the radial fan would have sent any stones flying sideways.""",
   "Mario Andretti 1978", "ANDRETTI: \"A GREAT VACUUM CLEANER\"")
sc("""The win stood, because the car was not considered illegal when it raced. But the page says Brabham withdrew it after one race, even though the F I A had ruled it could be used. The reason was concern from team owner Bernie Ecclestone that upset from other teams could collapse their association, FOCA.""",
   "Bernie Ecclestone 1978", "WITHDRAWN AFTER ONE RACE")
sc("""Wikipedia says the heads of the other FOCA teams, led by Colin Chapman, threatened to withdraw their support for Ecclestone unless he pulled the fan car. A deal was reached for Brabham to withdraw it voluntarily after three more races, but the sport's governing body then banned fan cars. It never raced again in Formula One.""",
   "Colin Chapman", "COLIN CHAPMAN LED THE REVOLT")
sc("""Lauda was not sentimental about it. Wikipedia says that when he accelerated through corners, the car would stick to the road as if it were on rails, which exposed him to very high lateral acceleration. He later called it unpleasant to drive, because of the lateral loads and reliance on aerodynamics over driver skill.""",
   "Niki Lauda", "\"UNPLEASANT TO DRIVE\"")
sc("""Remember the fan. Because it comes back later in this story. For now, the point is this. Gordon Murray had already built a car so effective that it was banned after winning its only race. And the next chapter of his career would put that creativity into a very different kind of machine.""",
   "Brabham BT46B", "THE FAN WILL RETURN")
sc("""There is an odd footnote. Wikipedia says that in nineteen seventy-nine, a B T forty-six ran in fan-car specification once again, at the Gunnar Nilsson Trophy. It was not an F I A event, so the car's illegality was not a factor. The race was a time trial, and Nelson Piquet finished fourth of five cars.""",
   "Nelson Piquet 1979", "A SECOND LIFE: THE 1979 TROPHY")

# ---------- 3. MCLAREN ----------
ch("Murray joins McLaren")
sc("""Wikipedia says that in nineteen eighty-six, Murray received an offer from Ron Dennis to join McLaren as technical director. McLaren was one of the top teams in Formula One. Murray moved from Brabham, and his career would be tied to McLaren for nearly two decades.""",
   "Ron Dennis", "1986: RON DENNIS CALLS")
sc("""And then came the airport. Here is the disagreement. Wikipedia says Murray sketched a three-seater sports car in nineteen eighty-eight while waiting for a flight home from the Italian Grand Prix, and proposed it to Ron Dennis. A longer account by Attic Capital says the meeting took place at Linate Airport in Milan.""",
   "Linate Airport Milan", "1988: THE AIRPORT")
sc("""Attic Capital says Ron Dennis, Mansour Ojjeh, Creighton Brown and Gordon Murray were all sitting at Linate Airport in nineteen eighty-eight. They discussed creating the ultimate road car, but it seemed like a huge leap, because McLaren had never built a road car before. The idea started growing in each of their minds.""",
   "airport lounge 1988", "FOUR MEN, ONE IDEA")
sc("""Ojjeh asked a simple question, according to the same account. Why do I have to go to Italy to buy a supercar? And Dennis later said the simple truth is that all four of them that day were essentially car nuts. He said he appreciated being associated with an achievement of which one could be proud.""",
   "Mansour Ojjeh", "\"WHY DO I HAVE TO GO TO ITALY?\"")
sc("""What Murray proposed was not new to him. Attic Capital says that in college, he had doodled a three-seat sports car, with one driver in the middle and two passengers slightly behind. That one-plus-two layout was the proposal. His notebook held a four-page goal summary, and the design proposal was handwritten on graph paper.""",
   "McLaren F1 sketch", "HANDWRITTEN ON GRAPH PAPER")
sc("""Murray's notes specified a three and a half liter, naturally aspirated engine derived from a Formula One engine, not turbocharged. They demanded the car be stunning from all angles, and that quality be instilled in staff from day one. The stated goal was, quite simply, the world's best car.""",
   "McLaren F1 design notes", "GOAL: \"THE WORLD'S BEST CAR\"")
sc("""Before designing, Murray tested rival supercars and made notes on what he disliked, an exercise he called an exorcism. The Honda N S X became his benchmark after a test-track visit. And he treated road car regulation as freedom. He said it was fantastic, because in effect, there was not any.""",
   "Honda NSX", "AN \"EXORCISM\" OF RIVAL CARS")
sc("""Dennis summed up the ambition. Attic Capital quotes him saying the goal was not only the finest sports car the world had ever seen, but also the finest sports car the world was ever going to see. That is quite a promise, for a company that had never built a road car.""",
   "Ron Dennis McLaren F1", "\"THE FINEST THE WORLD WOULD EVER SEE\"")
sc("""Gooding and Company says that Murray presented his ideas to McLaren's joint owners, Ron Dennis and Creighton Brown, who were agreeable and set up McLaren Cars in nineteen eighty-nine. Motor Authority says the team that was to create the F one came together for the first time in nineteen ninety, and two years later the car launched.""",
   "McLaren Cars Woking", "1989: McLAREN CARS IS BORN")

# ---------- 4. DESIGN ----------
ch("Designing the F1")
sc("""Motor Authority published photos of the original clay models. It says the exterior could have been significantly different. The headlight design, it says, is much better on the production car than on the clay model, and one clay model has a roof-mounted scoop that resembles the one on the later McLaren P one.""",
   "McLaren F1 clay model", "THE CLAY MODELS")
sc("""The final exterior came from Peter Stevens, Gooding and Company says. It describes a design simpler and more elegant than most supercars of its era. And Wikipedia says Murray's design concept was a common one among designers of high-performance cars, low weight and high power, pursued to an extreme.""",
   "Peter Stevens designer", "DESIGNED BY PETER STEVENS")
sc("""Then came the engine problem. Gooding and Company says McLaren's Formula One cars used Honda engines in the late eighties, but Honda would not build an engine for the road car. Murray had to shop around, eventually finding a collaborator in BMW's motorsport division, which built a six point one liter V twelve.""",
   "McLaren Honda engine", "HONDA SAID NO. BMW SAID YES.")
sc("""Wikipedia says the engine made six hundred eighteen horsepower, and that it was designed by BMW M under Paul Rosche. Gooding and Company says the original goal was five hundred fifty horsepower, and the engine delivered six hundred twenty-seven metric horsepower without further tuning. Murray's non-negotiable was that it be naturally aspirated.""",
   "BMW S70/2 V12 engine", "618 HP: MORE THAN PLANNED")
sc("""Murray's chassis was carbon fiber. Gooding and Company says it was the first road car with a full carbon fiber chassis, with titanium, magnesium and Kevlar in other areas. And the engine bay was lined with gold foil, which Wikipedia says used approximately sixteen grams of gold per car.""",
   "McLaren F1 carbon chassis", "FIRST FULL CARBON ROAD CAR")
sc("""And there was the driving position. Wikipedia says the driver's seat is in the middle of the car, ahead of the fuel tank and the engine. Gooding and Company points out that Ferrari's Tre Posti three sixty-five P of nineteen sixty-six used a similar layout, but that was a coachbuilt special, not a production car.""",
   "McLaren F1 interior", "THE CENTRAL SEAT")
sc("""Count the years. From the airport meeting in nineteen eighty-eight to the launch of the car in nineteen ninety-two is four years, by our own arithmetic. From the day Murray arrived in England in nineteen sixty-nine to that launch is twenty-three years. The F one was not a sudden idea. It was the result of a lifetime of engineering.""",
   "McLaren F1 launch 1992", "4 YEARS FROM SKETCH TO LAUNCH")
sc("""Then there was the test. Wikipedia says a test driver, wearing just shorts and a T-shirt, hit a rock and rolled the first prototype several times. The car survived well enough to continue the program. That crash was an early sign of how strong the carbon structure was.""",
   "McLaren F1 prototype crash test", "THE PROTOTYPE THAT ROLLED")
sc("""Production began in nineteen ninety-two, Gooding and Company says, with the first cars reaching customers in nineteen ninety-three, at a starting price of five hundred forty thousand pounds. It also says it is alleged that McLaren lost money on the F one project. In total, one hundred six cars were manufactured.""",
   "McLaren F1 production line", "106 CARS BUILT")

# ---------- 5. THE RACE CAR ----------
ch("The race car he did not want")
sc("""Here is a twist. Wikipedia's page on the T fifty says Murray intended the F one as a road car, was forced to race it, and found it a pain to do so. And the page on the F one GTR says Murray originally saw it as the ultimate road car, with no intention of racing it.""",
   "McLaren F1 GTR", "HE NEVER WANTED TO RACE IT")
sc("""The racing version was not a gentle conversion. Wikipedia says the bodywork gained cooling ducts, a large central nose duct and a large adjustable rear wing, and that even the nineteen ninety-five version generated enough downforce to run along the ceiling at one hundred miles per hour. The interior was stripped and given a full racing cage.""",
   "McLaren F1 GTR bodywork", "DOWNFORCE TO DRIVE ON THE CEILING")
sc("""But racers kept asking. The page says Le Mans winner John Nielsen turned to Murray to convince him to offer factory backing, and finally Murray relented and agreed to modify the F one into a racing car. Motor Sport adds that it was Ron Dennis who first wanted to race his F one.""",
   "John Nielsen Le Mans", "MURRAY RELENTED")
sc("""In June nineteen ninety-five, the F one GTR won the twenty-four hours of Le Mans at its first attempt. Wikipedia says it was one of the wettest races in the event's history, with about seventeen hours of steady rain, and the McLarens filled four of the first five places. It was the last road-legal, series-produced sports car to win the race outright.""",
   "McLaren F1 GTR Le Mans 1995", "LE MANS 1995: FIRST ATTEMPT, FIRST WIN")

# ---------- 6. THE RECORD ----------
ch("The record")
sc("""Three years later, the F one set its famous record. Wikipedia says that on the thirty-first of March, nineteen ninety-eight, Andy Wallace drove the five-year-old XP five prototype at Volkswagen's test track at Ehra-Lessien. The independently measured two-way average was two hundred forty point one miles per hour.""",
   "Ehra-Lessien test track", "MARCH 31, 1998: 240.1 MPH")
sc("""McLaren measured a peak of two hundred forty-three miles per hour, with the rev limiter raised to eight thousand three hundred r p m. And Gooding and Company says the car held the record for the world's fastest production car from nineteen ninety-eight to two thousand five.""",
   "McLaren F1 speed record", "HELD THE RECORD UNTIL 2005")

# ---------- 7. THE LIST ----------
ch("What Murray did next")
sc("""Murray led McLaren Cars from nineteen ninety-one to two thousand four, Wikipedia says. In two thousand seven he established a consultancy, Gordon Murray Design. Later came the T twenty-five city car, announced as smaller than a Smart Fortwo, and the electric T twenty-seven, developed with Zytek in two thousand nine.""",
   "Gordon Murray Design T.25", "GORDON MURRAY DESIGN, 2007")
sc("""In two thousand seventeen, Wikipedia says, he founded Gordon Murray Automotive, a low-volume car company. And in August two thousand twenty, it announced the T fifty. The page calls it the logical successor to the F one, and says it uses the fan car concept from the Brabham B T forty-six B.""",
   "Gordon Murray Automotive T.50", "THE T.50: THE FAN RETURNS")
sc("""The T fifty page says Murray's own list of what he disliked about the F one stuck in his head. The spine is fifty millimeters too wide. The headlamps are like glow worms in a jar. The air conditioning was hopeless, and the brakes squeak. The clutch needs adjusting every five thousand miles, and loading luggage in the lockers was a pain.""",
   "Gordon Murray T.50", "\"THE HEADLAMPS ARE LIKE GLOW WORMS IN A JAR\"")
sc("""So the T fifty fixes the list. Wikipedia says it has a naturally aspirated Cosworth V twelve of three thousand nine hundred ninety-four cubic centimeters, making six hundred fifty-four horsepower at eleven thousand five hundred r p m, with a redline of twelve thousand one hundred. Dry weight is nine hundred ninety-seven kilograms.""",
   "Cosworth V12 engine", "T.50: 12,100 RPM, 997 KG")
sc("""It keeps the F one's layout. The page says it has a central driving position with two passenger seats flanking the driver. And it has the fan. Wikipedia says an eight and a half kilowatt, forty centimeter aerodynamic fan is integrated into the rear, inspired by the Brabham fan car of nineteen seventy-eight.""",
   "Gordon Murray T.50 fan", "A FAN FROM 1978, ON A 2020s CAR")
sc("""The numbers show how Murray pushed his own idea. Wikipedia lists the T fifty at nine hundred ninety-seven kilograms dry, against eleven hundred forty for the F one. That is one hundred forty-three kilograms lighter, about twelve and a half percent, by our own arithmetic. Power is six hundred fifty-four horsepower against six hundred eighteen, about six percent more.""",
   "McLaren F1 and T.50", "T.50 IS 143 KG LIGHTER (OUR MATH)")
sc("""And the engine turns much faster. The T fifty's redline is twelve thousand one hundred r p m. The F one's rev limiter was raised to eight thousand three hundred for its record run. By our own arithmetic, the new redline is about forty-six percent higher. Thirty years of engineering, aimed at the same idea of low weight and high power.""",
   "Cosworth V12 T.50 tachometer", "12,100 RPM vs 8,300 RPM")
sc("""The page also lists the T fifty S, called the Niki Lauda variant, a track-only version with seven hundred sixty-one horsepower, priced at three point one million pounds before taxes, with twenty-five planned. Named for the driver who won the fan car's only race. Murray never forgot where the idea came from.""",
   "Niki Lauda 1978 Brabham", "THE T.50s NIKI LAUDA")
sc("""Price and production were limited. The page says Gordon Murray Automotive planned to build one hundred customer cars at its Surrey site, at two point three six million pounds each before taxes. It says all one hundred road cars were sold within forty-eight hours of the premiere, and that production started in March twenty twenty-three.""",
   "Gordon Murray Automotive factory", "100 CARS SOLD IN 48 HOURS")

# ---------- 8. HONORS ----------
ch("The legacy")
sc("""Murray's career has been recognized. Wikipedia says he was awarded a C B E in the twenty nineteen New Year Honours for services to motoring. His university made him an honorary professor in two thousand two, and gave him an honorary doctorate in twenty eleven.""",
   "Gordon Murray CBE", "CBE, 2019")
sc("""In twenty twenty-two he received the inaugural F I A President's Innovation Medal, and in twenty twenty-four the B B C Top Gear Lifetime Achievement Award, described as recognizing arguably the greatest and most original thinker in both Formula One and the wider automotive sphere.""",
   "Gordon Murray award", "FIA INNOVATION MEDAL, 2022")
sc("""And the F one he sketched at an airport? Top Gear quotes Murray, who sold the oldest surviving car, saying it became a little untenable to own. He used to drive it on Sunday mornings, but once it was worth many millions, he was reluctant to risk damaging it. Even its creator feared the legend he had made.""",
   "McLaren F1 Gordon Murray", "\"UNTENABLE TO OWN\"")

# ---------- 9. THE ANSWER ----------
ch("The man behind the legend")
sc("""So here is the story. A boy from Durban with a racing father. A designer who built a fan car that won its only race and was then banned. A meeting at a Milan airport, where four car lovers decided to build the best car in the world. A road car its creator never meant to race, that won Le Mans.""",
   "McLaren F1 Gordon Murray", "FROM DURBAN TO LE MANS")
sc("""And an engineer who kept a list of what he hated about his own masterpiece, and then built another car to fix it, with a fan from his first famous car. It is one of the most unlikely stories in the history of cars. And it started with a sketch on graph paper.""",
   "McLaren F1 and T.50", "A SKETCH ON GRAPH PAPER")
sc("""Which part of Murray's story surprised you the most? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the F one, compare it with the new McLaren W one, and work out what it really costs to own one today.""",
   "McLaren F1", "WHICH PART SURPRISED YOU?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video84", "The Insane Story Behind the McLaren F1", [
    "Wikipedia, Gordon Murray: https://en.wikipedia.org/wiki/Gordon_Murray",
    "Wikipedia, Brabham BT46: https://en.wikipedia.org/wiki/Brabham_BT46",
    "Wikipedia, McLaren F1: https://en.wikipedia.org/wiki/McLaren_F1",
    "Wikipedia, McLaren F1 GTR: https://en.wikipedia.org/wiki/McLaren_F1_GTR",
    "Wikipedia, Gordon Murray Automotive T.50: https://en.wikipedia.org/wiki/Gordon_Murray_Automotive_T.50",
    "Attic Capital, Gordon Murray and the McLaren F1: https://atticcapital.com/gordon-murray-mclaren-f1/",
    "Gooding and Company coverage of F1 chassis 029, JustCars (Australia): https://www.justcars.com.au/news-and-reviews/feature-1995-mclaren-f1/924590",
    "Motor Authority, A look back at the original clay models for the McLaren F1: https://www.motorauthority.com/news/1081316_a-look-back-at-the-original-clay-models-for-the-mclaren-f1",
    "Top Gear, McLaren F1s are now worth 16 million pounds: https://topgear.com.sg/features/mclaren-f1s-are-now-worth-ps16million",
], "D")
