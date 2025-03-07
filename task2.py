import string
from collections import Counter
import tkinter as tk
from tkinter import messagebox

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

def execute_analysis():
    ciphertext = message_entry.get()
    if not ciphertext:
        messagebox.showerror("Error", "Please enter an encrypted message.")
        return
    
    decrypted_text, mapping = frequency_analysis(ciphertext)
    result_label.config(text=f"Decrypted Text: {decrypted_text}")
    mapping_text.set("\n".join([f"{cipher} -> {plain}" for cipher, plain in mapping.items()]))

# GUI Setup
root = tk.Tk()
root.title("Frequency Analysis")
root.geometry("400x350")
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

tk.Label(frame, text="Encrypted Message:", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
message_entry = tk.Entry(frame, font=("Arial", 12), width=30)
message_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Analyze", command=execute_analysis, bg="#27ae60", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=1, columnspan=2, pady=10)

result_label = tk.Label(root, text="Decrypted Text:", bg="#2c3e50", fg="white", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

mapping_text = tk.StringVar()
mapping_label = tk.Label(root, textvariable=mapping_text, bg="#2c3e50", fg="white", font=("Arial", 10))
mapping_label.pack(pady=10)

root.mainloop()
