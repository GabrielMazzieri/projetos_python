import sys
import time

tarefas_user = []

while True:
    print('1. Visualizar tarefas')
    print('2. Adicionar uma tarefa')
    print('3. Remover tarefas')
    print('4. Sair do programa')

    try:
        user = int(input('Digite umas das opções: '))
    except ValueError:
        print('Digite um valor válido.')
        continue
    time.sleep(1)

    if user == 1:
        print(tarefas_user)
    elif user == 2:
        opc_2 = input('Adicionar tarefa: ')
        tarefas_user.append(opc_2)
    elif user == 3:
        if len(tarefas_user) == 0:
            print('Não tem tarefas para excluir.')
        else:
            print('Tarefas Disponíveis:')
            for i, tarefa in enumerate(tarefas_user):
                print(f'{i + 1}. {tarefa}')
            try:
                num_tarefa = int(input('Digite o número da tarefa a ser removida: '))
                if num_tarefa < 1 or num_tarefa > len(tarefas_user):
                    print('Número de tarefa inválido.')
                else:
                    del tarefas_user[num_tarefa - 1]
            except ValueError:
                print('Digite um número válido.')
    elif user == 4:
        user_exit = input('\nDeseja mesmo sair? (s/n): ')
        if user_exit.lower() == 's':
            print('\nflw')
            sys.exit()
        elif user_exit.lower() == 'n':
            continue
        else:
            print('Digite um valor válido.')
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        
        