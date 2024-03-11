#include <iostream>
#include <fstream>
#include <chrono>

void readAndWriteFile(const std::string& inputPath, const std::string& outputPath) {
    // Ler o conteúdo do arquivo de entrada
    std::ifstream inputFile(inputPath);
    std::string content((std::istreambuf_iterator<char>(inputFile)),
                        (std::istreambuf_iterator<char>()));

    // Escrever o conteúdo no arquivo de saída
    std::ofstream outputFile(outputPath);
    outputFile << content;
}

int main() {
    std::string inputPath = "data/sample.txt";
    std::string outputPath = "data/outputC++.txt";

    // Medindo o tempo de execução
    auto startTime = std::chrono::high_resolution_clock::now();

    readAndWriteFile(inputPath, outputPath);

    // Exibindo o tempo de execução
    auto endTime = std::chrono::high_resolution_clock::now();
    auto elapsedTime = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);
    std::cout << "Arquivo processado em: " << elapsedTime.count() << " milissegundos" << std::endl;

    return 0;
}
