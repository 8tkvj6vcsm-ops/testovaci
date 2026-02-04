jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Michaela", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"]
]
for jmeno in jmena: 
    for osoba in jmeno:
        if osoba.startswith("M") or osoba.startswith("H"):
            print(f"{osoba.upper()}")