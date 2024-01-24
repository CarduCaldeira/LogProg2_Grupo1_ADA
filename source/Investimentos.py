import csv
from datetime import datetime
import os

# funcao sera destinada a armazenar registros de investimento e calcular a taxa de investimento.

def investimento():
    """
    Tela inicial da selsção de investimentos
    """

    repeat_question = True

    while repeat_question:

        investimento = input("informe o tipo de investimento desejado: \n"
                        
                    "1: Tesouro Direto 10,06% a.a \n ")
                        
        

"""
    Tabela de valores investimento.

Tesouro Direto: 10,06% a.a
CDBs (Certificados de Depósito Bancário): 11,65% a.a 22,5% de IR sobre os ganhos
Fundos de Renda Fixa: 12,25% a.a Sem IR
LCIs (Letras de Crédito Imobiliário) 8,99% a.a
LCAs (Letras de Crédito do Agronegócio): 7,7% a.a
Poupança: 6,17% a.a

IR sobre 
Até 180 dias	22,5%
De 181 a 360 dias	20%
De 361 a 720 dias	17,5%
Acima de 720 dias	15%
"""