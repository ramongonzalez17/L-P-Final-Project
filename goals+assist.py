import csv

original_file = "data/player_stats.csv" 
new_file = "data/salaries.csv"  

original_names = []
with open(original_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        original_names.append(row["Player"])

goals_assists_data = {}
with open(new_file, "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    name = lines[i].strip()  
    if name in original_names:  
        if i + 2 < len(lines):  
            goals_assists = lines[i + 2].strip() 
            if goals_assists.replace('.', '', 1).isdigit():  
                goals_assists_data[name] = goals_assists

updated_data = []
with open(original_file, "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames + ["Goals+Assists"] 

    for row in reader:
        name = row["Player"]
        if name in goals_assists_data:
            row["Goals+Assists"] = goals_assists_data[name]  
        else:
            row["Goals+Assists"] = .5  
        updated_data.append(row)

output_file = "data/players_ratings_updated.csv"
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(updated_data)

print(f"Updated data saved to {output_file}!")
