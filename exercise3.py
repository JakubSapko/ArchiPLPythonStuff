'''Lab 8 Architektura PŁ'''

# ---- Zadanie 3 ----

# Pierwszy set ma zawierac liczby parzyste mniejsze od n (podane z klawiatury)
# Drugi set ma zawierac liczyb mniejsze od n, których modulo 3 daje 2


A = set()
B = set()

i = 0
n = int(input("Podaj liczbę n\n"))
while i < n:
    if i%2 == 0:
        A.add(i)
    if i%3 == 2:
        B.add(i)
    i+=1

print(A)
print(B)

C = A.union(B)
print(C)
print(len(C))
# wtf is A*B

E = A.difference(B)
print(E)
print(len(E))


F = B^A
print(F)
print(len(F))

if B.issubset(A):
    print("B zawiera sie w A")
else:
    print("B nie zawiera sie w A")