import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskUI(tk.Frame):
    def __init__(self, master, project_name, user_info, on_back):
        super().__init__(master)
        self.master = master
        self.project_name = project_name
        self.username = user_info["username"]
        self.role = user_info["role"]
        self.on_back = on_back
        self.tasks = []  # Replace with DB connection later
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="⬅ Back to Dashboard", command=self.on_back).pack(pady=5)

        tk.Label(self, text=f"Tasks for: {self.project_name}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(self, text="Mark as Complete", command=self.complete_task).pack(pady=5)

        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(fill="both", expand=True, padx=20)

        self.load_tasks()

    def load_tasks(self):
        self.tasks = [
            {"title": "Initial Setup", "status": "Pending"},
            {"title": "Wireframe Design", "status": "Complete"}
        ]
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status_icon = "✅" if task["status"] == "Complete" else "⏳"
            self.task_listbox.insert(tk.END, f"{status_icon} {task['title']}")

    def add_task(self):
        title = simpledialog.askstring("New Task", "Enter task title:")
        if title:
            self.tasks.append({"title": title, "status": "Pending"})
            self.load_tasks()
            messagebox.showinfo("Added", f"Task '{title}' added.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("No selection", "Select a task to mark complete.")
            return
        index = selected[0]
        self.tasks[index]["status"] = "Complete"
        self.load_tasks()
        messagebox.showinfo("Updated", "Task marked as complete.")
