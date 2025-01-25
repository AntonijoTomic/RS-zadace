from fastapi import FastAPI, HTTPException, Query
from models import Movie
from typing import Optional
import json
from routes.movies import router as movies_router


app = FastAPI()

movies = []

app.include_router(movies_router)

@app.get("/")
def home():
    return {"poruka": "Dobrodošli na FastAPI poslužitelj"}
