# Find_Pierrot
Petit jeu en python Backend


NORME DE COMMITS :

{ADD} = ajout de code
{FIX} = corriger un bug
{REMOVE} = suppression du code

exemple : git commit -m "{ADD} Ajout de la mécanique de déplacement"





Étapes de lancements de l'API :

cd Find_Pierrot
cd escape_engine_api
python -m uvicorn app.main:app --reload


(/docs dans la barre de l'url pour accéder à la doc)





-Tests possibles (l'essentiel) :



curl -X 'GET' \
  'http://127.0.0.1:8000/players/1' \               // Obtenir les informations sur un joueur (içi le 1)
  -H 'accept: */*'




curl -X 'PUT' \
  'http://127.0.0.1:8000/players/2' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{                                                                         // Pour update les informations d'un joueur (içi le 2) 
  "name": "Pierrot",
  "score": 0,
  "life": true
}'







curl -X 'POST' \
  'http://127.0.0.1:8000/players' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \                                           //créer un joueur 
  -d '{
  "name": "Gabor",
  "score": 0,
  "life": true
}




curl -X 'DELETE' \
  'http://127.0.0.1:8000/players/3' \                              // Supprimer un joueur (en fonction de son ID)
  -H 'accept: */*





curl -X 'GET' \
  'http://127.0.0.1:8000/objets' \                                           // obtenir la liste des objets 
  -H 'accept: */*'





curl -X 'GET' \
  'http://127.0.0.1:8000/salles' \                                      // obtenir la liste des salles et leurs atributs
  -H 'accept: */*'





curl -X 'GET' \
  'http://127.0.0.1:8000/enigmes' \                                       //Obtenir la liste des énigmes et leur stade de résolution
  -H 'accept: */*'




  curl -X 'GET' \
  'http://127.0.0.1:8000/notes' \                                            //obtenir toutes les notes du jeu
  -H 'accept: */*'





  curl -X 'GET' \
  'http://127.0.0.1:8000/game/state' \                                              //Dans quel état se trouve le jeu (Ou est le joueur, dans quel pièce se trouve-t-il etc)
  -H 'accept: */*'







curl -X 'POST' \
  'http://127.0.0.1:8000/game/answer' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \                                                 //Perment de répondre à une énigme et de voir les attributs de la salle
  -d '{
  "reponse": "5"
}'






curl -X 'POST' \
  'http://127.0.0.1:8000/game/objects/1/pickup' \                                          //Permet de rammaser des objets selon la salle
  -H 'accept: */*' \
  -d ''

