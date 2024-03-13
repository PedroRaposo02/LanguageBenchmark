use std::env;
use std::fs::{self, File};
use std::io::{self, Read, Write};
use std::path::Path;

fn read_write_file(input_path: &Path, output_path: &Path) -> io::Result<()> {
    let mut input_file = File::open(input_path)?;
    let mut output_file = File::create(output_path)?;

    let mut buffer = String::new();
    println!("Reading file...");
    input_file.read_to_string(&mut buffer)?;

    println!("Writing file...");
    output_file.write_all(buffer.as_bytes())?;

    Ok(())
}

fn main() -> io::Result<()> {
    println!("\n\n-----------------------------------");
    println!("\nRust Single Threaded Script");
    println!("\n-----------------------------------\n\n");

    let args: Vec<String> = env::args().collect();

    print!("Arguments: ");
    println!("{:?}", args);

    let base_path = if args.len() > 1 { &args[1] } else { "../../../" };

    let input_file = if args.len() > 2 {
        &args[2]
    } else {
        "data/biggerSample.txt"
    };

    let input_file_path = Path::new(base_path).join(input_file);
    let output_file_path = Path::new(base_path).join("data").join("outputRust.txt");

    print!("Input file: ");
    println!("{}", input_file_path.display());

    print!("Output file: ");
    println!("{}", output_file_path.display());

    read_write_file(&input_file_path, &output_file_path)?;

    Ok(())
}
