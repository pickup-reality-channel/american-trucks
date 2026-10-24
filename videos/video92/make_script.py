import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

# ---------- HOOK ----------
sc("""When Horacio Pagani arrived in Italy, Lamborghini had withdrawn its job offer. According to a published interview, he took any work he could find: florist, steel welder. He and his wife lived in a tent for a few months. Eventually Lamborghini hired him as a laborer, the lowest entry-level role in the company. Today, his name is on some of the most expensive cars in the world. This is the insane story behind Horacio Pagani.""",
   "Horacio Pagani", "THE INSANE STORY BEHIND HORACIO PAGANI")
sc("""Here is the twist. A letter from a world champion opened the door in Italy, a bank loan bought an oven that his employer refused to buy, and a Mercedes engineer was shown a workshop where friends in work coats had been asked to pretend to be a larger company. All of it is in published sources, and all of it is true as far as we can verify.""",
   "Pagani Zonda", "A LETTER · A LOAN · A WORKSHOP FULL OF FRIENDS")
sc("""Every fact in this video comes from published sources, listed in the description. Where sources disagree, we will tell you. And there are a few disagreements, starting with the very first car he built.""",
   "Horacio Pagani", "EVERY FACT IS SOURCED")

# ---------- 1. ARGENTINA ----------
ch("A boy in rural Argentina")
sc("""Wikipedia says Horacio Pagani was born on the tenth of November, nineteen fifty-five, in Casilda, in the Argentine province of Santa Fe. It describes him as an Argentine-Italian businessman and automobile engineer. The page names his parents as Luca and Maria Pagani, and says his father was a baker from Italy, though it marks that detail as needing a citation.""",
   "Casilda Santa Fe Argentina", "BORN 10 NOVEMBER 1955, CASILDA")
sc("""An interview summary published by Attic Capital says he grew up in a rural area, where his family and community had little exposure to the arts or technical subjects. Wikipedia adds that he showed an interest in engineering from an early age, and felt that his rural birth town was inadequate for an engineering career.""",
   "Argentine countryside", "A TOWN TOO SMALL FOR HIS DREAM")
sc("""At thirteen or fourteen, according to the Attic Capital summary, he found a line from Leonardo da Vinci in a magazine at his father's home. He later quoted it: art and science can go hand in hand. That sentence would become the way he describes his entire career, in which carbon fibre and sculpture are the same craft.""",
   "Leonardo da Vinci", "\"ART AND SCIENCE CAN GO HAND IN HAND\"")
sc("""His passion for cars came from another magazine, the same source says. An Argentine publication called Automundo covered racing and new sports cars, and that is where he first saw Ferrari, Bertone and Lamborghini. He built model cars and drew cars as a child. In his words, these cars seemed magical to him, and he realised that it was going to be his job.""",
   "Automundo magazine", "A MAGAZINE CALLED AUTOMUNDO")
sc("""Wikipedia says he opened a small shop at a very young age and gained craftsmanship experience. By the age of twenty, the page says, he had designed and built his first Formula Three racing car. The Attic Capital summary says it was a Formula Two single-seater built from scratch. The two sources disagree on the class, so we report both.""",
   "Formula 3 race car", "BY 20: A RACING CAR BUILT FROM SCRATCH")
sc("""Wikipedia also says Renault hired him to improve the body of a racing car, and that his work offered staggering improvements. Then he visited Lamborghini and met its chief technical director, Giulio Alfieri. So even before he left Argentina, a young man from a small town had been noticed by a French carmaker and an Italian one.""",
   "Renault racing car", "RENAULT HIRED HIM TO IMPROVE A RACE CAR")

# ---------- 2. FANGIO ----------
ch("The letter from Fangio")
sc("""The Attic Capital summary says he met Juan Manuel Fangio, the five-time Formula One world champion, through Oreste Berta. At that time, the summary says, Fangio was president of Mercedes-Benz Argentina. Pagani asked him for help getting into the Italian car industry. This is the most important introduction of his life.""",
   "Juan Manuel Fangio", "MEETING FANGIO")
sc("""Fangio wrote five letters of recommendation. The summary says he noted that it was only the second letter of recommendation he had ever written. Think about that. One of the most famous drivers in history, who almost never wrote such letters, wrote five for a young engineer from a small Argentine town.""",
   "Fangio letters", "5 LETTERS FROM A WORLD CHAMPION")
