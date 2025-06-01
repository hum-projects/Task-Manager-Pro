import tkinter as tk
from tkinter import messagebox, simpledialog
from task_ui import TaskUI

class Dashboard(tk.Frame):
    def __init__(self, master, username, role):
        super().__init__(master)
        self.master = master
        self.username = username
        self.role = role
        self.projects = []  # Placeholder for project list
        self.task_screen = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Welcome, {self.username} ({self.role})", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Create Project", command=self.create_project).pack(pady=5)
        tk.Button(self, text="Join Project", command=self.join_project).pack(pady=5)

        self.project_listbox = tk.Listbox(self)
        self.project_listbox.pack(fill="both", expand=True, padx=20, pady=10)
        self.project_listbox.bind("<Double-Button-1>", self.open_task_ui)

        self.load_projects()

    def load_projects(self):
        self.projects = ["Website Redesign", "Mobile App Launch"]
        self.project_listbox.delete(0, tk.END)
        for proj in self.projects:
            self.project_listbox.insert(tk.END, proj)

    def create_project(self):
        name = simpledialog.askstring("New Project", "Enter project name:")
        if name:
            self.projects.append(name)
            self.load_projects()
            messagebox.showinfo("Success", f"Project '{name}' created.")

    def join_project(self):
        messagebox.showinfo("Join", "Feature not implemented yet.")

    def open_task_ui(self, event):
        selection = self.project_listbox.curselection()
        if not selection:
            return
        project_name = self.project_listbox.get(selection[0])
        self.pack_forget()

        self.task_screen = TaskUI(
            self.master,
            project_name,
            {"username": self.username, "role": self.role},
            on_back=self.show_again
        )
        self.task_screen.pack(fill="both", expand=True)

    def show_again(self):
        if self.task_screen:
            self.task_screen.destroy()
            self.task_screen = None
        self.pack(fill="both", expand=True)