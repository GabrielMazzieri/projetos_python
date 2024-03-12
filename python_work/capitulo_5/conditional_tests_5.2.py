car = 'Audi'

if car.lower() == 'audi':
        print('carro disponivel')

else: 
    car != 'audi'
    print('todos os outros carros estão indisponiveis')


print(car == 'audi')
print(car != 'audi')

idade_autorizada = 60

if idade_autorizada == 18:
    print('\nautorizado(a) para a compra de preço cheio')

elif idade_autorizada < 18:
    print('\nVocê ainda não tem idade suficiente para comprar o carro')
    
elif idade_autorizada >= 60:
    print('\nautorizado(a) para a compra com 50% de desconto')

frutas = ['banana', 'abacaxi', 'maça']

print('banana' in frutas)
print('\nuva' not in frutas)
