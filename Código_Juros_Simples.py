captal_aplicado = float(input("escreva o capital aplicado. R$:"))
juros = float(input("escreva a porcentagem dos juros: "))
meses = float(input("escreva o tempo em meses: "))

juros_decimal = juros / 100

juros_simples = captal_aplicado * juros_decimal * meses

montante = juros_simples + captal_aplicado

print("o seu montante é de: R$", montante)