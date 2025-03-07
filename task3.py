import string
import tkinter as tk
from tkinter import messagebox

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

def execute_cipher():
    keyword = keyword_entry.get()
    message = message_entry.get()
    choice = choice_var.get()
    
    if not keyword or not message:
        messagebox.showerror("Error", "Please enter both keyword and message.")
        return
    
    playfair_matrix = generate_playfair_matrix(keyword)
    
    if choice == "encrypt":
        result = playfair_encrypt(message, playfair_matrix)
    else:
        result = playfair_decrypt(message, playfair_matrix)
    
    result_label.config(text=f"Result: {result}")

# GUI Setup
root = tk.Tk()
root.title("Playfair Cipher")
root.geometry("400x300")
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

tk.Label(frame, text="Keyword:", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
keyword_entry = tk.Entry(frame, font=("Arial", 12))
keyword_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Message:", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
message_entry = tk.Entry(frame, font=("Arial", 12))
message_entry.grid(row=1, column=1, padx=5, pady=5)

choice_var = tk.StringVar(value="encrypt")
tk.Radiobutton(frame, text="Encrypt", variable=choice_var, value="encrypt", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=5)
tk.Radiobutton(frame, text="Decrypt", variable=choice_var, value="decrypt", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=2, column=1, pady=5)

tk.Button(frame, text="Execute", command=execute_cipher, bg="#27ae60", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:", bg="#2c3e50", fg="white", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
