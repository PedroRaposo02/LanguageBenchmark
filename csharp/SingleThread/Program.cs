using System;

public class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("\n\n-----------------------------------");
        Console.WriteLine("\nC# Single Threaded Script");
        Console.WriteLine("\n-----------------------------------\n\n");

        string basePath = args.Length > 0 ? args[0] : "../";
        string inputFile = args.Length > 1 ? args[1] : "data/biggerSample.txt";

        string inputFileName = Path.Combine(basePath, inputFile);
        string outputFileName = Path.Combine(basePath, "data", "output.txt");

        ReadWriteFile(inputFileName, outputFileName);
    }

    static void ReadWriteFile(string inputPath, string outputPath)
    {
        try
        {
            Console.WriteLine($"Reading and Writing file...");
            using (StreamReader reader = new StreamReader(inputPath))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    File.AppendAllText(outputPath, line + Environment.NewLine);
                }
            }

            Console.WriteLine("Done!");

        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
            System.Environment.Exit(1);
        }
    }
}