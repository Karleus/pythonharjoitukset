def lasku(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

lista = []

while True:
    syote = input("syötä kokonaisluku tai paina Enter laskeaksi lukujesi summa: ")

    if syote == "":
        summa = lasku(lista)
        print(f"Lukujen summa: {summa}")
        break


    luku = int(syote)
    lista.append(luku)