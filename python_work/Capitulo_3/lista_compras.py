lista_compras = []

while True:
    print("Escolha uma opção: ")
    print("1. Adicionar itens na lista de compras: ")
    print("2. Ver lista de compras: ")
    print("3. Sair: ")
    
    opcao = input()

    if opcao == '1':
        item = input("Adicione o item: ")
        lista_compras.append(item)

    elif opcao == '2':
        if lista_compras:
            print("Lista de compras: ")
        for item in lista_compras:
            print(item)
    
    else:
        print("A lista está vazia.")
    
    elif opcao == '3':
    break
else:
print("Obrigado por utilizar o programa!")
