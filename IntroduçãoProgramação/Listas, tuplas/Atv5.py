"""Crie a função "inverter_extremidades" que receba uma lista como parâmetro. Para essa lista, a função deve trocar os valores das extremidades, ou seja, o valor da posição inicial deverá assumir o valor original da posição final e o valor da posição final deverá assumir o valor original da posição inicial. Esta função não deve ter  um valor de retorno, mas alterar diretamente a lista recebida como parâmetro.

"""

def inverter_extremidades(lista):
    
    if len(lista) == 0:
        return
    elif len(lista) == 1:
        return
    else:
        inicial = lista[0]
        final = lista[-1]
        lista.pop(0)
        lista.pop(-1)
        lista.insert(0, final)
        lista.append(inicial)