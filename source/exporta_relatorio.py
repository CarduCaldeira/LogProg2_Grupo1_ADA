import csv
from datetime import datetime
import os


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
        print("Nenhum registro encontrado.")
