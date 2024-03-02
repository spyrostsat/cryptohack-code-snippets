from typing import Tuple


def string_to_binary(input_string: str) -> str:
    binary_repr = ''
    for char in input_string:
        # Get ASCII value of character
        ascii_value = ord(char)
        # Convert ASCII value to binary and concatenate to binary_repr
        binary_repr += bin(ascii_value)[2:].zfill(8)  # [2:] to remove '0b' prefix, zfill(8) to ensure 8 bits
    return binary_repr


def int_to_binary(input_int: int) -> str:
    return bin(input_int)[2:]


def binary_to_string(binary_repr: str) -> str:
	# Split binary_repr into 8-bit chunks
	binary_chunks = [binary_repr[i:i + 8] for i in range(0, len(binary_repr), 8)]
	# Convert each 8-bit chunk to ASCII and concatenate to result
	result = ''
	for chunk in binary_chunks:
		result += chr(int(chunk, 2))
	return result


def xor_strings(string1: str, string2: str) -> str:
	if len(string1) != len(string2): raise ValueError("Both strings must be of equal length")
	if not all(char in '01' for char in string1) or not all(char in '01' for char in string2): raise ValueError("Both strings must be binary")
 
	result = ''
	for i in range(len(string1)):
		result += str(int(string1[i]) ^ int(string2[i]))

	return result


def hex_to_binary(hex_string: str) -> str:
	return bin(int(hex_string, 16))[2:]


def strings_equal_length_or_zfill(string1: str, string2: str) -> Tuple[str, str]:
	if len(string1) < len(string2): string1 = string1.zfill(len(string2))
	elif len(string1) > len(string2): string2 = string2.zfill(len(string1))
	return string1, string2


def gcd(a: int, b: int) -> int:
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = extended_gcd(b % a, a)
		return (g, x - (b // a) * y, y)
