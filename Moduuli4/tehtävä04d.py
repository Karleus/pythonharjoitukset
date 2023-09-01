import random

salaluku = random.randint(1, 10)

while True:
    veikkaus = int(input("Veikkaa luku: "))

    if veikkaus == salaluku:
        print("Veikkaisit oikein!")
        break

    else:
        print("nyt ei mennyt nappiin, koita uudestaan!")
