# 🧪 ÚKOL: Počet písmen
# Zadání
# Napiš funkci, která:
# vezme text jako parametr
# spočítá, kolik je v textu PÍSMEN
# (❗ nepočítej mezery, čísla ani interpunkci)
# vrátí číslo
# výsledek uložíš do proměnné pocet
# vypíšeš přesně:
# Počet písmen: <pocet>

text = "Python 3 je super!"

def pocet_pismen(text):
    pocet = 0
    for pismeno in text:
        if pismeno.isalpha():
            pocet += 1
    return pocet

pocet = pocet_pismen(text)

print(f"Počet písmen: {pocet}")