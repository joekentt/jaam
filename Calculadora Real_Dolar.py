#Exemplo de programa de calculadora de conversão Real para Dolar

print("Prezado usuário, informe o valor em reais e em seguida informa o valor da taxa de câmbio:")

valor_real = input("Valor: R$")
valor_cambio = input("Informe o valor da taxa de câmbio: ")

valor_real = float(valor_real)
valor_cambio = float(valor_cambio)

valor_final = valor_real / valor_cambio

print(" ")
print("Valor após conversão: US$", round(valor_final,2))
print(" ")