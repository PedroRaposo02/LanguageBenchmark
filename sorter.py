def parse_line(line):
    """Parse a single line into a dictionary."""

    # Extract the text from the parts
    parts = " ".join(line.split("|")[1:]).strip().split()

    if len(parts) < 7:  # Adjust based on the number of columns
        return None  # Skips malformed lines
    return {
        "Linguagem": parts[0],
        "Script": parts[1],
        "Input File": parts[2],
        "Error Code": parts[3],
        "Tempo de Execucao (s)": parts[4],
        "Tempo de Leitura (ms)": parts[5],
        "Tempo de Escrita (ms)": parts[6],
    }


def read_and_sort_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)  # Skip header line
        for line in file:
            parsed_line = parse_line(line)
            if parsed_line:
                data.append(parsed_line)
    # Sort data by 'Linguagem'
    sorted_data = sorted(data, key=lambda x: x["Linguagem"])
    return sorted_data


def write_sorted_data(filename, sorted_data):
    with open(filename, "w", encoding="utf-8") as file:
        # Writing the formatted header
        header_format = "{language:<20}{script_name:<30}{input_file:<20}{err_code:<15}{execution_time:<25}{reading_time:<25}{writing_time:<25}\n"
        file.write(
            header_format.format(
                language="| Linguagem",
                script_name="| Script",
                input_file="| Input File",
                err_code="| Error Code",
                execution_time="| Tempo de Execucao (s)",
                reading_time="| Tempo de Leitura (ms)",
                writing_time="| Tempo de Escrita (ms)",
            )
        )

        # Writing each entry in sorted_data with the same format
        for entry in sorted_data:
            file.write(
                header_format.format(
                    language=f"| {entry['Linguagem']}",
                    script_name=f"| {entry['Script']}",
                    input_file=f"| {entry['Input File']}",
                    err_code=f"| {entry['Error Code']}",
                    execution_time=f"| {entry['Tempo de Execucao (s)']}",
                    reading_time=f"| {entry['Tempo de Leitura (ms)']}",
                    writing_time=f"| {entry['Tempo de Escrita (ms)']}",
                )
            )


if __name__ == "__main__":
    filename = "data/results.txt"
    output_filename = "data/sorted_results.txt"
    sorted_data = read_and_sort_data(filename)
    write_sorted_data(output_filename, sorted_data)