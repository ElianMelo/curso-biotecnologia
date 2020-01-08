# from statistics import *


# calcula a media
def media(lista):
    # return mean(lista)
    return sum(lista) / float(len(lista))


# calcula a mediana
def mediana(lista):
    # return median(lista)
    lista_ordenada = sorted(lista)
    t = len(lista)

    if t % 2 == 0:
        return (lista_ordenada[int(t / 2)] + lista_ordenada[int((t / 2)) - 1]) / 2
    else:
        return lista_ordenada[int(t / 2)]


# calcula a moda
def moda(lista):
    # return mode(lista)
    lista_dic = {}

    for l in lista:
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            lista_dic[l] += 1

    maior_repeticao = max(lista_dic.values())

    for i in lista_dic:
        if lista_dic[i] == maior_repeticao:
            moda = i

    return moda
