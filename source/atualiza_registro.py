import datetime
import os
import csv
from utils import valida_data, determina_data

def le_arquivo(path:str):

    """Função que recebe o caminho do arquivo csv com os registros salvos 
    e retorna uma lista com os registros salvos caso tal csv exista, 
    caso contrario retorna None"""
    
    if os.path.exists(path):        
        with open(path,'r') as file:       
            registros = csv.reader(file)
       
        return registros  
    else: 
        return None

def mostra_opcoes(acao_realizada):
    """
    
    """
    registros_path = {  '1': '../registros/registros_receita.csv',
                        '2': '../registros/registros_despesa.csv',
                        '3': '../registros/registros_investimento.csv'
                    }
    
    while True:

        # fazer validao
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
            
            datas = dict()

            print("Informe um intervalo de data em que a operação desejada pertence \n")
            
            for i in ["antiga", "recente"]:
                
                print("Para a data mais {i} informe \n")
                
                data = []
                for tempo in ['dia', 'mes', 'ano']:

                    data.append(valida_data(tempo, acao_realizada))

                datas[i] = tuple(data)
            
            ids = seleciona_id_registros(lista_registro, datas["antiga"], datas["recente"])
            id = mostra_registros(ids, lista_registro)
            return id, lista_registro

        else:
            print("Opção inválida, informe a opção novamente!")
            continue
           
def seleciona_id_registros(lista_registro, data_antiga, data_recente):
    
    lista_len = list(range(len(lista_registro)))
    data_recente = datetime(data_recente[2],data_recente[1],data_recente[0])
    data_antiga = datetime(data_antiga[2],data_antiga[1],data_antiga[0])

    f = lambda i: lista_registro[i]
    g = lambda registro: registro[2]
    h = lambda data: datetime(data[2],data[1],data[0])
    r = lambda data: data_antiga <= data <= data_recente

    registros_id = list(filter(lambda i: r(h(g(f(i)))), lista_len))
    return registros_id

def mostra_registros(ids, lista_registro):
    
    x = lambda i : datetime(lista_registro[i][2][2], lista_registro[i][2][1],lista_registro[i][2][0] )
    
    ids_sorted = sorted(ids, key = x, reverse=True)
     
    if len(ids_sorted) < 5:
        repeticoes = len(ids_sorted)
    else:
         repeticoes = 5

    for j,i in enumerate(ids_sorted[:repeticoes]):
       
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
        id, lista_registros =id_tuple
        registro = #chama a função que pega o novo registro e retorna a lista com as informaçoes
        lista_registros[id] = registro
        print("Registro atualizado")


