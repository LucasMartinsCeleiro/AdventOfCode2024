from day_1_part_1 import separate_input_file

def count_occurrences(list_2):
    """Count the number of occurrences of each number in the right list
    Args:
        list_2 (list): list of numbers in the second column
    Returns:
        occurrences (dict): dictionary of number of occurrences of each number
    """
    occurrences = {}
    for num in list_2:
        occurrences[num] = occurrences.get(num, 0) + 1
    return occurrences

def calculate_similarity_score(list_1, list_2):
    """For each number in the left list, multiply it by the number of occurrences in the right list
    Args:
        list_1 (list): list of numbers in the first column
        list_2 (list): list of numbers in the second column
    Returns:
        similarity_score (int): sum of all the results
    """
    
    occurrences = count_occurrences(list_2)
    similarity_score = 0
    for num in list_1:
        similarity_score += num * occurrences.get(num, 0)
    return similarity_score

def main(file_path):
    list_1, list_2 = separate_input_file(file_path)
    score = calculate_similarity_score(list_1, list_2)
    print(score)

file_path = "day_1/input/input.txt"
main(file_path)


