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

def find_word_occurrences(grid, word):
    """Find all occurrences of a word in the grid
    Args:
        grid (list of str): the word search grid
        word (str): the word to find
    Returns:
        int: the total number of occurrences of the word
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    def is_valid(x, y):
        """Check if the coordinates are valid
        Args:
            x (int): row index
            y (int): column index
        Returns:
            bool: True if the coordinates are valid, False otherwise
        """
        return 0 <= x < rows and 0 <= y < cols
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                x, y = i, j
                match = True
                for k in range(word_len):
                    if not is_valid(x, y) or grid[x][y] != word[k]:
                        match = False
                        break
                    x += dx
                    y += dy
                if match:
                    count += 1
    return count

def main(file_path):
    data = read_input_file(file_path)
    word = "XMAS"
    total_occurrences = find_word_occurrences(data, word)
    print(total_occurrences)

if __name__ == '__main__':
    file_path = "day_4/input/input.txt"
    start_time = time.time()
    main(file_path)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")
