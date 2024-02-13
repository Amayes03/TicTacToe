from board import display_board, get_cell_selection, place_symbol, check_win, check_draw
from player import ask_for_usernames, select_first_player

# Fonction pour jouer le jeu
def play_game(update_counters, reset_counters, record_result):
    player1, player2 = ask_for_usernames()
    first_player = select_first_player(player1, player2)
    print(f"{first_player} starts!")

    games_played = 0   # Initialisation du compteur du jeu

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = first_player
        symbol = 'X'

        while True:
            display_board(board)
            row, col = get_cell_selection(current_player)

            place_symbol(board, row, col, symbol)
            if check_win(board, symbol):
                display_board(board)
                print(f"Player {current_player} wins!")
                record_result(current_player, player1 if current_player == player2 else player2, games_played)
                reset_counters()
                break

            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                update_counters("draw")
                games_played += 1  # Increment games_played counter
                break

            symbol = 'O' if symbol == 'X' else 'X'
            current_player = player1 if current_player == player2 else player2

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
