# Exercício 10: Calculadora de Média Ponderada

# Peça ao usuário três notas e seus respectivos pesos. 

nota1 = float(input("DIGITE A NOTA DA PRIMEIRA PROVA: "))
peso1 = float(input("DIGITE O PESO DESSA PROVA: "))

nota2 = float(input("DIGITE A NOTA DA SEGUNDA PROVA: "))
peso2 = float(input("DIGITE O PESO DESSA PROVA: "))

nota3 = float(input("DIGITE A NOTA DA TERCEIRA PROVA: "))
peso3 = float(input("DIGITE O PESO DESSA PROVA: "))

# Calcule e mostre a média ponderada das notas.

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

#Resultado

print("A MÉDIA PONDERADA DAS NOTAS É: ",media)