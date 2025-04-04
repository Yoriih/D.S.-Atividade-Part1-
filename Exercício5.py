# Exercício 5: Cálculo de IMC 

# Peça ao usuário seu peso (em kg) e altura (em metros)

peso = float(input("Qual o seu peso em Kg? "))
altura = float(input("Qual a sua altura em Metros? "))
             
# Calcule o Índice de Massa Corporal (IMC) utilizando a fórmula: IMC = peso / (altura * altura)

imc = (altura * altura) / peso

#Resultado

print("Seu IMC é : ",imc)