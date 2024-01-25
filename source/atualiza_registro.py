def atualizar_registro():
    # Obter o ID do registro a ser atualizado
    id = int(input("Digite o ID do registro a ser atualizado: "))

    # Obter a nova data
    data = datetime.datetime.now()

    # Obter o novo registro
    tipo = input(
        "Digite o novo tipo de registro (despesa, receita, investimento): ")

    # Obter o novo valor do registro
    valor = float(input("Digite o novo valor do registro: "))

    # Se o tipo de registro for despesa, multiplicar o valor por -1
    if tipo == "despesa":
        valor *= -1

        # Atualizar o registro no arquivo
    with open("registros.csv", "r") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.readlines()

    # Atualizar o registro
    linhas[id] = f"{data},{tipo},{valor}\n"

    # Salvar o arquivo
    with open("registros.csv", "w") as arquivo:
        arquivo.writelines(linhas)
