"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 2,5/5 *input deveria ser float
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 10/10
Utilizou estruturas de repetição: 8/10 *demonstrou entendimento no uso da estrutura de repetição, porém deveria utilizar em cada input para que o usuário não tenha que ver o erro somente no final da execução
Fez tratativa de erros: 5/10 *Fez a tratativa estruturada corretamente, mas de forma que compromete e usabilidade
Retornou mensagens de forma descritiva: 10/10
TOTAL: 50,5
"""

from os import system
system("cls")
while True:
    try:
        renda_mensal = int(input("Informe sua Renda mensal: "))
        aluguel = int(input("Informe o custo de Aluguel/Moradia: "))
        alimentacao = int(input("Informe o quanto gasta Alimentaçâo: "))
        transporte = int(input("Informe o quanto gasta Transporte: "))
        saude = int(input("Informe o quanto gasta com  Saúde: "))
        educacao = int(input("Informe o quanto gasta Educação: "))
        entreterimento = int(input("Informe o quanto gasta Entreterimentos: "))
        outros = int(input("Informe o custo de outras dispesas: "))
        soma_despesa = aluguel + alimentacao + transporte + saude + educacao + entreterimento + outros
        if renda_mensal >= 0 and aluguel >= 0 and alimentacao >= 0 and transporte >= 0 and saude >= 0 and educacao >= 0 and entreterimento >= 0 and outros >= 0:
            break
        else:
            print("Valor inseridos invalido!\nTente novamente!")
    except:
        print("Valor inserido incorreto!\nTente novamente")

sobrou_no_mes = renda_mensal - soma_despesa
if soma_despesa <= renda_mensal:
    print(f"Com uma renda mensal de {renda_mensal} e com uma despesa de {soma_despesa}, este mês sobrou R${sobrou_no_mes} e ficou abaixo do orçamento. Aproveite como quiser, ou guarde para investimentos.")
else:
    print(f"Com uma renda mensal de {renda_mensal} e com uma despesa de {soma_despesa}, este mês ficou acima do orçamento.")

