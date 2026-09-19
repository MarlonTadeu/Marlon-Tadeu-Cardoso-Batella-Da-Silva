jogadores = ["Lucas", "Pedro", "Marcos", "Rafael", "Bruno"]

print(jogadores)

posicao = int(input("Digite a posição do jogador (1 a 5): "))
novo = input("Digite o nome do novo jogador: ")

jogadores[posicao - 1] = novo

print(jogadores)