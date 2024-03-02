encrypted_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encrypted_bytes = bytes.fromhex(encrypted_data)

for key in range(256):
    decrypted_bytes = bytes([byte ^ key for byte in encrypted_bytes])
    decrypted_text = decrypted_bytes.decode('utf-8', errors='ignore')
    if decrypted_text.isprintable() and 'crypto' in decrypted_text.lower():
        print("Key found:", key)
        print("Decrypted text:", decrypted_text)
        break
