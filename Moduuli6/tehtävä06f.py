import math

def laske_metrihinta(koko, hinta):
    pintaala = math.pi * ((koko / 2) ** 2)
    metrihinta = hinta / pintaala
    return metrihinta

p1koko = float(input("Syötä ensimmäisen pizzan halkkaisija senttimetreinä: "))
p1hinta = float(input("syötä ensimmäisen pizzan hinta: "))

p2koko = float(input("Syötä toisen pizzan halkkaisija senttimetreinä: "))
p2hinta = float(input("syötä toisen pizzan hinta: "))

p1arvo = laske_metrihinta(p1koko, p1hinta)
p2arvo = laske_metrihinta(p2koko, p2hinta)

if p1arvo < p2arvo:
    print("Ensimmäinen pizza on parempi vastine rahoille")

elif p1arvo > p2arvo:
    print("Toinen pizza on parempi vastine rahoille")