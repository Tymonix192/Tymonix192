

class Karta:
    koszt = 0
    nazwa = ""
    punkty = 0
    akcja = 0
    monety = 0
    def __init__(self, koszt, nazwa, punkty, akcja, monety):
        self.koszt = koszt
        self.nazwa = nazwa
        self.punkty = punkty
        self.akcja = akcja
        self.monety = monety
    def print(self):
        wiad = "koszt: {0}, nazwa: {1}, punkty {2}"
        print(wiad.format(self.koszt, self.nazwa, self.punkty), end=" ")
    def nazwaprint(self):
        print(self.nazwa, self.koszt, end="")