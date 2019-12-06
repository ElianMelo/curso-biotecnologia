'''
Faça um programa que receba a idade do usuário
e diga se ele é maior ou menor de idade.
'''

idade = int(input("Informe sua idade: "))

if 0 < idade < 18:
    print("Você é menor de idade")
elif idade >= 18:
    print("Você é maior de idade")
else:
    print("Idade Inválida")
