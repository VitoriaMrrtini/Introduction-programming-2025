"""Efetue a leitura sucessiva de valores numéricos e apresente no final o somatório, a média e a quantidade de valores lidos. O programa deve continuar lendo os números até que seja fornecido um número negativo ou no máximo 10 números sejam informados. Quando esse número negativo for lido, o comando break pode ser usado para interromper o comando de repetição. Esse número negativo não deve entrar nos cálculos. Obs.: mostrar os resultados como ponto flutuante com duas casas decimais.

"""

def leitura():
    soma = 0
    media = 0
    quantidade = 0
    for i in range(10):
        num = float(input())
        if num < 0:
            break
        else:
            quantidade +=1
            soma += num
    if quantidade != 0:
        media = soma / quantidade
    print("%.2f" % soma)
    print("%.2f" % media)
    print("%.2f" % quantidade)
leitura()