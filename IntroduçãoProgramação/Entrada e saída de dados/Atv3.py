"""Leia um número real (ponto flutuante) e o mostre no formato de ponto fixo com duas casas decimais e na notação científica.

"""

numero = float(input('Digite um numero: '))
print("%.2f" % numero)
print("%e" % numero)
