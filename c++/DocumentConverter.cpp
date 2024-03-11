#include <iostream>
#include <thread>
#include <vector>
#include <chrono>

void convertSingleThreaded() {
    auto startTime = std::chrono::high_resolution_clock::now();

    // Lógica de conversão de documentos aqui

    auto endTime = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = endTime - startTime;
    std::cout << "Tempo de execução (single-threaded): " << duration.count() << " segundos" << std::endl;
}

void convertMultiThreaded() {
    auto startTime = std::chrono::high_resolution_clock::now();

    // Criar threads para simular conversão simultânea
    int numberOfThreads = 5;  // Exemplo com 5 threads
    std::vector<std::thread> threads;
    for (int i = 0; i < numberOfThreads; ++i) {
        threads.emplace_back([]() {
            // Lógica de conversão de documentos aqui
        });
    }

    // Aguardar a conclusão de todas as threads
    for (std::thread& thread : threads) {
        thread.join();
    }

    auto endTime = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = endTime - startTime;
    std::cout << "Tempo de execução (multi-threaded): " << duration.count() << " segundos" << std::endl;
}

int main() {
    convertSingleThreaded();
    return 0;
}
