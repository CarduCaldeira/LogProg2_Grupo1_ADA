import pyfiglet 
from source.cria_registro import cria_registro
from source.le_registro import le_registro
from source.deleta_registro import deleta_registro
from source.atualiza_registro import atualiza_registro
from source.mostra_features import mostra_features
from source.exporta_relatorio import exporta_relatorio 


def main():
    
    rodar_sistema = True

    f = pyfiglet.Figlet(font='big')
    print(f.renderText('Bem Vindo ao sistema da Ceu!'))
    print(f'{"="*70} \n'
          f'{"-"*70} \n'
          f'{"="*70} \n')
    

    while rodar_sistema:

        operacao = input("Informe o tipo de procedimento que deseja realizar: \n" 
                        "Para criar um registro digite:                             1 \n"
                        "Para ler um registro digite:                               2 \n"
                        "Para deletar um registro digite:                           3 \n"
                        "Para atualizar um registro digite:                         4 \n"
                        "Para obter informações sobre seus investimentos digite :   5 \n"
                        "Para exportar um relatorio  :                              6 \n"
                        "Para sair digite:                                          7 \n")

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


if __name__ == "__main__":
    main()