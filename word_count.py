"""
Module that counts appearances of words in a file given as a Command Line argument.
"""
import sys
import time

def read_words(file_name: str) -> list[str]:
    """ Read words from a file, assuming words are separated by spaces."""
    words = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words.extend(line.strip().split())
    return words

def count_words(words: list[str]) -> dict[str, int]:
    """Count the frequency of each distinct word in the list."""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_results(word_count: dict[str, int], file_name: str):
    """Write the word counts to both the console and a file."""
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write('\n')
        for word, count in word_count.items():
            result = f"{word}: {count}\n"
            print(result, end='')
            file.write(result)

def main():
    """The main function to execute the word count program."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    file_name = sys.argv[1]
    start_time = time.time()
    words = read_words(file_name)
    word_count = count_words(words)
    write_results(word_count, "WordCountResults.txt")
    elapsed_time = time.time() - start_time
    print(f"Execution Time: {elapsed_time:.2f} seconds")
    with open("WordCountResults.txt", 'a', encoding='utf-8') as file:
        file.write(f"Execution Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
