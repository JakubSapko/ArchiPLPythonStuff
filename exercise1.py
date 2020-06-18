'''Lab 8 Architektura PŁ'''

# ---- Zadanie 1 ----

set1 = {'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
       'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'}

# Wyświetl zawartość

print(set1)

# Elementy pojedynczo

for _ in set1:
    print(_)

# Ile różnych nazw kolorów = efektywnie pytanie o długość setu

print(len(set1))

# Dodać do zbioru inny kolor i print

set1.add("musztardowy")
print(set1)

# Usunąć kolor i print

set1.remove("zielony")
print(set1)

