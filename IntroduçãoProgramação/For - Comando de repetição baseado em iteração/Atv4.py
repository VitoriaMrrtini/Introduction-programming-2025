"""Crie uma função "imprimir_quadrado(comprimento, asteriscos)" que imprima um quadrado com "*" dado o comprimento de seu lado e o número de asteriscos disponíveis. Por exemplo, se o comprimento do lado do quadrado for 5, logo um quadrado precisará de 25 asteriscos para serem feitos. No entanto, se tivemos apenas 21 asteriscos, o programa deve imprimir o seguinte:

*****
*****
*****
*****
*

Observe que o comprimento do lado e o número de asteriscos disponíveis são parâmetros da função. Não é necessário definir um programa que chame essa chamada.

"""

def imprimir_quadrado(comprimento, asterisco):
    linha = "*" * comprimento
    if comprimento % 2 == 0:
        final = int(asterisco/comprimento) - 1
    else:
        final = int(asterisco/comprimento)
    for i in range(0, final):
        print(linha)