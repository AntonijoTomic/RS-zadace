from pydantic import BaseModel
from typing import Optional, Literal, TypedDict
from datetime import datetime

# 1. Definirajte Pydantic modele Knjiga i Izdavač koji će validirati podatke i knjigama i izdavačima. Svaka
# knjiga sastoji se od naslova, imena autora, prezimena autora, godine izdavanja, broja stranica i
# izdavača. Izdavač se sastoji od naziva i adrese. Ako godina izdavanja nije navedena, zadana vrijednost
# je trenutna godina.
class Izdavac(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    autora: str
    godina: Optional[int] = datetime.now().year
    brojstranica: int   
    izdavac : Izdavac
    
# 2. Definirajte Pydantic model Admin koji validira podatke o administratoru sustava. Administrator se
# sastoji od imena, prezimena, korisničkog imena, emaila te ovlasti. Ovlasti su lista stringova koje mogu
# sadržavati vrijednosti: dodavanje , brisanje , ažuriranje , čitanje . Ako ovlasti nisu navedene,
# zadana vrijednost je prazna lista. Za ograničavanje ovlasti koristite Literal tip iz modula typing .

class Admin(BaseModel):
    ime: str
    prezime: str
    email: str
    ovlasti: list[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []

# 3. Definirajte Pydantic model RestaurantOrder koji se sastoji od informacija o narudžbi u restoranu.
# Narudžba se sastoji od identifikatora, imena kupca, stol_info, liste jela i ukupne cijene. Definirajte još
# jedan model za jelo koje se sastoji od identifikatora, naziva i cijene. Za stol_info pohranite rječnik koji
# očekuje ključeve broj i lokacija . Primjerice, stol_info može biti {"broj": 5, "lokacija":
# "terasa"}. Za definiciju takvog rječnika koristite TypedDict tip iz modula typing

class Jelo (BaseModel):
    id:int
    naziv:str
    cijena: float

class StolInfo(TypedDict):
    broj: int
    lokacija: str
    
class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    lista_jela: list[Jelo]
    ukupna_cijena: float
    
#  4. Definirajte Pydantic modela CCTV_frame koji će validirati podatke o trenutnoj slici s CCTV kamere.
# Trenutna slika se sastoji od identifikatora, vremena snimanja, te koordiante x i y. Koordinate validirajte
# kao n-torku decimalnih brojeva. Ako koordinate nisu navedene, zadana vrijednost je (0.0, 0.0) .   

class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float, float] = (0.0, 0.0)