proibidas = ["spam", "propaganda", "golpe"]
palavras = []
quantidade = 0

for i in range(5):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)

    if palavra in proibidas:
        print("BLOQUEADA")
        quantidade += 1
    else:
        print("PERMITIDA")

print("Quantidade de palavras bloqueadas:", quantidade)