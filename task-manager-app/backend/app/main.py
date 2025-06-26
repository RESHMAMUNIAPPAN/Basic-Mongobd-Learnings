# app/main.py

from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager built with FastAPI and MongoDB",
    version="1.0.0"
)

# Allow frontend to access backend (e.g., React running on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all task routes
app.include_router(router)