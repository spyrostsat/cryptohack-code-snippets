from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import *

import pwn
from src.utils import *

input_string_str = "label"
input_string = string_to_binary(input_string_str)

num_int = 13
num = ""
for _ in range(len(input_string_str)):
	num += int_to_binary(num_int).zfill(8)
 
xor_result = xor_strings(input_string, num)
xor_result = binary_to_string(xor_result)
print(xor_result)

print(pwn.xor(b'label', 13))  # Test the result with pwn.xor