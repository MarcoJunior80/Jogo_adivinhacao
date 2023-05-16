import random
from time import sleep
import pygame

print("**********************************")
print("\033[34m Bem vindo ao jogo de adivinhação\033[m")
print("**********************************")

numero_secreto = random.randrange(1, 101)
print('Sou seu PC... Acabei de pensar em um número entre 0 e 100.')
print('Será que você consegue adivinhar qual foi? ')
print(numero_secreto)
rodada = 1
pontos = 1000

print("Qual o nível de dificuldade?")
print("\033[32m(1) Fácil\033[m" "\033[33m (2) Médio\033[m" "\033[31m (3) Difícil\033[m")

nivel = int(input("Defina o nível: "))

if nivel == 1:
    total_de_tentativas = 20

elif nivel == 2:
    total_de_tentativas = 10

else:
    total_de_tentativas = 5

while rodada <= total_de_tentativas:
    print("tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite o seu numero entre 1 e 100: "))
    print('PROCESSANDO....')
    sleep(3)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("PARABÉNS!!!, Você acertou e fez {} pontos!!".format(pontos))
        pygame.init()
        pygame.mixer.music.load('0000397_1.mp3')
        pygame.mixer.music.play()

        input()
        pygame.quit()
        break
    else:
        if maior:
            print("Você errou. O seu chute foi maior que o numero secreto!")
            if rodada == total_de_tentativas:
                print("O numero secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
        elif menor:
            print("Você errou. O seu chute foi menor que o número secreto!")
            if rodada == total_de_tentativas:
                print("VOCÊ PERDEU!! O numero secreto era {}." "Você fez \033[32m{}\033[m pontos".format(numero_secreto,pontos))
                pygame.init()
                pygame.mixer.music.load('Toques_Som_de_Derrota.mp3')
                pygame.mixer.music.play()

                input()
                pygame.quit()

    pontos_perdidos = abs(chute - numero_secreto)
    pontos -= pontos_perdidos

    rodada = rodada + 1

print("Fim do jogo")