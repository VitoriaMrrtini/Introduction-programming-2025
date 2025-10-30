"""Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m² deve-se usar 18 W de potência. Faça um função que receba as duas dimensões de um cômodo (em metros) e calcule a potência de iluminação que deverá ser utilizada.

"""
def calcular_iluminacao(dimensao1, dimensao2):
    return 18 * (dimensao1 * dimensao2)