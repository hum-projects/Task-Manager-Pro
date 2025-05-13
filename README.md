# Task-Manager-Pro
✅ Project Split Overview
1. Backend Module (Core Logic & Data)
Handles:

User authentication and roles

Project and task data management

SQLite database operations

Business logic (e.g., permission checks, data validation)

Key Technologies:

Python

SQLite (sqlite3)

Organized into classes/modules (e.g., UserManager, ProjectManager, TaskManager)

Suggested Structure:

bash
Copy
Edit
/backend
  ├── db.py               # DB connection and setup
  ├── models.py           # User, Project, Task classes
  ├── auth.py             # Login, registration, role-based access
  ├── manager.py          # Core logic for task/project operations


  
2. Frontend Module (GUI Interface)
Handles:

GUI layout and event handling

Input validation before passing to backend

Display of projects, tasks, and reports

Key Technologies:

Python

tkinter (built-in GUI library)

Optionally: ttkbootstrap or PyQt5/PySide6 for advanced UI

Suggested Structure:

bash
Copy
Edit
/frontend
  ├── main.py             # Launch GUI
  ├── login_screen.py     # Login and registration UI
  ├── dashboard.py        # Project/task dashboard for users
  ├── task_ui.py          # UI for assigning/updating tasks
  ├── report_ui.py        # Exporting to CSV
🔗 How They Communicate
The frontend will import functions and classes from the backend to:

Authenticate users

Create/join projects

Assign tasks

Generate and export reports

