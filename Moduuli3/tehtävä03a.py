kalapituus = int(input("Syötä kalan pituus: "))

if kalapituus < 37:
    pienuus = 37 - kalapituus
    print(f"Laske kala takaisin, se on {pienuus}cm liian lyhyt.")

