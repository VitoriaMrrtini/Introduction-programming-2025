"""Crie uma função "soma_todos_pares(N)" que retorna a soma de todos os números pares de 1 a N.
"""

def soma_todos_pares(N):
    soma = 0
    i = 1
    while i <= N:
        if i % 2 == 0:
            soma += i
        i += 1
    print(soma)