'''Lab 8 Architektura PŁ'''

# ---- Zadanie 3 ----

# Pierwszy set ma zawierac liczby parzyste mniejsze od n (podane z klawiatury)
# Drugi set ma zawierac liczyb mniejsze od n, których modulo 3 daje 2


even = set()
less = set()

i = 0
n = int(input("Podaj liczbę n\n"))
while i < n:
    if i%2 == 0:
        even.add(i)
    if i%3 == 2:
        less.add(i)
    i+=1

print(even)
print(less)
