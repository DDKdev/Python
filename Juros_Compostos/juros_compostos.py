from math import pow
print(pow(2, 3))

# função Juros Compostos


def jurosCompostos(capital, taxa, tempo):
    return capital*pow((1+taxa), tempo)


capital = float(input("Digite o valor a ser investido: "))
taxa = float(input("Digite a taxa anual do investimento: "))
tempo = int(input("Digite a quantidade de meses: "))

# Ajustes dos valores para a fórmula
taxa = taxa/100
tempo = tempo/12

# ajustando para DUAS CASAS DECIMAIS .02f
MontanteFinal = jurosCompostos(capital, taxa, tempo)
print(f'O Montante final será de: {MontanteFinal:.02f}')
print(f'O Total de juros foi: {MontanteFinal-capital:.02f}')
