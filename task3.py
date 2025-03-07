import string

def generate_playfair_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []
    
    for char in keyword + string.ascii_uppercase:
        if char not in seen and char != "J":
            seen.add(char)
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    raise ValueError(f"Letter {letter} not found in Playfair matrix")

def process_digraphs(text):
    text = ''.join(filter(str.isalpha, text.upper())).replace("J", "I")
    processed = ""
    i = 0
    
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        
        if a == b:
            processed += a + "X"
            i += 1
        else:
            processed += a + b
            i += 2
    
    if len(processed) % 2 == 1:
        processed += "X"
    
    return processed

def playfair_encrypt(plaintext, matrix):
    plaintext = process_digraphs(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a+1) % 5] + matrix[row_b][(col_b+1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a+1) % 5][col_a] + matrix[(row_b+1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            plaintext += matrix[row_a][(col_a-1) % 5] + matrix[row_b][(col_b-1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a-1) % 5][col_a] + matrix[(row_b-1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return plaintext

keyword = input("Enter the keyword: ")
playfair_matrix = generate_playfair_matrix(keyword)
print("\nPlayfair Matrix:")
for row in playfair_matrix:
    print(" ".join(row))

choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
message = input("Enter the message: ")

if choice == 'e':
    result = playfair_encrypt(message, playfair_matrix)
    print("\nEncrypted Text:", result)
elif choice == 'd':
    result = playfair_decrypt(message, playfair_matrix)
    print("\nDecrypted Text:", result)
else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
