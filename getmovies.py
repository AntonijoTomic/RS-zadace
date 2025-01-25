from fastapi import FastAPI, HTTPException, Query
from models import Movie
from typing import Optional
import json


def load_movies(file_path='movies.json'):
    movies = []  # Koristi globalnu varijablu
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        for m in data:
            movie = Movie(**m)
            movies.append(movie)
    
    return movies
