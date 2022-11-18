#Importer la fonction random qui sert a la fonction "ordinateur"
#Initialiser un tableau pour faire le morpion
#Initialiser le joueur comme "X" pour dire que le premier joueur aura les "X"
#Initialiser winner egale a  rien juste pour le réutiliser par la suite sans crée une fonction 
#Initialiser jeu égale a vrai pour le réutiliser après sans crée une fonction



#Définir la fonction printTableau pour afficher le tableau
    #Afficher tableau[0]+tableau[1]+tableau[2] et " | " pour afficher mon tableau et crée une grille
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement
    #Afficher tableau[3]+tableau[4]+tableau[5] et " | " pour afficher mon tableau et crée une grille     
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement 
    #Afficher tableau[6]+tableau[5]+tableau[8] et " | " pour afficher mon tableau et crée une grille
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement


#Définir la fonction joueurInput
    #Assigner a inp une string int , int a un input qui dit "Entrer un nombre entre 1-9:"
    #Si inp est égale ou supérieur a 1 et inp égale ou inférieur a 9 et tableau inp-1 est bien égale a "-"
        #Assigner joueur a tableau inp-1
    #Sinon afficher "Et non le joueur utilise déja cette case!"



#Définir la fonction Horizontale
    #Utiliser global pour rappeller winner qu'on initialise au début
    #Si tableau 0 égale a tableau 1 qui est égale a tableau 2 et tableau 1 différent de "-"
        #Alors assigner a winner tableau 0
        #retourner Vrai
    #Sinon si tableau 3 égale a tableau 4 qui est égale a tableau 5 et tableau 3 différent de "-"
        #Alors assigner a winner tableau 3
        #retourner Vrai
    #Sinon si tableau 6 égale a tableau 7 qui est égale a tableau 8 et tableau 6 différent de "-"
        #Alors assigner a winner tableau 6
        #retourner Vrai



#Définir la fonction ligne
    #Utiliser global pour rappeller winner qu'on initialise au début
    #Si tableau 0 égale a tableau 3 qui est égale a tableau 6 et tableau 0 différent de "-"
        #Alors assigner a winner tableau 0
        #Retourner Vrai
    #Sinon si tableau 1 égale a tableau 4 qui est égale a tableau 7 et tableau 1 différent de "-"
        #Alors assigner a winner tableau 1
        #Retourner Vrai
    #Sinon si tableau 2 égale a tableau 5 qui est égale a tableau 8 et tableau 2 différent de "-"
        #Alors assigner a winner tableau 2
        #Retourner Vrai



#Définir la fonction diagonale
    #Utiliser global pour rappeller winner qu'on initialise au début
    #Si tableau 0 égale a tableau 4 qui est égale a tableau 8 et tableau 0 différent de "-"
        #Alors assigner a winner tableau 0
        #Retourner Vrai
    #Sinon si tableau 2 égale a tableau 4 qui est égale a tableau 6 et tableau 2 différent de "-"
        #Alors assigner a winner tableau 2
        #Retourner Vrai



#Définir la fontion égalité
    #Utiliser global pour rappeller jeu qu'on initialise au début
    #Si "-" n'est pas dans tableau
        #Alors j'appelle ma fonction printTableau
        #Afficher "Egalité personne à gagner"
        #Assigner Faux a jeu



#Définir la fonction Win
    #Si la fonction diagonale ou la fonction Horizontale ou la fonction ligne
        #Alors afficher le winner avec la phrase "The winner is {winner} " , {winner} sert a dire qui est le winner joueur "X" ou joueur "O"



#Définir la fonction switchJoueur
    #Utiliser global pour rappeller jeu qu'on initialise au début 
    #Si joueur est égale a "X"
        #Alors assigner  "O" a joueur
    #Sinon assigner "X" a joueur




#Non utiliser ppur l'instant donc je le met en commentaire pour pas qu'il soit pris en compte dans le code 
#ordinateur
# def ordinateur():
#     while joueur == "O":
#         position = random.randint(0,8)
#         if tableau[position] == "-":
#             tableau[position] = "O"
#             switchJoueur()



#Crée une boucle pour éxécuter toutes les fonctions utiliser
    #Executer la fonction printTableau
    #Executer la fonction joueurInput
    #Executer la fonction Win
    #Executer la fonction ligne
    #Executer la fonction switchJoueur


    #Les fonctions qui permettent d'éxecuter toute la fonction Ordinateur non utilisé pour l'instant
    # ordinateur()
    # Win()
    # ligne()
