import os
import json

MEMORY_DIR = "user_memory"

os.makedirs(MEMORY_DIR, exist_ok=True)

def save_memory(user_id: str, memory_data: dict):
    filepath = os.path.join(MEMORY_DIR, f"{user_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory_data, f, ensure_ascii=False, indent=2)

def load_memory(user_id: str) -> dict:
    filepath = os.path.join(MEMORY_DIR, f"{user_id}.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
