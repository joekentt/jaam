# Jogo da forca do desafio de Python
# Contém os opcionais: 
#     1- Ler a lista de palavras do arquivo
#     2- Dificuldade - Porém não foi implementada a lista de palavras mais dificeis, apenas a quantidade de tentativas
#     3- Permite chutar a palavra completa a qualquer momento


import random

def num_aleatorio(tamanho_lista):
    # Gera um número aleatório entre 0 e tamanho_lista - 1
    return random.randint(0, tamanho_lista - 1)

def origem_arquivo():
    # Define a origem do arquivo
    arquivo = open(r'f:\palavras.txt', 'r')
    return arquivo

def palavras_lista():
    # Abre o arquivo em modo de leitura
    with origem_arquivo() as file:
        # Ler todas as linhas do arquivo
        palavras = file.readlines()

    # Remover os caracteres de nova linha (\n) de cada palavra e converter para minúsculas
    palavras = [palavra.strip().lower() for palavra in palavras]
    
    return palavras

def encontrar_letra(palavra, letra, enigma):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            enigma[i] = letra
    return enigma

def main():
    lista = palavras_lista()
    palavra_sorteada = lista[num_aleatorio(len(lista))]
    enigma = ["_"] * len(palavra_sorteada)  # Inicializa enigma com underscores
    dificuldade = (1,2,3)
    escolha = 0
        
    print("========= JOGO DA FORCA =========")
    print("Instruções:")
    print("Uma palavra será sorteada e você terá um número de vidas de acordo com a dificuldade escolhida.")
    print("Em cada palpite você deve informar uma letra da palavra sorteada.")
    print("Em qualquer palpite você pode tentar acertar a palavra completa, porém se errar você será elimiado.")
    
    while escolha not in dificuldade:
        try:
            escolha = int(input("Escolha a dificuldade(1- Fácil | 2- Médio | 3- Difícil ): "))
            if escolha == 1:
                vidas = 6
            elif escolha == 2:
                vidas = 4
            elif escolha == 3:
                vidas = 2
        except:  
            print("Opção inválida.")

    letras = " ".join(enigma)
    
    print(f"\nA palavra sorteada é: {letras}\n")
    
    
    while True:
        palpite = input("Informe o palpite da letra (ou '0' para sair): ").lower()
        if palpite == "0":
            print(f"\nA palavra era: {palavra_sorteada}")
            break
        elif len(palpite) == len(palavra_sorteada) and palpite != palavra_sorteada:
            print("\nVocê foi eliminado por errar a palavra inteira!")
            break
        elif len(palpite) > 1 and palpite == palavra_sorteada:
            print("\nParabéns, você adivinhou a palavra inteira!")
            break
        elif len(palpite) > 1 and len(palpite) < len(palavra_sorteada) :
            print("\nPor favor, insira apenas uma letra ou a palavra inteira.")
            continue
        elif len(palpite) > 0 and len(palpite) < 2 and palpite not in palavra_sorteada:
            vidas = vidas -1
            if vidas > 0 :
                print(f"\nErrou o palpite. Quantidade de vidas: {vidas}.")
                continue
            else:
                print(f"\nErrou o palpite e suas vidas acabaram. Você foi eliminado.")
                break
            
        enigma = encontrar_letra(palavra_sorteada, palpite, enigma)
        letras = " ".join(enigma)
        print(f"\nA palavra é: {letras}\n")

        # # Verifica se a palavra foi completamente adivinhada
        if "_" not in enigma:
            print("\nParabéns, você adivinhou todas as letras!")
            break

        # Exibir a palavra sorteada para conferência
        #print(f"(Para conferência: {palavra_sorteada})")


main()
