# 🔥 Úkol: Mini analyzátor hesel

# Napiš program, který:
# 	1.	Vezme vstup od uživatele (input)
# 	2.	Zkontroluje:
# 	•	délku hesla (minimálně 8 znaků)
# 	•	obsahuje alespoň:
# 	•	1 velké písmeno
# 	•	1 malé písmeno
# 	•	1 číslo
# 	3.	Spočítá:
# 	•	počet unikátních znaků (pomocí set)

def check_password(password):
    hodnoceni = {"velke_pismeno" : 0, "male_pismeno": 0, "cislo": 0}
    # logika kontroly
    for p in password:
        if p.isupper():
            hodnoceni["velke_pismeno"] += 1
        elif p.islower():
            hodnoceni["male_pismeno"] += 1
        elif p.isdigit():
            hodnoceni["cislo"] += 1    
    
    result = (  len(password) > 8 and
                hodnoceni["velke_pismeno"] >= 1 and
                hodnoceni["male_pismeno"] >= 1 and
                hodnoceni["cislo"] >= 1)
        
    return  result

def main():
    password = input("Zadej heslo: ")
    result = check_password(password)
    print(result)

main()

# mrkni na jine reseni, efektivnejsi, vic pro
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_digit = False

#     for p in password:
#         if p.isupper():
#             has_upper = True
#         elif p.islower():
#             has_lower = True
#         elif p.isdigit():
#             has_digit = True

#         if has_upper and has_lower and has_digit:
#             break

#     return len(password) > 8 and has_upper and has_lower and has_digit