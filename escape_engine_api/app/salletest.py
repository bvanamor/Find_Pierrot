try:
    from app.notes import Note
    from app.interface import InterfaceInventaire
    from app.objet import Objet
    from app.Perso import Perso
except ModuleNotFoundError:
    from notes import Note
    from interface import InterfaceInventaire
    from objet import Objet
    from Perso import Perso


note1 = Note("Note mystérieuse", "Ta geule")


class SalleTest:
    def __init__(self, joueur_api=None):
        self.nom = "Salle de test"
        self.personnage = (
            Perso.depuis_joueur_api(joueur_api)
            if joueur_api is not None
            else Perso("Jean-luc", 20)
        )
        self.interface_inventaire = InterfaceInventaire(self.personnage)
        self.objets = [
            Objet("Spray", "salle", True, False, points=0),
            Objet("Livre ancien", "couloir", False, True, points=0),
            Note("Note 1", "24 juin 1961\n Je me demande jusu'où descend ce fichu tunnel, je \n reviendrais plus tard avec une lampe. \n Pierre", points=25),
        ]

    def afficher(self):
        print(f"\nVous entrez dans la {self.nom}.")
        print("Objets visibles :")
        for objet in self.objets:
            print(f"- {objet.get_nom()}")

    def ramasser_objet(self, nom_objet):
        for objet in self.objets:
            if objet.get_nom().lower() == nom_objet.lower():
                self.objets.remove(objet)
                self.personnage.ramasser(objet)

                if isinstance(objet, Note):
                    objet.lire()
                elif objet.get_nom().lower() == "spray":
                    objet.utiliser(self.personnage)

                return True

        print(f"Objet introuvable : {nom_objet}")
        return False

    def lancer(self):
        self.afficher()
        self.ramasser_objet("Spray")

        while True:
            print("\nQue voulez-vous faire ?")
            print("1. Fouiller ses poches")
            print("2. Ramasser un objet")
            print("3. Observer la salle")
            print("4. Quitter la salle")

            choix = input("Votre choix : ").strip()

            if choix == "1":
                self.interface_inventaire.afficher()
            elif choix == "2":
                nom_objet = input("Nom de l'objet : ").strip()
                self.ramasser_objet(nom_objet)
            elif choix == "3":
                self.afficher()
            elif choix == "4":
                print("Vous quittez la salle.")
                break
            else:
                print("Option invalide.")


if __name__ == "__main__":
    SalleTest().lancer()
