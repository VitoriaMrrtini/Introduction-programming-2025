"""Leia números fornecidos pelo usuário (um número por vez!) até que sejam lidos dois números iguais em sequência ou que qualquer um dos números seja menor ou igual a zero. Faça isso no máximo 5 vezes. Informe quais desses três motivos levou ao término da leitura de números. Obs.: use as seguintes mensagens: "Número menor ou igual a zero", "Números iguais", "Número máximo de tentativas alcançado"

"""

def leitura():
    parou = False
    for i in range(0, 6, 2):
        num1 = int(input())
        if num1 <= 0:
            parou = True
            print("Número menor ou igual a zero")
            break
        else:
            num2 = int(input())
            if num2 <= 0:
                parou = True
                print("Número menor ou igual a zero")
                break
            elif num1 == num2:
                parou = True
                print("Números iguais")
                break
    if parou == False:
        print("Número máximo de tentativas alcançado")
leitura()