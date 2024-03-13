import subprocess
import time
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def execute_script(
    script_path,
    language,
    compile_command=None,
    run_command=None,
    output_file=None,
    input_file=None,
):
    try:
        base_path, script_name = os.path.split(script_path)
        # strip file extension
        stripped_name = script_name.split(".")[0]

        os.chdir(base_path)

        print(f"Executing {script_name}...")

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
                return

        command = (
            f"{run_command} {ROOT_DIR}"
            if run_command
            else f"./{stripped_name} {ROOT_DIR}"
        )
        if input_file:
            command = f"{command} {input_file}"

        err_code = "0"
        try:
            print(f"Running command: {command}")
            print(f"Current working directory: {os.getcwd()}")
            start_time = time.time()
            result = subprocess.run(
                command, check=True, text=True
            )
            end_time = time.time()

            err_code = result.returncode
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o script {script_name} em {language}: {e}")
            return

        execution_time = end_time - start_time
        print(
            f"Tempo de execução do script em {language}: {execution_time:.6f} segundos\n"
        )
        os.chdir(ROOT_DIR)

        input_file = (
            input_file if input_file else os.path.join("data", "large_file.txt")
        )

        input_file_name = os.path.basename(input_file)

        if output_file:
            with open(output_file, "a") as file:
                file.write(
                    f"| {language:<20}{script_name:<30}{input_file_name:<20}{err_code:<15}{execution_time:.6f} segundos\n"
                )

    except Exception as e:
        print(f"Erro ao executar o script {script_name} em {language}: {e}")

    os.chdir(ROOT_DIR)


def main():
    # Single-Threaded Scripts
    print("Executing Single-Threaded Scripts:")
    single_threaded_txt_path = "./data/single_threaded.txt"
    with open(single_threaded_txt_path, "w") as file:
        file.write("---------------- Single Thread ----------------\n".ljust(31))
        file.write(
            "{language:<20}{script_name:<30}{input_file:<20}{err_code:<15}{execution_time}\n".format(
                language="| Linguagem",
                script_name="| Script",
                input_file="| Input File",
                err_code="| Error Code",
                execution_time="| Tempo de Execucao |",
            )
        )

    execute_script(
        "c++/single_threaded.cpp",
        "c++",
        "g++ single_threaded.cpp -o single_threaded",
        "",
        "./data/single_threaded.txt",
        os.path.join("data", "huge_file.txt"),
    )
    execute_script(
        "python/single_threaded.py",
        "python",
        "",
        "python single_threaded.py",
        "./data/single_threaded.txt",
        os.path.join("data", "huge_file.txt"),
    )
    execute_script(
        "rust/src/bin/single_threaded.rs",
        "rust",
        "cargo build",
        "cargo run --bin single_threaded --",
        "./data/single_threaded.txt",
        os.path.join("data", "huge_file.txt"),
    )
    execute_script(
        "java/SingleThreaded.java",
        "java",
        "javac SingleThreaded.java",
        "java SingleThreaded",
        "./data/single_threaded.txt",
        os.path.join("data", "huge_file.txt"),
    )
    execute_script(
        "golang/single_thread/single_threaded.go",
        "golang",
        "go build single_threaded.go",
        "./single_threaded",
        "./data/single_threaded.txt",
        os.path.join(ROOT_DIR, "data", "huge_file.txt"),
    )
    execute_script(
        "csharp/SingleThread/Program.cs",
        "C#",
        "dotnet build",
        "dotnet run --",
        "./data/single_threaded.txt",
        os.path.join("data", "large_file.txt"),
    )

    # Multi-Threaded Scripts
    print("Executing Multi-Threaded Scripts:")
    multi_threaded_txt_path = "./data/multi_threaded.txt"
    with open(multi_threaded_txt_path, "w") as file:
        file.write("---------------- Multi Thread ----------------\n".ljust(31))
        file.write(
            "{language:<10} {script_name:<20} {execution_time} segundos\n".format(
                language="Linguagem",
                script_name="Script",
                execution_time="Tempo de Execucao",
            )
        )

    execute_script(
        "c++/multi_threaded.cpp",
        "c++",
        "g++ multi_threaded.cpp -o multi_threaded -pthread",
        "",
        "./data/multi_threaded.txt",
    )
    execute_script(
        "csharp/multi_threaded.csx",
        "csharp",
        "",
        "dotnet script multi_threaded.csx",
        "./data/multi_threaded.txt",
    )
    execute_script(
        "golang/multi_thread/multi_threaded.go",
        "golang",
        "go build multi_threaded.go",
        "./multi_threaded",
        "./data/multi_threaded.txt",
    )
    execute_script(
        "java/MultiThreaded.java",
        "java",
        "javac MultiThreaded.java",
        "java MultiThreaded",
        "./data/multi_threaded.txt",
    )
    execute_script(
        "python/multi_threaded.py",
        "python",
        "",
        "python multi_threaded.py",
        "./data/multi_threaded.txt",
    )
    execute_script(
        "rust/src/bin/multi_threaded.rs",
        "rust",
        "cargo build",
        "cargo run --bin multi_threaded",
        "./data/multi_threaded.txt",
    )


def executeSingleScript():
    # Single-Threaded Scripts
    print("Executing Single-Threaded Scripts:")
    single_threaded_txt_path = "./data/single_threaded.txt"
    with open(single_threaded_txt_path, "w") as file:
        file.write("---------------- Single Thread ----------------\n".ljust(31))
        file.write(
            "{language:<20}{script_name:<30}{input_file:<20}{err_code:<15}{execution_time}\n".format(
                language="| Linguagem",
                script_name="| Script",
                input_file="| Input File",
                err_code="| Error Code",
                execution_time="| Tempo de Execucao |",
            )
        )
    execute_script(
        "csharp/SingleThread/Program.cs",
        "C#",
        "dotnet build",
        "dotnet run --",
        "./data/single_threaded.txt",
        os.path.join("data", "large_file.txt"),
    )


if __name__ == "__main__":
    # executeSingleScript()
    main()
