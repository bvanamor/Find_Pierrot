class InterfaceInventaire:
    def __init__(self, personnage):
        self.personnage = personnage

    def afficher(self):
        inventaire = self.personnage.inventaire
        life = self.personnage.life

        print("\n=============================")
        print(f"Poches de {self.personnage.get_nom()}")
        print("=============================")

        if inventaire.est_vide():
            print("Aucun objet stocke.")
            return

        for numero, objet in enumerate(inventaire.objets, start=1):
            print(f"{numero}. {objet.get_nom()}")


def afficher_inventaire(personnage):
    InterfaceInventaire(personnage).afficher()

