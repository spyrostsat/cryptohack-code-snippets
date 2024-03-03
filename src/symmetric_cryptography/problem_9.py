import requests
from Crypto.Cipher import AES
import hashlib


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


def main():
	res = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words")
	words = res.text.split("\n")
	ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

	for word in words:
		key = hashlib.md5(word.encode()).digest().hex()
		plaintext = decrypt(ciphertext, key)

		if "error" not in plaintext:
			password = word
			possible_plaintext = plaintext['plaintext']
			try:
				possible_plaintext = bytes.fromhex(possible_plaintext).decode("utf-8")
				if "crypto" in possible_plaintext:
					print("Plaintext contains the word 'crypto'")
					print(f"Password: {password}")
					print(f"Plaintext: {possible_plaintext}")
					break
			except:
				continue
			


if __name__ == "__main__":
    main()
