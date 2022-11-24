#Importer la fonction random qui sert a la fonction "ordinateur"
import random
#Initialiser un tableau pour faire le morpion
tableau=["-","-","-",
         "-","-","-",
         "-","-","-"]
#Initialiser le joueur comme "X" pour dire que le premier joueur aura les "X"
joueur = "X"
#Initialiser winner egale a  rien juste pour le réutiliser par la suite sans crée une fonction 
winner=None
#Initialiser jeu égale a vrai pour le réutiliser après sans crée une fonction
jeu = True






#Définir la fonction printTableau pour afficher le tableau
def printTableau():
    #Afficher tableau[0]+tableau[1]+tableau[2] et " | " pour afficher mon tableau et crée une grille 
    print(tableau[0] + " | " + tableau[1]+ " | " + tableau[2])
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement
    print("----------")
    #Afficher tableau[3]+tableau[4]+tableau[5] et " | " pour afficher mon tableau et crée une grille 
    print(tableau[3] + " | " + tableau[4]+ " | " + tableau[5])
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement
    print("----------")
    #Afficher tableau[6]+tableau[5]+tableau[8] et " | " pour afficher mon tableau et crée une grille 
    print(tableau[6] + " | " + tableau[7]+ " | " + tableau[8])
    #Afficher "----------" pour crée une ligne dans ma grille pour séparer les signes proprement
    print("----------")

#Définir la fonction joueurInput
def joueurInput():
    #Assigner a inp une string int , int a un input qui dit "Entrer un nombre entre 1-9:"
    inp = int(input("Entrer un nombre entre 1-9:"))
    #Si inp est égale ou supérieur a 1 et inp égale ou inférieur a 9 et tableau inp-1 est bien égale a "-"
    if inp >= 1 and inp <= 9 and tableau[inp-1] == "-":
        #Assigner joueur a tableau inp-1
        tableau[inp-1] = joueur
    #Sinon afficher "Et non le joueur utilise déja cette case!"
    else:
        print("Et non le joueur utilise déjà cette case!")
#les wins et les loose 

#Définir la fonction Horizontale 
def Horizontale(tableau):
    #Utiliser global pour rappeller winner qu'on initialise au début 
    global winner 
    #Si tableau 0 égale a tableau 1 qui est égale a tableau 2 et tableau 1 différent de "-"
    if tableau[0] == tableau[1] == tableau[2] and tableau[1] == "-":
        #Alors assigner a winner tableau 0
        winner = tableau[0]
        #retourner Vrai
        return True
    #Sinon si tableau 3 égale a tableau 4 qui est égale a tableau 5 et tableau 3 différent de "-"
    elif tableau[3] == tableau[4] == tableau[5] and tableau[3] == "-":
        #Alors assigner a winner tableau 3
        winner = tableau[3]
        # Retourner Vrai
        return True
    #Sinon si tableau 6 égale a tableau 7 qui est égale a tableau 8 et tableau 6 différent de "-"
    elif tableau[6] == tableau[7] == tableau[8] and tableau[6] == "-":
        #Alors assigner a winner tableau 6
        winner = tableau[6]
        # Retourner Vrai 
        return True
#Définir la fonction ligne
def ligne(tableau):
    #Utiliser global pour rappeller winner qu'on initialise au début 
    global winner
    #Si tableau 0 égale a tableau 3 qui est égale a tableau 6 et tableau 0 différent de "-"
    if tableau[0] == tableau[3] == tableau[6] and tableau[0] == "-":
        #Alors assigner a winner tableau 0
        winner = tableau[0]
        #Retourner Vrai 
        return True
    #Sinon si tableau 1 égale a tableau 4 qui est égale a tableau 7 et tableau 1 différent de "-" 
    elif tableau[1] == tableau[4] == tableau[7] and tableau[1] == "-":
        #Alors assigner a winner tableau 1
        winner = tableau[1]
        #Retourner Vrai
        return True
    #Sinon si tableau 2 égale a tableau 5 qui est égale a tableau 8 et tableau 2 différent de "-" 
    elif tableau[2] == tableau[5] == tableau[8] and tableau[2] == "-":
        #Alors assigner a winner tableau 2
        winner = tableau[2]
        #Retourner Vrai
        return True 
#Définir la fonction diagonale
def diagonale(tableau):
    #Utiliser global pour rappeller winner qu'on initialise au début 
    global winner 
    #Si tableau 0 égale a tableau 4 qui est égale a tableau 8 et tableau 0 différent de "-"
    if tableau[0] == tableau[4] == tableau[8] and tableau[0] == "-":
        #Alors assigner a winner tableau 0
        winner = tableau[0]
        #Retourner Vrai
        return True
    #Sinon si tableau 2 égale a tableau 4 qui est égale a tableau 6 et tableau 2 différent de "-"
    elif tableau[2] == tableau[4] == tableau[6] and tableau[2] == "-":
        #Alors assigner a winner tableau 2
        winner = tableau[2]
        #Retourner Vrai
        return True 
#Définir la fontion égalité
def égalité(tableau):
    #Utiliser global pour rappeller jeu qu'on initialise au début 
    global jeu 
    #Si "-" n'est pas dans tableau
    if "-" not in tableau:
        #Alors j'appelle ma fonction printTableau
        printTableau(tableau)
        #Afficher "Egalité personne à gagner"
        print("Egalité personne à gagner")
        #Assigner Faux a jeu 
        jeu = False
#Définir la fonction Win
def Win(tableau):
    #Si la fonction diagonale ou la fonction Horizontale ou la fonction ligne
    if diagonale(tableau) or Horizontale(tableau) or ligne(tableau):
        #Alors afficher le winner avec la phrase "The winner is {winner} " , {winner} sert a dire qui est le winner joueur "X" ou joueur "O"
        print(f"The winner is {winner}")




#player 
#Définir la fonction switchJoueur
def switchJoueur():
    #Utiliser global pour rappeller jeu qu'on initialise au début 
    global joueur
    #Si joueur est égale a "X"
    if joueur == "X":
        #Alors assigner  "O" a joueur 
        joueur = "O"
    #Sinon assigner "X" a joueur 
    else:
        joueur = "X"


#Non utiliser ppur l'instant donc je le met en commentaire pour pas qu'il soit pris en compte dans le code 
# ordinateur
def ordinateur(tableau):
    while joueur == "O":
        position = random.randint(0,8)
        if tableau[position] == "-":
            tableau[position] = "O"
            switchJoueur()





#Crée une boucle pour éxécuter toutes les fonctions utiliser
while jeu:
    #Executer la fonction printTableau
    printTableau()
    #Executer la fonction joueurInput
    joueurInput()
    #Executer la fonction Win
    Win(tableau)
    #Executer la fonction ligne
    ligne(tableau)
    #Executer la fonction switchJoueur 
    switchJoueur()

    #Les fonctions qui permettent d'éxecuter toute la fonction Ordinateur non utilisé pour l'instant
    ordinateur(tableau)
    Win(tableau)
    ligne(tableau)


