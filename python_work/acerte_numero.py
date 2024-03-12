from random import randint 
import time
import sys

def somar_ponto(pontos):
  pontos += 1
  print('\nvocê acertou!')
  return pontos

while True:
  num_sis = randint(0, 10)
  #print(num_sis)
  chances = 10
  pontos = 0
  
  while chances:
    try:
      num_player = int(input('Digite um número: '))
    except ValueError:
      print('Digite números, não letras.')
      continue
    
    if num_player == num_sis:
      pontos = somar_ponto(pontos)
      num_sis = randint(0, 10)
      #print(num_sis)
      
    elif num_player < num_sis:
      chances = chances - 1
      print('\nVocê errou, tente um número maior.\n')
    elif num_player > num_sis:
      chances = chances - 1
      print('\nVocê errou, tente um número menor.\n')
      
    print('---------------------------------------------------')  
    print(f'\nVocê tem {chances} chances e {pontos} pontos.\n')
    print('---------------------------------------------------')
    if pontos == 10:
      ganhou = print('\nParabéns! Você ganhou o jogo!\n')
      time.sleep(1)
      reiniciar_vit = input('\nDeseja continuar? s/n: ')
      
      if reiniciar_vit.lower() == 's':
        print('\nReiniciando...\n')
        time.sleep(1)
        break
      elif reiniciar_vit.lower() == 'n':
        print('Você saiu.')
        time.sleep(1)
        sys.exit()
      else:
        print('Opção inválida. Por favor, digite "s" para continuar ou "n" para sair.') #Quando solicitado pede para digitar número.
    
  if chances == 0:
    reiniciar = input('Você deseja reiniciar? (s/n): ')
    print('Reiniciando...')
    time.sleep(1)
    if reiniciar.lower() != 's':
      print('você saiu')
      break
      

    


  
  
