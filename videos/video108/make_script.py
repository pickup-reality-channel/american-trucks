import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "pipeline"))
from scriptkit import sc, ch, save

sc("""It started in a bar in Hokkaido, with a question over drinks. It ended with five hundred cars, a loom with almost no equal, and the death of the man who had guided how the car drove. Every year, the project was on Toyota's list of things to be cancelled. Every year, someone saved it. This is the story behind the Lexus LFA, and it is stranger than the car.""",
   "Lexus LFA", "THE INSANE STORY BEHIND THE LEXUS LFA")
sc("""Here is the twist. The man who made the decision that defined the car, switching from aluminium to carbon fibre, was told by outside engineers that the timeline was insane. They would have budgeted about ten years. Toyota gave itself one. And the story has a human cost that the car's price tag never shows. We will tell it as the sources do, and say where they disagree.""",
   "Lexus LFA carbon fibre", "\"INSANE\": THE CARBON FIBRE DEADLINE")
sc("""Every fact in this video comes from a published source, listed in the description. Where sources disagree, we will tell you. Where we do the maths ourselves, we will say so.""",
   "Lexus LFA", "EVERY FACT IS SOURCED")

ch("The bar in Hokkaido")
sc("""The Truth About Cars traced the start to the tenth of February, two thousand. Haruhiko Tanahashi, later the LFA's chief engineer, told his boss Tetsuo Hattori, then Toyota's top vehicle engineer, over drinks in Hokkaido that he wanted to build the ultimate sports car. Hattori replied, why not. Tanahashi's diary logs it as approval to study a real sports car.""",
   "Hokkaido, Japan", "10 FEBRUARY 2000: \"WHY NOT\"")
sc("""A month later, the article says, a working group held its first meeting. On the sixth of July two thousand, at an evaluation drive at the Shibetsu proving ground, a director said that baby sports cars are bad. So the team aimed higher: a grown-up sports car. Lexus's magazine adds that colleagues sketched early concepts on table napkins.""",
   "Shibetsu proving ground", "JULY 2000: \"BABY SPORTS CARS ARE BAD\"")
sc("""Here is the first discrepancy. Lexus's timeline says the LFA began in early two thousand as a research and development project, and that Tanahashi was soon named project leader. The Truth About Cars gives the specific date. They agree on the year. We will use early two thousand, and the tenth of February as the date the second source reports.""",
   "Calendar", "SOURCES AGREE ON 2000 · DIFFERENT PRECISION")
sc("""In January two thousand one, Lexus says, Tanahashi recruited the master driver Hiromu Naruse, and they compiled a list of five hundred key assets. V ten engine development, it adds, began within a year of Tanahashi's arrival. Naruse is the second central figure in this story. We will come to why.""",
   "Hiromu Naruse", "JANUARY 2001: NARUSE JOINS · 500 KEY ASSETS")
sc("""Naruse helped define the blueprint, according to the Lexus magazine. He proposed a front-mounted mid-engine layout and a forgiving chassis. He also made a decision about the project's political survival. Because Toyota's board focused on volume production, the team needed a champion. Naruse suggested pitching the idea to Akio Toyoda, then in charge of operations in China.""",
   "Hiromu Naruse and Akio Toyoda", "THE TEAM NEEDED A CHAMPION")

ch("The champion")
sc("""Akio test-drove several supercars with Naruse and Tanahashi, the magazine says, and concluded the car could serve as a halo model that improves the whole Lexus brand. Lexus's timeline places Naruse's recommendation to add Toyoda to the team in January two thousand two, after which the board approved the team's proposals.""",
   "Akio Toyoda", "JANUARY 2002: TOYODA JOINS THE TEAM")
sc("""The first prototype was completed in June two thousand three, according to both Lexus and Wikipedia. Tanahashi was chief engineer, and Akio was always the first test driver. By our own arithmetic, that is about three years and four months from the bar in Hokkaido, a short time for a prototype of such a car.""",
   "Lexus LFA prototype", "JUNE 2003: FIRST PROTOTYPE")
sc("""The business case was harder. The article says the board initially rejected the project, and that Akio backed it afterwards. A marketing specialist, Atsushi Takada, compiled a dossier arguing for its value. At a top-level meeting of about a hundred people, he said he was just a divisional manager, but he thought it was worth it. The board approved the project with a cap of five hundred units.""",
   "Toyota board meeting", "\"I AM JUST A DIVISIONAL MANAGER BUT I THINK IT IS WORTH IT\"")
