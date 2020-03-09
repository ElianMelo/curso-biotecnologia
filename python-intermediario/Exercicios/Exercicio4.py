# -*- coding: utf-8 -*-

'''
Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer.
Se o usuário digitar 1, o programa deve chamar uma função que lê um arquivo de texto.
Se o usuário apertar 2, o programa deve imprimir o conteúdo do arquivo lido anteriormente.
Se o usuário apertar três o programa deve ser fechado.
'''

arq = None

def lerArquivo():
    try:
        global arq
        localArq = input("Digite o nome do arquivo: ")
        arq = open(localArq)
    except:
        print("Selecione um arquivo válido")

def mostrarArquivo():
    global arq
    linhas = arq.readlines()
    for linha in linhas:
        print(linha, end="")


while 1:
    print("[ Leitor de Arquivos ]")
    print("1. Ler um arquivo de texto")
    print("2. Mostrar conteudo do arquivo lido")
    print("3. Fechar o programa")

    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        lerArquivo()
    elif opc == 2:
        mostrarArquivo() if arq != None else print("Leia um arquivo antes")
    elif opc == 3:
        break
    else:
        print("Opcao Inválida")
    print()
