while True:

    nombres = input("saisir une liste de nombres séparés par des virgules exemple 1,2, : ")

    liste = nombres.split(",")

    liste_entiers = []
    for item in liste:
        nombre_converti = int(item)
        liste_entiers.append(nombre_converti)

    resultat = sum(liste_entiers)
    print(f"Le total des nombre : {resultat}")

    moyenne = sum(liste_entiers) / len(liste_entiers)
    print (f"La moyenne des nombres : {moyenne}")

    def superieur(x):
        return x > moyenne 

    supp = list(filter(superieur, liste_entiers))
    print(f"La moyennes des nombres : {supp}")

    again = input("Voulez-vous refaire ? Oui / Non ")
    if again != "oui":
        print(f"fin du programme")
        break