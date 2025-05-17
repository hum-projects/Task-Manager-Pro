# Login and registration UI
#2
import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Login to CollabManager Pro", font=("Arial", 16)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*") 
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Placeholder for backend call
        if username == "admin" and password == "admin":
            self.destroy()
            dashboard = Dashboard(self.master, username)
            dashboard.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        messagebox.showinfo("Register", "Redirecting to registration...")
        # Could open a registration screen here