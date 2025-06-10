from fastapi import FastAPI
import os
import json
import uuid
from datetime import datetime
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/store-json")
def store_json(data: dict):
    """Store JSON data to a file in the current directory"""
    # Generate a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}_{str(uuid.uuid4())[:8]}.json"
    filepath = os.path.join("./data", filename)
    
    # Write JSON data to file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    
    return {"message": f"JSON stored successfully", "filename": filename}

@app.get("/get-jsons")
def get_all_jsons() -> List[str]:
    """Return all JSON files in current directory as a list of strings"""
    json_files = []
    
    # Get all .json files in current directory
    for filename in os.listdir("."):
        if filename.endswith(".json"):
            filepath = os.path.join(".", filename)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    json_files.append(content)
            except Exception as e:
                # Skip files that can't be read
                continue
    
    return json_files