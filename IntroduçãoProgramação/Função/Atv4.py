"""Faça um função em Python que receba um valor que foi depositado e retorne o valor com rendimento após seis meses, arredondado para duas casas decimais. Considere fixo o juros da poupança em 0,50% ao mês.

O arredondamento deve ser feito com a função round. Esta função possui dois parâmetros: o número a ser arredondado e a quantidade casas decimais a serem preservadas no número arredondado. Por exemplo, a chamada de função round(7.4232, 3) terá como resultado o valor 7.423, que é o arredondamento do número 7.4232 com três casas decimais.

"""

def calcular_rendimento(valor, juros):
    return round(valor * ((1 + juros) ** 6), 2)