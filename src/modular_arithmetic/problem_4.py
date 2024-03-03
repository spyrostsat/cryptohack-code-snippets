from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import is_prime

p = 65537
print(f"Is {p} prime? {is_prime(p)}")

a = 273246787654

print(f"Is a divisible by {p}? {a % p == 0}")

print(f"By Fermat's Little Theorem, a^{p-1} % p = 1")