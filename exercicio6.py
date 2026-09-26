def maior_numero(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    return maior

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

print("Maior número:", maior_numero(a, b, c))