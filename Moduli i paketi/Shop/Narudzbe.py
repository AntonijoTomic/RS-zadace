from Main import *

class Narudzba:
    def __init__(self, proizvodi):
        self.proizvodi = proizvodi
        self.ukupna_cijena = sum([proizvod['cijena'] * proizvod['kolicina'] for proizvod in proizvodi])

    def ispis(self):
        print("Proizvodi u narudžbi:")
        for proizvod in self.proizvodi:
            print(f"{proizvod['naziv']} - {proizvod['cijena']} HRK - {proizvod['kolicina']} komada")
        print(f"Ukupna cijena: {self.ukupna_cijena} HRK")


def napravi_narudzbu(proizvodi):
    if type(proizvodi) is list:
        if(len(proizvodi) > 0):
            for proizvod in proizvodi:
                if (proizvod['kolicina'] < 1):
                    print(f"Proizvod {proizvod['naziv']} nije dostupan!")
                    return None
                elif (not isinstance(proizvod, dict)):
                 return None
                elif (proizvod['cijena'] <= 0):
                 print(f"Proizvod {proizvod['naziv']} ima neispravnu cijenu")
                 return None
                else:
                 return Narudzba(proizvodi)
        else:
              print("Lista ne smije biti prazna")
        return None      
    else:
        print("Argument mora biti lista.")
        return None
    
    

# Kreiranje narudžbe
