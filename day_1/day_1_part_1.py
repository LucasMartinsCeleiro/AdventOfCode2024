#Advent of Code 2024 - Day 1 : Part 1

# Step to solve the problem

# Step 1 : Separate the two columns of numbers into two separate lists
# Step 2 : Sort the two lists in ascending order
# Step 3 : Pair up the numbers from the two lists
# Step 4 : Calculate the distance between each pair
# Step 5 : Sum all the distances


def separate_input_file(file_path):
    """Separate the two columns of numbers into two separate lists
    Args:
        file_name (str): path to the input file
    Returns:
        list_1 (list): list of numbers in the first column
        list_2 (list): list of numbers in the second column
    """
    with open(file_path) as f:
        lines = f.readlines() 
    lines = [x.strip() for x in lines]
    list_1 = [int(x.split()[0]) for x in lines]
    list_2 = [int(x.split()[1]) for x in lines]
    return list_1, list_2

def sort_list_asc(list_1, list_2):
    """Sort the two lists in ascending order
    Args:
        list_1 (list): list of numbers in the first column
        list_2 (list): list of numbers in the second column
    Returns:
        list_1 (list): list of numbers in the first column sorted in ascending order
        list_2 (list): list of numbers in the second column sorted in ascending order
    """
    list_1.sort()
    list_2.sort()
    return list_1, list_2

def pair_up_numbers(list_1, list_2):
    """Pair up the numbers from the two lists
    Args:
        list_1 (list): list of numbers in the first column
        list_2 (list): list of numbers in the second column
    Returns:
        pairs (list): list of pairs of numbers
    """
    pairs = list(zip(list_1, list_2))
    return pairs

def calculate_distance(pairs):
    """Calculate the distance between each pair
    Args:
        pairs (list): list of pairs of numbers
    Returns:
        distances (list): list of distances between each pair
    """
    distances = [abs(x[0] - x[1]) for x in pairs]
    return distances

def main(file_path):
    list_1, list_2 = separate_input_file(file_path)
    list_1, list_2 = sort_list_asc(list_1, list_2)
    pairs = pair_up_numbers(list_1, list_2)
    distances = calculate_distance(pairs)
    print(sum(distances))
    
file_path = "day_1/input/input.txt"
main(file_path)