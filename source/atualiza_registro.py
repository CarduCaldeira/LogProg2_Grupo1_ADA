import os
import csv
import datetime
from utils import *


def ler_arquivo(path: str) -> list:
    """Função que recebe o caminho do arquivo csv com os registros salvos 
    e retorna uma lista com os registros salvos caso tal csv exista, 
    caso contrario retorna None"""

    if os.path.exists(path):
        with open(path, 'r') as file:
            registros = csv.reader(file)

        return registros
    else:
        return None


def mostrar_opcoes(acao_realizada):
    """

    """
    registros_path = {
        '1': '../registros/registros_receita.csv',
        '2': '../registros/registros_despesa.csv',
        '3': '../registros/registros_investimento.csv'
    }

    while True:

        operacao = input('''
    INFORME O TIPO DE REGISTRO QUE DESEJA EXECUTAR:
    
    [1] RECEITA                               
    [2] DESPESA
    [3] INVESTIMENTO
    [4] CANCELAR
                        
    ''')

        try:
            if operacao in registros_path:
                limpar_tela()
                tracos()
                registros_path[operacao]()
                break

            else:
                tentativas += 1

                if tentativas == 3:
                    print("Você atingiu o número máximo de tentativas.")
                    encerrar_programa()
                else:
                    limpar_tela()
                    print(
                        f"'{operacao}' Não é uma opção válida. Você tem mais {3 - tentativas} {'tentativa' if tentativas == 2 else 'tentativas'}.")
                    time.sleep(2)
                    limpar_tela()
                    tela_inicial()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        if operacao == '4':
            return None

        elif operacao in registros_path:

            lista_registro = ler_arquivo(registros_path[operacao])

            if not lista_registro:

                print("Não há registros com esse tipo de operação! ")
                return None

            datas = dict()

            print("Informe um intervalo de data em que a operação desejada pertence \n")

            for i in ["antiga", "recente"]:

                print("Para a data mais {i} informe \n")

                data = []
                for tempo in ['dia', 'mes', 'ano']:

                    data.append(valida_data(tempo, acao_realizada))

                datas[i] = tuple(data)

            ids = seleciona_id_registros(
                lista_registro, datas["antiga"], datas["recente"])
            id = mostra_registros(ids, lista_registro)
            return id, lista_registro

        else:
            print("Opção inválida, informe a opção novamente!")
            continue


def seleciona_id_registros(lista_registro, data_antiga, data_recente):

    lista_len = list(range(len(lista_registro)))
    data_recente = datetime(data_recente[2], data_recente[1], data_recente[0])
    data_antiga = datetime(data_antiga[2], data_antiga[1], data_antiga[0])

    def f(i): return lista_registro[i]
    def g(registro): return registro[2]
    def h(data): return datetime(data[2], data[1], data[0])
    def r(data): return data_antiga <= data <= data_recente

    registros_id = list(filter(lambda i: r(h(g(f(i)))), lista_len))
    return registros_id


def mostra_registros(ids, lista_registro):

    def x(i): return datetime(
        lista_registro[i][2][2], lista_registro[i][2][1], lista_registro[i][2][0])

    ids_sorted = sorted(ids, key=x, reverse=True)

    if len(ids_sorted) < 5:
        repeticoes = len(ids_sorted)
    else:
        repeticoes = 5

    for j, i in enumerate(ids_sorted[:repeticoes]):

        operacao = lista_registro[i][0]

        mensagem = f"[{j+1}] Tipo de operação:{lista_registro[i][0]}, Valor:{lista_registro[i][1]},"
        + f"Data:{lista_registro[i][2][0]}/{lista_registro[i][2][1]}/{lista_registro[i][2][2]}"

        if operacao == 'investimento':
            print(mensagem + f", Juros:{lista_registro[i][3]} \n")
        else:
            print(mensagem + "\n")

        # fazer validação
        tipo = input("Digite o numero do registro desejado")
        return tipo


def atualiza_registros():
    # retorna o (id, lista_de_registros) caso exista algum registro caso contrario retorna None
    id_tuple = mostra_opcoes()

    if id_tuple:
        id, lista_registros = id_tuple
        # registro = chama a função que pega o novo registro e retorna a lista com as informaçoes
        # lista_registros[id] = registro
        print("Registro atualizado")
