import datetime


def determina_data():
    """
    Obtem a data de realização do registro
    retornando um tupla no formato (dia, mes, ano) 
    """

    data = datetime.now().date()
    return data.day, data.month, data.year

def valida_digito(mensagem:str, mensagem_erro:str):
    """
    Faz a validacao do valor informado pelo usuario, caso nao seja
    um numero a conversao para float ira gerar um erro, que faz a função
    requisitar novamente o valor numerico. Caso o valor nao seja maior que zero
    a função  requisitara novamente o valor numerico
    """

    while True:
        try:
            despesa = float(input(mensagem))   
        except ValueError:
            print(mensagem_erro)
            continue
        else:
            if despesa > 0:
                return despesa 
            else:
                print("O valor deve ser maior que zero.")

def valida_data(data):
    """valor_min = input(f"Informe o {tempo} do registro que deseja {acao_realizada}: ")"""
