from pydantic import BaseModel, field_validator, Field
from typing import List, Optional

class Rating(BaseModel):
    Source: str
    Value: str

class Movie(BaseModel):
    Title: str = Field(..., title="Movie Title")
    Year: str = Field(..., title="Release Year")
    Rated: str = Field(..., title="Movie Rating")
    Released: Optional[str] = Field(None, title="Release Date")
    Runtime: str = Field(..., title="Movie Runtime")
    Genre: str = Field(..., title="Movie Genre")
    Director: str = Field(..., title="Director Name")
    Writer: str = Field(..., title="Writer Name")
    Actors: str = Field(..., title="Actors List")
    Plot: Optional[str] = Field(None, title="Movie Plot")
    Language: str = Field(..., title="Language")
    Country: str = Field(..., title="Country of Production")
    Awards: Optional[str] = Field(None, title="Awards Won")
    Poster: Optional[str] = Field(None, title="Poster URL")
    Ratings: List[Rating] = Field(default=[], title="List of Ratings")
    Metascore: Optional[str] = Field(None, title="Metascore Rating")
    imdbRating: Optional[str] = Field(None, title="IMDB Rating")
    imdbVotes: Optional[str] = Field(None, title="IMDB Votes Count")
    imdbID: str = Field(..., title="IMDB Identifier")
    Type: str = Field(..., title="Type of Content")
    Response: str = Field(..., title="API Response Status")
    Images: List[str] = Field(default=[], title="Images", min_length = 1)

    @field_validator('Type')
    def validate_type(cls, v):
        if v not in ['movie', 'series']:
            raise ValueError('Type must be either "movie" or "series".')
        return v
    
    @field_validator('Year')
    def validate_year(cls, v):
      if len(v) >= 4 and v[:4].isdigit():
            year_int = int(v[:4])
            if year_int <= 1900:
                raise ValueError(f"Year must be greater than 1900")
            return year_int
    @field_validator("Runtime")
    def validate_runtime(cls, runtime):
        if runtime == "N/A": 
            return runtime
        if runtime and runtime[0].isdigit():
            if int(runtime[0]) <= 0:
                raise ValueError(f"Runtime must start with a number greater than 0")
        else:
            raise ValueError(f"Runtime must start with a valid number or be 'N/A'")
        return runtime
    
    @field_validator("imdbRating")
    def validate_rating(cls, rating):
        if rating == "N/A": 
            return (rating)
        if float(rating) <= 0:
                raise ValueError(f"Rating must be a number greater than 0")
        return float(rating)
    
    @field_validator("imdbVotes")
    def validate_imdbVotes(cls, imdbVotes):
        if imdbVotes == "N/A": 
            return imdbVotes
        if int(imdbVotes[0]) <= 0:
                raise ValueError(f"Votes must be a number greater than 0")
        return (imdbVotes)
    
    


#dodajte provjere za sljedeće atribute filma unutar Pydantic modela za film:
# Images mora biti lista stringova (javnih poveznica na slike)
# type mora biti odabir između "movie" i "series"
# Obavezni atributi su: Title , Year , Rated , Runtime , Genre , Language , Country , Actors ,
# Plot , Writer
# Ostali atributi su neobavezni, a ako nisu navedeni, postavite im zadanu vrijednost
# Dodajte validacije za Year i Runtime atribut (godina mora biti veća od 1900, a trajanje filma mora
# biti veće od 0)
# Dodajte validacije za imdbRating i imdbVotes (ocjena mora biti između 0 i 10, a broj glasova
# mora biti veći od 0)


# 5. Definirajte Pydantic model Actor koji će sadržavati atribute name i surname .
# 6. Definirajte Pydantic model Writer koji će sadržavati atribute name i surname .

class Actor(BaseModel):
    name: str
    surname: str
    
class Writer(BaseModel):
    name: str
    surname: str