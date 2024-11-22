from Proizvodi import *
from Narudzbe import *
proizvodii = [
 {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
 {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
 {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
 {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for p in proizvodii:
    proizvod = Proizvod(p["naziv"], p["cijena"], p["kolicina"])
    dodaj_proizvod(proizvod)
    
    
for p in proizvodi:
    p.ispis()
    
narudzba = napravi_narudzbu(proizvodii)

narudzba.ispis()