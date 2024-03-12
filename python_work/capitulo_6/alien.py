alien_0 = {'x_position': 0, 'y_position':25, 'speed':'medium'}
print(f"posição original: {alien_0['x_position']}")

#deslocamento do alien para a direita
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #velocidade máxima
    x_increment = 3

#posição nova é a posiçaõ antiga mais (+) o incremento (increment)
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'Nova posição: {alien_0["x_position"]}')


