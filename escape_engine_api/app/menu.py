def afficher_menu():
    print("\n=============================")
    print("       Find Pierrot")
    print("=============================")
    print("1. Jouer")
    print("2. Histoire ")
    print("3. Quitter")


def main():
    try:
        from app.game import Game
    except ModuleNotFoundError:
        from game import Game

    choix = 0

    while choix != 3:
        afficher_menu()

        try:
            choix = int(input("Votre choix : "))

            if choix == 1:
                Game().start()

            elif choix == 2:
                print("Ton Objectif est de retrouver Pierrot. C'est ton meilleur ami et il a disparu du jour au lendemain.\nTu es donc allé chez lui et à découvert dans son sous-sol un tunnel sombre menant vers l'inconnu.")

            elif choix == 3:
                print("Bonne Journée !")
                break
  

            else:
                print("Option invalide.")

        except ValueError:
            print("Entrer un nombre:")


if __name__ == "__main__":
    main()