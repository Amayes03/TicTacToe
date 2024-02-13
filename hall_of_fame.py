import csv

# Fonction pour enregistrer le résultat du jeu dans le fichier Hall of Fame
def record_result(winner, loser, games_played):
    with open("hall_of_fame.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([winner, loser])

# Fonction d’affichage du Hall of Fame
def show_hall_of_fame():
    with open("hall_of_fame.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            winner, loser = row
            print(f"Winner: {winner} - Loser: {loser}")
