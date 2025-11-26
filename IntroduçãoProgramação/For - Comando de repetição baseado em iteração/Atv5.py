"""Faça uma função "imprimir_triangulo(x)" que receba o número de linhas que o triangulo terá. O triângulo deve ser impresso no seguinte formato:

    *

   ***

  *****

 *******

*********

OBS: Caso venha um número negativo o triangulo deve ser impresso ao contrário e caso o número de linha seja igual a zero a função deve imprimir a seguinte mensagem: "Erro impossivel desenhar com zero linhas!!!"

"""

def imprimir_triangulo(x):
    if x > 0:
        y = x - 1
        for i in range(1, x+1):
            espaço = " "*y
            triangulo = "*" * (i + (i-1))
            print(espaço + triangulo)
            y -=1
    elif x < 0:
        y = 0
        for i in range(abs(x), 0, -1):
            espaço = " " * y
            triangulo ="*" * ((i-1) + i)
            print(espaço + triangulo)
            y +=1
    else:
        print("Erro impossivel desenhar com zero linhas!!!")
        