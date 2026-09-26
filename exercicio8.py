def menor_preco(precos):
    menor = precos[0]

    for preco in precos:
        if preco < menor:
            menor = preco

    return menor

precos = [35.90, 12.50, 89.90, 22.00, 15.75]
print(f"Menor preço: R$ {menor_preco(precos):.2f}")