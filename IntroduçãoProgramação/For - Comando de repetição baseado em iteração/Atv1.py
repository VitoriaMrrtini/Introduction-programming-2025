"""Uma maneira de calcular a exponencial de um número x, ou seja, e(x), é pela expansão da série de Taylor, considerando o termo: x ** k / k! Mais detalhes sobre essa função podem ser encontrados em https://en.wikipedia.org/wiki/Characterizations_of_the_exponential_function. 

Isso exposto, crie uma função de nome exponential que calcule a exponencial de um número x. Também informe, como parâmetro dessa função, a quantidade de termos a serem utilizados para a expansão da série.

"""

def potencia(x, k):
    result = x
    if k == 0:
        return 1
    elif k == 1:
        return x
    else:
        for i in range(1, k):
            result *= x
    return result

def fatorial(k):
    result = k
    if k == 0:
        return 1
    else:
        for i in range((k-1), 1, -1):
            result *= i
    return result

def exponential(x, k):
    soma = 0
    for i in range(0, k):
        conta = potencia(x, i) / fatorial(i)
        soma += conta
    return soma