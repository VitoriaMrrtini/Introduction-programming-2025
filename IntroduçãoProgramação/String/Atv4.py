"""Em Python, é possível determinar a ordem de uma palavra em relação a outra. Por exemplo, "a" é menor que "b". No entanto, de forma pouco intuitiva, temos que "a" > "B", ou seja, um símbolo latino minúsculo é maior do que um símbolo maiúsculo. Cansados dessa peculiaridade, queremos criar uma função comparar que preserva a noção de que letras minúsculas são menores do que as maiúsculas. Essa função deve ter dois textos (strings) como parâmetro e deve retornar um número inteiro da seguinte forma: -1 se a primeira palavra for menor que a segunda; 0 se as palavras forem iguais; e 1 se a primeira palavra for maior do que segunda.

"""

def comparar(texto_um, texto_dois):
    try:
        if ord(texto_um[0]) > ord(texto_dois[0]):
            return -1
        else:
            return 1
    except IndexError:
        return 0