from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import sub_bytes, matrix2bytes
from src.const import inv_s_box

state = [
    [251, 64, 182, 81],
    [146, 168, 33, 80],
    [199, 159, 195, 24],
    [64, 80, 182, 255],
]

print(matrix2bytes(sub_bytes(state, inv_s_box)))