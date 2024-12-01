import csv

# File paths
ratings_file = "data/player_stats.csv"  # Existing CSV with Player, Rating, Goals+Assist
output_file = "data/final_stats.csv"  # Final CSV with Salaries added

# Load extracted salaries into a dictionary for easier lookup
salaries_dict = {}
with open("data/players_salaries.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        player = row["Player"]
        salary = row["Salary"]
        # Clean salary to extract only the numeric value or "Not Found"
        if "Not Found" not in salary:
            salary = salary.split(",")[0].replace('"', '').strip()  # Extract number
        salaries_dict[player] = salary

# Open the existing ratings file and merge the salaries
updated_rows = []
with open(ratings_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        player = row["Player"]
        salary = salaries_dict.get(player, "Not Found")  # Get salary or default to "Not Found"
        row["Salaries"] = salary  # Append the salary to the row
        updated_rows.append(row)

# Write the updated rows to a new CSV
with open(output_file, "w", newline="") as file:
    # Create fieldnames dynamically to include "Salaries"
    fieldnames = list(updated_rows[0].keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"Updated player data saved to {output_file}!")
