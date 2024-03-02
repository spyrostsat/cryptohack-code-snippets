from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.utils import *


key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_xor_key2= "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_xor_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_key1_xor_key2_xor_key3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


key1_binary = hex_to_binary(key1)
key1_xor_key2_binary = hex_to_binary(key1_xor_key2)
key2_xor_key3_binary = hex_to_binary(key2_xor_key3)
flag_xor_key1_xor_key2_xor_key3_binary = hex_to_binary(flag_xor_key1_xor_key2_xor_key3)

# Make sure both keys are of equal length, if not, pad the shorter one with zeros
key1_binary, key1_xor_key2_binary = strings_equal_length_or_zfill(key1_binary, key1_xor_key2_binary)

# Retrieve the key2 by XORing key1 with key1_xor_key2
key2_binary = xor_strings(key1_binary, key1_xor_key2_binary)
print(len(key2_binary))

# Make sure both keys are of equal length, if not, pad the shorter one with zeros
key2_binary, key2_xor_key3_binary = strings_equal_length_or_zfill(key2_binary, key2_xor_key3_binary)

# Retrieve the key3 by XORing key2 with key2_xor_key3
key3_binary = xor_strings(key2_binary, key2_xor_key3_binary)
print(len(key3_binary))

key1_xor_key2_xor_key3_binary = xor_strings(key1_xor_key2_binary, key3_binary)

flag_xor_key1_xor_key2_xor_key3_binary, key1_xor_key2_xor_key3_binary = strings_equal_length_or_zfill(flag_xor_key1_xor_key2_xor_key3_binary, key1_xor_key2_xor_key3_binary)

# Retrieve the flag by XORing flag_xor_key1_xor_key2_xor_key3 with key1_xor_key2_xor_key3
flag_binary = xor_strings(flag_xor_key1_xor_key2_xor_key3_binary, key1_xor_key2_xor_key3_binary)

# Convert the binary flag to ASCII
flag = binary_to_string(flag_binary)
print(flag)