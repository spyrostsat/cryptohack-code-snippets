from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

p = 17
q = 23

n = p * q
e = 65537

plaintext = 12
ciphertext = pow(plaintext, e, n)
print(ciphertext)