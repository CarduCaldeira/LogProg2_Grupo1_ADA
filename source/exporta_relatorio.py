import csv
import datetime
import re


def exporta_relatorio():
    registros = []

    # Tenta ler os registros de despesas
    try:
        with open('../registros/registros_despesa.csv', 'r', newline='') as arquivo_despesa:
            leitor_csv_despesa = list(csv.reader(arquivo_despesa, delimiter=';'))
            #for linha in leitor_csv_despesa:
            #    registros.append(['despesa'] + linha)
    except FileNotFoundError:
        print("Arquivo de despesa não encontrado.")

    # Tenta ler os registros de receita
    try:
        with open('../registros/registros_receita.csv', 'r', newline='') as arquivo_receita:
            leitor_csv_receita = list(csv.reader(arquivo_receita, delimiter=';'))
            #for linha in leitor_csv_receita:
            #    registros.append(['receita'] + linha)
    except FileNotFoundError:
        print("Arquivo de receita não encontrado.")

    # Tenta ler os registros geral
    try:
        with open('../registros/investimento.csv', 'r', newline='') as investimento:
            investimento = list(csv.reader(investimento, delimiter=';'))
            #for linha in leitor_csv_geral:
            #    registros.append(linha)
    except FileNotFoundError:
        print("Arquivo geral não encontrado.")

    def x(registro): return  registro[2]
    def y(string_data): return re.findall(r'\d+', string_data)
    def z(lista): return datetime.date(
        int(lista[2]), int(lista[1]), int(lista[0]))

    leitor_csv_despesa.extend(leitor_csv_receita)
    leitor_csv_despesa.extend(investimento)

    print(leitor_csv_despesa)
    input()
    # Ordena registros por data
    leitor_csv_despesa = sorted(leitor_csv_despesa, key=lambda registro: z(y(x(registro))))

    # Exporta registros para relatorio_exportado.csv
    with open('../registros/relatorio_exportado.csv', 'w', newline='') as relatorio:
        escritor_csv = csv.writer(relatorio, delimiter=',')
        escritor_csv.writerow(['Tipo', 'Valor', 'Data'])
        escritor_csv.writerows(leitor_csv_despesa)

    print("Relatório exportado para relatorio_exportado.csv com sucesso!")
