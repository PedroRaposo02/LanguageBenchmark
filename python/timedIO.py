import os
import sys
import time


def read_write_file(file_path, output_path):
    start_read = time.time()
    print("Reading file...")
    with open(file_path, "r") as file:
        lines = file.readlines()
    read_time = (time.time() - start_read) * 1000

    start_write = time.time()
    print("Writing file...")
    with open(output_path, "w") as file:
        for line in lines:
            file.write(line)
    write_time = (time.time() - start_write) * 1000

    print("Done!")
    return read_time, write_time


def main():
    print("\n-----------------------------------")
    print("Python Timed Script")
    print("-----------------------------------\n")

    base_path = sys.argv[1] if len(sys.argv) > 1 else "../"
    input_file = sys.argv[2] if len(sys.argv) > 2 else "biggerSample.txt"
    file_path = os.path.join(base_path, input_file)
    output_file = os.path.join(base_path, "data", "output.txt")

    read_time, write_time = read_write_file(file_path, output_file)

    print(f"Reading time: {read_time:.3f} ms")
    print(f"Writing time: {write_time:.3f} ms")


if __name__ == "__main__":
    main()
