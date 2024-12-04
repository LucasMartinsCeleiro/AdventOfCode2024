import re
import time

def read_input_file(file_path):
    """Read the input data
    Args:
        file_path (str): path to the input file
    Returns:
        str: the entire content as a single string
    """
    with open(file_path, 'r') as f:
        content = f.read()
    return content.replace("\n", "").strip()

def parse_instructions(content):
    """Parse the instructions from the content
    Args:
        content (str): string containing the instructions
    Returns:
        regex iterator
    """
    regex = re.compile(r"do(?:n't)?\(\)|mul\((\d+),(\d+)\)")
    return regex.finditer(content)

def process_input(content):
    """Process the instructions and return the final result
    Args:
        content (str): string containing the instructions
    Returns:
        int: final result
    """
    instructions = parse_instructions(content)
    total_sum = 0
    enabled = True

    for match in instructions:
        instruction = match.group(0)

        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul(") and enabled:
            t1, t2 = int(match.group(1)), int(match.group(2))
            total_sum += t1 * t2

    return total_sum

def main(file_path):
    content = read_input_file(file_path)
    result = process_input(content)
    print(result)

if __name__ == '__main__':
    file_path = 'day_3/input/input.txt'
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")
