import os
os.system("cls || clear")

# 1. LEITURA DOS DADOS
operacao = input("Digite a operação (+, -, *, /): ")
A = int(input("Digite o valor de A (inteiro): "))
B = int(input("Digite o valor de B (inteiro): "))

# 2. ESTRUTURA DE DECISÃO PARA CALCULAR O RESULTADO
if operacao == '+':
    resultado = A + B
elif operacao == '-':
    resultado = A - B
elif operacao == '*':
    resultado = A * B
elif operacao == '/':
    #VERIFICAÇÃO PARA EVITAR DIVIÃO POR ZERO
    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro! Divisão por zero não permitida."
else:
    resultado = "Operação inválida!"
    
# 3. EXIBIÇÃO DO RESULTADO
print(f"Resultado: {resultado}")
    