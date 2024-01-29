from functools import reduce
from source.registro_lista import RegistroLista

# Função de agrupamento usando reduce
def agrupar_registro_por_tipo(registro_lista):
    # Obtém todos os registros da lista
    registro = registro_lista.get_registro()

    # Agrupa os registros por tipo e calcula o total de valores para cada tipo
    agrupamento = reduce(lambda acc, reg: {**acc, reg.tipo: acc.get(reg.tipo, 0) + reg.valor}, registro, {})
    
    return agrupamento

def main():
    # Inicialize outras variáveis e estruturas necessárias
    registro_lista = RegistroLista()

    # Restante do código

    while tentativas < max_tentativas:
        limpar_tela()
        tracos()
        operacao = tela_inicial()

        if operacao in operacoes:
            if operacao == 1:
                cria_registro(registro_lista)
            elif operacao == 2:
                le_registro(registro_lista)
            elif operacao == 3:
                atualizar_registro(registro_lista)
            elif operacao == 4:
                deletar_registro(registro_lista)
            elif operacao == 5:
                mostra_features(registro_lista)
            elif operacao == 6:
                exporta_relatorio(registro_lista)
            elif operacao == 7:
                encerrar_programa(registro_lista)
        else:
            tentativas += 1
            print(f"{operacao} não é uma opção válida. "
                  f"Você tem mais {max_tentativas - tentativas} tentativa{'s' if tentativas != max_tentativas - 1 else ''}.")
            time.sleep(10)

    print("Você atingiu o número máximo de tentativas. Encerrando o programa.")
    time.sleep(2)
    encerrar_programa(registro_lista)

if __name__ == "__main__":
    main()