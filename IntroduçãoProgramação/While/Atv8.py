"""Crie uma função "soma_todos(N)" que retorna a soma de todos os números de 1 a N.

"""

def soma_todos(N):
    i = 0
    X = N
    Y = X
    while i < N:
        X += (Y - 1)
        Y -= 1
        i += 1
    print(X)