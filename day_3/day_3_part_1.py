import time
import re

def read_input_file(file_path):
    """Read the input data
    Args:
        file_path (str): path to the input file
    Returns:
        data (list): list of strings
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    data = [line.strip() for line in lines if line.strip()]
    return data

def delete_invalid_chars(data):
    """Keep only the valid mul instructions
    Args:
        data (list): list of strings
    Returns:
        valid_instructions (list): list of strings
    """
    valid_instructions = []
    for line in data:
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        valid_instructions.extend(matches)
    return valid_instructions

def calculate_result(instruction):
    """Calculate the result of a valid mul instruction
    Args:
        instruction (str): string representing a valid mul instruction
    Returns:
        int: result of the instruction
    """
    a, b = map(int, instruction[4:-1].split(','))
    return a * b

def sum_results(instructions):
    """Sum all the results and return the final result
    Args:
        instructions (list): list of strings representing valid mul instructions
    Returns:
        int: final result
    """
    results = [calculate_result(instruction) for instruction in instructions]
    return sum(results)

def main(file_path):
    data = read_input_file(file_path)
    valid_instructions = delete_invalid_chars(data)
    final_result = sum_results(valid_instructions)
    print(final_result)

if __name__ == '__main__':
    file_path = "day_3/input/input.txt"
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")

