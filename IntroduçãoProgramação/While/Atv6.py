"""Leia números fornecidos pelo usuário (um número por vez!) até que sejam lidos dois números iguais em sequência ou que qualquer um dos números seja menor ou igual a zero. Informe quais desses dois motivos levou ao término da leitura de números. Obs.: use as seguintes mensagens: "Numero menor ou igual a zero" e "Numeros iguais".

"""

def sequencia_num():
    while True:
        num1 = int(input())
        if num1 <= 0:
            print("Numero menor ou igual a zero")
            break
        else:
            num2 = int(input())
            if num1 <= 0 or num2 <= 0:
                print("Numero menor ou igual a zero")
                break
            else:
                if num1 == num2:
                    print("Numeros iguais")
                    break
                elif num1 <= 0 or num2 <= 0:
                    print("Numero menor ou igual a zero")
                    break
sequencia_num()

