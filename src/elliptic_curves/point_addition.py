from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))


from src.utils import ecc_points_addition

P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

# E: Y2 = X3 + 497 X + 1768, p: 9739
a = 497
b = 1768
p = 9739

# test
X = (5274, 2841)
Y = (8669, 740)
S = ecc_points_addition(X, X, a, p)
print(S, S == (7284, 2107))
S = ecc_points_addition(X, Y, a, p)
print(S, S == (1024, 4440))

print("=" * 50)
# S(x,y) = P + P + Q + R
S = ecc_points_addition(P, P, a, p)
S = ecc_points_addition(S, Q, a, p)
S = ecc_points_addition(S, R, a, p)
print('P + P + Q + R = ', S)
