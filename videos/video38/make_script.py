import json
S = []
def sc(text, query, caption):
    S.append({"text": " ".join(text.split()), "query": query, "caption": caption})

# ---------- HOOK ----------
sc("""The most American pickup truck you can buy in twenty twenty-six is not a Ford. It is not a Chevy. And it is not a Ram. A Toyota built in Texas now ranks ahead of every Silverado. A Honda built in Alabama beats the F-150. And one of America's best-selling heavy-duty trucks is built in Mexico. So which trucks are really built in America?""",
   "Toyota Tundra 2022", "MADE IN AMERICA?")

# ---------- COLD OPEN ----------
sc("""For decades, truck commercials have sold one idea above everything else. American trucks, built by American workers, for American roads. Flags, factories, and the words built Ford tough, or like a rock. But a truck's badge says very little about where it was actually built, where its engine came from, or where its parts were made.""",
   "Ford F-150 assembly line", "THE BADGE vs THE FACTORY")
sc("""In this video, we follow the trucks to their factories. We look at the two big rankings of American-made vehicles for twenty twenty-six, which pickups are built in Mexico and Canada, how the tariff war changed the math, and the billions of dollars automakers are now spending to bring truck production home. Every number is sourced in the description.""",
   "Dearborn Truck Plant", "WHERE ARE TRUCKS REALLY BUILT?")
sc("""And here is the first surprise. Depending on which ranking you trust, the most American truck is either a Jeep or a Tesla. The two rankings measure very different things, and that difference changes the whole answer. Let's start with how you even measure an American truck.""",
   "Jeep Gladiator", "A JEEP OR A TESLA?")

# ---------- 1. HOW IT IS MEASURED ----------
sc("""Every new car and light truck sold in the United States carries a label required by the American Automobile Labeling Act of nineteen ninety-four. That label lists four things. The percentage of United States and Canadian parts content, the final assembly location, and the country of origin of the engine and the transmission. It is printed right on the window sticker.""",
   "Monroney sticker", "THE LABEL ON EVERY WINDOW STICKER")
sc("""Notice something strange. The law treats the United States and Canada as one region. A part made in Ontario counts the same as a part made in Ohio. So a truck can show a high domestic parts number even if a large share of those parts crossed the northern border.""",
   "Ambassador Bridge Detroit Windsor", "CANADA COUNTS AS DOMESTIC")
sc("""Cars dot com builds its American-Made Index on top of that data. It ranks vehicles on five factors. Final assembly location, the percentage of United States and Canadian parts, the origin of the engines, the origin of the transmissions, and the size of the United States manufacturing workforce behind the vehicle.""",
   "car assembly plant workers", "CARS.COM: 5 FACTORS")
sc("""For twenty twenty-six, Cars dot com studied three hundred seventy-nine model-year vehicles and narrowed its main list to eighty-six base nameplates. That is down from four hundred vehicles and ninety-nine ranked vehicles in twenty twenty-five. Fewer vehicles qualified as American-made this year than last year.""",
   "car dealership lot", "ONLY 86 NAMEPLATES QUALIFIED")
sc("""But here is a catch for truck buyers. Cars dot com excludes vehicles with a gross vehicle weight rating above eight thousand five hundred pounds. That means heavy-duty pickups like the Super Duty, the Silverado twenty-five hundred, and the Ram twenty-five hundred are not ranked at all. The trucks that do the hardest work are left out of the most famous American-made list.""",
   "Ford Super Duty", "HEAVY-DUTY TRUCKS: NOT RANKED")
sc("""The second ranking comes from the Kogod School of Business at American University. Its Made in America Auto Index starts with the same federal label data, but it adds other measures, including where the company keeps its profits and where it does its research and development. A truck built in Texas by a company based in Japan loses points under that formula.""",
   "American University Washington", "KOGOD: PROFITS AND R&D COUNT")

# ---------- 2. THE MOST AMERICAN PICKUPS ----------
sc("""So, which pickups rank highest on the Cars dot com list? Number one among trucks, and number three overall, is the Jeep Gladiator, built in Toledo, Ohio. It climbed from fifth place in twenty twenty-five. The Gladiator is the most American pickup truck on the twenty twenty-six American-Made Index.""",
   "Jeep Gladiator Rubicon", "No. 3 OVERALL: JEEP GLADIATOR")
sc("""Number two among pickups, and fifth overall, is the Honda Ridgeline, built in Lincoln, Alabama. It rose from seventh place. So the second most American truck on the list comes from a Japanese automaker, and it is a unibody pickup that shares its basic structure with a crossover.""",
   "Honda Ridgeline", "No. 5 OVERALL: HONDA RIDGELINE")
