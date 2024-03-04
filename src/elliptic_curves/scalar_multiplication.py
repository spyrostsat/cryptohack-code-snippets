from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))


from src.utils import ecc_scalar_multiplication


# E: Y2 = X3 + 497 X + 1768, p: 9739
a = 497
b = 1768
p = 9739

n = 1337
X = (5323, 5438)
S = ecc_scalar_multiplication(X, n, a, p)
print(S, S == (1089, 6931))

P = (2339, 2213)
n = 7863
S = ecc_scalar_multiplication(P, n, a, p)
print(S)
