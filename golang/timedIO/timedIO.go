package main

import (
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func readFile(file_path string, output_path string) error {
	// Ler o conteúdo do arquivo de entrada
	print("Reading file...\n")

	startReading := time.Now()

	content, err := os.ReadFile(file_path)
	if err != nil {
		return err
	}

	readingTime := time.Since(startReading).Milliseconds()

	// Escrever o conteúdo no arquivo de saída
	startWriting := time.Now()

	file, err := os.Create(output_path)
	if err != nil {
		log.Fatal(err)
	}

	print("Writing to file...\n")

	_, err = file.Write(content)
	if err != nil {
		return err
	}

	writingTime := time.Since(startWriting).Milliseconds()

	print("Done!\n")

	if err := file.Close(); err != nil {
		log.Fatal(err)
	}

	print("Reading time: ", readingTime, " ms\n")
	print("Writing time: ", writingTime, " ms\n")

	return nil
}

func main() {
	print("\n\n-----------------------------------")
	print("\nGo Timed Script")
	print("\n-----------------------------------\n\n")

	base_path := ""

	if len(os.Args) < 2 {
		base_path = "../../"
	} else {
		base_path = os.Args[1]
	}

	base_path = strings.Trim(base_path, "'")

	file_path := ""
	if len(os.Args) > 1 {
		file_path = os.Args[2]
	} else {
		file_path = filepath.Join(base_path, "data", "biggerSample.txt")
	}

	file_path = filepath.Join(base_path, file_path)

	output_path := filepath.Join(base_path, "data", "output.txt")

	print("File path: ", file_path, "\n")
	print("Output path: ", output_path, "\n")

	err := readFile(file_path, output_path)

	if err != nil {
		log.Fatal(err)
	}
}