sc("""The five hundred figure is worth pausing on. Lexus says the board approved a cap of five hundred units. Wikipedia says five hundred were built. So the cap was also the production run, to the car. By our arithmetic, the cap and the total are the same number, and that is not a coincidence. It was the approved scale of the dream.""",
   "Lexus LFA production", "THE BOARD'S CAP = THE FINAL PRODUCTION RUN")

ch("The kill list")
sc("""The Truth About Cars describes a survival ritual. Each fall, the project was on Toyota's list of projects to be killed. Each year, a senior executive saved it. Tanahashi credits the timing, since Toyota was doing well. That is a remarkable detail: a ten year project that depended every autumn on whether someone senior chose to look away.""",
   "Toyota headquarters", "EVERY FALL, ON THE LIST OF PROJECTS TO KILL")
sc("""By our own arithmetic, if the project faced that review in each of the years between two thousand and its approval in two thousand nine, it faced the list roughly nine or ten times. We should say that the article does not give the exact count. It says each fall. So our sum is a rough estimate, not a sourced number.""",
   "Calendar", "~9–10 REVIEWS (OUR ESTIMATE — NOT IN THE SOURCE)")
sc("""The car was shown to the public before it was approved for production. The first concept debuted at the Detroit motor show in January two thousand five, with an aluminium body and a V ten engine under five litres, and a top speed near two hundred miles per hour, according to Lexus's timeline. A concept can be an experiment. It is not a promise.""",
   "Detroit Auto Show 2005", "JANUARY 2005: CONCEPT AT DETROIT — ALUMINIUM BODY")
sc("""Meanwhile, on the track, the prototypes were learning. Lexus says a heavily disguised prototype lapped the Nürburgring Nordschleife for the first time in October two thousand four, about sixteen months after the first prototype was completed. Wikipedia agrees on the date. From that point, the Nürburgring was the car's testing ground, and its eventual proving ground.""",
   "Nürburgring Nordschleife", "OCTOBER 2004: FIRST NÜRBURGRING LAP")

ch("The decision: aluminium or carbon?")
sc("""Now the decision that defined the car. According to The Truth About Cars, aluminium stayed the material through two thousand five. In the spring of that year, the car was close to final, and Tanahashi still wanted to keep aluminium, with possible carbon fibre for body panels or the tub. Carbon promised a saving of about two hundred twenty pounds, but it was very expensive.""",
   "Lexus LFA aluminium prototype", "SPRING 2005: KEEP ALUMINIUM, OR GO CARBON?")
sc("""Toyota, the article says, had only about two years of carbon research, begun in two thousand three. The head of research and development, Kazuo Okamoto, pushed for full carbon fibre and told Tanahashi to bring all carbon production in-house. That conflicted with Toyota's culture of insourcing. But it was the direction chosen. The article then turns to the reaction of outside engineers.""",
   "Carbon fibre laboratory", "R&D CHIEF OKAMOTO: ALL CARBON, ALL IN-HOUSE")
sc("""Those Fuji Heavy engineers reportedly called the timeline insane. They would have budgeted about ten years for such research, the article says, and Toyota aimed to do it in one. By our arithmetic, that is a tenth of the time. We report it as the article does: reportedly, and in the words of the engineers, not as our own verdict.""",
   "Carbon fibre research", "\"INSANE\": ~10 YEARS OF WORK IN ONE")
sc("""Lexus's own timeline gives a different date for the change. It says the second concept, shown in Detroit in January two thousand seven, was more production-focused, with a mid-mounted engine and a switch to carbon fibre reinforced plastic, which cut mass by a hundred kilograms. So one source says the decision was taken in spring two thousand five, and the other shows its result in January two thousand seven.""",
   "Lexus LF-A concept 2007", "DECISION 2005 (TTAC) · SHOWN JAN 2007 (LEXUS)")
sc("""These do not actually conflict. A decision in the spring of two thousand five could show in a concept two years later. We read them as two parts of the same story. The Lexus magazine adds that the Motomachi plant had no composites experience, and that the choice significantly extended pre-production development time. That fits, and our reading is that the two years was the cost.""",
   "Lexus LFA", "A 2005 DECISION, VISIBLE IN 2007 (OUR READING)")
