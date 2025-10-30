"""Faça uma função que receba o ano de nascimento de uma pessoa e o ano atual, calcule e retorne a idade dessa pessoa em dias. Desconsidere a existência de anos bissextos.

"""
def calcular_idade_em_dias(ano_nascimento, ano_atual):
    return 365 * (ano_atual - ano_nascimento)