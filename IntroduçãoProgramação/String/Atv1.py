"""Quantos dígitos, de zero (0) à nove (9), possui uma string? Crie  uma função de nome count_digits, que recebe um string como parâmetro e que retorna um número inteiro, que faz essa contagem.

"""
def count_digits(texto):
    i = 0
    cont = 0
    texto_formatado = texto.split()
    texto_junto = "".join(texto_formatado)
    while i < len(texto_junto):
        if texto_junto[i].isdigit():
            cont += 1
        i += 1
    return cont