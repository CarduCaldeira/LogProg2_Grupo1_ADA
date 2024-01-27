import csv
from datetime import datetime


def exporta_relatorio():
    registros = []

    # Tenta ler os registros de despesas
    try:
        with open('registros_despesa.csv', 'r', newline='') as arquivo_despesa:
            leitor_csv_despesa = csv.reader(arquivo_despesa, delimiter=';')
            for linha in leitor_csv_despesa:
                registros.append(['despesa'] + linha)
    except FileNotFoundError:
        print("Arquivo de despesa não encontrado.")

    # Tenta ler os registros de receita
    try:
        with open('registros_receita.csv', 'r', newline='') as arquivo_receita:
            leitor_csv_receita = csv.reader(arquivo_receita, delimiter=';')
            for linha in leitor_csv_receita:
                registros.append(['receita'] + linha)
    except FileNotFoundError:
        print("Arquivo de receita não encontrado.")

    # Tenta ler os registros geral
    try:
        with open('registros.csv', 'r', newline='') as arquivo_geral:
            leitor_csv_geral = csv.reader(arquivo_geral, delimiter=';')
            for linha in leitor_csv_geral:
                registros.append(linha)
    except FileNotFoundError:
        print("Arquivo geral não encontrado.")

    # Ordena registros por data
    registros.sort(key=lambda x: datetime.strptime(x[3], "%d/%m/%Y"))

    # Exporta registros para relatorio_exportado.csv
    with open('relatorio_exportado.csv', 'w', newline='') as arquivo_exportado:
        escritor_csv = csv.writer(arquivo_exportado, delimiter=',')
        escritor_csv.writerow(['Tipo', 'Valor', 'Dia', 'Mês', 'Ano'])

        for registro in registros:
            escritor_csv.writerow(registro)

    print("Relatório exportado para relatorio_exportado.csv com sucesso!")
