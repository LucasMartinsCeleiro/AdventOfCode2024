import time

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

def find_x_mas_occurrences(grid):
    """Find all occurrences of X-MAS in the grid
    Args:
        grid (list of str): the word search grid
    Returns:
        int: the total number of X-MAS patterns
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid_diagonal(c1, c2, c3):
        return (c1 + c2 + c3 == "MAS") or (c1 + c2 + c3 == "SAM")

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'A':
                if is_valid_diagonal(grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]):
                    if is_valid_diagonal(grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]):
                        count += 1

    return count

def main(file_path):
    data = read_input_file(file_path)
    total_occurrences = find_x_mas_occurrences(data)
    print(f"Total X-MAS patterns: {total_occurrences}")

if __name__ == '__main__':
    file_path = "day_4/input/input.txt"
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")
