import random as r


def heitto():
    tulo = r.randint(1, tahkot)
    return tulo

tahkot = int(input("Syötä nopan tahkojen määrä: "))

while True:
    tulos = heitto()
    print(tulos)
    if tulos == tahkot:
        break

