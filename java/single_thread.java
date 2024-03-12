import java.util.concurrent.CountDownLatch;

public class single_thread {

    public static void convertSingleThreaded() {
        long startTime = System.currentTimeMillis();

        //! Lógica de conversão de documentos aqui

        long endTime = System.currentTimeMillis();
        double executionTime = (endTime - startTime) / 1000.0; // em segundos
        System.out.println("Tempo de execução (single-threaded): " + executionTime + " segundos");
    }

    public static void main(String[] args) {
        convertSingleThreaded();
    }
}
