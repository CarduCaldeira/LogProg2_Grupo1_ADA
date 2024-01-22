from tqdm import tqdm
import time


def encerrar_programa():

    total_iteracoes = 10

    # Criação da barra de carregamento sem a visualização
    barra_carregamento = tqdm(total=total_iteracoes,
                              desc="Encerrando o Sistema",
                              position=0,
                              leave=True)

    for i in range(total_iteracoes):
        # Simulando uma operação demorada
        time.sleep(0.1)

        # Atualizando a barra de carregamento
        barra_carregamento.update(1)

    # Fechando a barra de carregamento
    barra_carregamento.close()
