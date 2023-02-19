import random

print("*************************")
print("Bem vindo ao jogo da adivinhação!!")
print("*************************")

numero_secreto = random.randrange(1, 101)
tentativa = 0
pontos = 1000
nivel = 1

print("Nível de difículdade:")
print("Fácil(1) Medio(2) Difícil(3)")
print("nivel inexistente, digite outro")
nivel = int(input("Digite o número do nível de difículade desejado:"))

while nivel < 1 or nivel > 3:
    nivel = int(input("o nível digitado é invalido, digite novamente:"))

if nivel == 1:
    tentativa = 20

elif nivel == 2:
    tentativa = 10

elif nivel == 3:
    tentativa = 5


for rodada in range(1, tentativa + 1):
    print("Tentativa {} de {}".format(rodada, tentativa))

    chute_str = input("Digite um número entre 1 e 100:")

    print("O seu palpite foi:", chute_str)

    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("você digitou um número invalido e perdeu uma rodada. Tente novamente")
        continue

    acerto = chute == numero_secreto
    menor = chute  <  numero_secreto
    maior = chute  >  numero_secreto

    if acerto:
        print("Parabéns!!! Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("O seu palpite foi maior que o número secreto.")
        elif menor:
            print("O seu palpite foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


if not acerto:
    print("suas chances acabaram. O número secreto era {}:".format(numero_secreto))

print("Fim de jogo!")