# Exercício 6: Cálculo de Desconto

# Peça ao usuário o valor de um produto e o percentual de desconto. 

valor = float(input("Qual o valor do produto? "))
desconto = float(input("Qual o percentual de desconto? "))

# Calcule preço original x (porcentagem descontada / 100)

preço = valor * (desconto / 100)
valorfinal = valor - preço

#Resultado

print("O valor com o desconto aplicado é: ",valorfinal)