"""Em algumas competições esportivas, a nota de um atleta é calculada a partir da média da pontuação obtida a cada tentativa, excluindo-se a menor e a maior pontuação. Crie a função "média_sem_extremos" que faz esse cálculo, recebendo como parâmetro uma lista ou tupla com as pontuações e retornando a nota do atleta.

"""
def média_sem_extremos(pontos):
    while True:
        i = 0
        soma = 0
        if len(pontos) == 0:
            return 0.0
        elif len(pontos) == 1:
            return float(pontos[0])
        elif len(pontos) == 2:
            while i < len(pontos):
                soma += pontos[i]
                i += 1
            nota = soma / len(pontos)
            return nota
        else:
            minimo = min(pontos)
            maximo = max(pontos)
            posicao_min = pontos.index(minimo)
            posicao_max = pontos.index(maximo)
            pontos.pop(posicao_min)
            pontos.pop(posicao_max)
            if len(pontos) == 1:
                return float(pontos[0])
            elif len(pontos) == 0:
                return 0.0
            else:
                while i < len(pontos):
                    soma += pontos[i]
                    i += 1
                nota = soma / len(pontos)
                return nota


