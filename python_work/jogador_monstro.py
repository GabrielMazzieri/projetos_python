import random

#Jogador
nome_usuario = input('Digite seu nome: ')

vida_usuario = 100
#Monstro
monstros = ['Lobisomem', 'Minotauro', 'Elfo', 'Goblin', 'Fantasma', 'Múmia', 'Vampiro', 'Zumbi']

monstro = random.choice(monstros)

vida_completa_monster = 100
#JogadorxMonstro
print(f'Bem-Vindo(a) {nome_usuario}, você enfrentará {monstro}')

#dado
numeros_dado = list(range (10, 70))

rolar_dado = random.choice(numeros_dado)

ataque = rolar_dado

nao_jogou = ("Você optou por não jogar o dado.")

confirmar_dado = input('Digite "Sim" para girar o dado: ' )
if confirmar_dado == "Sim":
    print(f"O valor do dado foi {rolar_dado}")
elif confirmar_dado == "Não":
    exit(nao_jogou)
else:
    exit("você não digitou corretamente")    

dano_causado = rolar_dado

vida_monstro = dano_causado - vida_completa_monster
   
#dano
if ataque < vida_completa_monster:
    print(f"Agora {monstro} está com {vida_monstro} de vida!")


        
        
