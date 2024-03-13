using System;
using System.IO;
using System.Diagnostics;

class simpleIO
{
    static void ReadAndWriteFile(string inputPath, string outputPath)
    {
        // Ler o conteúdo do arquivo de entrada
        string content = File.ReadAllText(inputPath);

        // Escrever o conteúdo no arquivo de saída
        File.WriteAllText(outputPath, content);
    }

    static void Main()
    {
        string inputPath = Path.Combine("..", "data", "sample.txt");
        string outputPath = Path.Combine("..", "data", "outputCSharp.txt");

        // Medindo o tempo de execução
        Stopwatch stopwatch = Stopwatch.StartNew();

        ReadAndWriteFile(inputPath, outputPath);

        // Exibindo o tempo de execução
        stopwatch.Stop();
        Console.WriteLine("Arquivo processado em: " + stopwatch.Elapsed);
    }
}
