# Projeto: Lista de Tarefas
# Versão 1.0.0

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
    tarefa = input("Digite sua nova tarefa: ").strip()
    if tarefa:
        lista.append(tarefa)
        print("Nova tarefa adicionada!")
    else:
        print("Não é possível adicionar tarefas vazias!")
        
# Listando terafas com numeração 
def listar_tarefas():
    if not lista: # Condição para caso não tenha adicionado nenhuma informação
        print("Nenhuma tarefa adicionada!")
    else: 
        print("A seguir, lista de tarefas:")
        for i, tarefa in enumerate(lista, start=1): # Enumado para começar no '1.'
            print(f"{i}. {tarefa}") # Formatação das variáveis
            
# Função para remover tarefas
def remover_tarefa():
    listar_tarefas()
    if not lista:
        return
    try:
        numero_da_tarefa = int(input("Informe qual tarefa você deseja remover da lista: "))
        if 1 <= numero_da_tarefa <= len(lista): # Verificador do removedor de tarefas
            numero_da_tarefa_removida = lista.pop(numero_da_tarefa - 1) # Remove o número da lista
            print(f"Tarefa {numero_da_tarefa_removida} removida com sucesso!")
        else:
            print("Número de tarefa incorreto/inválido!")
    except ValueError:
        print("Digite um número válido por gentileza!")
        
# Loop principal para manter o programa funcionando
while True:
    menu()
    opcoes_menu = input("Escolha uma opção (1-4): ").strip()
    
    if opcoes_menu == "1":
        adicionar_tarefa
    elif opcoes_menu == "2":
        listar_tarefas
    elif opcoes_menu == "3":
        remover_tarefa
    elif opcoes_menu == "4":
        print("Até a próxima, encerrando o programa...")
        break
    else:
        print("Digite um número válido por gentileza!")