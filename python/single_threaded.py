import os
import sys


def readWriteFile(file_path, output_path):

    print(f"Reading file...")

    with open(file_path, "r") as file:
        lines = file.readlines()

    print(f"Writing file...")
    with open(output_path, "w") as file:
        for line in lines:
            file.write(line)

    print("Done!")


def main():
    print("\n\n-----------------------------------")
    print("\nPython Single Threaded Script")
    print("\n-----------------------------------\n\n")

    base_path = sys.argv[1] if len(sys.argv) > 1 else "../"
    input_file = sys.argv[2] if len(sys.argv) > 2 else "biggerSample.txt"
    file_path = os.path.join(base_path, input_file)
    output_file = os.path.join(base_path, "data", "outputPython.txt")

    readWriteFile(file_path, output_file)


if __name__ == "__main__":
    main()
