convidados = ['Leonardo da Vinci', 'Nikola Tesla', 'Isaac Newton']

convidados.insert(0, 'Steve Jobs')
convidados.insert(2, 'Bill Gates')
convidados.append('Elon Musk')

lamento_1 = convidados.pop(5)
print(f'\nLamento {lamento_1}, mas você não está mais convidado.')

lamento_2 = convidados.pop(4)
print(f'\nLamento {lamento_2}, mas você não está mais convidado.')

lamento_3 = convidados.pop(2)
print(f'\nLamento {lamento_3}, mas você não está mais convidado.')

lamento_4 = convidados.pop(0)
print(f'\nLamento {lamento_4}, mas você não está mais convidado.\n')

print(f'Você ainda está convidado {convidados [0]}!')
print(f'Você ainda está convidado {convidados [1]}!\n')

del convidados[0]
del convidados[0]

print((len(convidados)))
