using System;
using System.Diagnostics;
using System.Threading;

private static void ConvertSingleThreaded()
{
    Console.WriteLine("Executing ConvertSingleThreaded...");

    Stopwatch stopwatch = Stopwatch.StartNew();

    // !Lógica de conversão de documentos aqui

    stopwatch.Stop();
    Console.WriteLine($"C# Tempo de execução (single-threaded): {stopwatch.Elapsed.TotalSeconds} segundos");
}

private static void Main()
{
    ConvertSingleThreaded();
}

Main();