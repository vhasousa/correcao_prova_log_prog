"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 10/10 * apenas cuidado, pois pode acontecer da pessoa, por exemplo, na despesa com outros não ter nada, ou seja, 0 e com a validação > 0 não permite a entrada 0
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10
TOTAL: 60
"""

nome1 = input("Insira seu nome: ")
while True:
    try:
        renda_mensal = float(input("Por favor insira sua renda mensal: "))
        if renda_mensal > 0:
            break
        else:
            print("Apenas números positivos por favor.")

    except:
            print("Insira apenas números por favor.")


while True:
    try:
        aluguel = float(input("Quanto é o seu aluguel? "))
        if aluguel > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
            print("Digite apenas valores numéricos por favor.")

while True:
    try:
        alimentacao = float(input("Quanto você gasta com alimentação? "))
        if alimentacao > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")

while True:
    try:
        transporte = float(input("Quanto você gasta com transporte? "))
        if transporte > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")

while True:
    try:
        saude = float(input("Quanto você gasta com saúde? "))
        if saude > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")

while True:
    try:
        educacao = float(input("Quanto você gasta com educação? "))
        if educacao > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")

while True:
    try:
        entreterimento = float(input("Quanto você gasta com entreterimento? "))
        if entreterimento > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")

while True:
    try:
        outras_despesas = float(input("Quanto você gasta com outras dispesas? "))
        if outras_despesas > 0:
            break
        else:
            print("Digite apenas números positivos.")
    except:
        print("Digite somente números por favor.")


totaldedespesas = (aluguel + alimentacao + transporte + saude + educacao + entreterimento + outras_despesas)
if renda_mensal > totaldedespesas:
    print("Você esta com uma renda acima das suas dispesas mensais, parabéns por economizar")
elif renda_mensal < totaldedespesas:
    print("Suas dispesas estão muito altas, revise seus gastos e veja se são realmente nescessários!")
else:
    print("Você cobriu seus gastos mas atenção .")

sobras_faltas = (renda_mensal - totaldedespesas)
if sobras_faltas > 0:
    print("Este é o valor que sobrou de sua renda: ", sobras_faltas)
elif sobras_faltas < 0:
    print("Isto é o que você ainda deve em despesas: ", sobras_faltas)
else:
    print("Você não tem saldo e tambem não deve nada.")