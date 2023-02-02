

class Karta:
    koszt = 0
    nazwa = ""
    punkty = 0
    akcja = 0
    def __init__(self, koszt, nazwa, punkty, akcja):
        self.koszt = koszt
        self.nazwa = nazwa
        self.punkty = punkty
        self.akcja = akcja
    def print(self):
        wiad = "koszt: {0}, nazwa: {1}, punkty {2}"
        print(wiad.format(self.koszt, self.nazwa, self.punkty))