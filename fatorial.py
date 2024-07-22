def fatorar():
    fat_lista = []
    numero = int(input("\nDigite um número inteiro para ser fatorado: ")) 
    limite = numero
    fatorial = numero

    while len(fat_lista) < limite :
        fat_lista.append(numero)
        numero -= 1
        if numero != 0:
            fatorial = fatorial * numero

    print("Números da fatoração:", fat_lista)
    print("Quantidade de números: ", len(fat_lista))
    print("Resultado da fatoração:", fatorial)

def main():
    while True:
        try:
            fatorar()
        except ValueError as e:
            print("O valor digitado não correponde a um número inteiro.")
            print("Por favor insira um número válido.")
main()