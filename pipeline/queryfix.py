"""Rewrite the photo-search query of every scene in videos/videoNN/script.json.

sc()'s 2nd argument is searched on Wikimedia Commons (pipeline/fetch_media.py), so it must name something
photographable. Many phase-2 scripts used section labels there ("Timeline"). Per topic group we keep a list of
(regex, query) rules: the rule whose regex matches the narration most often wins; scenes matching none cycle
through the group's default queries. The old query is kept as "orig_query"."""
import json, re, sys, pathlib

G = {}
def grp(nums, rules, default):
    G[tuple(nums)] = (rules, default)

grp([102], [(r"Valkyrie|Newey|Gaydon", "Aston Martin Valkyrie"), (r"Formula|Hamilton|Mercedes-AMG Petronas|F1", "Mercedes-AMG Petronas W08"), (r"Affalterbach", "AMG Affalterbach")],
    ["Mercedes-AMG One", "Mercedes-AMG Project One", "Aston Martin Valkyrie", "Mercedes-AMG One rear", "Mercedes-AMG One interior"])
grp([108], [(r"Nurburgring|N.rburgring", "Nürburgring Nordschleife"), (r"Yamaha", "Yamaha engine"), (r"Toyoda", "Akio Toyoda"), (r"Fuji", "Fuji Speedway")],
    ["Lexus LFA", "Lexus LFA interior", "Lexus LFA rear", "Lexus LFA engine", "Lexus LFA side"])
grp(range(130, 133), [(r"Tuatara", "SSC Tuatara"), (r"Veyron", "Bugatti Veyron Super Sport"), (r"Chiron", "Bugatti Chiron"), (r"Koenigsegg|Agera", "Koenigsegg Agera RS"), (r"Kennedy|Shuttle|Cape Canaveral", "Kennedy Space Center runway"), (r"Texas|Sealy", "Texas road"), (r"Nardo", "Nardò Ring"), (r"Hennessey|Venom", "Hennessey Venom F5")],
    ["Hennessey Venom F5", "SSC Tuatara", "Bugatti Chiron Super Sport", "Hennessey Venom GT", "Bugatti Veyron", "Koenigsegg Agera"])
grp([135, 136], [(r"Chiron", "Bugatti Chiron"), (r"EB110", "Bugatti EB110"), (r"Wolfsburg|Piech|Piëch", "Volkswagen Wolfsburg"), (r"Molsheim", "Molsheim Bugatti"), (r"Super Sport|Vitesse", "Bugatti Veyron Super Sport")],
    ["Bugatti Veyron", "Bugatti Veyron 16.4", "Bugatti Veyron interior", "Bugatti Veyron rear", "Bugatti Veyron engine", "Bugatti Veyron Grand Sport"])
grp([138, 140], [(r"LaFerrari", "Ferrari LaFerrari"), (r"P1", "McLaren P1"), (r"918", "Porsche 918 Spyder"), (r"Nurburgring|N.rburgring", "Nürburgring Nordschleife"), (r"Weissach", "Porsche Weissach")],
    ["Porsche 918 Spyder", "Ferrari LaFerrari", "McLaren P1", "Porsche 918 Spyder rear", "Porsche 918 Spyder interior", "McLaren P1 rear"])
grp(range(141, 145), [(r"Raptor", "Ford F-150 Raptor"), (r"Hellcat", "Dodge Challenger Hellcat engine"), (r"Silverado|Chevrolet", "Chevrolet Silverado"), (r"Jeep", "Jeep Gladiator"), (r"jump|desert|Baja", "Ford Raptor desert jump"), (r"Ram 1500|TRX|Ram", "Ram 1500 TRX")],
    ["Ram 1500 TRX", "Ford F-150 Raptor R", "Ram TRX rear", "Ram TRX interior", "Ford Raptor R", "Ram 1500 TRX front"])
grp(range(145, 149), [(r"Cullinan|Rolls", "Rolls-Royce Cullinan"), (r"Urus", "Lamborghini Urus"), (r"Roma", "Ferrari Roma"), (r"Montezemolo", "Luca di Montezemolo"), (r"Maranello", "Maranello Ferrari factory"), (r"Purosangue", "Ferrari Purosangue")],
    ["Ferrari Purosangue", "Rolls-Royce Cullinan", "Ferrari Purosangue rear", "Ferrari Purosangue interior", "Rolls-Royce Cullinan interior", "Lamborghini Urus"])
grp(range(149, 153), [(r"VelociRaptor|Hennessey", "Ford F-150 Raptor"), (r"Brabus", "Brabus G-Class"), (r"Graz|Magna|Puch", "Magna Steyr Graz"), (r"Land Rover|Defender", "Land Rover Defender"), (r"Unimog", "Mercedes Unimog"), (r"Mercedes|G63|G-Class|AMG", "Mercedes-Benz G63 AMG 6x6")],
    ["Mercedes-Benz G63 AMG 6x6", "Brabus G63 AMG 6x6", "Mercedes-Benz G-Class", "Mercedes-AMG G 63 6x6 rear", "Ford F-150 Raptor", "Hennessey VelociRaptor"])
grp(range(153, 157), [(r"Cybertruck", "Tesla Cybertruck"), (r"Giugiaro", "Giorgetto Giugiaro"), (r"Lotus|Chapman", "Lotus Esprit"), (r"Belfast|Dunmurry|Northern Ireland", "Belfast"), (r"Back to the Future|Marty|Doc Brown|Hollywood", "DeLorean Back to the Future"), (r"Musk|Tesla", "Tesla Cybertruck"), (r"John DeLorean", "John DeLorean"), (r"Pontiac", "Pontiac GTO"), (r"stainless", "DeLorean DMC-12 stainless steel")],
    ["DeLorean DMC-12", "Tesla Cybertruck", "DeLorean DMC-12 rear", "DeLorean DMC-12 interior", "Tesla Cybertruck rear", "DeLorean DMC-12 gull-wing door"])
