from utils import *
from cria_registro import cria_registro
from le_registro import le_registro
from deletar_registro import deletar_registro
from atualizar_registro import atualizar_registro
from mostra_features import mostra_features
from exporta_relatorio import exporta_relatorio
from encerrar_programa import encerrar_programa




def main():
    
    operacoes = {
        1: cria_registro,
        2: le_registro,
        3: atualizar_registro,
        4: deletar_registro,
        5: mostra_features,
        6: exporta_relatorio,
        7: encerrar_programa
    }

    tentativas = 0
    
    operacao = tela_inicial()
    
    try:
        if operacao in operacoes:
            limpar_tela()
            tracos()
            operacoes[operacao]()

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

if __name__ == "__main__":
    main()
