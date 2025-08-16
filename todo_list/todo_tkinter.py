import tkinter as tk
from tkinter import messagebox
from todo_core import add_task as core_add_task
from i18n import I18n
from storage import Storage

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "settings"))
from settings import Settings

settings = Settings()

# LANGUAGE SELECTION WINDOW
def choose_language():
    base_path = os.path.join(os.path.dirname(__file__), "..", "settings", "locales")
    files = [f[:-5] for f in os.listdir(base_path) if f.endswith(".json")]

    lang_window = tk.Toplevel(window)
    lang_window.title("Select Language")

    tk.Label(lang_window, text="Escolha o idioma / Choose your language").pack(pady=10)

    selected_lang = tk.StringVar(lang_window)
    selected_lang.set(settings.get("language", files[0]))

    tk.OptionMenu(lang_window, selected_lang, *files).pack(pady=5)

    def confirm():
        settings.set("language", selected_lang.get())
        lang_window.destroy()

    tk.Button(lang_window, text="OK", command=confirm).pack(pady=10)

    # Wait until the selection window be closed
    lang_window.grab_set()
    window.wait_window(lang_window)

    return settings.get("language")

# UPDATE UI TEXTS
def update_texts():
    window.title(i18n.t("tk_window_title"))
    add_button.config(text=i18n.t("tk_add_button"))
    remove_button.config(text=i18n.t("tk_remove_button"))
    lang_button.config(text=i18n.t("tk_change_lang"))

# TASK MANAGEMENT
def add_task():
    text = entry_task.get().strip()
    if text:
        core_add_task([], text)
        storage.add_task(text) 
        refresh_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning(i18n.t("tk_warning_title"), i18n.t("tk_warning_empty"))

def remove_task():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        task_id = tasks[index]["id"]
        try:
            storage.remove_task(task_id)
            refresh_list()
        except ValueError:
            messagebox.showerror(i18n.t("tk_error_title"), i18n.t("tk_remove_task_error"))
    else:
        messagebox.showinfo(i18n.t("tk_info_title"), i18n.t("tk_info_select_remove"))

def refresh_list():
    global tasks
    tasks = storage.get_tasks()
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, f"{task['text']} (ID: {task['id']})")

# LANGUAGE SWITCH
def change_language():
    lang_choice = choose_language()
    global i18n
    i18n = I18n(lang_choice)
    update_texts()
    refresh_list()

# MAIN WINDOW
window = tk.Tk()
window.geometry("400x400")

# If not have language saved, ask
if not settings.get("language"):
    lang_choice = choose_language()
else:
    lang_choice = settings.get("language")

i18n = I18n(lang_choice)
storage = Storage()
tasks = storage.get_tasks()

# WIDGETS
entry_task = tk.Entry(window, font=("Arial", 14))
entry_task.pack(pady=10, padx=10, fill="x")

add_button = tk.Button(window, text=i18n.t("tk_add_button"), command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(window, font=("Arial", 12), height=10)
task_list.pack(pady=10, padx=10, fill="both", expand=True)

remove_button = tk.Button(window, text=i18n.t("tk_remove_button"), command=remove_task)
remove_button.pack(pady=5)

lang_button = tk.Button(window, text=i18n.t("tk_change_lang"), command=change_language)
lang_button.pack(pady=5)

# VERSION
__version__ = "2.0.1"

# START
update_texts()
refresh_list()
window.mainloop()