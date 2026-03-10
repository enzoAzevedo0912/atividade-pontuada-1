import os
os.system("cls || clear")

# ENTRADA DE DADOS BÁSICOS 
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F):").upper()
estado_civil = input("Digite o estado civil: ").upper()

# CONDIÇÃO ESPECÍFICA PARA MULHERES CASADAS
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input ("Digite o tempo de casa (anos): ")
    
# EXIBIÇÃO DOS DADOS
print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

# SÓ MOSTRA O TEMPO DE CASA SE ELE TIVER SIDO PREENCHIDO
if tempo_casada:
    print(f"Tempo de casada: {tempo_casada} anos")