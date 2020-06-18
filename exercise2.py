'''Lab 8 Architektura PŁ'''

# ---- Zadanie 2 ----

A = {'aksamitka', 'bratek', 'cynia', 'kosmos', 'aster', 'sasanka', 'zawilec', 'konwalia', 'rumianek', 'tulipan', 'hiacynt', 'narcyz'}
B = {'bratek', 'pierwiosnek', 'przylaszczka', 'cebulica', 'zawilec', 'krokus', 'sasanka'}
print(A)
print(B)


# Set C zawiera elementy A lub B
C = A.union(B)
#print(C)
print(len(C))

# Set D zawiera elementy przecięcia A i B

D = A.intersection(B)
#print(D)
print(len(D))

# Set E zawiera elementy, które należą do A, ale nie do B

E = A.difference(B)
#print(E)
print(len(E))

# Set F zawiera elementy, które należą do B, ale nie do A

F = B.difference(A)
#print(F)
print(len(F))
