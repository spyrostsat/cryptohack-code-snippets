from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import extended_gcd

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
print(f"gcd({p}, {q}) = {gcd} \t u = {u} \t v = {v} \t {p} * {u} + {q} * {v} = {gcd}")