from fastapi import FastAPI

app = FastAPI(title="EscapeEngine API Test")


@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "Environnement Conda prêt pour l'Escape Game !"
    }