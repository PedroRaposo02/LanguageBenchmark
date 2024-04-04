using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.IO;

public class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("\n-----------------------------------");
        Console.WriteLine("C# Timed Script");
        Console.WriteLine("-----------------------------------\n");

        string basePath = args.Length > 0 ? args[0] : "../";
        string inputFile = args.Length > 1 ? args[1] : "data/biggerSample.txt";

        string inputFileName = Path.Combine(basePath, inputFile);
        string outputFileName = Path.Combine(basePath, "data", "output.txt");

        Console.WriteLine($"Input file: {inputFileName}");
        Console.WriteLine($"Output file: {outputFileName}");

        ReadWriteFile(inputFileName, outputFileName);
    }

    static void ReadWriteFile(string inputPath, string outputPath)
    {
        try
        {
            Stopwatch readStopwatch = new Stopwatch();
            Stopwatch writeStopwatch = new Stopwatch();

            List<string> lines = new List<string>();

            Console.WriteLine($"Reading file...");
            readStopwatch.Start();
            using (StreamReader reader = new StreamReader(inputPath))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    lines.Add(line); // Store each line in the list
                }
            }
            readStopwatch.Stop();

            Console.WriteLine($"Writing file...");
            writeStopwatch.Start();
            using (StreamWriter writer = new StreamWriter(outputPath))
            {
                foreach (string line in lines)
                {
                    writer.WriteLine(line); // Write each line to the output file
                }
            }
            writeStopwatch.Stop();

            Console.WriteLine($"Reading time: {readStopwatch.ElapsedMilliseconds} ms");
            Console.WriteLine($"Writing time: {writeStopwatch.ElapsedMilliseconds} ms");

            Console.WriteLine("Done!");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
            Environment.Exit(1);
        }
    }
}
