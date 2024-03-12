import subprocess
import time

def execute_script(script_path):
    start_time = time.time()
    subprocess.run(['./' + script_path], cwd=script_path[:-3])
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos\n")

def main():
    print("Executing Single-Threaded Scripts:")
    execute_script('c++/single_threaded.cpp')
    execute_script('c#/single_threaded.cs')
    execute_script('golang/single_threaded.go')
    execute_script('java/SingleThreaded.java')
    execute_script('python/single_threaded.py')
    execute_script('rust/single_threaded.rs')

    print("Executing Multi-Threaded Scripts:")
    execute_script('c++/multi_threaded.cpp')
    execute_script('c#/multi_threaded.cs')
    execute_script('golang/multi_threaded.go')
    execute_script('java/MultiThreaded.java')
    execute_script('python/multi_threaded.py')
    execute_script('rust/multi_threaded.rs')

if __name__ == "__main__":
    main()