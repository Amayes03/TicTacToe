# Fonction pour afficher les règles du jeu
def display_game_rules():
    print("""Two players compete in a turn-based game on a 3x3 board (3 rows and 3 columns).
Player 1 will have the symbol 'X' while Player 2 will have the symbol 'O'.
Players must place their symbols on an empty cell of the board by entering the corresponding coordinates for the cell (Example: 1,2 re
Players take turns placing a symbol in each round. The goal of the game is to align three identical symbols horizontally, vertically,
If neither player is able to align 3 identical symbols when the board is filled, the game ends in a draw.
At the end of the game, our winners will be recorded in our "Hall of Fame"!""")
