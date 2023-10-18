
"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5 
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 7/10 * na linha 82 utilizou comparação desnecessária no else. else é só utilizado quando nada é verdadeiro, logo não se utiliza comparação nenhuma. Além disso, a mensagem que está na linha 85 deveria estar dentro de um if, pois ela será exibida mesmo que a pessoa ultrapasse o seu orçamento
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 7/10 * faltaram os detalhes solicitados na descrição da prova. Volta para o erro citado na linha 6
TOTAL: 54
"""

while True:
    try:
        renda_mensal = float(input("Qual sua renda mensal? "))
        if renda_mensal > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:   
        aluguel = float(input("Qual seu gasto com aluguel? "))
        if aluguel > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:
        alimentaçao = float(input("Qual seu gasto com alimentação? "))
        if alimentaçao > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:
        transporte = float(input("Qual seu gasto com transporte? "))
        if transporte > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:
        saude = float(input("Qual seu gasto com saúde? "))
        if saude > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:
        educaçao = float(input("Qual seu gasto com educação? "))
        if educaçao > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
while True:
    try:
        entretenimento = float(input("Qual seu gasto com entreterimento? "))
        if entretenimento > 0:
            break
        else:
            print ("O valor deve ser maior que zero.")
    except:
        print ("Por favor, digite um número valido.")
total_gastos = aluguel + alimentaçao + transporte + saude + educaçao + entretenimento
margem = renda_mensal - total_gastos

if total_gastos <= renda_mensal:
    print ("\nVocê está dentro do seu orçamento")
else: 
    total_gastos > renda_mensal
    print ("\nVocê está acima do seu orçamento")

print (f"\nCom uma renda mensal de R${renda_mensal} e uma despesa de R${total_gastos}, este mês sobrou R${margem}. Aproveite como quiser, ou guarde para investimentos.")