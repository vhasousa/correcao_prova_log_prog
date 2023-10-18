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
    rendamensal = float(input("Informe sua renda mensal.\n"))
    if rendamensal <= 0:
      print("Por favor digite uma renda valida.")
    else:
      break
  except:
    print("Digite apenas números para sua renda mensal")

while True:
  try:
    aluguel = float(input("Digite o valor do seu aluguel\n"))
    if aluguel < 0:
      print("Por favor digite o valor certo do aluguel.")
    else:
      break
  except:
    print("Digite apenas números para o valor do aluguel.")

while True:
  try:
    alimento = float(
        input("Digite o valor gasto mensalmente com alimentação.\n"))
    if alimento < 0:
      print("Digite valores validos para seu gasto com alimentação.")
    else:
      break
  except:
    print("Digite apenas números para p valor da alimentação.")

while True:
  try:
    transporte = float(
        input("Digite o valor gasto mensalmente com locomoção.\n"))
    if transporte < 0:
      print("Digite valores validos para seu gasto com locomoção.")
    else:
      break
  except:
    print("Digite apenas números para p valor da locomoção.")

while True:
  try:
    saude = float(input("Digite o valor gasto mensalmente com saude.\n"))
    if saude < 0:
      print("Digite valores validos para seu gasto com saude.")
    else:
      break
  except:
    print("Digite apenas números para para valor da saude.")

while True:
  try:
    educação = float(input("Digite o valor gasto mensalmente com educação.\n"))
    if educação < 0:
      print("Digite valores validos para seu gasto com educação.")
    else:
      break
  except:
    print("Digite apenas números para para valor da educação.")

while True:
  try:
    entreterimento = float(
        input("Digite o valor gasto mensalmente com entreterimento.\n"))
    if entreterimento < 0:
      print("Digite valores validos para seu gasto com entreterimento.")
    else:
      break
  except:
    print("Digite apenas números para para valor da entreterimento.")

while True:
  try:
    Odespesas = float(
        input("Digite o valor gasto mensalmente com outras despesas.\n"))
    if Odespesas < 0:
      print("Digite valores validos para seu gasto com outras despesas.")
    else:
      break
  except:
    print("Digite apenas números para para valor da outras despesas.")

calculo = aluguel + alimento + transporte + saude + educação + entreterimento + Odespesas
print(f"Sua despesa esse mes foi de {calculo} reais.")
resto = rendamensal - calculo

if calculo > rendamensal:
  print(f"Você estourou seu orçamento em {resto} regule mais seus gastos.")
elif calculo == rendamensal:
  print("Você esta dentro do seu orçamento.")
else:
  print(
      f"Você não ultrapassou sua renda mensal parabens, e sobrou {resto} reais para utilizar como quiser.")

