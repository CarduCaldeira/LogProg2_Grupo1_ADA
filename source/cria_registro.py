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

