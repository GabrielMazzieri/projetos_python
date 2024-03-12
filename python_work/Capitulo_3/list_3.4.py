convidados = ['Leonardo da Vinci', 'Nikola Tesla', 'Albert Einstein']
print(convidados)

print(f'\nPrazer {convidados [0]}, você foi convidado para meu jantar!\n')
print(f'\nPrazer {convidados [1]}, você foi convidado para meu jantar!\n')
print(f'\nPrazer {convidados [2]}, você foi convidado para meu jantar!\n')

convidado_nao_vai = 'Albert Einstein'

convidados.remove(convidado_nao_vai)

print(convidados)

print(f'\nO convidado {convidado_nao_vai} não consiguira participar do evento.\n')

