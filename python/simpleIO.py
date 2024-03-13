import time


def read_and_write_file(input_path, output_path):
    # Ler o conteúdo do arquivo de texto
    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Escrever o conteúdo para um novo arquivo
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    input_file = "data/biggerSample.txt"
    output_file = "data/outputPython.txt"

    # Medindo o tempo de execução
    start_time = time.time()
    read_and_write_file(input_file, output_file)
    end_time = time.time()

    # Exibindo o tempo de execução
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
