from concurrent.futures import ProcessPoolExecutor
import time

def read_and_parse_input_file(file_path):
    """Read and parse the input data
    Args:
        file_path (str): path to the input file
    Returns:
        processed_data (list): list of reports (lists of integers)
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    processed_data = [list(map(int, line.split())) for line in lines if line.strip()]
    return processed_data

def is_consistent(report):
    """Check if the report is consistent.

    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is consistent, False otherwise
    """
    increasing = all(b > a for a, b in zip(report, report[1:]))
    decreasing = all(b < a for a, b in zip(report, report[1:]))
    
    if not (increasing or decreasing):
        return False
    return all(1 <= abs(b - a) <= 3 for a, b in zip(report, report[1:]))

def is_report_safe_with_dampener(report):
    """Check if a report is safe, considering the Problem Dampener.

    Args:
        report (list): list of integers representing levels
    Returns:
        bool: True if the report is safe, False otherwise
    """
    if is_consistent(report):
        return True

    for i in range(len(report)):
        if is_consistent(report[:i] + report[i+1:]):
            return True

    return False

# Refactored processing logic : added parallel processing
def process_reports_chunk(reports_chunk):
    """Process a chunk of reports and count the number of safe reports.

    Args:
        reports_chunk (list): chunk of reports (lists of integers)
    Returns:
        int: number of safe reports in the chunk
    """
    return sum(is_report_safe_with_dampener(report) for report in reports_chunk)

def count_safe_reports_parallel(data, chunk_size=100):
    """Count the number of safe reports in parallel.

    Args:
        data (list): list of reports (lists of integers)
        chunk_size (int): size of the chunks to process in parallel

    Returns:
        int: number of safe reports
    """
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    safe_count = 0

    with ProcessPoolExecutor() as executor:
        results = executor.map(process_reports_chunk, chunks)
        safe_count = sum(results)

    return safe_count

def main(file_path):
    data = read_and_parse_input_file(file_path)
    safe_count = count_safe_reports_parallel(data)
    print(safe_count)

if __name__ == '__main__':
    import time
    file_path = "day_2/input/input.txt"
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4} seconds")
