# Login and registration UI
#2
import tkinter as tk
from tkinter import messagebox
import sqlite3
from dashboard import Dashboard

# Ensure the database and table exist
def init_db():
    conn = sqlite3.connect("collabmanager.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        init_db()  # Setup DB on start
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

        conn = sqlite3.connect("collabmanager.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, role FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            username, role = user
            self.destroy()
            dashboard = Dashboard(self.master, username, role)
            dashboard.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        reg_window = tk.Toplevel(self.master)
        reg_window.title("Register Account")
        reg_window.geometry("300x220")

        tk.Label(reg_window, text="Username").pack(pady=5)
        username_entry = tk.Entry(reg_window)
        username_entry.pack()

        tk.Label(reg_window, text="Password").pack(pady=5)
        password_entry = tk.Entry(reg_window, show="*")
        password_entry.pack()

        tk.Label(reg_window, text="Role (admin/manager/member)").pack(pady=5)
        role_entry = tk.Entry(reg_window)
        role_entry.pack()

        def submit_registration():
            username = username_entry.get()
            password = password_entry.get()
            role = role_entry.get().lower()

            if not (username and password and role in ['admin', 'manager', 'member']):
                messagebox.showerror("Error", "Please fill all fields correctly.")
                return

            try:
                conn = sqlite3.connect("collabmanager.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"User '{username}' registered.")
                reg_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists.")

        tk.Button(reg_window, text="Submit", command=submit_registration).pack(pady=10)