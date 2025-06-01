# Project/task dashboard for users
#2
import tkinter as tk
from tkinter import messagebox, simpledialog
from task_ui import TaskUI
from task_ui import TaskUI


class Dashboard(tk.Frame):
    def __init__(self, master, username, role):
        super().__init__(master)
        self.master = master
        self.username = username
        self.role = role
        self.projects = []  # Placeholder for project list
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Welcome, {self.username} ({self.role})", font=("Arial", 14)).pack(pady=10)

        # Buttons for project actions
        tk.Button(self, text="Create Project", command=self.create_project).pack(pady=5)
        tk.Button(self, text="Join Project", command=self.join_project).pack(pady=5)

        # Project list label
        tk.Label(self, text="Your Projects:", font=("Arial", 12)).pack(pady=10)

        self.project_listbox = tk.Listbox(self)
        self.project_listbox.pack(fill="both", expand=True, padx=20)

        # Load mock data
        self.load_projects()
        # View/manage tasks for a project
        self.project_listbox.bind("<Double-Button-1>", self.open_task_ui)

    def load_projects(self):
        # Placeholder: should load from backend
        self.projects = ["Project Alpha", "Team Rocket", "DevOps Sprint"]
        self.project_listbox.delete(0, tk.END)
        for project in self.projects:
            self.project_listbox.insert(tk.END, project)

    def create_project(self):
        project_name = simpledialog.askstring("New Project", "Enter project name:")
        if project_name:
            # Placeholder: send to backend to create
            self.projects.append(project_name)
            self.project_listbox.insert(tk.END, project_name)
            messagebox.showinfo("Success", f"Project '{project_name}' created.")

    def join_project(self):
        project_code = simpledialog.askstring("Join Project", "Enter project code:")
        if project_code:
            # Placeholder: verify and join via backend
            messagebox.showinfo("Joined", f"Joined project with code: {project_code}")

    def open_task_ui(self, event):
        selection = self.project_listbox.curselection()
        if not selection:
            return
        project_name = self.project_listbox.get(selection[0])
        self.destroy()
        task_screen = TaskUI(self.master, project_name, {"username": self.username, "role": self.role})
        task_screen.pack(fill="both", expand=True)