# app/routes.py
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.database import task_collection
from app.models import Task

router = APIRouter()

# 🔁 Helper to convert MongoDB _id to string
def task_serializer(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task.get("description", ""),
        "completed": task["completed"]
    }

@router.post("/tasks", summary="Create a new task")
def create_task(task: Task):
    result = task_collection.insert_one(task.dict())
    return {"id": str(result.inserted_id), "message": "Task created"}

@router.get("/tasks", summary="Get all tasks")
def get_tasks():
    tasks = [task_serializer(task) for task in task_collection.find()]
    return tasks

@router.get("/tasks/{task_id}", summary="Get task by ID")
def get_task(task_id: str):
    task = task_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_serializer(task)

@router.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: str, task: Task):
    result = task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated"}

@router.delete("/tasks/{task_id}", summary="Delete a task")
def delete_task(task_id: str):
    result = task_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
