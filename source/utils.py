import os
import time
import datetime
import pyfiglet


def tela_inicial():
    """Exibe uma tela de boas-vindas ao Sistema.
    """
    f = pyfiglet.Figlet(font='big',
                        justify='center')
    print(f.renderText('ADA  ATM'))
    tracos()


def tracos():
    """Imprime uma linha decorativa composta por caracteres '=' e '-', delimitando uma área visual. 
    O comprimento total da linha é 90 caracteres.
    """
    print(f'{"="*85} \n'
          f'{"-"*85} \n'
          f'{"="*85} \n')


def limpar_tela():
    """
    Limpa a tela do terminal, detectando automaticamente o sistema operacional
    e usando 'cls' no Windows e 'clear' em sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')



def determina_data():
    """
    Obtem a data de realização do registro
    retornando um tupla no formato (dia, mes, ano) 
    """

    data = datetime.now().date()
    return data.day, data.month, data.year


def valida_digito(mensagem: str, mensagem_erro: str):
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

def valida_data(tempo, acao_realizada):
    """ """
    
    intervalo_valido = {'dia':(0,32),'mes':(0,13), 'ano':(2021,datetime.now().year +1)}

    while True:
        try:
            data = int(input(f"Informe o {tempo} do registro que deseja {acao_realizada}: "))   
        except ValueError:
            print("Valor invalido")
            continue
        else:
            if intervalo_valido[tempo][0] < data and data < intervalo_valido[tempo][1]:
                return data 
            else:
                print("Data invalida.")

