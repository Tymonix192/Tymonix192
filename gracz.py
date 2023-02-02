from karta import Karta
import random

miedziak = Karta(1,"miedziak", 0, 0, 1)
dom = Karta(3,"posesja", 0, 0, 0)
class Gracz:
    numerGracza = 0
    punkty = 0
    talia= []
    taliap =[]
    reka = []
    sumamonet = 0
    odrz = []
    kosztmonet = 0

    def __init__(self, numer):
        self.numerGracza = numer
        for i in range(0,7):
            self.talia.append(miedziak)
        for i in range(0,3):
            self.talia.append(dom)

    def zbierz(self):
        for i in range(self.odrz.__len__()):
            self.talia.append(self.odrz[i])
    def potasuj(self):
        for i in range(self.talia.__len__()):
            rand = random.randrange(self.talia.__len__())
            self.taliap.append(self.talia[rand])
        for obj in self.taliap:
            obj.print()
            print("")

    def jakiekarty(self):
        for object in self.talia:
            object.print()
            print("")

    def ilekart(self):
        ile = 0
        for obj in self.talia:
            ile+=1
        print(ile)

    def poka(self):
        for i in range(0,5):
            self.reka.append(self.talia.pop(i))
        print("Reka to")
        for obj in self.reka:
            obj.print()
            print("")
        print("talia: ")
        for vvv in self.talia:
            vvv.print()
            print("")

    def akcja_draw(self):
        if akcja ==1:
            self.reka.append(self.talia.pop(0))

    def sprawdmonety(self):
        self.kosztmonet = 0
        for i in range(self.reka.__len__()):
            self.kosztmonet += self.reka[i].monety