sc("""The letters worked. According to the same summary, Ferrari offered Pagani a job in its Formula One team. He declined because he wanted to build grand touring cars. We have no way to verify that conversation beyond the interview, but the story shows that he chose a harder path on purpose, with an offer from Ferrari on the table.""",
   "Ferrari Formula One", "HE TURNED DOWN A FERRARI F1 JOB")
sc("""Instead he accepted the offer from Giulio Alfieri at Lamborghini. The summary says he married his girlfriend, Cristina, in Argentina, and then moved to Italy. Wikipedia says the move happened in nineteen eighty-two. By our own arithmetic, he was twenty-six, and in the same year he started a new life in a new country.""",
   "Italy 1982", "1982: MOVING TO ITALY AT 26")

# ---------- 3. THE TENT ----------
ch("The job that disappeared")
sc("""Then the plan fell apart. The summary says Lamborghini withdrew the offer. Pagani went to Italy anyway and asked for any position at all. While waiting, he did odd jobs: the summary lists work as a florist and as a steel welder. And for a few months, it says, the couple lived in a tent.""",
   "Modena Italy 1980s", "FLORIST, WELDER, AND A TENT")
sc("""Lamborghini eventually hired him as a laborer, the lowest entry-level role in the company, according to the summary. Wikipedia describes it as starting with basic jobs such as sweeping floors. That is a remarkable detail. The man who would later design hypercars began his Italian career with a broom.""",
   "Lamborghini factory", "HIRED AS A LABORER")
sc("""But he rose quickly. The summary says he moved up through the ranks, and Wikipedia says he became chief engineer and built the Countach Evoluzione concept. Pagani's company page adds that he created and managed Lamborghini's composites department. A man with no job in the country became the person in charge of one of its most important technologies.""",
   "Lamborghini Countach Evoluzione", "FROM LABORER TO CHIEF ENGINEER")

# ---------- 4. THE AUTOCLAVE ----------
ch("The oven Lamborghini refused to buy")
sc("""Now the moment that changed his life. To make carbon fibre parts, you need an autoclave, a large pressurised oven that cures the material. Wikipedia says Pagani proposed buying one to extend production of the Evoluzione's carbon parts. Lamborghini refused, reasoning that Ferrari did not have an autoclave, so Lamborghini did not need one either.""",
   "Autoclave carbon fibre", "\"FERRARI DOESN'T HAVE ONE\"")
sc("""So he did something unusual. The Attic Capital summary says he rode his bicycle to a bank in Bologna and secured a loan to buy one. Wikipedia says he borrowed capital in late nineteen eighty-seven. The summary says Italy then had only about four or five autoclaves in total, by his own account.""",
   "Bank in Bologna", "LATE 1987: A BANK LOAN FOR AN OVEN")
sc("""His manager, the summary says, called the plan mad, and told him to store the equipment in a rented warehouse. So the man who bought the oven did it without his employer's support. By our own reading, he was risking his savings, his job and his reputation on a machine that nobody else in the company wanted.""",
   "Warehouse workshop", "\"YOU ARE COMMITTED, MAD!\"")
sc("""The company page says that in nineteen eighty-eight, he founded Pagani Composite Research, which worked with Lamborghini on the Countach twenty-fifth anniversary restyling, the L M zero zero two, the P one forty concept and the Diablo. In other words, the oven that Lamborghini refused to buy ended up working for Lamborghini.""",
   "Lamborghini Diablo", "1988: PAGANI COMPOSITE RESEARCH")
sc("""In nineteen ninety-one, Wikipedia says, he left Lamborghini and founded the consultancy Modena Design. It made carbon fibre composites for Formula One cars and for clients including Daimler, Ferrari and Aprilia. So Ferrari, the company whose lack of an autoclave had been used as a reason, became one of his customers.""",
   "Modena Design", "1991: MODENA DESIGN")

# ---------- 5. A CAR OF HIS OWN ----------
ch("Building a car at night")
sc("""Then came a recession. The Attic Capital summary says a slowdown in the auto industry around the Gulf War left Pagani with heavy equipment costs and few orders. He had debts from building his workshop and from paying staff. His own words, in the summary, are that he was jobless but had debts.""",
   "Modena workshop", "DEBTS, FEW ORDERS")
sc("""That was the moment he decided to build his own car. He worked on it in the evenings, early in the mornings and at weekends, the summary says. His quote is simple: that's how the Zonda was born. Wikipedia says that in the late nineteen eighties he had already begun designing the project he called the C eight.""",
   "Pagani sketches", "\"THAT'S HOW THE ZONDA WAS BORN\"")
