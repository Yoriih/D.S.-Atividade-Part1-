# Exercício 8: Conversão de Idade

# Peça ao usuário para digitar a idade em anos 

idade = int(input("Qual sua idade em anos? "))

# Converta-a para meses e dias (considere um ano com 365 dias).

meses = idade * 12
dias = idade * 365

# Resultado

print("Sua idade em meses é : ",meses,"meses")
print("Sua idade em dias é: ",dias,"dias")