sc("""But there is a twist about the Ridgeline. According to Pickup Truck plus SUV Talk, Honda may pause Ridgeline production in the fourth quarter of twenty twenty-six, because the current truck may not meet upcoming emissions regulations. The pause could last about eighteen months, with production restarting around the third quarter of twenty twenty-eight. One of the most American trucks could disappear for a year and a half.""",
   "Honda Ridgeline 2024", "PRODUCTION PAUSE: 18 MONTHS?")
sc("""Now the biggest surprise. The first full-size pickup on the list is the Toyota Tundra, built in San Antonio, Texas. The gas Tundra ranks nineteenth overall, up thirty-two places from fifty-first in twenty twenty-five. Pickup Truck plus SUV Talk called it the most American full-size pickup on the list.""",
   "Toyota Tundra TRD Pro", "No. 19: TOYOTA TUNDRA")
sc("""Next come the Hyundai Santa Cruz from Montgomery, Alabama, at twenty-fourth, and the GMC Canyon from Wentzville, Missouri, at twenty-fifth. So before you reach the first Ford on the list, you pass a Jeep, a Honda, a Toyota, a Hyundai, and a GMC midsize truck.""",
   "Hyundai Santa Cruz", "No. 24 SANTA CRUZ, No. 25 CANYON")

sc("""And notice something else about the Tundra. The gas version ranks nineteenth, but the Tundra Hybrid, built in the very same San Antonio plant, ranks forty-ninth. Same factory, same workers, thirty places apart. So the gap has to come from the other factors, like parts, the powertrain and the workforce. Further down, the Nissan Frontier from Canton, Mississippi, ranks sixty-third, up eight places from last year.""",
   "Toyota Tundra Hybrid", "SAME PLANT, 30 PLACES APART")

# ---------- 3. THE BIG THREE SURPRISE ----------
sc("""Then the F-150 family arrives. The F-150 Hybrid, built in Dearborn, Michigan, ranks twenty-seventh, up thirty-four places. The regular F-150, built in Claycomo, Missouri, or Dearborn, ranks twenty-eighth. The Ford Ranger from Wayne, Michigan, is twenty-ninth. And the Chevrolet Colorado from Wentzville is thirtieth, down eleven places.""",
   "Ford F-150 Hybrid", "F-150: No. 28")
sc("""Here is the next twist. The Ram fifteen hundred, built in Sterling Heights, Michigan, ranks fifty-fifth, ten places lower than last year. A truck built just outside Detroit sits behind a Hyundai, a Honda and a Toyota. Final assembly in Michigan is only one of the five factors. Parts, engines, transmissions and workforce count too.""",
   "Ram 1500 2025", "RAM 1500: No. 55")
sc("""And now the most surprising result of all. The Chevrolet Silverado fifteen hundred, one of the two best-selling trucks in America, ranks near the very bottom, in the eighties, behind the Nissan Frontier from Canton, Mississippi. Its sister truck, the GMC Sierra fifteen hundred, also falls in the high seventies.""",
   "Chevrolet Silverado 1500", "SILVERADO 1500: NEAR THE BOTTOM")
sc("""Why? Look at the assembly locations. According to the index, the Silverado fifteen hundred is built in Roanoke, Indiana, in Oshawa, Canada, or in Silao, Mexico. The Sierra fifteen hundred is built in Roanoke or in Silao. When you buy a Silverado, the truck in front of you may have come from any of three countries.""",
   "Chevrolet Silverado Trail Boss", "BUILT IN 3 COUNTRIES")
sc("""So here is a fact that would surprise most truck buyers. In twenty twenty-six, a Toyota from Texas ranks as more American than a Chevrolet Silverado on the Cars dot com index. A Honda ranks higher than the F-150. And the most American Ram product is not a Ram at all. It is the Jeep Gladiator, from the same company.""",
   "Toyota Tundra", "TOYOTA > SILVERADO?")

# ---------- 4. BUILT IN MEXICO ----------
sc("""Now let's talk about the trucks that are not on the list at all. Two popular pickups are missing completely, because they are assembled in Mexico. The Ford Maverick and the Toyota Tacoma. America's favorite small truck, and America's favorite midsize truck, are both built south of the border.""",
   "Ford Maverick", "NOT ON THE LIST: MAVERICK")
sc("""The Maverick is built at Ford's plant in Hermosillo, in the state of Sonora. And when tariffs hit, buyers felt it. In May twenty twenty-five, Ford told dealers it would raise prices on three Mexican-built models, the Maverick, the Bronco Sport, and the Mustang Mach-E. The Maverick XLT with all-wheel drive went up seven hundred dollars. Ford said some models could rise by up to two thousand dollars.""",
   "Ford Maverick XLT", "MAVERICK: BUILT IN HERMOSILLO")
