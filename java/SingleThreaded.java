import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;

public class SingleThreaded {

    public static void ReadWriteFile(String inputFileName, String outputFileName) {
        try {
            System.out.println("Reading file...");
            BufferedReader reader = new BufferedReader(new FileReader(inputFileName));
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFileName));
            String line;
            System.out.println("Writing file...");
            while ((line = reader.readLine()) != null) {
                writer.write(line);
                writer.newLine();
            }
            reader.close();
            writer.close();
            System.out.println("Done!");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        System.out.println("\n\n-----------------------------------");
        System.out.println("\nJava Single Threaded Script");
        System.out.println("\n-----------------------------------\n\n");
        String basePath = args.length > 0 ? args[0] : "../";

        String inputFile = args.length > 1 ? args[1] : "data/biggerSample.txt";

        String inputFileName = Paths.get(basePath, inputFile).toString();
        String outputFileName = Paths.get(basePath, "data", "outputJava.txt").toString();

        ReadWriteFile(inputFileName, outputFileName);
    }
}
