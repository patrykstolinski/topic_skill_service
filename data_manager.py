import os
import json

class JsonDataManager:

    def __init__(self, baseDir = None):
        self.baseDir = baseDir or os.path.dirname(__file__)

    
    def read_data(self, fileName):
        try: 
            filePath = os.path.join(self.baseDir, fileName)
            with open(filePath, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] File not found: {fileName}")
            return []
        except json.JSONDecodeError:
            print(f"[ERROR] File {fileName} contains invalid JSON.")
            return []

    def write_data(self, fileName, data):
        try:
            filePath = os.path.join(self.baseDir, fileName)
            with open(filePath, "w", encoding = "utf-8") as f:
                json.dump(data, f, indent = 2)
                print(f"[INFO] Successfully wrote to {fileName}")
                return True

        except TypeError:
            print(f"[ERROR] Data {data} is not JSON compatible.")
            return False
        