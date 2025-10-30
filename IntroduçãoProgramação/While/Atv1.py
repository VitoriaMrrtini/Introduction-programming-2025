"""Em matemática, a operação fatorial de um número natural n, denotada por denotado por n!, tem como resultado o produto de todos os naturais menores ou iguais a n. Em outras palavras, n ! = n × ( n − 1 ) × ( n − 2 ) × ( n − 3 ) × ⋯ × 3 × 2 × 1. O valor de 0! é 1, conforme a convenção para um produto vazio (Wikipedia, 2024). A seguir, temos uma implementação da operação fatorial em Python, especificada como uma função de nome fatorial, tendo um número inteiro como parâmetro e um número inteiro como resultado. No entanto, a implementação não está funcionando corretamente. Você poderia corrigí-la?

"""

def fatorial(n):
    result = 1
    i = 0
    if n == 0 or n == 1:
        return 1
    else:
        while i < n:
            result = result * (n - i)
            i += 1
    return result