sc("""The Tacoma tells a similar story. According to Automotive World, Toyota's plant in Baja California, Mexico, built one hundred sixty-six thousand, six hundred fifty-three Tacomas last year. A second plant in Guanajuato, Mexico, also builds Tacomas for export to the United States. The best-selling midsize pickup in America is a Mexican-built truck.""",
   "Toyota Tacoma 2024", "TACOMA: 166,653 BUILT IN BAJA")
sc("""And the heavy-duty market depends on Mexico even more. According to S and P Global data cited by Bloomberg, Stellantis built two hundred six thousand, nine hundred sixty-two Ram twenty-five hundred and thirty-five hundred trucks at its plant in Saltillo, Mexico, in a single year. Ram also builds its forty-five hundred and fifty-five hundred chassis cab trucks in Mexico.""",
   "Ram 2500", "RAM HD: 206,962 FROM SALTILLO")
sc("""And GM is not purely domestic either. According to Pickup Truck plus SUV Talk, some GMC heavy-duty trucks are built in Silao, Mexico. But GM also assembled about two hundred sixty-six thousand Silverado and Sierra twenty-five hundred and thirty-five hundred trucks in the United States.""",
   "GMC Sierra 2500HD", "GM HD: 266,000 BUILT IN THE U.S.")
sc("""Ford's Super Duty, meanwhile, is built at the Kentucky Truck Plant in Louisville. And Ford builds its F-six fifty and F-seven fifty medium-duty trucks in Avon Lake, Ohio. So among heavy-duty pickups, Ford and GM build mostly in the United States, while Ram builds its heavy-duty trucks mainly in Mexico. That difference was about to become a very big deal.""",
   "Ford F-650", "SUPER DUTY: LOUISVILLE, KENTUCKY")

# ---------- 5. THE TARIFF WAR ----------
sc("""In twenty twenty-five, the United States put a twenty-five percent tariff on imported vehicles. For trucks from Canada and Mexico that qualify under the trade agreement, the tariff applies to the parts content that is not American. Then in October twenty twenty-five, the administration announced a separate twenty-five percent tariff on imported medium and heavy-duty trucks, starting November first.""",
   "cargo ship cars port", "25% TARIFF")
sc("""That truck tariff followed a Section two thirty-two investigation by the Commerce Department into trucks over ten thousand pounds. The top five sources of imported trucks were Mexico, Canada, Japan, Germany, and Finland. The administration described the imports as a threat to national security.""",
   "semi truck highway", "TOP SOURCE: MEXICO")
sc("""And here is where the Detroit Three turned on each other. According to Pickup Truck plus SUV Talk, Ford CEO Jim Farley supported the tariff, saying it would help Ford's United States manufacturing. GM was described as largely unaffected. But Stellantis, which imports many Ram heavy-duty trucks from Mexico, reportedly asked for a waiver.""",
   "Jim Farley Ford", "FORD AND GM vs RAM")
sc("""Ford and GM reportedly argued that a waiver would give Stellantis an unfair cost advantage. Think about that. For years, the Detroit automakers fought together over trade. In twenty twenty-five, two of them pushed back against the third, over trucks built in Mexico.""",
   "Ram 3500 dually", "DETROIT DIVIDED")
sc("""And the tariffs did not only hit Mexico. Ford spent years preparing its Oakville plant in Ontario, Canada, to build Super Duty trucks. According to Ford Authority, vehicles exported from Canada to the United States face a twenty-five percent tariff on their non-American parts content. Ford's original estimate for the Oakville project was about four point one billion Canadian dollars. Ford now expects to spend about five billion.""",
   "Ford Oakville Assembly", "OAKVILLE: C$5 BILLION")
sc("""Here is the twist. While other automakers rushed to move production into the United States, Ford was adding Super Duty production in Canada. Six pre-production Super Duty trucks came off the Oakville line in April twenty twenty-six, and thirty-seven more in May. The plant is expected to reach up to one hundred thousand trucks a year, with some exported to the United States. Part of America's toughest Ford may soon come from Canada.""",
   "Ford F-250 Super Duty", "A CANADIAN SUPER DUTY")

# ---------- 6. COMING HOME ----------
sc("""Now the other side of the story. The tariffs started a wave of truck investment in the United States. On June tenth, twenty twenty-five, GM announced four billion dollars across three American plants. The biggest change is at Orion Assembly in Michigan, which had been planned for electric trucks. It will build gas-powered full-size pickups and SUVs instead, starting in early twenty twenty-seven.""",
   "Orion Assembly", "GM: $4 BILLION, ORION 2027")
