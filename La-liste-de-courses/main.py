import sys

LISTE = []

MENU = """Veuillez choisir un option :
1. Ajouter un élément à la liste de cources
2. Rétirer un élément de la liste de cources
3. Afficher les éléments de la liste de courses
4. Vider la liste de courses
5. Quitter le programme 
Votre choix :"""

Menu_choix = ["1", "2", "3", "4", "5"]

while True:
    choix = ""
    while choix not in Menu_choix:
        choix = input(MENU)
        if choix not in Menu_choix:
            print("Veiullez choisir une option valide !")
    if choix == "1":
        i = input("Veuillez entrer votre course : ")
        LISTE.append(i)
        print(f'{i} a été ajouter dans votre liste de courses')   
    elif choix == "2":
        i = input("Entrer le nom du liste que vous voulez retirer: ")
        if i in LISTE:
            LISTE.remove(i)
            print(f"L'élémént {i} a bien été retirer de la liste")
        else:
            print(f"L'élément {i} n'existe pas dans la liste, veuillez entrer un qui existe")
    elif choix == "3":
        for i, element in enumerate(LISTE):
            print(i+1,"-",element)
    elif choix == "4":
        LISTE.clear()
        print("La liste du course a bien été vider")
    elif choix == "5":
        print("Au revoir !!")
        sys.exit()
    print("-"*50)
