def main():
    
    qtd_numeros = int(input("Informe a quantidade de números que deseja comparar: "))
    
    contador = 0
    numero2 = 0
    numero1 = float(input("Informe um número: "))
    while contador < qtd_numeros:
         
                
        if numero1>numero2 and contador == 0:
            numero2 = float(input("Informe outro número: "))
        if numero2 > numero1:
            print(f"O maior número é:{numero2}")
            numero1 = float(input("Informe um número: "))
        if numero1 > numero2:
            print(f"O maior número é:{numero2}")
            numero2 = float(input("Informe outro número: "))
    contador = contador+1
    
        
    print(f"Foram lidos:{contador} números")
main()