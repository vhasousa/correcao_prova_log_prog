"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 8/10 *Não calculou o quanto sobrou ou faltou
Utilizou condicionais: 7/10 *demonstrou entendimento do uso de condicionais, porém, a principal condicional que mostra se a pessoa ficou com dívida ou não, não foi criação.
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 5/10 *a mensagem principal não foi criada
TOTAL: 50
"""

nome = input("Informe o nome do usuário: ")
while True:
    try:
        renda = float(input("Informe a sua renda mensal: "))
        if renda >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
        
while True:
    try:
        Aluguel_e_moradia = float(input("informe o quanto gasta com alguel/moradia: "))
        if Aluguel_e_moradia >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Alimentação = float(input("informe o quanto gasta com alimentação: "))
        if Alimentação >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Transporte = float(input("informe o quanto gasta com transporte: "))
        if Transporte >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Saúde = float(input("informe o quanto gasta com saúde: "))
        if Saúde >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Educação = float(input("informe o quanto gasta com educação: "))
        if Educação >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Entreterimento = float(input("informe o quanto gasta com entreterimento: "))
        if Entreterimento >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")
while True:
    try:
        Outras_despesas = float(input("informe o quanto gasta com outras despesas: "))
        if Outras_despesas >= 0:
            break
        else:
            print("Valor inválido. Valores abaixo de 0 não são aceitos")
    except:
        print("Valor inválido")

Despesas = (Aluguel_e_moradia + Alimentação + Transporte + Saúde + Educação + Entreterimento + Outras_despesas)- renda
