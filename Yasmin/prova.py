"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 9/10 *faltou colocar a variável educação no cálculo
Utilizou condicionais: 10/10 *Uma despesa pode ser 0. Ao utilizar > 0 não é permitido input 0 obrigando a pessoa a ter alguma despesa, nem que seja 1, atrapalhando o cálculo. Apenas um detalhe. Não tirei ponto pois demonstrou entendimento do uso de if
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10 *na mensagem na linha 90 poderia ter colocado que faltou e não sobrou. Apenas um detalhe. Não tirei ponto por isso
TOTAL: 59
"""

while True:
    try:    
        renda= float(input("Digite sua renda mensal:"))
        if renda > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        aluguel= float(input("Digite o valor do seu aluguel ou moradia :"))
        if aluguel > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")

while True:
    try:    
        alimentacao= float(input("Digite o valor que você gasta com alimentação mensalmente:"))
        if alimentacao > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        transporte= float(input("Digite o valor do seu transporte mensalmente:"))
        if transporte > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        saude= float(input("Digite o valor que você gasta com a saúde mensalmente:"))
        if saude > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        educacao= float(input("Digite o valor do gasto com educacao mensalmente:"))
        if educacao > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        entreterimento= float(input("Digite o valor do que você gasta com entreterimento mensalmente:"))
        if entreterimento > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
while True:
    try:    
        outras_despesas= float(input("Digite o valor do seu gasto com outras despesas:"))
        if outras_despesas > 0 : 
            break
        else:
            print("Você digitou um número inválido. Tente apenas números inteiros e positivos." )
    except:
            print("Número inválido.")
despesa =(aluguel + alimentacao + transporte + saude + entreterimento + outras_despesas) 
orcamento = (renda - despesa)  
if renda >= despesa:
    print(f"Com a renda mensal de R${renda} e uma despesa de R${despesa},sobrou R${orcamento}. Você está dentro do orçamento.") 
else:
   print(f"Com a renda mensal de R${renda} e uma despesa de R${despesa},sobrou R${orcamento}. Você está acima do orçamento.") 
