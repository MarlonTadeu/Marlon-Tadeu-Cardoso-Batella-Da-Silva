jogos = ["Minecraft", "FIFA", "Fortnite", "GTA", "Valorant"]
jogos_pedro = ["GTA", "Rocket League", "Minecraft", "CS", "Valorant"]

comum = []

for jogo in jogos:
    if jogo in jogos_pedro:
        comum.append(jogo)

print("Jogos em comum:", comum)