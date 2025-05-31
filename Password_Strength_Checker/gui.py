import tkinter as tk
from tkinter import ttk
from password_utils import check_password_strength, generate_password, copy_password
from about_me import show_about_me

def toggle_password(entry, var):
    entry.config(show="" if var.get() else "*")

def create_app():
    root = tk.Tk()
    root.title("Advanced Password Strength Checker")
    root.geometry("420x400")
    root.configure(bg="#f0f4f7")

    tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f0f4f7").pack(pady=10)

    tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f0f4f7").pack()
    entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
    entry.pack(pady=5)

    show_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Show Password", variable=show_var,
                   command=lambda: toggle_password(entry, show_var), bg="#f0f4f7").pack()

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f7")
    result_label.pack()

    suggestion_label = tk.Label(root, text="", fg="red", bg="#f0f4f7", font=("Arial", 10))
    suggestion_label.pack()

    tk.Button(root, text="Check Strength", command=lambda: check_password_strength(entry, result_label, suggestion_label, progress),
              bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
    tk.Button(root, text="🔁 Generate Password", command=lambda: generate_password(entry),
              bg="#2196F3", fg="white", font=("Arial", 11, "bold")).pack(pady=5)
    tk.Button(root, text="📋 Copy to Clipboard", command=lambda: copy_password(entry),
              bg="#FF9800", fg="white", font=("Arial", 11, "bold")).pack(pady=5)
    tk.Button(root, text="ℹ️ About Me", command=show_about_me,
              bg="#9C27B0", fg="white", font=("Arial", 11, "bold")).pack(pady=5)

    return root
