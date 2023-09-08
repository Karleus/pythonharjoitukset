def karsi(lista):
    parilliset = [luku for luku in lista if luku % 2 == 0]
    return parilliset



lista = []

while True:
    syote = input("syötä kokonaisluku tai paina Enter erottaaksesi parilliset: ")

    if syote == "":
        parilliset = karsi(lista)
        print(f"Koko lista: {lista}\nParilliset: {parilliset}")
        break


    luku = int(syote)
    lista.append(luku)