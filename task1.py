from itertools import permutations
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

def decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    key_map = {k: v for k, v in zip(key, alphabet)}
    return ''.join(key_map.get(c, c) for c in ciphertext)

def brute_force_attack(ciphertext, update_callback, stop_event):
    alphabet = string.ascii_uppercase
    possible_keys = permutations(alphabet)
    
    for attempt, key in enumerate(possible_keys, start=1):
        if stop_event.is_set():
            break
        decrypted_text = decrypt(ciphertext, key)
        update_callback(attempt, decrypted_text)

def execute_brute_force():
    ciphertext = message_entry.get()
    if not ciphertext:
        messagebox.showerror("Error", "Please enter an encrypted message.")
        return
    
    result_text.delete(1.0, tk.END)
    global stop_event
    stop_event.clear()
    
    def update_callback(attempt, decrypted_text):
        result_text.insert(tk.END, f"Attempt {attempt}: {decrypted_text}\n")
        result_text.see(tk.END)
    
    threading.Thread(target=brute_force_attack, args=(ciphertext.upper(), update_callback, stop_event), daemon=True).start()

def stop_brute_force():
    global stop_event
    stop_event.set()

# GUI Setup
root = tk.Tk()
root.title("Brute Force Attack")
root.geometry("600x500")
root.configure(bg="#2c3e50")

stop_event = threading.Event()

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

tk.Label(frame, text="Encrypted Message:", bg="#2c3e50", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
message_entry = tk.Entry(frame, font=("Arial", 12), width=30)
message_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Start Brute Force", command=execute_brute_force, bg="#e74c3c", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=1, column=0, pady=10)
tk.Button(frame, text="Stop", command=stop_brute_force, bg="#3498db", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=1, column=1, pady=10)

result_text = scrolledtext.ScrolledText(root, height=15, width=70, font=("Arial", 10))
result_text.pack(pady=10)

root.mainloop()
