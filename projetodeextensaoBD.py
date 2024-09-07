import mysql.connector

# Função para conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        port="3306",  # ou o endereço do seu servidor MySQL
        user="root",  # substitua pelo seu nome de usuário MySQL
        password="Bigodevermeimundo!",  # substitua pela sua senha MySQL
        database="PetshopAdocao"
    )

# Função para inserir um cliente
def inserir_cliente(nome, endereco, telefone, email):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Clientes (nome, endereco, telefone, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, endereco, telefone, email))
    conn.commit()
    print(f"Cliente {nome} inserido com sucesso!")
    cursor.close()
    conn.close()

# Função para inserir um pet
def inserir_pet(cliente_id, nome, idade, tipo, raca):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Pets (cliente_id, nome, idade, tipo, raca) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (cliente_id, nome, idade, tipo, raca))
    conn.commit()
    print(f"Pet {nome} inserido com sucesso!")
    cursor.close()
    conn.close()

# Função para inserir um serviço (ex: banho, tosa)
def inserir_servico(descricao, preco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Servicos (descricao, preco) VALUES (%s, %s)"
    cursor.execute(sql, (descricao, preco))
    conn.commit()
    print(f"Serviço '{descricao}' inserido com sucesso!")
    cursor.close()
    conn.close()

# Função para inserir um produto (ex: ração, brinquedo)
def inserir_produto(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, quantidade, preco))
    conn.commit()
    print(f"Produto '{nome}' inserido com sucesso!")
    cursor.close()
    conn.close()

# Função para inserir uma ordem de serviço
def inserir_ordem_servico(cliente_id, pet_id, data, descricao, valor_total):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO OrdensDeServico (cliente_id, pet_id, data, descricao, valor_total) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (cliente_id, pet_id, data, descricao, valor_total))
    conn.commit()
    print(f"Ordem de serviço para cliente ID {cliente_id} inserida com sucesso!")
    cursor.close()
    conn.close()

# Menu simples para inserir dados
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Inserir Cliente")
        print("2. Inserir Pet")
        print("3. Inserir Serviço")
        print("4. Inserir Produto")
        print("5. Inserir Ordem de Serviço")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            inserir_cliente(nome, endereco, telefone, email)

        elif escolha == "2":
            cliente_id = int(input("ID do Cliente: "))
            nome = input("Nome do pet: ")
            idade = int(input("Idade do pet: "))
            tipo = input("Tipo do pet (ex: cachorro, gato): ")
            raca = input("Raça do pet: ")
            inserir_pet(cliente_id, nome, idade, tipo, raca)

        elif escolha == "3":
            descricao = input("Descrição do serviço: ")
            preco = float(input("Preço do serviço: "))
            inserir_servico(descricao, preco)

        elif escolha == "4":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço do produto: "))
            inserir_produto(nome, quantidade, preco)

        elif escolha == "5":
            cliente_id = int(input("ID do Cliente: "))
            pet_id = int(input("ID do Pet: "))
            data = input("Data da Ordem (YYYY-MM-DD): ")
            descricao = input("Descrição da ordem de serviço: ")
            valor_total = float(input("Valor total: "))
            inserir_ordem_servico(cliente_id, pet_id, data, descricao, valor_total)

        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
