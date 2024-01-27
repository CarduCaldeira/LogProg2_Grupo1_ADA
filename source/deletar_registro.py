import datetime
import csv
from utils import valida_data, determina_data


def le_arquivo():
    pass


def mostrar_opcoes(acao_realizada):

    registros_path = {'1': 'registros_receita.csv',
                      '2': 'registros_despesa.csv',
                      '3': 'registros_investimento.csv'
                      }

    while True:

        # fazer validao
        operacao = input('''Informe o tipo de operação do registro que deseja {acao_realizada} ou se 
                            deseja cancelar: 
                        
                        [1] RECEITA                              
                        [2] DESPESA
                        [3] INVESTIMENTO
                        [4] CANCELAR''')

        if operacao == '4':

            return None

        elif operacao in registros_path:

            lista_registro = le_arquivo(registros_path[operacao])

            if not lista_registro:

                print("Não há registros com esse tipo de operação! ")
                return None

            data = []
            print("Informe um intervalo de data em que a operação desejada pertence \n")
            for i in ["antiga", "recente"]:
                print("Para a data mais antiga informe \n")  # O dia,mes ano
                for tempo in ['dia', 'mes', 'ano']:

                    data.append(valida_data(tempo))
                    # imaginar que em um app o usuario escolheria um intervalo
                    # de data em um calendario

            data = tuple(data)
            # seleciona os registros ques estao neste intevalo
            # aqui da pra usar funçao lambda e o filter
            # depois de selecionado printa os 5 primeiros registros dessa lista (para nao ficar muito grande
            # a mensagem na tela), o usuario retorna entao o id
        else:
            print("Opção inválida, informe a opção novamente!")
            continue

        # funcao_q_verifca quantas opcoes de registros com tal operação


def get_id(acao_realizada):
    """
    Função que retorna o id a ser atualizado/deletado
    espeficicando o tipo de operacaçao, a data, e a despesa
    """

    id = mostrar_opcoes(acao_realizada)

    return id


def deletar_registro():

    id = get_id()

    # Obter o ID do registro a ser deletado
    id = int(input("Digite o ID do registro a ser deletado: "))

    # Deletar o registro do arquivo
    with open("registros/registros_{operacao}.csv", "r") as arquivo:
        # Ler as linhas do arquivo
        linhas = arquivo.readlines()

    # Deletar o registro
    del linhas[id]

    # Salvar o arquivo
    with open("registros/registros_{operacao}.csv", "w") as arquivo:
        arquivo.writelines(linhas)
