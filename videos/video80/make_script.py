import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""In nineteen sixty-six, Ford finally beat Ferrari at Le Mans, the most famous endurance race in the world. The man most responsible for that win was not a Ford executive. He was a Texan who had once gone bankrupt raising chickens, a man with a bad heart who had been forced out of the driver's seat. His name was Carroll Shelby.""",
   "Carroll Shelby", "THE MAN WHO MADE FORD BEAT FERRARI")
sc("""Here is the twist. Shelby had already won Le Mans himself, years earlier, in a British car. And when his heart forced him to stop driving, he became something even more dangerous to Ferrari. A builder. This is the insane story behind the Ford GT, told through the man who made it a legend.""",
   "Le Mans 1966", "HE HAD ALREADY WON LE MANS")
sc("""Every fact in this video comes from published sources, listed in the description. And the story has a second hero, an English mechanic named Ken Miles, whose fate is one of the saddest in racing. We will get to him. First, let's meet a sick boy from Texas.""",
   "Ford GT40 Le Mans", "EVERY FACT IS SOURCED")

# ---------- 1. TEXAS ----------
ch("A boy from Texas")
sc("""Wikipedia says Carroll Hall Shelby was born on the eleventh of January, nineteen twenty-three, in Leesburg, Texas. His father, Warren, was a rural mail carrier. By the age of seven, Shelby already suffered from heart valve leakage problems, and the complications followed him for the rest of his life.""",
   "Leesburg Texas", "BORN 1923, LEESBURG, TEXAS")
sc("""The family moved to Dallas when he was seven. Around the age of ten, Wikipedia says, Shelby rode his bicycle to nearby dirt tracks to watch races. At fifteen, he was driving and looking after his father's Ford. A sick child with a leaking heart was already falling in love with speed.""",
   "Dallas Texas 1930s", "A BAD HEART, A LOVE OF SPEED")
sc("""He graduated from Woodrow Wilson High School in Dallas in nineteen forty. And on the eleventh of April, nineteen forty-one, eight months before Pearl Harbor, he enlisted in the United States Army Air Corps. The boy with the heart condition was going to fly.""",
   "Army Air Corps 1941", "ENLISTED APRIL 1941")
sc("""Wikipedia says he graduated as a staff sergeant pilot in September nineteen forty-two and was commissioned a second lieutenant that December. He served as a flight instructor and test pilot, trained bombardiers and navigators, and later flew the B-18, B-25, A-26 and B-29 aircraft.""",
   "B-25 bomber", "FLIGHT INSTRUCTOR, TEST PILOT")
sc("""After the war, Shelby tried to make a living. Wikipedia says he started a dump truck business, then worked as an oil-well roughneck in nineteen forty-eight and nineteen forty-nine. Then he started a poultry farm. In nineteen fifty-two, that farm went bankrupt.""",
   "chicken farm", "1952: THE POULTRY FARM GOES BANKRUPT")

# ---------- 2. THE DRIVER ----------
ch("The racing driver")
sc("""Here is the twist. In that same year that his luck ran out, his racing began. Wikipedia says that in January nineteen fifty-two, Shelby raced his friend Ed Wilkin's MG T C at a drag meet at the Grand Prairie Naval Air Station in Texas. The page does not record who won that first race. But what came after is clear.""",
   "MG TC", "JANUARY 1952: FIRST RACE")
sc("""Later in nineteen fifty-two, Shelby won four races, taking only trophies, not prize money. It was a small start. But Shelby kept going, and within a few years he was racing for some of the most famous teams in Europe.""",
   "SCCA racing 1952", "4 WINS IN HIS FIRST YEAR")
sc("""Wikipedia lists a remarkable roster. Shelby drove for Aston Martin, including John Wyer's team. He drove a Maserati two fifty F for Scuderia Centro Sud in the nineteen fifty-eight Formula One season, and he drove Ferraris for American owners like Allen Guiberson and Tony Paravano. He even drove a Porsche.""",
   "Maserati 250F", "ASTON, MASERATI, FERRARI, PORSCHE")
