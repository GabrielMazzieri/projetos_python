current_users = ['sofia', 'gabriel', 'isabela', 'lucas', 'amanda']
new_users = ['Mateus, Nicole, Larissa', 'Gabriel', 'AMANDA']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Já existe um nome igual "{new_user}", por favor digite outro nome')
    else:
        print(f'Você é unico {new_user}')

