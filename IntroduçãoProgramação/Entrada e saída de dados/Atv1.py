"""Leia um número inteiro, no formato decimal, e mostre-o como binário, octal, decimal e hexadecimal. Dica: para binário, use o comando bin(valor_numérico).

"""

numero_inteiro = int(input('Digite um número: '))
print("%s" % bin(numero_inteiro))
print("%s" % oct(numero_inteiro))
print("%d" % numero_inteiro)
print("%s" % hex(numero_inteiro))