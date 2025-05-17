# Launch GUI
#2
import tkinter as tk
from login_screen import LoginScreen

def main():
    root = tk.Tk()
    root.title("CollabManager Pro")
    root.geometry("600x400")

    app = LoginScreen(root)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()