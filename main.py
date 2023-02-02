from gracz import Gracz
from karta import Karta
import random

miedziak = Karta(1,"miedziak", 0, 0, 1)
dom = Karta(3,"posesja", 0, 0, 0)

kartysklep = [[miedziak, miedziak, miedziak, dom], [miedziak, miedziak, miedziak, dom],
              [miedziak, miedziak, miedziak, dom], [miedziak, miedziak, miedziak, dom]]
def sklep(gracz):
    for k in range(0, gracz.reka.__len__()):
        gracz.kosztmonet += gracz.reka[k].monety

    gracz.sumamonet+=gracz.kosztmonet
    wiad = "masz {0} monet"
    print(wiad.format(gracz.sumamonet))

    for i in range(0,4):
        for j in range(0,4):
            kartysklep[i][j].nazwaprint()
            print(" | ", end="")
        print("")
        print("--------------------------------------------------")

def buy(gracz, numer1, numer2):
    if kartysklep[numer1-1][numer2-1].koszt <=gracz.sumamonet:
        for i in range(0, kartysklep[numer1-1][numer2-1].koszt):
            if gracz.reka[i] == miedziak:
                gracz.odrz.append(gracz.reka.pop(i))
    print("masz teraz %s monet"%gracz.sprawdmonety() )
    gracz.odrz.append(kartysklep[numer1-1][numer2-1])



gracz1 = Gracz(1)
gracz1.potasuj()
gracz1.poka()
sklep(gracz1)
a = int(input("rząd karty: ") )
b = int(input("druga liczba: "))
buy(gracz1, a, b)
for xcv in gracz1.odrz:
    xcv.print()