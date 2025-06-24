import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_tool import encrypt_file, decrypt_file

def select_file():
    path = filedialog.askopenfilename()
    if path:
        file_path.set(path)

def encrypt_action():
    try:
        output_path = encrypt_file(file_path.get(), password.get())
        messagebox.showinfo("Success", f"File encrypted:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_action():
    try:
        output_path = decrypt_file(file_path.get(), password.get())
        messagebox.showinfo("Success", f"File decrypted:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("AES-256 Encryption Tool")
root.geometry("400x250")
root.resizable(False, False)

file_path = tk.StringVar()
password = tk.StringVar()

tk.Label(root, text="Select File to Encrypt/Decrypt:").pack(pady=5)
tk.Entry(root, textvariable=file_path, width=40).pack(padx=10)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)

tk.Label(root, text="Enter Password:").pack(pady=5)
tk.Entry(root, textvariable=password, show="*", width=30).pack()

tk.Button(root, text="Encrypt", command=encrypt_action, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Decrypt", command=decrypt_action, bg="blue", fg="white").pack()

root.mainloop()
