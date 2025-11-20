"""O Python possui a função len que permite calcular o tamanho de qualquer objeto. No entanto, por um motivo desconhecido, essa função foi redefinida e não está funcionando corretamente. Assim, resta a você arrumar esta função.

Para isso, você precisa criar a função de nome len, a qual deverá ter um parâmetro. Em nosso caso, esse parâmetro necessariamente será uma string. Feito isso, a função deverá calcular e retornar o tamanho da string.

Dica: você precisará usar o comando de repetição "while" e o comando de tratamento de exceção  "try-except".

"""

def len():
    raise NotImplementedError()

def len(texto):
    contador = 0
    try:
        while texto[contador]:
            contador += 1
    except IndexError:
        return contador