import os 
os.system("cls || clear")

# ENTRADA DE DADOS 
cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").lower()

# ESTRUTURA DE DECISÃO (SELEÇÃO MÚLTIPLA)
if cor == "verde":
    preco = 25.00
elif cor == "azul":
    preco = 50.00
elif cor == "amarelo":
    preco = 150.00
elif cor == "vermelho":
    preco = 250.00
else:
    preco = None
    
# EXIBIÇÃO DO RESULTADO:
if preco is not None:
    print(f"O preço do CD selecionado é: R$ {preco:.2f}")
else:
    print("Cor inválida! Por favor, escolha uma cor da table.")
    