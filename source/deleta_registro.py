# Função para deletar registros
def deleta_registros():
  # Obter o ID do registro a ser deletado
  linhas[id] = f"{data},{registros},{valor}\n"
  
  id = int(input("Digite o registro a ser deletado: "))

  # Deletar o registro do arquivo
  with open("registros.csv", "r") as arquivo:
    # Ler as linhas do arquivo
    linhas = arquivo.readlines()

  # Deletar o registro
  del linhas[id]

  # Salvar o arquivo
  with open("registros.csv", "w") as arquivo:
    arquivo.writelines(linhas)