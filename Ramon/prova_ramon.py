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

print("Vamos calcular suas despesas mensais e saber se você está dentro ou fora do seu orçamento")

renda_mensal = 0
aluguel = 0
alimentacao = 0 
transporte = 0
saude = 0
educacao = 0
entretenimento = 0
outras_despesas = 0
total_gastos = 0

def gasto(gasto1, gasto2, gasto3, gasto4, gasto5, gasto6, gasto7 ): #Essa função calcula todas as despesas do usuário
    return gasto1 + gasto2 + gasto3 + gasto4 + gasto5 + gasto6 + gasto7 

def diferenca( renda, gasto ): # Essa função faz o cálculo dos gastos sobre a renda do usuario
    return renda - gasto

#Essa parte pede que o usuario informe o valor da sua renda mensal, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        renda_mensal = float(input("Informe sua renda mensal! "))
        if renda_mensal >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")

#Essa parte pede que o usuario informe o valor do seu aluguel, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        aluguel = float(input("Informe o valor do seu aluguel! "))
        if aluguel >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com alimentação, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        alimentacao = float(input("Informe quanto você gasta com alimentação! "))
        if alimentacao >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com transporte, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        transporte = float(input("Informe quanto você gasta com transporte! "))
        if transporte >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com saúde, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        saude = float(input("Informe quanto você gasta com saúde! "))
        if saude >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com educação, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        educacao = float(input("Informe quanto você gasta com educação! "))
        if educacao >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com entretenimento, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        entretenimento = float(input("Informe quanto você gasta com entretenimento! "))
        if entretenimento >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")
#Essa parte pede que o usuario informe o valor gasto com outras despesas, e cuida para que ele não adicione nenhuma informação errada!
while True:
    try:
        outras_despesas = float(input("Informe quanto gastou com despesas extras! "))
        if outras_despesas >= 0:
            break
        else: 
            print("O valor inserido está incorreto! ")
    except:
        print("O valor inserido está incorreto!")

total_gastos = gasto(aluguel, alimentacao, transporte, saude, educacao, entretenimento, outras_despesas)

troco = diferenca(renda_mensal, total_gastos)

if total_gastos < renda_mensal:
    print("Você está dentro do orçamento")
    print(f"E sobrou do seu orçamento R${troco} ! Aproveite como quiser, ou guarde para investimentos")

elif  total_gastos == renda_mensal:
    print("Você está dentro do orçamento! Porém não sobrou para possíves emergências, tome cuidado! ") 

else:
    print("Você está fora do orçamento!")
    print(f"E faltou do seu orçamento R${troco} ! Cuida para não perder o controle! ")

