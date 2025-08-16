from todo_core import add_task as core_add_task, remove_task as core_remove_task
from i18n import I18n
from storage import Storage

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "settings"))
from settings import Settings

settings = Settings()

# Function to select the language
def choose_language():
    base_path = os.path.join(os.path.dirname(__file__), "..", "settings", "locales")
    files = [f[:-5] for f in os.listdir(base_path) if f.endswith(".json")]

    print("\nEscolha o idioma / Choose your language:")
    for i, lang in enumerate(files, start=1):
        print(f"{i}. {lang}")

    while True:
        choice = input("\nDigite o número / Enter number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(files):
                selected_lang = files[idx - 1]
                settings.set("language", selected_lang)
                return selected_lang
        print("Opção inválida, tente novamente. / Invalid option, please try again.")

# Ask for the language if it is not already saved
if not settings.get("language"):
    lang_choice = choose_language()
else:
    lang_choice = settings.get("language")

i18n = I18n(lang_choice)
storage = Storage()
todo_list = storage.get_tasks()

# Display the main menu
def show_menu():
    print(f"\n{i18n.t('menu_title')}")
    print(i18n.t("menu_add"))
    print(i18n.t("menu_list"))
    print(i18n.t("menu_remove"))
    print(i18n.t("menu_change_lang")) # New option
    print(i18n.t("menu_exit"))

# Add a new task to the list
def add_task():
    task = input(f"\n{i18n.t('prompt_task')} ").strip()
    if task:
        core_add_task([], task) # New add
        storage.add_task(task)
        print(f"\n{i18n.t('task_added')}")
    else:
        print(f"\n{i18n.t('task_empty')}")

# Show the current list of tasks
def list_tasks():
    todo_list[:] = storage.get_tasks()
    if not todo_list:
        print(f"\n{i18n.t('no_tasks')}")
    else:
        print(f"\n{i18n.t('list_tasks')}")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task['text']} (ID: {task['id']})")

# Remove a task by its number
def remove_task():
    list_tasks()
    if not todo_list:
        return
    try:
        task_number = int(input(f"\n{i18n.t('remove_prompt')} "))
        if 1 <= task_number <= len(todo_list):
            task_id = todo_list[task_number - 1]["id"]
            storage.remove_task(task_id)
            print(f"\n{i18n.t('remove_success')}")
        else:
            print(f"\n{i18n.t('remove_invalid')}")
    except ValueError:
        print(f"\n{i18n.t('remove_not_number')}")

# New function: Define the language during the loop
def change_language():
    global i18n
    lang_choice = choose_language()
    i18n = I18n(lang_choice)
    print(f"\n{i18n.t('language_changed')}")


# Version
__version__ = "2.0.1"

# Main loop to keep the program running
while True:
    show_menu()
    choice = input(f"\n{i18n.t('choice')}").strip()

    if not choice:
        print(f"\n{i18n.t('input_empty')}")
        continue

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        change_language()
    elif choice == "5":
        print(f"\n{i18n.t('bye')}")
        break
    else:
        print(f"\n{i18n.t('invalid_option')}")