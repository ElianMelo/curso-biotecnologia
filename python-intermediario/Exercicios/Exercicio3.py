# -*- coding: utf-8 -*-

'''
Escreva um programa que receba uma sequência 
digitada pelo usuário e a salve num arquivo no formato fasta.
'''

texto = input("Digite algo: ")
texto += "\n"

arq = open("arquivo3.fasta", "a")
arq.write(texto)

print("O seu texto foi salvo no arquivo arquivo3.fasta")
