dolar = 5.06
euro = 5.36
real = float(input("Digite o valor para ser convertido: "))

dolar_real = (f"O valor de dólar para real é: {real * dolar}")

euro_real = (f"O valor de euro para real é: {real * euro}")

print(dolar_real)
print(euro_real)

if dolar < euro:
    print("*Dólar está mais barato que o Euro*")

else:
    print("*Euro Está mais barato que o Dólar*")

    