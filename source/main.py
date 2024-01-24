import pyfiglet
from cria_registro import cria_registro 
def main():
    
    rodar_sistema = True

    f = pyfiglet.Figlet(font='big')
    print(f.renderText('Bem Vindo ao sistema da Ceu!'))
    print(f'{"="*70} \n'
          f'{"-"*70} \n'
          f'{"="*70} \n')
    

    while rodar_sistema:

        operacao = input('''Digite a opção que deseja realizar:
                         
                        [1] CRIAR UM REGISTRO                             
                        [2] LER UM REGISTRO                               
                        [3] DELETAR UM REGISTRO                           
                        [4] ATUALIZAR UM REGISTRO                         
                        [5] INFORMAÇÕES SOBRE SEUS INVESTIMETOS   
                        [6] EXPORTAR RELATÓRIO                              
                        [7] SAIR  
                        
                         Insira o número da opção desejada: ''')                                        

        if operacao == '7':
            
            rodar_sistema = False
            continue

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
     
        else:
            print("="*28)
            print("Opção Invalida!")
            print("="*28)


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