users = []

if users:
    for user in users:
        if user == 'admin':
            print('Olá ADM, gostaria de ver um relatório?')
        else:
            print(f'Olá {user}, obrigado por fazer login.')
else:
    print('É necessário encontrar alguns usuários.')