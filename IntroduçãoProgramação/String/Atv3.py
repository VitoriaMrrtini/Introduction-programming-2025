"""Quantas vezes uma palavra acontece em uma string? Crie a função contar_palavra que tem como parâmetros duas string: a primeira é o texto completo e a segunda é a palavra sendo procurada. Retorno um número inteiro com a quantidade de vezes que a palavra aparece no texto.

"""

def contar_palavra(texto_completo, palavra):
    contar = 0
    começo = 0
   
    while True: 
        i = texto_completo.find(palavra, começo)
        if i != -1:
            contar+=1
            começo = i + 1
        else:
            break
    return contar