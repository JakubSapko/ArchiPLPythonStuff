'''Lab 8 Architektura PŁ'''

# ---- Zadanie 1 ----

set = {'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
       'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'}

# Wyświetl zawartość

print(set)

# Elementy pojedynczo

for _ in set:
    print(_)

# Ile różnych nazw kolorów = efektywnie pytanie o długość setu

print(len(set))

# Dodać do zbioru inny kolor i print

set.add("musztardowy")
print(set)

# Usunąć kolor i print

set.remove("zielony")
print(set)


# ---- Zadanie 2 ----

A = {'aksamitka', 'bratek', 'cynia', 'kosmos'}