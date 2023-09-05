luvut = []

luku = input("Syötä luku: ")
while luku != "":
    luvut.append(luku)
    luku = input("Anna seuraava luku tai lopeta painamalla enter: ")

    luvut.sort(reverse=True)

print(luvut)