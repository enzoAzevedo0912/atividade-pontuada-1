import os 
os.system("cls || clear")

# ENTRADA DE DADOS
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# PROCESSAMENTO E SAIDA
soma = A + B 

if soma < C:
    print(f"A soma de A + B ({soma}) é maior que C ({C}).")
elif soma > C:
    print(f"A soma de A + B ({soma}) é maior que c ({C}).")
else:
    print(f"A soma de A + B ({soma}) é extamente igual a C ({C}).")