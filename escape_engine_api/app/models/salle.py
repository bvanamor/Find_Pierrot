from app.models.enigme import Enigme


class Salle:
    def __init__(self, nom):
        self.nom = nom
        self.enigmes = []
        self.terminee = False

    def ajouter_enigme(self, enigme: Enigme):
        self.enigmes.append(enigme)

    def verifier_salle(self):
        self.terminee = all(
            enigme.resolue
            for enigme in self.enigmes
        )

        return self.terminee