import customtkinter as ck
import webbrowser

window = ck.CTk() #criando a janela
btn1 = ck.CTkButton(window, text="Youtube", command=lambda: webbrowser.open('http://www.youtube.com/watch?v='))
btn1.pack()

btn2 = ck.CTkButton(window, text="Instagram", command=lambda: webbrowser.open('http://www.instagram.com/'))
btn2.pack()

window.mainloop()
