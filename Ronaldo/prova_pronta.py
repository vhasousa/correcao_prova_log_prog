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
        renda = float(input("qual sua renda mensal: "))
        if renda >= 0:
            break
        else:
            print("renda inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        aluguel = float(input("qual o seu aluguel: "))
        if aluguel >= 0:
            break
        else:
            print("aluguel inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        alimentação = float(input("quanto voce gasta com alimentação: "))
        if alimentação >= 0:
            break
        else:
            print("valor de alimentação inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        transporte = float(input("quanto voce gasta com transporte: "))
        if transporte >= 0:
            break
        else:
            print("valor de transporte inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        saúde = float(input("quanto voce gasta com saúde: "))
        if saúde >= 0:
            break
        else:
            print("valor de saúde inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        educação = float(input("quanto voce gasta com educação: "))
        if educação >= 0:
            break
        else:
            print("valor de educação inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        entretenimento = float(input("quanto voce gasta com entretenimento: "))
        if entretenimento >= 0:
            break
        else:
            print("valor de entretenimento inválida") 
    except:
        print("Valor inserido está incorreto")


while True:
    try:
        outras_despesas = float(input("quanto voce gasta com outras_despesas "))
        if outras_despesas >= 0:
            break
        else:
            print("valor de outras_despesa inválida") 
    except:
        print("Valor inserido está incorreto")

despesas = aluguel + alimentação + transporte + saúde + educação + entretenimento + outras_despesas
print(f"o total das despesas é de {despesas} por mês")

sobra = renda - despesas
if despesas == renda:
    print(f"sobrou {sobra} e o usuario está dentro do orçamento")

else:
    print(f"sobrou {sobra} e o usuario está acima do orçamento")



