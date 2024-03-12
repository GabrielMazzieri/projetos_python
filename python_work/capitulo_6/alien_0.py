alien_0 = {'color':'red', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

point_value = alien_0.get('points', 'Valor não encontrado')
print(point_value)
