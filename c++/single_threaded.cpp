#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

void readAndWriteFile(const std::string &inputPath, const std::string &outputPath)
{
    // Ler o conteúdo do arquivo de entrada
    std::cout << "\nReading file...";

    std::ifstream inputFile(inputPath);
    if (!inputFile.is_open())
    {
        std::cerr << "\nError: file not found" << std::endl;
        return;
    }

    std::ofstream output_file(outputPath);
    if (!output_file.is_open()) {
        std::cerr << "\nError opening output file: " << outputPath << "\n";
        return;
    }
    std::cout << "\nWriting file...";
    std::string line;
    while (std::getline(inputFile, line))
    {
        output_file << line << "\n";
    }
    std::cout << "\nDone!\n";
}

int main(int argc, char *argv[])
{
    std::cout << "\n\n-----------------------------------\n";
    std::cout << "\nC++ Single Threaded Script\n";

    std::string base_path = (argc > 1) ? argv[1] : "../";
    std::string input_file = (argc > 2) ? argv[2] : "biggerSample.txt";
    std::string file_path = base_path + '/' + input_file;
    std::string output_file = base_path + "/data/outputCpp.txt";

    readAndWriteFile(file_path, output_file);
    return 0;
}
