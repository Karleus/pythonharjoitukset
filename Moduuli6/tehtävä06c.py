def muunnos():
    tulo = gallons * 3.785
    return tulo


while True:

    gallons = float(input("Syötä gallonamäärä: "))

    if gallons <= 0:
        print("ohjelma lopetettu")
        break

    else:

        testi = muunnos()


        print(f"Määrä litroina: {testi}l")