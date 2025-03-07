import string
from collections import Counter

def frequency_analysis(ciphertext):
    letter_frequencies = {
        'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3, 'H': 6.1,
        'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2,
        'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0, 'K': 0.8, 'J': 0.2, 'X': 0.2,
        'Q': 0.1, 'Z': 0.1
    }
    
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    cipher_counts = Counter(ciphertext)
    sorted_cipher_letters = [pair[0] for pair in cipher_counts.most_common()]
    sorted_english_letters = sorted(letter_frequencies, key=letter_frequencies.get, reverse=True)
    
    decryption_map = {cipher: plain for cipher, plain in zip(sorted_cipher_letters, sorted_english_letters)}
    decrypted_text = ''.join(decryption_map.get(c, c) for c in ciphertext)
    
    return decrypted_text, decryption_map


encrypted_message = input("Enter the encrypted message: ")
decrypted_text, mapping = frequency_analysis(encrypted_message)


print("\nMost likely decrypted text:")
print(decrypted_text)

print("\nSubstitution mapping:")
for cipher, plain in mapping.items():
    print(f"{cipher} -> {plain}")
