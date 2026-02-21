# 🧪 ÚKOL: Počet velkých písmen
# Zadání
# Napiš funkci, která:
# vezme text jako parametr
# spočítá, kolik je v textu VELKÝCH písmen
# vrátí číslo
# výsledek uložíš do proměnné pocet
# vypíšeš přesně:
# Počet velkých písmen: <pocet>

text = "Python 3 je super!"

def pocet_velkych_pismen(text):
    pocet = 0
    for pismeno in text:
        if pismeno.isupper():
            pocet += 1
    return pocet
pocet = pocet_velkych_pismen(text)
print(f"Počet velkých písmen: {pocet}")   