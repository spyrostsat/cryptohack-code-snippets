from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

phi = (p - 1) * (q - 1)
print(phi)