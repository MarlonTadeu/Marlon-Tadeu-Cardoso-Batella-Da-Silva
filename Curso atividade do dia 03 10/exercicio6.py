def segundo_maior(numeros):
    maior = numeros[0]
    segundo = numeros[1]

    if segundo > maior:
        maior, segundo = segundo, maior

    for numero in numeros[2:]:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo:
            segundo = numero

    return segundo


numeros = [15, 8, 22, 10, 30, 18]

print("Segundo maior número:", segundo_maior(numeros))