"""Estamos chegando em uma época de promoções no comércio. Uma empresa resolveu que o desconto a ser ofertado para um produto seria baseado na sorte do cliente.  Os descontos podem chegar a 50%, a depender da diferença absoluta de dois números sorteados pelo programa, sendo o menor desconto possível 10% e o máximo 50%.

Para este programa, o cliente não precisa informar valores: tudo é calculado automaticamente. O valor do produto será gerado automaticamente a partir da data e hora atual do computador em que o programa está sendo executado. Esse valor deverá ser inteiro (sem casas decimais) e ser de, no máximo, 2000,00. Para esse máximo, utilize a função de módulo (% 2000) para limitar o valor.

Como resultado, o programa deverá mostrar o valor do produto sem aplicar o desconto,  o valor do desconto (quantos %) e o valor do produto com o desconto aplicado.

A geração de números aleatórios é feita pelo função randint do módulo random. A data e hora atual, em segundos a partir de epoch, podem ser obtidos pela função time do módulo time. Para obter um valor razoável para o produto, divida o valor obtido com a chamada de função time por 100000 (cem mil). Verifique o funcionamento dessas funções pela documentação do Python e com o auxílio da chamada de função help.

"""

from random import randint
from time import time

tempo = time()
valor = int((tempo / 100000) % 2000)
n1 = randint(10,60)
n2 = randint(10,60)
desconto = abs(n1 - n2)

produto_desconto = valor - (valor * (desconto / 100))

print(valor)
print(desconto)
print('%.2f' % produto_desconto)