import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()

while len(hrac_volby) < 3 or len(pocitac_volby) < 3:
  if len(hrac_volby) < 3:
    hrac_volby.append(random.choice(moznosti))
  if len(pocitac_volby) < 3:
    pocitac_volby.append(random.choice(moznosti))

for i in range(3):
  if hrac_volby[i] == pocitac_volby[i]:
      vysledek = "Remíza!"
  else: 
      vysledek = "Vyhrává hráč!"
  
  print(f"Výsledek: {vysledek}")
#Zkousim jen neco dopsat aby byla zmena sw