from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import extended_gcd

print(extended_gcd(13, 3))