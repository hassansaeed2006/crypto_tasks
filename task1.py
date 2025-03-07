from itertools import permutations
import string

def decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    key_map = {k: v for k, v in zip(key, alphabet)}
    return ''.join(key_map.get(c, c) for c in ciphertext)

def brute_force_attack(ciphertext):
    alphabet = string.ascii_uppercase
    possible_keys = permutations(alphabet)
    
    results = []
    for key in possible_keys:
        decrypted_text = decrypt(ciphertext, key)
        results.append(decrypted_text)
    
    return results

encrypted_message = input("Enter the encrypted message: ")
possible_plaintexts = brute_force_attack(encrypted_message.upper())

for i, plaintext in enumerate(possible_plaintexts[:5]):
    print(f"Attempt {i+1}: {plaintext}")