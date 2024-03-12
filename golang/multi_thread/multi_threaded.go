package multi_thread

import (
	"fmt"
	"sync"
	"time"
)


func convertMultiThreaded() {
	startTime := time.Now()

	// Criar wait group para aguardar a conclusão de todas as goroutines
	var wg sync.WaitGroup

	// Criar goroutines para simular conversão simultânea
	numOfGoroutines := 5 // Exemplo com 5 goroutines
	for i := 0; i < numOfGoroutines; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			// !Lógica de conversão de documentos aqui
		}()
	}

	// Aguardar a conclusão de todas as goroutines
	wg.Wait()

	endTime := time.Now()
	elapsed := endTime.Sub(startTime)
	fmt.Printf("Tempo de execução (multi-threaded): %s\n", elapsed)
}

func main() {
	convertMultiThreaded()
}
