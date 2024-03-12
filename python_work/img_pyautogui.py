import pyautogui

pyautogui.PAUSE = 1

#abrir sistema
pyautogui.press('win')
pyautogui.write('instagram')
pyautogui.press('enter')

#email
pyautogui.click(x=1494, y=392)
pyautogui.click(x=1494, y=392)
pyautogui.write('gabrielnmazzieri@gmail.com')
#senha
pyautogui.click(x=1482, y=439)
pyautogui.write('exemplo')
#entrar
pyautogui.click(x=1567, y=504)

