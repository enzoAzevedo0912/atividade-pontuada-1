import os
os.system("cls || clear")

# ENTRADA DE DADOS 
litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper ()

# PREÇOS BASE
preco_gasolina = 5.78
preco_alcool = 3.99

valor_total = 0 

# PROCESSAMENTO DA GASOLINA
if tipo == 'G':
    desconto = 0.06 # 6%
else:
    desconto = 0.07 # 7%
valor_total = litros * (preco_gasolina * (1 - desconto))

# PROCESSAMENTO DE ALCOOL 
if tipo == 'A':
    desconto = 0.04 # 4%
else: 
    desconto = 0.02 # 2%
valor_total = litros * (preco_alcool * (1- desconto))

else:
    print("Tipo de combustível inválido!")
    
# SAÍDA DO RESULTADO
if valor_total > 0:
    print(f"Valor a ser pago: R$ {valor_total:.2f}")