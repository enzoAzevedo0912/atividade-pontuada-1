import os 
os.system("cls || clear")

# 1. ENTRADA DE DADOS
renda_mensal = float(input("Digite sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor total do emprestimo: R$ "))
num_prestacoes = int(input("Digite a quantidade de prestações: "))

# 2. CÁLCULOS DE VERIFICAÇÃO
limite_total = renda_mensal * 10
valor_prestacao = valor_emprestimo / num_prestacoes
limite_prestacao = renda_mensal * 0.44

# 3. ESTRUTURA DE DECISÃO (CONDICIONAL COMPOSTA)
print("\n--- Resultado da Análise ---")

if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("Emprestimo CONCEDIDO!")
    print(f"O valor da prestação será de R$ {valor_prestacao}:.2f")
else:
    print("Emprestimo NEGADO.")

 # FEEDBACK DO MOTIVO ( OPCIONAL, MAS AMIGÁVEL)
if valor_emprestimo > limite_emprestimo:
     print(f"- O valor total excede o limite de R$ {limite_emprestimo:.2f} (10x a renda). ")
if valor_prestacao > limite_prestacao:
    print(f"- A prestação de R$ {valor_prestacao:.2f} excede 30% da sua renda (R$ {limite_prestacao:.2f}).")