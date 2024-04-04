import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;

public class TimedIO {

    public static void ReadWriteFile(String inputFileName, String outputFileName) {
        StringBuilder content = new StringBuilder(); // To store the content of the file

        try {
            long startRead = System.nanoTime();
            System.out.println("Reading file...");
            BufferedReader reader = new BufferedReader(new FileReader(inputFileName));
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n"); // Append each line to the content
            }
            reader.close();
            long endRead = System.nanoTime();
            double readTime = (endRead - startRead) / 1e6; // Convert nanoseconds to milliseconds

            long startWrite = System.nanoTime();
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFileName));
            System.out.println("Writing file...");
            writer.write(content.toString()); // Write the content to the output file
            writer.close();
            long endWrite = System.nanoTime();
            double writeTime = (endWrite - startWrite) / 1e6; // Convert nanoseconds to milliseconds

            System.out.println("Done!");
            System.out.println("Reading time: " + readTime + " ms");
            System.out.println("Writing time: " + writeTime + " ms");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        System.out.println("\n-----------------------------------");
        System.out.println("Java Timed Script");
        System.out.println("-----------------------------------\n");
        String basePath = args.length > 0 ? args[0] : "../";

        String inputFile = args.length > 1 ? args[1] : "data/biggerSample.txt";

        String inputFileName = Paths.get(basePath, inputFile).toString();
        String outputFileName = Paths.get(basePath, "data", "output.txt").toString();

        ReadWriteFile(inputFileName, outputFileName);
    }
}
