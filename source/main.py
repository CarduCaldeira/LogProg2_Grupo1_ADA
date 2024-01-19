import pyfiglet  
import datetime

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
    elif registro == '3':
        execute_investimento()
    else:
        cria_registro   


def execute_deposito():
    valor = float(input("Informe o valor do depósito: "))
    data = datetime.datetime.now()
    registros.append({"tipo": "receita", "valor": valor, "data": data})

def execute_despesa():
    valor = float(input("Informe o valor da despesa: "))
    data = datetime.datetime.now()
    registros.append({"tipo": "despesa", "valor": -valor, "data": data})

 def execute_investimento():
    valor = float(input("Informe o valor do investimento: "))
    taxa_juros = float(input("Informe a taxa de juros do investimento: "))
    data = datetime.datetime.now()
    registros.append({"tipo": "investimento", "valor": valor, "taxa_juros": taxa_juros, "data": data})   

def le_registro():
    tipo = input("Informe o tipo de registro que deseja ler (despesa, receita, investimento): ")
    for registro in registros:
        if registro["tipo"] == tipo:
            print(registro)

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