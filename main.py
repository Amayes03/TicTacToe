import csv
import random
from game import play_game
from menu import display_menu, handle_menu_choice
from hall_of_fame import record_result, show_hall_of_fame
from game_rules import display_game_rules


games_played = 0
draw_counter = 0

# Fonction pour mettre a jour les compteurs du jeu
def update_counters(result):
    global games_played, draw_counter
    games_played += 1
    if result == "draw":
        draw_counter += 1
    else:
        draw_counter = 0

# Fonction pour reinitialiser les compteurs du jeu
def reset_counters():
    global games_played, draw_counter
    games_played = 0
    draw_counter = 0

# Boucle principale du jeu
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        play_game(update_counters, reset_counters, record_result)
    elif choice == "2":
        display_game_rules()
    elif choice == "3":
        show_hall_of_fame()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