sc("""Wikipedia's Pagani page says he planned to call it the Fangio F one, in honour of the man who had written his letters. It adds that in nineteen ninety-two he began building a prototype, which was tested in the Dallara wind tunnel in nineteen ninety-three. Concept and bodywork were designed by late nineteen ninety-three, according to the summary.""",
   "Dallara wind tunnel", "1993: TESTED IN THE DALLARA WIND TUNNEL")
sc("""The company was formally founded in nineteen ninety-two, according to Wikipedia. By our arithmetic, he was thirty-six. He is listed as its founder, chairman, chief designer and chief executive. That is four jobs for one person, in a company that began with a few friends and a workshop near Modena.""",
   "Pagani Automobili", "1992: FOUNDED AT 36")

# ---------- 6. THE ENGINE ----------
ch("The engine problem")
sc("""There was one huge problem. The summary says the car was designed for a V twelve, but initially had no engine. Developing one was financially out of reach. A tiny company with no money was trying to build a V twelve supercar, and the heart of the car did not exist.""",
   "V12 engine", "A V12 CAR WITH NO ENGINE")
sc("""The solution came from Fangio again. The summary says Fangio's eightieth birthday, in nineteen ninety-one in Argentina, led to the Mercedes V twelve being introduced. By then Fangio was honorary president of Mercedes-Benz Argentina. A friendship that produced five letters now helped open the door to the engine itself.""",
   "Mercedes-Benz V12", "FANGIO'S 80TH BIRTHDAY, 1991")
sc("""Pagani met Dieter Zetsche, a Mercedes engineer, in Stuttgart, according to the summary. Zetsche called the design timeless. Pagani answered, in his words, thank goodness it's a timeless car, because I'm the one with no money and I'm going to need a lot of time to make it. It is one of the more honest sales pitches ever recorded.""",
   "Dieter Zetsche Stuttgart", "\"THANK GOODNESS IT'S A TIMELESS CAR\"")
sc("""Then Zetsche wanted to inspect the workshop. And here is the part that makes this story special. Pagani asked friends to dress in work coats, so that the shop would look like a larger operation. He later said, in the summary, that he did not know if the trick had any effect, but from that moment the Mercedes relationship began.""",
   "Pagani workshop 1990s", "FRIENDS IN WORK COATS")
sc("""The engine itself made an impression. Pagani says, in the summary, that when he put the Mercedes V twelve on the scale, it weighed seventy kilograms less than the Lamborghini Diablo engine he had designed around, and its centre of gravity was forty to fifty millimetres lower. He says he has a weight mania.""",
   "Engine on a scale", "70 KG LIGHTER THAN THE DIABLO'S ENGINE")
sc("""Pagani's company page says Mercedes-Benz agreed to supply V twelve engines in nineteen ninety-four. That agreement shaped everything that followed. Pagani's cars still use Mercedes-AMG V twelve engines. The Utopia, according to Top Gear, has a bespoke twin-turbo V twelve built specially for Pagani. Thirty years later, the partnership is still running.""",
   "Mercedes-AMG V12", "1994: MERCEDES AGREES TO SUPPLY V12s")

# ---------- 7. THE NAME ----------
ch("What to call it")
sc("""Fangio died in nineteen ninety-five, according to Wikipedia. And the summary says that a month before the Geneva Motor Show launch, Pagani worried that no car could live up to Fangio's name. He dropped it, out of respect. So the car that was designed as a tribute to Fangio was renamed, and the name Fangio F one was never used.""",
   "Fangio memorial", "THE NAME \"FANGIO\" WAS DROPPED")
sc("""Childhood friends in Argentina suggested Zonda, the summary says. It refers to the warm wind from the Andes, and also to the Autodromo El Zonda racetrack near the mountains. Wikipedia describes it as a hot air current above Argentina. So a car built in Italy was named after the place where its creator grew up.""",
   "Zonda wind Andes", "ZONDA: A WARM WIND FROM THE ANDES")
sc("""The full name was Zonda C twelve. The summary says the C stands for Cristina, his wife, and the twelve for the V twelve. The couple who lived in a tent when they arrived in Italy now had a car named after her. It is, in our reading, one of the most personal names in the history of supercars.""",
   "Pagani Zonda C12", "C = CRISTINA · 12 = V12")
