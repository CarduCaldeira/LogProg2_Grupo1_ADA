def atualizar_registros():
  # Obter o ID do registro a ser atualizado
  id = int(input("Digite o ID do registro a ser atualizado: "))

  # Obter a nova data
  data = datetime.datetime.now()

  # Obter o novo registro
  tipo = input("Digite o novo tipo de registro (despesa, receita, investimento): ")

  # Obter o novo valor da movimentação
  valor = float(input("Digite o novo valor do registro: "))

  # Se o tipo de movimentação for despesa, multiplicar o valor por -1
  if tipo == "despesa":
    valor *= -1