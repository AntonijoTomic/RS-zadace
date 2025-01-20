# 1. Definirajte novu FastAPI rutu GET /filmovi koja će klijentu vraćati listu filmova definiranu u sljedećoj
# listi:
from fastapi import FastAPI
app = FastAPI()


filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi")
def get_filmovi(): 
    return filmovi


# 2. Nadogradite prethodnu rutu na način da će output biti validiran Pydantic modelom Film kojeg
# definirate u zasebnoj datoteci models.py .
from models import Film 

@app.get("/filmovi_validirani", response_model=list[Film])  
def get_filmovi():
    return filmovi


# 3. Definirajte novu FastAPI rutu GET /filmovi/{id} koja će omogućiti pretraživanje novog filma prema
# id -u definiranom u parametru rute id . Dodajte i ovdje validaciju Pydantic modelom Film .

@app.get("/filmovi/{id}", response_model=Film)
def get_film(id :int):
    pronadeni_film = next((film for film in filmovi if film["id"] == id), None)
    return pronadeni_film

# Definirajte novu rutu POST /filmovi koja će omogućiti dodavanje novog filma u listu filmova.
# Napravite novi Pydantic model CreateFilm koji će sadržavati atribute naziv , genre i godina , a kao
# output vraćajte validirani Pydantic model Film koji predstavlja novododani film s automatski
# dodijeljenim id -em.
from models import CreateFilm 

@app.post("/dodaj_film", response_model=Film)
def add_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    film_s_id : Film = {"id" : new_id, **film.model_dump()}
    filmovi.append(film_s_id) 
    return film_s_id


# Dodajte query parametre u rutu GET /filmovi koji će omogućiti filtriranje filmova prema genre i
# min_godina . Zadane vrijednosti za query parametre neka budu None i 2000 .

@app.get("/filmoviquery") # u FastAPI-ju ne navodimo query parametre u URL putanji
def get_filmovi_by_query(genre: str = None, min_godina: int = 2000): 
    pronadenifilmovi = [film for film in filmovi if (genre is None or
    film["genre"] == genre) and (min_godina is None or film["godina"] <= min_godina)]
    return pronadenifilmovi