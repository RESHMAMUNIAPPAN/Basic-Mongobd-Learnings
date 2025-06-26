# 🗂️ Task Manager App

A full-stack **Task Manager** application built with:

- ⚙️ **Backend**: Python + FastAPI  
- 🌐 **Frontend**: React  
- 🗃️ **Database**: MongoDB (NoSQL)

## 🛠 How to Run the Task Manager Project

### ▶️ Backend (FastAPI)

📂 Path:  
D:\MACHINELEARNING\Mongodbproject\task-manager-app\backend


# 1. Activate the virtual environment
venv\Scripts\activate

# 2. Start FastAPI server with auto-reload
uvicorn app.main:app --reload

# 3. (Optional) Run backend script directly
python main.py

▶️ Frontend (React)
📂 Path:
D:\MACHINELEARNING\Mongodbproject\task-manager-app\frontend

# Start React development server
npm start

▶️ MongoDB Setup (Command Prompt)
Open Command Prompt and run:

mongosh
use taskdb
db.tasks.find().pretty()
