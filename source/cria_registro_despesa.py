import csv
from datetime import datetime
import os 

#funcao sera destinada para armazenar apenas os registros de despesa em um CSV na pasta registros.

def cria_registro_despesa():
    mensagem = "informe o valor da despesa: "
    mensagem_erro = "entrada inválida, informe um valor numérico"

    despesa = valida_digito(mensagem, mensagem_erro)
    data = determina_data()
    
    registro = ['despesa', despesa, data]
    salva_registro(registro)

def valida_digito(mensagem:str, mensagem_erro:str):

    while True:
        try:
            despesa = float(input(mensagem))
        except ValueError:
            print(mensagem_erro)
            continue
        else:
            if despesa > 0:
                return despesa
            else:
                print("valor deve ser maior que zero.")

def determina_data():
    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro(registro:list):
    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    if not os.path.isfile('../registros/registros_despesa.csv'):
        with open('../registros/registros_despesa.csv', 'w') as file:
             pass
        
    with open('../registros/registros_despesa.csv','a') as file:
        registros_despesa = csv.writer(file, delimiter=';', lineterminator='\n')
        registros_despesa.writerow(registro)

    print ('Registro de despesa salvo')