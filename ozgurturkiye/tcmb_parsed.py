import json
import os


def get_json_file():
    file_path = "kur/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return False
