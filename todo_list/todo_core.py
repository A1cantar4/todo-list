# Functions to import in terminal and tkinter (two versions of todo-list)

def add_task(tasks, task):
    task = task.strip()
    if not task:
        raise ValueError("A tarefa não pode ser vazia!")
    tasks.append(task)
    return tasks

def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise IndexError("Índice invalido!")
    tasks.pop(index)
    return tasks