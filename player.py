import random

# Demander aux joueurs d'entrer leurs noms d'utilisateur
def ask_for_usernames():
    player1 = input("Enter Player 1 username: ")
    player2 = input("Enter Player 2 username: ")
    return player1, player2

# Sélectionner le premier joueur aléatoirement
def select_first_player(player1, player2):
    first_player = random.choice([player1, player2])
    return first_player
