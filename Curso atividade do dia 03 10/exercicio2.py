def calcular_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        situacao = "Reprovado"
    elif media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Aprovado"

    return media, situacao


nota1 = 7
nota2 = 6
nota3 = 8

media, situacao = calcular_situacao(nota1, nota2, nota3)

print("Média:", media)
print("Situação:", situacao)