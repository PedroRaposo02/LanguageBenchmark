use std::thread;
use std::time::Instant;

fn convert_single_threaded() {
    let start_time = Instant::now();

    // Lógica de conversão de documentos aqui

    let end_time = Instant::now();
    let execution_time = end_time.duration_since(start_time);
    println!("Tempo de execução (single-threaded): {:?}", execution_time);
}

fn convert_multi_threaded() {
    let start_time = Instant::now();

    // Criar threads para simular conversão simultânea
    let number_of_threads = 5;  // Exemplo com 5 threads
    let handles: Vec<_> = (0..number_of_threads)
        .map(|_| {
            thread::spawn(|| {
                // Lógica de conversão de documentos aqui
            })
        })
        .collect();

    // Aguardar a conclusão de todas as threads
    for handle in handles {
        handle.join().unwrap();
    }

    let end_time = Instant::now();
    let execution_time = end_time.duration_since(start_time);
    println!("Tempo de execução (multi-threaded): {:?}", execution_time);
}

fn main() {
    convert_single_threaded();
}
