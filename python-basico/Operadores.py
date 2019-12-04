# -*- coding: utf-8 -*-
import math

x = 2
y = 3
z = 3

soma = x + y
subtracao = x - y
multiplicacao = x * y
modulo = x % y
divisao = float(x / y)

print(soma)
print(subtracao)
print(multiplicacao)
print(modulo)
print("{0:.2f}".format(divisao))

print("")

print(x > y)
print(x < y)
print(x == y)
print(y == z)
print(soma == x)
print(soma >= y)
print(soma <= y)
print(y == z and z == y)
print(y == z and x == y)
print(y == z or x == y)
print(y == z or x == y and x == z)
