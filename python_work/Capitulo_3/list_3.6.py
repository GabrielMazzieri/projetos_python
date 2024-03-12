convidados = ['Leonardo da Vinci', 'Nikola Tesla', 'Isaac Newton']
print(len(convidados))

convidados.insert(0, 'Steve Jobs')
convidados.insert(2, 'Bill Gates')
convidados.append('Elon Musk')

print(convidados)

print(f'\nVocê foi convidado {convidados [0]}!')
print(f'\nVocê foi convidado {convidados [1]}!')
print(f'\nVocê foi convidado {convidados [2]}!')
print(f'\nVocê foi convidado {convidados [3]}!')
print(f'\nVocê foi convidado {convidados [4]}!')
print(f'\nVocê foi convidado {convidados [5]}!')

atualizacao = (f'\n*Gostaria de informalos que infelizmente está disponível uma mesa para até dois convidados*')
print(atualizacao)
