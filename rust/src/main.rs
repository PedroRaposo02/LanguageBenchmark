use std::fs::File;
use std::io::{self, Read, Write};

fn read_and_write_file(input_path: &str, output_path: &str) -> io::Result<()> {
    // Abrir o arquivo de entrada
    let mut input_file = File::open(input_path)?;

    // Ler o conteúdo do arquivo de entrada
    let mut content = String::new();
    input_file.read_to_string(&mut content)?;

    // Abrir o arquivo de saída
    let mut output_file = File::create(output_path)?;

    // Escrever o conteúdo no arquivo de saída
    output_file.write_all(content.as_bytes())?;

    Ok(())
}

fn main() {
    let input_path = "../data/sample.txt";
    let output_path = "../data/outputRust.txt";

    // Medindo o tempo de execução
    let start_time = std::time::Instant::now();
    match read_and_write_file(input_path, output_path) {
        Ok(()) => {
            let elapsed = start_time.elapsed();
            println!("Arquivo processado em: {:?}", elapsed);
        }
        Err(e) => eprintln!("Erro ao processar o arquivo: {:?}", e),
    }
}
