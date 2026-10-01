from fastapi import FastAPI

from app.routers import game
from app.routers import players

from app.routers.puzzles import router as puzzles_router
from app.routers.rooms import router as rooms_router
from app.routers.players import router as players_router
from app.routers.corridors import router as corridors_router
from app.routers.chests import router as chests_router
from app.routers.doors import router as doors_router
from app.routers.books import router as books_router
from app.routers.libraries import router as libraries_router


app = FastAPI(
    title="Find Pierrot",
    description="API REST de gestion du jeu Find Pierrot",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Find Pierrot"}


@app.get("/health")
def health():
    return {
        "status": "online",
        "game_title": "Find Pierrot",
        "engine_version": "1.0.0"
    }


app.include_router(players.router)
app.include_router(game.router)

app.include_router(puzzles_router)
app.include_router(rooms_router)
app.include_router(players_router)
app.include_router(corridors_router)
app.include_router(chests_router)
app.include_router(doors_router)
app.include_router(books_router)
app.include_router(libraries_router)