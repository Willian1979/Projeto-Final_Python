import random


class Banco:

    def __init__(self, id):
        self.id = id
        self.tarifa = random.randint(10, 50)*1.68 # Valor em reais
        self.anuidade = random.randint(10, 500)*1.62 # Valor em reais
        self.qualidade = random.randint(1, 10)*1.44 # Qualidade do atendimento


class Cliente:

    def __init__(self, id, banco, pesos):
        self.id = id
        self.resiliencia_tarifa = random.randint(10, 50) # Valor em reais
        self.resiliencia_anuidade = random.randint(10, 500) # Valor em reais
        self.resiliencia_qualidade = random.randint(5, 10) # Qualidade do atendimento
        self.banco = banco
        self.conta = Conta(id, pesos['renda'])
        self.pesos = pesos

    def escolhe_banco(self, bancos):
        banco_atual = self.banco
        for banco in bancos:
            if self.resiliencia_tarifa >= banco.tarifa and self.resiliencia_anuidade >= banco.anuidade \
                    and self.resiliencia_qualidade >= banco.qualidade:
                self.banco = banco
                break

        if banco_atual == self.banco:
            for banco in bancos:
                num_requisitos = int(self.resiliencia_tarifa >= banco.tarifa) + int(self.resiliencia_anuidade >= banco.anuidade)\
                                + int(self.resiliencia_qualidade >= banco.qualidade)
                if num_requisitos == 2:
                    self.banco = banco
                    break

        if banco_atual == self.banco:
            return 0
        return 1

    def verifica_tarifa(self):
        experiencia = 10
        if self.resiliencia_tarifa < self.banco.tarifa:
            insatisfacao = self.banco.tarifa/self.resiliencia_tarifa
            experiencia -= insatisfacao
            experiencia = int(experiencia)
        return experiencia

    def verifica_anuidade(self):
        experiencia = 10
        if self.resiliencia_anuidade < self.banco.anuidade:
            insatisfacao = self.banco.tarifa/self.resiliencia_tarifa
            experiencia -= insatisfacao
            experiencia = int(experiencia)
        return experiencia

    def verifica_qualidade(self):
        experiencia = 10
        if self.resiliencia_qualidade > self.banco.qualidade:
            insatisfacao = self.resiliencia_qualidade - self.banco.qualidade
            experiencia -= insatisfacao
            experiencia = int(experiencia)
        return experiencia


class Conta:

    def __init__(self, id, saldo=0):
        self.id = id
        self.saldo = saldo
