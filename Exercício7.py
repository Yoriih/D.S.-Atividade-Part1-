# Exercício 7: Calculadora de Juros Simples

# Solicite ao usuário um capital principal, a taxa de juros (em porcentagem) e o número de anos. 

valor = float(input("Qual o capital principal? "))
juros = input("Qual a taxa de juros em porcentagem? ")
juros = juros.strip().replace("%", "")
percentual = float(juros) / 100
anos = int(input("Número de anos: "))

# Calcule o montante final utilizando a fórmula: Montante = capital + ( C × i × t ).

montate = valor + (valor * percentual * anos)

# Resultado

print("O Montante final é : ",montate)