sc("""Sports Illustrated named him its driver of the year in nineteen fifty-six, and again in nineteen fifty-seven. In nineteen sixty, he won the SCCA United States Road Racing Sports Car Championship. The man who had been a bankrupt farmer a few years earlier was now the best sports car driver in America.""",
   "Carroll Shelby 1950s", "SPORTS ILLUSTRATED DRIVER OF THE YEAR")
sc("""And in June nineteen fifty-nine, he reached the top. Wikipedia says Shelby co-drove an Aston Martin D B R one with Englishman Roy Salvadori to victory in the twenty-four hours of Le Mans. In Shelby's own words, winning the twenty-four hours was probably the greatest thrill he ever got out of racing.""",
   "Aston Martin DBR1", "LE MANS 1959: WINNER")
sc("""Think about that. Seven years after his poultry farm went bankrupt, Carroll Shelby was a Le Mans winner. He knew exactly how brutal that race was, how long it lasted, and what kind of car it took to survive twenty-four hours at full speed.""",
   "Le Mans 1959", "FROM BANKRUPTCY TO LE MANS IN 7 YEARS")
sc("""But his heart was getting worse. Wikipedia says Shelby retired from driving in October nineteen sixty, for health reasons. He was thirty-seven years old. A year later he opened the Shelby School of High Performance Driving with Pete Brock at Riverside, California. His driving career was over. His real career was just beginning.""",
   "Riverside raceway 1960", "OCTOBER 1960: FORCED TO RETIRE")

# ---------- 3. THE COBRA ----------
ch("The Cobra")
sc("""Shelby could no longer drive. So he decided to build. His idea was simple. Take a light British sports car and put a big American V8 in it. Wikipedia says Shelby became interested in the potential of the A C Ace chassis, built in England by A C Cars.""",
   "AC Ace", "A BRITISH BODY...")
sc("""He had almost no money, so the deals were made on credit. Wikipedia says A C's Charles Hurlock agreed to provide the chassis on credit. And Ford's Dave Evans agreed to provide two hundred twenty-one and two hundred sixty cubic inch V8 engines, plus transmissions, also on credit.""",
   "Ford small block V8", "...AN AMERICAN V8, ALL ON CREDIT")
sc("""Production of the Cobra began in March nineteen sixty-two, and Wikipedia says seventy-five cars were sold by the end of that year. That same year, nineteen sixty-two, Shelby established Shelby American to manufacture and market performance vehicles. The little company that would take on Ferrari was born.""",
   "Shelby Cobra", "1962: SHELBY AMERICAN IS BORN")
sc("""Shelby then turned Ford's new Mustang into a race car. Wikipedia says the Shelby G T three fifty began in nineteen sixty-five, and the Shelby G T five hundred followed in nineteen sixty-seven. Shelby produced them through nineteen sixty-eight. His name was becoming part of Ford's performance image. But the biggest job was still ahead.""",
   "Shelby GT350 1965", "GT350 (1965) AND GT500 (1967)")

# ---------- 4. FORD VS FERRARI ----------
ch("Ford wants Le Mans")
sc("""Meanwhile, Ford had a problem with Ferrari. Wikipedia's G T forty page says Enzo Ferrari was interested in selling to the Ford Motor Company. Ford reportedly spent several million dollars auditing Ferrari's factory assets. And then, in the page's words, Enzo cut the deal off out of spite.""",
   "Enzo Ferrari", "FERRARI SAYS NO")
sc("""Here is the twist. Henry Ford the second had wanted a Ford at Le Mans since the early nineteen sixties. Now he directed his racing division to find a company that could build a Ferrari-beater. The goal was specific. Beat Scuderia Ferrari, at the race Ferrari had dominated.""",
   "Henry Ford II", "BEAT FERRARI AT LE MANS")
sc("""The first G T forty was developed in England. Wikipedia says it was based on the British Lola Mark six, and Lola's owner and chief designer, Eric Broadley, agreed to make a short-term personal contribution. Ford set up a new subsidiary, Ford Advanced Vehicles, and at the end of nineteen sixty-three the team moved to Slough, near Heathrow Airport.""",
   "Lola Mk6", "BORN IN ENGLAND")
sc("""The name came from its height. Wikipedia explains that the G T stands for grand touring, and the forty is its height in inches, measured at the top of the windscreen, the minimum allowed. It was a very low car, built to be very fast.""",
   "Ford GT40 low profile", "WHY 'GT40'? 40 INCHES TALL")
