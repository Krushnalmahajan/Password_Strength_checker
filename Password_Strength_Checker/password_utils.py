import random
import string
import pyperclip

def check_password_strength(entry, result_label, suggestion_label, progress):
    password = entry.get()
    length = len(password)
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(c in string.punctuation for c in password)

    score = sum([lower, upper, digit, symbol])
    
    if length >= 12 and score == 4:
        result = "Strong"
        suggestion = ""
        progress["value"] = 100
        progress.configure(style="green.Horizontal.TProgressbar")
    elif length >= 8 and score >= 3:
        result = "Moderate"
        suggestion = "Try adding more variety and length."
        progress["value"] = 60
        progress.configure(style="yellow.Horizontal.TProgressbar")
    else:
        result = "Weak"
        suggestion = "Add uppercase, symbols, numbers, and increase length."
        progress["value"] = 30
        progress.configure(style="red.Horizontal.TProgressbar")

    result_label.config(text=f"Strength: {result}")
    suggestion_label.config(text=suggestion)

def generate_password(entry):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(16))
    entry.delete(0, 'end')
    entry.insert(0, password)

def copy_password(entry):
    pyperclip.copy(entry.get())