sc("""The result is the car we know. Wikipedia says carbon fibre makes up sixty-five percent of the body mass, with the rest aluminium. The Truth About Cars says sixty-five percent carbon and thirty-five percent aluminium, which is the same. The machine that weaves the structure is a laser-monitored circular loom with a hundred forty-four bobbins, built by Lexus engineers, according to their magazine.""",
   "Lexus LFA structure", "65% CARBON · 35% ALUMINIUM · A LOOM BUILT IN-HOUSE")
sc("""There is a cost in time that the car still carries. The Truth About Cars says carbon parts can take a day to produce, compared with seconds for stamped metal, and that the autoclave, a giant pressure cooker, caps production at about one car per day. Lexus says about five hundred cars were built over two years, roughly one per day. The two sources fit together well.""",
   "Autoclave", "AUTOCLAVE LIMIT: ~1 CAR PER DAY")

ch("The people")
sc("""Four people run through this story. Haruhiko Tanahashi, the chief engineer, who asked the question in the bar. Hiromu Naruse, the master driver, who shaped how the car drove and found it a champion. Akio Toyoda, who became that champion and the first test driver. And Atsushi Takada, who wrote the dossier that argued for the project to a room of about a hundred people.""",
   "Lexus LFA team", "TANAHASHI · NARUSE · TOYODA · TAKADA")
sc("""Lexus's magazine quotes Tanahashi on Akio: he may not be an engineer, but he knows what he likes and doesn't like. It is a modest sentence, and it explains something. The project was driven by a person with the authority to say yes, and the taste to say no. Without that combination, the kill list would have won one autumn.""",
   "Akio Toyoda", "\"HE MAY NOT BE AN ENGINEER, BUT HE KNOWS WHAT HE LIKES\"")
sc("""The magazine says Akio was promoted to vice president of product planning in two thousand five, the same year as the carbon decision. We do not know whether the promotion and the decision were connected, and the source does not say so. We note the coincidence of dates only. By our reading, it is at least consistent with a champion gaining the power to protect his project.""",
   "Toyota executive", "2005: AKIO PROMOTED · SAME YEAR AS THE CARBON DECISION")
sc("""There was also a workshop. The Truth About Cars says the LFA Works employs a hundred seventy people, and that series production began in December two thousand ten. By our arithmetic, a hundred seventy people building one car a day for five hundred cars is a small, specialised team, far from a normal Toyota line.""",
   "LFA Works", "LFA WORKS: 170 PEOPLE (TTAC)")

ch("The concepts, one by one")
sc("""Wikipedia and Lexus agree on the concepts. January two thousand five, Detroit, an aluminium concept. January two thousand seven, a second concept, with the carbon change and a mid-mounted engine. January two thousand eight, a roadster concept, which Lexus says previewed the speed-adaptive rear wing. Wikipedia adds that the trademark was filed in December two thousand eight.""",
   "Lexus LF-A roadster concept", "2005 · 2007 · 2008: THREE CONCEPTS BEFORE THE PRODUCTION CAR")
sc("""By our arithmetic, the gaps are two years, one year, and then nineteen months to Akio's confirmation of production on the fifth of August two thousand nine, and sixteen months more to the first production car. From the first concept to the first customer car is five years and eleven months. The public watched the LFA for nearly six years before they could buy one.""",
   "Lexus LFA concept", "FIRST CONCEPT TO PRODUCTION: 5 YEARS 11 MONTHS (OUR ARITHMETIC)")
sc("""A concept car is a promise the company can quietly break. Lexus showed three of them, and then built the car. That is not guaranteed. Many concepts never appear in showrooms. The LFA did, and the sources suggest it was only because people inside Toyota kept choosing to protect it, even while the board's focus was on volume.""",
   "Auto show", "MANY CONCEPTS NEVER REACH SHOWROOMS (OUR READING)")

ch("What the story cost, and what it bought")
sc("""Nobody in our sources publishes the cost of the project, so we will not guess. We know the car sold for three hundred seventy-five thousand dollars, per The Truth About Cars, and that five hundred were built. Multiply, and the revenue at list price is about one hundred eighty-seven million, five hundred thousand dollars, by our arithmetic. That is a revenue figure, not a profit.""",
   "Calculator", "500 × $375K ≈ $187.5M AT LIST PRICE (OUR ARITHMETIC)")
