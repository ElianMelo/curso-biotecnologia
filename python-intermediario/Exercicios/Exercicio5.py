# -*- coding: utf-8 -*-

'''
Escreva um programa que leia um arquivo multi-fasta e armazene 
em um dicionário: cabeçalho da sequência como a chave e a sequência como valor.
'''

arq = open("arquivo5.fasta")

fastaDicio = dict()
keyAtual = None

linhas = arq.readlines()
for linha in linhas:
    if linha[0] == ">": 
        keyAtual = linha
    else:
        fastaDicio.update({ keyAtual : linha})

for key in fastaDicio.keys():
    print(key + fastaDicio[key])