sc("""But fast was not enough. In nineteen sixty-four, Wikipedia says, all three Ford entries retired at Le Mans, although one led the field from the second lap until its first pit stop. In nineteen sixty-five, the cars again failed to finish. Ford was spending a fortune, and the car kept breaking.""",
   "Ford GT40 1964", "1964 AND 1965: FAILURE")

# ---------- 5. SHELBY TAKES OVER ----------
ch("Shelby takes over")
sc("""That is when Ford turned to Shelby. Wikipedia says that after the Nassau race in December nineteen sixty-four, Ford handed the G T forty program over to Carroll Shelby's Shelby American team. The man who could no longer drive was now in charge of beating Ferrari.""",
   "Shelby American", "DECEMBER 1964: SHELBY TAKES OVER")
sc("""And it worked quickly. Wikipedia says Ken Miles and Lloyd Ruby took a Shelby American-entered G T forty to victory in the Daytona two thousand kilometers in February nineteen sixty-five. It was proof that the car could win when the right people were running it.""",
   "Ford GT40 Daytona 1965", "FEBRUARY 1965: DAYTONA WIN")
sc("""Then came a bigger engine. The experience gained in nineteen sixty-four and nineteen sixty-five, Wikipedia says, allowed the seven-liter Mark two prototypes to dominate the following years. The big four hundred twenty-seven cubic inch V8 gave the car much more power, and put much more stress on every part of it.""",
   "Ford 427 engine", "THE 7-LITER MARK II")

# ---------- 6. KEN MILES ----------
ch("Ken Miles")
sc("""And the man who drove those cars harder than anyone was Ken Miles. Wikipedia says he was born on the first of November, nineteen eighteen, in Sutton Coldfield, then in Warwickshire and now part of Birmingham. He left school at fifteen and became an apprentice at Wolseley Motors, which sent him to a technical school.""",
   "Ken Miles", "KEN MILES: BORN 1918, ENGLAND")
sc("""In the Second World War, Miles served in the British Army. In October nineteen forty-two, he was among the founding members of the Royal Electrical and Mechanical Engineers. He landed in Normandy on the fifteenth of June, nineteen forty-four, and served as a tank commander. He reached the rank of staff sergeant.""",
   "Normandy 1944 tank", "NORMANDY, JUNE 15, 1944")
sc("""After the war, Miles raced Bugattis, Alfa Romeos and Alvises in England. Then in nineteen fifty-two, the same year Shelby started racing, he moved to the United States and settled in Los Angeles. He worked as a service manager for Gough Industries, the Southern California M G distributor.""",
   "Los Angeles 1950s", "1952: TO LOS ANGELES")
sc("""Miles was an engineer as much as a driver. In nineteen fifty-three, Wikipedia says, he won fourteen straight victories in SCCA racing in an M G-based special of his own design. In nineteen fifty-five he built the Flying Shingle, and he helped build a Cooper-based car nicknamed the Pooper, which dominated its class on the West Coast.""",
   "MG special race car", "14 STRAIGHT WINS IN HIS OWN CAR")
sc("""In March nineteen fifty-five, Miles crossed the line first at Palm Springs, ahead of Cy Yedor and a young actor named James Dean. But he was later disqualified because his fenders were too wide, which bumped Yedor and Dean up to first and second. Miles was a man who lost races on technicalities long before Le Mans.""",
   "Palm Springs races 1955", "BEATING JAMES DEAN, THEN DISQUALIFIED")
sc("""His American crew nicknamed him Teddy Teabag, and he was called the Stirling Moss of the West Coast for his courtesy on the track. He described himself plainly. I am a mechanic, he said. That has been the direction of my entire vocational life. In nineteen sixty-three, he became chief test driver of Shelby American.""",
   "Ken Miles Shelby American", "CHIEF TEST DRIVER, 1963")
sc("""He played a major role in the development and success of the racing Cobra two eighty-nine, the Daytona Coupe, the four twenty-seven Cobra and the Ford G T forty, Wikipedia says. If Shelby was the boss who got the deals, Miles was the one who found out whether the car would survive the race.""",
   "Shelby Daytona Coupe", "THE MAN WHO TESTED EVERYTHING")
