from app.enigme import Enigme


class Salle:
    def __init__(self, nom, description=""):
        self.nom = nom
        self.description = description
        self.enigmes = []
        self.objets = []
        self.notes = []
        self.terminee = False

    def ajouter_objet(self, objet):
        self.objets.append(objet)

    def ajouter_note(self, note):
        self.notes.append(note)

    def ajouter_enigme(self, enigme: Enigme):
        self.enigmes.append(enigme)

    def verifier_salle(self):
        self.terminee = all(
            enigme.resolue
            for enigme in self.enigmes
        )

        return self.terminee