import os
from random import choice, seed

hadana_slova = ['dva', 'hudba', 'vecernicek']

def tajne_slovo():
    slovo = choice(hadana_slova)
    return slovo

#test = tajne_slovo()
#print(test)

def vytvor_tajenku(slovo):
    tajenka = ['_'] * len(slovo)
    return tajenka

test = vytvor_tajenku(tajne_slovo())
#print(test) 

tajenka_list = vytvor_tajenku(tajne_slovo())

def zobraz_stav_hry(tajenka):
    joined_tajenka = ' '.join(tajenka)
    print(joined_tajenka)

test = zobraz_stav_hry(tajenka_list)
print(test)
