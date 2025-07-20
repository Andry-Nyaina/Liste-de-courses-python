import sys 
import os
import json

Recup_chemin_dossier = os.path.dirname(__file__)
print(f"Le chemin du dossier est : {Recup_chemin_dossier}")
Chemin_fichier_json = os.path.join(Recup_chemin_dossier, "liste.json")

MENU = """Veuillez choisir un option :
1. Ajouter un élément à la liste de cources
2. Rétirer un élément de la liste de cources
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme 
Votre choix :"""


Menu_choix = ["1","2","3","4","5"]

if os.path.exists(Chemin_fichier_json):
    with open(Chemin_fichier_json, "r", encoding="utf-8") as f:
        LISTE = json.load(f)
else:
    LISTE = []



while True:
    choix = ""
    while choix not in Menu_choix:
        choix = input(MENU)
        if choix not in Menu_choix:
            print("Veuillez choisir une option valide !")
        if choix == "1":
            i = input("Veuillez entre votre course : ")
            LISTE.append(i)
            print(f"{i} a été ajouter dans votre liste de courses")
        elif choix == "2":
            i = input("Entrer le nom du liste que vous voulez retirer : ")
            if i in LISTE:
                LISTE.remove(i)
                print(f"L'élément {i} a bien été retirer de la liste ")
            else:
                print(f"L'élément {i} n'existe pas dans la liste, veuillez entrer un qui existe")
        elif choix == "3":
            for i, element in enumerate(LISTE):
                print(i+1, element)
        elif choix == "4":
            LISTE.clear()
            print("La liste du votre course a bien été vider")
        elif choix == "5":
            with open(Chemin_fichier_json, "w") as f:
                json.dump(LISTE, f, indent=4)
            print("Beybey !")
            sys.exit()
        print("-"*50)