vstup = "Python je fajn"

def velka_pismena(text):
    vysledek = ""
    for znak in text:
        if znak.islower():
            vysledek += znak.upper()
        else:
            vysledek += znak
    return vysledek
vysledek = velka_pismena(vstup)

print(f"Upraveny text: {vysledek}")
