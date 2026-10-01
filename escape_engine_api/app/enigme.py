class Enigme:
    def __init__(self, question, reponse, recompense):
        self.question = question
        self.reponse = reponse
        self.recompense = recompense
        self.resolue = False

    def verifier(self, reponse_joueur):
        if self.resolue:
            return None

        if reponse_joueur.strip().lower() == self.reponse.lower():
            self.resolue = True
            return self.recompense

        return None