import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0

    print("Escolha o nível de dificuldade!")
    nivel = (input("(1) Fácil \n(2) Médio \n(3) Difícil\n"))
    nivel = int(nivel)

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2): 
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input ("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Número deve ser entre 1 e 100!')
            continue  

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if (acertou):
            print("Você acertou, você fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = 1000 - pontos_perdidos
        

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()