sc("""Whether the project made money, we cannot say. What we can say is what the Lexus magazine claims: the LFA streamlined engineering and development at Toyota, and inspired new directions for Lexus. That is a claim by the company about its own project. It may be true. We report it as a claim. The sources do not give a number to back it up.""",
   "Toyota engineers", "LEXUS CLAIMS THE LFA STREAMLINED TOYOTA'S ENGINEERING")
sc("""What it bought, in the end, was a reputation. Wikipedia says the final LFA sold in June two thousand twenty-three, more than ten years after production. In other videos of this series we showed that used cars have sold for more than double the original price. A project that began as a question in a bar became, for many enthusiasts, a symbol of what a car company can do when it takes a long view.""",
   "Lexus LFA", "A REPUTATION BUILT IN TEN YEARS (OUR READING)")
sc("""And the car's makers have not forgotten the lesson. Akio's comparison with the Ise Shrine, rebuilt every twenty years, is about renewal. Whether Toyota builds another car like the LFA is a question for the future, not for this video. What we can tell you is what happened in the first twelve years, and that it was made by people who did not know how it would end.""",
   "Ise Shrine", "RENEWAL, NOT AN ENDING (OUR READING)")

ch("The race that taught them")
sc("""While the car was being finished, Toyota went racing. Lexus says Naruse believed great cars are developed through road racing. In two thousand seven, Akio and Naruse founded Gazoo Racing to compete in the ADAC Nürburgring twenty-four hour race with LFA racing prototypes. Lexus's timeline lists entries in May two thousand eight, two thousand nine, two thousand ten and June two thousand eleven.""",
   "Nürburgring 24 Hours", "2007: GAZOO RACING FOUNDED · NÜRBURGRING 24H ENTRIES")
sc("""Akio raced under a pseudonym, Morizo, the magazine says. Wikipedia says the number fifteen car in two thousand nine finished with a driveshaft failure and a fire, and that the number fifty car won its class in two thousand ten. The Lexus article says LFAs won class victories in two thousand twelve and two thousand fourteen, but never the event outright.""",
   "Akio Toyoda racing", "AKIO RACED UNDER THE NAME \"MORIZO\"")
sc("""Note the disagreement. Wikipedia reports a class win in two thousand ten. Lexus's magazine mentions class victories in two thousand twelve and fourteen. They may be counting different classes or different cars, or one may simply be incomplete. We cannot resolve it, so we say only that the LFA won classes at the Nürburgring twenty-four hours, and that it never won the race outright.""",
   "Racing LFA", "SOURCES DISAGREE ON WHICH YEARS THE LFA WON ITS CLASS")

ch("Launch, and two losses")
sc("""On the fifth of August two thousand nine, Akio announced limited production, in a speech at the Center for Automotive Research in the United States, according to both Lexus and Wikipedia. The production car was unveiled at the Tokyo Motor Show on the twenty-first of October, and full specifications were confirmed. Production was limited to five hundred units, at a maximum of twenty a month.""",
   "Tokyo Motor Show 2009", "5 AUG 2009: PRODUCTION ANNOUNCED · OCT 2009: TOKYO")
sc("""Then came the human cost. Naruse died in a road accident near the Nürburgring in June two thousand ten, the timeline says, about six months before the launch. The other article gives his age as sixty-seven, and says he had been testing at the Nürburgring. Akio called him his right-hand man, and said that without him he felt so lonely.""",
   "Hiromu Naruse", "JUNE 2010: NARUSE DIES · \"WITHOUT HIM I FELT SO LONELY\"")
sc("""Another loss followed. Takashi Hata, a managing officer and Akio's longtime confidant, died of a degenerative bone disease weeks after Naruse, according to the article. We mention it because the source does, and because it shows that the people who made the LFA were living through their own story at the same time. We have no further details, and we will not invent any.""",
   "Toyota", "TAKASHI HATA ALSO DIED WEEKS LATER")
sc("""The first production car left the Motomachi line on the fifteenth of December two thousand ten. Lexus says Akio, brand ambassador Riyo Mori and a hundred fifty team members attended. By our own arithmetic, from the bar in February two thousand to that day is ten years and ten months. A hundred fifty people watching a car that had survived the kill list every autumn.""",
   "Motomachi plant", "15 DEC 2010: FIRST PRODUCTION CAR · 150 TEAM MEMBERS")

