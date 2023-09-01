maxvalue = float(0)
minvalue = float(0)


while True:

    numero = input("Syötä luku: ")
    if numero == "":
        break

    else:
        luku = float(numero)

    if luku >= maxvalue:
        maxvalue = luku

    if luku <= minvalue:
        minvalue = luku


print(f"suurin syöttämäsi arvo oli {maxvalue} ja pienin {minvalue}")
