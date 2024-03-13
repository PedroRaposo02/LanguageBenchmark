package main

import (
	"log"
	"os"
	"path/filepath"
	"strings"
)

func readFile(file_path string, output_path string) error {
	// Ler o conteúdo do arquivo de entrada

	print("Reading file...\n")

	content, err := os.ReadFile(file_path)
	if err != nil {
		return err
	}

	// Escrever o conteúdo no arquivo de saída
	file, err := os.Create(output_path)

	if err != nil {
		log.Fatal(err)
	}

	print("Writing to file...\n")

	_, err = file.Write(content)
	if err != nil {
		return err
	}

	print("Done!\n")

	if err := file.Close(); err != nil {
		log.Fatal(err)
	}

	return nil
}

func main() {
	print("\n\n-----------------------------------")
	print("\nGo Single Threaded Script")
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

	file_path = strings.Trim(file_path, "'")

	output_path := filepath.Join(base_path, "data", "outputGo.txt")

	err := readFile(file_path, output_path)

	if err != nil {
		log.Fatal(err)
	}
}
