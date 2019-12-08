# -*- coding: utf-8 -*-

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]
lista_vazia = []

tamanho = len(minha_lista)

print(minha_lista)
print(tamanho)
print(minha_lista_2)
print(minha_lista_3)
print(minha_lista[2])
print(minha_lista[1])
print(minha_lista[0])
print()

for item in minha_lista:
    print(item)
print()

lista_vazia.append("acao")
lista_vazia.append("aventura")

for item in lista_vazia:
    print(item)
print()

minha_lista.append("limao")
print(minha_lista)

if 7 in minha_lista_2:
    print("7 esta na lista")

if 3 in minha_lista_2:
    print("3 esta na lista")

del minha_lista[2:]
print(minha_lista)
