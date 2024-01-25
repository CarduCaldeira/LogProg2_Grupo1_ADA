import csv
from datetime import datetime
import os

# funcao sera destinada a armazenar registros de investimento e calcular a taxa de investimento.

def investimento():
    """
    Tela inicial da seleção de investimentos
    """

    repeat_question = True

    while repeat_question:

        investimento = input('''informe o tipo de investimento desejado: \n"
                        
                        [1] Tesouro Direto: 10,06% a.a                             
                        [2] CDBs (Certificados de Depósito Bancário): 11,65% a.a                            
                        [3] Fundos de Renda Fixa: 12,25% a.a                        
                        [4] LCIs (Letras de Crédito Imobiliário): 8,99% a.a
                        [5] LCAs (Letras de Crédito do Agronegócio): 7,7% a.a
                        [6] Poupança: 6,17% a.a 
                        [7] Cancelar
                               
                             insira o número da opção desejada: ''')
                        
        if investimento == '1':
        
            aplicacao_tesouro_direto()
        
        elif investimento == '2':

            aplicacao_cdb()
    
        elif investimento == '3':
    
            aplicacao_renda_fixa()
        
        elif investimento == '4':
        
            aplicacao_lci()
        
        elif investimento == '5':
        
            aplicacao_lca()
    
        elif investimento == '6':
        
            aplicacao_poupanca()
        
        elif investimento == '7':

            repeat_question = False
            return

def determina_data():
    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro_investimento(tipo_investimento, valor, tempo, lucro):
    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    if not os.path.isfile('../registros/investimentos.csv'):
        with open('../registros/investimentos.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["tipo_investimento", "valor", "tempo_investimento", "lucro", "datetime"])

    with open('../registros/investimentos.csv','a') as file:
        writer = csv.writer(file)
        data = datetime.now().date()
        writer.writerow([tipo_investimento, valor, tempo, lucro, data])
    
    print(f"O registro do investimento foi salvo e o lucro do seu investimento em {tipo_investimento} será de R$ {lucro:.2f}")


def aplicacao_tesouro_direto():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 10.06 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("Tesouro Direto", valor, tempo, lucro)

def aplicacao_cdb():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 11.65 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("CDBs", valor, tempo, lucro)

def aplicacao_renda_fixa():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 12.25 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("Fundo de Renda Fixa", valor, tempo, lucro)

def aplicacao_lci():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 8.99 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("LCIs (Letras de Crédito Imobiliário)", valor, tempo, lucro)

def aplicacao_lca():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 7.7 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("LCAs (Letras de Crédito do Agronegócio)", valor, tempo, lucro)

def aplicacao_poupanca():
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 6.17 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    salva_registro_investimento("Poupança", valor, tempo, lucro)