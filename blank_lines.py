def count_blank_lines(file_path):
    blank_line_count = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Strip the line of leading and trailing whitespace and check if it is empty
            if line.strip() == "":
                blank_line_count += 1

    return blank_line_count

# Example usage
file_path = '/nlsasfs/home/nltm-pilot/malavika/Sowmithaa/espnet/egs2/librispeech_100/asr2/data/valid/text'  # Replace with the actual file path
blank_lines = count_blank_lines(file_path)
print(f"The number of blank lines in the file is: {blank_lines}")
