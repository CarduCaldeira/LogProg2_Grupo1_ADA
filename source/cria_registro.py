import csv
from datetime import datetime
import os

def cria_registro():
    """
    Tela inicial com as opçoes de tipos de operacoes
    """

    repeat_question = True

    while repeat_question:

        operacao = input("Informe a operação desejada: \n" 
                      "Para despesa digite:     1 \n"
                      "Para receita digite:     2 \n"
                      "Para investimento digite: 3 \n"
                      "Para cancelar:            4 \n")
        
        if operacao not in ['1','2','3','4']:

            print("Entrada invalida")

        elif operacao == '4':
            
            repeat_question = False
            continue
        
        elif operacao == '1':
            
            executa_despesa()

        elif operacao == '2':
            
            executa_receita()

        elif operacao == '3':
            
            executa_investimento()

def executa_despesa():
    """
    Obtem as informacoes referentes a operacao despesa
    e salva o registro com a funcao salva_registro
    """

    mensagem = "Informe o valor da despesa (o valor deve ser positivo)"
    mensagem_erro = "Entrada invalida, informe um valor da numerico"
    despesa = valida_digito(mensagem, mensagem_erro)

    data = determina_data()
        
    registro = ['despesa', -despesa, data, -1]
    salva_registro(registro)

def executa_receita():
    """
    Obtem as informacoes referentes a operacao receita
    e salva o registro com a funcao salva_registro
    """
    
    mensagem = "Informe o valor da receita"
    mensagem_erro = "Entrada invalida, informe um valor da numerico"
    receita = valida_digito(mensagem, mensagem_erro)

    data = determina_data()

    registro = ['receita', receita, data, -1]
    salva_registro(registro)

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



    

    