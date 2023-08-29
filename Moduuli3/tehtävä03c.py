sukupuoli = str(input("Anna sukupuolesi m/n: "))



if sukupuoli=="m" :

    hba = float(input("syötä hemoglobaani arvosi: "))

    if  hba < 134:
        print(" Hemoglobaanisi on alhainen")

    elif hba > 195:
        print("Hemogloobanisi on korkea")

    else: print("Hemoglobaanisi on normaali")


if sukupuoli=="n" :

    hba = float(input("syötä hemoglobaani arvosi: "))

    if  hba < 117:
        print(" Hemoglobaanisi on alhainen")

    elif hba > 175:
        print("Hemogloobanisi on korkea")

    else: print("Hemoglobaanisi on normaali")

