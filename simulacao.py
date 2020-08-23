from classes import *

num_clientes = 10000
num_bancos = 10
pesos = [
    {
        'renda': 9706,
        'tarifa': 1,
        'anuidade': 1,
        'qualidade': 8
    },
    {
        'renda': 3422,
        'tarifa': 2,
        'anuidade': 3,
        'qualidade': 5,
    },
    {
        'renda': 1871,
        'tarifa': 4,
        'anuidade': 5,
        'qualidade': 1,
    }
]


class Simulacao():

    def __init__(self):
        self.clientes = list()
        self.bancos = list()

    def criar_agentes(self):
        for i in range(1, num_bancos + 1):
            self.bancos.append(Banco(i))

        pesos_selecionados = random.choices(pesos, weights=[0.1*num_clientes, 0.2*num_clientes, 0.7*num_clientes], k=num_clientes)

        for j in range(1, num_clientes + 1):
            banco_escolhido = random.choice(self.bancos)
            peso = pesos_selecionados.pop()
            self.clientes.append(Cliente(j, banco_escolhido, peso))

    def executar_modelo(self):

        valores = ['cliente,renda,banco,tarifa maxima esperada,tarifa cobrada,experiencia com a tarifa,anuidade maxima '
                   'esperada,anuidade cobrada, experiencia com anuidade,qualidade de atendimento minima esperada,'
                   'qualidade de atendimento prestado,experiencia com atendimento, media de nota']

        media_por_faixa = {
            9706: {
                7: 0,
                3: 0,
                0: 0,
                "troca": 0,
            },
            3422: {
                7: 0,
                3: 0,
                0: 0,
                "troca": 0,
            },
            1871: {
                7: 0,
                3: 0,
                0: 0,
                "troca": 0,
            },
        }

        medias = []
        num_zero = 0
        num_tres = 0
        num_sete = 0
        num_trocaram_banco = 0

        for cliente in self.clientes:
            experiencia_tarifa = cliente.verifica_tarifa()
            experiencia_anuidade = cliente.verifica_anuidade()
            experiencia_qualidade = cliente.verifica_qualidade()

            media = (experiencia_anuidade * cliente.pesos['anuidade'] + experiencia_tarifa * cliente.pesos['tarifa']
                     + experiencia_qualidade * cliente.pesos['qualidade']) / 10
            medias.append(media)

            valor = '\n' + str(cliente.id) + ',' + str(cliente.conta.saldo) + ',' + str(cliente.banco.id) + ',' + \
                    str(cliente.resiliencia_tarifa) + ',' + str("%.2f" % cliente.banco.tarifa) + ',' + \
                    str(cliente.verifica_tarifa()) + ',' + str(cliente.resiliencia_anuidade) + ',' + \
                    str("%.2f" % cliente.banco.anuidade) + ',' + str(cliente.verifica_anuidade()) + ',' + \
                    str(cliente.resiliencia_qualidade) + ',' + str(cliente.banco.qualidade) + ',' + \
                    str(cliente.verifica_qualidade()) + ',' + str(media)

            valores.append(valor)

            # Contagem de satisfação dos clientes
            if media >= 7:
                num_sete += 1
                media_por_faixa[cliente.conta.saldo][7] += 1
            elif media >= 3:
                num_tres += 1
                media_por_faixa[cliente.conta.saldo][3] += 1
            elif media > 0:
                media_por_faixa[cliente.conta.saldo][0] += 1
                troca = cliente.escolhe_banco(self.bancos)
                num_trocaram_banco += troca
                media_por_faixa[cliente.conta.saldo]['troca'] += troca
                num_zero += 1

            # print("Cliente: ", cliente.id)
            # print("Banco: ", cliente.banco.id)
            # print("Resiliência de tarifa: ", cliente.resiliencia_tarifa)
            # print("Tarifa cobrada: ", cliente.banco.tarifa)
            # print("Experiencia coma tarifa:", cliente.verifica_tarifa())
            # print("Resiliência de anuidade: ", cliente.resiliencia_anuidade)
            # print("Anuidade cobrada: ", cliente.banco.anuidade)
            # print("Experiencia com a anuidade:", cliente.verifica_anuidade())
            # print("Resiliência de qualidade: ", cliente.resiliencia_qualidade)
            # print("Qualidade prestada: ", cliente.banco.qualidade)
            # print("Experiencia com o atendimento:", cliente.verifica_qualidade())
            # print("-------------------------------------------")

        satisfacao_por_renda = ['faixa de renda,satisfacao maior que 7, satisfacao menor que 7 e maior que 3, '
                                'satisfacao menor que 3 e maior que 0, clientes que trocaram de banco']
        for chave in media_por_faixa:
            satisfacao = "\n" + str(chave) + "," + str(media_por_faixa[chave][7]) + "," \
                         + str(media_por_faixa[chave][3]) + "," + str(media_por_faixa[chave][0]) + ',' \
                         + str(media_por_faixa[chave]["troca"])
            satisfacao_por_renda.append(satisfacao)
            print("Faixa de renda de ", chave)
            print("Satisfacao maior que 7: ", media_por_faixa[chave][7])
            print("Satisfacao maior que 3 e menor que 7: ", media_por_faixa[chave][3])
            print("Satisfacao maior que 0 e menor que 3: ", media_por_faixa[chave][0])

            print("--------------------------------------------------")

        media_final = sum(medias)/num_clientes
        media_final = float("%.2f" % media_final)
        print("\nResultados consolidados dessa simulação: \n")
        print("Média de satisfação: ", media_final)
        print("Satisfação maior que 7: ", num_sete)
        print("Satisfação maior que 3 e menor que 7: ", num_tres)
        print("Satisfação maior que 0 e menor que 3: ", num_zero)
        print("Clientes que trocaram de banco: ", num_trocaram_banco)

        guardar('resultado.csv', valores)
        guardar('satisfacao_por_renda.csv', satisfacao_por_renda)


def guardar(arquivo, valores):
    with open(arquivo, 'w') as arquivo:
        arquivo.writelines(valores)


if __name__ == '__main__':
    numero_repeticoes = int(input("Número de vezes para executar simulacao"))
    for i in range(numero_repeticoes):
        print(f"{i+1}° simulação")
        simulacao = Simulacao()
        simulacao.criar_agentes()
        simulacao.executar_modelo()
        print('---------------------------------------')
