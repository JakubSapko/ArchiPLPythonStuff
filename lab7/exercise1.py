'''Lab 7 Architektura PŁ'''
import math

perimeter = 0

def length(x1, x2, y1, y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

x1 = float(input("Podaj wartosc dla x1\n"))
x2 = float(input("Podaj wartosc dla x2\n"))
x3 = float(input("Podaj wartosc dla x3\n"))
y1 = float(input("Podaj wartosc dla y1\n"))
y2 = float(input("Podaj wartosc dla y2\n"))
y3 = float(input("Podaj wartosc dla y3\n"))


perimeter = length(x1, x2, y1, y2) + length(x2, x3, y2, y3) + length(x1, x3, y1, y3)

print(perimeter)