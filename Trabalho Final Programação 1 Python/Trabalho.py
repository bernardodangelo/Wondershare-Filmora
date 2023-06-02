#MENU

print("")
print("----- MENU -----")
print("Digite uma opção")
print("1 - Cadastrar um dado")
print("2 - Pesquisar um dado")
print("3 - Alterar um dado")
print("4 - Mostra os dados")
print("5 - Sair do programa")
print("Integrantes do grupo: Bernardo")

opcao = input("")

#LÓGICA

if opcao == "1":
    print("Cadastrar um dado")
elif opcao == "2":
    print("Pesquisar um dado")
elif opcao == "3":
    print("Alterar um dado")
elif opcao == "4":
    print("Mostra os dados")
elif opcao == "5":
    exit()
else:
    print("Opção inválida")
