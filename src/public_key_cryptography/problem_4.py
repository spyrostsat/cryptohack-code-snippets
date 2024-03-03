from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import extended_gcd, is_prime

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# print(f"Is p prime? {is_prime(p)}")
# print(f"Is q prime? {is_prime(q)}")

n = p * q

phi = (p - 1) * (q - 1)

gcd, x, y = extended_gcd(e, phi)

print(f"GCD: {gcd}")
print(f"x: {x}")
print(f"y: {y}")