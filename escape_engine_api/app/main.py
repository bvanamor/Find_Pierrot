from fastapi import FastAPI

from app.routers import players
from app.routers import game


app = FastAPI(
    title="Players API",
    description="API REST de gestion des joueurs",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Find Pierrot"}


app.include_router(players.router)
app.include_router(game.router)