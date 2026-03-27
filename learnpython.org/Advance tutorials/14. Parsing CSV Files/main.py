import csv
from io import StringIO

csv_data = """name,hp,exp
Slime, 20, 5
Goblin, 50, 15
Dragon, 1000, 500"""

f = StringIO(csv_data)

reader = csv.DictReader(f)

for row in reader:
    print(f"{row['name']} has {row['hp']} HP and gives {row['exp']} EXP")