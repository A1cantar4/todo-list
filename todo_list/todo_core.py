from i18n import I18n

# Functions to import in terminal and tkinter (two versions of todo-list)
def add_task(tasks, task):
    task = task.strip()
    if not task:
        raise ValueError(I18n.t("core_task_empty"))
    tasks.append(task)
    return tasks

def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise IndexError(I18n.t("core_error_index"))
    tasks.pop(index)
    return tasks