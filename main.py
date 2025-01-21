# Definirajte rutu i odgovarajući Pydantic model za dohvaćanje podataka o automobilima. Svaki
# automobil ima sljedeće atribute: id , marka , model , godina_proizvodnje , cijena i boja . Ako
# korisnik pokuša dohvatiti automobil s ID-em koji ne postoji, podignite iznimku HTTPException s
# statusom 404 i porukom Automobil nije pronađen .

from fastapi import FastAPI, HTTPException,  Query
from models import Automobil, CarCreate, CarResponse
from typing import Optional

app = FastAPI()

auti = [
    Automobil(id=1, marka="Rimac", model="Nevera", godina_proizvodnje=2024, cijena=1000000.00, boja="Tirkizna"),
    Automobil(id=2, marka="Audi", model="a4", godina_proizvodnje=2010, cijena=7000.00, boja="Crna"),
    Automobil(id=3, marka="Renault", model="Clio", godina_proizvodnje=2007, cijena=1000.00, boja="Sivi"),
]


@app.get("/auti/{id}", response_model=Automobil)
def get_auto(id: int):
    pronadeni_auto = next((auto for auto in auti if auto.id == id), None)
    if pronadeni_auto is None:
        raise HTTPException(status_code=404, detail="Automobil nije pronađen")
    return pronadeni_auto

# 2. Nadogradite prethodnu rutu s query parametrima min_cijena , max_cijena , min_godina i
# max_godina . Implementirajte validaciju query parametra za cijenu i godinu proizvodnje. Minimalna
# cijena mora biti veća od 0, a minimalna godina proizvodnje mora biti veća od 1960. Unutar funkcije
# obradite iznimku kada korisnik unese minimalnu cijenu veću od maksimalne cijene ili minimalnu
# godinu proizvodnje veću od maksimalne godine proizvodnje te vratite odgovarajući HTTPException .

@app.get("/autiquery")
def get_automobili_by_query(
    min_cijena: Optional[float] = Query(None, gt=0), 
    max_cijena: Optional[float] = Query(None), 
    min_godina: Optional[int] = Query(None, gt=1960), 
    max_godina: Optional[int] = Query(None)
):

    if min_cijena is not None and max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena ne može biti veća od maksimalne cijene")
    if min_godina is not None and max_godina is not None and min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina proizvodnje ne može biti veća od maksimalne godine")

    filtrirani_auti = [
        auto for auto in auti
        if (min_cijena is None or auto.cijena >= min_cijena) and (max_cijena is None or auto.cijena <= max_cijena) and (min_godina is None or auto.godina_proizvodnje >= min_godina)
        and (max_godina is None or auto.godina_proizvodnje <= max_godina)
    ]
    
    return filtrirani_auti


# Definirajte rutu za dodavanje novog automobila u bazu podataka. id se mora dodati na poslužitelju,
# kao i atribut cijena_pdv (definirajte dodatni Pydantic model za to). Ako korisnik pokuša dodati
# automobil koji već postoji u bazi podataka, podignite odgovarajuću iznimku. Implementirajte ukupno 3
# Pydantic modela, uključujući BaseCar model koji će nasljeđivati preostala 2 modela.

@app.post("/auti", response_model=CarResponse)
def add_auto(auto: CarCreate):

    for provjeraAuto in auti:
        if (  provjeraAuto.marka.lower() == auto.marka.lower()
            and provjeraAuto.model.lower() == auto.model.lower()
              and provjeraAuto.boja.lower() == auto.boja.lower()
            and provjeraAuto.godina_proizvodnje == auto.godina_proizvodnje):
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi podataka.")

    new_id = len(auti) + 1

    
    auto_s_id = CarResponse(
            id=new_id,
            marka=auto.marka,
            model=auto.model,
            godina_proizvodnje=auto.godina_proizvodnje,
            cijena=auto.cijena,
            boja=auto.boja,
            cijena_pdv=auto.cijena * 1.25 
    )
   
    auti.append(auto_s_id)
    print(auti)
    return auto_s_id