sc("""It debuted at the nineteen ninety-nine Geneva Motor Show, according to Wikipedia. By our own arithmetic, Pagani was forty-three. Wikipedia's page on Pagani says the Zonda took seven years to complete. The Attic Capital summary says about six, from the completion of the design. Different starting points, and an easy way to see how long it really took.""",
   "Pagani Zonda Geneva 1999", "GENEVA 1999: AGE 43")
sc("""The summary quotes a book, Pagani: Hypercars d'Autore, which credits the Zonda with popularising the word hypercar. It lists four benchmarks: futuristic, provocative styling; composite materials for performance and safety; an official Mercedes-AMG V twelve; and customers able to follow their car's construction. The book says the Zonda was understood instantly at the show.""",
   "Pagani Zonda", "THE CAR THAT POPULARISED \"HYPERCAR\"")

# ---------- 8. THE GROWTH ----------
ch("From one car to a legend")
sc("""The Zonda grew in many versions. Wikipedia says about one hundred forty were built by twenty nineteen, including development cars. Then came the Huayra. The company page says it was revealed in January twenty eleven, with a twin-turbo Mercedes-AMG V twelve, seven hundred forty metric horsepower. A hundred were produced, each costing one million pounds before options.""",
   "Pagani Huayra", "HUAYRA: 100 CARS, 2011")
sc("""The summary adds a striking detail about the Huayra. Pagani sent sketches to existing Zonda owners, and deposits arrived immediately, with no specifications, no prices beyond a sketch and no delivery dates. That is how much trust the company had earned. His customers paid for a drawing.""",
   "Huayra sketch", "DEPOSITS FOR A SKETCH")
sc("""Then the Utopia. Wikipedia says it was unveiled in Milan on the twelfth of September, twenty twenty-two, and that all ninety-nine coupés were assigned to customers. Top Gear quotes Pagani: no heavy batteries, no hybrid power, just a wonderful V twelve. Supercar Blondie says a manual was added because customers demanded it.""",
   "Pagani Utopia", "UTOPIA: 99 COUPÉS, ALL ASSIGNED")
sc("""The prices have moved with it. The summary quotes Pagani saying prices run from roughly three to fifteen million euros per car. Wikipedia says the Utopia coupé starts at two point one nine million dollars and the roadster at three point four. The company page says two of the three Zonda HP Barchettas cost fifteen million dollars each.""",
   "Pagani cars", "€3M TO €15M PER CAR")

sc("""The Zonda kept improving. Wikipedia's Pagani page says a Zonda R completed the Nürburgring Nordschleife on the thirtieth of June, twenty ten, in six minutes forty-seven seconds, a production-car record that beat the Ferrari five ninety-nine X X. A car from the little workshop beat Ferrari on the most famous test track in the world.""",
   "Nürburgring Nordschleife", "2010: ZONDA R BEATS FERRARI AT THE NÜRBURGRING")
sc("""The same page says that in two thousand five, Pagani announced plans to triple production within three years and to enter the American market in two thousand seven. Remember where this began. A tent, a broom and an oven. Twenty-three years after arriving in Italy, by our arithmetic, he was planning to sell cars in the United States.""",
   "United States market", "2005: PLANS FOR THE US MARKET")
sc("""The Zonda even raced at Le Mans. Wikipedia's Zonda page says the Zonda G R, a racing version developed by Carsport Zonda, retired from the two thousand three twenty-four hours of Le Mans after ten laps, because of a gearbox failure. It was a short race. But the car that began as sketches in the evenings was on the grid at the most famous endurance race on Earth.""",
   "Le Mans 24 Hours", "2003: ZONDA GR AT LE MANS")
sc("""Pagani never forgot his first customers. The company page says the Huayra B C, unveiled in twenty sixteen, was named after Benny Caiola, Horacio Pagani's friend and the first Pagani customer. It made seven hundred sixty-four metric horsepower and weighed one thousand two hundred eighteen kilograms. Thirty were made, although Pagani had claimed a limit of twenty.""",
   "Pagani Huayra BC", "HUAYRA BC: NAMED AFTER THE FIRST CUSTOMER")
sc("""The Huayra's name, the company page says, comes from the Quechua god of wind, Huayra-tata. Wikipedia's page on Horacio Pagani calls it the Incan god of wind, with a note asking for a citation. So the two cars he is best known for are both named after winds, one from the Andes and one from a god of wind. A boy from Argentina never left the Andes behind.""",
   "Andes mountains", "ZONDA AND HUAYRA: BOTH NAMED AFTER WIND")
