import random

numero_minimo = int(input("Digite o número minimo do intervalo: \n"))
numero_maximo = int(input("Digite o número máximo do intervalo: \n"))
numero_tentaivas = int(input("Digite o número de tentativas: \n"))

numero_sorteado = random.randint(numero_minimo, numero_maximo)

while numero_tentaivas != 0:
    chute = int(input(f"digite um número entre {
                numero_minimo} e {numero_maximo}\n"))
    if chute == numero_sorteado:
        print(f"parabéns você acertou. o número sorteado é {numero_sorteado}")
        break
    else:
        numero_tentaivas -= 1
        print(f"Errou. tente novamente. Restam {numero_tentaivas}")
if numero_tentaivas == 0:
    print("Suas tentativas acabaram")
