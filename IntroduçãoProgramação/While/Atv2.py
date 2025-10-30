"""Faça uma função "imprimir_mensagem(mensagem, quantidade)" que imprima uma mensagem, informada por um parâmetro na função, várias vezes, sendo a quantidade de vezes também informada por um parâmetro na função.

"""
def imprimir_mensagem(mensagem, quantidade):
    i = 0
    while i < quantidade:
        i += 1
        print(mensagem)