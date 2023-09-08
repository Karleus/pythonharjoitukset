import random as r


def heitto():
    tulo = r.randint(1, 6)
    return tulo


while True:
    tulos = heitto()
    print(tulos)
    if tulos == 6:
        break

