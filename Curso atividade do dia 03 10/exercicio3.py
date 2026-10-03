def calcular_compra(valor):
    if valor < 100:
        desconto = 0
    elif valor < 300:
        desconto = 0.05
    elif valor < 500:
        desconto = 0.10
    else:
        desconto = 0.15

    valor_final = valor - (valor * desconto)
    return valor_final


valor = float(input("Valor da compra: "))

valor_final = calcular_compra(valor)
economizado = valor - valor_final

print("Valor original: R$", valor)
print("Valor final: R$", valor_final)
print("Valor economizado: R$", economizado)