sc("""In nineteen sixty-five, Miles won the Daytona two thousand kilometers with Lloyd Ruby, and finished second at Sebring with Bruce McLaren. At Le Mans that year, he shared a Mark two with McLaren but retired with gearbox trouble. Then came nineteen sixty-six, the year he almost won everything.""",
   "Ford GT40 Mk II 1965", "1965: DAYTONA WIN, LE MANS RETIREMENT")
sc("""In nineteen sixty-six, Miles won the twenty-four hours of Daytona with Lloyd Ruby, and then the twelve hours of Sebring. Two of the three biggest endurance races of the year. If he won Le Mans too, he would complete a historic triple. And after Sebring, Ford believed it was ready.""",
   "Ford GT40 Sebring 1966", "1966: DAYTONA + SEBRING")

# ---------- 7. LE MANS 1966 ----------
ch("Le Mans 1966")
sc("""Ford arrived at Le Mans in June nineteen sixty-six with an enormous effort. Wikipedia says it entered fifteen Mark two cars, of which the organizers accepted eight, plus five Mark ones. After two years of its three-year program, the page says, Ford had very little to show for its immense investment. This was the moment.""",
   "Le Mans 1966 Ford GT40", "FORD'S HUGE EFFORT")
sc("""The race started on a cool and cloudy afternoon in front of an official crowd of three hundred fifty thousand. Dan Gurney set the fastest qualifying lap, three minutes thirty point six seconds, a second faster than Miles, Gardner and McLaren. At dusk it began to drizzle, and heavy rain came after six hours.""",
   "Le Mans 1966 crowd", "350,000 SPECTATORS")
sc("""Then the Ferraris began to fall apart. Wikipedia says that of fourteen Ferraris entered, only two G Ts finished. The Ferrari P three challenge collapsed through overheating and mechanical failures. But Ford had problems too. Only three of the thirteen Fords finished. The three that survived were the three that mattered.""",
   "Ferrari P3 1966", "ONLY 3 OF 13 FORDS FINISHED")
sc("""By the end, Fords were first, second and third. Wikipedia says that a decision was made in the Ford pits to have the cars finish side by side, a photograph for the whole world. The page also says Miles's car was directly instructed to slow down during the last driver change to let McLaren catch up.""",
   "Ford GT40 1966 finish", "THE STAGED FINISH")
sc("""Here is the twist. The cars did cross the line together, but the organizers applied the tie rule. McLaren and Amon had started sixty feet behind Miles and Hulme on the grid, so they had covered more distance. The McLaren car was declared the winner, about six meters ahead at the line. Ken Miles was second.""",
   "Bruce McLaren 1966", "MILES LOSES BY A TECHNICALITY")
sc("""Miles's reaction, Wikipedia says, was simple. I'm disappointed, of course, but what are you going to do about it. Carroll Shelby later said that Ken Miles won the race, and expressed regret about the outcome. Miles had won Daytona, Sebring, and led Le Mans, and still missed the triple.""",
   "Ken Miles 1966", "\"WHAT ARE YOU GOING TO DO ABOUT IT?\"")
sc("""The winning car covered three thousand nine point three miles at an average of one hundred twenty-five point three nine miles per hour. It was the first time the three thousand mile and one hundred twenty-five mile per hour marks were exceeded. Chris Amon, at twenty-two, became the youngest winner in the history of the race.""",
   "Chris Amon Le Mans", "125.39 MPH, 3,009 MILES")
sc("""Ford had won Le Mans for the first time, with a one, two, three finish. The press release said the result showed that an American-built car could top Europe's best. Ferrari had been beaten at its own game. Henry Ford the second had his revenge.""",
   "Ford GT40 1-2-3", "AN AMERICAN CAR TOPS EUROPE'S BEST")

# ---------- 8. TRAGEDY ----------
ch("Riverside")
sc("""Two months later came the tragedy. After Walt Hansgen died testing a Mark two at Le Mans in April, Ford had shelved the J-car, the experimental successor to the G T forty. In August nineteen sixty-six, Shelby American resumed testing, with Ken Miles as the primary test driver.""",
   "Ford J-car", "THE EXPERIMENTAL J-CAR")
