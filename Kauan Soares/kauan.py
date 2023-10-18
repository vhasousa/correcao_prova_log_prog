"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 7/10 *na linha 98 você está comparando calculo == despesas, porém despesas é somente uma variável que armazena outras desepesas e não a soma de todas as despesas. O correto seria calculo == rendamensal
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 5/10 *mensagem informando a sobra retorna mesmo que não tenha sobrado nada. Linha 93 deveria estar dentro de alguma condicional
TOTAL: 52
"""

while True:
    try:
        rendamensal = float(input("Informe sua renda mensal.\n "))
        if rendamensal < 0:
            print("Por favor insira uma renda válida")
        else:    
            break
    except:
        print("Digite apenas numeros para sua renda mensal")

while True:
     try:
         aluguel = float(input("Digite o valor do aluguel.\n ")) 
         if aluguel < 0:
            print("Por favor insira novamente o valor do aluguel")
         else: 
            break
     except:  
        print("Digite apenas numeros no valor do aluguel") 

while True:
    try:
        alimentacao = float(input("Digite o valor da alimentacao.\n "))
        if alimentacao < 0:
            print("Por favor insira novamente o valor da alimentacao ")      
        else:
            break
    except:
        print("Digite apenas numeros no valor da alimentacao ") 

while True:
    try:
        transporte = float(input("Digite o valor do transporte.\n "))
        if transporte < 0:
            print("Por favor insira novamente o valor do transporte ")
        else:
            break
    except:
        print("Digite apenas numeros no valor do transporte")                

while True:
    try:
        saude = float(input("Digite o valor da saude.\n "))
        if saude < 0:
            print("Por favor insira novamente o valor da saude ")
        else:
            break
    except:
        print("Digite apenas numeros no valor da saude")

while True:
    try:
        educacao = float(input("Digite o valor da educação.\n "))
        if educacao < 0:
            print("Por favor insira novamente o valor da educação ")
        else:
            break
    except:
        print("Digite apenas numeros no valor da educação")

while True:
    try:
        entretenimento = float(input("Digite o valor do entretenimento.\n "))
        if entretenimento < 0:
            print("Por favor insira novamente o valor do entretenimento ")
        else:
            break
    except:
        print("Digite apenas numeros no valor do entretenimento")

while True:
    try:
        despesas = float(input("Digite o valor das despesas.\n"))
        if despesas < 0:
            print("Por favor insira novamente o valor das despesas ")
        else:
            break
    except:
        print("Digite apenas numeros no valor das despesas")

calculo = aluguel + alimentacao + transporte + saude + educacao + entretenimento + despesas
print(f"O que sobrou da sua renda apos o pagamento foi {calculo} reais")
resto = rendamensal- calculo

if calculo > rendamensal:
    print(f"você ultrapassou seu orçamento. ")
elif calculo == despesas:
    print("você está dentro do seu orçamento. ")
else:
    print(f"Você não ultrapassou seu orçamento, e sobrou {resto} reais para serem utilizados. ")
