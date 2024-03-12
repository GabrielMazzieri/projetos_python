def somar(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b != 0:
        return a/b
    else:
        return "Não é possível dividir por 0 (zero)"

while True:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    print("Soma: ", somar(num1,num2))
    print("Subtração: ", subtracao(num1,num2))
    print("Multiplicação: ", multiplicacao(num1, num2))
    print("Divisão: ", divisao(num1, num2))

    