sc("""Wikipedia describes the J-car as having a breadvan-shaped rear and a honeycomb panel design, and says it was unproven at high speed. After almost a day of testing at Riverside International Raceway, at the end of the mile-long back straight, the car suddenly flipped and caught fire.""",
   "Riverside International Raceway", "AUGUST 17, 1966")
sc("""The car was going at an estimated speed of over two hundred miles per hour. It broke into pieces and ejected Miles, killing him instantly. Ken Miles died on the seventeenth of August, nineteen sixty-six, at the age of forty-seven.""",
   "Ford J-car crash", "KEN MILES, AGE 47")
sc("""His son Peter, who was born in September nineteen fifty, was almost sixteen years old, and witnessed his father's death. Peter later worked in racing himself, and in a twenty nineteen interview said the last time he went to Le Mans was in nineteen sixty-five, with his father.""",
   "Peter Miles", "HIS SON PETER WITNESSED IT")
sc("""The lessons from the crash changed the car. Wikipedia says the J-car's aerodynamics were greatly modified to correct rear-end lift at race speeds, and Ford ordered a roll cage similar to those used in NASCAR Grand National racing. The revised car was renamed the Ford Mark four.""",
   "Ford GT40 Mk IV", "THE MARK IV")

# ---------- 9. 1967 ----------
ch("The all-American win")
sc("""In nineteen sixty-seven, the Mark four won the twelve hours of Sebring with Mario Andretti and Bruce McLaren. And at Le Mans, Dan Gurney and A J Foyt won the twenty-four hours, with Wikipedia saying the car proved to be the fastest in the field, reaching two hundred thirteen miles per hour.""",
   "Dan Gurney AJ Foyt Le Mans 1967", "1967: GURNEY AND FOYT WIN")
sc("""The Mark four was big and heavy, Wikipedia says, halfway between a road-legal passenger car and a race car, reliable and comfortable but heavy. Gurney was six feet four inches tall, and the car was given a bubble over the driver's seat so he could fit under the roof. Only six Mark fours were ever built.""",
   "Ford GT40 Mk IV bubble roof", "ONLY 6 MARK IVS BUILT")
sc("""The Mark four was Shelby's last prototype racer, Wikipedia says. And Ford's G T forty kept winning without him. The private John Wyer Gulf Oil team won Le Mans in nineteen sixty-eight, by just a few seconds, with the already outdated Mark one. The same chassis won again in nineteen sixty-nine, in a close finish over a Porsche nine oh eight.""",
   "Gulf GT40 Le Mans 1969", "1968 AND 1969: THE GULF CARS")
sc("""That makes four straight Le Mans wins for the G T forty, from nineteen sixty-six through nineteen sixty-nine. And only about one hundred cars in total were made, mostly as two eighty-nine cubic inch Mark ones. A tiny car, with a giant legacy.""",
   "Ford GT40 Gulf livery", "FOUR WINS, ABOUT 100 CARS")
sc("""Wikipedia says Ken Miles was posthumously inducted into the Motorsports Hall of Fame of America in two thousand one, and into the West Coast Stock Car Hall of Fame in twenty twenty. He is buried at the Abbey of the Psalms Mausoleum in Hollywood Forever Cemetery in Hollywood, California.""",
   "Hollywood Forever Cemetery", "HALL OF FAME, 2001")

# ---------- 10. SHELBY AFTER ----------
ch("Shelby after Le Mans")
sc("""Shelby kept building for decades. Wikipedia says that, at the request of Chrysler chairman Lee Iacocca, he began working with Dodge and became a performance consultant on the Dodge Viper Technical Policy Committee. He also helped develop performance cars with Oldsmobile at General Motors.""",
   "Dodge Viper", "DODGE VIPER AND OLDSMOBILE")
sc("""But his heart remained a problem. Wikipedia says Shelby received a heart transplant in nineteen ninety, and a kidney transplant in nineteen ninety-six. The child with a leaking heart valve, who retired at thirty-seven because of his heart, lived for more than twenty years with a transplanted one.""",
   "Carroll Shelby older", "HEART TRANSPLANT, 1990")
