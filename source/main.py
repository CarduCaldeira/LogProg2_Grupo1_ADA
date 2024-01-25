import pyfiglet
import os
import time
from cria_registro import cria_registro
from le_registro import le_registro
from deleta_registro import deleta_registro
from atualiza_registro import atualiza_registro
from mostra_features import mostra_features
from exporta_relatorio import exporta_relatorio
from encerrar_programa import encerrar_programa


def tracos():
    print(f'{"="*70} \n'
          f'{"-"*70} \n'
          f'{"="*70} \n')


def tela_inicial():
    f = pyfiglet.Figlet(font='big')
    print(f.renderText('Bem Vindo ao Sistema da Ceu!'))
    tracos()


def main():

    tela_inicial()

    menu = {
        '1': cria_registro,
        '2': le_registro,
        '3': atualiza_registro,
        '4': deleta_registro,
        '5': mostra_features,
        '6': exporta_relatorio,
        '7': encerrar_programa
    }

    tentativas = 0

    while True:
        operacao = input('''                         
    DIGITE UMA DAS OPÇÕES ABAIXO:
    
    [1] CRIAR UM REGISTRO
    [2] LER UM REGISTRO
    [3] ATUALIZAR UM REGISTRO
    [4] DELETAR UM REGISTRO
    [5] INFORMAÇÕES SOBRE SEUS INVESTIMENTOS
    [6] EXPORTAR RELATÓRIO
    [7] SAIR
        
     ''')

        try:
            if operacao in menu:
                os.system('cls' if os.name == 'nt' else 'clear')
                tracos()
                menu[operacao]()
                break

            else:
                tentativas += 1

                if tentativas == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(
                        "Você atingiu o número máximo de tentativas.", end='\n')
                    encerrar_programa()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(
                        f"\n'{operacao}' Não é uma entrada válida. Você tem mais {3 - tentativas} {'tentativa' if tentativas == 2 else 'tentativas'}.", end='\n')
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    tela_inicial()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def le_registro():
    pass


def atualiza_registro():
    pass


def deleta_registro():
    pass


def mostra_features():
    pass


def exporta_relatorio():
    pass


if __name__ == "__main__":
    main()
