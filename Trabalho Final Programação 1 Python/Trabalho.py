#MATRIZ
matriz = [["X"] * 5 for i in range(5)]

# MENU
while True:
    print("")
    print("----- MENU -----")
    print("Digite uma opção")
    print("1 - Cadastrar um dado")
    print("2 - Pesquisar um dado")
    print("3 - Alterar um dado")
    print("4 - Mostrar os dados")
    print("5 - Sair do programa")
    print("Integrantes do grupo: Bernardo")

    opcao = input("")

    # LÓGICA

    if opcao == "1":
        print("Cadastrar um dado")

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        dado = int(input("Digite o dado para cadastro: "))

        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("Erro: Linha ou coluna inválida")
            continue

        matriz[linha - 1][coluna - 1] = dado

        print("Dado cadastrado com sucesso!")

    elif opcao == "2":
        print("Pesquisar um dado")

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("Erro: Linha ou coluna inválida")
            continue

        dado = matriz[linha - 1][coluna - 1]
        print("Dado encontrado:", dado)

    elif opcao == "3":
        print("Alterar um dado")

    elif opcao == "4":
        print("Matriz:")
        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()

    elif opcao == "5":
        exit()

    else:
        print("Opção inválida")
