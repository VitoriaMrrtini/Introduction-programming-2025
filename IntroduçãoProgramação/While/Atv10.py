"""Uma maneira de calcular a exponencial de um número x, ou seja, e(x), é pela expansão da série de Taylor, considerando o termo: x ** k / k! Mais detalhes sobre essa função podem ser encontrados em https://en.wikipedia.org/wiki/Characterizations_of_the_exponential_function.

Isso exposto, crie uma função de nome exponential que calcule a exponencial de um número x. Também informe, como parâmetro dessa função, a quantidade de termos a serem utilizados para a expansão da série.

"""


def fatorial(k):
    result = 1
    i = 0
    if k == 0 or k == 1:
        return 1
    else:
        while i < k:
            result = result * (k - i)
            i += 1
    return result


def exponential(x, k):
    i = 0
    Y = 0
    while i < k:
        Y += (x ** i / fatorial(i))
        i += 1
    return Y


def calculo(x, k):
    H = 0
    while True:
        if H < 0.01:
            return H
        else:
            while H > 0.01:
                H = abs(exponential(x, k) - 2.718281828459045)

