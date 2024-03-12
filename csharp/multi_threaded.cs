using System;
using System.Diagnostics;
using System.Threading;

class Program
{
    static void ConvertMultiThreaded()
    {
        Stopwatch stopwatch = Stopwatch.StartNew();

        // Criar threads para simular conversão simultânea
        int numberOfThreads = 5;  // Exemplo com 5 threads
        Thread[] threads = new Thread[numberOfThreads];
        for (int i = 0; i < numberOfThreads; i++)
        {
            threads[i] = new Thread({
                // !Lógica de conversão de documentos aqui
            });
            threads[i].Start();
        }

        // Aguardar a conclusão de todas as threads
        foreach (Thread thread in threads)
        {
            thread.Join();
        }

        stopwatch.Stop();
        Console.WriteLine($"Tempo de execução (multi-threaded): {stopwatch.Elapsed.TotalSeconds} segundos");
    }

    static void Main()
    {
        ConvertMultiThreaded();
    }
}
