from fastapi import HTTPException

from app.models.game import (
    ObjetResponse,
    EnigmeResponse,
    NoteResponse,
    SalleResponse,
    GameStateResponse,
)


class GameService:

    def __init__(self, game):
        self.game = game

    def get_objets(self):
        objets_api = []
        objet_id = 1

        for salle_id, salle in enumerate(self.game.salles, start=1):
            for objet in salle.objets:
                objets_api.append(
                    ObjetResponse(
                        id=objet_id,
                        salle_id=salle_id,
                        nom=objet.get_nom(),
                        position=objet.position,
                        health_effect=objet.health_effect,
                        enigme_effect=objet.enigme_effect,
                        points=objet.get_points(),
                    )
                )

                objet_id += 1

        return objets_api

    def get_objet(self, objet_id: int):
        for objet in self.get_objets():
            if objet.id == objet_id:
                return objet

        raise HTTPException(
            status_code=404,
            detail="L'objet n'existe pas",
        )

    def get_enigmes(self):
        enigmes_api = []
        enigme_id = 1

        for salle_id, salle in enumerate(self.game.salles, start=1):
            for enigme in salle.enigmes:
                enigmes_api.append(
                    EnigmeResponse(
                        id=enigme_id,
                        salle_id=salle_id,
                        question=enigme.question,
                        resolue=enigme.resolue,
                        recompense=enigme.recompense,
                    )
                )

                enigme_id += 1

        return enigmes_api

    def get_enigme(self, enigme_id: int):
        for enigme in self.get_enigmes():
            if enigme.id == enigme_id:
                return enigme

        raise HTTPException(
            status_code=404,
            detail="L'énigme n'existe pas",
        )

    def get_notes(self):
        notes_api = []
        note_id = 1

        for salle_id, salle in enumerate(self.game.salles, start=1):
            for note in salle.notes:
                notes_api.append(
                    NoteResponse(
                        id=note_id,
                        salle_id=salle_id,
                        nom=note.get_nom(),
                        contenu=note.contenu,
                        points=note.get_points(),
                    )
                )

                note_id += 1

        return notes_api

    def get_note(self, note_id: int):
        for note in self.get_notes():
            if note.id == note_id:
                return note

        raise HTTPException(
            status_code=404,
            detail="La note n'existe pas",
        )

    def get_salles(self):
        objets = self.get_objets()
        enigmes = self.get_enigmes()
        notes = self.get_notes()

        salles = []

        for salle_id, salle in enumerate(self.game.salles, start=1):
            salles.append(
                SalleResponse(
                    id=salle_id,
                    nom=salle.nom,
                    description=salle.description,
                    terminee=salle.terminee,
                    objets=[
                        objet
                        for objet in objets
                        if objet.salle_id == salle_id
                    ],
                    enigmes=[
                        enigme
                        for enigme in enigmes
                        if enigme.salle_id == salle_id
                    ],
                    notes=[
                        note
                        for note in notes
                        if note.salle_id == salle_id
                    ],
                )
            )

        return salles

    def get_salle(self, salle_id: int):
        salles = self.get_salles()

        if salle_id < 1 or salle_id > len(salles):
            raise HTTPException(
                status_code=404,
                detail="La salle n'existe pas",
            )

        return salles[salle_id - 1]

    def get_salle_objets(self, salle_id: int):
        salle = self.get_salle(salle_id)
        return salle.objets

    def get_salle_enigmes(self, salle_id: int):
        salle = self.get_salle(salle_id)
        return salle.enigmes

    def get_salle_notes(self, salle_id: int):
        salle = self.get_salle(salle_id)
        return salle.notes

    def get_game_state(self):
        salle = self.get_salle(self.game.salle_actuelle + 1)

        return GameStateResponse(
            player_id=self.game.joueur.player_id,
            player_name=self.game.joueur.get_nom(),
            score=self.game.joueur.score,
            life=self.game.joueur.life,
            etape=self.game.etape,
            salle_actuelle=self.game.salle_actuelle + 1,
            salle=salle,
        )

    def answer_enigme(self, reponse: str):
        if self.game.etape > len(self.game.enigmes):
            raise HTTPException(
                status_code=404,
                detail="Toutes les énigmes sont déjà résolues",
            )

        enigme = self.game.enigmes[self.game.etape - 1]

        if not enigme.verifier(reponse):
            raise HTTPException(
                status_code=400,
                detail="Mauvaise réponse",
            )

        self.game.etape += 1

        self.game.salle.verifier_salle()

        if self.game.salle_actuelle < len(self.game.salles) - 1:
            self.game.salle_actuelle += 1

        return self.get_game_state()

    def pickup_object(self, objet_id: int):
        objet = next(
            (
                item
                for item in self.get_objets()
                if item.id == objet_id
            ),
            None,
        )

        if objet is None:
            raise HTTPException(
                status_code=404,
                detail="L'objet n'existe pas",
            )

        salle = self.game.salles[objet.salle_id - 1]

        objet_du_jeu = next(
            (
                item
                for item in salle.objets
                if item.get_nom() == objet.nom
            ),
            None,
        )

        if objet_du_jeu is None:
            raise HTTPException(
                status_code=404,
                detail="L'objet n'est plus disponible",
            )

        salle.objets.remove(objet_du_jeu)

        self.game.joueur.ramasser(objet_du_jeu)

        return self.get_game_state()

