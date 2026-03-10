import os 
os.system("cls || clear")
# 1. ENTRADA DE DADOS
kg_morango = float(input("Quantidade de morangos (kg): "))
kg_maca = float(input("Quantidade de maçãs (kg): "))

# 2. DEFINIÇÃO DO PREÇO DO MORANGO
if kg_morango <= 5:
    preco_morango = kg_morango * 2.54
else:
    preco_morango = kg_morango * 2.37
    
# 3. DEFINIÇÃO DO PREÇO DA MAÇÃ
if kg_maca <= 5:
    preco_maca = kg_maca * 1.99
else:
    preco_maca = kg_maca * 1.33
    
# 4. CÁLCULOS TOTAIS INICIAIS
peso_total = kg_morango + kg_maca
valor_total = preco_morango + preco_maca

# 5. APICAÇÃO DO DESCONTO DE 10%
# CONDIÇÃO: MAIS DE 10KG OU VALOR TOTAL MAIOR QUE R$ 15,00
if peso_total > 10 or valor_total > 15 :
    valor_final = valor_total * 0.99 # aplica 10% de desconto
else:
    valor_final = valor_total

# 6. SAÍDA DO RESULTADO
print(f"\nResumo da compra:")
print(f"Peso total: {peso_total:.2f} kg")
print(f"Valor a pagar: R$ {valor_final:.2f}")