# Projeto: Lista de Tarefas
# Versão 1.1.0

# Variável Global de armazenamento das tarefas
lista = []

# Função visual do menu
def menu():
    print("\n¨¨¨¨ MENU PRINCIPAL ¨¨¨¨")
    print("1. Adicionar uma tarefa")
    print("2. Listas as tarefas")
    print("3. Excluir uma tarefa")
    print("4. Sair")
    
# Atribuindo função ao botão 1.    
def adicionar_tarefa():
    tarefa = input("\nDigite sua nova tarefa: ").strip()
    if tarefa:
        lista.append(tarefa)
        print("\nNova tarefa adicionada!")
    else:
        print("\nNão é possível adicionar tarefas vazias!")
        
# Listando terafas com numeração 
def listar_tarefas():
    if not lista: # Condição para caso não tenha adicionado nenhuma informação
        print("\nNenhuma tarefa adicionada!")
    else: 
        print("\nA seguir, lista de tarefas:")
        for i, tarefa in enumerate(lista, start=1): # Enumado para começar no '1.'
            print(f"{i}. {tarefa}") # Formatação das variáveis
            
# Função para remover tarefas
def remover_tarefa():
    listar_tarefas()
    if not lista:
        return
    try:
        numero_da_tarefa = int(input("\nInforme qual tarefa você deseja remover da lista: "))
        if 1 <= numero_da_tarefa <= len(lista): # Verificador do removedor de tarefas
            numero_da_tarefa_removida = lista.pop(numero_da_tarefa - 1) # Remove o número da lista
            print(f"Tarefa {numero_da_tarefa_removida} removida com sucesso!")
        else:
            print("\nNúmero de tarefa incorreto/inválido!")
    except ValueError:
        print("\nDigite um número válido por gentileza!")
        
# Loop principal para manter o programa funcionando
while True:
    menu()
    opcoes_menu = input("\nEscolha uma opção (1-4): ").strip()

    if not opcoes_menu:
        print("\nVocê não digitou nada. Tente novamente.")
        continue  # Volta pro menu sem travar

    if opcoes_menu == "1":
        adicionar_tarefa()
    elif opcoes_menu == "2":
        listar_tarefas()
    elif opcoes_menu == "3":
        remover_tarefa()
    elif opcoes_menu == "4":
        print("\nAté a próxima, encerrando o programa...")
        break
    else:
        print("\nDigite uma opção válida (1, 2, 3 ou 4).")