'''
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
sinal = str(input("Digite um sinal: "))


if sinal == "/":
    print(valor1 / valor2)
elif sinal == "*":
    print(valor1 * valor2)
elif sinal == "%":
    print(valor1 % valor2)
elif sinal == "+":
    print(valor1 + valor2)
elif sinal == "-":
    print(valor1 - valor2)
elif sinal == "**":
    print(valor1 ** valor2)
else:
    print("Simbolo inválido")
