#include <iostream>
#include <vector>
#include <chrono>

void convertSingleThreaded() {
    auto startTime = std::chrono::high_resolution_clock::now();

    // !Lógica de conversão de documentos aqui

    auto endTime = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = endTime - startTime;
    std::cout << "Tempo de execução (single-threaded): " << duration.count() << " segundos" << std::endl;
}

int main() {
    convertSingleThreaded();
    return 0;
}
