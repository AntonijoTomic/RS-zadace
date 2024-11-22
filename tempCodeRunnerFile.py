class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime} i imam {self.godine} godina."
    
osoba2 = Osoba("Marko", "Marković", 30)
print(osoba2.ime) # Marko
print(osoba2.prezime) # Marković
print(osoba2.godine) 
print(osoba2.pozdrav());


class korisnik(Osoba):
    def __init__(self, ime, prezime, godine, privilegije):
        super().__init__(ime, prezime, godine)
        self.privilegije = privilegije
        
    def pozdrav(self):
          return f"Pozdrav, ja sam {self.ime} {self.prezime}, imam {self.godine} godina i imam sljedećću privilegiju {self.privilegije}"    
        

admin = korisnik("Anto","Antic",30,"Car")

print(admin.pozdrav())

