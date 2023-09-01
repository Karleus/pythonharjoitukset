yrit = 0

while True:

    if yrit >= 5:
        print("Pääsy evätty")
        break

    käyttäjätunnus = input("käyttäjätunnus: ")
    salasana = input("salasana: ")

    if käyttäjätunnus == "python" and salasana == "rules":
        print("Tervetuloa!")

    else:
        yrit += 1

        

