"""Faça um programa em Python que receba o raio, calcule e mostre: a) a área de uma esfera, sabe-se que A = 4πR²; b) o volume de uma esfera, sabe-se que V = (4πR³)/3. Mostre cada uma delas em uma linha separada, arredondada para duas casas decimais. Para o cálculo da área e do volume, utilize funções denominadas esfera_area e esfera_volume, criadas por você. Como parâmetro, essas funções recebem o valor do raio.

"""


def esfera_area(raio):
    return 4 * 3.14159265359 * raio ** 2


def esfera_volume(raio):
    return (4 * 3.14159265359 * raio ** 3) / 3


raio = float(input("digite o raio: "))
area = esfera_area(raio)
volume = esfera_volume(raio)

print("%.2f" % area)
print("%.2f" % volume)