sc("""The Zonda ended in twenty seventeen. Wikipedia's Zonda page says the HP Barchetta was unveiled at Pebble Beach and marks the end of Zonda production. Only three were built, and Horacio Pagani kept one for himself. After all those customers, the last Zonda in the list is one that he decided to keep.""",
   "Pagani Zonda HP Barchetta", "THE LAST ZONDA: HE KEPT ONE")
sc("""Let us do the maths on his timeline. He arrived in Italy in nineteen eighty-two. The Zonda was shown in nineteen ninety-nine, seventeen years later. The oven was bought in late nineteen eighty-seven, and the Utopia was unveiled in twenty twenty-two, thirty-four to thirty-five years later. All of it is our own arithmetic, from the dates in the sources.""",
   "Pagani timeline", "1982 → 1999 → 2022")
# ---------- 9. THE MAN ----------
ch("The man behind the cars")
sc("""What is he like? The summary says Pagani rides a bicycle to work, prefers driving to flying, and owns a Toyota Alphard van that he uses for trips to Milan. It also says he ordered his own Ferrari, and visits the factory to check its progress. The founder of one of the world's most exclusive car brands is also a customer of Ferrari.""",
   "Horacio Pagani bicycle", "A BICYCLE AND A TOYOTA VAN")
sc("""His philosophy is also in the summary. On humility, he says: we don't have to make a better car than Ferrari or Lamborghini. And on his own cars, he says: I don't fall in love with my cars. If I fell in love with my cars, I would lose objectivity. Both quotes show a man who stays practical about his own creations.""",
   "Horacio Pagani quote", "\"I DON'T FALL IN LOVE WITH MY CARS\"")
sc("""And the honours have arrived. Wikipedia says that in twenty twenty-five he received an honorary master's degree in design and engineering from the Polytechnic University of Milan, and several Pagani cars were displayed in the foyer of its Bovisa campus afterwards. A man who began with a broom now has a degree from one of Italy's top engineering universities.""",
   "Politecnico di Milano", "2025: HONORARY MASTER'S, POLITECNICO DI MILANO")

# ---------- 10. LESSON ----------
ch("How it happened")
sc("""So how does a boy from Casilda become the founder of Pagani? Look at the pattern in the sources. A magazine, a line from da Vinci, a letter from Fangio. A job offer that disappeared. A tent. A broom. An oven that his employer refused to buy, and a loan that bought it. A recession, and a car built in the evenings.""",
   "Horacio Pagani", "THE PATTERN")
sc("""And the end of that pattern is a Mercedes engine, a workshop filled with friends in work coats, a name taken from the wind of the Andes, and a letter C for Cristina. Nothing in this story came easily. But nearly every step is documented, which is why we trust it enough to tell it.""",
   "Pagani Zonda", "NOTHING CAME EASILY")
sc("""One caution. Much of the early part of the story comes from interviews, and interviews are memories. The details can differ, as the Formula Three and Formula Two difference shows. We have told you where we found conflicts. If you know of a primary source that settles them, please tell us in the comments.""",
   "Horacio Pagani", "INTERVIEWS ARE MEMORIES")
sc("""Which part of Horacio Pagani's story surprised you the most? Tell us in the comments. In the other videos of this series, we reveal two secrets hidden inside the Utopia, compare it with the Zonda, and work out what it really costs to own a Pagani.""",
   "Pagani Utopia", "WHICH PART SURPRISED YOU?")
sc("""And if you want to spend your money on something you can actually drive every day, our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality for more stories about the cars and trucks people really talk about.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video92", "The Insane Story Behind Horacio Pagani", [
    "Wikipedia, Horacio Pagani (auto executive): https://en.wikipedia.org/wiki/Horacio_Pagani_(auto_executive)",
    "Wikipedia, Pagani (company): https://en.wikipedia.org/wiki/Pagani_(company)",
    "Wikipedia, Pagani Zonda: https://en.wikipedia.org/wiki/Pagani_Zonda",
    "Wikipedia, Pagani Utopia: https://en.wikipedia.org/wiki/Pagani_Utopia",
    "Attic Capital, Horacio Pagani and the Zonda (interview summary): https://atticcapital.com/horacio-pagani-zonda/",
    "Top Gear, This is the brand new Pagani Utopia: https://www.topgear.com/car-news/first-look/brand-new-pagani-utopia-v12-engined-throwback",
    "Supercar Blondie, The Pagani Utopia is here: https://supercarblondie.com/pagani-utopia-c10-v12-manual-supercar-revealed/",
], "D")
