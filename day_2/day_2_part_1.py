import time

# Advent of Code 2024 - Day 2 : Part 1

# Step to solve the problem

# 1. Step 1 : Read and parse the input data
# 2. Step 2 : Check if the levels are increasing or decreasing
# 3. Step 3 : Check if the levels are increasing or decreasing by 1 or more and 3 or less
# 4. Step 4 : Count and return the number of safe reports

def read_and_parse_input_file(file_path):
    """Read and parse the input data
    Args:
        file_path (str): path to the input file
    Returns:
        processed_data (list): list of integers
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    processed_data = [list(map(int, line.split())) for line in lines if line.strip()]
    return processed_data
    
def is_report_safe(report):
    """Check if a single report is safe (increasing or decreasing by 1 or more and 3 or less)
    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is safe, False otherwise
    """
    if not (all(b - a > 0 for a, b in zip(report, report[1:])) or
        all(b - a < 0 for a, b in zip(report, report[1:]))):
        return False

    for a, b in zip(report, report[1:]):
        if not (1 <= abs(b - a) <= 3):
            return False

    return True

def count_safe_reports(data):
    """Count the number of safe reports
    Args:
        data (list): list of reports (lists of integers)
    Returns:
        int: number of safe reports
    """
    safe_count = sum(is_report_safe(report) for report in data)
    return safe_count

    
def main(file_path):
    data = read_and_parse_input_file(file_path)
    safe_count = count_safe_reports(data)
    print(safe_count)

if __name__ == '__main__':
    file_path = "day_2/input/input.txt"
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")