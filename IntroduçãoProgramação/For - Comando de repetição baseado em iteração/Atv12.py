"""Crie um programa que mostra a tabuada de números informados pelo usuário. Quando for informado o número -1, o programa deve ser encerrado. Esse programa deve ter uma função que faz esse cálculo e mostra o resultado.

Para este programa, você pode usar _uma_ vez o comando while e quantas vezes quanto necessárias o comando for.

"""

def tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

def main():
    while True:
        num = int(input())
        if num != -1:
            tabuada(num)
        else:
            return True  
main()