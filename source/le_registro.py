def le_registro():

  repeat_question = True

  while repeat_question:
    menu_leitura = input('''Menu de leitura de registros:
                       
                       [1] DESPESA
                       [2] RECEITA
                       [3] INVESTIMENTOS
                       [4] CANCELAR
                       
                          Digite o numero da opção de deseja acessar: ''')
  
    if menu_leitura not in ['1','2','3','4']:
        print("Entrada invalida")

    elif menu_leitura == '1':
        leitura_despesa()

    elif menu_leitura == '2':
        leitura_receita()

    elif menu_leitura == '3':
        leitura_investimentos()




def leitura_despesa():
    with open("../registros/registros_despesa.csv", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            print(linha)

def leitura_receita():
   with open("../registros/registros_receita.csv", "r") as arquivo:
      linhas = arquivo.readlines()

      for linha in linhas:
            print(linha)

def leitura_investimentos():
   with open("../registros/investimento.csv", "r") as arquivo:
      
        for linha in linhas:
           print(linha)