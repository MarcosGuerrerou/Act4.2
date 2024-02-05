"""
Module to compute statistics from a file given as a Command Line argument.
"""
import sys
import time

def read_data(file_name: str) -> list:
    """
    Load a list of all numbers in a file.
    """
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = float(line.strip())
                data.append(number)
            except ValueError as e:
                print(f"Error parsing line '{line.strip()}': {e}")
    return data

def calculate_mean(data: list) -> float:
    """
    Calculate the mean of a list of numbers.
    """
    return sum(data) / len(data) if data else 0

def calculate_median(data: list) -> float:
    """
    Calculate the median of a list of numbers.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n//2]
    else:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    return median

def calculate_mode(data: list) -> list:
    """
    Calculate the mode of a list of numbers.
    """
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def calculate_variance(data: list, mean: float) -> float:
    """
    Calculate the variance of a list of numbers.
    """
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1) if len(data) > 1 else 0

def calculate_std_dev(variance: float) -> float:
    """
    Calculate the standard deviation from the variance
    """
    return variance ** 0.5

def write_results(results: dict, file_name: str) -> None:
    """
    Write the results to a file.
    """
    with open(file_name, 'a', encoding='utf-8') as file:
        for key, value in results.items():
            print(f"{key}: {value}")
            file.write(f"{key}: {value}\n")

def main():
    """
    Main function to compute statistics from a file.
    """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_data(file_name)

    if not data:
        print("No valid data to process.")
        sys.exit(1)

    start_time = time.time()
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(variance)
    elapsed_time = time.time() - start_time

    results = {
        "Filename": file_name,
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Standard Deviation": std_dev,
        "Variance": variance,
        "Execution Time": f"{elapsed_time:.2f} seconds"
    }

    write_results(results, "StatisticsResults.txt")

if __name__ == "__main__":
    main()
