import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class simpleIO {

    public static void readAndWriteFile(String inputPath, String outputPath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(inputPath));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath))) {

            String line;
            while ((line = reader.readLine()) != null) {
                // Escrever cada linha no novo arquivo
                writer.write(line);
                writer.newLine();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String inputFile = "data\\biggerSample.txt";
        String outputFile = "data/outputJava.txt";

        // Medindo o tempo de execução
        long startTime = System.currentTimeMillis();
        readAndWriteFile(inputFile, outputFile);
        long endTime = System.currentTimeMillis();

        // Exibindo o tempo de execução
        double executionTime = (endTime - startTime) / 1000.0; // em segundos
        System.out.println("Tempo de execução: " + executionTime + " segundos");
    }
}