ch("The last car, and what it left behind")
sc("""The Nürburgring Package came next. Lexus's timeline says it was announced in March two thousand ten, shown at Geneva in March two thousand eleven, limited to fifty, with five hundred sixty-two brake horsepower. Test driver Akira Iida recorded seven fourteen point six four in August two thousand eleven, which Lexus says was then the fastest lap by a production car. Wikipedia lists sixty-four built, and a September confirmation.""",
   "Lexus LFA Nürburgring Package", "NÜRBURGRING PACKAGE: 7:14.64 · 50 PLANNED, 64 BUILT (WIKIPEDIA)")
sc("""The last LFA, a white Nürburgring Package, left the Motomachi line on the fourteenth of December two thousand twelve, the timeline says, exactly two years after production began. Wikipedia gives two end dates, the fourteenth and seventeenth. We use the Lexus date. Each car, the article adds, was built to order, with allegedly thirty billion possible configurations.""",
   "Lexus LFA final car", "14 DEC 2012: LAST LFA, A WHITE NÜRBURGRING PACKAGE")
sc("""The magazine also says Lexus keeps a three thousand, five hundred page reference document for each vehicle. That is the other side of the story. A car conceived in a bar was documented, at the end, to a degree that few cars ever are. By our arithmetic, five hundred cars at three thousand, five hundred pages each is one point seven five million pages.""",
   "Lexus documents", "3,500 PAGES PER CAR × 500 = 1.75M PAGES (OUR ARITHMETIC)")
sc("""What did the car leave behind? The Lexus magazine says it streamlined engineering and development at Toyota and inspired new directions for Lexus. And Akio compared it to the twenty-year rebuilding cycle of the Ise Shrine. He noted that the Toyota two thousand G T from the nineteen sixties and the Supra from the nineteen eighties followed a similar pattern, and said a new supercar would come in about twenty years.""",
   "Ise Shrine", "AKIO: A NEW SUPERCAR IN ~20 YEARS (LEXUS MAGAZINE)")
sc("""By our arithmetic, twenty years from December two thousand twelve is twenty thirty-two. That is a statement of intent, quoted in a Lexus magazine, not a commitment, and we found no source that gives a date for a successor. We mention it because it tells you how the people behind the LFA thought: in cycles of decades, not model years.""",
   "Lexus", "~2032: AKIO'S SUGGESTED TIMESCALE (OUR ARITHMETIC)")
sc("""Look at what the numbers add up to. A project begun over drinks in February two thousand. A prototype in June two thousand three. A decision to go all in on carbon in two thousand five. A launch in December two thousand ten. A final car in December two thousand twelve. Five hundred cars. Two deaths along the way. And a car that is now worth more than when new.""",
   "Lexus LFA", "2000 → 2012: FROM A BAR TO 500 CARS")
sc("""One caution. We have not been inside Toyota. We have read what Wikipedia, Lexus's own magazine and an outside journalist wrote, and where they differ we have said so. A story like this one grows with retelling, and some details may be softened or sharpened. We have tried to give you what is on the record, and to keep our own reading labelled.""",
   "Lexus LFA", "THE RECORD, NOT THE LEGEND")
sc("""What part of the story surprised you most, the bar, the kill list, or the carbon decision? Tell us in the comments. In the other videos of this series, we reveal two things you did not know about the LFA, compare it with the Nissan GT-R, and explain why it is worth more now than new. Our twenty twenty-seven Truck Buyer's Guide is linked in the description. Subscribe to Pickup Reality.""",
   "Ford F-150", "SUBSCRIBE: PICKUP REALITY")

save("video108", "The Insane Story Behind the Lexus LFA", [
    "Wikipedia, Lexus LFA: https://en.wikipedia.org/wiki/Lexus_LFA",
    "Lexus UK Magazine, Untold history of the Lexus LFA: https://mag.lexus.co.uk/untold-history-of-the-lexus-lfa",
    "Lexus UK Magazine, Lexus LFA timeline: redefining the Japanese supercar: https://mag.lexus.co.uk/lexus-lfa-timeline/",
    "The Truth About Cars, The making of the Lexus LFA supercar, chapter 1 (9 July 2012): https://thetruthaboutcars.com/2012/07/the-making-of-the-lexus-lfa-supercar-who-what-where-and-most-of-all-why-an-inside-report-chapter-1-from-a-bar-to-bar-none/",
    "Lexus UK Magazine, Engineering innovations: the Lexus carbon loom: https://mag.lexus.co.uk/engineering-innovations-the-lexus-carbon-loom",
], "D")
