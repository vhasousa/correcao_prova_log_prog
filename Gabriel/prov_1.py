"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 5/5
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 0/10 *UTILIZOU PORÉM DE FORMA INCORRETA. NENHUMA VALIDAÇÃO FUNCIONOU, MESMO COM VALORES INCORRETOS, A CONDICIONAL DEIXA PASSAR.
Utilizou estruturas de repetição: 10/10
Fez tratativa de erros: 0/10 *Fez a tratativa estruturada corretamente, mas mesmo com erros no input, o código deixa passar.
Retornou mensagens de forma descritiva: 10/10
TOTAL: 40
"""

renda_mesal= float(input('qual o valor da sua renda mesal:'))
while True:
    try:
        alugue_moradia= float(input('insira o valor do seu aluguel/moradia:'))
        if alugue_moradia >=0 and alugue_moradia:
            break
        else:
            print('falor incorreto digite falor positivo')
    except:
        print(" valor invalido ")

while True:
    try:
        alimentação= float(input('digite o valor da sua alimentação'))
        if alimentação>=0 or alimentação:
            break
        else:
            print('valor incorreto digite falor maior 0')
    except:
        print(' valor ivalido')

while True:
    try:
        transport= float(input('valor do transporte:'))
        if transport >=0 or transport:
            break
        else:
            print('valor incorreto tende valor positivo')
    except: 
        print(' valor incorreto ')

while True:
    try:
        educação= float( input('digite o valor da escola:'))
        if educação >=0 or educação:
            break
        else:
            print('valor incorreto tende valor positivo')
    except:
        print('valor incorreto')
while True:
    try:
        entreterimendo  = float(input('digite o valor od entreterimendo:'))
        if entreterimendo >=0 or entreterimendo:
           break
        else:
            print('valor incorreto tende valor positivo') 
    except:
        print('valor invalido')

while True:
    try:
        outras_despesas= float(input('digite o valor da despesas estras:'))
        if outras_despesas>=0 or outras_despesas:
            break
        else:
            print('valor incorreto tende valor positivo')
    except:
        print('valor invalido')

despesa = (alugue_moradia + transport + educação + entreterimendo + outras_despesas + alimentação)
sobra = renda_mesal - despesa

if renda_mesal >= 0 :
    print(f'com uma renda mensal de {renda_mesal} e uma despesa de {despesa}, ira sobra {sobra} ')
else:
    print(f'voce esta abaixo da sua renda mensal {renda_mesal}')



    





"""alugue_moradia= float(input('insira o valor do seu alugue/moradia:'))
transport= float(input('valor do transporte:'))
educação= float( input('digite o valor da escola:'))
entreterimendo = float(input('insira o valor do intreterimendo: '))
outras_despesas= float(input('despesas extra:'))
despesa = (alugue_moradia + transport + educação + entreterimendo + outras_despesas)
sobra= renda_mesal - despesa
print(f'com uma renda mensal de {renda_mesal} e uma despesa de {despesa}, ira sobra {sobra} ')"""