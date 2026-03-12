# exercise
import re

all_functions = dir(re)

print(all_functions)

find_related = [name for name in all_functions if "find" in name]

print(f"Functions in 're' that contain 'find': {find_related}")