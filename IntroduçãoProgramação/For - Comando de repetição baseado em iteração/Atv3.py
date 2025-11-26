"""Faça uma função "imprimir_fibonacci(x)" que imprime a sequência de Fibonacci até o elemento recebido. Por exemplo, caso x seja igual a 6 ele deverá imprimir até o número 5, dado a sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.... Observe que os números devem ser impressos um em cada linha.

"""

def imprimir_fibonacci(x):
    a = 0
    b = 1
    for i in range(x):
        print(a)
        novo_b = a + b
        novo_a = b 
        a = novo_a
        b = novo_b
