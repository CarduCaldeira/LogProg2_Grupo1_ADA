import csv
from datetime import datetime
import os
from cria_registro_receita import cria_registro_receita
from cria_registro_despesa import cria_registro_despesa
from utils import determina_data, valida_digito 
from investimento import investimento

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cria_registro(main):
    """
    Tela inicial com as opções de tipos de operações
    """

    menu_cria_registro = {
        '1': cria_registro_despesa,
        '2': cria_registro_receita,
        '3': investimento,
        '4': main,
    }

    while True:
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
            
            executa_investimento()

def  executa_investimento():
    """
    Obtem as informacoes referentes a operacao investimento
    e salva o registro com a funcao salva_registro
    """
    
    mensagem = "Informe o valor do Investimento"
    mensagem_erro = "Entrada invalida, informe um valor da numerico"
    investimento = valida_digito(mensagem, mensagem_erro)

    data = determina_data()
    taxa_de_juros = 0.11

    registro = ['investimento', investimento, data, taxa_de_juros]
    salva_registro(registro)

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



    

    