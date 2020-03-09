# -*- coding: utf-8 -*-

'''
Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela.
'''

import sys

for args in sys.argv:
    arq = open(args)
    linhas = arq.readlines()
    for linha in linhas:
        print(linha, end="")
    print()