grp(range(157, 161), [(r"Regera", "Koenigsegg Regera"), (r"Jesko", "Koenigsegg Jesko"), (r"Agera", "Koenigsegg Agera"), (r"CC8S|CCX|One:1", "Koenigsegg CCX"), (r"Angelholm|Ängelholm|hangar|Swed", "Ängelholm"), (r"Christian", "Christian von Koenigsegg"), (r"Gemera", "Koenigsegg Gemera")],
    ["Koenigsegg Gemera", "Koenigsegg Regera", "Koenigsegg Gemera interior", "Koenigsegg Regera rear", "Koenigsegg Jesko", "Koenigsegg Agera"])
grp(range(161, 165), [(r"Goldfinger|Connery|Bond|007|Skyfall", "Aston Martin DB5 James Bond"), (r"Gaydon", "Aston Martin Gaydon"), (r"Newport Pagnell", "Newport Pagnell"), (r"DB12", "Aston Martin DB12"), (r"DB4|DB6|DB9|DB11", "Aston Martin DB11"), (r"Bentley", "Bentley Continental GT"), (r"E-Type|Jaguar", "Jaguar E-Type"), (r"Volante|convertible", "Aston Martin DB5 Volante")],
    ["Aston Martin DB5", "Aston Martin DB12", "Aston Martin DB5 interior", "Aston Martin DB5 rear", "Aston Martin DB12 interior", "Aston Martin DB5 engine"])
grp(range(165, 169), [(r"Huracan|Huracán|STO", "Lamborghini Huracán STO"), (r"Murcielago|Murciélago", "Lamborghini Murciélago"), (r"Miura", "Lamborghini Miura"), (r"Revuelto", "Lamborghini Revuelto"), (r"Ultimae", "Lamborghini Aventador Ultimae"), (r"SVJ", "Lamborghini Aventador SVJ"), (r"Nurburgring|N.rburgring|Ring", "Nürburgring Nordschleife"), (r"Felicity Ace|ship", "Car carrier ship"), (r"Sant'Agata", "Sant'Agata Bolognese Lamborghini"), (r"Pebble Beach|Monterey", "Pebble Beach Concours")],
    ["Lamborghini Aventador SVJ", "Lamborghini Huracán STO", "Lamborghini Aventador", "Lamborghini Aventador SVJ rear", "Lamborghini Huracán STO rear", "Lamborghini Aventador interior"])
grp(range(169, 173), [(r"240Z|Fairlady|Datsun|Katayama", "Datsun 240Z"), (r"Goertz", "Albrecht Goertz"), (r"Connery|Bond|You Only Live Twice|Aki", "Toyota 2000GT You Only Live Twice"), (r"Shelby", "Shelby Cobra"), (r"E-Type|Jaguar", "Jaguar E-Type"), (r"Porsche|911", "Porsche 911"), (r"Mazda|767B", "Mazda 767B"), (r"Celica", "Toyota Celica"), (r"Yamaha|Iwata", "Toyota 2000GT engine"), (r"Gazoo|GR ", "Toyota GR Yaris"), (r"Toyota 7", "Toyota 7"), (r"Tokyo Motor Show", "Tokyo Motor Show"), (r"Suzuka", "Suzuka Circuit"), (r"Yatabe", "Yatabe test track"), (r"Silvia", "Nissan Silvia CSP311"), (r"Z432|S20", "Nissan Fairlady Z432"), (r"Crown", "Toyota Crown")],
    ["Toyota 2000GT", "Toyota 2000GT interior", "Toyota 2000GT rear", "Toyota 2000GT engine", "Toyota 2000GT side", "Toyota 2000GT front"])
grp(range(173, 177), [(r"F50", "Ferrari F50"), (r"F40", "Ferrari F40"), (r"LaFerrari", "Ferrari LaFerrari"), (r"MC12|Maserati", "Maserati MC12"), (r"FXX", "Ferrari FXX"), (r"Schumacher", "Michael Schumacher Ferrari"), (r"Montezemolo", "Luca di Montezemolo"), (r"Pininfarina", "Pininfarina"), (r"Maranello|Fiorano", "Ferrari Maranello"), (r"Paris", "Paris Motor Show"), (r"Okuyama", "Ken Okuyama"), (r"Enzo", "Ferrari Enzo")],
    ["Ferrari Enzo", "Ferrari F50", "Ferrari Enzo interior", "Ferrari Enzo rear", "Ferrari F50 rear", "Maserati MC12"])

def fix(path):
    path = pathlib.Path(path)
    n = int(re.findall(r"video(\d+)", str(path))[0])
    key = next((k for k in G if n in k), None)
    if not key: return None
    rules, default = G[key]
    d = json.loads(path.read_text())
    for i, s in enumerate(d["scenes"]):
        s.setdefault("orig_query", s["query"])
        best, bc = None, 0
        for rx, q in rules:
            c = len(re.findall(rx, s["text"]))
            if c > bc: best, bc = q, c
        s["query"] = best or default[i % len(default)]
    path.write_text(json.dumps(d, indent=1))
    return d

if __name__ == "__main__":
    for p in sys.argv[1:]:
        d = fix(p)
        if d: print(p, [s["query"] for s in d["scenes"]])