sc("""GM also said it would increase United States production of full-size light-duty pickups in Fort Wayne, Indiana, and move production out of Mexico because of the tariffs. When all three plants are running, GM says it will be able to build more than two million vehicles a year in the United States, and add three to four thousand jobs.""",
   "GM Fort Wayne Assembly", "MOVING PICKUPS OUT OF MEXICO")
sc("""Then in October twenty twenty-five, Stellantis announced thirteen billion dollars over four years, the largest investment in its one-hundred-year American history. It promised a fifty percent increase in its United States vehicle production, five new vehicles, and more than five thousand new jobs.""",
   "Stellantis Sterling Heights Assembly", "STELLANTIS: $13 BILLION")
sc("""For trucks, the key line is in Toledo, Ohio. Stellantis said an all-new midsize truck will be built at the Toledo Assembly Complex starting in twenty twenty-eight, next to the Jeep Wrangler and Gladiator, with more than nine hundred new jobs. That truck was originally planned for the Belvidere plant in Illinois. The company did not name the brand in its announcement.""",
   "Toledo Assembly Complex", "NEW MIDSIZE TRUCK: TOLEDO 2028")
sc("""And Toyota made the biggest truck move of twenty twenty-six. In July, Toyota announced a three point six billion dollar plant at its San Antonio, Texas campus, where the Tundra is built. Tacoma production will move there from Baja California. The new facility is due to open by twenty thirty, adding about one hundred fifty thousand trucks a year and about two thousand jobs.""",
   "Toyota Motor Manufacturing Texas", "TOYOTA: $3.6 BILLION IN TEXAS")
sc("""Toyota's North America president, Ted Ogawa, called it deepening our commitment to American manufacturing. With this plant, Toyota's total investment in San Antonio reaches eight point three billion dollars. And Automotive World noted that vehicles shipped from Mexico face tariffs of up to twenty-five percent, which have weighed on Toyota's margins.""",
   "Toyota Tacoma TRD Pro", "TACOMA COMING TO TEXAS BY 2030")
sc("""So here is the strange result. By the end of this decade, the Tacoma may be built in Texas, while part of Ford's Super Duty production comes from Canada. The Japanese midsize truck could become more American, while a piece of the most famous American heavy-duty truck moves north.""",
   "Toyota Tacoma", "THE MAP IS FLIPPING")

# ---------- 7. THE KOGOD ANSWER ----------
sc("""Now back to that second ranking, because it tells a completely different story. On the twenty twenty-six Kogod Made in America Auto Index, the top spots belong to Tesla. The Model three is first. And the most American pickup on the Kogod list is the Tesla Cybertruck, tied for third place overall, built in Austin, Texas.""",
   "Tesla Cybertruck", "KOGOD No. 3: CYBERTRUCK")
sc("""The Jeep Gladiator is fourth on the Kogod list. And the Ford Ranger, built in Wayne, Michigan, is tied for sixth, alongside the Bronco and the Model X. Kogod says Tesla took six places in the top ten for the first time.""",
   "Ford Ranger 2024", "KOGOD: GLADIATOR 4th, RANGER 6th")
sc("""And the Kogod list shows how much moving a factory matters. The Volkswagen ID four jumped from thirty-third place in twenty twenty-five to tenth in twenty twenty-six. The reason, according to Kogod, is that production moved from Germany to Tennessee. Change the factory, and a vehicle can climb twenty-three places in a single year.""",
   "Volkswagen ID.4", "ID.4: No. 33 TO No. 10")
sc("""Why is Kogod so different? Because it counts where the money goes. Look at the average total domestic content by brand for twenty twenty-six. Tesla scores eighty-four. Ford sixty-three. Stellantis sixty. GM fifty-four. Honda fifty-three. Toyota only twenty-three, and Nissan twenty-two.""",
   "Tesla Gigafactory Texas", "TESLA 84 / FORD 63 / TOYOTA 23")
sc("""So here is the twist. On Cars dot com, a Texas-built Tundra beats a Silverado by more than sixty places. On Kogod, Toyota as a brand scores far below GM. Both rankings are honest. One asks where the truck was built. The other asks where the profits and the engineering stay. Your answer depends on which question matters to you.""",
   "Toyota Tundra 2024", "TWO RANKINGS, TWO ANSWERS")
