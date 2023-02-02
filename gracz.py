from karta import Karta
import random

miedziak = Karta(1,"miedziak", 0, 0)
dom = Karta(3,"posesja", 0, 0)
class Gracz:
    numerGracza = 0
    punkty = 0
    talia= []
    taliap =[]
    reka = []

    def __init__(self, numer):
        self.numerGracza = numer
        for i in range(0,7):
            self.talia.append(miedziak)
        for i in range(0,3):
            self.talia.append(dom)
        for i in range(0,3):
            rand = random.randrange(self.talia.__len__()-i)
            self.reka.append(self.talia[rand])
            for j in range(0, self.talia.__len__()):
                self.taliap.append(self.talia[i])
            self.talia.clear()
            for k in range(0,self.taliap.__len__()-1):
                if k!=rand:
                    self.talia.append(self.taliap[k])
    def jakiekarty(self):
        for object in self.talia:
            object.print()
    def ilekart(self):
        ile = 0
        for obj in self.talia:
            ile+=1
        print(ile)
    def poka(self):
        print("twoja ręka to: ")
        for obj in self.reka:
            obj.print()