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

while True:
    try:
        renda_mensal = float(input("Informe sua renda mensal:"))
        if renda_mensal >=0:
            break
        else:
            print("Apenas zero e números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        aluguel_moradia = float(input("Informe sua renda gasta com alugel e moradia:"))
        if aluguel_moradia >=0:
            break
        else:
            print("Apenas zero enúmeros positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        alimentação = float(input("Informe sua renda gasta com alimentação:"))
        if alimentação >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        transporte = float(input("Informe sua renda gasta com transporte:"))
        if transporte >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        saúde = float(input("Informe sua renda gasta com saúde:"))
        if saúde >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        educação = float(input("Informe sua renda gasta com educação:"))
        if educação >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        entreterimento = float(input("Informe sua renda gasta com lazer:"))
        if entreterimento >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

while True:
    try:
        outras_despesas = float(input("Informe qualquer outra renda que não foi citada acima:"))
        if outras_despesas >=0:
            break
        else:
            print("Apenas zero números positivos serão aceitos") 
    except:
        print("O valor inserido é inválido")

despesas = (aluguel_moradia + alimentação + transporte + saúde + educação + entreterimento + outras_despesas)


if despesas <= renda_mensal:
    print(f"Parabéns!Você está dentro do orçamento.Suas despesas deram R${despesas}.Este mês sobrou R${renda_mensal-despesas}.")
else: 
    print(f"Fique atento!Você se encontra acima do orçamento.Suas despesas esse mês deram R${despesas}.Você excedeu limite em R${despesas-renda_mensal}")