from day_2_part_1 import read_and_parse_input_file
import time

def is_safe(report):
    """Check if the report is safe
    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is safe, False otherwise
    """
    if all(b - a > 0 for a, b in zip(report, report[1:])) or all(b - a < 0 for a, b in zip(report, report[1:])):
        return all(1 <= abs(b - a) <= 3 for a, b in zip(report, report[1:]))
    return False

def is_report_safe_with_dampener(report):
    """Check if a report is safe, considering the Problem Dampener
    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is safe, False otherwise
    """
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports(data):
    """Count the number of safe reports
    Args:
        data (list): list of reports (lists of integers)
    Returns:
        int: number of safe reports
    """
    safe_count = sum(is_report_safe_with_dampener(report) for report in data)
    return safe_count

def main(file_path):
    data = read_and_parse_input_file(file_path)
    safe_count = count_safe_reports(data)
    print(safe_count)

if __name__ == '__main__':
    start_time = time.time()
    file_path = "day_2/input/input.txt"
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")