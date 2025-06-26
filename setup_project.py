import os

folders = [
    "task-manager-app/backend/app",
    "task-manager-app/frontend/public",
    "task-manager-app/frontend/src/components"
]

files = {
    "task-manager-app/backend/app/__init__.py": "",
    "task-manager-app/backend/app/main.py": "",
    "task-manager-app/backend/app/database.py": "",
    "task-manager-app/backend/app/models.py": "",
    "task-manager-app/backend/app/routes.py": "",
    "task-manager-app/backend/requirements.txt": "",
    "task-manager-app/backend/README.md": "",
    "task-manager-app/frontend/public/index.html": "",
    "task-manager-app/frontend/src/components/TaskForm.js": "",
    "task-manager-app/frontend/src/components/TaskList.js": "",
    "task-manager-app/frontend/src/App.js": "",
    "task-manager-app/frontend/src/index.js": "",
    "task-manager-app/frontend/package.json": "",
    "task-manager-app/frontend/README.md": "",
    "task-manager-app/README.md": "# Task Manager App (FastAPI + MongoDB + React)"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully!")