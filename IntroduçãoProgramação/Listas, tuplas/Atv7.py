"""Escreva uma função "histogram(days)" que recebe uma lista de números inteiros com sete elementos. A lista armazena as temperaturas para cada dia da semana, iniciando por domingo. A função deve mostrar graficamente (de modo textual) essas temperaturas, usando o símbolo ">" para cada grau observado naquele dia. Por exemplo, se as temperaturas em days forem [19, 21, 25, 22, 20, 17, 15] graus celsius, a função deverá exibir:

D: >>>>>>>>>>>>>>>>>>>
S: >>>>>>>>>>>>>>>>>>>>>
T: >>>>>>>>>>>>>>>>>>>>>>>>>
Q: >>>>>>>>>>>>>>>>>>>>>>
Q: >>>>>>>>>>>>>>>>>>>>
S: >>>>>>>>>>>>>>>>>
S: >>>>>>>>>>>>>>>

"""

def histogram(days):
    while True:
        dias_semana = ("D", "S", "T", "Q", "Q", "S", "S")
        i = 0
        while i < len(days):
            temp = ">" * days[i]
            semana = dias_semana[i]
            i += 1
            mensagem = "%s: %s" % (semana, temp)
            print(mensagem)
        return