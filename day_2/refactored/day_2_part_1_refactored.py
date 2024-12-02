import time

# Refactored read_and_parse_input_file function : simplified input parsing
def read_and_parse_input_file(file_path):
    """Read and parse the input data
    Args:
        file_path (str): path to the input file
    Returns:
        processed_data (list): list of reports (lists of integers)
    """
    with open(file_path, 'r') as f:
        return [list(map(int, line.split())) for line in f if line.strip()]

# Refactored is_report_safe function : consolidated the logic and added early return
def is_report_safe(report):
    """Check if a single report is safe (increasing or decreasing by 1 or more and 3 or less)
    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is safe, False otherwise
    """
    increasing = True
    decreasing = True
    for a, b in zip(report, report[1:]):
        diff = b - a
        if not (1 <= abs(diff) <= 3):
            return False
        if diff < 0:
            increasing = False
        if diff > 0:
            decreasing = False
        if not (increasing or decreasing):
            return False
    return True

# Refactored count_safe_reports function : replaced explicit loop with sum
def count_safe_reports(data):
    """Count the number of safe reports
    Args:
        data (list): list of reports (lists of integers)
    Returns:
        int: number of safe reports
    """
    return sum(is_report_safe(report) for report in data)

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
