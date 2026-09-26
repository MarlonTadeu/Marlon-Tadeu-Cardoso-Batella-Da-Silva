def contar_pares(numeros):
    quantidade = 0

    for numero in numeros:
        if numero % 2 == 0:
            quantidade += 1

    return quantidade

numeros = [12, 7, 9, 20, 14, 3, 8, 11]
print("Quantidade de números pares:", contar_pares(numeros))
