import lorem
import os

def write_to_file(file_path, data, num_lines):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            file.write(data + '\n')


def generate_large_file(file_path, data, num_lines):
    print(f"Generating a large file: {file_path}")
    write_to_file(file_path, data, num_lines)
    print("File generation complete.")
    

if __name__ == "__main__":
    data_dict = './data'
    
    dict = [
        {
            "file_path": "huge_file.txt",
            "data": lorem.paragraph(),
            "num_lines": 10000000
        },
        {
            "file_path": "large_file.txt",
            "data": lorem.paragraph(),
            "num_lines": 1000000
        },
        {
            "file_path": "medium_file.txt",
            "data": lorem.paragraph(),
            "num_lines": 500000
        },
        {
            "file_path": "small_file.txt",
            "data": lorem.paragraph(),
            "num_lines": 100000
        }
    ]
    for file in dict:
        file_path = os.path.join(data_dict, file['file_path'])
        data = file['data']
        num_lines = file['num_lines']
        generate_large_file(file_path, data, num_lines)