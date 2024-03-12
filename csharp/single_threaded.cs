using System;
using System.Diagnostics;
using System.Threading;

class Program
{
    static void ConvertSingleThreaded()
    {
        Stopwatch stopwatch = Stopwatch.StartNew();

        // !Lógica de conversão de documentos aqui

        stopwatch.Stop();
        Console.WriteLine($"Tempo de execução (single-threaded): {stopwatch.Elapsed.TotalSeconds} segundos");
    }

    static void Main()
    {
        ConvertSingleThreaded();
    }
}
