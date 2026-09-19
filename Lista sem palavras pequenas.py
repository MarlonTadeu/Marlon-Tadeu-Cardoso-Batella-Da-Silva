palavras = ["sol", "computador", "casa", "programação", "pé", "python"]
palavras_grandes = []

for palavra in palavras:
    if len(palavra) >= 5:
        palavras_grandes.append(palavra)

print(palavras_grandes)