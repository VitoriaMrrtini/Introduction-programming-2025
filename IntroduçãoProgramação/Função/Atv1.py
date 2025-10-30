"""Ordene e indente as linhas abaixo de modo com que o programa que calcula a raiz de uma equação polinomial de primeiro grau (ax + b) funcione corretamente.

Observe que, neste programa, existem duas funções, calcular_raiz e main. A função calcular_raiz possui a responsabilidade de calcular a raiz da equação de primeiro grau. A função main possui a responsabilidade de mostrar a raiz da equação, o que requer chamar a função calcular_raiz. Finalmente, o programa principal faz uma chamada à função main.

"""

def calcular_raiz(a, b):
    return -b  / a
def main():
    coef_angular = float(input("Informe o coeficiente angular da equação"))
    coef_reta = float(input("Informe o coeficiente linear da reta"))
    raiz = calcular_raiz(coef_angular, coef_reta)
    print("A raiz da equação é:", raiz)
main()
