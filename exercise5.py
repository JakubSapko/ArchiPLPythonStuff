'''Lab 8 Architektura PŁ'''

text = "pliszka, pleszka, sikorka, trznadel, gil, kruk, remiz, sroka, wilga, rudzik, mazurek, bocian, perkoz, zimorodek, kos, drozd"

text_to_set = set(text.split(", "))

run = True

while run:
    com = input("Co chcesz zrobic?\n")
    if com == "wyswietl":
        print(text_to_set)
    elif com == "dodaj":
        content = input("Podaj wyraz ktory chcesz dodac\n")
        text_to_set.add(content)
    elif com == "usun":
        er_content = input("Podaj wyraz ktory chcesz usunac\n")
        text_to_set.discard(er_content)
    elif com == "wyjdz":
        print("Dziekuje za korzystanie z programu\n")
        run = False
    else:
        print("Niepoprawna komenda! Wprowadz jedna z czterech opcji: wyswietl/dodaj/usun/wyjdz\n")