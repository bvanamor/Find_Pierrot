from app.enigme import Enigme
from app.notes import Note
from app.objet import Objet
from app.Perso import Perso
from app.salle import Salle


class Game:
    def __init__(self, joueur=None):
        self.joueur = joueur or Perso("Explorateur")
        self.salles = self._creer_salles()
        self.notes = []
        self.enigmes = []
        self.salle_actuelle = 0
        self.etape = 1

        for salle in self.salles:
            self.notes.extend(salle.notes)
            self.enigmes.extend(salle.enigmes)

    def _creer_salles(self):
        entree = Salle(
            "Salle 1",
            "Une petite piece poussiereuse avec une trace de pas pres du tunnel.",
        )
        entree.ajouter_objet(Objet("Spray", "salle", True, False, points=0))
        entree.ajouter_note(Note(
            "Note 1",
            "24 juin 1961\nJe me demande jusqu'ou descend ce fichu tunnel.\nPierre",
            points=25,
        ))
        entree.ajouter_enigme(Enigme(
            "Combien font 2 + 3 ?",
            "5",
            "La porte du tunnel s'ouvre.",
        ))

        tunnel = Salle(
            "le tunnel",
            "Un grand tunnel qui semble s'étendre sous la maison.",
        )
        tunnel.ajouter_objet(Objet("Livre ancien", "tunnel", False, True, points=10))
        tunnel.ajouter_note(Note(
            "Indice du tunnel",
            "Le mot de passe est le nom de celui que tu es venu retrouver.",
        ))
        tunnel.ajouter_enigme(Enigme(
            "Quel est le prenom de ton ami disparu ?",
            "Pierrot",
            "Une trappe se deverrouille.",
        ))

        coffre = Salle(
            "la chambre secrete",
            "Une chambre cachee. Un coffre porte une derniere inscription.",
        )
        coffre.ajouter_note(Note(
            "Dernier indice",
            "Additionne les points des objets trouves : 0 + 10.",
        ))
        coffre.ajouter_enigme(Enigme(
            "Combien font 0 + 10 ?",
            "10",
            "Le coffre s'ouvre : Pierrot est retrouve !",
        ))
        return [entree, tunnel, coffre]

    def ajouter_salle(self, salle: Salle):
        self.salles.append(salle)

    def ajouter_note(self, note: Note):
        self.notes.append(note)

    def ajouter_enigme(self, enigme: Enigme):
        self.enigmes.append(enigme)

    @property
    def salle(self):
        return self.salles[self.salle_actuelle]

    def afficher_salle(self):
        print(f"\nVous entrez dans {self.salle.nom}.")
        print(self.salle.description)
        print("Objets visibles :")
        if self.salle.objets:
            for objet in self.salle.objets:
                print(f"- {objet.get_nom()}")
        else:
            print("Aucun objet visible.")

    def ramasser_objet(self, nom_objet):
        for objet in self.salle.objets:
            if objet.get_nom().lower() == nom_objet.lower():
                self.salle.objets.remove(objet)
                self.joueur.ramasser(objet)
                return True

        print(f"Objet introuvable : {nom_objet}")
        return False


    def afficher_notes(self):
        print("\n===== NOTES ET INDICES =====")

        if not self.notes:
            print("Aucune note trouvée.")
            return

        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note.get_nom()}")


    def lire_note(self, numero):
        if numero < 1 or numero > len(self.notes):
            print("Cette note n'existe pas.")
            return

        note = self.notes[numero - 1]

        print("\n===== NOTE =====")
        print(f"Titre : {note.get_nom()}")
        print()
        note.lire()


    def repondre(self, reponse_joueur):

        if self.etape > len(self.enigmes):
            print("\nToutes les énigmes sont terminées !")
            return

        enigme = self.salle.enigmes[0]

        recompense = enigme.verifier(reponse_joueur)

        if recompense:
            print("\n======================")
            print("    BONNE RÉPONSE !")
            print("======================")

            print(f"Récompense : {recompense}")

            self.etape += 1
            self.salle.verifier_salle()

            if self.salle_actuelle < len(self.salles) - 1:
                self.salle_actuelle += 1
                print(f"Vous avancez vers {self.salle.nom}.")
            else:
                print("\nFélicitations, tu as retrouvé Pierrot!")

            print(f"Nouvelle étape : {self.etape}")

        else:
            print("\nMauvaise réponse.")
            print("Réessaye.")


    def start(self):
        self.afficher_salle()
        self.afficher_menu()

    def afficher_menu(self):

        while True:

            print("\n")
            print("==============================")
            print("        Find Pierrot")
            print("==============================")
            print(f"Étape actuelle : {self.etape}")
            print()
            print("1. Observer la salle")
            print("2. Ramasser un objet")
            print("3. Fouiller ses poches")
            print("4. Voir les notes")
            print("5. Lire une note")
            print("6. Répondre à l'énigme")
            print("7. Quitter")
            print("==============================")

            choix = input("Votre choix : ")


            if choix == "1":
                self.afficher_salle()

            elif choix == "2":
                nom_objet = input("Nom de l'objet : ").strip()
                self.ramasser_objet(nom_objet)

            elif choix == "3":
                self.joueur.afficher_inventaire()

            elif choix == "4":
                self.afficher_notes()

            elif choix == "5":

                self.afficher_notes()

                if self.notes:
                    try:
                        numero = int(
                            input("\nNuméro de la note : ")
                        )

                        self.lire_note(numero)

                    except ValueError:
                        print(
                            "Veuillez entrer un numéro valide."
                        )


            elif choix == "6":

                if self.etape > len(self.enigmes):

                    print(
                        "\nToutes les énigmes sont terminées !"
                    )

                else:

                    enigme = self.enigmes[self.etape - 1]

                    print("\n===== ÉNIGME =====")
                    print(enigme.question)

                    reponse = input(
                        "\nVotre réponse : "
                    )

                    self.repondre(reponse)


            elif choix == "7":

                print("\nMerci d'avoir joué au jeu !!!")
                break


            else:

                print(
                    "\nChoix invalide."
                )