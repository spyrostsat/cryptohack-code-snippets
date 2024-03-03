from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))


def mul_mod(a, b, mod):
    return ((a % mod)*(b % mod)) % mod


p = 991
g = 209

for i in range(p):
   if(mul_mod(i, g, p)==1):
       print(i)
       break
