from todo_core import add_task as core_add_task, remove_task as core_remove_task

todo_list = []

# Display the main menu
def show_menu():
    print("\n¨¨¨¨ MENU PRINCIPAL ¨¨¨¨")
    print("1. Adicionar uma tarefa")
    print("2. Listar as tarefas")
    print("3. Excluir uma tarefa")
    print("4. Sair")

# Add a new task to the list
def add_task():
    task = input("\nDigite sua nova tarefa: ").strip()
    if task:
        core_add_task(todo_list, task) # New way to add task
        print("\nNova tarefa adicionada!")
    else:
        print("\nNão é possível adicionar tarefas vazias!")

# Show the current list of tasks
def list_tasks():
    if not todo_list:  # If the list is empty
        print("\nNenhuma tarefa adicionada!")
    else:
        print("\nA seguir, lista de tarefas:")
        for i, task in enumerate(todo_list, start=1):  # Start numbering from 1
            print(f"{i}. {task}")

# Remove a task by its number
def remove_task():
    list_tasks()
    if not todo_list:
        return
    try:
        task_number = int(input("\nInforme qual tarefa você deseja remover da lista: "))
        try:
            core_remove_task(todo_list, task_number - 1) # New way remove task
            print("\nTarefa removida com sucesso!")
        except IndexError:
            print("\nNúmero de tarefa incorreto/inválido!")
    except ValueError:
        print("\nDigite um número válido por gentileza!")

__version__ = "1.2.0"

# Main loop to keep the program running
while True:
    show_menu()
    choice = input("\nEscolha uma opção (1-4): ").strip()

    if not choice:
        print("\nVocê não digitou nada. Tente novamente.")
        continue  # Go back to menu without crashing

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\nAté a próxima, encerrando o programa...")
        break
    else:
        print("\nDigite uma opção válida (1, 2, 3 ou 4).")