import pyfiglet
from cria_registro import cria_registro
from le_registro import le_registro
from deleta_registro import deleta_registro
from atualiza_registro import atualiza_registro
from mostra_features import mostra_features
from exporta_relatorio import exporta_relatorio
from encerrar_programa import encerrar_programa


def cabecalho():
    f = pyfiglet.Figlet(font='big')
    print(f.renderText('Bem Vindo ao sistema da Ceu!'))
    print(f'{"="*70} \n'
          f'{"-"*70} \n'
          f'{"="*70} \n')

def main():
    cabecalho()


    aux = {
        '1': cria_registro(),
        '2': le_registro(),
        '3': atualiza_registro(),
        '4': deleta_registro(),
        '5': mostra_features(),
        '6': exporta_relatorio(),
        '7': encerrar_programa()
    }

    tentativas = 0

    while True:
        operacao = input('''
                            
        Digite a opção que deseja realizar:
            
        [1] CRIAR UM REGISTRO                             
        [2] LER UM REGISTRO                               
        [3] ATUALIZAR UM REGISTRO                         
        [4] DELETAR UM REGISTRO                           
        [5] INFORMAÇÕES SOBRE SEUS INVESTIMENTOS   
        [6] EXPORTAR RELATÓRIO                              
        [7] SAIR  
        
        Insira o número da opção desejada: ''')

        try:

            if operacao in aux.keys():
                aux.get(operacao)

            else:
                tentativas += 1

                if tentativas == 3:
                    print(
                        "Você atingiu o número máximo de tentativas. Encerrando o programa.")
                    encerrar_programa()
                else:
                    print(
                        f"Entrada inválida. Você tem mais {3 - tentativas} {'tentativa' if tentativas == 2 else 'tentativas'}.")
                    break

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
    # %%
