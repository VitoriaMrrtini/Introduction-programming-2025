"""Complete a função "in_rainbow" para determinar se as cores fornecidas como parâmetro na forma de uma lista, são um subconjunto  das cores do arco-íris.

"""
def in_rainbow(cores):
    cores_arco_íris = ["vermelho", "laranja", "azul", "verde", "azul", "anil", "violeta"]
    if len(cores) == 0:
        return True
    else:
        y = 0
        while y < len(cores):
            if cores[y] not in cores_arco_íris:
                return False
            y +=1
    return True