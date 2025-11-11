"""Em Python não existe um tipo de dado matriz nativo. No entanto, é possível simular uma com uma lista de listas. A lista inicial possui as linhas, cada qual, por sua vez, representada por uma nova lista. Por exemplo, para criar uma matriz de 5 linhas e 8 colunas, você criaria uma lista que conteria outras 5 listas, sendo que essas listas contidas possuem, cada uma oito valores. Por exemplo, o seguinte código criaria tal lista:

matriz = [[0] * 8] * 5

Observe que [0] * 8 cria uma lista com oito posições, cada uma preenchida com zero. O restante do comando, [ ... ] * 5 cria uma lista com cinco posições, cada uma delas preenchida com o conteúdo dentre de [ ], que, em nosso caso, é uma lista com oito posições preenchidas com zero.

Isso feito, crie a função criar_matriz() que crie e retorne uma matriz, recebendo três parâmetros: quantidade de linhas, quantidade de colunas e valor padrão a ser utilizado para preencher cada posição da matriz.

"""

def criar_matriz(linhas, colunas, valor):
    menor, maior = min(colunas, linhas), max(colunas, linhas)
    return [[valor] * menor] * maior