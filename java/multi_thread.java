import java.util.concurrent.CountDownLatch;

public class multi_thread {

    private static void convertMultiThreaded() {
        long startTime = System.currentTimeMillis();

        // Criar wait group para aguardar a conclusão de todas as threads
        int numberOfThreads = 5;  // Exemplo com 5 threads
        Thread[] threads = new Thread[numberOfThreads];
        CountDownLatch latch = new CountDownLatch(numberOfThreads);

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                //! Chamar a função de conversão
                latch.countDown();
            });
            threads[i].start();
        }

        // Aguardar a conclusão de todas as threads
        try {
            latch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        long endTime = System.currentTimeMillis();
        double executionTime = (endTime - startTime) / 1000.0; // em segundos
        System.out.println("Tempo de execução (multi-threaded): " + executionTime + " segundos");
    }

    public static void main(String[] args) {
        convertMultiThreaded();
    }
}
