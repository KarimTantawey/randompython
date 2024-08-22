import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    characters = ''
    length = length_var.get()
    if useCapital_var.get():
        characters += string.ascii_uppercase
    if useLower_var.get():
        characters += string.ascii_lowercase
    if useDigits_var.get():
        characters += string.digits
    if useSymbols_var.get():
        characters += string.punctuation
    
    if characters: 
        password = ''.join(random.choice(characters) for i in range(length))
        password_var.set(password)
    else:
        password_var.set("Please select at least one option")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500")
root.configure(bg='#2b2b2b')

length_var = tk.IntVar(value=12)
useCapital_var = tk.BooleanVar(value=True)
useLower_var = tk.BooleanVar(value=True)
useDigits_var = tk.BooleanVar(value=True)
useSymbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

title_label = tk.Label(root, text="Password Generator", bg='#2b2b2b', fg='#ffffff', font=("Helvetica", 16))
length_label = tk.Label(root, text="Password Length:", bg='#2b2b2b', fg='#ffffff')
length_entry = tk.Entry(root, textvariable=length_var)

useCapital_check = tk.Checkbutton(root, text="Include Uppercase", bg='#2b2b2b', fg='#ffffff', selectcolor='#3c3f41', variable=useCapital_var)
useLower_check = tk.Checkbutton(root, text="Include Lowercase", bg='#2b2b2b', fg='#ffffff', selectcolor='#3c3f41', variable=useLower_var)
useDigits_check = tk.Checkbutton(root, text="Include Numbers", bg='#2b2b2b', fg='#ffffff', selectcolor='#3c3f41', variable=useDigits_var)
useSymbols_check = tk.Checkbutton(root, text="Include Symbols", bg='#2b2b2b', fg='#ffffff', selectcolor='#3c3f41', variable=useSymbols_var)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#3c3f41', fg='#ffffff')
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='#3c3f41', fg='#ffffff')

password_label = tk.Label(root, textvariable=password_var, bg='#2b2b2b', fg='#ffffff', font=("Helvetica", 12))


title_label.pack(pady=10)
length_label.pack(pady=5)
length_entry.pack(pady=5)
useCapital_check.pack(pady=5)
useLower_check.pack(pady=5)
useDigits_check.pack(pady=5)
useSymbols_check.pack(pady=5)
generate_button.pack(pady=10)
copy_button.pack(pady=5)
password_label.pack(pady=10)


root.mainloop()
