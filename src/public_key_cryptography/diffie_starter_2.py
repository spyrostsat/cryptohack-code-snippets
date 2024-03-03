from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))


p = 28151

primitive_root = None

for g in range(2, p):
	is_primitive_root = True
	numbers_included = []
	for i in range(1, p):
		numbers_included.append(pow(g, i, p))
  
	if len(set(numbers_included)) == p-1:
		primitive_root = g
		break

print(primitive_root)