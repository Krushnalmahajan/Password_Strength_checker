from gui import create_app

if __name__ == "__main__":
    app = create_app()
    app.mainloop()   # This line runs the Tkinter window



import tkinter as tk
import styles

root = tk.Tk()
root.title("Example")
root.geometry("300x200")
root.configure(bg=styles.BG_COLOR)

label = tk.Label(root, text="Hello!", font=styles.TITLE_FONT, bg=styles.BG_COLOR)
label.pack(pady=20)

button = tk.Button(root, text="Click me", bg=styles.BUTTON_BG_GREEN, fg=styles.BUTTON_FG)
button.pack()

root.mainloop()
