mochila = ["caderno", "caneta", "lápis", "borracha", "régua"]

item = input("Digite o objeto que deseja retirar: ")

if item in mochila:
    mochila.remove(item)
else:
    print("O objeto não está na mochila.")

print(mochila)