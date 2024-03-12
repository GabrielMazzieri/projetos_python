my_foods = ['pizza', 'falafel', 'carrot cake', ]
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Minhas comidas favoritas são:")
for my_food in my_foods[:]:
    print(my_food)

print("\nComidas favoritas do meu amigo são:")
for friend_food in friend_foods[:]:
    print(friend_food)
    
    