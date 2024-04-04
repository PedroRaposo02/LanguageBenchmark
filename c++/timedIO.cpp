#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <chrono>

void readAndWriteFile(const std::string &inputPath, const std::string &outputPath) {
    std::cout << "\nReading file...";

    // Start read timer
    auto read_start = std::chrono::steady_clock::now();

    std::ifstream inputFile(inputPath, std::ios::binary | std::ios::ate);
    if (!inputFile.is_open()) {
        std::cerr << "\nError: file not found" << std::endl;
        return;
    }

    // Get file size and resize vector accordingly
    std::streamsize size = inputFile.tellg();
    inputFile.seekg(0, std::ios::beg);

    std::vector<char> buffer(size);
    if (inputFile.read(buffer.data(), size)) {
        // Successfully read file into buffer
    } else {
        std::cerr << "\nError reading file into memory\n";
        return;
    }

    // End read timer
    auto read_end = std::chrono::steady_clock::now();
    auto read_duration = std::chrono::duration_cast<std::chrono::milliseconds>(read_end - read_start);
    std::cout << "\nReading time: " << read_duration.count() << " ms\n";

    // Start write timer
    auto write_start = std::chrono::steady_clock::now();

    std::ofstream outputFile(outputPath, std::ios::binary);
    if (!outputFile.is_open()) {
        std::cerr << "\nError opening output file: " << outputPath << "\n";
        return;
    }

    std::cout << "\nWriting file...";
    outputFile.write(buffer.data(), size);

    // End write timer
    auto write_end = std::chrono::steady_clock::now();
    auto write_duration = std::chrono::duration_cast<std::chrono::milliseconds>(write_end - write_start);
    std::cout << "\nWriting time: " << write_duration.count() << " ms\n";

    std::cout << "\nDone!\n";
}

int main(int argc, char *argv[])
{
    std::cout << "\n\n-----------------------------------\n";
    std::cout << "C++ Timed Script\n";
    std::cout << "-----------------------------------\n";

    std::string base_path = (argc > 1) ? argv[1] : "../";
    std::string input_file = (argc > 2) ? argv[2] : "biggerSample.txt";
    std::string file_path = base_path + '/' + input_file;
    std::string output_file = base_path + "/data/output.txt";

    readAndWriteFile(file_path, output_file);
    return 0;
}
