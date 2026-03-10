import os
os.system("cls || clear")
 # 1. ENTRADA DE DADOS
nome_produto = input("Descrição do produto (nome): ")
quantidade = int(input(f"Quantidade adquirida de {nome_produto}: "))
preco_unitario = float(input("Preço unitário: R$ "))

# 2. CÁLCULO DO TOTAL BRUTO
total_bruto = quantidade * preco_unitario

# 3. ESTRUTURA DE DECISÃO PARA O DESCONTO
if quantidade <= 5:
    porcentagem_desconto = 0.03 # 3%
elif quantidade <= 10:
    porcentagem_desconto = 0.05 # 5%
else:
    porcentagem_desconto = 0.07 # 7%
    
# 4. CÁLCULOS FINAIS 
valor_desconto = total_bruto * porcentagem_desconto
total_a_pagar = total_bruto - valor_desconto

# 5. EXIBIÇÃO DIS RESULTADOS
print(f"\n--- Resumo da Compra: {nome_produto} ---")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto * 100:.0f}% (R$ {valor_desconto:.2f})")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
