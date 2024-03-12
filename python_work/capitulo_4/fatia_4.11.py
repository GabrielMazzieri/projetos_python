my_pizzas = ['portuguesa', 'quatro queijos', 'frango com catupiry']
friend_pizzas = my_pizzas[:]

my_pizzas.append('atum')
friend_pizzas.append('queijo')

print('Minhas pizzas favoritas são:')
for pizza in my_pizzas[:]:
    print(pizza)

print('\nPizzas favoritas de meu amigo é:')
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza)



