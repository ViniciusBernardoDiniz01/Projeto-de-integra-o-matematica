print("**Bem vindo ao nosso programa para resolução do juros simples e composto**")
print("")
print("")
capital_aplicado = float(input("Escreva o valor do capital aplicado R$: "))
juros = float(input("Escreva o valor do juros a ser aplicado: "))
meses = float(input("Escreva o tempo aplicado em meses: "))


print("**Qual a forma de juros**")
print("")
simples = 1
composto = 2
qual_tipo_de_juros = int(input("Escreva: (1 - simples , 2 - composto): "))


if qual_tipo_de_juros == 1:
    print("**Você está calculando juros simples**")
    print("")
    juros_decimal = juros / 100
    juros_simples = capital_aplicado * juros_decimal * meses
    montante = juros_simples + capital_aplicado
    print("")
    print("o seu montante é de: R$", montante)


elif qual_tipo_de_juros == 2:
    print("**Você esta calculando juros composto**")
    print("")
    juros_decimais = juros / 100
    montante = capital_aplicado * (1 + juros_decimais)**meses
    print("O montante é de R$: ", montante)

else:
    print("Escreva um numero entre 1 e 2")






