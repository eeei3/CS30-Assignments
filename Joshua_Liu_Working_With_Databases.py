Marvel_Superheros = {
  "Spiderman": {
           "Name": "Peter Parker",
           "Weapons": ["Webbing"],
           "Super Powers": ["Speed", "Reflexes",
                            "Spider-Sense"],
           "Weaknesses": ["Ethyl Chloride Pesticide"]},
  "Thing" : {
           "Name": "Ben Grimm",
           "Weapons": ["Fists"],
           "Powers": ["Immortal", "Super Strength",
                      "Enhanced Lung Capacity", "Good Fighter"],
           "Weakness": [None]},
  "Baby_Groot" : {
           "Name": "Baby Groot",
           "Weapons": ["Strong Branches"],
           "Super Powers": ["Self-Healing", "Controls Plant",
                            "Immune to Fire"],
           "Weaknesses": ["Termites"]},
  "Ironman": {
           "Name": "Tony Stark",
           "Weapons": ["Ironman Suit", "AI", "Blasters"],
           "Superpowers": ["Smart", "Rich"],
           "Weaknesses": ["Arrogant"]},
  "Deadpool": {
           "Name": "Wade Wilson",
           "Weapons": ["Katanas", "Grenades", "Guns"],
           "Super Powers": ["Speed", "Bullet Proof",
                            "Self-Healing"],
           "Weaknesses": ["Women", "Ugly"] },
  "Antman": {
           "Name": "Scott Lang",
           "Weapons": ["Antman Suit"],
           "Super Powers": ["Communication with Insects",
                            "Sound Amplification"],
           "Weaknesses": ["Lacks Ability Control"]}
}

for key in Marvel_Superheros:
    print(key)

for key in Marvel_Superheros:
    print(Marvel_Superheros[key]["Name"])

print("{:<12} {:<12}".format("Hero Title:", "Name:"))
for key in Marvel_Superheros:
    print("{:<12} {:<12}".format(key, Marvel_Superheros[key]["Name"]))
