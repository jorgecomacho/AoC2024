import itertools
import time, os

def evaluate_left_to_right(numbers, ops):
    """Evaluates an expression left-to-right given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def evaluate_with_concat(numbers, ops):
    """Evaluates an expression left-to-right with +, *, and || operators."""
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            # Concatenate the numbers
            result = int(str(result) + str(numbers[i + 1]))
    return result

def parse_input(file_path):
    """Parses the input file into a list of test cases."""
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, file_path])
    test_cases = []
    with open(full_path, 'r') as file:
        for line in file:
            if ':' not in line:
                continue
            target, numbers = line.strip().split(':')
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            test_cases.append((target, numbers))
    return test_cases

def solve_part_one(test_cases):
    """Solves Part 1 using only + and * operators."""
    valid_test_values = []
    operators = ['+', '*']
    for target, numbers in test_cases:
        possible = False
        for ops in itertools.product(operators, repeat=len(numbers) - 1):
            if evaluate_left_to_right(numbers, ops) == target:
                possible = True
                break
        if possible:
            valid_test_values.append(target)
    return sum(valid_test_values)

def solve_part_two(test_cases):
    """Solves Part 2 using +, *, and || operators."""
    valid_test_values = []
    operators = ['+', '*', '||']
    for target, numbers in test_cases:
        possible = False
        for ops in itertools.product(operators, repeat=len(numbers) - 1):
            if evaluate_with_concat(numbers, ops) == target:
                possible = True
                break
        if possible:
            valid_test_values.append(target)
    return sum(valid_test_values)

if __name__ == "__main__":
    # Update file_path with the input file location
    file_path = "day07.txt"  # Change this to your actual input file

    # Parse the input
    test_cases = parse_input(file_path)

    # Solve Part 1
    print("Starting part 001...")
    start_time = time.time()
    part_one_result = solve_part_one(test_cases)
    part_one_time = time.time() - start_time
    print(f"Part 1 finished in {part_one_time:,.9f} s")
    print(f"Part 1 Total Calibration Result: {part_one_result}")

    # Solve Part 2
    print("Starting part 002...")
    part_two_start_time = time.time()
    part_two_result = solve_part_two(test_cases)
    part_two_time = time.time() - part_two_start_time
    cumulative_time = part_one_time + part_two_time
    print(f"Part 2 finished in {part_two_time:,.9f} s, cumulative time {cumulative_time:,.9f} s")
    print(f"Part 2 Total Calibration Result: {part_two_result}")