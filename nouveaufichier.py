from random import choice
from os import system
import platform

JOUEUR = -1
ORDI = +1
PLATEAU = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, ORDI):
        score = +1
    elif wins(state, JOUEUR):
        score = -1
    else:
        score = 0

    return score

def wins(etat, joueur):
    win_etat = [
        [etat[0][0], etat[0][1], etat[0][2]],
        [etat[1][0], etat[1][1], etat[1][2]],
        [etat[2][0], etat[2][1], etat[2][2]],
        [etat[0][0], etat[1][0], etat[2][0]],
        [etat[0][1], etat[1][1], etat[2][1]],
        [etat[0][2], etat[1][2], etat[2][2]],
        [etat[0][0], etat[1][1], etat[2][2]],
        [etat[2][0], etat[1][1], etat[0][2]],
    ]
    if [joueur, joueur, joueur] in win_etat:
        return True
    else:
        return False

def game_over(etat):
    return wins(etat, JOUEUR) or wins(etat, ORDI)


def cellule_vide(etat):
    cells = []

    for x, row in enumerate(etat):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_movement(x, y):
    if [x, y] in cellule_vide(PLATEAU):
        return True
    else:
        return False

def set_move(x, y, joueur):
    if valid_movement(x, y):
        PLATEAU[x][y] = joueur
        return True
    else:
        return False

def minimax(etat, incr, joueur):
    if joueur == ORDI:
        best = [-1, -1, -float('inf')]
    else:
        best = [-1, -1, +float('inf')]

    if incr == 0 or game_over(etat):
        score = evaluate(etat)
        return [-1, -1, score]

    for cell in cellule_vide(etat):
        x, y = cell[0], cell[1]
        etat[x][y] = joueur
        score = minimax(etat, incr - 1, -joueur)
        etat[x][y] = 0
        score[0], score[1] = x, y

        if joueur == ORDI:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def affiche(etat, o_choice, j_choice):
    chars = {
        -1: j_choice,
        +1: o_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in etat:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def tour_ordi(o_choice, j_choice):

    incr = len(cellule_vide(PLATEAU))
    if incr == 0 or game_over(PLATEAU):
        return

    clean()
    print(f'Tour de ordinateur [{o_choice}]')
    affiche(PLATEAU, o_choice, j_choice)

    if incr == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(PLATEAU, incr, ORDI)
        x, y = move[0], move[1]

    set_move(x, y, ORDI)
    #time.sleep(1)

def tour_joueur(o_choice, j_choice):
    incr = len(cellule_vide(PLATEAU))
    if incr == 0 or game_over(PLATEAU):
        return

    # Dictionnaires des bon mouvements
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Tour joueur [{j_choice}]')
    affiche(PLATEAU, o_choice, j_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Utilisé le clavier numérique (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], JOUEUR)

            if not can_move:
                print('Mauvais mouvement')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choix')

def main():
    clean()
    j_choice = ''  # X or O
    o_choice = ''  # X or O
    first = ''  # Si le joueur est premier

    # Choix de X ou O pour le joueur
    while j_choice != 'O' and j_choice != 'X':
        try:
            print('')
            j_choice = input('Choisie X ou O\n: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choi')

    # Choix pour l'ordinateur
    if j_choice == 'X':
        o_choice = 'O'
    else:
        o_choice = 'X'

    # Joueur joue en premier
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('Premier à jouer?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choix')

    # boucle principal 
    while len(cellule_vide(PLATEAU)) > 0 and not game_over(PLATEAU):
        if first == 'N':
            tour_ordi(o_choice, j_choice)
            first = ''

        tour_joueur(o_choice, j_choice)
        tour_ordi(o_choice, j_choice)

    # Game over message
    if wins(PLATEAU, JOUEUR):
        clean()
        print(f'Tour joueur [{j_choice}]')
        affiche(PLATEAU, o_choice, j_choice)
        print('GAGNER!')
    elif wins(PLATEAU, ORDI):
        clean()
        print(f'Tour ordinateur [{o_choice}]')
        affiche(PLATEAU, o_choice, j_choice)
        print('PERDU!')
    else:
        clean()
        affiche(PLATEAU, o_choice, j_choice)
        print('EGALITE!')

    exit()

main()