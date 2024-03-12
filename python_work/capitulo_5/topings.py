available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for resquested_topping in requested_toppings:
    if resquested_topping in available_toppings:        
        print(f'Adicione {resquested_topping}.')

    else:   
        print(f"Desculpe, não temos {resquested_topping}")

print('\nterminamos de criar sua pizza')