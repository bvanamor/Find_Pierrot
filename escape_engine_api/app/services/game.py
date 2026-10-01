from app.models.salle import Salle
from app.models.enigme import Enigme
from app.models.note import Note


class Game:
    def __init__(self):
        self.salles = []
        self.notes = []
        self.enigmes = []
        self.etape = 1

    def ajouter_salle(self, salle: Salle):
        self.salles.append(salle)

    def ajouter_note(self, note: Note):
        self.notes.append(note)

    def ajouter_enigme(self, enigme: Enigme):
        self.enigmes.append(enigme)


    def afficher_notes(self):
        print("\n===== NOTES ET INDICES =====")

        if not self.notes:
            print("Aucune note trouvée.")
            return

        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note.titre}")


    def lire_note(self, numero):
        if numero < 1 or numero > len(self.notes):
            print("Cette note n'existe pas.")
            return

        note = self.notes[numero - 1]

        print("\n===== NOTE =====")
        print(f"Titre : {note.titre}")
        print()
        print(note.lire())


    def repondre(self, reponse_joueur):

        if self.etape > len(self.enigmes):
            print("\nToutes les énigmes sont terminées !")
            return

        enigme = self.enigmes[self.etape - 1]

        recompense = enigme.verifier(reponse_joueur)

        if recompense:
            print("\n======================")
            print("    BONNE RÉPONSE !")
            print("======================")

            print(f"Récompense : {recompense}")

            self.etape += 1

            print(f"Nouvelle étape : {self.etape}")

        else:
            print("\nMauvaise réponse.")
            print("Essayez encore.")


    def afficher_menu(self):

        while True:

            print("\n")
            print("==============================")
            print("        ESCAPE GAME")
            print("==============================")
            print(f"Étape actuelle : {self.etape}")
            print()
            print("1. Voir les notes")
            print("2. Lire une note")
            print("3. Répondre à l'énigme")
            print("4. Quitter")
            print("==============================")

            choix = input("Votre choix : ")


            if choix == "1":

                self.afficher_notes()


            elif choix == "2":

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


            elif choix == "3":

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


            elif choix == "4":

                print("\nMerci d'avoir joué !")
                break


            else:

                print(
                    "\nChoix invalide."
                )