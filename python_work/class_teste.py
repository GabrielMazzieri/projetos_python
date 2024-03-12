class computador:
  def __init__(self, marca, memoria, processador):
    self.marca = marca 
    self.memoria = memoria
    self.processador = processador

  def Ligar(self):
    print('Ligando...')

  def Desligar(self):
    print('Desligando...')

  def Informacoes_pc(self):
    print(self.marca, self.memoria, self.processador)

computador_1 = computador('dell', '15GB', 'AMD')
computador_1.Ligar()
computador_1.Desligar()
computador_1.Informacoes_pc()



