import json
import os

class Settings:
    def __init__(self, path=None):
        if path is None:
            base_dir = os.path.dirname(__file__)
            path = os.path.join(base_dir, "settings.json")
        self.path = path
        self.data = self.load_settings()
        
    def load_settings(self):
        if not os.path.exists(self.path):
            return {"language": "pt"}
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_settings(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            
    def get(self, key, default=None):
        return self.data.get(key, default)
    
    def set(self, key, value):
        self.data[key] = value
        self.save_settings()