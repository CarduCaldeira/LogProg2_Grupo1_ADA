def exporta_relatorio():
   pass
   """ try:
        with open(ARQUIVO_REGISTROS_CSV, 'r', newline='') as arquivo_csv:
            registros = [linha.split(',') for linha in arquivo_csv.readlines()]

        nome_arquivo_exportacao = input("Digite o nome do arquivo de exportação (sem extensão): ")

        with open(f'{nome_arquivo_exportacao}.csv', 'w', newline='') as arquivo_exportacao:
            for registro in registros:
                linha = ','.join(map(str, registro))
                arquivo_exportacao.write(f"{linha}\n")

        print(f"Relatório exportado com sucesso para {nome_arquivo_exportacao}.csv")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")"""
