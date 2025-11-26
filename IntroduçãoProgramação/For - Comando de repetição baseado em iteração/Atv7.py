"""Faça uma função "imprimir_mensagem(mensagem, quantidade)" que imprima uma mensagem, informada por um parâmetro na função, várias vezes, sendo a quantidade de vezes também informada por um parâmetro na função.

"""

def imprimir_mensagem(mensagem, quantidade):
    mensagens = [mensagem] * quantidade
    for frase in mensagens:
        print(frase)