import csv

ratings_file = "data/player_stats.csv"  
output_file = "data/final_stats.csv"  

salaries_dict = {}
with open("data/players_salaries.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        player = row["Player"]
        salary = row["Salary"]
        if "Not Found" not in salary:
            salary = salary.split(",")[0].replace('"', '').strip()  
        salaries_dict[player] = salary

updated_rows = []
with open(ratings_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        player = row["Player"]
        salary = salaries_dict.get(player, "Not Found") 
        row["Salaries"] = salary  
        updated_rows.append(row)

with open(output_file, "w", newline="") as file:
    fieldnames = list(updated_rows[0].keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"Updated player data saved to {output_file}!")
