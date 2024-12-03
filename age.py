import csv

ages_file = "./data/Player_Ages.csv"  
stats_file = "./data/final_stats.csv" 
output_file = "updated_final_statss.csv"  

ages_dict = {}
with open(ages_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 2:  
            continue
        player_name = row[0].strip()
        age = row[1].strip()
        ages_dict[player_name] = age  

updated_rows = []
with open(stats_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        player_name = row["Player"]  
        age = ages_dict.get(player_name, "Not Found")  
        row["Age"] = age  
        updated_rows.append(row)

with open(output_file, "w", newline="") as file:
    fieldnames = list(updated_rows[0].keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

print(f"Updated player stats saved to {output_file}!")
