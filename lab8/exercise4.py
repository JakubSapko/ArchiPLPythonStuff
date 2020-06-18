'''Lab 8 Architektura PŁ'''

text = "pliszka, pleszka, sikorka, trznadel, gil, kruk, remiz, sroka, wilga, rudzik, mazurek, bocian, perkoz, zimorodek, kos, drozd"

text_to_set = set(text.split(", "))

print(text_to_set)


word = input("Podaj wyraz")

if word in text_to_set:
    print("Wyraz znajduje sie w zdaniu")
else:
    print("Wyraz nie znajduje sie w zdaniu")