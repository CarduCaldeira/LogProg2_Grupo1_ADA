import csv
from datetime import datetime
import os
from cria_registro_receita import cria_registro_receita
from cria_registro_despesa import cria_registro_despesa
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
        
        if operacao in menu_cria_registro:
            limpar_tela()
            if operacao == '4':
                main()
        else:
            print("Entrada inválida")
