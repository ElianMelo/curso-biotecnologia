'''
Escreva um programa que ordene uma lista numérica com três elementos.
'''

valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor1: "))
valor3 = int(input("Digite o valor1: "))

maior = 0
menor = 0
medio = 0

# Caso 1
if valor3 >= valor2 and valor3 >= valor1:
    maior = valor3
    if valor2 >= valor1:
        medio = valor2
        menor = valor1

# Caso 2
if valor2 >= valor1 and valor2 >= valor3:
    maior = valor2
    if valor3 >= valor1:
        medio = valor3
        menor = valor1

# Caso 3
if valor3 >= valor2 and valor3 >= valor1:
    maior = valor3
    if valor1 >= valor2:
        medio = valor1
        menor = valor2

# Caso 4
if valor2 >= valor1 and valor2 >= valor3:
    maior = valor2
    if valor1 >= valor3:
        medio = valor1
        menor = valor3

# Caso 5
if valor1 >= valor2 and valor1 >= valor3:
    maior = valor1
    if valor3 >= valor2:
        medio = valor3
        menor = valor2

# Caso 6
if valor1 >= valor2 and valor1 >= valor3:
    maior = valor1
    if valor2 >= valor3:
        medio = valor2
        menor = valor3

print("{}, {}, {}".format(menor, medio, maior))
