#Exemplo de programa de calculadora que aplica desconto

print("Prezado usuário, informe o valor do produto que deseja aplicar o desconto e em seguida o valor da % do desconto:")

valor_produto = input("Valor do produto: ")
valor_desconto = input("Informe a porcentagem do desconto: ")

valor_produto = float(valor_produto)
valor_desconto = float(valor_desconto)

valor_final_produto = valor_produto - (valor_produto * (valor_desconto/100))
valor_final_desconto = valor_produto - valor_final_produto

print(" ")
print("Valor inicial do produto: R$", valor_produto)
print("Porcentagem desconto: ", valor_desconto, "% . Valor em R$ do desconto: ", valor_final_desconto)
print("Valor final do produto: R$", valor_final_produto)
print(" ")