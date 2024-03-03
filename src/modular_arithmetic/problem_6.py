from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

p = 29
ints = [14, 6, 11]

for num in ints:
    square_root_exists = False
    for a in range(1, p):
        if (a ** 2) % p == num:
            print(f'{num} has a square root of {a} mod {p}')
            square_root_exists = True
            break
    if not square_root_exists:
        print(f'{num} has no square root mod {p}')
