def le_registro():
  # Abrir o arquivo
  with open("registros.csv", "r") as arquivo:
    # Ler as linhas do arquivo
    linhas = arquivo.readlines()

    # Imprimir as linhas
    for linha in linhas:
      print(linha)