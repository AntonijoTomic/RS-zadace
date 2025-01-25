from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Literal
from getmovies import load_movies 
from models import Movie
router = APIRouter()

movies = load_movies()  

def parse_year(year: Optional[str]) -> Optional[int]:
    print("Parsing year:", year)
    if not year:
        return None
    
    # Ako je godina broj, pretvaramo je u string
    if isinstance(year, int):
        year = str(year)
    
    if "–" in year:  # Provjeravamo je li godina raspon
        return int(year.split("–")[0])  # Vraćamo prvu godinu iz raspona
    return int(year)  # Ako nije raspon, vraćamo jednostavnu godinu


@router.get("/movies", response_model=List[Movie])
def get_all_movies(
    min_year: Optional[int] = Query(None, ge=1900, description="Minimum release year of the movie"),
    max_year: Optional[int] = Query(None, ge=1900, description="Maximum release year of the movie"),
    min_rating: Optional[float] = Query(None, ge=0.0, le=10.0, description="Minimum IMDb rating of the movie"),
    max_rating: Optional[float] = Query(None, ge=0.0, le=10.0, description="Maximum IMDb rating of the movie"),
    type: Optional[Literal["movie", "series"]] = Query(None, description="Type of content: 'movie' or 'series'")
):
    filtered_movies = movies
    print(filtered_movies)    
    if min_year is not None:  
        filtered_movies = [
            movie for movie in filtered_movies 
            if parse_year(movie.Year) is not None and parse_year(movie.Year) >= min_year
        ]
    print(filtered_movies)    
    if max_year is not None:  
        filtered_movies = [
            movie for movie in filtered_movies 
            if parse_year(movie.Year) is not None and parse_year(movie.Year) <= max_year
        ]
    
    if min_rating is not None: 
        filtered_movies = [
            movie for movie in filtered_movies 
            if movie.imdbRating != "N/A" and float(movie.imdbRating) >= min_rating
        ]
    if max_rating is not None:  
        filtered_movies = [
            movie for movie in filtered_movies 
            if movie.imdbRating != "N/A" and float(movie.imdbRating) <= max_rating
        ]


   
    if type is not None: 
        filtered_movies = [movie for movie in filtered_movies if movie.Type == type]
    
    if not filtered_movies:
        raise HTTPException(status_code=404, detail="No movies found with the given criteria")
    
    return filtered_movies


@router.get("/movies/{imdb_id}", response_model=Movie)
def get_movie_by_imdb_id(imdb_id: str):
    """Retrieve a movie by its IMDb ID."""
    for movie in movies:
        if movie.imdbID == imdb_id:
            return movie
    raise HTTPException(status_code=404, detail=f"Movie with IMDb ID {imdb_id} not found.")

@router.get("/movies/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    """Retrieve a movie by its title."""
    for movie in movies:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail=f"Movie with title '{title}' not found.")