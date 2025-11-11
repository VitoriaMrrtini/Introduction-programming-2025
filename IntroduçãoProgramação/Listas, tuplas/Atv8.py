"""Escreva uma função "list_intersection" que recebe duas listas e realiza a interseção entre o conteúdo de ambas, colocando o resultado em uma nova lista, a ser retornada.

"""

def list_intersection(lista_1, lista_2): 
    i = 0 
    nova_lista = [] 
    if len(lista_1) >= len(lista_2): 
        while i < len(lista_2): 
            if lista_2[i] in lista_1: 
                nova_lista.append(lista_2[i]) 
            i += 1 
    elif len(lista_1) <= len(lista_2): 
        while i < len(lista_1): 
            if lista_1[i] in lista_2: 
                nova_lista.append(lista_1[i]) 
            i += 1 
    return nova_lista