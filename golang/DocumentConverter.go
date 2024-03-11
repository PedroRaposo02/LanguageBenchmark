package main

import (
	"fmt"
	"time"
)

func convertSingleThreaded() {
	startTime := time.Now()

	// Lógica de conversão de documentos aqui

	elapsed := time.Since(startTime)
	fmt.Printf("Tempo de execução (single-threaded): %s\n", elapsed)
}

func main() {
	convertSingleThreaded()
}
