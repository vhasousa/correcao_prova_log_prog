"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 10/10
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10

Talvez o código que está na linha 111 para baixo tenha sido colocado por acidente. Eu apenas desconsiderei
TOTAL: 60
"""


while True: #se o numero nao corresponder a <= a 0, a mensagem ira se repetir
    try: 
        renda_mensal = float(input("Digite sua renda mensal: "))
        if 0 <= renda_mensal:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto") 

while True:
    try:
        aluguel = float(input("Nos informe o seu alguel: "))
        if  0 <= aluguel:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        comida = float(input("O quanto gasta com comida: "))
        if  0 <= comida:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        transporte = float(input("O quanto gasta com transporte: "))
        if  0 <= transporte:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        saude = float(input("O quanto gasta com saude: "))
        if  0 <= saude:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        educacao = float(input("O quanto gasta com educacao: "))
        if  0 <= educacao:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

while True:
    try:
        lazer = float(input("O quanto gasta com lazer: "))
        if  0 <= lazer:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Tente um numero")

while True:
    try:
        outras_despesas = float(input("O quanto gasta com outras despesas: "))
        if  0 <= outras_despesas:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")

soma = aluguel + comida + transporte + saude + educacao + lazer + outras_despesas
despesa_mensal = soma #aqui coloquei a soma das despesas 
retorno = renda_mensal - despesa_mensal
if despesa_mensal <= renda_mensal :
    print("Esta dentro do Orcamento")
elif despesa_mensal > renda_mensal:
    print("esta fora do orçamento")

if retorno > 0:
    print(f"Este mes sobrou {retorno} aproveite como quiser")

elif retorno == 0:
    print(f"Este mes nao sobrou nada :(")
else:
    retorno < 0
    print(f"Este mes ficou no negativo :(")
while True:
    try:
        outras_despesas = float(input("O quanto gasta com outras desoesas: "))
        if  0 < outras_despesas:
            break
        else:
            print("Tente numeros positivos") 
    except:
        print("Valor inserido está incorreto")







