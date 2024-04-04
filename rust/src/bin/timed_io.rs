use std::env;
use std::fs::File;
use std::io::{self, Read, Write};
use std::path::Path;
use std::time::Instant;

fn read_write_file(input_path: &Path, output_path: &Path) -> io::Result<(u128, u128)> {
    let mut input_file = File::open(input_path)?;
    let mut output_file = File::create(output_path)?;

    let start_read = Instant::now();
    let mut buffer = String::new();
    input_file.read_to_string(&mut buffer)?;
    let read_duration = start_read.elapsed().as_millis();

    let start_write = Instant::now();
    output_file.write_all(buffer.as_bytes())?;
    let write_duration = start_write.elapsed().as_millis();

    Ok((read_duration, write_duration))
}

fn main() -> io::Result<()> {
    println!("\n\n-----------------------------------");
    println!("\nRust Timed Script");
    println!("\n-----------------------------------\n\n");

    let args: Vec<String> = env::args().collect();

    let base_path = if args.len() > 1 { &args[1] } else { "../../../" };

    let input_file = if args.len() > 2 {
        &args[2]
    } else {
        "data/biggerSample.txt"
    };

    let input_file_path = Path::new(base_path).join(input_file);
    let output_file_path = Path::new(base_path).join("data").join("output.txt");

    let (read_time, write_time) = read_write_file(&input_file_path, &output_file_path)?;
    
    println!("Reading time: {} ms", read_time);
    println!("Writing time: {} ms", write_time);

    Ok(())
}
