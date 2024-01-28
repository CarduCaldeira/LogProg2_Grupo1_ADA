import csv
from datetime import datetime
import os

# funcao sera destinada a armazenar registros de investimento e calcular a taxa de investimento.

def investimento(flag_atualiza):
    """
    Tela inicial da seleção de investimento
    """

    repeat_question = True

    while repeat_question:

        investimento = input('''informe o tipo de investimento desejado: \n"
                        
                        [1] Tesouro Direto: 10,06% a.a                             
                        [2] CDBs (Certificados de Depósito Bancário): 11,65% a.a                            
                        [3] Poupança: 6,17% a.a 
                        [4] Cancelar
                               
                             insira o número da opção desejada: ''')
                        
        if investimento == '1':
        
            aplicacao_tesouro_direto(flag_atualiza)
            repeat_question = False
            continue
        
        elif investimento == '2':

            aplicacao_cdb(flag_atualiza)
            repeat_question = False
            continue
    
        elif investimento == '3':
    
            aplicacao_poupanca(flag_atualiza)
            repeat_question = False
            continue
        
        elif investimento == '4':

            repeat_question = False
            return

def determina_data():
    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro_investimento(tipo_investimento, valor, tempo, lucro:list):
    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    if not os.path.isfile('../registros/investimento.csv'):
        with open('../registros/investimento.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["tipo_investimento", "valor", "datetime","tempo_investimento", "lucro"])

    with open('../registros/investimento.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        data = determina_data()
        writer.writerow([tipo_investimento, valor, data, tempo, lucro])
    
    print(f"O registro do investimento foi salvo e o lucro do seu investimento em {tipo_investimento} será de R$ {lucro:.2f}")


def aplicacao_tesouro_direto(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 10.06 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("tesouro direto", valor, tempo, lucro, flag_atualiza['id'])
    else:
        salva_registro_investimento("tesouro direto", valor, tempo, lucro)

def aplicacao_cdb(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 11.65 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("cbds", valor, tempo, lucro, flag_atualiza['id'])
    else:
        salva_registro_investimento("cbds", valor, tempo, lucro)

def aplicacao_poupanca(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 6.17 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("poupanca", valor, tempo, lucro, flag_atualiza['id'])
    else:   
        salva_registro_investimento("poupanca", valor, tempo, lucro)


def atualiza_registro_investimento(tipo_investimento, valor, tempo, lucro:list, id):
    
    data = determina_data()
    registro = [tipo_investimento, valor, data, tempo, lucro]

    with open('../registros/investimento.csv','r') as file:

        registros = list(csv.reader(file, delimiter=';', lineterminator='\n'))
        
    registros[id] = registro

    with open('../registros/registros_despesa.csv','w') as file:

        escritor = csv.writer(file, delimiter=';', lineterminator='\n')
        escritor.writerows(registros)

    print(f"O registro do investimento foi salvo e o lucro do seu investimento em {tipo_investimento} será de R$ {lucro:.2f}")
    print('Registro atualizado')