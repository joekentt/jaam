#Exemplo de programa de calculadora simples utilizando as quatro operações

print(" ")
print("Prezado usuário, informe dois números e o programa fará a soma, subtração, multiplicação e divisão dos números:")

numero1 = input("Informe o primeiro número: ")
numero2 = input("Informe o segundo número: ")

numero1 = float(numero1)
numero2 = float(numero2)

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(" ")
print("Resultado da soma: ", soma)
print("Resultado da subtração: ", subtracao)
print("Resultado da multiplicação: ", multiplicacao)
print("Resultado da divisão: ", divisao)
print(" ")