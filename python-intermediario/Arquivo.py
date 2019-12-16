# -*- coding: utf-8 -*-

arq = open("Arquivo.txt")
print(arq)

linhas = arq.readlines()
for linha in linhas:
    print(linha)

arq2 = open("Arquivo2.txt", "w")

arq2.write("Esse é o meu arquivo")

arq2.close()

arq.close()

arq = open("Arquivo.txt", "a")

arq.write("Esse é o meu arquivo\n")

arq.close()
