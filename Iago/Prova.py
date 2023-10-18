
"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 2,5/5 *input deveria ser float
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 10/10 *pode ter alguma despesas em que a pessoa não gastou nada. Ao colocar menor ou 0 (<=) na validação você impossibilita a pessoa de não informar essa despesa.
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10
TOTAL: 55,5
"""

while True:
    try:
        renda = int(input("Informe sua Renda mensal: "))

        if renda <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        aluguel = int(input("Informe seus gastos de moradia: "))

        if renda <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        alimentacao = int(input("Informe seus gastos de alimentação: "))

        if renda <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        transporte = int(input("Informe seus gastos de transposte: "))

        if transporte <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        saude = int(input("Informe seus gastos de saúde: "))

        if saude <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        educacao = int(input("Informe seus gastos de educação: "))

        if educacao <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        entretenimento = int(input("Informe gastos de entretenimento: "))

        if entretenimento <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        outras_despesas = int(input("Informe gastos de outras despesas: "))

        if outras_despesas <= 0:
            print("Valor inserido está incorreto")
        else:
            break
    except:
        print("Valor inserido está incorreto")

calculo_despesas = (aluguel + alimentacao + transporte + saude + educacao + entretenimento + outras_despesas) 
valor = renda - calculo_despesas

if calculo_despesas >= renda :
    print(f"O usuario ficou fora do orçamento, faltando R${valor} ")
else:
    print(f"O usuario ficou acima do orçamento, R${valor} para investimentos.")




