"""Crie um programa que mostre quais letras foram as mais utilizadas em uma string. Para este programa, é esperado que você defina a função contar_letras_alfabeto, que receberá como parâmetro o texto (string) a qual deverá ser processada e que retornará uma lista, de tamanho 26, contendo quantas vezes cada letra do alfabeto apareceu no texto. Para esta lista, a primeira posição (índice 0) corresponderá à quantidade de vezes que a letra a foi utilizada, a segunda posição (índice 1) corresponderá à letra b e assim por diante. Observe que, para os símbolos do alfabeto, não faz diferença entre usar o símbolo em maiúsculo ou minúscula (conta da mesma forma).

"""

lista_letras = list("abcdefghijklmnopqrstuvwxyz")

def contar_letras_alfabeto(texto):
    i = 0
    j = 0
    texto_tratado = texto.lower()
    lista_numeros = [0] * 26

    while i < len(texto_tratado):
        while j < 26:
            if texto_tratado[i] == lista_letras[j]:
                lista_numeros[j] += 1
            j += 1
        j = 0
        i += 1
    
    return lista_numeros


texto = input("")
lista_numeros = contar_letras_alfabeto(texto)

maior = max(lista_numeros)

if maior == 0:
    print()
else:
    lista_nova = []
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i] == maior:
            letra_ref = lista_letras[i]
            lista_nova.append(letra_ref)
            lista_nova.append(maior)
        i += 1

    k = 0
    while k < len(lista_nova):
        print(f"{lista_nova[k]}: {lista_nova[k+1]}")
        k += 2
