from source.main import main

def cria_registro():

    repeat_question = True

    while repeat_question:

        registro = input("Informe a operação desejada: \n" 
                      "Para despesa digite:     1 \n"
                      "Para receita digite:     2 \n"
                      "Para investimento digite: 3 \n"
                      "Para cancelar:            4 \n")
        

        if registro == '4':
            
            repeat_question = False
            continue
        
        elif registro == '1':
            
            executa_despesa()

        elif registro == '2':
            
            executa_receita()

        elif registro == '3':
            
            executa_investimento()

    main() 

def executa_despesa():
    pass

def executa_receita():
    pass

def  executa_investimento():
    pass

