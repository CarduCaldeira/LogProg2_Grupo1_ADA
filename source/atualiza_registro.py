import datetime
import csv
from utils import valida_data, determina_data

def le_arquivo():
    pass


def mostrar_opcoes(acao_realizada):

    
    registros_path = {  '1': 'registros_receita.csv',
                        '2': 'registros_despesa.csv',
                        '3': 'registros_investimento.csv'
                    }
    
    while True:

        #fazer validao 
        operacao = input('''Informe o tipo de operação do registro que deseja {acao_realizada} ou se 
                            deseja cancelar: 
                        
                        [1] RECEITA                              
                        [2] DESPESA
                        [3] INVESTIMENTO
                        [4] CANCELAR''')
        
        if operacao =='4':

            return None
        
        elif operacao in registros_path:
           
            lista_registro = le_arquivo(registros_path[operacao])

            if not lista_registro:

                print("Não há registros com esse tipo de operação! ")
                return None
            
            data = []
            print("Informe um intervalo de data em que a operação desejada pertence \n")
            for i in ["antiga", "recente"]:
                print("Para a data mais antiga informe \n") #O dia,mes ano
                for tempo in ['dia', 'mes', 'ano']:

                    data.append(valida_data(tempo))
                    #imaginar que em um app o usuario escolheria um intervalo 
                    #de data em um calendario

            data = tuple(data)
            #seleciona os registros ques estao neste intevalo
            #aqui da pra usar funçao lambda e o filter
            #depois de selecionado printa os 5 primeiros registros dessa lista (para nao ficar muito grande 
            #a mensagem na tela), o usuario retorna entao o id 
        else:
            print("Opção inválida, informe a opção novamente!")
            continue
           
        
        #funcao_q_verifca quantas opcoes de registros com tal operação

          

def get_id(acao_realizada):
    """
    Função que retorna o id a ser atualizado/deletado
    espeficicando o tipo de operacaçao, a data, e a despesa
    """                                   

    id = mostrar_opcoes(acao_realizada)

    return id


def atualiza_registro():
  
    id = get_id()
    
    # Obter a nova data
    data = determina_data()

    # Obter o novo registro
    tipo = input("Digite o novo tipo de registro (despesa, receita, investimento): ")
    # Obter o novo registro
    tipo = input(
        "Digite o novo tipo de registro (despesa, receita, investimento): ")

    # Obter o novo valor do registro
    valor = float(input("Digite o novo valor do registro: "))
    # Obter o novo valor do registro
    valor = float(input("Digite o novo valor do registro: "))

    # Se o tipo de registro for despesa, multiplicar o valor por -1
    if tipo == "despesa":
        valor *= -1
    # Se o tipo de registro for despesa, multiplicar o valor por -1
    if tipo == "despesa":
        valor *= -1

        # Atualizar o registro no arquivo
    with open("registros/registros_{operacao}.csv", "r") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.readlines()

    with open("registros/registros_{operacao}.csv", "w") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.writer()


    # Atualizar o registro
    linhas[id] = f"{data},{tipo},{valor}\n"

    # Salvar o arquivo
    with open("registros.csv", "w") as arquivo:
        arquivo.writelines(linhas)
    # Salvar o arquivo
    with open("registros.csv", "w") as arquivo:
        arquivo.writelines(linhas)
