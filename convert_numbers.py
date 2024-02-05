"""
Module to convert numbers from a file given as a Command Line argument.
"""
import sys
import time

def read_data(file_name: str) -> list[int]:
    """Read numbers from a file and return them as a list of integers."""
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = int(line.strip())
                data.append(number)
            except ValueError as e:
                print(f"Error parsing line '{line.strip()}': {e}")
    return data

def to_binary(number: int) -> str:
    """Convert a number to its binary representation using basic algorithms."""
    if number == 0:
        binary = "0"
    elif number > 0:
        binary = ""
        while number > 0:
            binary = str(number % 2) + binary
            number = number // 2
    else:
        abs_binary = to_binary(abs(number))
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in abs_binary)
        binary_list = list(inverted_binary)
        length = len(binary_list)
        carry = 1
        for i in range(length - 1, -1, -1):
            if binary_list[i] == '1' and carry == 1:
                binary_list[i] = '0'
                carry = 1
            else:
                binary_list[i] = str(int(binary_list[i]) + carry)
                carry = 0
                break
        if carry == 1:
            binary_list.insert(0, '1')
        binary = ''.join(binary_list)
    return binary

def to_hexadecimal(number: int) -> str:
    """Convert a number to its hexadecimal representation. """
    hex_chars = "0123456789ABCDEF"
    if number == 0:
        return "0"
    hexadecimal = ""
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal

def write_results(data: list[int], file_name: str):
    """Write the conversion results to both the console and a file."""
    with open(file_name, 'a', encoding='utf-8') as file:
        for number in data:
            binary = to_binary(number)
            hexadecimal = to_hexadecimal(number)
            result = f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}\n"
            print(result, end='')
            file.write(result)

def main():
    """The main function to execute the conversion program."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_data(file_name)

    start_time = time.time()
    write_results(data, "ConversionResults.txt")
    elapsed_time = time.time() - start_time

    print(f"Execution Time: {elapsed_time:.2f} seconds")
    with open("ConversionResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"Execution Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
