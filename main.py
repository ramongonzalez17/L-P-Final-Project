import csv

# Correct relative path to the file
data_file = "data/salaries.csv"

old = "data/salaries.csv"


with open(data_file, "r") as file:
    lines = file.readlines()

player_data = []

i = 0  # Start from the first line
while i < len(lines):
    name = lines[i].strip()  # First line is the player's name
    if i + 2 < len(lines):
        rating = lines[i + 2].strip()  # Third line is the player's rating
        if rating.replace('.', '', 1).isdigit():  # Ensure the rating is numeric
            player_data.append([name, rating])  # Only add name and rating
    i += 5  # Move to the next block of 4 lines

# Save to a new CSV file
output_file = "data/players_ratings.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Player", "Rating"])  # Header row
    writer.writerows(player_data)

print(f"Data saved to {output_file}!")
