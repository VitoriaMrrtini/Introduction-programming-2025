"""Faça uma função "imprimir_triangulo(x)" que receba o número de linhas que o triangulo terá. O triângulo deve ser impresso no seguinte formato:

    *

   ***

  *****

 *******

*********

OBS: Caso venha um número negativo o triangulo deve ser impresso ao contrário e caso o número de linha seja igual a zero a função deve imprimir a seguinte mensagem: "Erro impossivel desenhar com zero linhas!!!"

"""

def imprimir_triangulo(x):
    i = 1
    if x > 0:
        while i <= x:
            espaço = x - i
            asteriscos = 2 * i - 1
            print(" " * espaço + "*" * asteriscos)
            i += 1
    elif x < 0:
        i = abs(x) - 1
        while i >= 0:
            espaço = (abs(x) - i) - 1
            asteriscos = 2 * i + 1
            print(" " * espaço + "*" * asteriscos)
            i -= 1
    else:
        print("Erro impossivel desenhar com zero linhas!!!")