sc("""He also gave back. Wikipedia says Shelby established the Carroll Shelby Children's Foundation to cover medical bills of children who have heart disease. From two thousand eight, he funded scholarships for the automotive program at Northeast Texas Community College in Leesburg, which renamed the program for him.""",
   "Leesburg Texas college", "THE CHILDREN'S FOUNDATION")
sc("""His life was not simple. Wikipedia says he was married seven times. He published an autobiography, The Carroll Shelby Story, in nineteen sixty-seven. And in two thousand three, he became technical advisor to the Ford G T project, the modern tribute to the car he had helped make famous.""",
   "Ford GT 2005", "TECHNICAL ADVISOR TO THE NEW FORD GT")
sc("""Carroll Shelby died on the tenth of May, two thousand twelve, in Dallas, Texas, at the age of eighty-nine. He had suffered from a serious heart ailment for decades. The doctors might have told him to slow down. In his own way, he never did.""",
   "Dallas Texas", "MAY 10, 2012: AGE 89")

# ---------- 11. LEGEND ----------
ch("The legend")
sc("""In two thousand nineteen, the story reached a much bigger audience. Wikipedia says Miles and Shelby's efforts at Le Mans were dramatized in the Oscar-winning film Ford versus Ferrari, released as Le Mans sixty-six in some parts of Europe. Matt Damon played Carroll Shelby, and Christian Bale played Ken Miles.""",
   "Ford v Ferrari film", "FORD v FERRARI (2019)")
sc("""Like any film, it simplified and dramatized parts of the story. But it brought Ken Miles to millions of people who had never heard his name, and reminded them that Ford's Le Mans victory was built by a small group of racers and mechanics, not only by a corporation.""",
   "Ford GT40 museum", "MILES, REMEMBERED")
sc("""And the story still lives in the modern Ford GT. Wikipedia says that in twenty sixteen, exactly fifty years after the nineteen sixty-six win, a Ford Chip Ganassi Racing GT won its class at Le Mans. Ford chose that anniversary on purpose. It was a tribute to the team that beat Ferrari.""",
   "Ford GT Le Mans 2016", "2016: 50 YEARS LATER")

# ---------- 12. THE ANSWER ----------
ch("The man behind the win")
sc("""So who made Ford beat Ferrari? Henry Ford the second wanted it, and Ford's money made it possible. Drivers like Ken Miles, Bruce McLaren, Chris Amon, Dan Gurney and A J Foyt delivered it on the track. But the man who brought the pieces together was Carroll Shelby.""",
   "Carroll Shelby Ford GT40", "THE MAN WHO BROUGHT IT TOGETHER")
sc("""A sick child from Texas. A bankrupt poultry farmer. A Le Mans winner forced to retire at thirty-seven. A builder who put Ford engines into British cars, and then turned Ford's failing Le Mans program into a winner. It is one of the most unlikely stories in motorsport.""",
   "Shelby Cobra and GT40", "THE MOST UNLIKELY STORY")
sc("""And here is the final twist. The car that beat Ferrari was born in England, based on a British race car, designed with help from a British engineer, and developed by an English test driver. The team that made it win was led by a Texan. Ford's great American victory was truly international.""",
   "Ford GT40 Mk II", "AN INTERNATIONAL VICTORY")
sc("""Who do you think deserves the most credit, Shelby or Miles? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Ford GT, compare it with the original G T forty, and look at the real cost of owning a modern Ford GT.""",
   "Ford GT", "SHELBY OR MILES?")
sc("""And if you want a Ford you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description, with real numbers on the trucks most people buy. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video80", "The Man Who Made Ford Beat Ferrari", [
    "Wikipedia, Carroll Shelby: https://en.wikipedia.org/wiki/Carroll_Shelby",
    "Wikipedia, Ken Miles: https://en.wikipedia.org/wiki/Ken_Miles",
    "Wikipedia, Ford GT40: https://en.wikipedia.org/wiki/Ford_GT40",
    "Wikipedia, 1966 24 Hours of Le Mans: https://en.wikipedia.org/wiki/1966_24_Hours_of_Le_Mans",
    "Wikipedia, Ford v Ferrari: https://en.wikipedia.org/wiki/Ford_v_Ferrari",
    "Wikipedia, Ford GT: https://en.wikipedia.org/wiki/Ford_GT",
], "D")
