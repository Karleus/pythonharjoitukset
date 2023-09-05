import random

lkm = int(input("syötä noppien määrä: "))

for _ in range(lkm):
    noppa = random.randint(1, 6)
    print(noppa)