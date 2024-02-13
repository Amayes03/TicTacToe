from game import play_game
from game_rules import display_game_rules
from hall_of_fame import show_hall_of_fame

# Fonction pour afficher le menu
def display_menu():
    print("\nMenu:")
    print("1. Play")
    print("2. Game rules")
    print("3. Show our Hall of Fame")
    print("4. Quit")

# Fonction pour gérer le choix du menu
def handle_menu_choice(choice):
    if choice == "1":
        play_game()
    elif choice == "2":
        display_game_rules()
    elif choice == "3":
        show_hall_of_fame()
    elif choice == "4":
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.\n")
