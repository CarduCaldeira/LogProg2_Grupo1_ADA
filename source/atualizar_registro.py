import os
import csv
import datetime
import time
import re
from cria_registro import cria_registro
from utils import encerrar_programa
from utils import valida_data

def atualizar_registro():
    
    flag_mostra_opcao = mostrar_opcoes()
    
    if flag_mostra_opcao:
        id, operacao = flag_mostra_opcao
        if str(id):
            cria_registro(atualiza = True, id= id)
    
      

def ler_arquivo(path: str) -> list:
    """Função que recebe o caminho do arquivo csv com os registros salvos 
    e retorna uma lista com os registros salvos caso tal csv exista, 
    caso contrario retorna None"""

    if os.path.exists(path):
            file = open(path, 'r', newline='')
            registros = list(csv.reader(file, delimiter=';', lineterminator='\n'))
            return registros
    else:
        return None

def mostrar_opcoes():
    """

    """

    tentativas = 0

    registros_path = {
        '1': '../registros/registros_despesa.csv',
        '2': '../registros/registros_receita.csv',
        '3': '../registros/investimento.csv'}

    while True:

        print("DIGITE UMA DAS OPÇÕES ABAIXO:\n")
        print("[1] ATUALIZAR UM REGISTRO DE DESPESA")
        print("[2] ATUALIZAR UM REGISTRO DE RECEITA")
        print("[3] ATUALIZAR UM REGISTRO DE INVESTIMENTO \n")
        print("[4] SAIR")

        operacao = input()

        #try:
        if operacao == '4':
            encerrar_programa()
            break

        elif operacao in registros_path:

            lista_registro = ler_arquivo(registros_path[operacao])

            if not lista_registro:

                print("Não há registros com esse tipo de operação! \n")
                return None

            datas = dict()

            print(
                "Informe um intervalo de data em que a operação desejada pertence \n")

            for i in ["antiga", "recente"]:

                print(f"Para a data mais {i} informe \n")

                data = []
                for tempo in ['dia', 'mes', 'ano']:

                    data.append(valida_data(tempo))

                datas[i] = datetime.date(data[2], data[1], data[0])
                
            if not datas["antiga"]  <= datas["recente"]:
                print("Periodo invalido")
                return None
                
            ids = selecionar_id_registros(
                lista_registro, datas["antiga"], datas["recente"])
            
            if len(ids)== 0:
                print("Sem registros nesse periodo")
                return None
            
            id = mostrar_registros(ids, lista_registro)
            return id, operacao

        else:
            tentativas += 1

            if tentativas == 3:
                print("Você atingiu o número máximo de tentativas.")
                encerrar_programa()
            else:
                print(
                    f"'{operacao}' Não é uma opção válida. Você tem mais {3 - tentativas} {'tentativa' if tentativas == 2 else 'tentativas'}.")
                time.sleep(2)
        


def selecionar_id_registros(lista_registro, data_antiga, data_recente):
    """
    
    """
    lista_len = list(range(len(lista_registro)))

    def f(i): return lista_registro[i]
    def g(registro): return registro[2]
    def s(data): return re.findall(r'\d+', data)
    def h(data): return datetime.date(int(data[2]), int(data[1]), int(data[0]))
    def r(data): return data_antiga <= data <= data_recente

    registros_id = list(filter(lambda i: r(h(s(g(f(i))))), lista_len))
    return registros_id

1
def mostrar_registros(ids, lista_registro):
    """

    """
    def x(i): return  lista_registro[i][2]
    def y(string_data): return re.findall(r'\d+', string_data)
    def z(lista): return datetime.date(
        int(lista[2]), int(lista[1]), int(lista[0]))
    
    def comp(i): return z(y(x(i)))

    ids_sorted = sorted(ids, key=comp, reverse=True)

    if len(ids_sorted) < 5:
        repeticoes = len(ids_sorted)
    else:
        repeticoes = 5


    for j, i in enumerate(ids_sorted[:repeticoes]):

        operacao = lista_registro[i][0]

        mensagem = (f"\n [{j+1}] Tipo de operação:{lista_registro[i][0]}, Valor:{lista_registro[i][1]},"
        f"Data:{lista_registro[i][2]}")

        if operacao == 'investimento':
            print(mensagem + f", Juros:{lista_registro[i][3]}")
        else:
            print(mensagem)
    
    while True:
        try:
            escolha = int(input("\n Digite o numero do registro desejado \n"))
            if escolha not in list(range(1,repeticoes+1)):
                print("Digite um número inteiro válido \n")
            else:
                break
        except ValueError:
            print("Digite um número inteiro válido \n")
            continue       
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            continue
        
    return ids_sorted[escolha-1]



