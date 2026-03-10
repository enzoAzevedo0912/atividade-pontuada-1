import os 
os.system ("cls || clear")

# 1. ENTRADA DE NOTAS (USAMOS FLOAT PARA CEITAR NÚMEROS DECIMAIS)
notal = float(input("Digite a peirmeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. CÁLCULO DA MÉDIA ARTMÉTICA
media = (notal + nota2) / 2

# 3. EXIBIÇÃO DA MÉDIA 
print(f"\nMédia final: {media:.1f}")

# 4. ESTRUTURA DE DECISÃO PARA O STATUS DO ALUNO
if media >= 6.0:
    print("Parabens! Voce está APROVADO!")
elif media >= 4.0:
    print("O aluno está de RECUPERAÇÃO.")
else:
    print("O aluno está REPROVADO.")
    