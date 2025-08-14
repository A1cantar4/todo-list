import tkinter as tk
from tkinter import messagebox
from todo_core import add_task as core_add_task, remove_task as core_remove_task

# CREATE A TK WINDOW
window = tk.Tk()
window.title("Lista de Tarefas")
window.geometry("400x400")

# TASK LIST
tasks = []

# ADD TASKS ON LIST
def add_task():
    text = entry_task.get().strip()
    if text:
        core_add_task(tasks, text) # New add task
        refresh_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Necessita digitar uma tarefa!") # WHEN SOMETHING IS TYPED WRONG

# REMOVE TASKS, BUT YOU NEED TO SELECT A TASK FIRST
def remove_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        try: 
            core_remove_task(tasks, index) # New remove
            refresh_list()
        except IndexError:
            messagebox.showerror("Erro", "Índice inválido")
    else:
        messagebox.showinfo("Remover", "Selecione uma tarefa para remover por gentileza!")

# REFRESH TASK LIST AND SHOW ALL TASKS ADDED
def refresh_list():
    task_list.delete(0, tk.END) # It serves to visually CLEAN the list
    for task in tasks:
        task_list.insert(tk.END, task)
        
# WIDGETS
entry_task = tk.Entry(window, font=("Arial", 14))
entry_task.pack(pady=10, padx=10, fill="x")

add_button = tk.Button(window, text="Adicionar Tarefa", command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(window, font=("Arial", 12), height=10)
task_list.pack(pady=10, padx=10, fill="both", expand=True)

remove_button = tk.Button(window, text="Remover Selecionada", command=remove_task)
remove_button.pack(pady=5)

__version__ = "1.2.0"

# START THE INTERFACE
window.mainloop()