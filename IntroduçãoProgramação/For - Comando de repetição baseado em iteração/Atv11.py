"""Crie um programa que mostra o resultado de cada somatório dos números naturais de a à b, sendo que tais números são informados pelo usuário. Para isso, crie uma função somatório que tenha como parâmetro o número natural e retorne o resultado do somatório.

"""

def somatorio(num1):
    soma = 0
    for i in range(1, num1+1):
        soma += i
    print(soma)
def main():
    num1 = int(input())
    num2 = int(input())
    if num2 >= num1:
        for i in range(num1, num2+1):
            somatorio(i)
    else:
        for i in range(num1, num2-1, -1):
            somatorio(i)
main()