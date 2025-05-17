# UI for assigning/updating tasks
#2
import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskUI(tk.Frame):
    def __init__(self, master, project_name):
        super().__init__(master)
        self.master = master
        self.project_name = project_name
        self.tasks = []  # Placeholder for backend tasks
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"Tasks for: {self.project_name}", font=("Arial", 14)).pack(pady=10)

        # Buttons
        tk.Button(self, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(self, text="Mark as Complete", command=self.complete_task).pack(pady=5)

        # Task list
        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(fill="both", expand=True, padx=20)

        self.load_tasks()

    def load_tasks(self):
        # Placeholder: fetch from backend
        self.tasks = [
            {"title": "Design UI", "status": "Pending"},
            {"title": "Set up DB", "status": "Complete"},
        ]
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["status"] == "Complete" else "⏳"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        title = simpledialog.askstring("New Task", "Enter task title:")
        if title:
            # Placeholder: save to backend
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