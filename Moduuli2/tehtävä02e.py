leiviska = float(input("Anna massa leivisköinä: "))
naula = float(input("Anna massa nauloina: "))
luoti = float(input("Anna massa luoteina: "))

leiviskakg = leiviska*8512
naulakg = naula*425.6
luotikg = luoti*13.3

kilot = (leiviskakg + naulakg + luotikg)/1000
print (f"Paino kilogrammoina: {kilot}")


#hae kg math.floor, modulo eli %