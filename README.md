# Mestrado Profissional em Políticas Públicas e Desenvolvimento
# Instituto de Pesquisa Econômica Aplicada - Ipea
# Disciplina: Python para Modelagem Baseada em Agentes
# Professor: Bernardo Alves Furtado
# Aluno: Willian Costa Araujo
# Turma: MPPPD 4 Turma - IPEA
## Trabalho Final

## ABM - Projeto

Pergunta: É possivel mensurar a satisfação do cliente bancarizado com
base numa simplificação usando o tripé: preço da tarifa de manutenção
de conta, valor da anuidade do cartão e qualidade do atendimento?

Hipótese I: o cliente bancarizado brasileiro apresenta índices de
satisfação, na média, superiores a 70%.

Hipótese II: não são percebidas grandes discrepâncias na troca de banco, 
idependente da faixa de renda do cliente.    

## ABM é adequado para a pergunta?

Sim. É possivel, observar o grau de satisfação dos clientes por meio
das interações das classes que representam os produtos e serviços bancários, com razoável
precisão, quando considerados os resultados obtidos pela pesquisa
realizada pela opinionbox em 2018.

### Agentes
a) Bancos (id, tarifa, anuidade, qualidade)

b) Clientes (id, resiliencia_tarifa, resiliencia_anuidade,
resiliencia_qualidade, banco, pesos, conta)

c) Contas (id, saldo)

OBS: Os pesos foram utilizados usando dicionários em python

### Ambiente

Relacionamento do Cliente com o seu banco (seja de forma física ou
virtual). De acordo com as expectativas prévias do cliente com relação
ao que ele espera gastar e com a qualidade mínima do atendimento que
ele espera receber, atribui-se um escore para a satisfação do cliente
(0 a 10).

### Regras das ações

Criamos ações simultâneas, probabilísticas, de caráter randômico,
com limites previamente estabelecido para cada um dos elementos
(tarifa, anuidade e qualidade do atendimento).

### Comportamento

- Satisfação média dos clientes com os bancos;
- Quantidade de clientes insatisfeitos (nível de satisfação de 0 a 3) que trocam de bancos.

### Resposta do Modelo

- Comportamento (satisfação) do cliente frente ao seu gasto mensal com
tarifa de conta, anuidade do cartão e qualidade do atendimento
percebida com o seu banco.

A saída é dada com o seguinte layout:

Informação consolidada dos clientes por cada simulção*

```
# Exemplo
3° simulação
Faixa de renda de  9706
Satisfacao maior que 7:  812
Satisfacao maior que 3 e menor que 7:  176
Satisfacao maior que 0 e menor que 3:  48
--------------------------------------------------
Faixa de renda de  3422
Satisfacao maior que 7:  1577
Satisfacao maior que 3 e menor que 7:  371
Satisfacao maior que 0 e menor que 3:  11
--------------------------------------------------
Faixa de renda de  1871
Satisfacao maior que 7:  5548
Satisfacao maior que 3 e menor que 7:  1381
Satisfacao maior que 0 e menor que 3:  76
--------------------------------------------------

Resultados consolidados dessa simulação: 

Média de satisfação:  7.94
Satisfação maior que 7:  7937
Satisfação maior que 3 e menor que 7:  1928
Satisfação maior que 0 e menor que 3:  135
Clientes que trocaram de banco:  98
---------------------------------------
```
*Satisfação de 0 a 10.

#### Arquivos gerados

São gerados dois arquivos CSV contendo os dados obtidos pela simulação, sendo eles: resultado.csv e satisfacao_por_renda.csv.
Ambos, armazenam os resultados da última simulação executada. 
 
### Calibração e Validação

I) Usamos essa [pesquisa](https://www.nexojornal.com.br/expresso/2020/05/11/A-desigualdade-de-renda-no-Brasil-%C3%A9-alta.-E-vai-piorar) para estabelecer 3 perfis de clientes:

a) 10% dos clientes com renda acima de R$ 9.706,00;

b) 20% dos clientes com renda entre R$ 1.871,00 e R$ 3.422,00;

c) 70% dos clientes com renda até R$ 1.871.00.

II) Pesquisa exclusiva sobre bancos: [perfil dos bancarizados no Brasil](https://blog.opinionbox.com/pesquisa-exclusiva-bancarizados-no-brasil/)

O principal dado dessa pesquisa que nos interessa saber é replicarmos
no modelo uma média de 70% dos clientes satisfeitos com seus bancos,
mesmo considerando que mais de 70% da população tem renda média abaixo
de 2 salários mínimos e que as despesas com serviços e produtos
bancários no Brasil são relativamente pesadas no orçamento de grande
parte do público que atende.

***Dados utilizados para definir dados dos bancos:***
Da mesma pesquisa citada acima no item II, retiramos os índices dos 3
itens e os aplicamos a construção da classe "banco" na expectativa de oferecer melhor
calibragem ao modelo.

Dados:
- 68% tarifas
- 62% anuidade
- 44% qualidade do atendimento

Classe:
```python
class Banco:

    def __init__(self, id):
        self.id = id
        self.tarifa = random.randint(10, 50)*1.68 # Valor em reais
        self.anuidade = random.randint(10, 500)*1.62 # Valor em reais
        self.qualidade = random.randint(1, 10)*1.44 # Qualidade do atendimento
```

# Sugestões/Recomendações

Para ficar mais próximo aos dados da pesquisa, usamos apenas 10 bancos
e um nr limitado de clientes(apenas 10.000). Considerando que há mais
de 100 milhões de correntistas no Brasil, o modelo pode falhar para um
contingente grande de clientes.
Qualquer alteração nas premissas do modelo (pesos das variáveis,
utilização de outros percentis de faixa de renda, entre outros) podem
afetar drasticamente o resultado.

# Conclusão

Considerando um modelo simplificado, com dados gerados aleatoriamente, 
foi possível obervar que, usando os critérios de taxa de manutenção de conta, 
qualidade de atendimento e valor de anuidade, a satisfação dos clientes fica acima de 70%
e que a quantidade de clientes que trocam de banco não apresenta grande variação entre 
as três faixas de renda simuladas no exercício. 
