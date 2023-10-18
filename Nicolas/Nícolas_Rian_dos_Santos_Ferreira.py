"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 10/10
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10
TOTAL: 60
"""

nome = input("Digite seu nome: ")
while True:
    try:
        renda_mensal = float(input("Digite sua Renda mensal: "))
        if renda_mensal >= 0:
             break
        else:
            print("Valor invalido. Digite uma renda maior que 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        aluguel_moradia = float(input("Digite seu gasto com moradia: "))
        if aluguel_moradia >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        alimentaçao = float(input("Digite seu gasto com alimentação: "))
        if alimentaçao >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maio ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        transporte = float(input("Digite seu gasto com trasnporte: "))
        if transporte >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        saude = float(input("Digite seu gasto com saude: "))
        if saude >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        educaçao = float(input("Digite seu gasto em educaçao "))
        if educaçao >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        entretenimento  = float(input("Digite seu gasto em entretenimento "))
        if entretenimento >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior que ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

while True:
    try:
        outras_despesas = float(input("Digite os gasto de outras despesas: "))
        if outras_despesas >= 0:
             break
        else:
            print("Valor invalido. Digite um gasto maior que ou igual a 0.")
    except:
        print("O valor inserido não é valido!")

total_despesas = (aluguel_moradia + alimentaçao + transporte + saude + educaçao + entretenimento + outras_despesas)
print(f"O total de sua despesas é de {total_despesas}")

if total_despesas <= renda_mensal:
    print("Você está dentro do orçamento.")
else:
    print("Você está fora do orçamento.")

retorno = renda_mensal - total_despesas
if retorno >= 0:
    print(f"Com uma renda de R${renda_mensal} e uma despesa de R${total_despesas}, este mês sobrou R${retorno}. Aproveite como quiser, ou guarde para investimentos ")
else:
    print(f"Com uma renda de R${renda_mensal} e uma despesa de R${total_despesas} este mês você teve uma divida de {retorno}. ")








