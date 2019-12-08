# -*- coding: utf-8 -*-

meu_dicionario = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORRO"}

print(meu_dicionario)
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])

print()

# Itera pelo dicionario
for chave in meu_dicionario:
    print(chave + " " + meu_dicionario[chave])

print()

# Itera pelas tuplas chave/valor
for i in meu_dicionario.items():
    print(i)

print()

# Itera pelo valores
for i in meu_dicionario.values():
    print(i)

print()

# Itera pelas chaves
for i in meu_dicionario.keys():
    print(i)
