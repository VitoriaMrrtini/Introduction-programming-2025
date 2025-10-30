"""Leia um número real (ponto flutuante), converta-o para um número inteiro e mostre o valor resultante no formato de ponto fixo com duas casas decimais e na notação científica.

"""

numero = float(input('digite um número: '))
numero = int(numero)
print("%.2f" % numero)
print("%e" % numero)