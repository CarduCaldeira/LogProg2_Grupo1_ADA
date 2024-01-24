import pyfiglet 
from cria_registro import cria_registro
from le_registro import le_registro
from deleta_registro import deleta_registro
from atualiza_registro import atualiza_registro
from mostra_features import mostra_features
from exporta_relatorio import exporta_relatorio 
from encerrar_programa import encerrar_programa


def main():
    
    f = pyfiglet.Figlet(font='big')
    print(f.renderText('Bem Vindo ao sistema da Ceu!'))
    print(f'{"="*70} \n'
        f'{"-"*70} \n'
        f'{"="*70} \n')

    tentativas = 0

    while True:
        operacao = input('''Digite a opção que deseja realizar:
                            
                        [1] CRIAR UM REGISTRO                             
                        [2] LER UM REGISTRO                               
                        [3] ATUALIZAR UM REGISTRO                         
                        [4] DELETAR UM REGISTRO                           
                        [5] INFORMAÇÕES SOBRE SEUS INVESTIMETOS   
                        [6] EXPORTAR RELATÓRIO                              
                        [7] SAIR  
                        
                         Insira o número da opção desejada: ''')                                        


        elif operacao == '1':
            
            cria_registro()
        
        elif operacao == '2':
            
            le_registro()

        elif operacao == '3':

            deleta_registro()

        elif operacao == '4':
            
            atualiza_registro()
     
        elif operacao == '5':
            
            mostra_features()

        elif operacao == '6':
            
            exporta_relatorio()
     
        elif operacao == '7':
            
            encerrar_programa()
            break

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
    