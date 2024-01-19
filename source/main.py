import pyfiglet  

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
                        "Para obter informações sobre seus investimentos digite :   4 \n"
                        "Para exportar um relatorio  :                              5 \n"
                        "Para sair digite:                                          6 \n")

        if operacao == '6':
            rodar_sistema = False

        elif operacao in ['1','2','3','4','5']:
            
            executa_operacao()
        
        else:
            print("="*28)
            print("Opção Invalida!")
            print("="*28)


   
def cria_registro():

    repeat_question = True

    while repeat_question:

        registro = input("Informe a operação desejada: \n" 
                      "Para deposito digite:     1 \n"
                      "Para deposito digite:     2 \n"
                      "Para investimento digite: 3 \n"
                      "Para cancelar:            4 \n")
        
        if registro not in ['1','2','3']:
            
            print("="*28)
            print("Opção Invalida!")
            print("="*28)

        else:
            repeat_question = False
            
    if registro =='1':
        execute_deposito()
    elif registro =='2':
        execute_deposito()
    else:
        execute_deposito()

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