class Objet:
    def __init__(self, nom, position, health_effect, enigme_effect, points=0):
        self.nom = str(nom)
        self.position = position
        self.health_effect = bool(health_effect)
        self.enigme_effect = bool(enigme_effect)
        self.points = int(points)

    def get_nom(self):
        return self.nom

    def get_points(self):
        return self.points

    def set_nom(self, nom):
        self.nom = nom

    def utiliser(self, personnage):
        if self.health_effect:
            personnage.life = True
            print(f"{personnage.get_nom()} utilise {self.nom} : état de santé restauré.")
            return True

        if self.enigme_effect:
            print(f"{self.nom} aide à résoudre une énigme.")
            return True

        print(f"{self.nom} n'a aucun effet immédiat.")
        return False

    def __str__(self):
        return f"Nom: {self.nom}, Position: {self.position}, Effet de santé: {self.health_effect}, Effet d'énigme: {self.enigme_effect}"
