def contar_acima_do_valor(precos, limite):
    quantidade = 0

    for preco in precos:
        if preco > limite:
            quantidade += 1

    return quantidade

precos = [10, 25, 80, 15, 120, 45]
limite = float(input("Digite o limite: R$ "))

print("Quantidade acima do limite:",
      contar_acima_do_valor(precos, limite))