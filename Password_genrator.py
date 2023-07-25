import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()

    if length.isdigit():
        length = int(length)
        if length > 0:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            password_entry.delete(0, tk.END)
            password_entry.insert(tk.END, password)
        else:
            messagebox.showwarning("Invalid Length", "Please enter a positive number for password length.")
    else:
        messagebox.showwarning("Invalid Length", "Please enter a valid number for password length.")

root = tk.Tk()
root.title("Password Generator")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, width=30)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

root.mainloop()
