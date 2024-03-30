import csv
import os

def criar_arquivo_csv():
    if not os.path.isfile('clientes.csv'):
        with open('clientes.csv', mode='w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Email', 'Telefone'])

def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    with open('clientes.csv', mode='a', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, email, telefone])
    
    print("Cliente adicionado com sucesso!")

def buscar_cliente():
    criar_arquivo_csv()  # Garante que o arquivo CSV existe
    nome = input("Digite o nome do cliente que deseja buscar: ")
    encontrado = False
    
    with open('clientes.csv', mode='r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            if linha[0].lower() == nome.lower():
                print(f"Cliente encontrado - Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")
                encontrado = True
                break
    
    if not encontrado:
        print("Cliente não encontrado.")

def visualizar_clientes():
    with open('clientes.csv', mode='r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        print("Lista de clientes cadastrados:")
        for linha in leitor:
            print(f"Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")

def menu():
    while True:
        print("\n##################################")
        print("\n--------------MENU--------------")
        print("1. Adicionar novo cliente")
        print("2. Visualizar todos os clientes")
        print("3. Buscar cliente pelo nome")
        print("4. Encerrar o programa")
        print("\n##################################")
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")

if __name__ == "__main__":
    menu()
