import os
os.system("cls || clear")

# ENTRADA DE DADOS (convertendo para inteiros)
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# ESTRUTURA DE DECISÃO
if A == B:
    C = A + B
    operacao = "soma"
else: 
    C = A * B
    operacao = "multiplicação"
    
# SAÍDA DO RESULTADO
print(f"Os valor são {'iguais' if A == B else 'diferentes'}.")
print(f"O resultado da {operacao} é: {C}")