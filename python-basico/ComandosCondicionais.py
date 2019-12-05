# -*- coding: utf-8 -*-

x = 1
y = 10000000

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

x = 1
y = 2

if x > y:
    print("x maior que y")
else:
    print("x não é maior que y")

a = 7
b = 6

if b > a:
    if b > 0:
        print("b é maior que a\nb é positivo")
    else:
        print("b não é maior que a nem positivo")
else:
    print("b menor que a")

x = 1
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")
