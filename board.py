# Fonction pour afficher le tableau de jeu
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Fonction permettant de sélectionner une cellule
def get_cell_selection(player):
    print(player + ", it's your turn.")
    while True:
        try:
            row = int(input("Enter the row number (1-3): ")) - 1
            col = int(input("Enter the column number (1-3): ")) - 1
            if not is_valid_cell(row, col):
                raise ValueError
            break
        except ValueError:
            print("Invalid cell selection. Please try again.")
    return row, col

# Fonction permettant de vérifier si la cellule choisie est valide
def is_valid_cell(row, col):
    if row < 0 or row >= 3 or col < 0 or col >= 3:
        return False
    return True

# Fonction pour placer le symbole dans la cellule choisie
def place_symbol(board, row, col, symbol):
    board[row][col] = symbol

# Fonction de vérification de victoire
def check_win(board, symbol):
    # lignes
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

# Fonction de vérification de match nul
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True
