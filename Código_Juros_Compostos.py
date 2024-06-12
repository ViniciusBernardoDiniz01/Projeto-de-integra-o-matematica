capital_aplicado = float(input("Informe o valor do capital aplicado. R$: "))
juros = float(input("Informe a porcentagem dos juros: "))
meses = float(input("Informe o tempo em meses: "))

juros_decimais = juros / 100

montante = capital_aplicado * (1 + juros_decimais)**meses

print("O montante é de R$: ", montante)