"""Considere uma lista de números inteiros. Qual é a menor distância entre dois números consecutivos? Crie uma função, de nome distância_mínima, que receba uma lista como parâmetro e retorne uma tupla contendo a distância e os dois números envolvidos. Caso a lista esteja vazia, retorne a distância como zero e sinalizando que não existiam números usando o valor None.

"""

def distância_mínima(lista):
    if not lista:
        return (0, None, None)
    
    if len(lista) == 1:
        return (0, lista[0], lista[0])
    
    menor_distancia = float('inf')
    num_1, num_2 = None, None
    
    i = 0
    while i < len(lista) - 1:
        distancia = abs(lista[i] - lista[i + 1])
        
        if distancia < menor_distancia:
            menor_distancia = distancia
            num_1, num_2 = lista[i], lista[i + 1]
        
        i += 1
    
    return (menor_distancia, num_1, num_2)