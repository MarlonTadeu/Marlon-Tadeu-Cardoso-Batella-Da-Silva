def contar_sem_estoque(estoque):
    quantidade = 0

    for item in estoque:
        if item == 0:
            quantidade += 1

    return quantidade


def contar_estoque_baixo(estoque):
    quantidade = 0

    for item in estoque:
        if item < 5:
            quantidade += 1

    return quantidade


def maior_estoque(estoque):
    maior = estoque[0]

    for item in estoque:
        if item > maior:
            maior = item

    return maior


estoque = [15, 2, 8, 0, 20, 4, 11]

print("Itens sem estoque:", contar_sem_estoque(estoque))
print("Itens com estoque baixo:", contar_estoque_baixo(estoque))
print("Maior quantidade em estoque:", maior_estoque(estoque))