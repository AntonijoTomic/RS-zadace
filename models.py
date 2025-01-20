from pydantic import BaseModel

class Film(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int   
    
class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int
    
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},