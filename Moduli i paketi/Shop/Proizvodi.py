class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina
    
    def ispis(self):
        print(f"Naziv proizvoda: {self.naziv}, cijena- {self.cijena} ukupna kolicina {self.kolicina}")


proizvod1 = Proizvod("Iphone 16", 1500, 10)

proizvod2 = Proizvod("Iphone 15", 1100, 1)


proizvodi = [proizvod1, proizvod2]

def dodaj_proizvod(Proizvod):
    proizvodi.append(Proizvod)
    