import subprocess
import time
import re
import os
from sorter import *


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():

    output_file = "data/results.txt"

    file_dict = [
        os.path.join("data", "small_file.txt"),
        os.path.join("data", "medium_file.txt"),
        os.path.join("data", "large_file.txt"),
        os.path.join("data", "huge_file.txt"),
        # os.path.join("data", "humongous_file.txt"),
        # os.path.join("data", "ginormus_file.txt"),
    ]

    file_dict.reverse()

    write_header(output_file)

    for file in file_dict:
        # continue
        # Single-Threaded Scripts
        executeSingleThreadedScripts(file, output_file)

    filename = "data/results.txt"
    sorted_path = "data/sorted_results.txt"
    sorted_data = read_and_sort_data(filename)
    write_sorted_data(sorted_path, sorted_data)


def execute_script(
    script_path,
    language,
    compile_command=None,
    run_command=None,
    output_file=None,
    input_file=None,
    capture_output=True,
):
    def print_line(
        script_name, input_file_name, err, execution_time, reading_time, writing_time
    ):
        os.chdir(ROOT_DIR)
        if output_file:
            with open(output_file, "a") as file:
                file.write(
                    "{language:<20}{script_name:<30}{input_file_name:<20}{err_code:<15}{execution_time:<25}{reading_time:<25}{writing_time:<25}\n".format(
                        language=f"| {language}",
                        script_name=f"| {script_name}",
                        input_file_name=f"| {input_file_name}",
                        err_code=f"| {err_code}",
                        execution_time=f"| {execution_time:.3f}",
                        reading_time=f"| {reading_time:.3f}",
                        writing_time=f"| {writing_time:.3f}",
                    )
                )

    try:
        os.chdir(ROOT_DIR)

        base_path, script_name = os.path.split(script_path)
        # strip file extension
        stripped_name = script_name.split(".")[0]

        input_file = (
            input_file if input_file else os.path.join("data", "large_file.txt")
        )

        input_file_name = os.path.basename(input_file)

        os.chdir(base_path)

        print(f"Executing {script_name}...")

        err_code = "0"

        if compile_command:
            # Compile the script if a compilation command is provided
            try:
                result = subprocess.run(compile_command, shell=True)
                if result.returncode != 0:
                    print(
                        f"Erro ao compilar o script {script_name} em {language}: {result.stderr}"
                    )
                    return
            except subprocess.CalledProcessError as e:
                print(f"Erro ao compilar o script {script_name} em {language}: {e}")
                err_code = 1

        if err_code != "0":
            print_line(script_name, input_file_name, err_code, 0, 0, 0)
            return

        command = (
            f"{run_command} {ROOT_DIR}"
            if run_command
            else f"./{stripped_name} {ROOT_DIR}"
        )
        if input_file:
            command = f"{command} {input_file}"

        reading_time = 0
        writing_time = 0
        try:
            print(f"Running command: {command}")
            print(f"Current working directory: {os.getcwd()}")

            print("\n-----------------------------------")
            print(f"{language} Timed Script")
            print("-----------------------------------\n")

            start_time = time.time()
            result = subprocess.run(
                command, check=True, text=True, capture_output=capture_output
            )
            end_time = time.time()

            # Capture the output and extract reading and writing times
            stdout_str = result.stdout
            stderr_str = result.stderr
            output = stdout_str if stdout_str else stderr_str
            if capture_output:
                reading_time = float(output.split("Reading time: ")[1].split("ms")[0])
                writing_time = float(output.split("Writing time: ")[1].split("ms")[0])

            print(f"Reading time: {reading_time} milliseconds")
            print(f"Writing time: {writing_time} milliseconds")

            err_code = result.returncode
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o script {script_name} em {language}: {e}")
            err_code = 1

        if err_code != 0:
            print_line(script_name, input_file_name, err_code, 0, 0, 0)
            return

        execution_time = end_time - start_time
        print(
            f"Tempo de execução do script em {language}: {execution_time:.6f} segundos\n"
        )
        os.chdir(ROOT_DIR)

        print_line(
            script_name,
            input_file_name,
            err_code,
            execution_time,
            reading_time,
            writing_time,
        )

    except Exception as e:
        print(f"Erro no script {script_name} em {language}: {e}")
        print_line(script_name, input_file_name, 1, 0, 0, 0)

    os.chdir(ROOT_DIR)


def write_header(output_path):
    with open(output_path, "w") as file:
        file.write(
            "{language:<20}{script_name:<30}{input_file:<20}{err_code:<15}{execution_time:<25}{reading_time:<25}{writing_time:<25}\n".format(
                language="| Linguagem",
                script_name="| Script",
                input_file="| Input File",
                err_code="| Error Code",
                execution_time="| Tempo de Execucao (s)",
                reading_time="| Tempo de Leitura (ms)",
                writing_time="| Tempo de Escrita (ms)",
            )
        )


def executeSingleThreadedScripts(
    input_file="data/huge_file.txt", output_file="data/results.txt"
):
    print("Executing Timed Scripts:")

    execute_script(
        "javascript/timedIO.js",
        "Javascript",
        "",
        "node timedIO.js",
        output_file,
        input_file,
    )
    execute_script(
        "c++/timedIO.cpp",
        "C++",
        "g++ timedIO.cpp -o timedIO",
        "",
        output_file,
        input_file,
    )
    execute_script(
        "golang/timedIO/timedIO.go",
        "Golang",
        "go build timedIO.go",
        "./timedIO",
        output_file,
        input_file,
    )
    execute_script(
        "rust/src/bin/timed_io.rs",
        "Rust",
        "cargo build",
        "cargo run --bin timed_io --",
        output_file,
        input_file,
    )
    execute_script(
        "python/timedIO.py",
        "Python",
        "",
        "python timedIO.py",
        output_file,
        input_file,
    )
    execute_script(
        "java/TimedIO.java",
        "Java",
        "javac TimedIO.java",
        "java TimedIO",
        output_file,
        input_file,
    )
    execute_script(
        "csharp/TimedIO/Program.cs",
        "C#",
        "dotnet build",
        "dotnet run --",
        output_file,
        input_file,
    )

    # ----------------------------------------------------------------


def executeSingleScript(
    input_file="data/huge_file.txt", output_file="data/results.txt"
):
    # Single-Threaded Scripts
    print("Executing Single-Threaded Scripts:")
    single_threaded_txt_path = "./data/single_threaded.txt"
    with open(single_threaded_txt_path, "w") as file:
        file.write(
            "{language:<20}{script_name:<30}{input_file:<20}{err_code:<15}{execution_time:<25}{reading_time:<25}{writing_time:<25}\n".format(
                language="| Linguagem",
                script_name="| Script",
                input_file="| Input File",
                err_code="| Error Code",
                execution_time="| Tempo de Execucao (s)",
                reading_time="| Tempo de Leitura (ms)",
                writing_time="| Tempo de Escrita (ms)",
            )
        )
    execute_script(
        "golang/timedIO/timedIO.go",
        "Golang",
        "go build timedIO.go",
        "./timedIO",
        output_file,
        input_file,
    )

if __name__ == "__main__":
    # executeSingleScript()
    main()
