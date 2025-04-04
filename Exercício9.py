# Exercício 9: Troca de Valores

# Solicite ao usuário dois valores 

valor1 = float(input("DIGITE UM VALOR: "))
valor2 = float(input("DIGITE SÓ MAIS UM VALOR: "))
 
# Troque o valor da primeira variável com o da segunda variável, e vice-versa.

troca1 = valor2
valor2 = valor1
valor1 = troca1

#Resultado

print("Seu primeiro valor agora é: ",valor1)
print("Seu segundo valor agora é: ",valor2)
