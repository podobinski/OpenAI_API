input_file_path = 'input.txt'
output_file_path = 'output.txt'

replacement_string = ' '

with open(input_file_path, 'r') as file:
    file_contents = file.read()

modified_contents = file_contents.replace('\n', replacement_string)

with open(output_file_path, 'w') as file:
    file.write(modified_contents)

print("End-of-line replacement complete. Output written to", output_file_path)
