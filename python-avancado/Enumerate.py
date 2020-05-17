# -*- coding: utf-8 -*-

# Buscando apenas o valor
lista = ["abacate", "bola", "cachorro"]

for nome in lista:
    print(nome)

print()

# Buscando valor e índice utilizando range e len
for i in range(len(lista)):
    print(i, lista[i])

print()

# Buscando valor e índice utilizando enumerate
for i, nome in enumerate(lista):
    print(i, nome)
