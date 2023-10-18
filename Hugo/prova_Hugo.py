"""
Criou variáveis descritivas: 5/5
Aplicou o uso de input corretamente: 2,5/5 *input deveria ser float
Realizou os cálculos corretamente: 10/10
Utilizou condicionais: 7/10 *ao verificar se o que sobrou é maior ou igual a renda mensal, sempre dará um valor falso. Nunca o que sobrou será maior que a renda mensal, a pessoa sempre irá gastar alguma coisa
Utilizou estruturas de repetição: 10/10 
Fez tratativa de erros: 10/10 
Retornou mensagens de forma descritiva: 10/10
TOTAL: 54,5
"""

nome = input("Informe o nome do cidadão: ")
while True:
      try:
       renda_mensal = int(input("informe a renda mensal: "))
       if renda_mensal > 0:
          break
      except:
       print("Valor inserido esta incorreto")

while True:
  try:
   aluguel = int(input("informe o aluguel: "))
   if aluguel >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

while True:
  try:
   alimentação = int(input("informe o valor gasto com alimentação: "))
   if alimentação >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

while True:
  try:
   transporte = int(input("informe o valor gasto com transporte: "))
   if transporte >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

while True:
  try:
   saude = int(input("informe o valor gasto com saude: "))
   if saude >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

while True:
  try:
   educação = int(input("informe o valor gasto com educação: "))
   if educação >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

while True:
  try:
   outras_despesas = int(input("informe o valor gasto com outras despesas: "))
   if outras_despesas >= 0:
      break
  except:
   print("Valor inserido esta incorreto")

sobrou = renda_mensal - (aluguel + alimentação + transporte + saude + educação + outras_despesas)

if sobrou >= renda_mensal:
  print(f"O cidadão {nome} está abaixo do orçamento {sobrou}, reveja seus conceitos")
else:
  print(f"O cidadão {nome} está acima do orçamento {sobrou}, parabéns!")