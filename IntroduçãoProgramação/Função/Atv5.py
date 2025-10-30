"""Crie uma função de nome 'imc' que calcule o IMC, conforme definido na documentação.

"""

# Crie a função 'imc' (e informe aqui a sua assinatura):
"""
    Calcula o Índice de Massa Corporal (IMC) a partir da massa e altura da
    pessoa. O valor é calculado dividindo-se a massa da pessoa (massa m em kg)
    pela altura da mesma elevada ao quadrado (IMC= massa/altura²).

    Parameters
    ----------
    massa : float
            massa em kg da pessoa
    altura : float
             altura em metros da pessoa.

    Returns
    -------
    float
    IMC.
    """


def imc(massa, altura):
    return massa / (altura ** 2)