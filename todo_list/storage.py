import json
import os
from i18n import I18n

class Storage:
    def __init__(self, path=None):
        if path is None:
            base_dir = os.path.join(os.path.dirname(__file__), "..", "settings")
            path = os.path.join(base_dir, "tasks.json")
        self.path = path
        self.data = self.load()
        self.next_id = self._get_next_id()

    def _get_next_id(self):
        tasks = self.data.get("tasks", [])
        if not tasks:
            return 1
        return max(task["id"] for task in tasks) + 1

    def load(self):
        if not os.path.exists(self.path):
            return {"tasks": []}
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def get_tasks(self):
        return self.data.get("tasks", [])

    def add_task(self, text):
        task = {"id": self.next_id, "text": text}
        self.next_id += 1
        self.data["tasks"].append(task)
        self.save()

    def remove_task(self, task_id):
        tasks = self.data["tasks"]
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                tasks.pop(i)
                self.save()
                return
        raise ValueError(I18n.t('storage_remove_task_error'))