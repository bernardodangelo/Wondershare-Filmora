#CATEGORIAS
produto = ["Arroz","Feijão","Açúcar","Café","Lentilha"]
peso = ["1kg", "2kg", "3kg", "5kg", "10kg"]

#MATRIZ
matriz = [["X"] * 5 for i in range(5)]

# MENU
while True:
    print("")
    print("====== MENU ======")
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
        print("ㅤ")
        linha = int(input("Digite a linha: "))
        coluna = int(input("\nDigite a coluna: "))
        dado = int(input("\nDigite o dado para cadastro: "))

        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("ㅤ")
            print("Erro: Linha ou coluna inválida")
            
        else:
            matriz[linha - 1][coluna - 1] = dado
        
            print("ㅤ")
            print("Dado cadastrado com sucesso!")
        
# PESQUISAR UM DADO
    elif opcao == "2":
        print("ㅤ")
        linha = int(input("Digite a linha: "))
        coluna = int(input("\nDigite a coluna: "))

        if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
            print("ㅤ")
            print("Erro: Linha ou coluna inválida")
        
        else:
            dado = matriz[linha - 1][coluna - 1]
            print("ㅤ")
            print("Dado encontrado:", dado)
        
# ALTERAR UM DADO
    elif opcao == "3":
        print("ㅤ")
        linha = int(input("Digite a linha: "))
        coluna = int(input("\nDigite a coluna: "))
        anterior = matriz[linha - 1][coluna - 1]
        print("Dado a ser alterado:", anterior)
        escolha = str(input("\nDeseja prosseguir? (Digite 's' para sim e 'n' para não): "))
        
        if escolha == "s":
            print("ㅤ")
            dado = int(input("Digite o novo dado: "))
        
            if linha > 5 or linha < 1 or coluna > 5 or coluna < 1:
                print("ㅤ")
                print("Erro: Linha ou coluna inválida")
        
            else:
                matriz[linha - 1][coluna - 1] = dado
                print("ㅤ")
                print("Dado alterado com sucesso!")
        
        else:
            print("ㅤ")
            print("Nenhum dado foi alterado")
    
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
        print("ㅤ")
        print("Tabela reiniciada com sucesso!")
    
# SAIR DO PROGRAMA
    elif opcao == "6":
        print("ㅤ")
        print("Integrantes do grupo:")
        print("\nBernardo")
        print("Emanoel")
        print("Yuri")
        print("\nTema:")
        print("\nEstoque de Produtos")
        print("\nProfessor(a):")
        print("\nRenata Laranja")
        print("\nDisciplina:")
        print("\nProgramação 1")
        print("\nObrigado por utilizar o programa!")
        print("")
        exit()

# OPÇÃO INVÁLIDA
    else:
        print("ㅤ")
        print("Opção inválida! Digite um número correspondente a uma opção do menu.")