luku = int(input("Syötä luku: "))

if luku <= 1:
    print(f"{luku} ei ole alkuluku")
elif luku <= 3:
    print(f"{luku} on alkuluku")
elif luku % 2 == 0 or luku % 3 == 0:
    print(f"{luku} ei ole alkuluku")

else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            print(f"{luku} ei ole alkuluku")
            break
        i += 6

    else:
        print(f"{luku} on alkuluku")