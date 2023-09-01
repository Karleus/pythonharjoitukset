import random

lkm = int(input("syötä arvottavien pisteiden määrä: "))

def laskutoimitus(lkm):
    sisalla = 0

    for _ in range(lkm):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            sisalla += 1

    likiarvo = 4 * sisalla / lkm
    return likiarvo

piin_likiarvo = laskutoimitus(lkm)
print(f"Piin likiarvo on {piin_likiarvo}")
