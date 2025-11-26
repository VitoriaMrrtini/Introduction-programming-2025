"""Crie uma função "soma_todos_pares(N)" que retorna a soma de todos os números pares de 1 a N.
"""

def soma_todos_pares(N):
    soma = 0
    for i in range(0, N+1):
        if i % 2 == 0:
            soma += i
    return soma