from tkinter import ttk, messagebox
import tkinter as tk
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.usernames import add_username

def get_character_name(parent, character_type, color):
    dialog = tk.Toplevel(parent)
    dialog.title(f"Nom del {character_type}")
    dialog.geometry("400x200")
    dialog.configure(bg="#f5f5f5")
    dialog.transient(parent)
    dialog.grab_set()

    dialog.update_idletasks()
    width = dialog.winfo_width()
    height = dialog.winfo_height()
    x = (dialog.winfo_screenwidth() // 2) - (width // 2)
    y = (dialog.winfo_screenheight() // 2) - (height // 2)
    dialog.geometry(f'{width}x{height}+{x}+{y}')

    tk.Label(dialog, text=f"Introdueix el nom del teu {character_type}:", 
             font=("Arial", 14), bg="#f5f5f5", fg="#333").pack(pady=(20, 10))

    name_var = tk.StringVar()
    ttk.Entry(dialog, textvariable=name_var, font=("Arial", 12), width=30).pack(pady=10)

    def on_ok():
        name = name_var.get().strip()
        if name:
            add_username(name)
            dialog.destroy()
        else:
            messagebox.showwarning("Nom buit", "Si us plau, introdueix un nom per al teu personatge.")

    button_frame = tk.Frame(dialog, bg="#f5f5f5")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Acceptar", command=on_ok, bg=color, fg="white", 
            font=("Arial", 12), padx=10, pady=5).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Cancel·lar", command=dialog.destroy, bg="#999999", fg="white", 
            font=("Arial", 12), padx=10, pady=5).pack(side=tk.LEFT, padx=5, )

    dialog.bind("<Return>", lambda e: on_ok())
    dialog.bind("<Escape>", dialog.destroy)

    dialog.wait_window()
    return name_var.get().strip()