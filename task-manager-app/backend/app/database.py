# app/database.py
from pymongo import MongoClient
import os

# Connect to MongoDB (local or cloud)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# Select the database and collection
db = client["taskdb"]
task_collection = db["tasks"]
