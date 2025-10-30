"""Efetue a leitura sucessiva de valores numéricos e apresente no final o somatório, a média e a quantidade de valores lidos. O programa deve continuar lendo os números até que seja fornecido um número negativo. Quando esse número negativo for lido, o comando break pode ser usado para interromper o comando de repetição while. Esse número negativo não deve entrar nos cálculos. Obs.: mostrar os resultados como ponto flutuante com duas casas decimais.

"""


def somatorio(num):
    soma_num = 0.00
    if num > 0:
        soma_num = num
    media_num = 0.00
    quant_num = 0.00
    i = 1
    while num > 0:
        num = float(input())
        if num < 0:
            break
        else:
            i += 1
            soma_num += num
            media_num = soma_num / i
            quant_num = i

    print("%.2f" % soma_num)
    print("%.2f" % media_num)
    print("%.2f" % quant_num)


def main():
    num = float(input())
    somatorio(num)


main()
