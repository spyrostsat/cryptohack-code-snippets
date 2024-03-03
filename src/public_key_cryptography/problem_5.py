from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import extended_gcd, is_prime

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

n = p * q

phi = (p - 1) * (q - 1)

gcd, x, y = extended_gcd(e, phi)

d = x

N = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932

plaintext = pow(c, d, N)
print(plaintext)