package main

import (
	"io/ioutil"
	"log"
	"path/filepath"
	"time"
)

func readAndWriteFile(inputPath, outputPath string) error {
	// Ler o conteúdo do arquivo de entrada
	content, err := ioutil.ReadFile(inputPath)
	if err != nil {
		return err
	}

	// Escrever o conteúdo no arquivo de saída
	err = ioutil.WriteFile(outputPath, content, 0644)
	if err != nil {
		return err
	}

	return nil
}

func run() {
	inputPath := filepath.Join("data", "sample.txt")
	outputPath := filepath.Join("data", "outputGo.txt")

	// Medindo o tempo de execução
	startTime := time.Now()

	err := readAndWriteFile(inputPath, outputPath)
	if err != nil {
		log.Fatal("Erro ao processar o arquivo:", err)
	}

	// Exibindo o tempo de execução
	elapsed := time.Since(startTime)
	log.Printf("Arquivo processado em: %s", elapsed)
}
