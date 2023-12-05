jogos = ['red dead', 'a plague tale', 'cyberpunk', 'mafia', 'detroit']
print(jogos)

jogos.insert(5, 'the witcher')

jogos.append('mario')

del jogos[6]

jogo_nao_jogado = jogos.pop(4)
print(jogo_nao_jogado)

jogos.sort()
print(jogos)

print(sorted(jogos, reverse=True))

print(jogos)

jogos.reverse()
print(jogos)

print('Total de jogos jogados, zerados e não zerados: ')
print(len(jogos))
