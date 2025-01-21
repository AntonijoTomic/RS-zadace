# automobil ima sljedeće atribute: id , marka , model , godina_proizvodnje , cijena i boja . Ako
from pydantic import BaseModel

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str
    
    
class baseCar (BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str   
    
    
class CarCreate(baseCar):
    pass    

class CarResponse(baseCar):
    id: int
    cijena_pdv: float 