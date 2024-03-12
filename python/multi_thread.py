import time
from threading import Thread
    
def convert_multi_threaded():
    def convert_single_threaded():
        start_time = time.time()

        #! Lógica de conversão de documentos aqui

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tempo de execução (single-threaded): {execution_time} segundos")
    start_time = time.time()

    # Criar threads para simular conversão simultânea
    threads = [Thread(target=convert_single_threaded) for _ in range(5)]  # Exemplo com 5 threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução (multi-threaded): {execution_time} segundos")

if __name__ == "__main__":
    convert_multi_threaded()
