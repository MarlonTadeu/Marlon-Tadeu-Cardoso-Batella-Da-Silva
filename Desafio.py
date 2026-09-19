carrinho = []

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Mostrar carrinho")
    print("4 - Procurar produto")
    print("5 - Mostrar quantidade de produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        carrinho.append(produto)
        print("Produto adicionado!")

    elif opcao == "2":
        produto = input("Digite o produto que deseja remover: ")

        if produto in carrinho:
            carrinho.remove(produto)
            print("Produto removido!")
        else:
            print("Produto não está no carrinho.")

    elif opcao == "3":
        print("Carrinho:", carrinho)

    elif opcao == "4":
        produto = input("Digite o produto que deseja procurar: ")

        if produto in carrinho:
            print("O produto está no carrinho.")
        else:
            print("O produto não está no carrinho.")

    elif opcao == "5":
        print("Quantidade de produtos:", len(carrinho))

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")