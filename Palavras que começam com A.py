palavras = []

for i in range(8):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)

palavras_a = []

for palavra in palavras:
    if palavra[0].lower() == "a":
        palavras_a.append(palavra)

print(palavras_a)