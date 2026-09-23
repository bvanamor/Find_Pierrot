class Note:
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.lue = False

    def lire(self):
        self.lue = True
        return self.contenu