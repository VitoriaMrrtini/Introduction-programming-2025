"""Faça uma função "imprimir_decrescente(N)" que imprima os números de 1 a N em ordem decrescente. Mostre um número por linha.

"""
def imprimir_decrescente(N):
    if N > 0:
        i = N
        while i > 0:
            print(N)
            i -= 1
            N -= 1
    elif N < 0:
        i = abs(N)
        while i > 0:
            print(N)
            i -= 1
            N += 1