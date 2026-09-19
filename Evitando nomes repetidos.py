convidados = []

for i in range(8):
    nome = input("Digite o nome do convidado: ")

    if nome not in convidados:
        convidados.append(nome)
    else:
        print("O convidado já foi cadastrado.")

print("Convidados:", convidados)