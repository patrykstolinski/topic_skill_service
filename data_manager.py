import os
import json
 
class JsonDataManager:

    # Handles reading from and writing to JSON files in a specified directory.
    def __init__(self, baseDir = None):
        # Use the provided base directory or default to the directory of this file
        self.baseDir = baseDir or os.path.dirname(__file__)
    
    def read_data(self, filepath):
        
        if not os.path.exists(filepath):
            return []
        # Reads JSON data from a file. Returns parsed data if successful, or an empty list on error.
        try: 
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] File not found: {filepath}")
            return []
        except json.JSONDecodeError:
            print(f"[ERROR] File {filepath} contains invalid JSON.")
            return []


    def write_data(self, filepath, data):        
        # Writes JSON data to a file. Returns True if successful, False if data is not serializable.
        # check if directory exists, if yes, go ahead
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            with open(filepath, "w", encoding = "utf-8") as f:
                json.dump(data, f, indent = 4)
                print(f"[INFO] Successfully wrote to {filepath}")
                return True
        except TypeError:
            print(f"[ERROR] Data {data} is not JSON compatible.")
            return False
        