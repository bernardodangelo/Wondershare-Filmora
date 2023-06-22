#CATEGORIAS
produto = ["Arroz","Feijão","Açúcar","Café","Lentilha"]
peso = ["1kg", "2kg", "3kg", "5kg", "10kg"]

#MATRIZ
matriz = [["X"] * 5 for i in range(5)]

# MENU
while True:
    print("")
    print("====== MENU ======")
    print("Digite uma opção")
    print("1 - Cadastrar um dado")
    print("2 - Pesquisar um dado")
    print("3 - Alterar um dado")
    print("4 - Mostrar os dados")
    print("5 - Reiniciar a tabela")
    print("6 - Sair do programa")
    opcao = input("Digite um número para selecionar no uma opção no Menu: ")

# LÓGICA
    
# CADASTRAR UM DADO
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
        
# PESQUISAR UM DADO
    elif opcao == "2":
        print("Pesquisar um dado")

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("Erro: Linha ou coluna inválida")
            continue

        dado = matriz[linha - 1][coluna - 1]
        print("Dado encontrado:", dado)
        
# ALTERAR UM DADO
    elif opcao == "3":
        print("Alterar um dado")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        dado = int(input("Digite o novo dado: "))
        
        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("Erro: Linha ou coluna inválida")
            continue
        
        matriz[linha - 1][coluna - 1] = dado

        print("Dado alterado com sucesso!")
    
# MOSTRAR DADOS
    elif opcao == "4":
        print("ㅤ")
        print("Produtos:")
        print(produto)
        print("\nPesagem:")
        print(peso)
        print("\nMatriz:")
        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()
    
# REINICIAR TABELA
    elif opcao == "5":
        matriz = [["X"] * 5 for i in range(5)]
    
# SAIR DO PROGRAMA
    elif opcao == "6":
        print("Obrigado por utilizar o programa!")
        print("Integrantes do grupo: Bernardo, Emanoel, Yuri")
        exit()

    
# OPÇÃO INVÁLIDA
    else:
        print("Opção inválida")