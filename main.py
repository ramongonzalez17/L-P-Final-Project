import csv

data_file = "data/salaries.csv"

old = "data/salaries.csv"


with open(data_file, "r") as file:
    lines = file.readlines()

player_data = []

i = 0 
while i < len(lines):
    name = lines[i].strip()  
    if i + 2 < len(lines):
        rating = lines[i + 2].strip()  
        if rating.replace('.', '', 1).isdigit():  
            player_data.append([name, rating])  
    i += 5  

output_file = "data/players_ratings.csv"
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Player", "Rating"])  
    writer.writerows(player_data)

print(f"Data saved to {output_file}!")
