# -*- coding: utf-8 -*-

# Condição que será utilizada para aplicar o filtro
def pares(i):
    if i % 2 == 0:
        return 1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cria uma nova lista com base na filtragem de uma
lista_pares = filter(pares, lista)
print(list(lista_pares))
