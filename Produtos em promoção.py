precos = [25.0, 80.0, 15.0, 120.0, 45.0]
promocao = []

for preco in precos:
    if preco > 50:
        promocao.append(preco * 0.90)
    else:
        promocao.append(preco)

print("Lista original:", precos)
print("Promoção:", promocao)