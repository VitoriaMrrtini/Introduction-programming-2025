"""Dada a velocidade máxima permitida de uma via e a velocidade com que o motorista estava dirigindo nela,  temos um programa que identifica o tipo de infração e calcule o valor da multa. Os tipos de infração são os seguintes:

Velocidade superior à máxima em até 20% (inclusive): Infração média
Velocidade superior à máxima em mais de 20% e até 50% (inclusive): infração grave
Velocidade superior à máxima em mais de 50%: infração gravíssima
Observe que, dependendo da velocidade máxima da via, existe uma tolerância de velocidade. Para velocidade máxima de até 100 km/h, a tolerância é de 7 km/h. Para velocidade máxima superior a 100 km/h, a tolerância é de 7% daquela velocidade. Por exemplo, se o veículo estiver à 107 km/h em uma via cujo limite é de 100 km/h, embora a velocidade esteja acima da máxima permitida, ainda está dentro da tolerância. Assim, não seria emitida uma infração. Por outro lado, se o veículo estiver à 108 km/h nessa via, seria emitida uma infração média por estar acima da tolerância.

O valor da multa, conforme o tipo de infração, é o seguinte:

Infração média: R$ 130,16
Infração grave: R$ 195,23
Infração gravíssima: R$ 293,47
Organize o seu programa para que ele tenha ao menos três funções, considerando a velocidade máxima tolerada, tipo de multa e valor. Para essa organização, faça a refatoração do código, extraindo funções conforme necessário.

"""

def valor_velocidade():
    velocidade_máxima_via = int(input())
    velocidade_veículo = int(input())
    return velocidade_máxima_via, velocidade_veículo

def tolerancia(velocidade_máxima_via):
    if velocidade_máxima_via <= 100:
        return 7
    else:
        tolerância = int(velocidade_máxima_via * 0.07)
        return tolerância

def tipo_multa(velocidade_máxima_via, velocidade_veículo):
        tolerância = tolerancia(velocidade_máxima_via)
        velocidade_máxima_tolerada = velocidade_máxima_via + tolerância
        if velocidade_veículo <= velocidade_máxima_tolerada:
            return 0
        elif velocidade_veículo > (velocidade_máxima_via * 1.50):
            return 4
        elif velocidade_veículo > (velocidade_máxima_via * 1.20):
            return 3
        else:
            return 2

def valor(tipo_infracao):
    if tipo_infracao == 2:
        return 130.16
    elif tipo_infracao == 3:
        return 195.23
    elif tipo_infracao == 4:
        return 293.47
    else:
        return 0

def resultado():
    velocidade_max, velocidade_veiculo = valor_velocidade()
    tipo_infracao = tipo_multa(velocidade_max, velocidade_veiculo)
    valor_multa = valor(tipo_infracao)
    if tipo_infracao == 0:
        print("Parabéns, bom motorista!")
    else:
        print("Você cometeu uma infração e precisa pagar uma multa de R$ %.2f" % valor_multa)
resultado()