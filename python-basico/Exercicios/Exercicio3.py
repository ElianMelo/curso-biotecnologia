'''
Escreva um programa que resolva uma equação de segundo grau.
'''

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b * b) - (4 * a * c)

if delta > 0:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)

    print("Essa equacao possui duas raizes reais")
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
elif delta == 0:
    x1 = (-b) / (2 * a)

    print("Essa equacao possui uma raiz real")
    print("x1 = {}".format(x1))
else:
    print("Essa equacao não apresenta raiz real")