sc("""And look at GM's history on the Kogod index. GM averaged sixty-six in twenty fifteen, fell to fifty-three in twenty twenty-five, and sits at fifty-four in twenty twenty-six. Ford fell from sixty-five to fifty-five, then climbed back to sixty-three. Stellantis went from sixty to fifty and back to sixty. Over the last decade, the Detroit brands became less American, and only now are coming back.""",
   "Chevrolet Silverado 2019", "GM: 66 IN 2015, 54 NOW")
sc("""And the rules may change again. According to Kogod, in June twenty twenty-six the United States proposed raising the regional content requirement under the trade agreement with Mexico and Canada from seventy-five to eighty-two percent, with at least fifty percent American content. If that happens, trucks built in Mexico and Canada would have to use far more American parts.""",
   "Mexico United States border trucks", "PROPOSED: 82% REGIONAL CONTENT")

# ---------- 8. WHAT IT MEANS FOR BUYERS ----------
sc("""So what does all of this mean if you are shopping for a truck? First, read the window sticker. The American Automobile Labeling Act section shows the parts content, the assembly plant, and where the engine and transmission were made. It takes thirty seconds, and it tells you more than any commercial.""",
   "window sticker new car", "1. READ THE STICKER")
sc("""Second, check the first character of the vehicle identification number. A one, a four or a five means the truck was built in the United States. A two means Canada. A three means Mexico. Two trucks with the same name, on the same lot, can have different first digits. That is especially true for the Silverado and Sierra fifteen hundred.""",
   "vehicle identification number", "2. CHECK THE VIN: 1, 4, 5 = USA")
sc("""Third, remember that built in America does not always mean cheaper or better. Tariffs raised the prices of some Mexican-built trucks, like the Maverick. But American plants also need investment, and new plants take years. Toyota's Texas Tacoma line will not open until twenty thirty, and GM's Orion pickups start in twenty twenty-seven.""",
   "pickup trucks dealership", "3. AMERICAN ≠ CHEAPER")
sc("""And fourth, if buying American matters to you, choose your ranking first. If you care about the factory and the workers, the Cars dot com list points you to the Gladiator, the Ridgeline, the Tundra and the F-150. If you care about where the profits and engineering stay, the Kogod list points you to the Cybertruck, the Gladiator, and the Ranger.""",
   "Jeep Gladiator Mojave", "4. PICK YOUR RANKING")

# ---------- CLOSE ----------
sc("""So, which trucks are really built in America? The answer is messier than any ad. The Jeep Gladiator is the most American pickup on one list, and the Cybertruck on the other. A Toyota beats a Chevy. A Honda beats a Ford. America's favorite small and midsize trucks come from Mexico, and most Ram heavy-duty trucks do too. And one of the best-selling trucks in America comes from three different countries.""",
   "Jeep Gladiator", "THE VERDICT")
sc("""And the final twist. The map is being redrawn right now. GM is moving pickups out of Mexico. Toyota is bringing the Tacoma to Texas. Stellantis is building a new midsize truck in Ohio. And Ford is adding Super Duty production in Canada. The truck you buy in twenty thirty may be built somewhere completely different from the truck you buy today.""",
   "pickup truck factory", "THE MAP IS CHANGING")
sc("""We put the assembly plant, the parts content, and the engine origin of every twenty twenty-seven pickup into the Twenty Twenty-Seven Truck Buyer's Guide. The link is in the description and in the pinned comment. Subscribe, because next we look at the future of the V8. And tell us in the comments, does it matter to you where your truck was built? Thanks for watching.""",
   "Ford F-150 pickup truck", "2027 TRUCK BUYER'S GUIDE: LINK BELOW")

CH = {"The most American pickup truck you can buy": "Intro", "Every new car and light truck sold": "How 'American' is measured",
      "So, which pickups rank highest": "The most American pickups", "Then the F-150 family arrives": "The Big Three surprise",
      "Now let's talk about the trucks that are not": "Built in Mexico", "In twenty twenty-five, the United States put": "The tariff war",
      "Now the other side of the story": "Bringing trucks home", "Now back to that second ranking": "The Kogod answer",
      "So what does all of this mean": "What it means for buyers", "So, which trucks are really built": "The verdict"}
CUTS = {0: 8, 1: 8, 2: 5, 3: 4}
for idx, s in enumerate(S):
    if idx in CUTS: s["cuts"] = CUTS[idx]
    for k, v in CH.items():
        if s["text"].startswith(k): s["chapter"] = v
json.dump({"id": "video38", "length_scale": 1.4,
  "title": "Which Trucks Are Really Built in America? (A Toyota Beats the Silverado)", "scenes": S},
  open("script.json", "w"), indent=1)
words = sum(len(s["text"].split()) for s in S)
print(len(S), "scenes", words, "words", round(words*1.4/197,1), "min")
