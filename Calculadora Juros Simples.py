#Exemplo de programa de calculadora de juros simples

print("Prezado usuário, informe o valor onde será aplicado os juros, qual a porcentagem da taxa de juros e em seguida informe a quantidade de anos:")

valor_inicial = input("Valor: R$")
valor_juros = input("Informe a % dos juros: ")
valor_tempo = input("Informe a quantidade de anos: ")

valor_inicial = float(valor_inicial)
valor_juros = float(valor_juros)
valor_tempo = int(valor_tempo)

valor_final = valor_inicial + (valor_inicial * (valor_juros/100) * valor_tempo)
valor_aumento = valor_final - valor_inicial

print(" ")
print("Valor final com os juros aplicados: R$", valor_final)
print("Aumento de R$", valor_aumento)
print(" ")