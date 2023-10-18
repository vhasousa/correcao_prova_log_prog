"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 0/10 *não fez nenhum cálculo. Deveria somar as variáveis que continham as despesas e depois subtrair esse valor da renda mensal e chegaria ao resultado esperado
Utilizou condicionais: 5/10 *demonstrou entendimento do uso de condicionais, porém utilizou de forma incorreta
Utilizou estruturas de repetição: 0/10 
Fez tratativa de erros: 0/10 
Retornou mensagens de forma descritiva: 0/10
TOTAL: 15
"""

print ("Vamos calcular as suas despesas mensais")

nome = input("Digite seu nome")
Renda_Mensal = float(input("Digite quanto você gastou com renda mensal."))
Aluguel = float(input("Digite quanto você gastou com aluguel"))
Alimentação = float(input("Digite quanto você gastou com alimentação"))
Transporte = float(input("Digite quanto você gastou com Transporte"))
Saúde = float(input("Digite quanto você gastou em relação a saude"))
Educação = float(input("Digite quanto você gastou com sua educação"))
Entretenimento = float(input("Digite quando você gastou com seu entreterimento"))
Outras_despesas = float(input("Digite quanto gastou com outras despesas"))

if Aluguel  >= Renda_Mensal:
    print(f" {nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Alimentação >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Transporte >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Saúde >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Educação >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Entretenimento >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")

if Outras_despesas >= Renda_Mensal:
    print(f"{nome} Esta dentro do orçamento")
else:
    print(f"{nome} Esta fora do orçamento")
