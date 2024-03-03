from typing import Tuple, List
from src.const import *


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


def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def bytes2matrix(text: bytes) -> List[List[int]]:
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix: List[List[int]]) -> bytes:
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))


def add_round_key(state: List[List[int]], round_key: List[List[int]]) -> List[List[int]]:
    """ Adds (XORs) the round key to the state. """
    return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]


def sub_bytes(state: List[List[int]], s_box: List[int]) -> List[List[int]]:
    """ Substitutes the values in the state with the values in the SBox using the state value as index. """
    return [[s_box[state[i][j]] for j in range(4)] for i in range(4)]


def shift_rows(s: List[List[int]]) -> None:
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s: List[List[int]]) -> None:
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

 
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

 
def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)


def expand_key(master_key: bytes, N_ROUNDS: int) -> List[List[List[int]]]:
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]


def decrypt(key: bytes, ciphertext: bytes, N_ROUNDS: int) -> bytes:
    round_keys = expand_key(key, N_ROUNDS) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix
    state = bytes2matrix(ciphertext)

    # Initial add round key step
    state = add_round_key(state, round_keys[-1])
        
    for i in range(N_ROUNDS - 1, 0, -1):
        inv_shift_rows(state)
        state = sub_bytes(state, inv_s_box)
        state = add_round_key(state, round_keys[i])
        inv_mix_columns(state)

    # Run final round (skips the InvMixColumns step)
    inv_shift_rows(state)
    state = sub_bytes(state, inv_s_box)
    state = add_round_key(state, round_keys[0])

    # Convert state matrix to plaintext
    return matrix2bytes(state)
