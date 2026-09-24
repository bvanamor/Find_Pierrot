import json
from urllib import request, error

from pydantic import BaseModel, ConfigDict, Field

try:
    from app.inventory import Inventaire
except ModuleNotFoundError:
    from inventory import Inventaire


API_BASE_URL = "http://127.0.0.1:8000"


class Perso(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
    )

    nom: str = Field(min_length=3, max_length=30)
    age: int = 0
    life: bool = True
    score: int = 0
    player_id: int | None = None
    inventaire: Inventaire = Field(default_factory=Inventaire, exclude=True)

    def __init__(self, nom, age=0, life=True, score=0, player_id=None):
        super().__init__(
            nom=nom,
            age=age,
            life=life,
            score=score,
            player_id=player_id,
        )

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def synchroniser_score_api(self):
        if self.player_id is None:
            return False

        payload = {
            "name": self.nom,
            "score": self.score,
            "life": self.life,
        }

        url = f"{API_BASE_URL}/players/{self.player_id}/score"
        try:
            req = request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="PUT",
            )
            with request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                print(f"Score en temps réel sur l'API : {data['score']}")
                return data
        except (error.URLError, ValueError, KeyError):
            return False

    def ramasser(self, objet):
        self.inventaire.ajouter(objet)

        self.score += objet.get_points()
        result = self.synchroniser_score_api()

        print(f"{self.nom} ramasse : {objet.get_nom()}")
        if result:
            print(f"Score actuel : {result['score']}")
        else:
            print(f"Score actuel : {self.score}")

    @classmethod
    def depuis_joueur_api(cls, joueur):
        return cls(
            joueur["name"],
            life=joueur.get("life", True),
            score=joueur.get("score", 0),
            player_id=joueur.get("id"),
        )

    def afficher_inventaire(self):
        self.inventaire.afficher()

    def __str__(self):
        return f"Nom: {self.nom}, Age: {self.age}"