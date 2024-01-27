import csv
from datetime import datetime
import os
from cria_registro_receita import cria_registro_receita
from cria_registro_despesa import cria_registro_despesa
from investimento import investimento

def cria_registro():
    """
    Tela inicial com as opçoes de tipos de operacoes
    """

    repeat_question = True

    while repeat_question:

        operacao = input('''Digite a opção que deseja realizar:  \n"
                        
                        [1] DESPESA                             
                        [2] RECEITA                               
                        [3] INVESTIMENTO                         
                        [4] CANCELAR 
                             
                             insira o número da opção desejada: ''')
        
        if operacao not in ['1','2','3','4']:

            print("Entrada invalida")

        elif operacao == '4':
            
            repeat_question = False
            continue
        
        elif operacao == '1':
            
            cria_registro_despesa()

        elif operacao == '2':
            
            cria_registro_receita()

        elif operacao == '3':
            
            investimento()


def valida_digito(mensagem:str, mensagem_erro:str):
    """
    Faz a validacao do valor informado pelo usuario, caso nao seja
    um numero a conversao para float ira gerar um erro, que faz a função
    requisitar novamente o valor numerico. Caso o valor nao seja maior que zero
    a função  requisitara novamente o valor numerico
    """

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
                print("O valor deve ser maior que zero.")

        
def determina_data():
    """
    Obtem a data de realização do registro
    retornando um tupla no formato (dia, mes, ano) 
    """

    data = datetime.now().date()
    return data.day, data.month, data.year
     
def salva_registro(registro:list):
    """
    Recebe uma lista representando o registro com as suas 
    respectivas informações e salva no arquivo registros/registros.csv.
    """

    with open('registros/registros.csv','a') as file:

        registros = csv.writer(file, delimiter=';', lineterminator='\n')
        registros.writerow(registro)
    
    print('Registro salvo')



    

    