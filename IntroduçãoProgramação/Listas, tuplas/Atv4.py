"""Crie a função "remove_max" que remove o maior número de uma lista recebida por parâmetro.

"""

def remove_max(lista):
    if len(lista) == 0:
        return
    else:
        maximo_elemento = max(lista)
        numero_max = lista.index(maximo_elemento)
        lista.pop(numero_max)