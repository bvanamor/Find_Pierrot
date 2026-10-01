class Note:
    def __init__(self, nom, contenu, points=10):
        self.nom = nom
        self.contenu = contenu
        self.points = int(points)

    def get_nom(self):
        return self.nom

    def get_points(self):
        return self.points

    def lire(self):
        print(f"\n[Note] {self.nom}")
        print(self.contenu)

    def __str__(self):
        return self.nom
